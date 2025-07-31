import argparse
from organizer.utils.data import rules


def parse_args():
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
        default=rules,
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

    return parser.parse_args()
