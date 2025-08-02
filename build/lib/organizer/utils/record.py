from datetime import datetime
import json
from organizer.logger_code import get_logger
from organizer.utils.data import UNDO_PATH


def record_move(original_path, new_path, simulate=False, logger=None):
    """
    Records a file move operation in the undo history.

    Args:
        original_path: The original path of the file before the move.
        new_path: The new path of the file after the move.
        simulate: If True, the move is simulated and not actually performed.
        logger: Logger object for logging operations.

    The function records a file move operation in the undo history. If the undo file
    exists, it loads the existing history data. If the undo file does not exist, it
    creates a new empty history. The function then appends the move operation to the
    history and writes it back to the undo file. If simulate is True, the move is
    simulated and not actually performed.
    """
    if logger:
        log = logger
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
    """
    Updates the undo history with the specified data.

    Args:
        data: The data to be written to the undo file.
        logfile: Path to the log file for logging.

    The function updates the undo history with the specified data. If the undo file
    exists, it loads the existing history data. If the undo file does not exist, it
    creates a new empty history. The function then writes the specified data to the
    undo file.
    """
    log = get_logger(log_to_file=True, log_file=logfile) if logfile else get_logger()
    try:
        with open(UNDO_PATH, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        log.error(f"Error updating undo file '{UNDO_PATH}': {e}")


def reset(logfile=None):
    """
    Resets the undo history by deleting the undo file.

    Args:
        logfile: Path to the log file for logging.

    The function resets the undo history by deleting the undo file. If the undo file
    exists, it is deleted. If the undo file does not exist, the function does nothing.
    """
    log = get_logger(log_to_file=True, log_file=logfile) if logfile else get_logger()
    try:
        with open(UNDO_PATH, "w") as f:
            json.dump([], f, indent=2)
    except Exception as e:
        log.error(f"Error resetting undo file '{UNDO_PATH}': {e}")
