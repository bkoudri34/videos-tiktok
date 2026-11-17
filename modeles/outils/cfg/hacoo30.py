import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo import *
from hacoo_items import icon
# Hacoo test du 17/11/2026 - style D « Duo 3D » (1re vidéo de ce style) : le malin vs le pigeon.
# Baskets 35 € + survêt 28 € + sacoche 12 € = 75,00 € -> 64,50 € avec le code promo Hacoo hzklink (-14 %, 10,50 € d'économie), prix d'exemple.
# Articles sport génériques sans marque ni logo. Voix : M = xAI « cosmo », P = Inworld « Mathieu », vitesse 1.1, une synthèse par réplique.
NAME = 'hacoo30'
TITLE = 'Hacoo duo 3D plein pot'
HEAD = THREE
LINES = [
 ("Frérot, t'as payé tes baskets plein pot sur l'appli Hacou ?", [("Frérot,", None), ("t'as payé tes baskets", None), ("<em>plein pot</em>", None), ("sur l'appli <em>Hacoo</em> ?", None)]),
 ("Ben ouais, trente-cinq euros. C'est le prix, non ?", [("Ben ouais,", None), ("<em>35 €</em>.", None), ("C'est le prix,", None), ("non ?", None)]),
 ("Et le survêt ? Et la sacoche ?", [("Et le <em>survêt</em> ?", None), ("Et la <em>sacoche</em> ?", None)]),
 ("Soixante-quinze euros en tout. Pourquoi tu me regardes comme ça ?", [("<em>75 €</em> en tout.", None), ("Pourquoi tu me", None), ("regardes comme ça ?", None)]),
 ("T'as pas mis le code promo Hacou, H Z K link ?", [("T'as pas mis", None), ("le <em>code promo Hacoo</em>", None), ("<i>hzklink</i> ?", None)]),
 ("Le quoi ?!", [("Le <em>quoi</em> ?!", None)]),
 ("Moins quatorze pour cent. Soixante-quatre euros cinquante au lieu de soixante-quinze.", [("<em>-14 %</em>.", None), ("<i>64,50 €</i>", None), ("au lieu de 75.", None)]),
 ("Attends... j'ai perdu dix euros cinquante ?!", [("Attends...", None), ("j'ai perdu", None), ("<em>10,50 €</em> ?!", None)]),
 ("Code promo Hacou, H Z K link. Les liens des articles sont dans ma bio.", [("<em>Code promo Hacoo</em>", None), ("<i>hzklink</i>.", None), ("Les liens des articles", None), ("dans ma <em>bio</em>.", None)]),
]
SPLITS = [(0.2, 2.747), (3.197, 5.477), (5.927, 7.885), (8.335, 11.034), (11.484, 14.535), (14.985, 15.39), (15.84, 19.797), (20.247, 22.586), (23.036, 27.923)]
MINLEN = 0.9
GAP = 0.12
TAIL = 2.6
DUO_LINES = [
 {'who': 'M', 'M': 'point', 'P': 'idle', 'shot': 'wide'},
 {'who': 'P', 'M': 'hip', 'P': 'shrug', 'shot': 'P'},
 {'who': 'M', 'M': 'talk', 'P': 'idle', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'think', 'P': 'talk', 'shot': 'P'},
 {'who': 'M', 'M': 'point', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'hip', 'P': 'shock', 'shot': 'P'},
 {'who': 'M', 'M': 'talk', 'P': 'shock', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'shrug', 'P': 'head', 'shot': 'P'},
 {'who': 'M', 'M': 'cool', 'P': 'idle', 'shot': 'wide'},
]
JS = duo_js(DUO_LINES)

CSS = '''
#sub i{text-transform:none}
.hook{top:250px}
'''


def prod(ic, price, g, x, y, w=330):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;padding:14px 0 16px" data-g="{g}" data-fx="pop">'
            f'{icon(ic, 170)}<div class="p">{price}</div><div class="x">prix d\'exemple</div></div>')


BODY = duo_body() + '''
  <div class="scene" data-s="0"><div class="hook">Tu paies <em>plein pot</em><br>sur Hacoo ?</div></div>
''' + anc('P', prod('Baskets', '35 €', '1.1', -190, -330, 380), '1') + '''
  <div class="scene" data-s="2" data-in="pop">''' + prod('Survêt', '28 €', '2.0', 150, 190) + prod('Sacoche', '12 €', '2.1', 600, 190) + '''</div>
''' + anc('P', '''<div class="card" style="left:-240px;top:-350px;width:480px;padding:22px 20px;white-space:normal" data-g="3.0" data-fx="stamp">
   <div class="t">ticket · panier hacoo</div><div style="font:700 24px Inter,Arial,sans-serif;color:#374151;margin:10px 0">baskets 35 € · survêt 28 € · sacoche 12 €</div>
   <div class="p">75,00 €</div><div class="x">sans code · prix d'exemple</div></div>''', '3') + '''
''' + anc('M', '''<div class="phone" style="left:-260px;top:-360px" data-g="4.0" data-fx="up"><div class="t">CODE PROMO HACOO</div>
   <div class="f"><span data-g="4.2" data-fx="type">hzklink</span></div><div class="ok" data-g="4.2" data-fx="fade">✓ -14 % appliqué</div></div>''', '4') + '''
''' + anc('P', '<div class="bub" style="left:-95px;top:-230px" data-g="5.0" data-fx="stamp">?!</div>', '5') + '''
  <div class="scene" data-s="6" data-in="pop">
   <div class="tag" style="left:390px;top:200px" data-g="6.0" data-fx="pop"><s>75,00 €</s>-14 %</div>
   <div class="card" style="left:240px;top:300px;width:600px;padding:18px 0" data-g="6.1" data-fx="stamp" data-slow="6.1"><div class="t">avec le code promo hacoo</div><div class="p" style="font-size:120px;color:#e5322d">64,50 €</div><div class="x">hzklink · prix d'exemple</div></div>
  </div>
''' + anc('P', '<div class="tag red" style="left:-190px;top:-150px;font-size:64px" data-g="7.2" data-fx="stamp">-10,50 € perdus</div>', '7') + '''
  <div class="scene" data-s="8" data-in="pop" style="z-index:7">
   <div class="endc" data-g="8.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div>
    <div class="b" data-g="8.2" data-fx="pop">liens des articles tendance en bio</div><div class="x">Prix d'exemple · -14 % avec le code promo Hacoo hzklink, selon conditions sur l'appli Hacoo</div></div>
  </div>
'''
