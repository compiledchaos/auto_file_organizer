from datetime import datetime
import json
from organizer.logger_code import get_logger
from organizer.utils.data import UNDO_PATH


def record_move(original_path, new_path, simulate=False, logfile=None):
    if logfile:
        log = get_logger(log_to_file=True, log_file=logfile)
    else:
        log = get_logger()

    move = {
        "original_path": str(original_path),
        "new_path": str(new_path),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    try:
        if UNDO_PATH.exists():
            with open(UNDO_PATH, "r") as f:
                try:
                    data = json.load(f)
                    if not isinstance(data, list):
                        data = []
                        log.warning("isinstance error")
                except json.JSONDecodeError:
                    log.warning("JSONDecodeError")
                    data = []
        else:
            data = []
            log.warning("Undo file not found")
    except Exception as e:
        log.error(f"Error reading undo file '{UNDO_PATH}': {e}")
        data = []

    data.append(move)

    if not simulate:
        try:
            with open(UNDO_PATH, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            log.error(f"Error writing to undo file '{UNDO_PATH}': {e}")
    else:
        log.info(data)


def update(data, logfile=None):
    log = get_logger(log_to_file=True, log_file=logfile) if logfile else get_logger()
    try:
        with open(UNDO_PATH, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        log.error(f"Error updating undo file '{UNDO_PATH}': {e}")


def reset(logfile=None):
    log = get_logger(log_to_file=True, log_file=logfile) if logfile else get_logger()
    try:
        with open(UNDO_PATH, "w") as f:
            json.dump([], f, indent=2)
    except Exception as e:
        log.error(f"Error resetting undo file '{UNDO_PATH}': {e}")
