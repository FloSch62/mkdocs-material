document.addEventListener("DOMContentLoaded",()=>{
  document.querySelectorAll("pre").forEach(pre=>{
    if(pre.scrollWidth<=pre.clientWidth)return;
    pre.classList.add("code-expandable");
    const btn=document.createElement("button");
    btn.type="button";
    btn.className="code-expand-button";
    btn.title="Expand";
    btn.textContent="⇱";
    btn.addEventListener("click",()=>showOverlay(pre));
    pre.appendChild(btn);
  });
  function showOverlay(pre){
    const overlay=document.createElement("div");
    overlay.className="code-overlay";
    const clone=pre.cloneNode(true);
    const b=clone.querySelector(".code-expand-button");
    if(b)b.remove();
    overlay.appendChild(clone);
    overlay.addEventListener("click",()=>overlay.remove());
    document.body.appendChild(overlay);
  }
});
