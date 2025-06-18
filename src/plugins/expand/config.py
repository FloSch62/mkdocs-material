from mkdocs.config.config_options import Type
from mkdocs.config.base import Config

# Expand plugin configuration
class ExpandConfig(Config):
    enabled = Type(bool, default=True)
