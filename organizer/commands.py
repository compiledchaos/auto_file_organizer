import json
import sys
from pathlib import Path
from organizer.core import FileOrganizer
from organizer.utils.data import history
from organizer.logger_code import get_logger
from organizer.utils.data import rules
from organizer.file_watcher import activate_watchdog
from organizer.cli import parse_args
from organizer.app import run_gui

x = rules


def cli(args):

    log = get_logger(log_to_file=bool(args.logfile), log_file=args.logfile)

    source = args.source or str(Path.home() / "Downloads")
    rules_path = args.rules
    data = history()
    simulate = args.simulate
    reset = args.reset
    if args.rules is str:
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
    else:
        rules = x
    try:
        organizer = FileOrganizer(source, rules, data, simulate, logger=log)
        organizer.organize()
        if args.undo:
            organizer.undo()
        if reset:
            organizer.reset()
    except Exception as e:
        log.error(f"Error during organization: {e}")
        sys.exit(1)


def entry():
    args = parse_args()
    log = get_logger(log_to_file=bool(args.logfile), log_file=args.logfile)

    try:
        if args.gui:
            log.info("Launching GUI")
            run_gui(args)
        elif args.watchdog:
            activate_watchdog(args)
        else:
            cli(args)
    except Exception as e:
        log.critical(f"Fatal error: {e}")
        sys.exit(1)
