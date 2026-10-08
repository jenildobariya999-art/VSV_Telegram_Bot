(function(){
const $=s=>document.querySelector(s); const q=$('#q'),repl=$('#repl'),res=$('#results'),info=$('#info');
const tog={case:false,word:false,regex:false}; let timer=null, last='';
const esc=s=>s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
['case','word','regex'].forEach(k=>$('#t-'+k).addEventListener('click',e=>{tog[k]=!tog[k];e.currentTarget.classList.toggle('on',tog[k]);run();}));
const H=()=>{try{return JSON.parse(localStorage.getItem('tbc_hist')||'[]')}catch(e){return[]}};
function addHist(v){ if(!v)return; let h=H().filter(x=>x!==v); h.unshift(v); localStorage.setItem('tbc_hist',JSON.stringify(h.slice(0,12))); }
$('#t-hist').addEventListener('click',()=>{const b=$('#hist'); const h=H(); b.style.display=b.style.display==='none'?'block':'none';
  b.innerHTML=h.length?h.map(x=>`<a href="#" class="pill mu" style="display:inline-block;margin:0 6px 6px 0" data-h="${esc(x)}">${esc(x)}</a>`).join(''):'<span class="sub">No searches yet.</span>';
  b.querySelectorAll('[data-h]').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();q.value=a.dataset.h;b.style.display='none';run();}));});
function hl(line,v){ if(!v||tog.regex) { if(!v) return esc(line); } let re; try{ re=new RegExp(tog.regex?v:v.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'), tog.case?'g':'gi'); if(tog.word&&!tog.regex) re=new RegExp('\\b'+re.source+'\\b',re.flags);}catch(e){return esc(line)}
  return esc(line).replace(new RegExp(re.source.replace(/&/g,'&amp;'),re.flags),m=>'<mark>'+m+'</mark>'); }
async function run(){ const v=q.value; last=v; if(!v){res.innerHTML=res.dataset.empty||res.innerHTML; return;}
  const p=new URLSearchParams({q:v,case:+tog.case,word:+tog.word,regex:+tog.regex}); const r=await fetch(`/bots/${BID}/search.json?`+p); const j=await r.json(); if(v!==last)return;
  if(j.error){res.innerHTML=`<div class="err">${esc(j.error)}</div>`;return;}
  info.textContent=j.total?`${j.total} matches in ${j.results.length} command(s).`:'No matches.';
  res.innerHTML=j.results.map(x=>`<a class="res" href="/bots/${BID}/cmd?name=${encodeURIComponent(x.name)}&line=${x.lines[0]?x.lines[0].n:''}"><div class="h"><b>${esc(x.name)}</b><span class="pill mu">${x.count}</span></div>`+x.lines.map(l=>`<div class="ln"><i>${l.n}</i>${hl(l.t,v)}</div>`).join('')+`</a>`).join('')||'<div class="empty">No matches.</div>'; }
if(res) res.dataset.empty=res.innerHTML;
q.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(run,250)}); q.addEventListener('keydown',e=>{if(e.key==='Enter')addHist(q.value)}); q.addEventListener('blur',()=>addHist(q.value));
$('#btn-replace').addEventListener('click',async()=>{ const v=q.value; if(!v){alert('Type what to search for first');return;}
  const n=repl.value; if(!confirm(`Replace "${v}" with "${n}" in all commands?\n(Commands that would get a syntax error are skipped.)`))return;
  const f=new URLSearchParams({q:v,repl:n,case:+tog.case,word:+tog.word,regex:+tog.regex}); const r=await fetch(`/bots/${BID}/replace`,{method:'POST',headers:{'X-CSRF':csrf()},body:f}); const j=await r.json();
  if(j.error){alert(j.error);return;} addHist(v); alert(`Replaced ${j.replaced} occurrence(s) in ${j.commands} command(s).`+(j.skipped.length?`\nSkipped (would break syntax): ${j.skipped.join(', ')}`:'')); run(); });
})();
