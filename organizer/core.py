from pathlib import Path
from organizer.utils import record_move, update, reset


class FileOrganizer:
    def __init__(self, source_folder, rules, history):
        self.source = Path(source_folder)
        self.rules = rules
        self.files = [x for x in self.source.iterdir() if x.is_file()]
        self.history = history

    def organize(self):
        for dir in self.rules.values():
            Path(self.source / dir).mkdir(parents=True, exist_ok=True)
        for x in self.files:
            for a, b in self.rules.items():
                if Path(x).suffix == a:
                    dest = Path(self.source) / b / Path(x).name
                    Path(x).rename(dest)
                    record_move(x, dest)

    def undo(self):
        self.last_move = self.history.pop()
        orig = Path(self.last_move["original_path"])
        new = Path(self.last_move["new_path"])
        backup = orig.with_name(orig.stem + "_backup" + orig.suffix)

        if orig.exists():
            # Backup the existing file before replacing
            orig.rename(backup)
        new.rename(orig)
        update(self.history)

    def reset(self):
        reset()
