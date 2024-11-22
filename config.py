import pathlib
import os
import logging
from logging.config import dictConfig
from    dotenv import load_dotenv

load_dotenv()

DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")
GUILD_ID = int(os.getenv("DISCORD_GUILD_ID"))

# STAFF ROLES ID
ADMIN_ROLE_ID = int(os.getenv("DISCORD_ADMINISTRATOR_ROLE_ID"))
DEVELOPER_ROLE_ID = int(os.getenv("DISCORD_DEVELOPER_ROLE_ID"))
CURATOR_ROLE_ID = int(os.getenv("DISCORD_CURATOR_ROLE_ID"))
MODERATOR_ROLE_ID = int(os.getenv("DISCORD_MODERATOR_ROLE_ID"))
HELPER_ROLE_ID = int(os.getenv("DISCORD_HELPER_ROLE_ID"))
EVENTER_ROLE_ID = int(os.getenv("DISCORD_EVENTER_ROLE_ID"))

PRIVATE_CATEGORY_ID = int(os.getenv("DISCORD_PRIVATE_CATEGORY_ID"))
MAIN_PRIVATE_CHANNEL_ID = int(os.getenv("DISCORD_MAIN_PRIVATE_CHANNEL_ID"))

# DIR
BASE_DIR = pathlib.Path(__file__).parent
COGS_DIR = BASE_DIR / "cogs"

# COG EXTENSIONS
EXTENSIONS = [
    'cogs.TemporaryVoice'
]

# STAFF ROLES LISTS
HIGHER_STAFF_ROLES = [
    ADMIN_ROLE_ID,
    DEVELOPER_ROLE_ID,
    CURATOR_ROLE_ID
]

LOGGING_CONFIG = {  
    "version": 1,   
    "disabled_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard": {"format": "%(levelname)-10s - %(name)-15s : %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "console2": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/infos.log",
            "mode": "w",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "bot": {"handlers": ["console"], "level": "INFO", "propagate": False},
        "discord": {
            "handlers": ["console2", "file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

dictConfig(LOGGING_CONFIG)