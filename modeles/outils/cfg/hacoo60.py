import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo import *
from hacoo_items import icon, ICONS
# baskets sans bandes obliques (lacets en points) pour éviter toute ressemblance avec une marque
ICONS = dict(ICONS)
import hacoo_items
hacoo_items.ICONS = ICONS
ICONS['Baskets'] = ICONS['Baskets'].replace('<path d="M60 98 L70 120 M76 94 L86 118 M92 90 L102 114" stroke="#9aa3b2" stroke-width="5" stroke-linecap="round"/>', '<g fill="#9aa3b2"><circle cx="88" cy="96" r="4"/><circle cx="100" cy="90" r="4"/><circle cx="112" cy="86" r="4"/></g>')
# Hacoo n°2 du 26/11/2026 - style D « Duo 3D » (brief veille du 26/11, vidéo 2), format F1 STOP « Première commande sur l'appli ? Il allait oublier ça ».
# Le pigeon va payer sa 1re commande, le malin l'arrête : la case code promo avant de payer -> code du jour HACOO847 (demande de Badr du 26/11 :
# code mis en évidence, aujourd'hui seulement, -14 %, écrit à l'image par exception) -> baskets 49 € + sacoche 16 € + gourde 11 € = 76,00 €
# -> -10,64 € -> 65,36 € (ralenti) -> « enregistre pour ta première commande ». Sol bleu nuit, accent orange vif.
# Prix d'exemple : 76,00 × 0,14 = 10,64 ; 76,00 × 0,86 = 65,36. Articles génériques, sans marque ni logo. « Hacoo » écrit seulement dans le code du jour.
# Voix : le malin (M) = cosmo (xai), le pigeon (P) = Mathieu (inworld), speed 1.1, une synthèse par réplique, silences coupés,
# atempo 1.1, recollées avec 0,2 s au début et 0,45 s entre les répliques (SPLITS). Réplique « Quelle case ? » remplacée par la bulle « ?! ».
NAME = 'hacoo60'
TITLE = 'Duo 3D premiere commande'
HEAD = THREE
LINES = [
 ("Ma première commande sur l'appli Hacou, je paie direct !", [("Ma <em>première</em>", None), ("commande", None), ("sur l'appli,", None), ("je paie direct&nbsp;!", None)]),
 ("Stop ! T'as rempli la case code promo ?", [("<em>Stop&nbsp;!</em>", None), ("T'as rempli la case", None), ("<em>code promo&nbsp;?</em>", None)]),
 ("Avant de payer, sur la page de commande, t'as une case code promo.", [("Avant de payer,", None), ("sur la page", None), ("de commande,", None), ("une case <em>code promo.</em>", None)]),
 ("Aujourd'hui seulement : code promo Hacou huit cent quarante-sept. Moins quatorze pour cent.", [("<em>Aujourd'hui</em> seulement :", None), ("code promo", None), ("<i>HACOO847</i>.", None), ("<em>-14&nbsp;%</em>", None)]),
 ("Mes baskets, ma sacoche et ma gourde… soixante-seize euros.", [("Mes baskets,", None), ("ma sacoche", None), ("et ma gourde…", None), ("<em>76&nbsp;€.</em>", None)]),
 ("Ça fait dix euros soixante-quatre de moins.", [("Ça fait", None), ("<em>10,64&nbsp;€</em>", None), ("de moins.", None)]),
 ("Soixante-cinq euros et trente-six centimes ? Et je l'avais pas vue !", [("<i>65,36&nbsp;€&nbsp;?</i>", None), ("Et je l'avais", None), ("pas <em>vue&nbsp;!</em>", None)]),
 ("Enregistre la vidéo pour ta première commande. Code promo Hacou huit cent quarante-sept, aujourd'hui seulement.", [("<em>Enregistre</em> la vidéo", None), ("pour ta première", None), ("commande.", None), ("Code promo", None), ("<i>HACOO847</i>,", None), ("<em>aujourd'hui</em> seulement.", None)]),
]
SPLITS = [(0.2, 2.46), (2.91, 4.61), (5.06, 8.23), (8.68, 12.74), (13.19, 16.04), (16.49, 18.09), (18.54, 21.01), (21.46, 26.41)]
MINLEN = 0.9
GAP = 0.12
TAIL = 2.6
DUO_LINES = [
 {'who': 'P', 'M': 'idle', 'P': 'talk', 'shot': 'wide'},
 {'who': 'M', 'M': 'point', 'P': 'shock', 'shot': 'M'},
 {'who': 'M', 'M': 'talk', 'P': 'think', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'cool', 'P': 'idle', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'idle', 'P': 'think', 'shot': 'P'},
 {'who': 'M', 'M': 'hip', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'cool', 'P': 'shock', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'point', 'P': 'cool', 'shot': 'wide', 'lbl': False},
]
JS = duo_js(DUO_LINES, bg=0x060c1c)

CSS = '''
#sub{font-size:76px;left:70px;width:860px}
#sub i{text-transform:none}
#sub em,.hook em{background:#ff7a00}
.hook{top:225px;font-size:64px;left:90px;width:840px}
#bgtex,#stage,html,body{background:#060c1c}
.phone.big{width:620px;height:400px}
.endc{left:110px;width:810px}
.endc .c{color:#ff7a00}
.first{position:absolute;padding:10px 24px;border-radius:18px;background:#ff7a00;color:#fff;font:900 46px 'Inter',sans-serif;white-space:nowrap;box-shadow:0 8px 0 rgba(0,0,0,.35)}
.stop{position:absolute;width:230px;height:230px;background:#e5322d;color:#fff;clip-path:polygon(30% 0,70% 0,100% 30%,100% 70%,70% 100%,30% 100%,0 70%,0 30%);display:flex;align-items:center;justify-content:center;font:900 64px 'Inter',sans-serif}
.today{position:absolute;padding:10px 26px;border-radius:18px;background:#e5322d;color:#fff;font:900 40px 'Inter',sans-serif;white-space:nowrap;transform:rotate(-4deg);box-shadow:0 8px 0 rgba(0,0,0,.35)}
'''


def prod(ic, name, price, g, x, y, w=260):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;padding:12px 0 14px" data-g="{g}" data-fx="pop">'
            f'{icon(ic, 120)}<div class="t">{name}</div><div class="p" style="font-size:56px">{price}</div><div class="x">prix d\'exemple</div></div>')


BODY = duo_body('LE MALIN', 'LE PIGEON') + '''
  <div class="scene" data-s="0"><div class="hook">Première commande<br>sur l'appli ?<br>Il allait oublier <em>ça</em></div></div>
''' + anc('P', '<div class="first" style="left:-120px;top:-40px;transform:rotate(-5deg)" data-g="0.0" data-fx="pop">1re COMMANDE</div>', '0') + '''
''' + anc('M', '<div class="stop" style="left:-115px;top:-250px" data-g="1.0" data-fx="stamp">STOP</div>', '1') + '''
  <div class="scene" data-s="2" data-in="pop">
   <div class="phone big" style="left:220px;top:240px" data-g="2.0" data-fx="up"><div class="t">PAGE DE COMMANDE</div>
    <div class="f" style="font-size:40px;color:#9ca3af" data-g="2.3" data-fx="pop">CODE PROMO : ________</div><div class="ok" style="color:#ff7a00" data-g="2.3" data-fx="fade">↑ avant « Payer »</div></div>
  </div>
  <div class="scene" data-s="3" data-in="pop">
   <div class="today" style="left:330px;top:200px" data-g="3.0" data-fx="stamp">AUJOURD'HUI SEULEMENT</div>
   <div class="phone big" style="left:220px;top:290px" data-g="3.0" data-fx="up"><div class="t">CODE PROMO DU JOUR</div>
    <div class="f"><span data-g="3.2" data-fx="type">HACOO847</span></div><div class="ok" data-g="3.3" data-fx="fade">✓ code appliqué · -14 %</div></div>
  </div>
  <div class="scene" data-s="4" data-in="pop">''' + prod('Baskets', 'baskets', '49 €', '4.0', 60, 250) + prod('Sacoche', 'sacoche', '16 €', '4.1', 360, 225) + prod('Gourde', 'gourde', '11 €', '4.2', 660, 250) + '''
   <div class="tag" style="left:380px;top:560px" data-g="4.3" data-fx="stamp">= 76,00 €</div></div>
''' + anc('M', '<div class="tag red" style="left:-170px;top:-150px;font-size:64px" data-g="5.1" data-fx="stamp">-10,64 €</div>', '5') + '''
  <div class="scene" data-s="6" data-in="pop">
   <div class="tag" style="left:390px;top:200px" data-g="6.0" data-fx="pop"><s>76,00 €</s>-14 %</div>
   <div class="card" style="left:250px;top:300px;width:580px;padding:18px 0" data-g="6.0" data-fx="stamp" data-slow="6.0"><div class="t">avec le code du jour</div><div class="p" style="font-size:120px;color:#ff7a00">65,36 €</div><div class="x"><span style="text-transform:none">HACOO847</span> · prix d'exemple</div></div>
  </div>
  <div class="scene" data-s="7" data-in="pop" style="z-index:7">
   <div class="endc" data-g="7.0" data-fx="up"><div class="k">CODE PROMO DU JOUR</div><div class="c">HACOO847</div><div class="d">-14 % · aujourd'hui seulement</div>
    <div class="b" data-g="7.3" data-fx="pop">liens des articles tendance en bio</div><div class="x">Prix d'exemple · -14 % avec le code promo HACOO847<br>Offre soumise aux conditions en vigueur</div></div>
  </div>
'''
