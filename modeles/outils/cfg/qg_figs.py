from tuto import svg
"""Briques communes des vidéos QG en style T « tuto illustré » : bonshommes au trait qui bougent (bras, rebond),
téléphone dessiné, bulles. À importer après `from tuto import *`. Les animations « vivantes » passent par extra(t)."""

MOUTH = {
    'smile': '<path d="M100 104 Q120 124 140 104"/>',
    'sad': '<path d="M100 118 Q120 102 140 118"/>',
    'open': '<ellipse cx="120" cy="112" rx="14" ry="16"/>',
    'flat': '<path d="M102 112 L138 112"/>',
}
HAIR = {
    'none': '',
    'cap': '<path d="M64 66 Q120 0 176 66 Z" style="fill:#111"/><path d="M168 64 L222 70"/>',
    'spiky': '<path d="M70 52 L80 22 L96 44 L110 14 L124 40 L140 12 L150 42 L166 24 L170 56"/>',
    'bun': '<path d="M66 70 Q70 26 120 24 Q170 26 174 70"/><circle cx="120" cy="14" r="18"/>',
    'curly': '<path d="M66 60 q8 -22 22 -10 q6 -24 26 -12 q12 -20 28 -4 q18 -14 26 12 q14 4 6 24"/>',
}


def guy(x, y, hair='none', mouth='smile', arms='down', scale=1.0, g=None, fx='up', mirror=False, extra_svg=''):
    """Bonhomme au trait (240x470 à l'échelle 1). arms: down | up | point | hip | shrug."""
    A = {
        'down': ('M120 190 L60 300', 'M120 190 L180 300'),
        'up': ('M120 190 L50 90', 'M120 190 L190 90'),
        'point': ('M120 190 L50 290', 'M120 190 L240 160'),
        'hip': ('M120 190 L70 240 L110 290', 'M120 190 L170 240 L130 290'),
        'shrug': ('M120 190 L50 170 L30 120', 'M120 190 L190 170 L210 120'),
    }[arms]
    w, h = int(240 * scale), int(470 * scale)
    flip = ' style="transform:scaleX(-1);transform-origin:120px 235px"' if mirror else ''
    inner = (f'<g class="ink live"{flip}><circle cx="120" cy="80" r="56" style="fill:#fff"/>{HAIR[hair]}'
             f'<path d="M98 72 l0 8 M142 72 l0 8"/>{MOUTH[mouth]}'
             f'<path d="M120 136 L120 330"/><path d="M120 330 L72 460 M120 330 L168 460"/>'
             f'<g class="armL"><path d="{A[0]}"/></g><g class="armR"><path d="{A[1]}"/></g>{extra_svg}</g>')
    s = svg(x, y, w, h, inner, 'ink', '0 0 240 470')
    if g:
        s = s.replace('class="abs ink"', f'class="abs ink" data-g="{g}" data-fx="{fx}"', 1)
    return s


def bubble(x, y, w, html, g, tail='left', size=46, rot=-2):
    t = 'left:60px' if tail == 'left' else 'right:60px'
    return (f'<div class="bub" style="left:{x}px;top:{y}px;width:{w}px;font-size:{size}px;transform:rotate({rot}deg)" '
            f'data-g="{g}" data-fx="pop">{html}<i class="tl" style="{t}"></i></div>')


FIGCSS = '''
.bub{position:absolute;background:#fff;border:6px solid #111;border-radius:34px;padding:22px 28px;font-weight:900;font-family:Inter;text-align:center;line-height:1.1;box-shadow:8px 9px 0 #111}
.bub .tl{position:absolute;bottom:-34px;width:40px;height:40px;background:#fff;border-right:6px solid #111;border-bottom:6px solid #111;transform:rotate(45deg) skew(10deg,10deg)}
.bub em{font-style:normal;background:#ffe14d;padding:0 8px}
.bub b{color:#e63946}
.phone{position:absolute;width:440px;height:800px;border:9px solid #111;border-radius:64px;background:#fff;box-shadow:12px 14px 0 #111;overflow:hidden}
.phone:before{content:'';position:absolute;left:150px;top:18px;width:120px;height:26px;border-radius:13px;background:#111}
.phone .scr{position:absolute;left:34px;right:34px;top:80px;font-family:Inter}
.phone .tt{font:900 40px Inter;margin-bottom:22px}
.phone .ln{height:26px;border-radius:13px;background:#e9e5dc;margin:14px 0}
.phone .bt{height:96px;border-radius:48px;background:#111;color:#fff;font:900 34px Inter;display:flex;align-items:center;justify-content:center;margin-top:26px;white-space:nowrap}
.phone .fl{height:90px;border:5px solid #111;border-radius:18px;display:flex;align-items:center;padding:0 18px;font:800 30px Inter;white-space:nowrap;margin-top:14px}
.tag{position:absolute;font:900 38px Inter;letter-spacing:1px;padding:8px 22px;border:5px solid #111;border-radius:16px;background:#fff;white-space:nowrap}
.cond{position:absolute;left:110px;width:820px;font:600 25px/1.35 Inter;color:#444;text-align:center}
.endc{position:absolute;left:110px;top:240px;width:820px;padding:40px 30px 36px;border:7px solid #111;border-radius:40px;background:#fff;text-align:center;box-shadow:12px 14px 0 #111}
.endc .k{font:900 46px Inter}
.endc .c{display:inline-block;margin:14px 0;font:900 100px Inter;background:#ffe14d;padding:0 22px;line-height:1.15}
.endc .d{font:800 40px Inter}
.endc .b{margin-top:18px;display:inline-block;padding:12px 30px;border-radius:30px;background:#111;color:#fff;font:800 32px Inter}
'''

# Bonshommes vivants : léger rebond + bras qui bougent (calé sur le temps t de la vidéo)
FIGJS = '''
const LIVE=[...document.querySelectorAll('.live')];
function extra(t){LIVE.forEach((g,i)=>{const p=i*1.7;
 const al=g.querySelector('.armL'),ar=g.querySelector('.armR');
 g.parentNode.style.translate=`0 ${Math.sin(t*5.2+p)*7}px`;
 if(al){al.style.transformOrigin='100% 0%';al.style.transformBox='fill-box';al.style.transform=`rotate(${Math.sin(t*4.1+p)*7}deg)`}
 if(ar){ar.style.transformOrigin='0% 0%';ar.style.transformBox='fill-box';ar.style.transform=`rotate(${Math.sin(t*3.6+p+1)*9}deg)`}
});}
'''
