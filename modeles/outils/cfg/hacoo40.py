import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo2d import *
from hacoo_items import icon
# Hacoo n°4 du 20/11/2026 - style D2 « Duo dessiné » (1re vidéo de ce style, briques cfg/duo2d.py + duo2d.js + base_duo2d.css).
# Format F10 « même panier, pas le même prix » : la pigeonne paie 55 €, le malin a payé 47,30 € le même panier avec le code promo Hacoo.
# Prix d'exemple : survêt 32 € + sacoche 14 € + bonnet 9 € = 55,00 € ; -14 % = 7,70 € ; total 47,30 €.
# Articles génériques, sans marque ni logo.
# Voix : le malin (M) = Etienne (cartesia sonic-3.5, c6ccfe32-...), la pigeonne (P) = Hélène (inworld-tts-2), speed 1.08,
# une synthèse par réplique, silences internes plafonnés à 0,24 s.
NAME = 'hacoo40'
TITLE = 'Hacoo duo dessine meme panier'
LINES = [
 ("Sur l'appli Hacou, mon panier : cinquante-cinq euros.", [("Sur l'appli <em>Hacoo</em>,", None), ("mon panier :", None), ("<em>55&nbsp;€</em>", None)]),
 ("Moi, le même panier : quarante-sept euros trente.", [("Moi, le même panier :", None), ("<i>47,30&nbsp;€</i>", None)]),
 ("Quoi ?! Le même survêt, la même sacoche ?", [("<em>Quoi ?!</em>", None), ("Le même survêt,", None), ("la même sacoche&nbsp;?", None)]),
 ("Et le même bonnet. Mais moi, j'ai mis le code promo Hacou.", [("Et le même <em>bonnet</em>", None), ("Mais moi, j'ai mis", None), ("<em>code promo Hacoo</em>", None)]),
 ("Lequel ?", [("<em>Lequel ?</em>", None)]),
 ("H, Z, K, link. Moins quatorze pour cent.", [("<i>hzklink</i>", None), ("<em>-14&nbsp;%</em>", None)]),
 ("Donc sept euros soixante-dix de moins ?! Pourquoi tu me l'as pas dit ?", [("Donc <em>7,70&nbsp;€</em>", None), ("de moins&nbsp;?!", None), ("Pourquoi tu me", None), ("l'as pas <em>dit ?</em>", None)]),
 ("Je te le dis là. Code promo Hacou, H, Z, K, link. Les liens sont dans ma bio.", [("Je te le dis là.", None), ("<em>Code promo Hacoo</em>", None), ("<i>hzklink</i>", None), ("Les liens sont", None), ("dans ma <em>bio</em>.", None)]),
]
SPLITS = [(0.2, 2.927), (3.377, 6.004), (6.454, 8.613), (9.063, 12.433), (12.883, 13.403), (13.853, 17.606), (18.056, 20.87), (21.32, 27.564)]
DUO_LINES = [
 {'who': 'P', 'M': 'idle', 'P': 'hip', 'shot': 'wide'},
 {'who': 'M', 'M': 'cool', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'hip', 'P': 'shock', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'talk', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'idle', 'P': 'think', 'shot': 'P'},
 {'who': 'M', 'M': 'point', 'P': 'shock', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'shrug', 'P': 'head', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'talk', 'P': 'idle', 'shot': 'wide', 'lbl': False},
]
JS = duo2d_js(DUO_LINES, p_bun=True)

CSS = ''


def prod(ic, name, price, g, x, y, w=290):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;padding:10px 0 12px" data-g="{g}" data-fx="pop">'
            f'<span class="ico">{icon(ic, 140)}</span><div class="t">{name}</div><div class="p" style="font-size:62px">{price}</div><div class="x">prix d\'exemple</div></div>')


BODY = duo2d_body('le malin', 'la pigeonne') + '''
  <div class="scene" data-s="0"><div class="hook">Même panier <mark>Hacoo</mark>…<br>pas le même <em>prix</em>&nbsp;?!</div></div>
''' + anc('P', '<div class="tag" style="left:-110px;top:-150px" data-g="0.2" data-fx="stamp">55,00 €</div>', '0') + '''
''' + anc('M', '<div class="tag green" style="left:-120px;top:-170px" data-g="1.1" data-fx="stamp">47,30 €</div>', '1') + '''
  <div class="scene" data-s="2-3" data-in="pop">''' + prod('Survêt', 'survêt', '32 €', '2.1', 80, 200) + prod('Sacoche', 'sacoche', '14 €', '2.2', 395, 170) + prod('Bonnet', 'bonnet', '9 €', '3.0', 710, 200) + '''</div>
''' + anc('P', '<div class="bub" style="left:-90px;top:-200px" data-g="4.0" data-fx="stamp">?</div>', '4') + '''
  <div class="scene" data-s="5" data-in="pop">
   <div class="phone" style="left:280px;top:230px" data-g="5.0" data-fx="up"><div class="t">CODE PROMO HACOO</div>
    <div class="f"><span data-g="5.0" data-fx="type">hzklink</span></div><div class="ok" data-g="5.1" data-fx="fade">✓ -14 % appliqué</div></div>
  </div>
  <div class="scene" data-s="6" data-in="pop">
   <div class="tag" style="left:390px;top:200px" data-g="6.0" data-fx="pop"><s>55,00 €</s>-14 %</div>
   <div class="card" style="left:240px;top:300px;width:600px;padding:18px 0" data-g="6.0" data-fx="stamp" data-slow="6.0"><div class="t">avec le code promo hacoo</div><div class="p" style="font-size:120px;color:#2bb673">47,30 €</div><div class="x">hzklink · -7,70 € · prix d'exemple</div></div>
  </div>
  <div class="scene" data-s="7" data-in="pop" style="z-index:7">
   <div class="endc" style="top:170px" data-g="7.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div>
    <div class="b" data-g="7.3" data-fx="pop">liens des articles tendance en bio</div><div class="x">Prix d'exemple · -14 % avec le code promo Hacoo hzklink · Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
   <div class="note" style="left:170px;top:706px;font-size:36px;transform:rotate(-2deg)" data-g="7.1" data-fx="pop">envoie-la à ton pote avant qu'il paie</div>
  </div>
'''
