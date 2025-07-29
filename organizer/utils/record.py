from datetime import datetime
import json
import os


def record_move(original_path, new_path, simulate=False, undo_file="undo.json"):
    move = {
        "original_path": str(original_path),
        "new_path": str(new_path),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    try:
        if os.path.exists(undo_file):
            with open(undo_file, "r") as f:
                try:
                    data = json.load(f)
                    if not isinstance(data, list):
                        data = []
                except json.JSONDecodeError:
                    data = []
        else:
            data = []
    except Exception as e:
        print(f"Error reading undo file '{undo_file}': {e}")
        data = []

    data.append(move)
    if not simulate:
        try:
            with open(undo_file, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error writing to undo file '{undo_file}': {e}")
    else:
        print(data)


def update(data, undo_file="undo.json"):
    try:
        with open(undo_file, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error updating undo file '{undo_file}': {e}")


def reset(undo_file="undo.json"):
    try:
        with open(undo_file, "w") as f:
            json.dump([], f, indent=2)
    except Exception as e:
        print(f"Error resetting undo file '{undo_file}': {e}")
