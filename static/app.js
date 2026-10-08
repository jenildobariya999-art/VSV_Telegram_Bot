(function(){
const $=(s,r)=> (r||document).querySelector(s), $$=(s,r)=>[...(r||document).querySelectorAll(s)];
window.$=$; window.$$=$$;
window.csrf=()=> (document.querySelector('meta[name=csrf]')||{}).content||'';
// copy buttons
document.addEventListener('click',e=>{
  const c=e.target.closest('[data-copy]');
  if(c){ const v=c.dataset.copy; (navigator.clipboard?navigator.clipboard.writeText(v):Promise.reject()).catch(()=>{const t=document.createElement('textarea');t.value=v;document.body.appendChild(t);t.select();document.execCommand('copy');t.remove();});
    const old=c.innerHTML; c.dataset.o=old; const r=c.querySelector('.r'); if(r){const o=r.innerHTML;r.textContent='Copied ✓';setTimeout(()=>r.innerHTML=o,1200);} else {c.style.opacity=.6;setTimeout(()=>c.style.opacity=1,600);} }
  if(!e.target.closest('.menu')) $$('.menu.open').forEach(m=>m.classList.remove('open'));
});
// keep active tab visible
const tabs=$('#tabs'); if(tabs){const a=$('a.on',tabs); if(a) tabs.scrollLeft=a.offsetLeft-60;}
// uptime
const up=$('#uptime'); if(up){const st=parseFloat(up.dataset.start||0); if(st){const f=n=>String(n).padStart(2,'0'); const t=()=>{let s=Math.max(0,Math.floor(Date.now()/1000-st));up.textContent=f(Math.floor(s/3600))+':'+f(Math.floor(s%3600/60))+':'+f(s%60)}; t(); setInterval(t,1000);} }
// ---- dashboard chart
function nice(mx){const raw=Math.max(mx,4)/4,p=Math.pow(10,Math.floor(Math.log10(raw)));for(const m of [1,1.5,2,2.5,3,5,7.5,10]){if(m*p>=raw)return m*p}return 10*p}
function curve(pts,base){ // smooth path, never dips below the baseline
  let d='M'+pts[0][0]+','+pts[0][1]; for(let i=0;i<pts.length-1;i++){const p0=pts[i-1]||pts[i],p1=pts[i],p2=pts[i+1],p3=pts[i+2]||p2;
    const c1=[p1[0]+(p2[0]-p0[0])/6,p1[1]+(p2[1]-p0[1])/6],c2=[p2[0]-(p3[0]-p1[0])/6,p2[1]-(p3[1]-p1[1])/6];
    c1[1]=Math.min(c1[1],base);c2[1]=Math.min(c2[1],base); d+=' C'+c1[0].toFixed(1)+','+c1[1].toFixed(1)+' '+c2[0].toFixed(1)+','+c2[1].toFixed(1)+' '+p2[0]+','+p2[1];} return d}
const ch=$('#chart'); if(ch){
  const s=JSON.parse(ch.dataset.series||'[]'),hrs=JSON.parse(ch.dataset.hours||'[]'); const W=520,H=260,L=46,R=16,T=14,B=34;
  const step=nice(Math.max(...s,1)), mx=step*4, x=i=>L+(W-L-R)*i/(s.length-1||1), y=v=>T+(H-T-B)*(1-Math.min(v,mx)/mx);
  let g=''; for(let k=0;k<=4;k++){const v=step*k,yy=y(v); g+=`<line x1="${L}" x2="${W-R}" y1="${yy}" y2="${yy}" stroke="#2a2a31" stroke-dasharray="4 5"/><text x="${L-10}" y="${yy+4}" text-anchor="end">${Math.round(v)}</text>`}
  const base=y(0); const clampY=(p)=>Math.min(p,base); const pts=s.map((v,i)=>[+x(i).toFixed(1),+y(v).toFixed(1)]); const line=pts.length>1?curve(pts,base):''; 
  const area=pts.length>1?line+` L${pts[pts.length-1][0]},${y(0)} L${pts[0][0]},${y(0)} Z`:'';
  let xl=''; [0,6,12,18,s.length-1].forEach(i=>{ if(i<0||!hrs[i])return; const d=new Date(hrs[i]*1000); const t=d.toLocaleTimeString([], {hour:'numeric'}).toLowerCase(); xl+=`<text x="${x(i)}" y="${H-10}" text-anchor="${i==0?'start':(i==s.length-1?'end':'middle')}">${t}</text>`});
  ch.innerHTML=`<svg class="chart" viewBox="0 0 ${W} ${H}" width="100%"><defs><linearGradient id="ar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8b5cf6" stop-opacity=".55"/><stop offset="1" stop-color="#8b5cf6" stop-opacity=".02"/></linearGradient></defs>${g}<path d="${area}" fill="url(#ar)"/><path d="${line}" fill="none" stroke="#8b5cf6" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>${xl}</svg>`;
}
// ---- commands page
const cf=$('#cfilter'); if(cf){
  cf.addEventListener('input',()=>{const q=cf.value.toLowerCase(); $$('#cmdlist .cmdrow').forEach(r=>r.style.display=r.dataset.name.includes(q)?'':'none');});
  $$('[data-del]').forEach(b=>b.addEventListener('click',()=>{ if(confirm('Delete '+b.dataset.del+' ?')){ $('#onedelname').value=b.dataset.del; $('#onedel').submit(); } }));
  const bs=$('#btn-sel'), bd=$('#btn-delsel'), lst=$('#cmdlist');
  bs.addEventListener('click',()=>{const on=lst.classList.toggle('selmode'); bs.classList.toggle('ac',on); bd.style.display=on?'':'none'; if(!on)$$('#cmdlist input[type=checkbox]').forEach(c=>c.checked=false);});
  $('#delform').addEventListener('submit',e=>{const n=$$('#cmdlist input:checked').length; if(!n||!confirm('Delete '+n+' command(s)?'))e.preventDefault();});
  $('#btn-check').addEventListener('click',async()=>{const box=$('#checkres'); box.innerHTML='<div class="card pad mt sub">Checking…</div>';
    const j=await (await fetch(location.pathname.replace('/commands','/check.json'))).json();
    if(!j.bad.length) box.innerHTML=`<div class="flash">✓ All ${j.total} commands have valid syntax.</div>`;
    else box.innerHTML=`<div class="err"><b>${j.bad.length} command(s) have syntax errors:</b>`+j.bad.map(b=>`\n• <a href="${location.pathname.replace('/commands','/cmd')}?name=${encodeURIComponent(b.name)}&line=${b.line||''}" style="text-decoration:underline">${b.name.replace(/</g,'&lt;')}</a> — line ${b.line}: ${(b.msg||'').replace(/</g,'&lt;')}`).join('')+'</div>';});
}
// ---- broadcast live status
$$('[data-bc]').forEach(el=>{ if(el.dataset.status!=='running')return; const id=el.dataset.bc, base=location.pathname.replace(/\/admin\/.*/,'');
  const t=setInterval(async()=>{try{const j=await (await fetch(base+'/broadcast/'+id+'.json')).json(); $('.bc-ok',el).textContent=j.ok||0; $('.bc-err',el).textContent=j.err||0; const p=$('.pill',el); if(p)p.textContent=j.status; if(j.status!=='running')clearInterval(t);}catch(e){clearInterval(t)}},2000);});
})();
