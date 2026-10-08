/* Lightweight code editor for TPY commands: line numbers, error-line highlight, auto-indent,
   autocomplete (Bot.sendmsg -> Bot.sendMessage) with snippets and Tab-through placeholders. No external libraries. */
(function(){
const ta=document.getElementById('code'); if(!ta) return;
const API=window.TBC_API||[];
// ---------- build DOM
const ed=document.createElement('div'); ed.className='ed';
ed.innerHTML='<div class="gut"><pre></pre></div><div class="body"><div class="hl"></div></div><div class="pop"></div>';
ta.parentNode.insertBefore(ed,ta); const body=ed.querySelector('.body'); body.appendChild(ta);
ta.setAttribute('wrap','off'); ta.setAttribute('autocapitalize','off'); ta.setAttribute('autocorrect','off'); ta.spellcheck=false; ta.removeAttribute('rows');
const gut=ed.querySelector('.gut pre'), hl=ed.querySelector('.hl'), pop=ed.querySelector('.pop');
let errLine=parseInt(ta.dataset.errline||'')||0;
function lh(){return parseFloat(getComputedStyle(ta).lineHeight)||19}
function pad(){return parseFloat(getComputedStyle(ta).paddingTop)||0}
function renderGutter(){ const n=ta.value.split('\n').length; let s=''; for(let i=1;i<=n;i++)s+=(i===errLine?'●':i)+'\n'; if(gut.textContent!==s)gut.textContent=s; gut.parentNode.scrollTop=ta.scrollTop;
  if(errLine&&errLine<=n){hl.style.display='block';hl.style.height=lh()+'px';hl.style.top=(pad()+(errLine-1)*lh()-ta.scrollTop)+'px'}else hl.style.display='none'; }
ta.addEventListener('scroll',renderGutter);
// ---------- caret position (mirror technique)
function caretXY(pos){
  const d=document.createElement('div'), cs=getComputedStyle(ta);
  ['fontFamily','fontSize','fontWeight','lineHeight','letterSpacing','paddingTop','paddingLeft','paddingRight','paddingBottom','borderLeftWidth','borderTopWidth','tabSize','boxSizing'].forEach(p=>d.style[p]=cs[p]);
  d.style.cssText+=';position:absolute;visibility:hidden;white-space:pre;top:0;left:0;width:'+ta.clientWidth+'px;overflow:hidden';
  d.textContent=ta.value.slice(0,pos); const sp=document.createElement('span'); sp.textContent='\u200b'; d.appendChild(sp); body.appendChild(d);
  const r={x:sp.offsetLeft-ta.scrollLeft,y:sp.offsetTop-ta.scrollTop+lh()}; d.remove(); return r;
}
// ---------- suggestions
let items=[],sel=0,wstart=0,open=false;
function score(it,w){ const t=it.t.toLowerCase(), q=w.toLowerCase(); if(t===q)return 0; if(t.startsWith(q))return 1; const i=t.indexOf(q); if(i>=0)return 2+i/100;
  let j=0; for(const ch of t){ if(ch===q[j])j++; if(j===q.length)return 5; } return -1; }
function wordAt(pos){ let s=pos; while(s>0&&/[\w.]/.test(ta.value.charAt(s-1)))s--; return {s:s,w:ta.value.slice(s,pos)}; }
function inStringOrComment(pos){ const ls=ta.value.lastIndexOf('\n',pos-1)+1, line=ta.value.slice(ls,pos); if(line.indexOf('#')>=0&&!/["'].*#/.test(line))return true; return false; }
function showList(force){
  const pos=ta.selectionStart; if(pos!==ta.selectionEnd){hide();return;}
  const {s,w}=wordAt(pos); if(!force&&(w.length<2||/^\d/.test(w)||inStringOrComment(pos))){hide();return;}
  items=API.map(it=>[score(it,w),it]).filter(x=>x[0]>=0).sort((a,b)=>a[0]-b[0]||a[1].t.length-b[1].t.length).slice(0,30).map(x=>x[1]);
  if(!items.length||(items.length===1&&items[0].t===w)){hide();return;}
  wstart=s; sel=0; open=true; renderList(); const c=caretXY(s);
  pop.style.display='block'; const maxL=ed.clientWidth-pop.offsetWidth-8; pop.style.left=Math.max(4,Math.min(c.x+ta.offsetLeft+gut.parentNode.offsetWidth,maxL))+'px'; pop.style.top=(c.y+pad()+2)+'px';
  if(c.y+pad()+pop.offsetHeight>ed.clientHeight) pop.style.top=Math.max(4,c.y+pad()-lh()-pop.offsetHeight-4)+'px';
}
function renderList(){ pop.innerHTML=items.map((it,i)=>'<div class="opt'+(i===sel?' on':'')+'" data-i="'+i+'"><b>'+esc(it.t)+'</b><span>'+esc(it.d)+'</span></div>').join('');
  const on=pop.querySelector('.on'); if(on) on.scrollIntoView({block:'nearest'}); }
function hide(){open=false;pop.style.display='none'}
function esc(s){return s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]))}
pop.addEventListener('mousedown',e=>{ e.preventDefault(); const o=e.target.closest('.opt'); if(o){ sel=+o.dataset.i; accept(); } });
// ---------- snippets
let stops=null,cur=-1,quiet=false;
function accept(){
  const it=items[sel]; if(!it){hide();return;} const pos=ta.selectionStart; hide();
  insertSnippet(it.s,wstart,pos);
}
function insertSnippet(snip,from,to){
  const found=[]; let out='',last=0,m; const re=/\$\{(\d+)(?::((?:[^{}]|\{[^{}]*\})*))?\}/g;
  // indent continuation lines to the current line's indent
  const ls=ta.value.lastIndexOf('\n',from-1)+1, indent=(ta.value.slice(ls,from).match(/^\s*/)||[''])[0];
  while((m=re.exec(snip))){ out+=snip.slice(last,m.index).replace(/\n/g,'\n'+indent); const d=(m[2]||'').replace(/\n/g,'\n'+indent); found.push({n:+m[1],start:from+out.length,len:d.length}); out+=d; last=re.lastIndex; }
  out+=snip.slice(last).replace(/\n/g,'\n'+indent);
  ta.focus(); ta.setSelectionRange(from,to); quiet=true; document.execCommand('insertText',false,out); quiet=false; hide(); // keeps undo history
  if(ta.value.slice(from,from+out.length)!==out){ ta.value=ta.value.slice(0,from)+out+ta.value.slice(to); }
  found.sort((a,b)=>a.n-b.n); stops=found.length?found:null; cur=-1; prev=ta.value; renderGutter(); if(stops)nextStop(); else ta.setSelectionRange(from+out.length,from+out.length);
}
function nextStop(){ if(!stops)return false; cur++; if(cur>=stops.length){stops=null;return false;} const s=stops[cur]; ta.setSelectionRange(s.start,s.start+s.len); return true; }
// keep stops positions in sync with edits
let prev=ta.value, selB=[0,0];
ta.addEventListener('beforeinput',()=>{selB=[ta.selectionStart,ta.selectionEnd];});
ta.addEventListener('keydown',()=>{selB=[ta.selectionStart,ta.selectionEnd];},true);
ta.addEventListener('input',()=>{
  if(stops){ const rem=selB[1]-selB[0], ins=ta.value.length-prev.length+rem, p=selB[0], d=ins-rem;
    stops.forEach(s=>{ if(s.start>=p+rem&&!(s.start===p&&rem===0&&s.len===0&&cur>=0&&stops[cur]===s)) s.start+=d; else if(s.start<=p&&s.start+s.len>=p+rem) s.len=Math.max(0,s.len+d); }); }
  prev=ta.value; renderGutter(); if(!quiet) showList(false);
});
// ---------- keys
ta.addEventListener('keydown',e=>{
  if(open){
    if(e.key==='ArrowDown'){e.preventDefault();sel=(sel+1)%items.length;renderList();return;}
    if(e.key==='ArrowUp'){e.preventDefault();sel=(sel-1+items.length)%items.length;renderList();return;}
    if(e.key==='Enter'||e.key==='Tab'){e.preventDefault();accept();return;}
    if(e.key==='Escape'){e.preventDefault();hide();return;}
  }
  if((e.ctrlKey||e.metaKey)&&e.code==='Space'){e.preventDefault();showList(true);return;}
  if(e.key==='Tab'){ e.preventDefault();
    if(!e.shiftKey&&stops&&nextStop())return;
    const a=ta.selectionStart,b=ta.selectionEnd, v=ta.value;
    if(a!==b&&v.slice(a,b).indexOf('\n')>=0||e.shiftKey){ // block indent / outdent
      const ls=v.lastIndexOf('\n',a-1)+1, blk=v.slice(ls,b), nl=e.shiftKey?blk.replace(/^( {1,4}|\t)/gm,''):blk.replace(/^/gm,'    ');
      ta.setSelectionRange(ls,b); document.execCommand('insertText',false,nl); ta.setSelectionRange(ls,ls+nl.length); }
    else document.execCommand('insertText',false,'    ');
    return; }
  if(e.key==='Enter'&&!e.ctrlKey&&!e.metaKey&&!e.shiftKey){ // auto-indent
    const a=ta.selectionStart, v=ta.value, ls=v.lastIndexOf('\n',a-1)+1, line=v.slice(ls,a), ind=line.match(/^\s*/)[0]; let extra=/:\s*$/.test(line)?'    ':'';
    e.preventDefault(); document.execCommand('insertText',false,'\n'+ind+extra); return; }
  const pairs={'(':')','[':']','{':'}','"':'"',"'":"'"}; // auto-close
  if(pairs[e.key]&&!e.ctrlKey&&!e.metaKey&&ta.selectionStart===ta.selectionEnd){ const a=ta.selectionStart, nx=ta.value.charAt(a), pv=ta.value.charAt(a-1);
    if((e.key==='"'||e.key==="'")&&(/\w/.test(pv)||nx===e.key)){ if(nx===e.key){e.preventDefault();ta.setSelectionRange(a+1,a+1);} return; }
    if(e.key==='"'||e.key==="'"||!/\w/.test(nx)){ e.preventDefault(); document.execCommand('insertText',false,e.key+pairs[e.key]); ta.setSelectionRange(a+1,a+1); } }
  else if((e.key===')'||e.key===']'||e.key==='}')&&ta.value.charAt(ta.selectionStart)===e.key&&ta.selectionStart===ta.selectionEnd){ e.preventDefault(); ta.setSelectionRange(ta.selectionStart+1,ta.selectionStart+1); }
});
ta.addEventListener('blur',()=>setTimeout(hide,120)); ta.addEventListener('click',hide);
renderGutter();
if(errLine){ const y=(errLine-1)*lh(); setTimeout(()=>{ta.scrollTop=Math.max(0,y-ta.clientHeight/3); renderGutter();},50); const p=ta.value.split('\n').slice(0,errLine-1).join('\n').length+(errLine>1?1:0); ta.setSelectionRange(p,p); }
window.addEventListener('resize',renderGutter);
})();
