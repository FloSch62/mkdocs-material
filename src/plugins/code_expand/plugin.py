from __future__ import annotations

import os
from mkdocs.plugins import BasePlugin
from mkdocs.utils import copy_file
from mkdocs.config.defaults import MkDocsConfig

from .config import CodeExpandConfig


class CodeExpandPlugin(BasePlugin[CodeExpandConfig]):
    def on_config(self, config: MkDocsConfig):
        if not self.config.enabled:
            return

        self.script_name = os.path.join('assets', 'javascripts', 'code-expand.js')
        self.style_name = os.path.join('assets', 'stylesheets', 'code-expand.css')
        self.script_source = os.path.join(os.path.dirname(__file__), 'code-expand.js')
        self.style_source = os.path.join(os.path.dirname(__file__), 'code-expand.css')

        if self.script_name not in config.extra_javascript:
            config.extra_javascript.append(self.script_name)
        if self.style_name not in config.extra_css:
            config.extra_css.append(self.style_name)

    def on_post_build(self, *, config: MkDocsConfig):
        if not self.config.enabled:
            return
        dest_script = os.path.join(config.site_dir, self.script_name)
        dest_style = os.path.join(config.site_dir, self.style_name)
        os.makedirs(os.path.dirname(dest_script), exist_ok=True)
        os.makedirs(os.path.dirname(dest_style), exist_ok=True)
        copy_file(self.script_source, dest_script)
        copy_file(self.style_source, dest_style)
