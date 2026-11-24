import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo import *
from hacoo_items import icon, ICONS
# Hacoo, 24/11/2026, vidéo 4 (compte affiliation, tâche « 2 vidéos Hacoo en plus ») - style D « Duo 3D » (la maligne vs le pigeon),
# fond prune nuit, accent turquoise. Format F2 démystification dans un dialogue F10 : « Il attend vendredi (Black Friday) pour commander ».
# Le pigeon n'achète rien avant vendredi ; la maligne lui montre que le code promo Hacoo hzklink marche déjà aujourd'hui.
# Aucune opération Black Friday annoncée ni démentie : on montre seulement le -14 % du code.
# Prix d'exemple : bottines 44 € + écharpe 15 € + bonnet 9 € = 68,00 € ; -14 % = 9,52 € ; total 58,48 €. Articles génériques, sans marque ni logo.
# Voix : la maligne (M) = Eve (xai), le pigeon (P) = Louis (smallest), speed 1.1, une synthèse par réplique, silences coupés
# (internes plafonnés à 0,22 s), atempo 1.1 (Eve, +3 dB) / 1.07 (Louis, -1 dB), 0,2 s au début et 0,45 s entre les répliques (SPLITS).
# Réplique « Et tu attends quoi, exactement ? » retirée (durée), remplacée par la bulle « ?! » au-dessus de la maligne.
NAME = 'hacoo54'
TITLE = 'Hacoo duo 3D il attend vendredi'
HEAD = THREE
LINES = [
 ("Moi, je commande rien sur l'appli Hacou avant vendredi. J'attends le Black Friday.", [("Moi, je commande", None), ("<em>rien</em> sur l'appli", None), ("<em>Hacoo</em> avant", None), ("vendredi.", None), ("J'attends le", None), ("<em>Black Friday.</em>", None)]),
 ("Ben, une réduction ! Y aura sûrement des promos.", [("Ben, une", None), ("<em>réduction&nbsp;!</em>", None), ("Y aura sûrement", None), ("des promos.", None)]),
 ("Bottines, écharpe, bonnet : soixante-huit euros.", [("Bottines,", None), ("écharpe, bonnet :", None), ("<em>68&nbsp;€.</em>", None)]),
 ("Code promo Hacou : H, Z, K, link. Dans la case code promo, et j'applique.", [("<em>Code promo Hacoo&nbsp;:</em>", None), ("<i>hzklink</i>.", None), ("Dans la case", None), ("code promo,", None), ("et j'applique.", None)]),
 ("Ça fait neuf euros cinquante-deux de moins ?! Aujourd'hui ?", [("Ça fait", None), ("<em>9,52&nbsp;€</em> de moins&nbsp;?!", None), ("<em>Aujourd'hui&nbsp;?</em>", None)]),
 ("Aujourd'hui. Pas besoin d'attendre vendredi.", [("<em>Aujourd'hui.</em>", None), ("Pas besoin", None), ("d'attendre vendredi.", None)]),
 ("Cinquante-huit euros et quarante-huit centimes… et moi qui attendais.", [("<i>58,48&nbsp;€…</i>", None), ("et moi", None), ("qui <em>attendais.</em>", None)]),
 ("Envoie cette vidéo à ton pote. Code promo Hacou, H, Z, K, link. Les liens sont dans ma bio.", [("Envoie cette vidéo", None), ("à ton <em>pote</em>.", None), ("<em>Code promo Hacoo</em>", None), ("<i>hzklink</i>.", None), ("Les liens sont", None), ("dans ma <em>bio</em>.", None)]),
]
SPLITS = [(0.2, 3.66), (4.11, 6.15), (6.6, 9.35), (9.8, 14.51), (14.96, 16.93), (17.38, 19.34), (19.79, 22.77), (23.22, 28.63)]
MINLEN = 0.9
GAP = 0.12
TAIL = 2.6
DUO_LINES = [
 {'who': 'P', 'M': 'idle', 'P': 'cool', 'shot': 'wide'},
 {'who': 'P', 'M': 'think', 'P': 'shrug', 'shot': 'M'},
 {'who': 'M', 'M': 'point', 'P': 'idle', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'point', 'P': 'think', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'hip', 'P': 'shock', 'shot': 'P'},
 {'who': 'M', 'M': 'cool', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'shrug', 'P': 'head', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'talk', 'P': 'idle', 'shot': 'wide', 'lbl': False},
]
JS = duo_js(DUO_LINES, bg=0x1a0b14)

CSS = '''
#sub{font-size:76px;left:70px;width:860px}
#sub i{text-transform:none}
#sub em,.hook em{background:#19b8a6}
.hook{top:225px;font-size:62px;left:90px;width:840px}
#bgtex,#stage,html,body{background:#1a0b14}
.phone.big{width:600px;height:380px}
.endc{left:110px;width:810px}
.endc .c{color:#0f9e8e}
.mini{position:absolute;padding:6px 18px;border-radius:14px;background:#fff;color:#111;font:900 40px 'Inter',sans-serif;box-shadow:0 8px 0 rgba(0,0,0,.35);white-space:nowrap}
.ok2{position:absolute;left:-150px;top:-120px;padding:8px 22px;border:7px solid #19b8a6;color:#0f9e8e;border-radius:14px;font:900 50px 'Inter',sans-serif;background:#fff;transform:rotate(-6deg);white-space:nowrap}
'''


def prod(ic, name, price, g, x, y, w=260):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;padding:12px 0 14px" data-g="{g}" data-fx="pop">'
            f'{icon(ic, 120)}<div class="t">{name}</div><div class="p" style="font-size:56px">{price}</div><div class="x">prix d\'exemple</div></div>')


BODY = duo_body('LA MALIGNE', 'LE PIGEON') + '''
  <div class="scene" data-s="0"><div class="hook">Il attend vendredi…<br>et rate le<br><em>code promo Hacoo</em></div></div>
''' + anc('P', '<div class="mini" style="left:-60px;top:20px;transform:rotate(-5deg)" data-g="0.3" data-fx="pop">📅 vendredi ?</div>', '0') + '''
''' + anc('M', '<div class="bub" style="left:-95px;top:-230px" data-g="1.0" data-fx="stamp">?!</div>', '1') + '''
  <div class="scene" data-s="2" data-in="pop">''' + prod('Bottines', 'bottines', '44 €', '2.0', 60, 250) + prod('Écharpe', 'écharpe', '15 €', '2.1', 360, 225) + prod('Bonnet', 'bonnet', '9 €', '2.1', 660, 250) + '''
   <div class="tag" style="left:380px;top:560px" data-g="2.2" data-fx="stamp">= 68,00 €</div></div>
  <div class="scene" data-s="3" data-in="pop">
   <div class="phone big" style="left:230px;top:230px" data-g="3.0" data-fx="up"><div class="t">CODE PROMO HACOO</div>
    <div class="f"><span data-g="3.1" data-fx="type">hzklink</span></div><div class="ok" data-g="3.4" data-fx="fade">✓ code appliqué · -14 %</div></div>
  </div>
''' + anc('P', '<div class="tag red" style="left:-150px;top:-150px;font-size:64px" data-g="4.1" data-fx="stamp">-9,52 €</div>', '4') + '''
''' + anc('M', '<div class="ok2" data-g="5.0" data-fx="stamp">AUJOURD’HUI ✓</div>', '5') + '''
  <div class="scene" data-s="6" data-in="pop">
   <div class="tag" style="left:390px;top:200px" data-g="6.0" data-fx="pop"><s>68,00 €</s>-14 %</div>
   <div class="card" style="left:250px;top:300px;width:580px;padding:18px 0" data-g="6.0" data-fx="stamp" data-slow="6.0"><div class="t">avec le code promo hacoo</div><div class="p" style="font-size:120px;color:#0f9e8e">58,48 €</div><div class="x"><span style="text-transform:none">hzklink</span> · prix d'exemple</div></div>
  </div>
  <div class="scene" data-s="7" data-in="pop" style="z-index:7">
   <div class="endc" data-g="7.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div>
    <div class="b" data-g="7.4" data-fx="pop">liens des articles tendance en bio</div><div class="x">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
  </div>
'''
