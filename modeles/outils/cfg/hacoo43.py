import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo2d import *
from hacoo_items import icon
# Hacoo n°1 du 22/11/2026 - style D2 « Duo dessiné », accent bleu glacier (brief veille/briefs/2026-11-22.md, vidéo 1).
# Format F10 « le connaisseur vs l'ignorant », thème « 14 %, ça sert à rien » : le pigeon pense que le code promo Hacoo
# ne sert à rien, le malin lui fait taper hzklink sur son panier d'hiver.
# Prix d'exemple : doudoune 46 € + bonnet 8 € + gants 9 € = 63,00 € ; -14 % = 8,82 € ; total 54,18 € (8,82 € > 8 € : « ton bonnet est payé »).
# Articles génériques, sans marque ni logo.
# Voix : le malin (M) = cosmo (xai), le pigeon (P) = Mathieu (inworld), speed 1.1, une synthèse par réplique,
# silences de bord coupés, silences internes plafonnés à 0,24 s, 0,2 s au début et 0,45 s entre répliques.
# Réplique 8 du brief (« Bon… ça sert à quelque chose. ») supprimée pour rester sous 30 s.
NAME = 'hacoo43'
TITLE = 'Hacoo duo dessine 14 pour cent glacier'
LINES = [
 ("Le code promo de l'appli Hacou ? Quatorze pour cent, ça sert à rien.", [("Le <em>code promo Hacoo</em>&nbsp;?", None), ("<em>14&nbsp;%</em>,", None), ("ça sert à <em>rien.</em>", None)]),
 ("Ah ouais ? Montre-moi ton panier.", [("Ah ouais ?", None), ("Montre-moi ton <em>panier.</em>", None)]),
 ("Une doudoune, un bonnet, des gants. Soixante-trois euros.", [("Une doudoune,", None), ("un bonnet, des gants.", None), ("<em>63&nbsp;€</em>", None)]),
 ("Tu tapes H, Z, K, link dans la case code promo, avant de payer.", [("Tu tapes <i>hzklink</i>", None), ("dans la case", None), ("<em>code promo</em>,", None), ("avant de payer.", None)]),
 ("Attends… ça fait huit euros quatre-vingt-deux de moins ?!", [("Attends…", None), ("ça fait <em>8,82&nbsp;€</em>", None), ("de <em>moins&nbsp;?!</em>", None)]),
 ("Voilà. Ton bonnet, il est payé.", [("Voilà.", None), ("Ton bonnet,", None), ("il est <em>payé.</em>", None)]),
 ("Cinquante-quatre euros dix-huit… au lieu de soixante-trois !", [("<em>54,18&nbsp;€</em>…", None), ("au lieu de 63&nbsp;€&nbsp;!", None)]),
 ("Envoie cette vidéo à ton pote. Code promo Hacou, H Z K link. Les liens sont dans ma bio.", [("Envoie cette vidéo", None), ("à ton pote.", None), ("<em>Code promo Hacoo</em>", None), ("<i>hzklink</i>", None), ("Les liens sont", None), ("dans ma <em>bio</em>.", None)]),
]
SPLITS = [(0.2, 3.07), (3.52, 5.038), (5.488, 8.373), (8.823, 13.475), (13.925, 16.269), (16.719, 18.416), (18.866, 21.55), (22.0, 27.818)]
DUO_LINES = [
 {'who': 'P', 'M': 'idle', 'P': 'shrug', 'shot': 'wide'},
 {'who': 'M', 'M': 'think', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'idle', 'P': 'talk', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'point', 'P': 'idle', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'hip', 'P': 'shock', 'shot': 'P'},
 {'who': 'M', 'M': 'cool', 'P': 'idle', 'shot': 'M', 'lbl': False},
 {'who': 'P', 'M': 'shrug', 'P': 'head', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'talk', 'P': 'idle', 'shot': 'wide', 'lbl': False},
]
JS = duo2d_js(DUO_LINES, p_bun=False, cap='#5fb8e6')

CSS = '''
#sub{left:90px;width:840px;font-size:66px}
.hook{left:90px;width:840px;font-size:70px}

#sub em{background:#2f8fd0}
.hook em{color:#2f8fd0}
.tag.ice{background:#bfe6fb;color:#0d3550}
'''


def prod(ic, name, price, g, x, y, w=250):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;padding:10px 0 12px" data-g="{g}" data-fx="pop">'
            f'<span class="ico">{icon(ic, 120)}</span><div class="t">{name}</div><div class="p" style="font-size:60px">{price}</div><div class="x">prix d\'exemple</div></div>')


BODY = duo2d_body('le malin', 'le pigeon') + '''
  <div class="scene" data-s="0"><div class="hook">Il croyait que le<br><mark>code promo Hacoo</mark><br>servait à <em>rien</em></div></div>
''' + anc('P', '<div class="tag ice" style="left:-150px;top:-150px" data-g="0.1" data-fx="stamp">panier : 63,00 €</div>', '0') + '''
''' + anc('M', '<div class="bub" style="left:-80px;top:-200px" data-g="1.1" data-fx="stamp">?</div>', '1') + '''
  <div class="scene" data-s="2" data-in="pop">''' + prod('Doudoune', 'doudoune', '46 €', '2.0', 100, 230) + prod('Bonnet', 'bonnet', '8 €', '2.1', 380, 210) + prod('Gants', 'gants', '9 €', '2.1', 660, 230) + '''
   <div class="tag" style="left:390px;top:560px" data-g="2.2" data-fx="stamp">= 63,00 €</div></div>
  <div class="scene" data-s="3" data-in="pop">
   <div class="phone" style="left:270px;top:230px" data-g="3.0" data-fx="up"><div class="t">CODE PROMO HACOO</div>
    <div class="f"><span data-g="3.0" data-fx="type">hzklink</span></div><div class="ok" data-g="3.3" data-fx="fade">✓ -14 % appliqué</div></div>
  </div>
''' + anc('P', '<div class="tag green" style="left:-120px;top:-170px" data-g="4.1" data-fx="stamp">-8,82 €</div>', '4') + '''
  <div class="scene" data-s="5" data-in="pop">''' + prod('Bonnet', 'bonnet', '8 €', '5.1', 400, 230, 280) + '''
   <div class="tag red" style="left:590px;top:250px;transform:rotate(-12deg)" data-g="5.2" data-fx="stamp">PAYÉ</div></div>
  <div class="scene" data-s="6" data-in="pop">
   <div class="tag" style="left:380px;top:220px" data-g="6.0" data-fx="pop"><s>63,00 €</s>-14 %</div>
   <div class="card" style="left:240px;top:320px;width:600px;padding:18px 0" data-g="6.0" data-fx="stamp" data-slow="6.0"><div class="t">avec le code promo hacoo</div><div class="p" style="font-size:120px;color:#2f8fd0">54,18 €</div><div class="x"><span style="text-transform:none">hzklink</span> · -8,82 € · prix d'exemple</div></div>
  </div>
  <div class="scene" data-s="7" data-in="pop" style="z-index:7">
   <div class="endc" style="top:205px;left:95px;width:820px" data-g="7.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div>
    <div class="b" data-g="7.4" data-fx="pop">liens des articles tendance en bio</div><div class="x">Prix d'exemple · -14 % avec le code promo Hacoo hzklink · Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
   <div class="note" style="left:170px;top:738px;font-size:30px;transform:rotate(-2deg)" data-g="7.1" data-fx="pop">envoie-la au pote qui dit « ça sert à rien »</div>
  </div>
'''
