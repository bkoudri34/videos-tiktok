"""Briques du style T « Tuto illustré » (fond papier, dessins au trait, annotations au feutre rouge) : à importer dans cfg/<nom>.py.
Sous-titres mot par mot via #sub (les textes de LINES sont affichés : <em> = surligneur jaune, <i> = rouge)."""
BASE = 'base_tuto.css'
SFX = 'sfx_luxe_template.py'
JS = 'const CAM=0.6, PUSH=0.010;'
GAP = 0.3
TAIL = 2.2
MINLEN = 1.8
ROOT = ':root{--bg:#faf9f6}'


def title(html, top=220, g=None, size=None):
    a = f' data-g="{g}" data-fx="pop"' if g else ''
    s = f'top:{top}px' + (f';font-size:{size}px' if size else '')
    return f'<div class="ttl" style="{s}"{a}>{html}</div>'


def svg(x, y, w, h, inner, cls='ink', vb=None):
    vb = vb or f'0 0 {w} {h}'
    return f'<svg class="abs {cls}" style="left:{x}px;top:{y}px;overflow:visible" width="{w}" height="{h}" viewBox="{vb}">{inner}</svg>'


def circle(x, y, w, h, g, rot=-4):
    """Cercle au feutre rouge qui se trace (ellipse un peu tremblée)."""
    d = f'M{w*0.08} {h*0.55} C{w*0.05} {h*0.1},{w*0.85} {-h*0.05},{w*0.97} {h*0.45} C{w*1.02} {h*0.9},{w*0.2} {h*1.05},{w*0.06} {h*0.62} L{w*0.12} {h*0.4}'
    return svg(x, y, w, h, f'<path class="dr" pathLength="1" d="{d}" data-g="{g}" data-fx="draw" style="transform:rotate({rot}deg)"/>', 'red')


def arrow(x, y, w, h, d, g):
    """Flèche au feutre : d = chemin du trait, la pointe est ajoutée en fin de chemin par l'appelant si besoin."""
    return svg(x, y, w, h, f'<path class="dr" pathLength="1" d="{d}" data-g="{g}" data-fx="draw"/>', 'red')


def underline2(x, y, w, g):
    return svg(x, y, w, 40, f'<path class="dr" pathLength="1" d="M0 8 Q{w/2} 0 {w} 10" data-g="{g}" data-fx="draw"/><path class="dr" pathLength="1" d="M10 30 Q{w/2} 22 {w-6} 32" data-g="{g}" data-fx="draw"/>', 'red')


GUY = '''<g class="ink"><circle cx="120" cy="80" r="56"/><path d="M98 72 l0 6 M142 72 l0 6"/><path d="M100 108 Q120 120 140 108"/>
 <path d="M120 136 L120 330"/><path d="M120 330 L70 460 M120 330 L170 460"/><path d="M120 190 L40 270"/><path d="M120 190 L230 170"/></g>'''

HANDSTOP = '''<g class="ink"><path d="M60 250 L60 120 Q60 100 78 100 Q96 100 96 120 L96 60 Q96 40 114 40 Q132 40 132 60 L132 50 Q132 30 150 30 Q168 30 168 50 L168 64 Q168 46 186 46 Q204 46 204 66 L204 190 Q204 260 140 270 L100 270 Q60 268 60 250 Z" style="fill:#fff"/>
 <path d="M96 120 L96 170 M132 60 L132 160 M168 64 L168 160"/></g>'''
