document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('pre > code').forEach(code => {
    const pre = code.parentElement;
    if (!pre) return;
    if (pre.scrollWidth <= pre.clientWidth) return;

    pre.classList.add('code-expandable');
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'code-expand-button';
    btn.textContent = 'Expand';
    btn.addEventListener('click', () => {
      pre.classList.toggle('code-expanded');
      btn.textContent = pre.classList.contains('code-expanded') ? 'Collapse' : 'Expand';
    });
    pre.insertBefore(btn, pre.firstChild);
  });
});
