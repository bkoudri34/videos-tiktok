"""Briques du style A « Alerte stickers » (repéré chez @hacooultra14 le 22/11/2026 ; on ne reprend que la mise en scène) : à importer dans cfg/<nom>.py.
Papier crème à points + gribouillis roses, étiquette de rubrique jaune (tag), compte à rebours en haut à droite (#cd),
bandeaux noirs / rouges / jaunes / verts (ban), dessins plats façon autocollants (stk + dessins ci-dessous), sous-titres karaoké :
écris les groupes de LINES avec kara("tu risques <em>de</em>") -> pavés noirs, <em> = pavé jaune, <i> = pavé rouge.
Exemple complet : cfg/hacoo_alerte1.py."""
import re
BASE = 'base_alerte.css'
SFX = 'sfx_luxe_template.py'
GAP = 0.22
TAIL = 2.2
MINLEN = 1.6
ROOT = ':root{--bg:#f3ece0}'
JS = '''const CAM=0.45, PUSH=0.008;
function extra(t){const cd=document.getElementById('cd');if(cd){const r=Math.max(0,Math.ceil(END-t));cd.textContent=Math.floor(r/60)+':'+String(r%60).padStart(2,'0');}
 document.querySelectorAll('.dood span').forEach((s,k)=>{s.style.transform=`translate(${Math.sin(t*0.7+k)*10}px,${Math.cos(t*0.55+k*1.7)*12}px) rotate(${(k%2?1:-1)*(12+Math.sin(t*0.4+k)*6)}deg)`});
 document.querySelectorAll('[data-wob]').forEach((s,k)=>{s.style.rotate=(Math.sin(t*2.2+k)*2.2)+'deg'});}'''


def kara(s):
    """« tu risques <em>de</em> » -> chaque mot dans un pavé noir, <em>/<i> gardés (pavé jaune / rouge)."""
    out = []
    for m in re.finditer(r'<(em|i)>.*?</\1>|\S+', s):
        w = m.group(0)
        if out and re.fullmatch(r'[.,:;!?…]+', w):  # ponctuation seule : collée au pavé précédent
            out[-1] = re.sub(r'(</(?:b|em|i)>)$', lambda m: (' ' if w[0] in ':;!?' else '') + w + m.group(1), out[-1]); continue
        out.append(w if w.startswith('<') else f'<b>{w}</b>')
    return ' '.join(out)


DOODLES = [('%', 60, 330), ('€', 900, 300), ('★', 820, 640), ('%', 70, 900), ('☾', 930, 1000), ('€', 120, 1560), ('★', 860, 1620), ('%', 640, 1760), ('☾', 300, 470)]


def chrome():
    """Fond de gribouillis + compte à rebours : à mettre une fois au début de BODY."""
    d = ''.join(f'<span style="left:{x}px;top:{y}px">{c}</span>' for c, x, y in DOODLES)
    return f'<div class="dood">{d}</div><div id="cd">0:30</div>'


def tag(txt):
    return f'<div class="tag">{txt}</div>'


def ban(txt, top, cls='', g=None, fx='pop', rot=-2, size=None):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    s = f';font-size:{size}px' if size else ''
    return f'<div class="ban {cls}" style="top:{top}px"{a}><b style="transform:rotate({rot}deg){s}">{txt}</b></div>'


def stk(x, y, w, h, inner, g=None, fx='pop', vb=None, wob=True):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    vb = vb or f'0 0 {w} {h}'
    wb = ' data-wob="1"' if wob else ''
    return f'<div class="stk" style="left:{x}px;top:{y}px"{a}{wb}><svg width="{w}" height="{h}" viewBox="{vb}">{inner}</svg></div>'


# ---- dessins (viewBox 0 0 400 400 sauf mention) ----
PADLOCK = '''<path d="M125 200 V135 Q125 55 200 55 Q275 55 275 135 V200" fill="none" stroke="#141414" stroke-width="58" stroke-linecap="round"/>
<path d="M125 200 V135 Q125 55 200 55 Q275 55 275 135 V200" fill="none" stroke="#c9d0d8" stroke-width="38" stroke-linecap="round"/>
<path d="M112 128 Q118 80 160 66" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round" opacity=".8"/>
<rect class="ol" x="70" y="175" width="260" height="200" rx="36" fill="#ffcc33"/>
<path d="M78 300 H322 V340 Q322 367 295 367 H105 Q78 367 78 340 Z" fill="#f0a900"/>
<rect class="ol" x="70" y="175" width="260" height="200" rx="36" fill="none"/>
<circle cx="200" cy="250" r="26" fill="#141414"/><path d="M186 258 L178 318 H222 L214 258 Z" fill="#141414"/>
<path d="M96 200 H170" stroke="#fff6c9" stroke-width="12" stroke-linecap="round"/>'''

TEE = '<path class="ol" d="M120 70 L170 48 Q200 80 230 48 L280 70 L335 130 L292 165 L280 152 L280 330 L120 330 L120 152 L108 165 L65 130 Z" fill="{c}"/><path d="M170 48 Q200 92 230 48" fill="none" class="ol"/>'


def tee(c='#5fb3ff'):
    return TEE.format(c=c)


def avatar(cx, cy, skin, hair, mouth='smile'):
    m = {'smile': f'M{cx-18} {cy+18} Q{cx} {cy+34} {cx+18} {cy+18}', 'flat': f'M{cx-16} {cy+24} H{cx+16}', 'sad': f'M{cx-18} {cy+30} Q{cx} {cy+16} {cx+18} {cy+30}'}[mouth]
    return (f'<circle class="ol" cx="{cx}" cy="{cy}" r="58" fill="{skin}"/>'
            f'<path class="ol" d="M{cx-58} {cy-4} Q{cx-60} {cy-62} {cx} {cy-60} Q{cx+60} {cy-62} {cx+58} {cy-4} Q{cx+30} {cy-34} {cx} {cy-30} Q{cx-34} {cy-34} {cx-58} {cy-4} Z" fill="{hair}"/>'
            f'<circle cx="{cx-20}" cy="{cy+2}" r="7" fill="#141414"/><circle cx="{cx+20}" cy="{cy+2}" r="7" fill="#141414"/>'
            f'<path d="{m}" fill="none" stroke="#141414" stroke-width="7" stroke-linecap="round"/>')


def banned(cx, cy, g):
    return (f'<g data-g="{g}" data-fx="stamp"><circle cx="{cx}" cy="{cy}" r="66" fill="rgba(238,59,59,.22)" stroke="#ee3b3b" stroke-width="14"/>'
            f'<path d="M{cx-46} {cy+46} L{cx+46} {cy-46}" stroke="#ee3b3b" stroke-width="14" stroke-linecap="round"/></g>')


BOX = '''<path class="ol" d="M70 190 L200 150 L330 190 L330 345 L200 385 L70 345 Z" fill="#d79a5c"/>
<path class="ol" d="M200 230 L200 385 M70 190 L200 230 L330 190" fill="none"/>
<path class="ol" d="M70 190 L30 245 L160 285 L200 230 Z" fill="#e8b27a"/><path class="ol" d="M330 190 L370 245 L240 285 L200 230 Z" fill="#c4874a"/>
<path d="M120 300 L170 315" stroke="#fff" stroke-width="10" stroke-linecap="round" opacity=".55"/>'''

GUY = '''<path class="ol" d="M70 520 Q70 400 200 392 Q330 400 330 520 Z" fill="#f2c59a"/>
<path class="ol" d="M88 300 Q200 270 312 300 L322 418 Q200 440 78 418 Z" fill="#2fa35a"/>
<path class="ol" d="M88 300 L40 380 L72 400 L100 352" fill="#2fa35a"/><path class="ol" d="M312 300 L360 380 L328 400 L300 352" fill="#2fa35a"/>
<ellipse cx="200" cy="476" rx="9" ry="6" fill="#141414"/>
<circle class="ol" cx="200" cy="170" r="92" fill="#f2c59a"/>
<path class="ol" d="M108 160 Q104 70 200 70 Q296 70 292 160 Q262 118 200 122 Q140 118 108 160 Z" fill="#3b2a20"/>
<circle cx="168" cy="178" r="9" fill="#141414"/><circle cx="232" cy="178" r="9" fill="#141414"/>
<path d="M176 222 Q200 210 224 222" fill="none" stroke="#141414" stroke-width="8" stroke-linecap="round"/>
<path d="M150 150 L184 160 M250 150 L216 160" stroke="#141414" stroke-width="8" stroke-linecap="round"/>'''

ARROWS_IN = '''<path d="M0 360 H62 M40 336 L66 360 L40 384" fill="none" stroke="#ee3b3b" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M400 360 H338 M360 336 L334 360 L360 384" fill="none" stroke="#ee3b3b" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>'''

TAPE = '''<path class="ol" d="M40 60 H360 V140 H40 Z" fill="#ffd84a"/>
<path d="M80 60 V95 M120 60 V82 M160 60 V95 M200 60 V82 M240 60 V95 M280 60 V82 M320 60 V95" stroke="#141414" stroke-width="7" stroke-linecap="round"/>'''

BOOKMARK = '<path class="ol" d="M60 20 H200 Q220 20 220 40 V300 L130 240 L40 300 V40 Q40 20 60 20 Z" fill="#ff8a2a"/><path d="M80 50 V200" stroke="#ffc08a" stroke-width="12" stroke-linecap="round"/>'


def red_circle(x, y, w, h, g, rot=-3):
    d = f'M{w*0.07} {h*0.55} C{w*0.04} {h*0.08},{w*0.86} {-h*0.04},{w*0.97} {h*0.45} C{w*1.02} {h*0.92},{w*0.2} {h*1.06},{w*0.05} {h*0.62} L{w*0.11} {h*0.38}'
    return (f'<svg class="abs" style="left:{x}px;top:{y}px;overflow:visible;z-index:5" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<path pathLength="1" d="{d}" fill="none" stroke="#ee3b3b" stroke-width="11" stroke-linecap="round" style="stroke-dasharray:1;stroke-dashoffset:1;transform:rotate({rot}deg)" data-g="{g}" data-fx="draw"/></svg>')
