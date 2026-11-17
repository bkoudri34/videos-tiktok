// Style « Duo 3D » : deux mannequins façon pâte à modeler, construits en primitives Three.js,
// rendus image par image (renderAt(t) -> extra(t)). Déterministe : tout dépend uniquement de t.
// La config (avant ce fichier) définit DUO = {lines:[{who:'M'|'P', M:'pose', P:'pose', shot:'wide'|'M'|'P'}...]}
// Poses : idle, talk, point, shrug, hip, shock, head (mains sur la tête), cool (bras levés), think.
(function(){
const W=1080,H=1920;
const R=new THREE.WebGLRenderer({antialias:true,preserveDrawingBuffer:true});
R.setPixelRatio(1);R.setSize(W,H,false);
R.shadowMap.enabled=true;R.shadowMap.type=THREE.PCFSoftShadowMap;
R.outputEncoding=THREE.sRGBEncoding;
document.getElementById('three').appendChild(R.domElement);
const BG=(DUO.bg!==undefined)?DUO.bg:0x07080b;
const sc=new THREE.Scene();sc.background=new THREE.Color(BG);sc.fog=new THREE.Fog(BG,8,20);
const cam=new THREE.PerspectiveCamera(30,W/H,0.1,60);

// lumières : ciel/sol + projecteur principal qui projette les ombres + contre-jour
sc.add(new THREE.HemisphereLight(0xdfe6ff,0x0d0f14,0.5));
const key=new THREE.DirectionalLight(0xffffff,0.95);key.position.set(2.2,5,4.5);key.castShadow=true;
key.shadow.mapSize.set(1024,1024);key.shadow.camera.left=-3;key.shadow.camera.right=3;key.shadow.camera.top=3;key.shadow.camera.bottom=-1;key.shadow.radius=6;key.shadow.bias=-0.0005;
sc.add(key);
const rim=new THREE.DirectionalLight(0x9fb4ff,0.55);rim.position.set(-3,3,-4);sc.add(rim);

// sol sombre + quadrillage
const floor=new THREE.Mesh(new THREE.PlaneGeometry(60,60),new THREE.MeshStandardMaterial({color:0x0a0c11,roughness:1}));
floor.rotation.x=-Math.PI/2;floor.receiveShadow=true;sc.add(floor);
const grid=new THREE.GridHelper(60,90,0x4a5878,0x2f3a52);grid.position.y=0.002;sc.add(grid);

function mat(c){return new THREE.MeshStandardMaterial({color:c,roughness:0.88,metalness:0})}
function M(geo,m){const x=new THREE.Mesh(geo,m);x.castShadow=true;x.receiveShadow=true;return x}
function cap(r,len,m){return M(new THREE.CapsuleGeometry(r,len,8,16),m)}
function sph(r,m){return M(new THREE.SphereGeometry(r,32,24),m)}

// segment de membre : pivot au niveau de l'articulation, le membre pend vers -Y
function seg(r,len,m){const p=new THREE.Group();const c=cap(r,len,m);c.position.y=-(len/2+r*0.6);p.add(c);p.userData.len=len+r*1.2;return p}

function guy(o){
 const fat=o.fat||0,mu=o.muscle||0,m=mat(o.color||0xe9e5de);
 const root=new THREE.Group(),body=new THREE.Group();root.add(body);
 const hipY=0.93;
 // jambes
 const legs=[];
 for(const s of [-1,1]){
  const th=seg(0.075+fat*0.035+mu*0.01,0.36,m);th.position.set(s*(0.1+fat*0.05),hipY,0);
  const sh=seg(0.058+fat*0.02,0.34,m);sh.position.y=-th.userData.len;th.add(sh);
  const ft=cap(0.05,0.12,m);ft.rotation.x=Math.PI/2;ft.position.set(0,-sh.userData.len-0.02,0.06);sh.add(ft);
  body.add(th);legs.push({th,sh});
 }
 // bassin + tronc
 const pel=sph(0.17+fat*0.07,m);pel.scale.set(1.1,0.75,0.85);pel.position.y=hipY+0.04;body.add(pel);
 const torso=new THREE.Group();torso.position.y=hipY+0.05;body.add(torso);
 if(fat>0){
  const belly=sph(0.29,m);belly.scale.set(1.05+fat*0.1,1.0,0.95+fat*0.2);belly.position.set(0,0.27,0.05*fat);torso.add(belly);
  const ch=sph(0.27,m);ch.scale.set(1.1,0.8,0.85);ch.position.y=0.5;torso.add(ch);
 } else {
  const ab=cap(0.15,0.16,m);ab.scale.set(1.05,1,0.72);ab.position.y=0.2;torso.add(ab);
  const ch=sph(0.2,m);ch.scale.set(1.25+mu*0.25,0.95,0.7);ch.position.y=0.44;torso.add(ch);

 }
 const shY=0.55,shX=0.25+fat*0.1+mu*0.05;
 for(const s of [-1,1]){const d=sph(0.085+mu*0.02+fat*0.02,m);d.position.set(s*shX,shY,0);torso.add(d)}
 // cou + tête
 const neck=cap(0.055+mu*0.015,0.06,m);neck.position.y=shY+0.1;torso.add(neck);
 const head=new THREE.Group();head.position.y=shY+0.17;torso.add(head);
 const hd=sph(0.115,m);hd.scale.set(0.92,1.12,1.0);hd.position.y=0.11;head.add(hd);
 const jaw=sph(0.08,m);jaw.scale.set(1.0,0.8,1.0);jaw.position.set(0,0.04,0.025);head.add(jaw);
 const nose=sph(0.022,m);nose.position.set(0,0.1,0.115);head.add(nose);
 for(const s of [-1,1]){const ear=sph(0.025,m);ear.scale.set(0.5,1,0.8);ear.position.set(s*0.105,0.1,0);head.add(ear)}
 // bras
 const arms={};
 for(const s of [-1,1]){
  const ua=seg(0.05+mu*0.025+fat*0.03,0.24,m);ua.position.set(s*shX,shY,0);
  const fa=seg(0.042+mu*0.012+fat*0.018,0.22,m);fa.position.y=-ua.userData.len;ua.add(fa);
  const hn=sph(0.048,m);hn.scale.set(0.85,1.15,0.6);hn.position.y=-fa.userData.len-0.02;fa.add(hn);
  torso.add(ua);arms[s]={ua,fa};
 }
 root.traverse(x=>{});
 return {root,body,torso,head,arms,legs,fat};
}

const G2={P:guy({fat:1,color:0xeae3d7}),M:guy({muscle:1,color:0xe6e8ec})};
const XP=-0.52,XM=0.52;
G2.P.root.position.x=XP;G2.M.root.position.x=XM;
G2.P.root.rotation.y=0.38;G2.M.root.rotation.y=-0.38;
sc.add(G2.P.root);sc.add(G2.M.root);

// poses : angles des épaules (z = écarté, x = devant), coudes, tête ; s = côté (+1 = côté de l'autre perso)
// chaque pose renvoie {L:[uz,ux,fz,fx], O:[...] , hy, hp, lean, jump} ; L = bras côté intérieur (vers l'autre), O = bras extérieur
const P0={L:[0.12,0,0,0.15],O:[0.12,0,0,0.15],hy:0,hp:0,lean:0,jump:0};
function pose(n,t,talking){
 const w=Math.sin(t*7.3),w2=Math.sin(t*4.1+1);
 switch(n){
  case 'talk':return {L:[0.25,-0.55+0.28*w,0,1.1+0.25*w2],O:[0.15,-0.1,0,0.3],hy:0.1*w2,hp:0.05*w,lean:0.04,jump:0};
  case 'point':return {L:[1.35,-0.35,0,0.05],O:[0.14,0,0,0.25],hy:0.15,hp:-0.05,lean:0.06,jump:0};
  case 'shrug':return {L:[0.55,-0.6,0,1.6],O:[0.55,-0.6,0,1.6],hy:0.15*w2,hp:0.12,lean:-0.02,jump:0.02};
  case 'hip':return {L:[0.25,-0.4,0,1.2+0.15*w],O:[0.75,0.25,-2.0,0],hy:0.1,hp:0,lean:0.03,jump:0};
  case 'shock':return {L:[1.1,-0.5,0,0.6],O:[1.1,-0.5,0,0.6],hy:0,hp:-0.15,lean:-0.12,jump:0.06};
  case 'head':return {L:[2.35,-0.3,-2.75,0],O:[2.35,-0.3,-2.75,0],hy:0.25*Math.sin(t*9),hp:0.18,lean:0.05,jump:0};
  case 'cool':return {L:[2.5,0,-0.4,0],O:[2.5,0,-0.4,0],hy:0,hp:-0.12,lean:0,jump:0.05*Math.abs(Math.sin(t*6))};
  case 'think':return {L:[0.2,-0.9,0,2.3],O:[0.2,-0.5,0,1.5],hy:0.2,hp:-0.12,lean:0,jump:0};
  default:return {L:[0.12,0,0,0.15],O:[0.12,0,0,0.15],hy:0.05*Math.sin(t*1.3),hp:0,lean:0,jump:0};
 }
}
function mix(a,b,k){const f=(x,y)=>x+(y-x)*k;return {L:a.L.map((v,i)=>f(v,b.L[i])),O:a.O.map((v,i)=>f(v,b.O[i])),hy:f(a.hy,b.hy),hp:f(a.hp,b.hp),lean:f(a.lean,b.lean),jump:f(a.jump,b.jump)}}
function apply(g,p,inner,t,talking){
 // inner = signe x du côté intérieur (vers l'autre personnage)
 for(const s of [-1,1]){
  const a=s===inner?p.L:p.O;const A=g.arms[s];
  A.ua.rotation.set(a[1],0,s*a[0]);A.fa.rotation.set(-a[3],0,s*a[2]);
 }
 g.head.rotation.set(p.hp+(talking?0.06*Math.sin(t*11):0),p.hy,0);
 g.torso.rotation.set(p.lean,0,0);
 const br=Math.sin(t*2.2+(g.fat?1:0))*0.008;
 g.body.position.y=p.jump+br+(talking?Math.abs(Math.sin(t*9))*0.012:0);
 g.torso.scale.set(1+br,1+br,1+br);
}
function lineAt(t){let i=0;for(let k=0;k<S.length;k++)if(t>=S[k]-0.05)i=k;return i}
// caméra : plan large / plan sur un perso ; coupe franche à chaque réplique + petit zoom « punch »
const SHOT={
 wide:{p:[0,1.3,8.6],l:[0,1.08,0]},
 P:{p:[XP*0.3,1.6,5.4],l:[XP+0.08,1.38,0]},
 M:{p:[XM*0.3,1.6,5.4],l:[XM-0.08,1.38,0]},
};
const v3=(a)=>new THREE.Vector3(...a);
function proj(obj,dy){const v=new THREE.Vector3();obj.getWorldPosition(v);v.y+=dy;v.project(cam);return [(v.x*0.5+0.5)*W,(-v.y*0.5+0.5)*H]}
const lbl={P:document.getElementById('lblP'),M:document.getElementById('lblM')};
const ancs=[...document.querySelectorAll('.anc')];

window.extra=function(t){
 const i=lineAt(t),L=DUO.lines[i],prev=DUO.lines[Math.max(0,i-1)];
 const t0=S[i],k=Math.min(1,Math.max(0,(t-t0+0.05)/0.28)),ke=1-Math.pow(1-k,3);
 const lp=t-(END-0.45);
 for(const w of ['P','M']){
  const talking=(L.who===w)&&(t<S[i]+0.1+(G[i][G[i].length-1][1]-S[i]));
  const a=pose(i>0?prev[w]:L[w],t,false),b=pose(L[w],t,talking);
  apply(G2[w],mix(a,b,i>0?ke:1),w==='M'?-1:1,t,talking);
 }
 // caméra
 const sh=SHOT[L.shot||'wide'];
 const since=t-t0;const punch=since>=0&&since<0.4?(1-Math.min(1,since/0.4))**2*0.35:0;
 const drift=0.05*Math.sin(t*0.7),dz=-0.12*Math.min(1,since/3);
 const p=v3(sh.p),l=v3(sh.l);const dir=p.clone().sub(l).normalize();
 p.addScaledVector(dir,dz-punch);p.x+=drift;p.y+=0.02*Math.sin(t*1.1);
 if(lp>0){/* boucle : retour vers le plan d'ouverture */const w0=SHOT[DUO.lines[0].shot||'wide'];const q=Math.min(1,lp/0.4);p.lerp(v3(w0.p),q);l.lerp(v3(w0.l),q)}
 cam.position.copy(p);cam.lookAt(l);cam.updateMatrixWorld();
 R.render(sc,cam);
 // étiquettes + ancres au-dessus des têtes
 for(const w of ['P','M']){
  const [x,y]=proj(G2[w].head,0.32);
  if(lbl[w]){lbl[w].style.left=x+'px';lbl[w].style.top=y+'px';lbl[w].style.opacity=(i===0||lp>0||L.lbl===false||(L.shot&&L.shot!=='wide'&&L.shot!==w))?0:1}
  for(const a of ancs)if(a.dataset.who===w){a.style.left=x+'px';a.style.top=(y-60)+'px'}
 }
};
})();
