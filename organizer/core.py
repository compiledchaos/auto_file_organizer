from pathlib import Path
from organizer.utils import record_move, update, reset
import time
import logging


class FileOrganizer:

    def __init__(self, source_folder, rules, history, simulate=False, logger=None):
        """
        Initializes a new instance of the FileOrganizer class.

        Args:
            source_folder: The source directory to organize.
            rules: The rules for organizing files.
            history: The history of file moves.
            simulate: Whether to simulate the organization process.
            logger: The logger to use for logging events.
        """
        self.source = Path(source_folder)
        self.rules = rules

        self.history = history
        self.simulate = simulate
        self.logger = logger or logging.getLogger(__name__)

    def organize(self):
        """
        Organizes all files in the source directory based on the rules.

        For each file in the source directory, it checks if the file extension matches
        one of the rules. If it does, it moves the file to the directory specified by
        the rule. If the directory does not exist, it is created.

        If the simulate flag is set, the file moves are only simulated and the files
        are not actually moved.

        If an error occurs during the move (e.g. permission denied), the error is
        logged and the move is retried up to 5 times. If the move fails after 5
        retries, the error is logged and the move is skipped.
        """
        files = [x for x in self.source.iterdir() if x.is_file()]
        if not self.simulate:
            for dir in self.rules.values():
                try:
                    Path(self.source / dir).mkdir(parents=True, exist_ok=True)
                except Exception as e:
                    self.logger.error(f"Error creating directory '{dir}': {e}")
        for x in files:
            for a, b in self.rules.items():
                if Path(x).suffix == a:
                    dest = Path(self.source) / b / Path(x).name
                    for attempt in range(5):  # Try up to 5 times
                        try:
                            if not self.simulate:
                                Path(x).rename(dest)
                            record_move(x, dest, self.simulate, logger=self.logger)
                            break  # Success, exit retry loop
                        except PermissionError:
                            if attempt < 4:
                                time.sleep(0.5)  # Wait half a second before retrying
                            else:
                                self.logger.error(
                                    f"Permission denied after retries: {x}"
                                )
                        except FileNotFoundError:
                            self.logger.error(f"File not found: {x}")
                            break
                        except Exception as e:
                            self.logger.error(f"Error moving '{x}' to '{dest}': {e}")
                            break

    def undo(self):
        """
        Reverts the last file move operation recorded in history.

        This function checks the history for the last file move, backs up the
        original file if it still exists, and then restores the file to its
        original location. If the history is empty, it logs an informational
        message. In case of any errors during the undo process, an error message
        is logged.
        """
        if not self.history:
            self.logger.info("No history to undo.")
            return
        try:
            self.last_move = self.history.pop()
            orig = Path(self.last_move["original_path"])
            new = Path(self.last_move["new_path"])
            backup = orig.with_name(orig.stem + "_backup" + orig.suffix)

            if orig.exists():
                # Backup the existing file before replacing
                orig.rename(backup)
            new.rename(orig)
            update(self.history, logfile=self.logger)
        except Exception as e:
            self.logger.error(f"Error during undo: {e}")

    def reset(self):
        """
        Resets the history of file moves.

        This function resets the history of file moves by removing all entries from
        the history file. If an error occurs during the reset process, an error
        message is logged.
        """
        try:
            reset(logfile=self.logger)
        except Exception as e:
            self.logger.error(f"Error during reset: {e}")
