"""Briques du style C « Collage POV en papier découpé » (vidéos QG, construit le 24/11/2026).
Mise en scène repérée chez @cryptoboye (veille du 23/11/2026) ; rien de copié (ni texte, ni visuel, ni son, ni code promo).
- fond uni vif (jaune moutarde par défaut, ou bleu ciel `BG_SKY`) avec texture papier kraft (SVG feTurbulence statique) ;
- personnages en papier découpé : `perso(x, y, échelle, couleur, bouche, bras, regard, g)` (tête ronde, gros yeux sur attache
  parisienne, bras en bandes de papier qui pivotent sur une attache) ;
- étiquettes de papier collées de travers (`.lab`, `tape(x, y, rot)`), téléphone en papier `phone(...)`, confettis `confetti(...)` ;
- animation saccadée façon stop-motion : tout le rendu est cadencé à 12 i/s (`STOP_JS`), avec un léger « boil » (chaque élément
  `.pp` tremble d'une image à l'autre comme un papier reposé à la main) ;
- son : beat libre de droits synthétisé, bruitages de papier froissé et de ciseaux, disque rayé sur la chute
  (`qg_sfx_collage_template.py`).
À importer dans cfg/qg_<sujet><n>.py : `from qg_collage import *`."""
import random

BASE = 'qg_collage.css'
SFX = 'qg_sfx_collage_template.py'
GAP = 0.3
TAIL = 1.6
MINLEN = 1.2
CAM = 0.25

_PAPER = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='420' height='420'>"
          "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' seed='7'/>"
          "<feColorMatrix values='0 0 0 0 .35  0 0 0 0 .25  0 0 0 0 .1  0 0 0 .22 0'/></filter>"
          "<filter id='f'><feTurbulence type='fractalNoise' baseFrequency='.012 .09' numOctaves='2' seed='3'/>"
          "<feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .10 0'/></filter>"
          "<rect width='420' height='420' filter='url(%23n)'/><rect width='420' height='420' filter='url(%23f)'/></svg>\")")
BG_MUSTARD = '#e3ad2f'
BG_SKY = '#7cc4e8'


def root(bg=BG_MUSTARD):
    return ':root{--bg:%s;--paper:%s}' % (bg, _PAPER)


ROOT = root()

ARMS = {  # angles (deg) bras gauche / droit, 0 = pendant le long du corps
    'down': (8, -8), 'up': (150, -150), 'point': (8, -115), 'pointl': (115, -8), 'hip': (40, -40), 'shrug': (70, -70), 'wave': (8, -150),
}
MOUTHS = {
    'smile': '<path d="M78 112 Q100 134 122 112 Z" fill="#1b1a17"/>',
    'open': '<path d="M80 108 Q100 150 120 108 Z" fill="#1b1a17"/><path d="M90 128 Q100 140 110 128 Z" fill="#e2452f"/>',
    'o': '<ellipse cx="100" cy="122" rx="12" ry="15" fill="#1b1a17"/>',
    'flat': '<rect x="82" y="116" width="36" height="8" rx="4" fill="#1b1a17"/>',
}


def perso(x, y, scale=1.0, color='#2f6fe2', mouth='smile', arms='down', look=0, g=None, fx='pop', hair='#1b1a17', wave=False, jump=False):
    """Personnage en papier découpé (200 x 330 à l'échelle 1) : tête ronde crème, gros yeux sur attache parisienne."""
    al, ar = ARMS[arms]
    w, h = int(200 * scale), int(330 * scale)
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    px = 6 * look
    inner = (
        f'<g class="legs"><rect x="66" y="270" width="24" height="58" rx="6" fill="#1b1a17"/><rect x="110" y="270" width="24" height="58" rx="6" fill="#1b1a17"/></g>'
        f'<g class="arm" data-a="{al}" data-wave="{1 if wave else 0}" style="transform-origin:58px 182px;transform:rotate({al}deg)"><rect x="46" y="176" width="24" height="92" rx="10" fill="{color}"/>'
        f'<circle cx="58" cy="268" r="15" fill="#f6efe3"/></g>'
        f'<g class="arm r" data-a="{ar}" data-wave="{1 if wave else 0}" style="transform-origin:142px 182px;transform:rotate({ar}deg)"><rect x="130" y="176" width="24" height="92" rx="10" fill="{color}"/>'
        f'<circle cx="142" cy="268" r="15" fill="#f6efe3"/></g>'
        f'<path d="M54 168 Q100 150 146 168 L156 284 Q100 296 44 284 Z" fill="{color}"/>'
        '<circle cx="58" cy="182" r="6" fill="#c9a227"/><circle cx="142" cy="182" r="6" fill="#c9a227"/>'
        '<circle cx="100" cy="92" r="80" fill="#f6efe3"/>'
        f'<path d="M24 80 Q30 6 100 10 Q170 6 176 80 Q150 40 100 44 Q50 40 24 80 Z" fill="{hair}"/>'
        f'<g class="eyes"><circle cx="70" cy="84" r="26" fill="#fff" stroke="#1b1a17" stroke-width="4"/><circle cx="130" cy="84" r="26" fill="#fff" stroke="#1b1a17" stroke-width="4"/>'
        f'<g class="pup" data-look="{look}"><circle cx="{70 + px}" cy="88" r="12" fill="#1b1a17"/><circle cx="{130 + px}" cy="88" r="12" fill="#1b1a17"/>'
        f'<circle cx="{70 + px}" cy="88" r="4" fill="#c9a227"/><circle cx="{130 + px}" cy="88" r="4" fill="#c9a227"/></g></g>'
        '<ellipse cx="52" cy="118" rx="12" ry="7" fill="rgba(226,69,47,.35)"/><ellipse cx="148" cy="118" rx="12" ry="7" fill="rgba(226,69,47,.35)"/>'
        f'<g class="mouth">{MOUTHS[mouth]}</g>')
    return (f'<svg class="pp perso" data-jump="{1 if jump else 0}" style="left:{x}px;top:{y}px" width="{w}" height="{h}" viewBox="0 0 200 330"{a}>{inner}</svg>')


def tape(x, y, rot=-8, w=150):
    return f'<div class="tape" style="left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg)"></div>'


def phone(x, y, rot, bank, amount, line2='Virement reçu', cond='prime filleul si conditions remplies', g=None, fx='pop', ng=None):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    n = f' data-g="{ng}" data-fx="pop"' if ng else ''
    return (f'<div class="abs" style="left:{x}px;top:{y}px"{a}><div class="pp" style="transform:rotate({rot}deg)"><div class="ph"><div class="scr">'
            f'<div class="tm">09:41</div><div class="dt">mardi 24 novembre</div>'
            f'<div class="nt"{n}><div class="a">{bank}</div><div class="b">{line2}</div><div class="c">{amount}</div></div>'
            f'<div class="cond">{cond}</div></div></div></div></div>')


def lab(x, y, rot, text, cls='', g=None, fx='stamp', size=None):
    """Étiquette de papier collée de travers (l'animation d'entrée est sur l'enveloppe, la rotation sur l'étiquette)."""
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    fs = f';font-size:{size}px' if size else ''
    return f'<div class="abs" style="left:{x}px;top:{y}px"{a}><div class="lab {cls}" style="transform:rotate({rot}deg){fs}">{text}</div></div>'


def confetti(scene_g, n=22, seed=3, x0=80, x1=930, y0=160):
    """Confettis de papier qui tombent (animés dans STOP_JS à partir de l'instant du groupe scene_g)."""
    r = random.Random(seed)
    cols = ['#e2452f', '#2f6fe2', '#2e9e5b', '#fbf7ee', '#1b1a17', '#ff8fb1']
    out = []
    for i in range(n):
        out.append(f'<div class="conf" data-cg="{scene_g}" data-x="{r.randint(x0, x1)}" data-y="{y0 - r.randint(0, 260)}" data-v="{r.randint(380, 760)}" '
                   f'data-r="{r.randint(-400, 400)}" style="background:{r.choice(cols)}"></div>')
    return ''.join(out)


STOP_JS = r'''
const FPS_STOP=12;const CAM=0.25;
const __ra=renderAt;
renderAt=function(t){return __ra(Math.floor(t*FPS_STOP+1e-6)/FPS_STOP)};
function __h(i,k){let x=Math.sin(i*127.1+k*311.7)*43758.5453;return x-Math.floor(x)}
function extra(t){
 const f=Math.floor(t*FPS_STOP+1e-6);
 const boil=Math.floor(f/2);
 document.querySelectorAll('.pp').forEach((el,i)=>{el.style.rotate=((__h(i,boil)-.5)*1.6)+'deg';el.style.translate=((__h(i+50,boil)-.5)*5)+'px '+((__h(i+90,boil)-.5)*5)+'px'});
 document.querySelectorAll('.perso').forEach((el,i)=>{
  el.querySelectorAll('.arm').forEach((a,k)=>{const b=+a.dataset.a;const w=+a.dataset.wave?(Math.sin(f*0.9+k*2)*28):(Math.sin(f*0.35+k)*5);a.style.transform=`rotate(${b+(k?-w:w)}deg)`});
  if(+el.dataset.jump){const y=-Math.abs(Math.sin(f*0.55))*38;el.style.translate=`0px ${y}px`}
  const bl=(f+i*7+15)%40<2; el.querySelector('.eyes').style.transform=bl?'scaleY(0.12)':'none'; el.querySelector('.eyes').style.transformOrigin='100px 86px';
 });
 document.querySelectorAll('.conf').forEach((c,i)=>{const [a,b]=c.dataset.cg.split('.').map(Number);const d=t-GT(a,b);
  const yy=+c.dataset.y+d*(+c.dataset.v);if(d<0||yy>1010){c.style.opacity=0;return}
  c.style.opacity=1;c.style.left=(+c.dataset.x+Math.sin(d*3+i)*30)+'px';c.style.top=(+c.dataset.y+d*(+c.dataset.v))+'px';c.style.transform=`rotate(${d*(+c.dataset.r)}deg)`});
}
'''
