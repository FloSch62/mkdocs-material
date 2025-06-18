from mkdocs.config.config_options import Type
from mkdocs.config.base import Config


class ExpandConfig(Config):
    """Configuration for the expand plugin."""

    enabled = Type(bool, default=True)
