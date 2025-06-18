import os
from mkdocs.plugins import BasePlugin
from mkdocs.utils import copy_file

from .config import ExpandCodeConfig

class ExpandCodePlugin(BasePlugin[ExpandCodeConfig]):
    def on_config(self, config):
        if not self.config.enabled:
            return
        config.extra_javascript.append('assets/javascripts/expand-code.js')
        config.extra_css.append('assets/stylesheets/expand-code.css')

    def on_post_build(self, *, config):
        if not self.config.enabled:
            return
        assets = os.path.join(os.path.dirname(__file__), 'assets')
        js_src = os.path.join(assets, 'expand-code.js')
        css_src = os.path.join(assets, 'expand-code.css')
        js_dst = os.path.join(config.site_dir, 'assets', 'javascripts', 'expand-code.js')
        css_dst = os.path.join(config.site_dir, 'assets', 'stylesheets', 'expand-code.css')
        os.makedirs(os.path.dirname(js_dst), exist_ok=True)
        os.makedirs(os.path.dirname(css_dst), exist_ok=True)
        copy_file(js_src, js_dst)
        copy_file(css_src, css_dst)
