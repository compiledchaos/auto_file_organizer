import json
from pathlib import Path

RULES_PATH = Path(__file__).parent.parent.parent / "rules.json"
UNDO_PATH = Path(__file__).parent.parent.parent / "undo.json"

with open(RULES_PATH, "r") as f:
    rules = json.load(f)


def history():
    with open(UNDO_PATH, "r") as w:
        history = json.load(w)
    return history
