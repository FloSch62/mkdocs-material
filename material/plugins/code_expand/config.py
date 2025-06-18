from mkdocs.config.base import Config
from mkdocs.config.config_options import Type

class CodeExpandConfig(Config):
    enabled = Type(bool, default=True)
