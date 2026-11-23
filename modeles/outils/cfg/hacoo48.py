import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo import *
from hacoo_items import icon, ICONS
# baskets sans bandes obliques (lacets en points) pour éviter toute ressemblance avec une marque
ICONS = dict(ICONS)
import hacoo_items
hacoo_items.ICONS = ICONS
ICONS['Baskets'] = ICONS['Baskets'].replace('<path d="M60 98 L70 120 M76 94 L86 118 M92 90 L102 114" stroke="#9aa3b2" stroke-width="5" stroke-linecap="round"/>', '<g fill="#9aa3b2"><circle cx="88" cy="96" r="4"/><circle cx="100" cy="90" r="4"/><circle cx="112" cy="86" r="4"/></g>')
# Hacoo n°2 du 23/11/2026 - style D « Duo 3D » (brief veille du 23/11, vidéo 2), format F10 « il compare tout… sauf le code ».
# Le pigeon a comparé 10 fois les prix mais n'a jamais regardé la case code promo ; le malin lui montre le panier, tape hzklink
# -> -10,92 € (la gourde à 9 € est « payée ») -> total 67,08 € (ralenti) -> écran de fin. Fond bleu nuit, accent orange corail.
# Prix d'exemple : baskets 52 € + sacoche 17 € + gourde 9 € = 78,00 € ; -14 % = 10,92 € ; total 67,08 €. Articles génériques, sans marque ni logo.
# Voix : le malin (M) = cosmo (xai), le pigeon (P) = Mathieu (inworld), speed 1.1, une synthèse par réplique, silences coupés,
# atempo 1.1, recollées avec 0,2 s au début et 0,4 s entre les répliques (SPLITS). Réplique « Quelle case ? » retirée (durée), remplacée par la bulle « ?! ».
NAME = 'hacoo48'
TITLE = 'Hacoo duo 3D compare tout'
HEAD = THREE
LINES = [
 ("J'ai comparé dix fois les prix sur l'appli Hacou. Je suis trop fort.", [("J'ai comparé", None), ("<em>10 fois</em> les prix", None), ("sur l'appli <em>Hacoo</em>.", None), ("Je suis trop fort.", None)]),
 ("Et la case code promo, tu l'as regardée ?", [("Et la case", None), ("<em>code promo</em>,", None), ("tu l'as regardée&nbsp;?", None)]),
 ("Ton panier : baskets, sacoche, gourde. Soixante-dix-huit euros.", [("Ton panier :", None), ("baskets, sacoche,", None), ("gourde.", None), ("<em>78&nbsp;€.</em>", None)]),
 ("Tu tapes H, Z, K, link dans la case code promo Hacou, et tu appliques.", [("Tu tapes", None), ("<i>hzklink</i>", None), ("dans la case", None), ("<em>code promo Hacoo,</em>", None), ("et tu appliques.", None)]),
 ("Attends… ça fait dix euros quatre-vingt-douze de moins ?!", [("Attends…", None), ("ça fait", None), ("<em>10,92&nbsp;€</em> de moins&nbsp;?!", None)]),
 ("Ta gourde est payée, et il te reste de la monnaie.", [("Ta gourde", None), ("est <em>payée</em>,", None), ("et il te reste", None), ("de la monnaie.", None)]),
 ("Soixante-sept euros et huit centimes… j'ai comparé pour rien !", [("<i>67,08&nbsp;€…</i>", None), ("j'ai comparé", None), ("pour <em>rien&nbsp;!</em>", None)]),
 ("Envoie cette vidéo à ton pote. Code promo Hacou, H Z K link. Les liens sont dans ma bio.", [("Envoie cette vidéo", None), ("à ton <em>pote</em>.", None), ("<em>Code promo Hacoo</em>", None), ("<i>hzklink</i>.", None), ("Les liens sont", None), ("dans ma <em>bio</em>.", None)]),
]
SPLITS = [(0.2, 3.14), (3.54, 5.33), (5.73, 9.33), (9.73, 14.33), (14.73, 17.1), (17.5, 19.65), (20.05, 22.74), (23.14, 28.62)]
MINLEN = 0.9
GAP = 0.12
TAIL = 2.6
DUO_LINES = [
 {'who': 'P', 'M': 'idle', 'P': 'cool', 'shot': 'wide'},
 {'who': 'M', 'M': 'think', 'P': 'idle', 'shot': 'M'},
 {'who': 'M', 'M': 'point', 'P': 'shrug', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'point', 'P': 'idle', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'hip', 'P': 'shock', 'shot': 'P'},
 {'who': 'M', 'M': 'cool', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'shrug', 'P': 'head', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'talk', 'P': 'idle', 'shot': 'wide', 'lbl': False},
]
JS = duo_js(DUO_LINES, bg=0x07101f)

CSS = '''
#sub{font-size:76px;left:70px;width:860px}
#sub i{text-transform:none}
#sub em,.hook em{background:#ff6b4a}
.hook{top:225px;font-size:62px;left:90px;width:840px}
#bgtex,#stage,html,body{background:#07101f}
.phone.big{width:600px;height:380px}
.endc{left:110px;width:810px}
.endc .c{color:#ff5a36}
.mini{position:absolute;padding:6px 18px;border-radius:14px;background:#fff;color:#111;font:900 40px 'Inter',sans-serif;box-shadow:0 8px 0 rgba(0,0,0,.35);white-space:nowrap}
.mini s{text-decoration-color:#ff5a36;text-decoration-thickness:5px}
.paid{position:absolute;left:140px;top:-5px;padding:4px 16px;border:7px solid #2fa35a;color:#2fa35a;border-radius:12px;font:900 50px 'Inter',sans-serif;background:rgba(255,255,255,.9);transform:rotate(-12deg)}
'''


def prod(ic, name, price, g, x, y, w=260):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;padding:12px 0 14px" data-g="{g}" data-fx="pop">'
            f'{icon(ic, 120)}<div class="t">{name}</div><div class="p" style="font-size:56px">{price}</div><div class="x">prix d\'exemple</div></div>')


BODY = duo_body('LE MALIN', 'LE PIGEON') + '''
  <div class="scene" data-s="0"><div class="hook">Il compare tout…<br>sauf le<br><em>code promo Hacoo</em></div></div>
''' + anc('P', '<div class="mini" style="left:-220px;top:60px;transform:rotate(-6deg)" data-g="0.0" data-fx="pop"><s>54 €</s> 52 €</div><div class="mini" style="left:30px;top:-40px;transform:rotate(5deg)" data-g="0.1" data-fx="pop"><s>19 €</s> 17 €</div><div class="mini" style="left:210px;top:70px;transform:rotate(-3deg)" data-g="0.2" data-fx="pop"><s>10 €</s> 9 €</div>', '0') + '''
''' + anc('P', '<div class="bub" style="left:-95px;top:-230px" data-g="1.2" data-fx="stamp">?!</div>', '1') + '''
  <div class="scene" data-s="2" data-in="pop">''' + prod('Baskets', 'baskets', '52 €', '2.1', 60, 250) + prod('Sacoche', 'sacoche', '17 €', '2.1', 360, 225) + prod('Gourde', 'gourde', '9 €', '2.2', 660, 250) + '''
   <div class="tag" style="left:380px;top:560px" data-g="2.3" data-fx="stamp">= 78,00 €</div></div>
  <div class="scene" data-s="3" data-in="pop">
   <div class="phone big" style="left:230px;top:230px" data-g="3.0" data-fx="up"><div class="t">CODE PROMO HACOO</div>
    <div class="f"><span data-g="3.1" data-fx="type">hzklink</span></div><div class="ok" data-g="3.4" data-fx="fade">✓ code appliqué · -14 %</div></div>
  </div>
''' + anc('P', '<div class="tag red" style="left:-170px;top:-150px;font-size:64px" data-g="4.2" data-fx="stamp">-10,92 €</div>', '4') + '''
''' + anc('M', '<div class="card" style="left:-130px;top:-200px;width:240px;padding:10px 0;position:absolute" data-g="5.0" data-fx="pop">' + icon('Gourde', 120) + '<div class="t">gourde 9 €</div><div class="paid" data-g="5.1" data-fx="stamp">PAYÉE</div></div>', '5') + '''
  <div class="scene" data-s="6" data-in="pop">
   <div class="tag" style="left:390px;top:200px" data-g="6.0" data-fx="pop"><s>78,00 €</s>-14 %</div>
   <div class="card" style="left:250px;top:300px;width:580px;padding:18px 0" data-g="6.0" data-fx="stamp" data-slow="6.0"><div class="t">avec le code promo hacoo</div><div class="p" style="font-size:120px;color:#ff5a36">67,08 €</div><div class="x"><span style="text-transform:none">hzklink</span> · prix d'exemple</div></div>
  </div>
  <div class="scene" data-s="7" data-in="pop" style="z-index:7">
   <div class="endc" data-g="7.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div>
    <div class="b" data-g="7.4" data-fx="pop">liens des articles tendance en bio</div><div class="x">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
  </div>
'''
