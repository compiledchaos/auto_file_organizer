import json
import sys
from pathlib import Path
from organizer.core import FileOrganizer
from organizer.utils.data import history
from organizer.logger_code import get_logger
from organizer.utils.data import rules_func
from organizer.file_watcher import activate_watchdog
from organizer.cli import parse_args
from organizer.app import run_gui

x = rules_func()


def cli(args):
    """
    Command Line Interface function for the file organizer.

    Args:
        args: Parsed command line arguments which include options for
              source directory, rules file, simulation mode, reset, undo, and logging.

    This function initializes the logger, parses the source and rules,
    and creates a FileOrganizer instance. It then performs the organization
    of files based on the specified rules, with options to undo the last
    operation or reset the history. Errors during processing are logged
    and the application exits with a non-zero status code on failure.
    """

    log = get_logger(log_to_file=bool(args.logfile), log_file=args.logfile)

    source = args.source or str(Path.home() / "Downloads")
    rules_path = args.rules
    data = history()
    simulate = args.simulate
    reset = args.reset
    if args.rules is not None:
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
        log.info(f"Starting file organization in directory: {source}")
        organizer = FileOrganizer(source, rules, data, simulate, logger=log)
        organizer.organize()
        if args.undo:
            organizer.undo()
        if reset:
            organizer.reset()
        log.info("File organization completed successfully")
    except Exception as e:
        log.error(f"Error during organization: {e}")
        sys.exit(1)


def entry():
    """
    Entry point for the file organizer application.

    This function parses command line arguments and handles different modes of operation:
    - GUI mode: Launches the graphical user interface for file organization.
    - Watchdog mode: Activates the file watcher to monitor and organize files in real-time.
    - CLI mode: Performs file organization based on command line arguments.

    Args:
        None

    Returns:
        None

    Raises:
        SystemExit: If an error occurs during argument parsing or execution.
    """
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
