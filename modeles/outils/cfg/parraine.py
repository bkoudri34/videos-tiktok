"""Briques du 26/11/2026 (règles anti-bannissement de Badr) pour les vidéos parrainage v3 nuit & or :
bandeau de mentions visible pendant toute la vidéo, mascotte dessinée (jamais de vraie personne), amis, schéma « un seul niveau ».
Aucun montant écrit à l'image."""
from luxe import *

BANNER = '''  <div class="ment"><b>Lien de parrainage : je touche une prime</b><span>Offre soumise à conditions</span></div>'''

PCSS = '''
.ment{position:absolute;left:150px;top:1436px;width:760px;padding:12px 20px;border-radius:22px;background:rgba(8,8,10,.82);border:2px solid rgba(255,255,255,.35);text-align:center;z-index:6;line-height:1.3}
.ment b{display:block;font:800 26px Inter;color:#fff;white-space:nowrap}
.ment span{display:block;font:600 22px Inter;color:#cfc8ba;white-space:nowrap}
.card2{position:absolute;border-radius:34px;background:rgba(18,16,22,.92);border:3px solid var(--ac);box-shadow:0 24px 70px rgba(0,0,0,.6);padding:30px 38px;color:#f3efe6}
.card2 .t{font:900 40px Inter;letter-spacing:1px;color:var(--ac);white-space:nowrap;text-transform:uppercase}
.chk{font:700 34px Inter;margin-top:16px;white-space:nowrap}
.chk i{font-style:normal;display:inline-block;width:46px;height:46px;border-radius:50%;background:var(--ac);color:#111;text-align:center;line-height:46px;font:900 28px Inter;margin-right:16px;vertical-align:2px}
.num{position:absolute;width:150px;height:150px;border-radius:50%;border:5px solid #e0ac55;background:radial-gradient(circle,#2a1f10,#0b0906);display:flex;align-items:center;justify-content:center;font:900 92px 'DejaVu Serif',serif;color:#f3c766;box-shadow:0 0 40px rgba(240,180,80,.45)}
.tagp{position:absolute;padding:14px 30px;border-radius:40px;background:var(--ac);color:#111;font:900 34px Inter;white-space:nowrap}
.lnk2{position:absolute;height:6px;background:linear-gradient(90deg,#e0ac55,var(--ac));transform-origin:0 50%;border-radius:3px}
.x{position:absolute;font:900 90px Inter;color:#ff5a5a;text-shadow:0 0 20px rgba(255,60,60,.6)}
.grey{filter:grayscale(1) brightness(.55)}
.bubble2{position:absolute;background:#fff;color:#141414;border-radius:30px;padding:20px 30px;font:800 34px Inter;white-space:nowrap}
'''


def mascot(x, y, s, body, acc='scarf', g=None, fx='pop', cls=''):
    """Mascotte ronde générique (pas de personnage connu). acc : 'scarf' | 'cap' | 'bow' | 'glasses'."""
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    extra = {
        'scarf': '<path d="M50 150 Q100 175 150 150 L150 168 Q100 192 50 168 Z" fill="#f3c766"/><rect x="128" y="160" width="18" height="40" rx="6" fill="#f3c766"/>',
        'cap': '<path d="M44 70 Q100 18 156 70 Z" fill="#f3c766"/><rect x="100" y="60" width="78" height="12" rx="6" fill="#f3c766"/>',
        'bow': '<path d="M100 40 L70 22 L72 58 Z M100 40 L130 22 L128 58 Z" fill="#f3c766"/><circle cx="100" cy="40" r="9" fill="#e0ac55"/>',
        'glasses': '<circle cx="78" cy="100" r="20" fill="none" stroke="#f3c766" stroke-width="6"/><circle cx="122" cy="100" r="20" fill="none" stroke="#f3c766" stroke-width="6"/><line x1="98" y1="100" x2="102" y2="100" stroke="#f3c766" stroke-width="6"/>',
    }[acc]
    return f'''<svg class="abs {cls}" style="left:{x}px;top:{y}px" width="{s}" height="{s}" viewBox="0 0 200 200"{a}>
 <ellipse cx="100" cy="192" rx="62" ry="8" fill="rgba(0,0,0,.45)"/>
 <path d="M38 120 Q38 46 100 46 Q162 46 162 120 L162 160 Q162 186 136 186 L64 186 Q38 186 38 160 Z" fill="{body}"/>
 <circle cx="78" cy="100" r="11" fill="#141414"/><circle cx="122" cy="100" r="11" fill="#141414"/>
 <circle cx="82" cy="96" r="4" fill="#fff"/><circle cx="126" cy="96" r="4" fill="#fff"/>
 <path d="M80 130 Q100 146 120 130" stroke="#141414" stroke-width="6" fill="none" stroke-linecap="round"/>
 <circle cx="62" cy="124" r="9" fill="rgba(255,140,140,.45)"/><circle cx="138" cy="124" r="9" fill="rgba(255,140,140,.45)"/>
 {extra}
</svg>'''


def friend(x, y, s, col, g=None, cls='', fx='pop'):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    return f'''<svg class="abs {cls}" style="left:{x}px;top:{y}px" width="{s}" height="{s}" viewBox="0 0 100 100"{a}>
 <circle cx="50" cy="50" r="48" fill="rgba(255,255,255,.06)" stroke="{col}" stroke-width="3"/>
 <circle cx="50" cy="38" r="16" fill="{col}"/><path d="M20 84 Q22 58 50 58 Q78 58 80 84 Z" fill="{col}"/></svg>'''


def link(x1, y1, x2, y2, g=None):
    import math
    L = math.hypot(x2 - x1, y2 - y1); ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
    a = f' data-g="{g}" data-fx="grow"' if g else ''
    return f'<div style="position:absolute;left:{x1}px;top:{y1}px;width:{L:.0f}px;height:6px;transform-origin:0 50%;transform:rotate({ang:.1f}deg)"><div class="lnk2" style="left:0;top:0;width:100%;transform-origin:0 50%"{a}></div></div>'


def hdx(top, items, left=90, width=840):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px;left:{left}px;width:{width}px">' + ''.join(out) + '</div>'
