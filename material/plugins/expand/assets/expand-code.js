document.addEventListener('DOMContentLoaded',()=>{
  document.querySelectorAll('.md-typeset pre > code').forEach(code=>{
    const pre=code.parentElement;
    if(pre.scrollWidth>pre.clientWidth){
      const btn=document.createElement('button');
      btn.className='md-expand-code';
      btn.title='Expand code';
      btn.addEventListener('click',()=>{
        pre.classList.toggle('md-code--expanded');
      });
      pre.insertBefore(btn,code);
    }
  });
});
