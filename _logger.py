from loguru import logger
import configparser as cfg
import os


def logger_handler(msg: str, mode=2) -> None:
    """
    Handles logging of messages
    mode: 0 = debug, 1 = info, 2 = error (default)
    """

    # construct logger
    _log_constructor(mode)

    # log message
    if mode == 0:
        logger.exception(msg)
    elif mode == 1:
        logger.info(msg)
    else:
        logger.error(msg)


def _log_constructor(mode: int) -> None:
    """
    internal function to construct the logger 
    requires config file in the same directory!
    """

    # read config file
    config = cfg.ConfigParser()
    config.read('config.ini')

    _log_level_mapping = {0: 'DEBUG', 1: 'INFO', 2: 'ERROR'}

    # define log levels as defined in config file
    _config_level = {0: 'LOGGING_DEBUG', 1: 'LOGGING_INFO', 2: 'LOGGING_ERROR'}

    _mode = _log_level_mapping[mode]

    _cnf_lvl = _config_level[mode]

    _file_name = os.path.expanduser(
        config.get(_cnf_lvl, 'log_file', fallback=''))

    _serialize = config.get(_cnf_lvl, 'log_serialize')
    _diagnose = config.get(_cnf_lvl, 'log_diagnose')

    logger.add(_file_name,
               rotation=config.get(_cnf_lvl, 'log_rotate', fallback=''),
               level=_mode,
               format=config.get(_cnf_lvl, 'log_format', fallback=''),
               compression=config.get(
                   _cnf_lvl, 'log_compression', fallback=''),
               diagnose=eval(_diagnose),
               serialize=eval(_serialize))
