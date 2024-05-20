import logging as logg
from logging import config

log_config = {
    "version": 1,
    "root": {
        "handlers": ["console", "file"],
        "level": "DEBUG"
    },
    "handlers": {
        "console": {
            "formatter": "std_out",
            "class": "logging.StreamHandler",
            "level": "DEBUG"
        },
        "file": {
            "formatter": "std_out",
            "class": "logging.FileHandler",
            "level": "INFO",
            "filename": "interfazNax_log_py.log"
        }
    },
    "formatters": {
        "std_out": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(module)s : %(funcName)s : %(message)s",
        }
    },
}
class logging_ilu(object):
    def __init__(self) -> None:
        config.dictConfig(config=log_config)

    @staticmethod
    def info(mensaje):
        try:
            print('mensaje desde el info de log')
            print(mensaje)
            logg.info(mensaje)
            # logg.basicConfig().__dir__
            print(logg.__path__)
        except Exception as e:
            print(e)

    @staticmethod
    def error(mensaje):
        logg.error(mensaje)