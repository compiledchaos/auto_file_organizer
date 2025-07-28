from datetime import datetime
import json


def record_move(original_path, new_path, undo_file="undo.json"):
    move = {
        "original_path": str(original_path),
        "new_path": str(new_path),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    try:
        with open(undo_file, "r") as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(move)

    with open(undo_file, "w") as f:
        json.dump(data, f, indent=2)


def update(data, undo_file="undo.json"):
    with open(undo_file, "w") as f:
        json.dump(data, f, indent=2)


def reset(undo_file="undo.json"):
    with open(undo_file, "w") as f:
        json.dump([], f, indent=2)
