import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo import *
from hacoo_items import icon
# Hacoo n°2 du 21/11/2026 - style D « Duo 3D » (brief veille du 21/11, vidéo 2), format F10 « le code tapé au mauvais endroit ».
# Le pigeon croit que le code promo Hacoo ne marche pas : il l'a tapé dans la barre de recherche. Le malin lui montre la case
# code promo dans la commande -> -11,34 € -> total 69,66 € (ralenti) -> écran de fin. Fond bleu nuit (différent du vert sapin de hacoo39).
# Prix d'exemple : baskets de running 54 € + sacoche 16 € + casquette 11 € = 81,00 € ; -14 % = 11,34 € ; total 69,66 €.
# Articles génériques, sans marque ni logo.
# Voix : le malin (M) = cosmo (xai), le pigeon (P) = Mathieu (inworld), speed 1.1, une synthèse par réplique, silences coupés,
# recollées avec 0,2 s au début et 0,45 s entre les répliques (SPLITS). Répliques 7 et 10 refaites (« onze zéro trente-quatre », « en voilà »).
NAME = 'hacoo42'
TITLE = 'Hacoo duo 3D mauvais endroit'
HEAD = THREE
LINES = [
 ("Le code promo de l'appli Hacou, ça marche pas !", [("Le <em>code promo</em>", None), ("de l'appli <em>Hacoo</em>,", None), ("ça marche pas !", None)]),
 ("Fais voir ton téléphone.", [("Fais voir", None), ("ton <em>téléphone</em>.", None)]),
 ("Regarde, j'ai bien tapé H, Z, K, link.", [("Regarde,", None), ("j'ai bien tapé", None), ("<i>hzklink</i>.", None)]),
 ("Mais t'as tapé ça dans la recherche !", [("Mais t'as tapé ça", None), ("dans la <em>recherche !</em>", None)]),
 ("Bah... c'est pas là ?", [("Bah...", None), ("c'est pas <em>là ?</em>", None)]),
 ("La case code promo, c'est dans ta commande, juste avant de payer.", [("La case <em>code promo</em>,", None), ("c'est dans ta commande,", None), ("juste avant de <em>payer</em>.", None)]),
 ("Ah ! Ça fait onze euros trente-quatre de moins !", [("Ah ! Ça fait", None), ("<em>11,34&nbsp;€</em> de moins&nbsp;!", None)]),
 ("Et regarde ton total.", [("Et regarde", None), ("ton <em>total</em>.", None)]),
 ("Soixante-neuf euros soixante-six ?! J'ai failli payer onze euros de trop !", [("<i>69,66&nbsp;€&nbsp;?!</i>", None), ("J'ai failli payer", None), ("<em>11&nbsp;€</em> de&nbsp;trop&nbsp;!", None)]),
 ("Envoie cette vidéo à ton pote. Code promo Hacou, H, Z, K, link. Les liens sont dans ma bio.", [("Envoie cette vidéo", None), ("à ton <em>pote</em>.", None), ("<em>Code promo Hacoo</em>", None), ("<i>hzklink</i>.", None), ("Les liens sont", None), ("dans ma <em>bio</em>.", None)]),
]
SPLITS = [(0.2, 2.306), (2.756, 3.78), (4.23, 7.911), (8.361, 9.872), (10.322, 11.686), (12.136, 15.432), (15.882, 18.112), (18.562, 19.569), (20.019, 23.637), (24.087, 30.308)]
MINLEN = 0.9
GAP = 0.12
TAIL = 2.6
DUO_LINES = [
 {'who': 'P', 'M': 'idle', 'P': 'shock', 'shot': 'wide'},
 {'who': 'M', 'M': 'think', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'idle', 'P': 'talk', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'head', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'hip', 'P': 'shrug', 'shot': 'P', 'lbl': False},
 {'who': 'M', 'M': 'point', 'P': 'idle', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'hip', 'P': 'think', 'shot': 'P'},
 {'who': 'M', 'M': 'cool', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'shrug', 'P': 'head', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'talk', 'P': 'idle', 'shot': 'wide', 'lbl': False},
]
JS = duo_js(DUO_LINES, bg=0x060a1a)

CSS = '''
#sub{font-size:80px}
#sub i{text-transform:none}
.hook{top:225px;font-size:58px}
#bgtex,#stage,html,body{background:#060a1a}
.phone.big{width:640px;height:380px}
.phone .f svg{margin-right:18px;flex:none}
.phone .f.srch{border:6px solid #e5322d}
.phone .ok.no{color:#ff6b6b}
'''
LOUPE = '<svg width="54" height="54" viewBox="0 0 50 50"><circle cx="21" cy="21" r="14" fill="none" stroke="#111" stroke-width="6"/><path d="M31 31 L44 44" stroke="#111" stroke-width="7" stroke-linecap="round"/></svg>'


def prod(ic, name, price, g, x, y, w=280):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;padding:12px 0 14px" data-g="{g}" data-fx="pop">'
            f'{icon(ic, 130)}<div class="t">{name}</div><div class="p" style="font-size:60px">{price}</div><div class="x">prix d\'exemple</div></div>')


BODY = duo_body('LE MALIN', 'LE PIGEON') + '''
  <div class="scene" data-s="0"><div class="hook">Il a tapé le code promo<br><em>Hacoo</em> au mauvais endroit</div></div>
''' + anc('P', '<div class="tag" style="left:70px;top:60px;font-size:58px" data-g="0.1" data-fx="stamp">81,00 €</div>', '0') + '''
''' + anc('M', '<div class="tag" style="left:-120px;top:-140px" data-g="1.1" data-fx="pop">montre ?</div>', '1') + '''
  <div class="scene" data-s="2" data-in="pop">
   <div class="phone big" style="left:220px;top:230px" data-g="2.0" data-fx="up"><div class="t">BARRE DE RECHERCHE</div>
    <div class="f srch">''' + LOUPE + '''<span data-g="2.2" data-fx="type">hzklink</span></div><div class="ok no" data-g="2.2" data-fx="fade">0 résultat</div></div>
  </div>
''' + anc('M', '<div class="bub" style="left:-95px;top:-230px" data-g="3.0" data-fx="stamp">?!</div>', '3') + '''
  <div class="scene" data-s="4" data-in="pop">''' + prod('Baskets', 'baskets', '54 €', '4.0', 40, 250) + prod('Sacoche', 'sacoche', '16 €', '4.0', 350, 225) + prod('Casquette', 'casquette', '11 €', '4.1', 660, 250) + '''</div>
  <div class="scene" data-s="5" data-in="pop">
   <div class="phone big" style="left:220px;top:230px" data-g="5.0" data-fx="up"><div class="t">MA COMMANDE · CODE PROMO HACOO</div>
    <div class="f"><span data-g="5.1" data-fx="type">hzklink</span></div><div class="ok" data-g="5.2" data-fx="fade">✓ juste avant Payer</div></div>
  </div>
''' + anc('P', '<div class="tag red" style="left:-170px;top:-150px;font-size:64px" data-g="6.1" data-fx="stamp">-11,34 €</div>', '6') + '''
''' + anc('M', '<div class="tag" style="left:-110px;top:-140px" data-g="7.1" data-fx="pop">total ?</div>', '7') + '''
  <div class="scene" data-s="8" data-in="pop">
   <div class="tag" style="left:390px;top:200px" data-g="8.0" data-fx="pop"><s>81,00 €</s>-14 %</div>
   <div class="card" style="left:240px;top:300px;width:600px;padding:18px 0" data-g="8.0" data-fx="stamp" data-slow="8.0"><div class="t">avec le code promo hacoo</div><div class="p" style="font-size:120px;color:#1d4ed8">69,66 €</div><div class="x">hzklink · prix d'exemple</div></div>
  </div>
  <div class="scene" data-s="9" data-in="pop" style="z-index:7">
   <div class="endc" data-g="9.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div>
    <div class="b" data-g="9.4" data-fx="pop">liens des articles tendance en bio</div><div class="x">Prix d'exemple · -14 % avec le code promo Hacoo hzklink · Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
  </div>
'''
