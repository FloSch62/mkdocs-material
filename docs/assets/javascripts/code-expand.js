function initCodeExpand() {
  document.querySelectorAll('pre > code').forEach(function(code) {
    var pre = code.parentElement;
    if (pre.scrollWidth > pre.clientWidth) {
      pre.classList.add('code-expand');
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'code-expand-toggle';
      btn.textContent = '\u2B48'; // unicode symbol for expand
      btn.title = 'Expand';
      btn.addEventListener('click', function() {
        pre.classList.toggle('expanded');
        btn.title = pre.classList.contains('expanded') ? 'Collapse' : 'Expand';
      });
      pre.insertBefore(btn, pre.firstChild);
    }
  });
}

if (document.readyState !== 'loading') {
  initCodeExpand();
} else {
  document.addEventListener('DOMContentLoaded', initCodeExpand);
}
