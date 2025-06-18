import os
from mkdocs.plugins import BasePlugin
from mkdocs.utils import copy_file

from .config import ExpandConfig

class ExpandPlugin(BasePlugin[ExpandConfig]):
    JS_PATH = "assets/javascripts/expand.js"
    CSS_PATH = "assets/stylesheets/expand.css"

    def on_config(self, config):
        if not self.config.enabled:
            return
        if self.JS_PATH not in config.extra_javascript:
            config.extra_javascript.append(self.JS_PATH)
        if self.CSS_PATH not in config.extra_css:
            config.extra_css.append(self.CSS_PATH)

    def on_post_build(self, *, config):
        if not self.config.enabled:
            return
        src_dir = os.path.join(os.path.dirname(__file__), "assets")
        files = [
            (os.path.join(src_dir, "expand.js"), os.path.join(config.site_dir, self.JS_PATH)),
            (os.path.join(src_dir, "expand.css"), os.path.join(config.site_dir, self.CSS_PATH)),
        ]
        for src, dest in files:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            copy_file(src, dest)
