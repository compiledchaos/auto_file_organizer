import logging
from pathlib import Path


def get_logger(
    name: str = "file_organizer",
    log_to_file: bool = False,
    log_file: str = "organizer.log",
) -> logging.Logger:
    """
    Returns a logger instance with the specified name and configuration.

    Args:
        name: The name of the logger.
        log_to_file: If True, the logger will write logs to a file.
        log_file: The path to the log file.

    The function returns a logger instance with the specified name and configuration.
    If the logger already exists, it returns the existing logger instance. Otherwise,
    it creates a new logger instance with the specified name and configuration.
    """
    logger = logging.getLogger(name)

    # If logger already exists and we need file logging, check if file handler exists
    if logger.handlers:
        if log_to_file:
            # Check if file handler already exists
            has_file_handler = any(isinstance(h, logging.FileHandler) for h in logger.handlers)
            if not has_file_handler:
                # Add file handler to existing logger
                log_path = Path(log_file)
                log_path.parent.mkdir(parents=True, exist_ok=True)
                fh = logging.FileHandler(log_path, mode="a", encoding="utf-8")
                fh.setLevel(logging.DEBUG)
                formatter = logging.Formatter(
                    "[%(asctime)s] %(levelname)s: %(message)s %(funcName)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                )
                fh.setFormatter(formatter)
                logger.addHandler(fh)
        return logger

    logger.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s: %(message)s %(funcName)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File handler (optional)
    if log_to_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(log_path, mode="a", encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
