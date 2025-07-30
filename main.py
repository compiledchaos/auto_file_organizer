import sys
from args import parse_args
from organizer.logger_code import get_logger
from organizer.app import run_gui
from commands import cli
from file_watcher import activate_watchdog

if __name__ == "__main__":
    args = parse_args()
    log = get_logger(log_to_file=bool(args.logfile), log_file=args.logfile)

    try:
        if args.gui:
            run_gui()
        elif args.watchdog:
            activate_watchdog()
        else:
            cli()  # cli() will re-parse args again, this is fine if you prefer separation
    except Exception as e:
        log.critical(f"Fatal error: {e}")
        sys.exit(1)
