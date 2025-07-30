from organizer.app import run_gui
from commands import cli, args
import sys
from file_watcher import activate_watchdog
from organizer.logger_code import get_logger

if args.logfile:
    log = get_logger(log_to_file=True, log_file=args.logfile)
else:
    log = get_logger()

if __name__ == "__main__":
    try:
        if args.gui:
            run_gui()
        else:
            if args.watchdog:
                activate_watchdog()
            cli()
    except Exception as e:
        log.critical(f"Fatal error: {e}")
        sys.exit(1)
