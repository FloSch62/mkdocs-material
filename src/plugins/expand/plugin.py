from __future__ import annotations

from mkdocs.plugins import BasePlugin

from .config import ExpandConfig


SCRIPT = """
<script>
document.addEventListener('DOMContentLoaded',function(){
  document.querySelectorAll('pre > code').forEach(function(code){
    const pre = code.parentElement;
    if(pre.scrollWidth > pre.clientWidth){
      const wrapper = document.createElement('div');
      wrapper.className = 'md-code-expand';
      pre.parentNode.insertBefore(wrapper, pre);
      wrapper.appendChild(pre);
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'md-code-expand__toggle';
      button.textContent = 'Expand';
      button.addEventListener('click', function(){
        wrapper.classList.toggle('expanded');
        button.textContent = wrapper.classList.contains('expanded') ? 'Collapse' : 'Expand';
      });
      wrapper.appendChild(button);
    }
  });
});
</script>
<style>
.md-code-expand{position:relative;margin:0}
.md-code-expand__toggle{position:absolute;top:4px;right:4px;font-size:.75em;cursor:pointer}
.md-code-expand.expanded pre{max-width:none;width:auto}
</style>
"""


class ExpandPlugin(BasePlugin[ExpandConfig]):
    """MkDocs plugin to add expandable code blocks."""

    def on_post_page(self, output: str, *, page, config) -> str:
        if not self.config.enabled:
            return output
        if '</body>' in output:
            return output.replace('</body>', SCRIPT + '</body>')
        return output
