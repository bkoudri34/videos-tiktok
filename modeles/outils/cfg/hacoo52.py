import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo2d import *
from hacoo_items import icon
# Hacoo n°2 du 24/11/2026 - style D2 « Duo dessiné », accent vert menthe (brief veille/briefs/2026-11-24.md, vidéo 2).
# Format F8 « résultat d'abord » dans un dialogue F10 : « Ce ticket Hacoo, il croit que c'est un bug » : le ticket du malin
# avec la ligne -12,46 € entourée est affiché dès la 1re image, le pigeon croit à un bug, le malin lui montre le code promo Hacoo.
# Prix d'exemple : doudoune 61 € + casquette 17 € + gants 11 € = 89,00 € ; -14 % = 12,46 € ; total 76,54 €
# (12,46 € > 11 € : « tes gants sont offerts, et il en reste »). Articles génériques, sans marque ni logo.
# Voix : le malin (M) = cosmo (xai), le pigeon (P) = Mathieu (inworld), speed 1.1, une synthèse par réplique,
# silences de bord coupés, silences internes plafonnés à 0,24 s, atempo 1.1, 0,2 s au début et 0,45 s entre répliques.
NAME = 'hacoo52'
TITLE = 'Hacoo duo dessine bug menthe'
LINES = [
 ("Ton ticket de l'appli Hacou, il t'enlève douze euros ?! C'est un bug !", [("Ton ticket <em>Hacoo</em>,", None), ("il t'enlève <em>12&nbsp;€&nbsp;?!</em>", None), ("C'est un <em>bug&nbsp;!</em>", None)]),
 ("C'est pas un bug. C'est le code promo Hacou.", [("C'est pas un bug.", None), ("C'est le <em>code promo Hacoo.</em>", None)]),
 ("Moi j'ai pris le même panier. J'ai payé plein pot.", [("Moi j'ai pris", None), ("le même panier.", None), ("J'ai payé <em>plein pot.</em>", None)]),
 ("Doudoune, casquette, gants : quatre-vingt-neuf euros.", [("Doudoune,", None), ("casquette, gants&nbsp;:", None), ("<em>89&nbsp;€</em>", None)]),
 ("Avant de payer, tu tapes H, Z, K, link dans la case code promo. Appliquer.", [("Avant de payer,", None), ("tu tapes <i>hzklink</i>", None), ("dans la case", None), ("<em>code promo.</em>", None), ("Appliquer.", None)]),
 ("Ça fait douze euros quarante-six de moins ?!", [("Ça fait <em>12,46&nbsp;€</em>", None), ("de <em>moins&nbsp;?!</em>", None)]),
 ("Tes gants sont offerts, et il en reste.", [("Tes gants", None), ("sont <em>offerts</em>,", None), ("et il en reste.", None)]),
 ("Soixante-seize euros et cinquante-quatre centimes… et moi qui croyais à un bug.", [("<em>76,54&nbsp;€</em>…", None), ("et moi qui croyais", None), ("à un <em>bug.</em>", None)]),
 ("Envoie cette vidéo à ton pote. Code promo Hacou, H Z K link. Les liens sont dans ma bio.", [("Envoie cette vidéo", None), ("à ton pote.", None), ("<em>Code promo Hacoo</em>", None), ("<i>hzklink</i>", None), ("Les liens sont", None), ("dans ma <em>bio</em>.", None)]),
]
SPLITS = [(0.2, 3.148), (3.598, 5.553), (6.003, 8.153), (8.603, 11.014), (11.464, 16.106), (16.556, 18.023), (18.473, 20.08), (20.53, 23.919), (24.369, 29.937)]
DUO_LINES = [
 {'who': 'P', 'M': 'idle', 'P': 'shock', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'cool', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'idle', 'P': 'shrug', 'shot': 'P'},
 {'who': 'M', 'M': 'point', 'P': 'idle', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'point', 'P': 'think', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'hip', 'P': 'shock', 'shot': 'P'},
 {'who': 'M', 'M': 'cool', 'P': 'idle', 'shot': 'M', 'lbl': False},
 {'who': 'P', 'M': 'shrug', 'P': 'head', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'talk', 'P': 'idle', 'shot': 'wide', 'lbl': False},
]
JS = duo2d_js(DUO_LINES, p_bun=False, cap='#2fc79b')

MINT = '#14a37a'
CSS = '''
#sub{left:90px;width:840px;font-size:68px}
.hook{left:90px;width:840px;font-size:70px}
#sub em{background:''' + MINT + '''}
.hook em{color:''' + MINT + '''}
.hook mark{background:#bff3e1}
.tag.mint{background:#bff3e1;color:#0b4a37}
.tag.green{background:''' + MINT + '''}
.tk{position:absolute;width:600px;padding:14px 34px 12px;background:#fff;border:6px solid #111;border-radius:22px;box-shadow:9px 11px 0 #111;font:700 34px 'Inter',sans-serif;color:#111;white-space:nowrap;transform:rotate(-2deg)}
.tk .h{font:900 26px Inter;letter-spacing:3px;text-align:center;color:#555;border-bottom:4px dashed #bbb;padding-bottom:10px;margin-bottom:10px}
.tk .r{display:flex;justify-content:space-between;line-height:1.5}
.tk .r.cd{position:relative;color:''' + MINT + ''';font-weight:900;font-size:40px;margin:8px 0}
.tk .r.cd b{position:relative}
.tk .r.cd b:after{content:'';position:absolute;left:-14px;top:-6px;right:-10px;bottom:-6px;border:5px solid #e63946;border-radius:50%;transform:rotate(-4deg)}
.tk .r.tt{border-top:4px dashed #bbb;margin-top:8px;padding-top:6px;font:900 38px Inter}
.tk .x{text-align:center;font:700 18px Inter;letter-spacing:2px;color:#888;text-transform:uppercase;margin-top:6px}
.endc .nt{margin-top:12px;font:700 32px 'Comic Relief','Comic Sans MS',cursive;color:#e63946}
.stampo{position:absolute;padding:6px 22px;border:7px solid #e63946;border-radius:14px;color:#e63946;font:900 50px Inter;letter-spacing:2px;transform:rotate(-12deg);background:rgba(255,255,255,.85);white-space:nowrap}
'''


def prod(ic, name, price, g, x, y, w=240):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;padding:10px 0 12px" data-g="{g}" data-fx="pop">'
            f'<span class="ico">{icon(ic, 115)}</span><div class="t">{name}</div><div class="p" style="font-size:58px">{price}</div><div class="x">prix d\'exemple</div></div>')


def ticket(x, y, g=None):
    a = f' data-g="{g}" data-fx="pop"' if g else ''
    return (f'<div class="tk" style="left:{x}px;top:{y}px"{a}><div class="h">TICKET · APPLI HACOO</div>'
            '<div class="r"><span>panier</span><span>89,00 €</span></div>'
            '<div class="r cd"><span>code hzklink</span><b>-12,46 €</b></div>'
            '<div class="r tt"><span>total</span><span>76,54 €</span></div><div class="x">prix d\'exemple</div></div>')


BODY = duo2d_body('le malin', 'le pigeon') + '''
  <div class="scene" data-s="0"><div class="hook">Ce ticket <mark>Hacoo</mark>,<br>il croit que<br>c'est un <em>bug</em></div>''' + ticket(230, 452) + '''</div>
''' + anc('M', '<div class="tag mint" style="left:-200px;top:-150px" data-g="1.1" data-fx="stamp">CODE PROMO HACOO</div>', '1') + '''
''' + anc('P', '<div class="bub" style="left:-260px;top:-230px" data-g="2.0" data-fx="stamp">?!</div><div class="tag red" style="left:-120px;top:-150px" data-g="2.2" data-fx="stamp">plein pot : 89 €</div>', '2') + '''
  <div class="scene" data-s="3" data-in="pop">''' + prod('Doudoune', 'doudoune', '61 €', '3.0', 110, 230) + prod('Casquette', 'casquette', '17 €', '3.1', 420, 210) + prod('Gants', 'gants', '11 €', '3.1', 700, 230, 220) + '''
   <div class="tag" style="left:395px;top:560px" data-g="3.2" data-fx="stamp">= 89,00 €</div></div>
  <div class="scene" data-s="4" data-in="pop">
   <div class="phone" style="left:270px;top:230px" data-g="4.0" data-fx="up"><div class="t">CODE PROMO HACOO</div>
    <div class="f"><span data-g="4.1" data-fx="type">hzklink</span></div><div class="ok" data-g="4.4" data-fx="fade">Appliquer ✓ -14 %</div></div>
  </div>
''' + anc('P', '<div class="tag green" style="left:-130px;top:-170px" data-g="5.0" data-fx="stamp">-12,46 €</div>', '5') + '''
  <div class="scene" data-s="6" data-in="pop">''' + prod('Gants', 'gants', '11 €', '6.0', 400, 230, 280) + '''
   <div class="stampo" style="left:560px;top:250px" data-g="6.1" data-fx="stamp">OFFERTS</div></div>
  <div class="scene" data-s="7" data-in="pop">
   <div class="tag" style="left:370px;top:220px" data-g="7.0" data-fx="pop"><s>89,00 €</s>-14 %</div>
   <div class="card" style="left:240px;top:320px;width:600px;padding:18px 0" data-g="7.0" data-fx="stamp" data-slow="7.0"><div class="t">avec le code promo hacoo</div><div class="p" style="font-size:120px;color:''' + MINT + '''">76,54 €</div><div class="x"><span style="text-transform:none">hzklink</span> · -12,46 € · prix d'exemple</div></div>
  </div>
  <div class="scene" data-s="8" data-in="pop" style="z-index:7">
   <div class="endc" style="top:215px;left:95px;width:820px" data-g="8.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div>
    <div class="b" data-g="8.4" data-fx="pop">liens des articles tendance en bio</div><div class="nt" data-g="8.1" data-fx="pop">envoie cette vidéo au pote qui croit au bug</div><div class="x">Prix d'exemple · -14 % avec le code promo Hacoo hzklink · Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
  </div>
'''
