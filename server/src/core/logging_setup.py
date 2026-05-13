import logging
import logging.config

from .config import LOG_LEVEL
from .paths import LOG_DIR


def setup_logging() -> None:
  LOG_DIR.mkdir(parents=True, exist_ok=True)
  log_file = LOG_DIR / "app.log"

  logging.config.dictConfig(
    {
      "version": 1,
      "disable_existing_loggers": False,
      "formatters": {
        "default": {
          "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        }
      },
      "handlers": {
        "console": {
          "class": "logging.StreamHandler",
          "formatter": "default",
        },
        "file": {
          "class": "logging.handlers.RotatingFileHandler",
          "formatter": "default",
          "filename": str(log_file),
          "maxBytes": 1_000_000,
          "backupCount": 3,
          "encoding": "utf-8",
        },
      },
      "root": {
        "handlers": ["console", "file"],
        "level": LOG_LEVEL,
      },
    }
  )
