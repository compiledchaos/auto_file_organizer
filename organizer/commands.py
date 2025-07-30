import json
import sys
from pathlib import Path
from organizer.core import FileOrganizer
from organizer.utils.data import history
from organizer.logger_code import get_logger
from organizer.args import parse_args  # <- not args!


def cli():
    args = parse_args()  # <- moved inside the function

    log = get_logger(log_to_file=bool(args.logfile), log_file=args.logfile)

    source = args.source or str(Path.home() / "Downloads")
    rules_path = args.rules
    data = history
    simulate = args.simulate
    reset = args.reset

    try:
        with open(rules_path) as f:
            rules = json.load(f)
            if not isinstance(rules, dict):
                log.error(f"Rules file '{rules_path}' is not a valid JSON object.")
                sys.exit(1)
    except FileNotFoundError:
        log.warning(f"Rules file '{rules_path}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        log.error(f"Error decoding JSON from rules file '{rules_path}': {e}")
        sys.exit(1)
    except Exception as e:
        log.error(f"Unexpected error reading rules file '{rules_path}': {e}")
        sys.exit(1)

    try:
        organizer = FileOrganizer(source, rules, data, simulate, logger=log)
        if args.undo:
            organizer.undo()
        if reset:
            organizer.reset()
        organizer.organize()
    except Exception as e:
        log.error(f"Error during organization: {e}")
        sys.exit(1)
