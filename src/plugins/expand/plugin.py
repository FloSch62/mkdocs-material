# Copyright (c) 2016-2025 Martin Donath <martin.donath@squidfunk.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from __future__ import annotations

import os

from mkdocs.plugins import BasePlugin

from .config import ExpandConfig

_JS = """
(function() {
  function init() {
    document.querySelectorAll('pre').forEach(function(pre) {
      if (pre.scrollWidth > pre.clientWidth) {
        pre.classList.add('md-expand');
        var btn = document.createElement('button');
        btn.className = 'md-expand-button';
        btn.type = 'button';
        btn.textContent = 'Expand';
        btn.onclick = function() {
          pre.classList.toggle('md-expanded');
          btn.textContent = pre.classList.contains('md-expanded') ? 'Collapse' : 'Expand';
        };
        pre.appendChild(btn);
      }
    });
  }
  if (document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);
})();
"""

_CSS = """
.md-expand {
  position: relative;
  overflow: auto;
}
.md-expand-button {
  position: absolute;
  top: 4px;
  right: 4px;
  font-size: 0.75rem;
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 2px;
  cursor: pointer;
}
.md-expand.md-expanded {
  width: max-content;
  max-width: none;
}
"""


class ExpandPlugin(BasePlugin[ExpandConfig]):

    def on_config(self, config):
        if not self.config.enabled:
            return

        self.dest_dir = os.path.join('assets', 'expand')
        js = os.path.join(self.dest_dir, 'expand.js')
        css = os.path.join(self.dest_dir, 'expand.css')
        if js not in config.extra_javascript:
            config.extra_javascript.append(js)
        if css not in config.extra_css:
            config.extra_css.append(css)

    def on_post_build(self, *, config):
        if not self.config.enabled:
            return

        dest = os.path.join(config.site_dir, self.dest_dir)
        os.makedirs(dest, exist_ok=True)
        with open(os.path.join(dest, 'expand.js'), 'w', encoding='utf-8') as f:
            f.write(_JS)
        with open(os.path.join(dest, 'expand.css'), 'w', encoding='utf-8') as f:
            f.write(_CSS)
