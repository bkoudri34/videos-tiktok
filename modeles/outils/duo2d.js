// Style D2 « Duo dessiné » : deux bonshommes au trait (SVG), posés image par image par extra(t). Déterministe : tout dépend de t.
// La config (avant ce fichier) définit DUO = {lines:[{who:'M'|'P', M:'pose', P:'pose', shot:'wide'|'M'|'P'}...], bun:bool, cap:'#couleur'}
// Poses : idle, talk, point, shrug, hip, shock, head (mains sur la tête), cool (bras levés), think.
(function(){
const NS='http://www.w3.org/2000/svg';
const svg=document.getElementById('duo2d');
function el(tag,attrs,parent){const e=document.createElementNS(NS,tag);for(const k in attrs)e.setAttribute(k,attrs[k]);(parent||svg).appendChild(e);return e}
// « boil » : léger tremblement du trait (bruit qui change de graine toutes les 0,15 s)
const defs=el('defs',{});
const flt=el('filter',{id:'boil',x:'-20%',y:'-20%',width:'140%',height:'140%'},defs);
const turb=el('feTurbulence',{type:'fractalNoise',baseFrequency:'0.035',numOctaves:'2',seed:'1',result:'n'},flt);
el('feDisplacementMap',{in:'SourceGraphic',in2:'n',scale:'5',xChannelSelector:'R',yChannelSelector:'G'},flt);
const world=el('g',{id:'world'});
const FEET=1330;
// sol au feutre + ombres
el('path',{class:'k',d:'M-200 '+(FEET+6)+' Q300 '+(FEET-4)+' 540 '+(FEET+4)+' T1280 '+(FEET+2),filter:'url(#boil)'},world);
el('ellipse',{cx:330,cy:FEET+8,rx:130,ry:16,fill:'rgba(0,0,0,.08)'},world);
el('ellipse',{cx:760,cy:FEET+8,rx:100,ry:14,fill:'rgba(0,0,0,.08)'},world);

// personnages : origine aux pieds ; in = côté intérieur (vers l'autre)
const C={
 P:{x:330,in:1,sh:[85,-330],Lu:95,Lf:92,head:[0,-470],r:62,mouth:[0,-438],eyes:[[-22,-482],[22,-482]],top:-532},
 M:{x:760,in:-1,sh:[44,-412],Lu:100,Lf:96,head:[0,-490],r:52,mouth:[-8,-462],eyes:[[-26,-498],[8,-498]],top:-560},
};
function build(w){
 const c=C[w];const g=el('g',{transform:`translate(${c.x},${FEET})`,filter:'url(#boil)'},world);
 const b=el('g',{},g);c.g=g;c.b=b;
 if(w==='P'){
  el('path',{class:'k',d:'M-42 -140 L-58 0 M-72 0 L-40 0 M42 -140 L58 0 M40 0 L72 0'},b);
  const cp=el('clipPath',{id:'clipP'},defs);el('ellipse',{cx:0,cy:-255,rx:105,ry:135},cp);
  el('ellipse',{class:'kf',cx:0,cy:-255,rx:105,ry:135},b);
  const hz=el('g',{'clip-path':'url(#clipP)'},b);
  for(let k=-6;k<7;k++)el('path',{class:'h',d:`M${k*34-80} -120 L${k*34+80} -400`},hz);
  if(DUO.bun)el('circle',{class:'kf',cx:46,cy:-530,r:24},b);
 } else {
  el('path',{class:'k',d:'M-22 -200 L-38 0 M-56 0 L-34 0 M22 -200 L38 0 M34 0 L56 0'},b);
  el('rect',{class:'kf',x:-48,y:-430,width:96,height:236,rx:24},b);
  el('path',{class:'k',d:'M0 -430 L0 -415'},b);
 }
 c.arm={};
 for(const s of [-1,1]){c.arm[s]=el('path',{class:'k',d:''},b)}
 el('circle',{class:'kf',cx:c.head[0],cy:c.head[1],r:c.r},b);
 if(w==='M'){
  el('path',{d:'M-54 -500 Q0 -585 54 -500 Z',fill:DUO.cap||'#e63946',stroke:'#111','stroke-width':7,'stroke-linejoin':'round'},b);
  el('path',{class:'k',d:'M-50 -502 L-104 -494'},b);
 }
 c.eye=c.eyes.map(([x,y])=>el('path',{class:'k',d:''},b));c.eyesXY=c.eyes;
 c.mo=el('path',{class:'k',d:''},b);
 c.brow=el('path',{class:'k',d:''},b);
}
build('P');build('M');

// poses : [haut, avant-bras] en degrés depuis la verticale basse, positif = vers l'extérieur ; I = bras intérieur, O = bras extérieur
const PO={
 idle:{I:[12,6],O:[12,6]},
 talk:{I:[48,95],O:[16,10]},
 point:{I:[92,90],O:[12,6]},
 shrug:{I:[50,125],O:[50,125]},
 hip:{I:[40,95],O:[42,-55]},
 shock:{I:[140,165],O:[140,165]},
 head:{I:[150,-140],O:[150,-140]},
 cool:{I:[160,178],O:[160,178]},
 think:{I:[22,-150],O:[14,-30]},
};
const MOUTH={shock:'O',head:'O',cool:'big'};
function armD(c,s,u,f){
 const [sx,sy]=[s*c.sh[0],c.sh[1]];const r=Math.PI/180;
 const ex=sx+s*Math.sin(u*r)*c.Lu,ey=sy+Math.cos(u*r)*c.Lu;
 const hx=ex+s*Math.sin(f*r)*c.Lf,hy=ey+Math.cos(f*r)*c.Lf;
 return `M${sx.toFixed(1)} ${sy.toFixed(1)} L${ex.toFixed(1)} ${ey.toFixed(1)} L${hx.toFixed(1)} ${hy.toFixed(1)} M${(hx-8).toFixed(1)} ${hy.toFixed(1)} a8 8 0 1 0 16 0 a8 8 0 1 0 -16 0`;
}
function lineAt(t){let i=0;for(let k=0;k<S.length;k++)if(t>=S[k]-0.05)i=k;return i}
function lerp(a,b,k){return a+(b-a)*k}
function poseFor(name,t,talking){
 const p=JSON.parse(JSON.stringify(PO[name]||PO.idle));
 const w=Math.sin(t*7.3);
 if(name==='talk'){p.I[0]+=12*w;p.I[1]+=18*Math.sin(t*4.1)}
 if(name==='head'){p.I[0]+=5*Math.sin(t*9);p.O[0]+=5*Math.sin(t*9+1)}
 if(name==='cool'){p.I[0]+=6*Math.sin(t*6);p.O[0]+=6*Math.sin(t*6+2)}
 if(talking&&name!=='talk'){p.I[1]+=6*w}
 return p;
}
// plans : large / serré sur un personnage (point du monde -> point de l'écran, échelle)
const SHOT={wide:{s:1,c:[545,1000],to:[540,1000]},P:{s:1.55,c:[330,960],to:[560,980]},M:{s:1.55,c:[760,960],to:[520,980]}};
const lbl={P:document.getElementById('lblP'),M:document.getElementById('lblM')};
const ancs=[...document.querySelectorAll('.anc')];
window.extra=function(t){
 turb.setAttribute('seed',String(1+Math.floor(t/0.15)%7));
 const i=lineAt(t),L=DUO.lines[i],prev=DUO.lines[Math.max(0,i-1)];
 const k=Math.min(1,Math.max(0,(t-S[i]+0.05)/0.22)),ke=1-Math.pow(1-k,3);
 const lp=t-(END-0.45);
 for(const w of ['P','M']){
  const c=C[w];
  const talking=(L.who===w)&&(t<S[i]+0.1+(G[i][G[i].length-1][1]-S[i]));
  const a=poseFor(i>0?prev[w]:L[w],t,false),b=poseFor(L[w],t,talking),kk=i>0?ke:1;
  for(const s of [-1,1]){const A=(s===c.in)?'I':'O';c.arm[s].setAttribute('d',armD(c,s,lerp(a[A][0],b[A][0],kk),lerp(a[A][1],b[A][1],kk)))}
  // bouche
  const mt=MOUTH[L[w]]||'smile';const [mx,my]=c.mouth;
  let md;
  if(talking){const o=Math.abs(Math.sin(t*15))*14+3;md=`M${mx-14} ${my} Q${mx} ${my+o*2} ${mx+14} ${my} Q${mx} ${my-4} ${mx-14} ${my}`}
  else if(mt==='O')md=`M${mx-11} ${my+4} a11 14 0 1 0 22 0 a11 14 0 1 0 -22 0`;
  else if(mt==='big')md=`M${mx-20} ${my-4} Q${mx} ${my+26} ${mx+20} ${my-4} Z`;
  else md=`M${mx-15} ${my} Q${mx} ${my+12} ${mx+15} ${my}`;
  c.mo.setAttribute('d',md);
  // yeux (ronds quand choqué), sourcils
  const big=(mt==='O');const blink=(Math.floor(t*10+(w==='M'?3:0))%37===0);
  c.eye.forEach((e,j)=>{const [ex,ey]=c.eyesXY[j];e.setAttribute('d',blink?`M${ex-6} ${ey} L${ex+6} ${ey}`:big?`M${ex-7} ${ey} a7 9 0 1 0 14 0 a7 9 0 1 0 -14 0`:`M${ex} ${ey-6} L${ex} ${ey+6}`)});
  const [e1,e2]=c.eyesXY;const by=e1[1]-(big?24:18)-(L[w]==='think'?6:0);
  c.brow.setAttribute('d',L[w]==='think'?`M${e1[0]-10} ${by+6} L${e1[0]+8} ${by} M${e2[0]-8} ${by-2} L${e2[0]+10} ${by+6}`:`M${e1[0]-9} ${by} L${e1[0]+9} ${by-2} M${e2[0]-9} ${by-2} L${e2[0]+9} ${by}`);
  // rebond quand il parle + respiration
  const bob=(talking?-Math.abs(Math.sin(t*9))*8:0)+Math.sin(t*2.2+(w==='M'?1:0))*2+((L[w]==='cool'||L[w]==='shock')?-Math.abs(Math.sin(t*6))*10:0);
  c.b.setAttribute('transform',`translate(0 ${bob.toFixed(1)})`);
 }
 // caméra : coupe franche à chaque réplique + zoom « punch »
 const sh=SHOT[L.shot||'wide'];
 const since=t-S[i];const punch=since>=0&&since<0.4?Math.pow(1-Math.min(1,since/0.4),2)*0.12:0;
 let s=sh.s*(1+punch+0.03*Math.min(1,since/3)),cx=sh.c[0],cy=sh.c[1],tx=sh.to[0],ty=sh.to[1];
 if(lp>0){const w0=SHOT[DUO.lines[0].shot||'wide'];const q=Math.min(1,lp/0.4);s=lerp(s,w0.s,q);cx=lerp(cx,w0.c[0],q);cy=lerp(cy,w0.c[1],q);tx=lerp(tx,w0.to[0],q);ty=lerp(ty,w0.to[1],q)}
 const ox=tx-s*cx+6*Math.sin(t*0.7),oy=ty-s*cy;
 world.setAttribute('transform',`translate(${ox.toFixed(2)} ${oy.toFixed(2)}) scale(${s.toFixed(4)})`);
 // étiquettes + ancres au-dessus des têtes
 for(const w of ['P','M']){
  const c=C[w];const x=ox+s*(c.x),y=oy+s*(FEET+c.top-20);
  if(lbl[w]){lbl[w].style.left=x+'px';lbl[w].style.top=y+'px';lbl[w].style.opacity=(i===0||lp>0||L.lbl===false||(L.shot&&L.shot!=='wide'&&L.shot!==w))?0:1}
  for(const a of ancs)if(a.dataset.who===w){a.style.left=x+'px';a.style.top=(y-50)+'px'}
 }
};
})();
