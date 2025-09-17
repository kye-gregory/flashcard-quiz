import logging
import logging.config
import tomllib
from pathlib import Path

from app.config.loader import settings
from .exceptions import LoggingConfigError


def setup_logging() -> None:
    """Configure logging from TOML file."""

    config_path = Path(settings.LOGGING_CONFIG_FILE)
    try:
        with config_path.open("rb") as f:
            config = tomllib.load(f)
        logging.config.dictConfig(config)

    except Exception as e:
        raise LoggingConfigError(e)
