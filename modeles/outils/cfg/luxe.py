"""Shared building blocks for the 'nuit & or' (luxe) style, modelled on Badr's reference video."""
BASE = 'base_luxe.css'
SFX = 'sfx_luxe_template.py'
JS = 'const CAM=0.45, PUSH=0.012;'
GAP = 0.32
TAIL = 1.6
MINLEN = 1.6


def hud(place, tag):
    return f'''  <div id="hud"><div class="c tl"></div><div class="c tr"></div><div class="c bl"></div><div class="c br"></div>
   <div class="l"><span id="rec"></span>REC · CAM 01<small>{place}</small></div><div class="r"><span id="tm">00:00.00</span><small>{tag}</small></div></div>'''


def head(top, lines):
    """lines: list of (cls, text, group or None). group None => visible from frame 1 (hook)."""
    out = []
    for cls, txt, g in lines:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        out.append(f'<div class="{cls}"{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


GUY = '''<svg class="abs" style="left:{x}px;top:{y}px" width="330" height="400" viewBox="0 0 330 400">
 <path d="M30 400 Q40 270 165 255 Q290 270 300 400 Z" fill="#2f5aa8"/>
 <path d="M95 268 Q165 330 235 268" fill="none" stroke="#24478a" stroke-width="10"/>
 <line x1="140" y1="300" x2="136" y2="350" stroke="#e8e8f0" stroke-width="5" stroke-linecap="round"/><line x1="190" y1="300" x2="194" y2="350" stroke="#e8e8f0" stroke-width="5" stroke-linecap="round"/>
 <rect x="145" y="220" width="40" height="45" fill="#e9b88f"/>
 <ellipse cx="78" cy="150" rx="18" ry="24" fill="#f3c9a2"/><ellipse cx="252" cy="150" rx="18" ry="24" fill="#f3c9a2"/>
 <ellipse cx="165" cy="140" rx="88" ry="98" fill="#f3c9a2"/>
 <path d="M75 125 Q70 40 165 38 Q262 40 255 125 Q240 80 205 78 Q170 95 120 80 Q90 92 75 125 Z" fill="#4a2e1c"/>
 <g class="brow"><path d="M108 98 Q128 84 148 96" stroke="#4a2e1c" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M182 96 Q202 84 222 98" stroke="#4a2e1c" stroke-width="7" fill="none" stroke-linecap="round"/></g>
 <circle cx="128" cy="135" r="27" fill="rgba(255,255,255,.35)" stroke="#2a2a2a" stroke-width="6"/><circle cx="202" cy="135" r="27" fill="rgba(255,255,255,.35)" stroke="#2a2a2a" stroke-width="6"/>
 <line x1="155" y1="135" x2="175" y2="135" stroke="#2a2a2a" stroke-width="6"/>
 <circle cx="128" cy="137" r="7" fill="#1c1c1c"/><circle cx="202" cy="137" r="7" fill="#1c1c1c"/>
 <path d="M145 195 Q165 207 185 195" stroke="#a5523f" stroke-width="6" fill="none" stroke-linecap="round"/>
 <ellipse cx="165" cy="198" rx="17" ry="23" fill="#7a2626" data-g="{gshock}" data-fx="pop"/>
 <path d="M262 70 Q252 92 262 100 Q272 92 262 70 Z" fill="#7ec8f2" data-g="{gshock}" data-fx="up"/>
</svg>'''


def counter_scene(sid, sign, sub, total, bubble, gshock, gbubble, strip_txt):
    return f'''  <div class="scene" data-s="{sid}">
   <div class="wall"></div><div class="lamp" style="left:120px;top:900px"></div><div class="lamp" style="left:520px;top:880px"></div><div class="lamp" style="left:930px;top:900px"></div>
   <div class="sign gold">{sign}<small>{sub}</small></div>
   {GUY.format(x=70, y=840, g0=gshock, gshock=gshock)}
   <div class="abs" style="left:440px;top:1196px;width:180px;height:30px;border-radius:50%;background:#f4f1ea"></div><div class="abs" style="left:500px;top:1170px;width:40px;height:40px;border-radius:50%;background:#8bd450"></div>
   <div class="counter"></div>
   <div class="reg"><div class="scr">{total}</div><div class="body"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div>
   <div class="bubble" style="left:420px;top:880px" data-g="{gbubble}" data-fx="pop">{bubble}</div>
   <div class="strip" data-g="{gbubble}" data-fx="growY">{strip_txt}</div>
  </div>'''
