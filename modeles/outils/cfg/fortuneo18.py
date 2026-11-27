import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parraine import *
# Fortuneo, 27/11/2026 (vidéo C) - style v3 nuit & or, accent rouge signal. Format F5 « chrono » : page de calendrier « 30 NOV »
# dès la 1re image -> 3 points à vérifier avant la date (dossier complet, code parrain, versement initial sous 6 jours) -> carte Gold
# (prime de bienvenue dite à l'oral, le seul ralenti) -> garder compte et carte 1 an -> appel discret. Pas de mascotte.
# AUCUN montant écrit (ni la prime, ni le versement initial) : à l'oral seulement.
# Source (fortuneo.fr/parrainage, consultée le 27/11/2026) : offre du 01/11 au 30/11/2026 (dossier complet reçu au plus tard le 30/11) ;
# filleul 150 € pour une 1re ouverture avec Gold CB Mastercard (80 € Fosfo), code parrain renseigné à la souscription, versement initial
# de 300 € dans les 6 jours suivant l'ouverture, compte et carte conservés au moins un an ; parrain 120 € (Gold), 10 filleuls par an.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08, une synthèse par réplique, atempo 1.15, -19 dB moyen.
NAME = 'fortuneo18'
TITLE = 'Fortuneo chrono 30 novembre rouge'
ROOT = ':root{--bg:#0b0404;--ac:#ff5a4f}'
LINES = [
 ("Parrainage Fortunéo : l'offre actuelle s'arrête le trente novembre.", [("Parrainage Fortuneo :", None), ("l'offre actuelle s'arrête", None), ("le 30 novembre.", None)]),
 ("Avant, vérifie ces trois points.", [("Avant,", None), ("vérifie ces trois points.", None)]),
 ("Un : ton dossier complet, reçu avant le trente novembre.", [("1 : ton dossier complet,", None), ("reçu avant le 30 novembre.", None)]),
 ("Deux : le code parrain, à renseigner pendant la souscription.", [("2 : le code parrain,", None), ("à renseigner", None), ("pendant la souscription.", None)]),
 ("Trois : le versement initial de trois cents euros, dans les six jours.", [("3 : le versement initial,", None), ("dans les six jours.", None)]),
 ("Pour une première ouverture avec la carte Gold : jusqu'à cent cinquante euros de prime de bienvenue, si tu remplis les conditions.", [("Pour une 1re ouverture", None), ("avec la carte Gold :", None), ("jusqu'à … de prime de bienvenue,", None), ("si tu remplis les conditions.", None)]),
 ("Et garde ton compte et ta carte au moins un an.", [("Et garde ton compte", None), ("et ta carte", None), ("au moins un an.", None)]),
 ("Si tu veux que je te parraine, écris-moi en privé.", [("Si tu veux", None), ("que je te parraine,", None), ("écris-moi en privé.", None)]),
]
SPLITS = [(0.2, 2.891), (3.341, 4.709), (5.159, 7.489), (7.939, 10.3), (10.75, 13.437), (13.887, 18.398), (18.848, 20.552), (21.002, 22.739)]
MINLEN = 1.6
GAP = 0.3
TAIL = 1.9

CSS = PCSS + '''
.rd{color:#ff6b5f;text-shadow:0 0 18px rgba(255,80,70,.5)}
.cal{position:absolute;width:420px;height:470px;border-radius:30px;background:#f5efe4;box-shadow:0 30px 80px rgba(0,0,0,.7);overflow:hidden;text-align:center}
.cal .top{height:110px;background:#e0443a;color:#fff;font:900 54px Inter;letter-spacing:8px;line-height:110px}
.cal .d{font:900 230px 'DejaVu Serif',serif;color:#1a1414;line-height:270px}
.cal .r{position:absolute;left:0;right:0;top:0;height:30px}
.clock{position:absolute;width:190px;height:190px;border-radius:50%;background:#141010;border:8px solid #e0ac55;box-shadow:0 0 30px rgba(224,172,85,.4)}
.clock i{position:absolute;left:91px;top:30px;width:8px;height:66px;background:#f3efe6;border-radius:4px;transform-origin:4px 66px}
.clock b{position:absolute;left:91px;top:50px;width:8px;height:46px;background:#ff5a4f;border-radius:4px;transform-origin:4px 46px;transform:rotate(120deg)}
.box{position:absolute;left:130px;width:780px;height:120px;border-radius:26px;background:rgba(20,16,16,.92);border:3px solid rgba(255,255,255,.2);display:flex;align-items:center;font:800 38px Inter;color:#f3efe6;white-space:nowrap}
.box .c{width:66px;height:66px;margin:0 28px 0 28px;border-radius:14px;border:5px solid #ff5a4f;display:flex;align-items:center;justify-content:center;font:900 44px Inter;color:#ff5a4f}
.folder{position:absolute;width:420px;height:300px;border-radius:22px;background:linear-gradient(180deg,#f3c766,#d79a3a);box-shadow:0 30px 70px rgba(0,0,0,.6)}
.folder:before{content:'';position:absolute;left:30px;top:-40px;width:170px;height:60px;border-radius:16px 16px 0 0;background:#f3c766}
.folder .p{position:absolute;left:40px;right:40px;top:-20px;height:120px;border-radius:12px;background:#fff;transform:rotate(-3deg)}
.folder .ok{position:absolute;right:-30px;bottom:-30px;width:110px;height:110px;border-radius:50%;background:#ff5a4f;color:#fff;font:900 64px Inter;display:flex;align-items:center;justify-content:center}
.code{position:absolute;left:150px;width:740px;height:150px;border-radius:30px;border:4px dashed #ff5a4f;background:rgba(40,20,20,.85);display:flex;align-items:center;justify-content:center;gap:24px;font:900 54px 'DejaVu Sans Mono',monospace;color:#f3efe6;letter-spacing:6px;white-space:nowrap}
.code small{font:800 26px Inter;color:#ff6b5f;letter-spacing:2px}
.days{position:absolute;left:150px;width:740px;display:grid;grid-template-columns:repeat(7,1fr);gap:12px}
.days i{height:90px;border-radius:16px;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.18);font:900 34px Inter;font-style:normal;color:#cfc8ba;display:flex;align-items:center;justify-content:center}
.days i.on{background:#ff5a4f;border-color:#ff5a4f;color:#141010}
.gcard{position:absolute;width:460px;height:288px;border-radius:28px;background:linear-gradient(135deg,#f6e3a8,#c99a3e 55%,#f1d589);box-shadow:0 30px 70px rgba(0,0,0,.6);transform:rotate(-7deg)}
.gcard:before{content:'';position:absolute;left:44px;top:88px;width:80px;height:60px;border-radius:10px;background:linear-gradient(135deg,#e9e2cf,#a89d82)}
.gcard b{position:absolute;left:44px;bottom:36px;font:900 36px Inter;color:#3a2808;letter-spacing:3px}
.hg{position:absolute;font:900 170px Inter;color:#e0ac55;text-shadow:0 0 30px rgba(224,172,85,.5)}
'''


def cal(x, y, g=None, fx='pop', rot=-4):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    return f'<div class="cal" style="left:{x}px;top:{y}px;transform:rotate({rot}deg)"{a}><div class="top">NOV.</div><div class="d">30</div></div>'


CLOCK = '<div class="clock" style="left:700px;top:560px"><i style="transform:rotate(-30deg)"></i><b></b></div>'
DAYS = '<div class="days" style="top:900px" data-g="4.1" data-fx="up">' + ''.join(f'<i class="on">J{k}</i>' if k <= 6 else f'<i>J{k}</i>' for k in range(1, 8)) + '</div>'

BODY = hud('FRANCE · CHRONO', 'FORTUNEO') + BANNER + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hdx(230, [('h1 rd', 'PARRAINAGE FORTUNEO', None, 'font-size:68px'), ('it gold', "l'offre s'arrête", None, 'font-size:74px'), ('it gold', 'le 30 novembre.', None, 'font-size:74px')]) + cal(300, 620) + CLOCK + '''</div>
  <div class="scene" data-s="1" data-in="up">''' + hdx(230, [('h1', 'AVANT,', '1.0', 'font-size:72px'), ('it rd', 'vérifie ces 3 points.', '1.1', 'font-size:70px')]) + '''
   <div class="box" style="top:560px" data-g="1.1" data-fx="right"><div class="c"></div>dossier complet</div>
   <div class="box" style="top:710px" data-g="1.1" data-fx="right"><div class="c"></div>code parrain</div>
   <div class="box" style="top:860px" data-g="1.1" data-fx="right"><div class="c"></div>versement initial</div></div>
  <div class="scene" data-s="2" data-in="right"><div class="floor"></div>''' + '<div class="num" style="left:110px;top:230px" data-g="2.0" data-fx="stamp">1</div>' + hdx(250, [('h1', 'DOSSIER COMPLET', '2.0', 'font-size:62px'), ('it rd', 'reçu avant le 30/11.', '2.1', 'font-size:62px')], left=290, width=640) + '''
   <div class="folder" style="left:310px;top:640px" data-g="2.0" data-fx="up"><div class="p"></div><div class="ok" data-g="2.1" data-fx="stamp">✓</div></div></div>
  <div class="scene" data-s="3" data-in="up">''' + '<div class="num" style="left:110px;top:230px" data-g="3.0" data-fx="stamp">2</div>' + hdx(250, [('h1', 'LE CODE PARRAIN', '3.0', 'font-size:62px'), ('it rd', 'pendant la souscription.', '3.2', 'font-size:56px')], left=290, width=640) + '''
   <div class="code" style="top:620px" data-g="3.1" data-fx="stamp"><small>CODE PARRAIN</small>• • • • • •</div>
   <div class="tagp" style="left:240px;top:840px" data-g="3.2" data-fx="pop">à renseigner, sinon pas de prime</div></div>
  <div class="scene" data-s="4" data-in="right"><div class="floor"></div>''' + '<div class="num" style="left:110px;top:230px" data-g="4.0" data-fx="stamp">3</div>' + hdx(250, [('h1', 'VERSEMENT INITIAL', '4.0', 'font-size:60px'), ('it rd', 'dans les 6 jours.', '4.1', 'font-size:64px')], left=290, width=640) + DAYS + '''
   <div class="cond" style="top:1040px;color:#e6cfc6" data-g="4.1" data-fx="fade">après l'ouverture du compte</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hdx(230, [('h1', 'CARTE GOLD', '5.0', 'font-size:72px'), ('it gold', '1re ouverture', '5.1', 'font-size:66px')]) + '''
   <div class="gcard" style="left:300px;top:540px" data-g="5.1" data-fx="pop" data-slow="5.1"><b>CARTE GOLD</b></div>
   <div class="tagp" style="left:230px;top:920px" data-g="5.2" data-fx="stamp">prime de bienvenue</div>
   <div class="cond" style="top:1030px;color:#e6cfc6" data-g="5.3" data-fx="fade">si tu remplis les conditions</div></div>
  <div class="scene" data-s="6" data-in="up"><div class="floor"></div>''' + hdx(230, [('h1', 'GARDE TON COMPTE', '6.0', 'font-size:64px'), ('h1', 'ET TA CARTE', '6.1', 'font-size:64px'), ('it rd', 'au moins un an.', '6.2', 'font-size:68px')]) + '''
   <div class="hg" style="left:430px;top:600px" data-g="6.0" data-fx="pop">⌛</div>
   <div class="tagp" style="left:330px;top:920px" data-g="6.2" data-fx="pop">12 mois minimum</div></div>
  <div class="scene" data-s="7" data-in="pop"><div class="floor"></div>''' + hdx(230, [('h1', 'SI TU VEUX QUE', '7.0', 'font-size:66px'), ('h1', 'JE TE PARRAINE,', '7.1', 'font-size:66px'), ('it gold', 'écris-moi en privé.', '7.2', 'font-size:72px')]) + cal(340, 640, rot=4) + '''
   <div class="cond" style="top:1160px;font-size:24px">Offre soumise aux conditions en vigueur · jusqu'au 30/11/2026<br>1re ouverture, carte Gold, code parrain, versement sous 6 jours</div></div>
'''
