import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parraine import *
# 3 banques, 26/11/2026 (vidéo B) - style v3 nuit & or, accent vert émeraude. Format F9/F2 « comparatif en colonnes » :
# 3 colonnes Hello bank / BoursoBank / Fortuneo dès la 1re image -> fiche Hello bank (conditions) -> date de fin 30/11 15 h
# -> fiche BoursoBank (4 étapes) -> fiche Fortuneo (carte Gold, versement sous 6 jours) -> « compare les conditions, pas seulement la prime »
# (balance, ralenti) -> appel à l'action discret. Règles de Badr du 26/11 : AUCUN montant écrit, offres présentées une par une,
# jamais additionnées, montants à l'oral seulement avec « jusqu'à » et « si tu remplis les conditions ».
# Sources consultées le 26/11/2026 :
#   hellobank.fr/fr/votre-offre-parrainage : filleul « jusqu'à 330 € d'avantages » (80 € ouverture + 50 € le 13e mois avec Hello Prime
#   + bon d'achat 200 € avec Hello Start+), via l'invitation avant le 30/11/2026 15h
#   boursobank.com/bon-plan/parrainage-boursobank : filleul « prime maximale de 300 € » (60 + 80 + 80 + 80, par étapes)
#   fortuneo.fr/parrainage : filleul 150 € avec Gold CB Mastercard, versement de 300 € sous 6 jours, offre du 01/11 au 30/11/2026
# Voix : Speko (voix par défaut), speed 1.08, atempo 1.1, silences internes plafonnés à 0,22 s.
NAME = 'trio16'
TITLE = '3 banques colonnes emeraude'
ROOT = ':root{--bg:#030a07;--ac:#4fd69c}'
LINES = [
 ("Parrainage : Hello bank, Bourso Bank ou Fortunéo, laquelle choisir ?", [("Parrainage :", None), ("Hello bank, BoursoBank ou Fortuneo,", None), ("laquelle choisir ?", None)]),
 ("Hello bank : jusqu'à trois cent trente euros d'avantages, dont un bon d'achat, si tu remplis les conditions.", [("Hello bank :", None), ("jusqu'à … d'avantages,", None), ("dont un bon d'achat,", None), ("si tu remplis les conditions.", None)]),
 ("Mais attention, l'offre s'arrête le trente novembre, à quinze heures.", [("Mais attention,", None), ("l'offre s'arrête le 30 novembre,", None), ("à 15 heures.", None)]),
 ("Bourso Bank : jusqu'à trois cents euros de prime, versés par étapes, si tu remplis les conditions.", [("BoursoBank :", None), ("jusqu'à … de prime,", None), ("versés par étapes,", None), ("si tu remplis les conditions.", None)]),
 ("Fortunéo : jusqu'à cent cinquante euros avec la carte Gold, jusqu'au trente novembre.", [("Fortuneo :", None), ("jusqu'à …", None), ("avec la carte Gold,", None), ("jusqu'au 30 novembre.", None)]),
 ("Mon conseil : compare les conditions, pas seulement la prime.", [("Mon conseil :", None), ("compare les conditions,", None), ("pas seulement la prime.", None)]),
 ("Si tu veux que je te parraine, écris-moi en privé.", [("Si tu veux", None), ("que je te parraine,", None), ("écris-moi en privé.", None)]),
]
SPLITS = [(0.2, 3.19), (3.64, 7.41), (7.86, 10.12), (10.57, 14.14), (14.59, 17.73), (18.18, 20.31), (20.76, 22.61)]
MINLEN = 1.7
GAP = 0.3
TAIL = 1.9

CSS = PCSS + '''
.em{color:#4fd69c;text-shadow:0 0 18px rgba(60,220,150,.5)}
.col{position:absolute;top:720px;width:240px;height:520px;border-radius:30px;border:3px solid rgba(79,214,156,.7);background:linear-gradient(180deg,rgba(20,40,32,.9),rgba(8,14,12,.9));text-align:center;padding-top:40px}
.col b{display:block;font:900 34px Inter;color:#fff;white-space:nowrap}
.col .q{margin-top:110px;font:900 150px 'DejaVu Serif',serif;color:#f3c766;opacity:.85}
.col.hi{border-color:#f3c766;box-shadow:0 0 50px rgba(240,180,80,.35)}
.bank{position:absolute;left:0;width:1080px;text-align:center;font:900 92px Inter;color:#fff;letter-spacing:1px;white-space:nowrap}
.step{position:absolute;left:150px;width:780px;height:120px;border-radius:24px;background:rgba(14,30,24,.92);border:3px solid #4fd69c;display:flex;align-items:center;gap:26px;padding:0 30px;font:800 36px Inter;white-space:nowrap;color:#f3efe6}
.step i{font-style:normal;flex:none;width:76px;height:76px;border-radius:50%;background:#f3c766;color:#141414;display:flex;align-items:center;justify-content:center;font:900 40px 'DejaVu Serif',serif}
.date{position:absolute;left:0;width:1080px;text-align:center}
.date .v{font:900 230px 'DejaVu Serif',serif;line-height:1}
.date .h{font:900 90px 'DejaVu Serif',serif;color:#4fd69c}
.gcard{position:absolute;width:400px;height:250px;border-radius:26px;background:linear-gradient(135deg,#f6e3a8,#c99a3e 55%,#f1d589);box-shadow:0 30px 70px rgba(0,0,0,.6);transform:rotate(6deg)}
.gcard:before{content:'';position:absolute;left:40px;top:76px;width:70px;height:52px;border-radius:10px;background:linear-gradient(135deg,#e9e2cf,#a89d82)}
.gcard b{position:absolute;left:40px;bottom:32px;font:900 32px Inter;color:#3a2808;letter-spacing:3px}
'''
SCALE = '''<svg class="abs" style="left:240px;top:640px" width="600" height="440" viewBox="0 0 600 440" data-g="5.1" data-fx="pop">
 <rect x="292" y="60" width="16" height="330" fill="#e0ac55"/><rect x="200" y="390" width="200" height="22" rx="11" fill="#e0ac55"/>
 <g transform="rotate(-9 300 70)"><rect x="60" y="62" width="480" height="14" rx="7" fill="#f3c766"/>
  <path d="M80 76 L40 200 H180 L140 76" fill="none" stroke="#f3c766" stroke-width="5"/><path d="M30 200 Q110 250 190 200 Z" fill="#4fd69c"/>
  <path d="M460 76 L420 200 H560 L520 76" fill="none" stroke="#f3c766" stroke-width="5"/><path d="M410 200 Q490 250 570 200 Z" fill="#6b6457"/></g>
 <text x="110" y="345" text-anchor="middle" font-family="Inter" font-weight="900" font-size="34" fill="#4fd69c">CONDITIONS</text>
 <text x="490" y="190" text-anchor="middle" font-family="Inter" font-weight="900" font-size="34" fill="#b9b0a0">PRIME</text></svg>'''


def cols(hi=None):
    out = ''
    for k, (x, n) in enumerate([(110, 'HELLO<br>BANK'), (400, 'BOURSO<br>BANK'), (690, 'FORTUNEO')]):
        out += f'<div class="col{" hi" if hi == k else ""}" style="left:{x}px"><b>{n}</b><div class="q">?</div></div>'
    return out


BODY = hud('FRANCE · COMPARATIF', '3 BANQUES') + BANNER + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hdx(230, [('h1 em', 'PARRAINAGE :', None, 'font-size:76px'), ('it gold', 'Hello bank, BoursoBank', None, 'font-size:66px'), ('it gold', 'ou Fortuneo ?', None, 'font-size:66px')]) + cols() + '''</div>
  <div class="scene" data-s="1" data-in="right"><div class="bank" style="top:250px" data-g="1.0" data-fx="stamp">HELLO BANK</div>
   <div class="it gold abs" style="left:0;width:1080px;text-align:center;top:370px;font-size:60px" data-g="1.1" data-fx="tw">des avantages, sous conditions</div>
   <div class="card2" style="left:130px;top:520px;width:800px" data-g="1.1" data-fx="up"><div class="t">Pour le filleul</div>
    <div class="chk"><i>✓</i>offre Hello One ou Hello Prime</div><div class="chk" data-g="1.2" data-fx="fade"><i>✓</i>bon d'achat avec Hello Start+</div>
    <div class="chk" data-g="1.2" data-fx="fade"><i>✓</i>bonus le 13e mois (Hello Prime)</div><div class="chk" data-g="1.3" data-fx="fade"><i>✓</i>via le lien d'invitation</div></div>
   <div class="tagp" style="left:250px;top:1050px" data-g="1.3" data-fx="pop">si tu remplis les conditions</div></div>
  <div class="scene" data-s="2" data-in="pop"><div class="rays" style="top:420px"></div>''' + hdx(240, [('h1', 'MAIS ATTENTION,', '2.0', 'font-size:72px'), ('it em', "l'offre s'arrête le", '2.1', 'font-size:62px')]) + '''
   <div class="date" style="top:520px" data-g="2.1" data-fx="stamp"><div class="v gold">30/11</div></div>
   <div class="date" style="top:780px" data-g="2.2" data-fx="pop"><div class="h">à 15 h</div></div>
   <div class="cond" style="top:940px">offre Hello bank · demande d'ouverture via l'invitation</div></div>
  <div class="scene" data-s="3" data-in="right"><div class="bank" style="top:250px" data-g="3.0" data-fx="stamp">BOURSOBANK</div>
   <div class="it gold abs" style="left:0;width:1080px;text-align:center;top:370px;font-size:60px" data-g="3.2" data-fx="tw">une prime versée par étapes</div>
   <div class="step" style="top:500px" data-g="3.1" data-fx="left"><i>1</i>ouverture du compte</div>
   <div class="step" style="top:640px" data-g="3.2" data-fx="left"><i>2</i>1er versement</div>
   <div class="step" style="top:780px" data-g="3.2" data-fx="left"><i>3</i>carte utilisée 3 mois</div>
   <div class="step" style="top:920px" data-g="3.3" data-fx="left"><i>4</i>EasyMove sous 30 jours</div>
   <div class="tagp" style="left:250px;top:1080px" data-g="3.3" data-fx="pop">si tu remplis les conditions</div></div>
  <div class="scene" data-s="4" data-in="up"><div class="bank" style="top:250px" data-g="4.0" data-fx="stamp">FORTUNEO</div>
   <div class="gcard" style="left:340px;top:410px" data-g="4.2" data-fx="pop"><b>CARTE GOLD</b></div>
   <div class="card2" style="left:130px;top:730px;width:800px" data-g="4.2" data-fx="up"><div class="t">Pour le filleul</div>
    <div class="chk"><i>✓</i>1re ouverture avec la carte Gold</div><div class="chk"><i>✓</i>versement initial sous 6 jours</div>
    <div class="chk" data-g="4.3" data-fx="fade"><i>✓</i>offre jusqu'au 30/11</div></div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="floor"></div>''' + hdx(230, [('h1 em', 'MON CONSEIL :', '5.0', 'font-size:72px'), ('it gold', 'compare les conditions,', '5.1', 'font-size:64px'), ('it gold', 'pas seulement la prime.', '5.2', 'font-size:64px')]) + SCALE + '''
   <div class="tagp" style="left:230px;top:1140px" data-g="5.2" data-fx="stamp" data-slow="5.2">chaque banque a ses conditions</div></div>
  <div class="scene" data-s="6" data-in="pop"><div class="floor"></div>''' + hdx(230, [('h1', 'SI TU VEUX QUE', '6.0', 'font-size:68px'), ('h1', 'JE TE PARRAINE,', '6.1', 'font-size:68px'), ('it em', 'écris-moi en privé.', '6.2', 'font-size:72px')]) + '<div class="abs" style="left:0;top:-100px;width:1080px">' + cols(None).replace('<div class="q">?</div>', '<div class="q" style="font-size:110px;margin-top:80px">✓</div>') + '</div>' + '''
   <div class="cond" style="top:1250px;font-size:24px">Offres soumises aux conditions en vigueur · offres présentées<br>une par une, non additionnées · Hello bank et Fortuneo : jusqu'au 30/11</div></div>
'''
