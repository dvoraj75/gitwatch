import logging


def get_logger(log_fmt: str = None, log_level: int = logging.DEBUG, stream=None) -> logging.RootLogger:
    formatter = log_fmt or "%(asctime)s %(levelname)s: %(message)s"
    handler = logging.StreamHandler(stream)
    handler.setFormatter(logging.Formatter(formatter))
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(log_level)
    return logger
