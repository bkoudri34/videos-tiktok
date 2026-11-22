"""Briques du style X « Explainer mascotte » (vidéos QG, construit le 22/11/2026, style envoyé par Badr le 22/11).
Mécanique reprise (pas l'identité visuelle) d'un explainer « pourquoi une banque te paie » : une mascotte qui réagit,
des icônes plates qui surgissent en rebond, un sous-titre court en pastille, une relance en bulle de BD, une fin en fausse
conversation de messagerie. Identité htm.invest : fond anthracite chaud + points dorés, or #d4af37, blanc cassé, Anton.
Mascotte maison : « Sou », une pièce dorée avec des yeux, des sourcils, une bouche et de petits bras (prénom gravé).
À importer dans cfg/qg_<sujet><n>.py : `from qg_explainer import *`.
Animations vivantes (clignement, sourcils, rebond, saut de joie, bras qui pointent) dans extra(t) : data-anim="idle|jump|talk",
data-brow="up" pour hausser les sourcils."""
BASE = 'qg_explainer.css'
SFX = 'qg_sfx_ecran_template.py'
GAP = 0.25
TAIL = 1.5
MINLEN = 1.6
ROOT = ':root{--bg:#0d0b09}'

ARMS = {
    'down': ('M48 170 Q14 200 6 236', 'M252 170 Q286 200 294 236', (6, 236), (294, 236)),
    'up': ('M48 160 Q10 120 4 70', 'M252 160 Q290 120 296 70', (4, 70), (296, 70)),
    'point': ('M48 170 Q14 200 6 236', 'M252 150 Q300 120 340 96', (6, 236), (340, 96)),
    'pointl': ('M48 150 Q0 120 -40 96', 'M252 170 Q286 200 294 236', (-40, 96), (294, 236)),
    'hip': ('M50 180 Q10 190 30 240', 'M250 180 Q290 190 270 240', (30, 240), (270, 240)),
}
MOUTHS = {
    'smile': '<path d="M112 178 Q150 214 188 178" style="fill:none;stroke:#16130f;stroke-width:9;stroke-linecap:round"/>',
    'open': '<path d="M114 176 Q150 236 186 176 Z" style="fill:#16130f"/><path d="M130 200 Q150 220 170 200 Z" style="fill:#e0633f"/>',
    'o': '<ellipse cx="150" cy="192" rx="17" ry="21" style="fill:#16130f"/>',
    'flat': '<path d="M122 190 L178 190" style="fill:none;stroke:#16130f;stroke-width:9;stroke-linecap:round"/>',
}


def mascot(x, y, scale=1.0, mouth='smile', arms='down', anim='idle', brow='', g=None, fx='pop', name='SOU'):
    """Sou, la pièce mascotte (300x330 à l'échelle 1)."""
    al, ar, hl, hr = ARMS[arms]
    w, h = int(300 * scale), int(330 * scale)
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    inner = (
        '<defs><radialGradient id="cg" cx="38%" cy="30%" r="75%"><stop offset="0" stop-color="#fff0b3"/>'
        '<stop offset=".45" stop-color="#e3bf4c"/><stop offset="1" stop-color="#9c7716"/></radialGradient></defs>'
        '<g class="mb">'
        f'<g class="armL"><path d="{al}" style="fill:none;stroke:#e3bf4c;stroke-width:16;stroke-linecap:round"/>'
        f'<circle cx="{hl[0]}" cy="{hl[1]}" r="17" style="fill:#f4efe4;stroke:#9c7716;stroke-width:4"/></g>'
        f'<g class="armR"><path d="{ar}" style="fill:none;stroke:#e3bf4c;stroke-width:16;stroke-linecap:round"/>'
        f'<circle cx="{hr[0]}" cy="{hr[1]}" r="17" style="fill:#f4efe4;stroke:#9c7716;stroke-width:4"/></g>'
        '<path d="M118 268 L112 300 M182 268 L188 300" style="stroke:#9c7716;stroke-width:12;stroke-linecap:round"/>'
        '<ellipse cx="104" cy="306" rx="26" ry="12" style="fill:#16130f"/><ellipse cx="196" cy="306" rx="26" ry="12" style="fill:#16130f"/>'
        '<circle cx="150" cy="150" r="126" style="fill:url(#cg);stroke:#8a6a12;stroke-width:9"/>'
        '<circle cx="150" cy="150" r="102" style="fill:none;stroke:rgba(138,106,18,.55);stroke-width:5;stroke-dasharray:4 9"/>'
        f'<text x="150" y="252" text-anchor="middle" style="font:400 34px Anton;letter-spacing:6px;fill:#8a6a12">{name}</text>'
        '<g class="brows"><path d="M94 92 Q116 78 138 90" style="fill:none;stroke:#16130f;stroke-width:9;stroke-linecap:round"/>'
        '<path d="M162 90 Q184 78 206 92" style="fill:none;stroke:#16130f;stroke-width:9;stroke-linecap:round"/></g>'
        '<g class="eyes"><ellipse cx="116" cy="130" rx="23" ry="27" style="fill:#fff"/><ellipse cx="184" cy="130" rx="23" ry="27" style="fill:#fff"/>'
        '<circle cx="120" cy="134" r="12" style="fill:#16130f"/><circle cx="188" cy="134" r="12" style="fill:#16130f"/>'
        '<circle cx="124" cy="129" r="4" style="fill:#fff"/><circle cx="192" cy="129" r="4" style="fill:#fff"/></g>'
        f'<g class="mouth">{MOUTHS[mouth]}</g>'
        '<ellipse cx="96" cy="176" rx="14" ry="8" style="fill:rgba(224,99,63,.35)"/><ellipse cx="204" cy="176" rx="14" ry="8" style="fill:rgba(224,99,63,.35)"/>'
        '</g>')
    return (f'<svg class="abs masc" data-anim="{anim}" data-brow="{brow}" style="left:{x}px;top:{y}px;overflow:visible" '
            f'width="{w}" height="{h}" viewBox="0 0 300 330"{a}>{inner}</svg>')


ICONS = {
    'bank': '<path class="f" d="M100 14 L190 62 L10 62 Z"/><rect class="f" x="14" y="66" width="172" height="14" rx="4"/>'
            '<rect class="w" x="30" y="88" width="22" height="70" rx="4"/><rect class="w" x="68" y="88" width="22" height="70" rx="4"/>'
            '<rect class="w" x="110" y="88" width="22" height="70" rx="4"/><rect class="w" x="148" y="88" width="22" height="70" rx="4"/>'
            '<rect class="f" x="10" y="164" width="180" height="20" rx="5"/><circle class="d" cx="100" cy="44" r="10"/>',
    'tv': '<path class="sk" d="M70 20 L100 48 L130 20"/><rect class="w" x="10" y="48" width="180" height="124" rx="22"/>'
          '<rect class="d" x="26" y="62" width="148" height="96" rx="12"/><path class="f" d="M86 86 L124 110 L86 134 Z"/>'
          '<rect class="w" x="60" y="176" width="80" height="12" rx="6"/>',
    'pub': '<rect class="w" x="40" y="130" width="14" height="62" rx="5"/><rect class="w" x="146" y="130" width="14" height="62" rx="5"/>'
           '<rect class="f" x="6" y="22" width="188" height="116" rx="16"/><rect class="d" x="18" y="34" width="164" height="92" rx="10"/>'
           '<text x="100" y="108" text-anchor="middle" style="font:400 70px Anton;fill:#d4af37;letter-spacing:3px">PUB</text>',
    'phone': '<rect class="w" x="46" y="6" width="108" height="188" rx="22"/><rect class="d" x="56" y="24" width="88" height="148" rx="12"/>'
             '<path class="f" d="M100 54 l10 22 24 3 -18 16 5 24 -21 -12 -21 12 5 -24 -18 -16 24 -3z"/>'
             '<path class="r" d="M100 158 C88 146 76 140 82 132 C86 126 96 128 100 136 C104 128 114 126 118 132 C124 140 112 146 100 158Z"/>',
    'bill': '<rect class="g" x="8" y="50" width="184" height="100" rx="14" style="fill:#2f9e5c"/><rect x="20" y="62" width="160" height="76" rx="10" style="fill:none;stroke:#bff0cf;stroke-width:5"/>'
            '<circle cx="100" cy="100" r="28" style="fill:#bff0cf"/><text x="100" y="114" text-anchor="middle" style="font:400 40px Anton;fill:#1d6b3e">€</text>',
    'card': '<rect class="f" x="8" y="40" width="184" height="120" rx="18"/><rect class="d" x="8" y="64" width="184" height="24"/>'
            '<rect class="w" x="26" y="104" width="38" height="28" rx="6"/><rect class="d" x="110" y="130" width="64" height="10" rx="5"/>',
    'piggy': '<ellipse class="f" cx="96" cy="108" rx="78" ry="60"/><path class="f" d="M60 60 L72 26 L94 54 Z"/>'
             '<rect class="f" x="40" y="150" width="22" height="34" rx="8"/><rect class="f" x="120" y="150" width="22" height="34" rx="8"/>'
             '<ellipse cx="172" cy="108" rx="20" ry="24" style="fill:#e3bf4c;stroke:#8a6a12;stroke-width:4"/><circle class="d" cx="168" cy="100" r="4"/><circle class="d" cx="168" cy="116" r="4"/>'
             '<circle class="d" cx="124" cy="86" r="7"/><rect class="d" x="74" y="56" width="44" height="9" rx="4"/><circle class="w" cx="96" cy="30" r="18"/>'
             '<text x="96" y="38" text-anchor="middle" style="font:400 24px Anton;fill:#8a6a12">€</text>',
    'client': '<circle class="w" cx="84" cy="56" r="34"/><path class="w" d="M24 184 Q24 102 84 100 Q144 102 144 184 Z"/>'
              '<path class="r" d="M156 116 C130 92 112 80 124 64 C132 52 150 56 156 70 C162 56 180 52 188 64 C200 80 182 92 156 116Z"/>',
    'arrow': '<path class="sk" d="M10 100 L170 100" style="stroke:#d4af37;stroke-width:16"/><path d="M140 64 L190 100 L140 136 Z" style="fill:#d4af37"/>',
}


def icon(name, x, y, size=200, g=None, fx='pop', rot=0):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    r = f';rotate:{rot}deg' if rot else ''
    return f'<svg class="ico" style="left:{x}px;top:{y}px{r}" width="{size}" height="{size}" viewBox="0 0 200 200"{a}>{ICONS[name]}</svg>'


def xtitle(l1, l2, top=250, g_line=None, s1=None, s2=None, uw=560):
    """Titre Anton 2 lignes ; la 2e ligne est soulignée par un trait doré qui se dessine (g_line)."""
    st1 = f' style="font-size:{s1}px"' if s1 else ''
    st2 = f' style="font-size:{s2}px"' if s2 else ''
    h2 = (s2 or 92) * 1.02
    uy = top + (s1 or 112) * 1.02 + h2 + 4
    ux = 485 - uw // 2
    ul = ''
    if g_line:
        ul = (f'<svg class="uline" style="left:{ux}px;top:{uy:.0f}px;overflow:visible" width="{uw}" height="30" viewBox="0 0 {uw} 30">'
              f'<path class="dr" pathLength="1" d="M6 18 Q{uw/2} 4 {uw-6} 14" data-g="{g_line}" data-fx="draw"/></svg>')
    return f'<div class="xt" style="top:{top}px"><div class="l1"{st1}>{l1}</div><div class="l2"{st2}>{l2}</div></div>' + ul


def notif(top, amount, title='Virement reçu', sub='Prime de bienvenue', g=None, fx='up'):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    ic = ('<svg width="80" height="80" viewBox="0 0 200 200"><path d="M100 14 L190 62 L10 62 Z" style="fill:#d4af37"/>'
          '<rect x="30" y="80" width="26" height="74" style="fill:#f4efe4"/><rect x="87" y="80" width="26" height="74" style="fill:#f4efe4"/>'
          '<rect x="144" y="80" width="26" height="74" style="fill:#f4efe4"/><rect x="10" y="162" width="180" height="22" style="fill:#d4af37"/></svg>')
    return (f'<div class="notif" style="top:{top}px"{a}><div class="ic">{ic}</div><div class="tx"><div class="a">MAINTENANT · Banque</div>'
            f'<div class="b">{title}</div><div class="a">{sub}</div></div><div class="m">+{amount}</div></div>')


# Mascotte vivante : rebond, clignement, sourcils, saut de joie, bras qui bougent.
XJS = '''
const MASC=[...document.querySelectorAll('.masc')];
function extra(t){MASC.forEach((m,i)=>{const p=i*1.37;const an=m.dataset.anim;
 const b=m.querySelector('.mb'),ey=m.querySelector('.eyes'),br=m.querySelector('.brows'),al=m.querySelector('.armL'),ar=m.querySelector('.armR');
 let y=Math.sin(t*4.2+p)*7, sq=1;
 if(an==='jump'){const k=Math.abs(Math.sin(t*5.2+p));y=-k*70;sq=k<0.15?0.93:1;}
 b.style.transform=`translateY(${y}px) scale(${1/sq},${sq})`;
 const bl=((t+p*0.9+1.3)%2.6)<0.13; ey.style.transform=`scaleY(${bl?0.12:1})`;
 const up=m.dataset.brow==='up'?(-12-5*Math.sin(t*3+p)):(-2*Math.sin(t*2+p)); br.style.transform=`translateY(${up}px)`;
 const wv=an==='jump'?22:8;
 al.style.transformOrigin='100% 0%';al.style.transform=`rotate(${Math.sin(t*5.1+p)*wv}deg)`;
 ar.style.transformOrigin='0% 100%';ar.style.transform=`rotate(${Math.sin(t*4.4+p+1)*wv*0.8}deg)`;
});
document.querySelectorAll('.dots i').forEach((d,k)=>{d.style.transform=`translateY(${-Math.max(0,Math.sin(t*9-k*0.9))*10}px)`});
document.querySelectorAll('.fly').forEach((f,k)=>{f.style.translate=`0 ${Math.sin(t*3.1+k)*10}px`;f.style.rotate=`${Math.sin(t*2.3+k*2)*6}deg`});
}
'''
JS = 'const CAM=0.5, PUSH=0.008;' + XJS
