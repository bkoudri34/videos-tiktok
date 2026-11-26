import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parraine import *
# Fortuneo, 26/11/2026 (vidéo A) - style v3 nuit & or, accent améthyste. Format F18 « Parraine à ton tour » (règles de Badr du 26/11) :
# mascotte ronde à écharpe dorée -> 1 je te parraine en privé -> 2 tu ouvres ton compte (carte Gold, checklist des conditions)
# -> 3 une fois client, ton propre code parrain -> 4 tu le partages à tes amis (un seul niveau, plafond fixé par la banque, ralenti)
# -> « je ne touche rien sur les amis de mes filleuls » -> appel à l'action discret. AUCUN montant écrit : montants à l'oral seulement.
# Source (fortuneo.fr/parrainage, consultée le 26/11/2026) : offre du 01/11 au 30/11/2026 ; filleul 150 € avec Gold CB Mastercard (80 € Fosfo),
# 1re ouverture, code parrain renseigné, versement de 300 € dans les 6 jours ; parrain 120 € (Gold) / 80 € (Fosfo), jusqu'à 10 filleuls par an.
# Pas de total annoncé : l'offre se termine le 30/11 (moins de 12 mois).
# Voix : Speko (voix par défaut), speed 1.08, atempo 1.12, silences internes plafonnés à 0,22 s ; réplique 5 refaite (« dix amis par an »).
NAME = 'fortuneo17'
TITLE = 'Fortuneo parraine a ton tour amethyste'
ROOT = ':root{--bg:#07040b;--ac:#c39bff}'
LINES = [
 ("Parrainage Fortunéo : bientôt, c'est toi qui parraines.", [("Parrainage Fortuneo :", None), ("bientôt,", None), ("c'est toi qui parraines.", None)]),
 ("Un : je te parraine, en privé.", [("1 :", None), ("je te parraine,", None), ("en privé.", None)]),
 ("Deux : tu ouvres ton compte avec la carte Gold. Jusqu'à cent cinquante euros de prime de bienvenue, si tu remplis les conditions.", [("2 : tu ouvres ton compte", None), ("avec la carte Gold.", None), ("Jusqu'à … de prime de bienvenue,", None), ("si tu remplis les conditions.", None)]),
 ("Trois : une fois client, tu as ton propre code parrain.", [("3 :", None), ("une fois client,", None), ("ton propre code parrain.", None)]),
 ("Quatre : tu le partages à tes amis. Jusqu'à cent vingt euros par ami qui remplit les conditions, dans la limite de dix amis par an, fixée par la banque.", [("4 : tu le partages", None), ("à tes amis.", None), ("par ami qui remplit les conditions,", None), ("dans la limite fixée", None), ("par la banque.", None)]),
 ("Un seul niveau : je ne touche rien sur les amis de mes filleuls.", [("Un seul niveau :", None), ("je ne touche rien", None), ("sur les amis de mes filleuls.", None)]),
 ("Si tu veux que je te parraine, écris-moi en privé.", [("Si tu veux", None), ("que je te parraine,", None), ("écris-moi en privé.", None)]),
]
SPLITS = [(0.2, 2.35), (2.8, 4.21), (4.66, 9.29), (9.74, 11.74), (12.19, 18.04), (18.49, 20.76), (21.21, 22.77)]
MINLEN = 1.6
GAP = 0.3
TAIL = 1.9

CSS = PCSS + '''
.am{color:#c39bff;text-shadow:0 0 18px rgba(170,120,255,.55)}
.gcard{position:absolute;width:420px;height:262px;border-radius:26px;background:linear-gradient(135deg,#f6e3a8,#c99a3e 55%,#f1d589);box-shadow:0 30px 70px rgba(0,0,0,.6);transform:rotate(-8deg)}
.gcard:before{content:'';position:absolute;left:40px;top:80px;width:74px;height:56px;border-radius:10px;background:linear-gradient(135deg,#e9e2cf,#a89d82)}
.gcard b{position:absolute;left:40px;bottom:34px;font:900 34px Inter;color:#3a2808;letter-spacing:3px}
.code{position:absolute;left:190px;width:700px;height:150px;border-radius:30px;border:4px dashed #c39bff;background:rgba(30,20,45,.85);display:flex;align-items:center;justify-content:center;gap:24px;font:900 54px 'DejaVu Sans Mono',monospace;color:#f3efe6;letter-spacing:6px;white-space:nowrap}
.code small{font:800 26px Inter;color:#c39bff;letter-spacing:2px}
.lantern{position:absolute;width:16px;height:16px;border-radius:50%;background:#e8c3ff;box-shadow:0 0 26px 10px rgba(190,140,255,.45)}
'''
LANTERNS = ''.join(f'<div class="lantern" style="left:{x}px;top:{y}px"></div>' for x, y in [(130, 560), (320, 520), (760, 540), (930, 600), (520, 500)])
ME = '#c39bff'

BODY = hud('FRANCE · PARRAINE À TON TOUR', 'FORTUNEO') + BANNER + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + LANTERNS + hdx(230, [('h1 am', 'PARRAINAGE FORTUNEO', None, 'font-size:70px'), ('it gold', 'bientôt, c\'est toi', None, 'font-size:74px'), ('it gold', 'qui parraines.', None, 'font-size:74px')]) + mascot(330, 650, 420, ME, 'scarf') + '''
   <div class="bubble2" style="left:640px;top:640px;transform:rotate(6deg)">à ton tour ?</div></div>
  <div class="scene" data-s="1" data-in="right"><div class="floor"></div>''' + '<div class="num" style="left:465px;top:230px" data-g="1.0" data-fx="stamp">1</div>' + hdx(410, [('h1', 'JE TE PARRAINE,', '1.1', 'font-size:72px'), ('it am', 'en privé.', '1.2', 'font-size:74px')]) + mascot(110, 760, 330, ME, 'scarf') + friend(690, 820, 230, '#f3c766', g='1.2') + '''
   <div class="bubble2" style="left:400px;top:760px" data-g="1.1" data-fx="right">✉ invitation</div></div>
  <div class="scene" data-s="2" data-in="up">''' + '<div class="num" style="left:110px;top:230px" data-g="2.0" data-fx="stamp">2</div>' + hdx(250, [('h1', 'TU OUVRES', '2.0', 'font-size:66px'), ('h1', 'TON COMPTE', '2.0', 'font-size:66px')], left=280, width=650) + '''
   <div class="gcard" style="left:330px;top:470px" data-g="2.1" data-fx="pop"><b>CARTE GOLD</b></div>
   <div class="card2" style="left:130px;top:800px;width:780px" data-g="2.2" data-fx="up"><div class="t">Prime de bienvenue</div>
    <div class="chk"><i>✓</i>1re ouverture de compte</div><div class="chk"><i>✓</i>code parrain renseigné</div><div class="chk" data-g="2.3" data-fx="fade"><i>✓</i>versement initial sous 6 jours</div></div>
   <div class="tagp" style="left:250px;top:1270px" data-g="2.3" data-fx="pop">si tu remplis les conditions</div></div>
  <div class="scene" data-s="3" data-in="pop"><div class="floor"></div>''' + '<div class="num" style="left:465px;top:230px" data-g="3.0" data-fx="stamp">3</div>' + hdx(410, [('h1', 'UNE FOIS CLIENT,', '3.1', 'font-size:68px'), ('it am', 'ton propre code parrain.', '3.2', 'font-size:64px')]) + friend(420, 640, 240, '#f3c766') + '''
   <div class="code" style="top:930px" data-g="3.2" data-fx="stamp"><small>CODE PARRAIN</small>• • • • • •</div></div>
  <div class="scene" data-s="4" data-in="right">''' + '<div class="num" style="left:110px;top:230px" data-g="4.0" data-fx="stamp">4</div>' + hdx(260, [('h1', 'TU LE PARTAGES', '4.0', 'font-size:62px'), ('it am', 'à tes amis.', '4.1', 'font-size:66px')], left=280, width=650) + \
    link(540, 760, 240, 1000, '4.1') + link(540, 760, 440, 1060, '4.1') + link(540, 760, 640, 1060, '4.1') + link(540, 760, 840, 1000, '4.1') + \
    friend(420, 560, 240, '#f3c766') + friend(160, 960, 160, ME, g='4.1') + friend(360, 1010, 160, ME, g='4.1') + friend(560, 1010, 160, ME, g='4.1') + friend(760, 960, 160, ME, g='4.1') + '''
   <div class="tagp" style="left:200px;top:1220px" data-g="4.3" data-fx="stamp" data-slow="4.3">plafond fixé par la banque</div>
   <div class="cond" style="top:1310px;color:#cfc3e6" data-g="4.2" data-fx="fade">prime pour chaque ami qui remplit les conditions</div></div>
  <div class="scene" data-s="5" data-in="up">''' + hdx(230, [('h1 am', 'UN SEUL NIVEAU', '5.0', 'font-size:72px'), ('it gold', 'je ne touche rien sur', '5.1', 'font-size:60px'), ('it gold', 'les amis de mes filleuls.', '5.2', 'font-size:60px')]) + \
    mascot(150, 640, 230, ME, 'scarf') + link(380, 760, 520, 760) + friend(520, 680, 170, '#f3c766') + link(690, 765, 800, 900, '5.2') + friend(760, 900, 130, '#9a8fae', g='5.2', cls='grey') + friend(560, 960, 130, '#9a8fae', g='5.2', cls='grey') + link(640, 850, 620, 960, '5.2') + '''
   <div class="x" style="left:790px;top:880px" data-g="5.2" data-fx="stamp">✕</div><div class="x" style="left:590px;top:940px" data-g="5.2" data-fx="stamp">✕</div>
   <div class="cond" style="top:1180px;color:#cfc3e6" data-g="5.1" data-fx="fade">toi → tes amis, c'est tout</div></div>
  <div class="scene" data-s="6" data-in="pop"><div class="floor"></div>''' + LANTERNS + hdx(230, [('h1', 'SI TU VEUX QUE', '6.0', 'font-size:68px'), ('h1', 'JE TE PARRAINE,', '6.1', 'font-size:68px'), ('it gold', 'écris-moi en privé.', '6.2', 'font-size:72px')]) + mascot(380, 640, 320, ME, 'scarf', g='6.2') + '''
   <div class="tagp" style="left:270px;top:1010px" data-g="6.2" data-fx="pop">Offre Fortuneo jusqu'au 30/11</div>
   <div class="cond" style="top:1120px;font-size:24px">Offres soumises aux conditions en vigueur · 1re ouverture,<br>code parrain, versement initial sous 6 jours, compte et carte gardés 1 an</div></div>
'''
