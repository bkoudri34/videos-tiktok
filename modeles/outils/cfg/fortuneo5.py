import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Fortuneo, 09/11/2026 18:00 - style v3 nuit & or, accent bleu nuit. Offre de bienvenue jusqu'à 260 € (carte Gold : 160 + 80 mobilité + 20 Livret +), jusqu'au 20/12/2026.
NAME = 'fortuneo5'
TITLE = 'Fortuneo 260 euros nuit et or'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Deux cent soixante euros pour ouvrir un compte. Sans blague.", [("260 €", None), ("pour ouvrir un compte.", None), ("Sans blague.", None)]),
 ("C'est l'offre de bienvenue Fortuneo, avec la carte Gold.", [("C'est l'offre de bienvenue", None), ("Fortuneo,", None), ("avec la carte Gold.", None)]),
 ("Cent soixante euros pour la carte, après cinq paiements.", [("160 €", None), ("pour la carte,", None), ("après cinq paiements.", None)]),
 ("Quatre-vingts euros si tu changes de banque, et vingt avec le Livret plus.", [("80 €", None), ("si tu changes de banque,", None), ("et 20 avec le Livret +.", None)]),
 ("Mais attention, ça s'arrête le vingt décembre.", [("Mais attention,", None), ("ça s'arrête", None), ("le 20 décembre.", None)]),
 ("Envoie-moi FORTUNEO en privé, je t'explique tout.", [("Envoie-moi", None), ("FORTUNEO", None), ("en privé,", None), ("je t'explique tout.", None)]),
]
SPLITS = [(0.0, 2.574), (2.876, 5.322), (5.578, 8.002), (8.492, 11.477), (11.808, 13.533), (14.034, 16.113)]
GSTART = [[0.1, 1.0, 2.0], [2.9, 3.7, 4.4], [5.6, 6.3, 7.1], [8.5, 9.0, 10.1], [11.81, 12.4, 12.8], [14.04, 14.5, 15.0, 15.4]]
MINLEN = 2.5
GAP = 0.4
TAIL = 2.0
CSS = '''
.vault{position:absolute;left:290px;top:760px;width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,#1b2233,#0b0e16 70%);border:10px solid #3b4d73;box-shadow:0 0 0 6px #d9a24c,0 0 60px rgba(74,123,208,.45)}
.vault:before{content:'';position:absolute;inset:60px;border-radius:50%;border:4px dashed rgba(217,162,76,.6)}
.vault .sp{position:absolute;left:240px;top:60px;width:10px;height:360px;background:linear-gradient(#f3c766,#a8701f);border-radius:5px}
.vault .hub{position:absolute;left:185px;top:185px;width:120px;height:120px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#fff0c0,#d9a24c 60%,#7a5016)}
.card{position:absolute;left:190px;top:760px;width:700px;height:440px;border-radius:36px;background:linear-gradient(135deg,#f6dc8e 0%,#d6a347 40%,#8a5a18 100%);box-shadow:0 40px 90px rgba(0,0,0,.7),0 0 60px rgba(240,180,80,.35);color:#2a1a05;padding:44px 50px}
.card .chip{width:100px;height:76px;border-radius:14px;background:linear-gradient(135deg,#fff1c4,#b98a3a);margin-top:40px}
.card .num{font:700 44px 'DejaVu Sans Mono',monospace;letter-spacing:4px;margin-top:40px}
.card .nm{font:900 40px Inter;letter-spacing:3px}
.dots{position:absolute;left:150px;top:1200px;width:780px;display:flex;justify-content:space-between}
.dots div{width:120px;height:120px;border-radius:50%;border:4px solid #4a7bd0;display:flex;align-items:center;justify-content:center;font:900 54px Inter;color:#fff;background:rgba(74,123,208,.25)}
.cal{position:absolute;left:290px;top:660px;width:500px;height:560px;border-radius:30px;background:#f4f0e6;box-shadow:0 40px 90px rgba(0,0,0,.7);overflow:hidden;text-align:center;color:#1b1b22}
.cal .tp{height:130px;background:#2b3f6b;color:#f3c766;font:900 56px Inter;letter-spacing:8px;line-height:130px}
.cal .d{font:900 260px 'DejaVu Serif',serif;line-height:1.2}
.cal .y{font:700 34px Inter;letter-spacing:8px;color:#666}
.blue{color:#8fb3ff}
'''
BODY = hud('FRANCE · BANQUE EN LIGNE', 'OFFRE DE BIENVENUE') + '''
  <div class="scene" data-s="0"><div class="floor"></div>
   ''' + head(210, [('it gold" style="font-size:60px', "jusqu'à", None), ('big gold', '260 €', None), ('h1 s', 'POUR OUVRIR UN COMPTE', None), ('it gold', 'sans blague.', '0.2')]).replace('class="big gold"', 'class="big gold" style="font-size:190px"').replace('class="h1 s"', 'class="h1 s" style="font-size:56px"') + '''
   <div class="vault" style="top:820px"><div class="sp"></div><div class="sp" style="transform:rotate(60deg)"></div><div class="sp" style="transform:rotate(-60deg)"></div><div class="hub"></div></div></div>
  <div class="scene" data-s="1" data-in="pop">''' + head(230, [('h1 s', "L'OFFRE DE BIENVENUE", '1.0'), ('h1', 'FORTUNEO', '1.1'), ('it gold', 'avec la carte Gold.', '1.2')]) + '''
   <div class="orb" style="left:140px;top:640px;width:800px;height:680px"></div>
   <div class="card" data-g="1.1" data-fx="up"><div class="nm">CARTE GOLD</div><div class="chip"></div><div class="num">•••• •••• •••• 2026</div></div>
   <div class="spark" style="left:170px;top:720px" data-g="1.2" data-fx="pop">✦</div><div class="spark" style="left:860px;top:1220px" data-g="1.2" data-fx="pop">✦</div></div>
  <div class="scene" data-s="2" data-in="right"><div class="rays" style="top:560px"></div>''' + head(230, [('big gold', '160 €', '2.0'), ('h1 s', 'POUR LA CARTE', '2.1'), ('it gold', 'après 5 paiements.', '2.2')]).replace('class="big gold"', 'class="big gold" style="font-size:170px"') + '''
   <div class="coin" style="left:380px;top:1000px" data-g="2.0" data-fx="pop"></div><div class="coin" style="left:380px;top:890px" data-g="2.1" data-fx="pop"></div><div class="coin" style="left:380px;top:780px" data-g="2.1" data-fx="pop"></div>
   <div class="dots"><div data-g="2.2" data-fx="pop">1</div><div data-g="2.2" data-fx="pop">2</div><div data-g="2.2" data-fx="pop">3</div><div data-g="2.2" data-fx="pop">4</div><div data-g="2.2" data-fx="pop">5</div></div></div>
  <div class="scene" data-s="3" data-in="pop"><div class="floor"></div>''' + head(230, [('h1', 'EN PLUS…', '3.0'), ('it gold', 'si tu changes de banque', '3.1')]).replace('class="it gold"', 'class="it gold" style="font-size:64px"') + '''
   <div class="coin" style="left:130px;top:960px" data-g="3.0" data-fx="pop"></div><div class="coin" style="left:130px;top:850px" data-g="3.0" data-fx="pop"></div>
   <div class="ldr" style="left:450px;top:898px;width:90px" data-g="3.1" data-fx="grow"></div><div class="lbl" style="top:872px" data-g="3.1" data-fx="left"><b>80 €</b> · MOBILITÉ</div>
   <div class="coin" style="left:130px;top:1200px;width:240px;height:76px;margin-left:40px" data-g="3.2" data-fx="pop"></div>
   <div class="ldr" style="left:450px;top:1228px;width:90px" data-g="3.2" data-fx="grow"></div><div class="lbl" style="top:1202px" data-g="3.2" data-fx="left"><b>20 €</b> · LIVRET +</div></div>
  <div class="scene" data-s="4" data-in="left">''' + head(230, [('h1', 'MAIS ATTENTION,', '4.0'), ('it gold', "ça s'arrête…", '4.1')]) + '''
   <div class="cal" data-g="4.2" data-fx="stamp" data-slow="4.2"><div class="tp">DÉCEMBRE</div><div class="d">20</div><div class="y">2026</div></div>
   <div class="abs" style="left:300px;top:1260px;width:480px;text-align:center;font:800 38px Inter;letter-spacing:4px;color:#8fb3ff" data-g="4.2" data-fx="fade">FIN DE L'OFFRE</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', 'ENVOIE-MOI', '5.0'), ('big gold', '« FORTUNEO »', '5.1'), ('it gold', 'en privé.', '5.2')]).replace('class="big gold"', 'class="big gold" style="font-size:112px"') + '''
   <div class="pill" style="top:700px" data-g="5.2" data-fx="up"><div class="pin">€</div><div><b>JUSQU'À 260 €</b><span>offre de bienvenue · jusqu'au 20/12</span></div></div>
   <div class="pill" style="top:825px" data-g="5.3" data-fx="up"><div class="pin">✉</div><div><b>JE T'EXPLIQUE TOUT</b><span>en privé sur @htm.invest</span></div></div>
   <div class="cond" style="top:980px">Offre de bienvenue Fortuneo soumise aux conditions en vigueur<br>nouveaux clients · carte Gold (revenus ≥ 2 200 €/mois)<br>montant maximum · jusqu'au 20/12/2026</div></div>
'''
