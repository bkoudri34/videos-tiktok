import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo import *
from hacoo_items import icon, ICONS
# Hacoo, 27/11/2026, vidéo 4 (compte affiliation, tâche « 2 vidéos Hacoo en plus ») - style D « Duo 3D », sol vert forêt, accent framboise.
# Format F10 « le connaisseur vs l'ignorant » : « « -14 %, c'est rien »… vraiment ? » -> la maligne lui demande son panier ->
# casque 48 € + lampe 25 € + porte-clés 7 € = 80,00 € -> code promo hzklink avant de payer -> -11,20 € (« plus que ton porte-clés »)
# -> 68,80 € (ralenti) « bon… c'est pas rien » -> « envoie cette vidéo au pote qui dit que 14 %, c'est rien ».
# Calcul : 80,00 × 0,14 = 11,20 ; 80,00 × 0,86 = 68,80 ; 80,00 - 11,20 = 68,80. Prix d'exemple, articles génériques sans marque.
# Règle du 26/11 : « Hacoo » n'est JAMAIS écrit à l'image (ni sous-titres) : seulement dit à l'oral.
# Voix : la maligne (M) = Eve (xai), le pigeon (P) = Etienne (cartesia), speed 1.1, une synthèse par réplique, silences coupés
# (internes plafonnés à 0,22 s), atempo 1.1, normalisées à -19 dB moyen, recollées avec 0,2 s au début et 0,45 s entre elles (SPLITS).
NAME = 'hacoo66'
TITLE = 'Duo 3D 14 pour cent c est rien'
HEAD = THREE
LINES = [
 ("Le code promo de l'appli Hacou ? Moins quatorze pour cent, c'est rien !", [("Le code promo", None), ("de l'appli&nbsp;?", None), ("<em>-14&nbsp;%</em>,", None), ("c'est <em>rien&nbsp;!</em>", None)]),
 ("Rien ? Montre-moi ton panier.", [("<em>Rien&nbsp;?</em>", None), ("Montre-moi ton panier.", None)]),
 ("Un casque, une lampe et un porte-clés : quatre-vingts euros.", [("Un casque,", None), ("une lampe", None), ("et un porte-clés :", None), ("<em>80&nbsp;€.</em>", None)]),
 ("Code promo Hacou : H, Z, K, link. Tu le tapes avant de payer.", [("<em>Code promo</em>", None), ("<i>hzklink</i>.", None), ("Tu le tapes", None), ("avant de <em>payer.</em>", None)]),
 ("Ça fait onze euros vingt de moins. Plus que ton porte-clés !", [("Ça fait", None), ("<em>11,20&nbsp;€</em>", None), ("de moins.", None), ("Plus que ton porte&#8209;clés&nbsp;!", None)]),
 ("Soixante-huit euros et quatre-vingts centimes ? Bon… c'est pas rien.", [("<i>68,80&nbsp;€&nbsp;?</i>", None), ("Bon…", None), ("c'est pas <em>rien.</em>", None)]),
 ("Envoie cette vidéo au pote qui dit que quatorze pour cent, c'est rien. Code promo Hacou, H, Z, K, link.", [("<em>Envoie</em> cette vidéo", None), ("au pote qui dit", None), ("que 14&nbsp;%,", None), ("c'est rien.", None), ("Code promo", None), ("<i>hzklink</i>.", None)]),
]
SPLITS = [(0.2, 3.5), (3.95, 5.55), (6.0, 8.92), (9.37, 13.79), (14.24, 16.76), (17.21, 20.08), (20.53, 26.65)]
MINLEN = 0.9
GAP = 0.12
TAIL = 2.6
DUO_LINES = [
 {'who': 'P', 'M': 'idle', 'P': 'shrug', 'shot': 'wide'},
 {'who': 'M', 'M': 'hip', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'think', 'P': 'talk', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'point', 'P': 'think', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'cool', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'hip', 'P': 'shock', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'point', 'P': 'head', 'shot': 'wide', 'lbl': False},
]
JS = duo_js(DUO_LINES, bg=0x08180f)

CSS = '''
#sub{font-size:76px;left:70px;width:860px}
#sub i{text-transform:none}
#sub em,.hook em{background:#e0457b}
.hook{top:225px;font-size:66px;left:90px;width:840px}
#bgtex,#stage,html,body{background:#08180f}
.phone.big{width:620px;height:400px}
.endc{left:110px;width:810px}
.endc .c{color:#d6336c}
.mini{position:absolute;padding:8px 22px;border-radius:16px;background:#fff;color:#111;font:900 42px 'Inter',sans-serif;box-shadow:0 8px 0 rgba(0,0,0,.35);white-space:nowrap}
'''


def prod(ic, name, price, g, x, y, w=260):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;padding:12px 0 14px" data-g="{g}" data-fx="pop">'
            f'{icon(ic, 120)}<div class="t">{name}</div><div class="p" style="font-size:56px">{price}</div><div class="x">prix d\'exemple</div></div>')


BODY = duo_body('LA MALIGNE', 'LE PIGEON') + '''
  <div class="scene" data-s="0"><div class="hook">« -14 %,<br>c'est rien »…<br><em>vraiment ?</em></div></div>
''' + anc('M', '<div class="bub" style="left:-95px;top:-230px" data-g="1.0" data-fx="stamp">?!</div>', '1') + '''
  <div class="scene" data-s="2" data-in="pop">''' + prod('Casque', 'casque', '48 €', '2.0', 60, 250) + prod('Lampe', 'lampe', '25 €', '2.1', 360, 225) + prod('Porte-clés', 'porte-clés', '7 €', '2.2', 660, 250) + '''
   <div class="tag" style="left:380px;top:560px" data-g="2.3" data-fx="stamp">= 80,00 €</div></div>
  <div class="scene" data-s="3" data-in="pop">
   <div class="phone big" style="left:220px;top:240px" data-g="3.0" data-fx="up"><div class="t">CODE PROMO</div>
    <div class="f"><span data-g="3.1" data-fx="type">hzklink</span></div><div class="ok" data-g="3.3" data-fx="fade">✓ -14 % · avant « Payer »</div></div>
  </div>
''' + anc('M', '<div class="tag red" style="left:-170px;top:-260px;font-size:64px" data-g="4.1" data-fx="stamp">-11,20 €</div><div class="mini" style="left:-200px;top:-150px;transform:rotate(-4deg)" data-g="4.3" data-fx="pop">&gt; le porte-clés (7 €)</div>', '4') + '''
  <div class="scene" data-s="5" data-in="pop">
   <div class="tag" style="left:390px;top:200px" data-g="5.0" data-fx="pop"><s>80,00 €</s>-14 %</div>
   <div class="card" style="left:250px;top:300px;width:580px;padding:18px 0" data-g="5.0" data-fx="stamp" data-slow="5.0"><div class="t">avec le code promo</div><div class="p" style="font-size:120px;color:#d6336c">68,80 €</div><div class="x"><span style="text-transform:none">hzklink</span> · prix d'exemple</div></div>
  </div>
  <div class="scene" data-s="6" data-in="pop" style="z-index:7">
   <div class="endc" data-g="6.0" data-fx="up"><div class="k">CODE PROMO</div><div class="c">hzklink</div><div class="d">-14 % avec le code hzklink</div>
    <div class="b" data-g="6.3" data-fx="pop">liens des articles tendance en bio</div><div class="x">Prix d'exemple · -14 % avec le code promo hzklink<br>Offre soumise aux conditions en vigueur</div></div>
  </div>
'''
