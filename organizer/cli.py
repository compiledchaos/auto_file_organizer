import argparse
from organizer.utils.data import rules_func


def parse_args():
    """
    Parses command-line arguments for the Auto File Organizer.

    Returns:
        argparse.Namespace: Parsed arguments including options for source directory,
        rules file, simulation mode, undo functionality, logging, reset, GUI mode, and watchdog.

    Options:
        --source: The source directory to organize. Default is the Downloads folder.
        --rules: Path to the JSON file containing file organization rules.
        --simulate: Show what would happen without actually moving files.
        --undo: Undo the last batch of file moves using undo.json.
        --logfile: Path to log file (enables file logging).
        --reset: Reset history before organizing new folder.
        --gui: Switch to GUI.
        --watchdog: Activates WatchDog.
    """
    parser = argparse.ArgumentParser(
        description="🗂️ Auto File Organizer — Clean up your messy folders with custom rules!"
    )

    parser.add_argument(
        "--source",
        type=str,
        required=False,
        help="The source directory to organize. Default is the Downloads folder.",
    )

    parser.add_argument(
        "--rules",
        type=str,
        default=None,
        help="Path to the JSON file containing file organization rules.",
    )

    parser.add_argument(
        "--simulate",
        action="store_true",
        help="Show what would happen without actually moving files.",
    )

    parser.add_argument(
        "--undo",
        action="store_true",
        help="Undo the last batch of file moves using undo.json",
    )

    parser.add_argument(
        "--logfile", type=str, help="Path to log file (enables file logging)."
    )

    parser.add_argument(
        "--reset",
        action="store_true",
        help="Reset history before organizing new folder",
    )

    parser.add_argument(
        "--gui",
        action="store_true",
        help="Swich to GUI",
    )

    parser.add_argument(
        "--watchdog",
        action="store_true",
        help="Activates WatchDog",
    )

    parser.add_argument(
        "--history",
        action="store_true",
        help="Path to history file (enables history logging).",
    )

    return parser.parse_args()
