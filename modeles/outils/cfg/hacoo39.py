import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo import *
from hacoo_items import icon
# Hacoo n°3 du 20/11/2026 - style D « Duo 3D » (1re vidéo 3D depuis que Three.js r149 est embarqué dans outils/vendor/).
# Format F10 « la maligne vs le pigeon », thème cadeaux de Noël : le pigeon a fini ses cadeaux plein pot sur l'appli Hacoo.
# Prix d'exemple : écharpe 18 € + pyjama 24 € + guirlande 6 € = 48,00 € ; -14 % = 6,72 € ; total 41,28 €.
# Articles génériques, sans marque ni logo. Fond vert sapin très sombre.
# Voix : la maligne (M) = Soleil (azure, fr-FR-Soleil:MAI-Voice-2.1), le pigeon (P) = Louis (smallest, louis), speed 1.08,
# une synthèse par réplique, silences internes plafonnés à 0,24 s, atempo 1.12 (Soleil) / 1.04 (Louis).
# Soleil avale « euros » dans les montants (transcription « six soixante-douze ») : c'est le pigeon qui dit les montants.
NAME = 'hacoo39'
TITLE = 'Hacoo duo 3D cadeaux de Noel'
HEAD = THREE
LINES = [
 ("Sur l'appli Hacou, j'ai fini mes cadeaux de Noël !", [("Sur l'appli <em>Hacoo</em>,", None), ("j'ai fini mes", None), ("cadeaux de <em>Noël !</em>", None)]),
 ("Ah ouais ? T'as payé combien ?", [("Ah ouais ?", None), ("T'as payé <em>combien ?</em>", None)]),
 ("Écharpe, pyjama, guirlande : quarante-huit euros.", [("Écharpe, pyjama,", None), ("guirlande :", None), ("<em>48&nbsp;€</em>", None)]),
 ("Et t'as tapé le code promo Hacou ?", [("Et t'as tapé", None), ("le <em>code promo Hacoo ?</em>", None)]),
 ("Y'a un code ?!", [("Y'a un <em>code ?!</em>", None)]),
 ("Code promo Hacou : H, Z, K, link. Et c'est moins quatorze pour cent.", [("<em>Code promo Hacoo</em>", None), ("<i>hzklink</i>.", None), ("Et c'est", None), ("<em>-14&nbsp;%</em>", None)]),
 ("Attends... ça fait six euros soixante-douze de moins ?!", [("Attends...", None), ("ça fait", None), ("<em>6,72&nbsp;€</em> de moins&nbsp;?!", None)]),
 ("Eh oui. Et regarde ton nouveau total.", [("Eh oui.", None), ("Et regarde ton", None), ("nouveau <em>total</em>.", None)]),
 ("Quarante et un euros vingt-huit ?! J'aurais pu acheter un cadeau en plus !", [("<i>41,28&nbsp;€&nbsp;?!</i>", None), ("J'aurais pu acheter", None), ("un <em>cadeau</em> en&nbsp;plus&nbsp;!", None)]),
 ("Envoie-la à ton pote avant Noël. Code promo Hacou, H, Z, K, link. Les liens sont dans ma bio.", [("Envoie-la à ton pote", None), ("avant <em>Noël</em>.", None), ("<em>Code promo Hacoo</em>", None), ("<i>hzklink</i>.", None), ("Les liens sont", None), ("dans ma <em>bio</em>.", None)]),
]
SPLITS = [(0.2, 2.665), (3.115, 4.067), (4.517, 7.102), (7.552, 8.638), (9.088, 9.659), (10.109, 14.581), (15.031, 17.604), (18.054, 19.777), (20.227, 23.032), (23.482, 29.978)]
MINLEN = 0.9
GAP = 0.12
TAIL = 2.6
DUO_LINES = [
 {'who': 'P', 'M': 'idle', 'P': 'hip', 'shot': 'wide'},
 {'who': 'M', 'M': 'think', 'P': 'hip', 'shot': 'M'},
 {'who': 'P', 'M': 'idle', 'P': 'talk', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'point', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'hip', 'P': 'shock', 'shot': 'P'},
 {'who': 'M', 'M': 'talk', 'P': 'shock', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'hip', 'P': 'think', 'shot': 'P'},
 {'who': 'M', 'M': 'cool', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'shrug', 'P': 'head', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'talk', 'P': 'idle', 'shot': 'wide'},
]
JS = duo_js(DUO_LINES, bg=0x07120d)

CSS = '''
#sub{font-size:82px}
#sub i{text-transform:none}
.hook{top:240px;font-size:74px}
.hook em.g{background:#1f8a4c}
#bgtex,#stage,html,body{background:#07120d}
'''


def prod(ic, name, price, g, x, y, w=300):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;padding:12px 0 14px" data-g="{g}" data-fx="pop">'
            f'{icon(ic, 150)}<div class="t">{name}</div><div class="p" style="font-size:66px">{price}</div><div class="x">prix d\'exemple</div></div>')


BODY = duo_body('LA MALIGNE', 'LE PIGEON') + '''
  <div class="scene" data-s="0"><div class="hook">Ses cadeaux de <em class="g">Noël</em><br>sur <em>Hacoo</em>… plein&nbsp;pot&nbsp;?</div></div>
  <div class="scene" data-s="2" data-in="pop">''' + prod('Écharpe', 'écharpe', '18 €', '2.0', 70, 190) + prod('Pyjama', 'pyjama', '24 €', '2.0', 390, 160) + prod('Guirlande', 'guirlande', '6 €', '2.1', 710, 190) + '''
   <div class="tag" style="left:330px;top:620px;font-size:64px" data-g="2.2" data-fx="stamp">total 48,00 €</div></div>
''' + anc('M', '<div class="tag" style="left:-250px;top:-150px" data-g="1.1" data-fx="pop">combien ?</div>', '1') + '''
''' + anc('M', '''<div class="phone" style="left:-260px;top:-360px" data-g="3.1" data-fx="up"><div class="t">CODE PROMO HACOO</div>
   <div class="f"><span style="color:#b9b4aa;font:700 40px Inter">Ajouter un code</span></div><div class="ok" style="color:#e5322d">case vide</div></div>''', '3') + '''
''' + anc('P', '<div class="bub" style="left:-95px;top:-230px" data-g="4.0" data-fx="stamp">?!</div>', '4') + '''
  <div class="scene" data-s="5" data-in="pop">
   <div class="phone" style="left:280px;top:220px" data-g="5.0" data-fx="up"><div class="t">CODE PROMO HACOO</div>
    <div class="f"><span data-g="5.1" data-fx="type">hzklink</span></div><div class="ok" data-g="5.3" data-fx="fade">✓ -14 % appliqué</div></div>
  </div>
''' + anc('P', '<div class="tag red" style="left:-170px;top:-150px;font-size:64px" data-g="6.2" data-fx="stamp">-6,72 €</div>', '6') + '''
  <div class="scene" data-s="8" data-in="pop">
   <div class="tag" style="left:390px;top:200px" data-g="8.0" data-fx="pop"><s>48,00 €</s>-14 %</div>
   <div class="card" style="left:240px;top:300px;width:600px;padding:18px 0" data-g="8.0" data-fx="stamp" data-slow="8.0"><div class="t">avec le code promo hacoo</div><div class="p" style="font-size:120px;color:#1f8a4c">41,28 €</div><div class="x">hzklink · prix d'exemple</div></div>
  </div>
  <div class="scene" data-s="9" data-in="pop" style="z-index:7">
   <div class="endc" data-g="9.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div>
    <div class="b" data-g="9.4" data-fx="pop">liens des articles tendance en bio</div><div class="x">Prix d'exemple · -14 % avec le code promo Hacoo hzklink · Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
  </div>
'''
