from pathlib import Path
from organizer.utils import record_move, update, reset
import time
import logging


class FileOrganizer:

    def __init__(self, source_folder, rules, history, simulate=False, logger=None):
        self.source = Path(source_folder)
        self.rules = rules

        self.history = history
        self.simulate = simulate
        self.logger = logger or logging.getLogger(__name__)

    def organize(self):
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
                            record_move(x, dest, self.simulate, logfile=self.logger)
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
        try:
            reset(logfile=self.logger)
        except Exception as e:
            self.logger.error(f"Error during reset: {e}")
