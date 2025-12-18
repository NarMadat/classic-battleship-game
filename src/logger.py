import logging
import os

_logger_cache = {}

def setup_logger(name="battleship", log_file="outputs/game.log"):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

def get_logger(name="battleship", log_file="outputs/game.log"):
    cache_key = (name, log_file)
    if cache_key not in _logger_cache:
        _logger_cache[cache_key] = setup_logger(name, log_file)
    return _logger_cache[cache_key]

LOGGER = get_logger()
