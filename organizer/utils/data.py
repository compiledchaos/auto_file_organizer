import json
from pathlib import Path
from organizer.logger_code import get_logger

RULES_PATH = Path.home() / ".auto_file_organizer" / "rules.json"
UNDO_PATH = Path.home() / ".auto_file_organizer" / "undo.json"

UNDO_PATH.parent.mkdir(parents=True, exist_ok=True)


log = get_logger()


def rules_func():
    """
    Returns a dictionary of rules that map file extensions to folder names.

    If the rules file at `~/.auto_file_organizer/rules.json` does not exist,
    it generates a default rules file with the following rules:

    {
        ".jpg": "Images",
        ".pdf": "Pdfs/Epubs",
        ".png": "Images",
        ".txt": "Documents",
        ".zip": "Archives",
        ".exe": "Application",
        ".xlsx": "Excel",
        ".epub": "Pdfs/Epubs",
        ".csv": "Excel",
        ".docx": "Documents",
        ".py": "Python",
        ".ipynb": "Python",
        ".jar": "Jar_Files",
        ".mp4": "Videos",
    }

    The generated rules file is written to `~/.auto_file_organizer/rules.json`.
    """

    if RULES_PATH.exists():
        with open(RULES_PATH, "r") as f:
            rules = json.load(f)
    else:
        rules = {
            ".txt": "Documents",
            ".pdf": "Documents",
            ".doc": "Documents",
            ".docx": "Documents",
            ".jpg": "Images",
            ".jpeg": "Images",
            ".png": "Images",
            ".gif": "Images",
            ".mp4": "Videos",
            ".avi": "Videos",
            ".mov": "Videos",
            ".zip": "Archives",
            ".rar": "Archives",
            ".7z": "Archives",
        }
        with open(RULES_PATH, "w") as w:
            json.dump(rules, w)
        log.info(f"Rules file not found, generated default rules at {RULES_PATH}")
    return rules


def history(args=None):
    """
    Returns the stored history from the undo.json file.

    If the file does not exist, it creates a new empty file and returns an empty dict.
    If args is provided, it attempts to open the file at the given path and returns the
    loaded history.

    The history file is written to `~/.auto_file_organizer/undo.json`.
    """
    if UNDO_PATH.exists() and not args:
        with open(UNDO_PATH, "r") as w:
            return json.load(w)
    elif args:
        with open(args, "r") as w:
            return json.load(w)
    else:
        history = {}
        with open(UNDO_PATH, "w") as w:
            json.dump(history, w)
        log.info(f"History file not found, Genarated file. Found at {UNDO_PATH}")
        with open(UNDO_PATH, "r") as w:
            return json.load(w)
