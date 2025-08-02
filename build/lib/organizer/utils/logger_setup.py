from organizer.logger_code import get_logger


def setup(args):
    """
    Sets up the logger based on the specified logging options.

    Args:
        args: Parsed command line arguments containing options for logging.

    The function initializes a logger based on the specified logging options. If a log file
    path is provided in args.logfile, it configures the logger to write logs to the specified
    file. Otherwise, it configures the logger to write logs to the console.
    """
    if args.logfile:
        log = get_logger(log_to_file=True, log_file=args.logfile)
    else:
        log = get_logger()

    return log
