const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const eo=x=>1-Math.pow(1-cl(x),3);
const eb=x=>{x=cl(x);const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)};
// G[i][j] = start time of subtitle group j of scene i (absolute, seconds, from the real voice-over)
const GT=(i,j)=>G[i][Math.min(j,G[i].length-1)][0];
(function(){const c=document.createElement('canvas');c.width=c.height=512;const x=c.getContext('2d');const d=x.createImageData(512,512);
 let s=23;for(let i=0;i<d.data.length;i+=4){s=(s*16807)%2147483647;const v=(s%255);d.data[i]=d.data[i+1]=d.data[i+2]=v;d.data[i+3]=255}
 x.putImageData(d,0,0);$('grain').style.backgroundImage=`url(${c.toDataURL()})`;})();
function tr(el,o,tx=0,ty=0,sc=1,rot=0){el.style.opacity=o;el.style.transform=`translate(${tx}px,${ty}px) scale(${sc}) rotate(${rot}deg)`;el.style.visibility=o<=0.001?'hidden':'visible'}
const scenes=[...document.querySelectorAll('.scene')].map(el=>{const [a,b]=el.dataset.s.split('-').map(Number);return {el,a,b:b===undefined?a:b,inn:el.dataset.in||'up'}});
document.querySelectorAll('[data-fx=tw]').forEach(el=>{const t=el.textContent;el.innerHTML=[...t].map(c=>`<span class=ch>${c===' '?'&nbsp;':c}</span>`).join('');});
const CAMA=(typeof CAM!=='undefined')?CAM:1;
const items=[...document.querySelectorAll('[data-g]')].map(el=>{const [i,j]=el.dataset.g.split('.').map(Number);return {el,i,j,fx:el.dataset.fx||'pop',cnt:el.dataset.count?Number(el.dataset.count):null,suf:el.dataset.suf||' €'}});
const SLOW=document.querySelector('[data-slow]');
const slowT=SLOW?GT(...SLOW.dataset.slow.split('.').map(Number)):-9;
function itemAt(it,t,final){
 const d=final?9:t-GT(it.i,it.j); const el=it.el;
 if(d<0){el.style.opacity=0;el.style.visibility='hidden';return}
 if(it.fx==='tw'){el.style.visibility='visible';el.style.opacity=1;const cs=el.querySelectorAll('.ch');const n=cs.length;const k=d/0.032;cs.forEach((c,i)=>{const v=cl(k-i,0,4)/4;c.style.opacity=v;c.style.filter=v<1?`blur(${(1-v)*8}px)`:'none';});return}
 if(it.fx==='draw'){el.style.visibility='visible';el.style.opacity=1;el.style.strokeDashoffset=1-eo(d/0.45);return}
 if(it.fx==='growY'){el.style.visibility='visible';el.style.opacity=1;el.style.transform=`scaleY(${cl(d/1.6)})`;return}
 if(it.fx==='sweep'){el.style.visibility='visible';el.style.opacity=1;el.style.transform=`rotate(${-90+360*eo(d/1.4)}deg)`;return}
 if(it.fx==='fade'){el.style.visibility='visible';el.style.opacity=cl(d/0.35);el.style.transform='none';return}
 if(it.fx==='strike'){el.style.visibility='visible';el.style.opacity=1;el.style.transform=`scaleX(${eo(d/0.25)})`;return}
 el.style.visibility='visible';
 let o=cl(d/0.12),tx=0,ty=0,sc=1,rot=0;
 if(it.fx==='pop'){sc=0.6+0.4*eb(d/0.35)}
 else if(it.fx==='up'){ty=(1-eb(d/0.4))*160}
 else if(it.fx==='right'){tx=(1-eb(d/0.4))*420}
 else if(it.fx==='left'){tx=-(1-eb(d/0.4))*420}
 else if(it.fx==='stamp'){sc=1+0.7*(1-eo(d/0.28));rot=-6*(1-eo(d/0.28))}
 else if(it.fx==='tick'){sc=1+0.35*(1-eo(d/0.3))}
 if(el===SLOW){const md=d;sc*=1+0.12*Math.pow(1-cl(md/1.3),2.5)}
 if(it.fx==='type'){el.style.opacity=1;el.style.transform='none';const n=el.textContent.length,k=Math.min(n,Math.floor(cl(d/0.7)*n+0.999));el.style.clipPath=`inset(0 ${100-100*k/n}% 0 0)`;}
 else if(it.fx==='grow'){el.style.opacity=1;el.style.transform=`scaleX(${eb(d/0.5)})`;}
 else {el.style.opacity=o;el.style.transform=`translate(${tx}px,${ty}px) scale(${sc}) rotate(${rot}deg)`;}
 if(it.cnt!==null){const dur=el===SLOW?1.1:0.55;el.querySelector('.v').textContent=Math.round(it.cnt*eo(d/dur))+it.suf}
}
function sceneAt(sc,t){
 const t0=S[sc.a], t1=S[sc.b+1]??END;
 const d=t-t0, o2=t-(t1-0.08);
 if(d<0||o2>0.18){sc.el.style.opacity=0;sc.el.style.visibility='hidden';return}
 let o=cl(d/0.1),tx=0,ty=0,s=1;
 if(sc.a>0){ if(sc.inn==='up')ty=(1-eb(d/0.42))*520; else if(sc.inn==='right')tx=(1-eb(d/0.42))*900; else if(sc.inn==='left')tx=-(1-eb(d/0.42))*900; else if(sc.inn==='pop')s=0.7+0.3*eb(d/0.4);}
 else o=1;
 if(o2>0){const k=eo(o2/0.18);o*=1-k;tx-=k*260;}
 tr(sc.el,o,tx,ty,s);
}
function renderAt(t){
 const hx=(Math.sin(t*1.05)*9+Math.sin(t*3.4+2)*3)*CAMA, hy=(Math.cos(t*0.85)*7+Math.sin(t*2.7)*3)*CAMA, hr=Math.sin(t*0.6+1)*0.6*CAMA;
 let pz=0;for(const s of S.slice(1)){const d=t-s;if(d>=0&&d<0.35)pz=Math.max(pz,(1-eo(d/0.35))*0.07*CAMA)}
 const md=t-slowT; let mz=0; if(md>0&&md<1.4) mz=0.05*Math.sin(cl(md/1.4)*Math.PI);
 const push=(typeof PUSH!=='undefined')?PUSH*((t-(S.filter(x=>x<=t).pop()||0))):0;
 $('cam').style.transform=`translate(${hx}px,${hy}px) rotate(${hr}deg) scale(${1+pz+mz+push})`;
 if($('tm')){const r=Math.max(0,END-t);$('tm').textContent='00:'+String(Math.floor(r)).padStart(2,'0')+'.'+String(Math.floor((r%1)*100)).padStart(2,'0');}
 if($('rec'))$('rec').style.opacity=(Math.floor(t*1.6)%2)?0.25:1;
 $('flash').style.opacity=(md>=0&&md<0.12)?0.35*(1-md/0.12):0;
 const lp=t-(END-0.45);
 for(const sc of scenes){ if(lp>0&&sc.a===0){tr(sc.el,eo(lp/0.25),0,0,1.06-0.06*eo(lp/0.4));} else if(lp>0){sceneAt(sc,t);const o=parseFloat(sc.el.style.opacity||0)*(1-eo(lp/0.2));sc.el.style.opacity=o;} else sceneAt(sc,t);}
 for(const it of items) itemAt(it,t,lp>0&&it.i===0);
 if(typeof extra==='function')extra(t);
 // subtitles
 let txt='',st=-1;
 for(let i=0;i<G.length;i++)for(const [ts,te,s] of G[i]){if(t>=ts&&t<te){txt=s;st=ts}}
 const sub=$('sub');if(sub.dataset.cur!==txt){sub.innerHTML=txt;sub.dataset.cur=txt}
 sub.style.transform=`scale(${txt?1+0.12*(1-eo((t-st)/0.12)):1})`;sub.style.opacity=txt?1:0;
 $('grain').style.transform=`translate(${Math.floor((Math.sin(t*91.3)*.5+.5)*180)}px,${Math.floor((Math.cos(t*77.9)*.5+.5)*180)}px)`;
}
renderAt(0);
window.READY=true;
