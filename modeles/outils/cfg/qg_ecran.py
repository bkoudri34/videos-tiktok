"""Briques du style E « Écran d'appli en gros plan » (vidéos QG) : à importer dans cfg/qg_<nom>.py.
Barre de recherche avec le mot-clé (visible dès 0 s), gros téléphone dessiné sans logo, doigt qui tape (data-tap),
zoom « punch » (classe zm + data-zg/data-zs/data-zo), pastille d'étape, gains qui surgissent."""
BASE = 'qg_base_ecran.css'
SFX = 'qg_sfx_ecran_template.py'
GAP = 0.3
TAIL = 2.2
MINLEN = 1.8
ROOT = ':root{--bg:#e6edf5}'

LOUPE = '<svg width="50" height="50" viewBox="0 0 50 50"><circle cx="21" cy="21" r="14" fill="none" stroke="#0f172a" stroke-width="6"/><path d="M31 31 L44 44" stroke="#0f172a" stroke-width="7" stroke-linecap="round"/></svg>'


def search(q):
    return f'<div class="search">{LOUPE}<span class="q">{q}</span><span class="cur" id="cur"></span></div>'


def phone(inner, clock='9:41'):
    return (f'<div class="ph"><div class="sc"><div class="isl"></div><div class="bar"><span>{clock}</span><span>●●● ▮</span></div>'
            f'<div class="ap">{inner}</div></div></div>')


def step(n, tot, label, g=None):
    a = f' data-g="{g}" data-fx="pop"' if g else ''
    return f'<div class="step"{a}>ÉTAPE <b>{n}/{tot}</b> · {label}</div>'


HANDSVG = '''<svg width="150" height="190" viewBox="0 0 150 190"><path d="M52 18 Q52 4 66 4 Q80 4 80 18 L80 84 Q84 72 98 74 Q110 76 110 90 Q116 80 128 84 Q140 88 138 104 L136 132 Q132 176 92 184 L70 186 Q40 184 28 156 L10 112 Q4 98 16 92 Q28 88 36 100 L52 124 Z" fill="#fff" stroke="#0f172a" stroke-width="7" stroke-linejoin="round"/>
<path d="M80 84 L80 112 M110 90 L110 116" stroke="#0f172a" stroke-width="5" stroke-linecap="round"/></svg>'''


def hand(x, y, g, frm=(260, 420)):
    """Doigt dont le bout arrive en (x, y) au temps du groupe g (« i.j ») ; part de (x+frm[0], y+frm[1])."""
    return (f'<div class="hand" data-tap="{g}" data-fx0="{frm[0]}" data-fy0="{frm[1]}" style="left:{x - 66}px;top:{y - 6}px">{HANDSVG}</div>'
            f'<div class="rip" data-rip="{g}" style="left:{x}px;top:{y}px"></div><i class="abs" data-g="{g}" data-fx="tap"></i>')


JSX = '''
const HANDS=[...document.querySelectorAll('[data-tap]')].map(el=>{const [i,j]=el.dataset.tap.split('.').map(Number);return {el,i,j,fx:+el.dataset.fx0,fy:+el.dataset.fy0}});
const RIPS=[...document.querySelectorAll('[data-rip]')].map(el=>{const [i,j]=el.dataset.rip.split('.').map(Number);return {el,i,j}});
const ZMS=[...document.querySelectorAll('.zm[data-zg]')].map(el=>{const [i,j]=el.dataset.zg.split('.').map(Number);return {el,i,j,s:+(el.dataset.zs||1.25)}});
function extra(t){
 HANDS.forEach(h=>{const t0=GT(h.i,h.j);const d=t-t0;
  if(d<-0.55){h.el.style.opacity=0;return}
  const k=eo((d+0.55)/0.5);const press=(d>-0.05&&d<0.18)?0.86:1;
  h.el.style.opacity=cl((d+0.55)/0.15);
  h.el.style.transform=`translate(${(1-k)*h.fx}px,${(1-k)*h.fy}px) scale(${press})`;h.el.style.transformOrigin='44% 3%';});
 RIPS.forEach(r=>{const d=t-GT(r.i,r.j);if(d<0||d>0.6){r.el.style.opacity=0;return}
  r.el.style.opacity=1-d/0.6;r.el.style.transform=`scale(${1+d*7})`;});
 ZMS.forEach(z=>{const d=t-GT(z.i,z.j);const k=d<0?0:eb(d/0.35);z.el.style.transform=`scale(${1+(z.s-1)*k})`;});
 const c=document.getElementById('cur');if(c)c.style.opacity=(Math.floor(t*2.2)%2)?0:1;
}
'''
JS = 'const CAM=0.35, PUSH=0.006;' + JSX
