from pathlib import Path
from organizer.utils import record_move, update, reset


class FileOrganizer:

    def __init__(self, source_folder, rules, history, simulate=False, logger=None):
        self.source = Path(source_folder)
        self.rules = rules
        try:
            self.files = [x for x in self.source.iterdir() if x.is_file()]
        except Exception as e:
            self.files = []
            if logger:
                logger(f"Error reading source folder: {e}")
            else:
                print(f"Error reading source folder: {e}")
        self.history = history
        self.simulate = simulate
        self.log = logger or print

    def organize(self):
        if not self.simulate:
            for dir in self.rules.values():
                try:
                    Path(self.source / dir).mkdir(parents=True, exist_ok=True)
                except Exception as e:
                    self.log(f"Error creating directory '{dir}': {e}")
        for x in self.files:
            for a, b in self.rules.items():
                if Path(x).suffix == a:
                    dest = Path(self.source) / b / Path(x).name
                    try:
                        if not self.simulate:
                            Path(x).rename(dest)
                        record_move(x, dest, self.simulate)
                    except FileNotFoundError:
                        self.log(f"File not found: {x}")
                    except PermissionError:
                        self.log(f"Permission denied: {x}")
                    except Exception as e:
                        self.log(f"Error moving '{x}' to '{dest}': {e}")

    def undo(self):
        if not self.history:
            self.log("No history to undo.")
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
            update(self.history)
        except Exception as e:
            self.log(f"Error during undo: {e}")

    def reset(self):
        try:
            reset()
        except Exception as e:
            self.log(f"Error during reset: {e}")
