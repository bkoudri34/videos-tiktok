import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from tuto import *
from qg_figs import *
# Vidéos QG du 20/11/2026, vidéo 2 : Fortuneo. Style T « tuto illustré » (personnages blancs animés).
# Format F1 « STOP / erreur à éviter » : 3 erreurs qui font perdre la prime (code parrain oublié, 300 € pas versés sous 6 jours,
# offre qui se termine le 30/11), puis le résultat (Fosfo 80 € / Gold 150 €) et l'appel à l'action.
# Source : https://www.fortuneo.fr/parrainage/cartes-bancaires (consultée le 20/11/2026) : offre du 01/11 au 30/11/2026
# (dossier complet reçu au plus tard le 30/11), filleul 80 € (Fosfo Mastercard, sans condition de revenus) ou 150 €
# (Gold CB Mastercard, dès 2 200 € de revenus nets mensuels), code parrain renseigné pendant la souscription, versement
# initial de 300 € dans les 6 jours suivant l'ouverture, compte et carte conservés au moins 1 an, prime versée au plus tard le 31/12/2026.
# Voix : Mathieu (inworld-tts-2), ≈ 167 mots/min.
NAME = 'qg_fortuneo2'
TITLE = 'QG Fortuneo STOP 3 erreurs'
JS = 'const CAM=0.6, PUSH=0.010;' + FIGJS
GAP = 0.25
TAIL = 1.6
MINLEN = 1.8
LINES = [
 ("Parrainage Fortuneo : stop, trois erreurs qui te font perdre ta prime.", [("<em>Parrainage Fortuneo</em> :", None), ("<i>STOP</i>,", None), ("3 erreurs qui te font", None), ("<i>perdre ta prime</i>.", None)]),
 ("Un : oublier le code parrain. Il se met pendant l'ouverture, pas après.", [("Un : oublier le <em>code parrain</em>.", None), ("Il se met pendant l'ouverture,", None), ("<i>pas après</i>.", None)]),
 ("Deux : oublier de verser 300 € dans les six jours.", [("Deux : oublier de verser", None), ("<em>300 €</em>", None), ("dans les <em>6 jours</em>.", None)]),
 ("Trois : attendre. L'offre s'arrête le 30 novembre.", [("Trois : <i>attendre</i>.", None), ("L'offre s'arrête", None), ("le <em>30 novembre</em>.", None)]),
 ("Résultat : 80 € avec la carte Fosfo, 150 € avec la Gold, dès 2200 € de revenus nets.", [("Résultat :", None), ("<em>80 €</em> avec la carte Fosfo,", None), ("<em>150 €</em> avec la Gold,", None), ("dès 2 200 € nets / mois.", None)]),
 ("Envoie-moi Fortuneo en privé, je t'envoie mon code.", [("Envoie-moi <em>FORTUNEO</em>", None), ("en privé,", None), ("je t'envoie mon code.", None)]),
]
SPLITS = [(0.0, 3.98), (4.42, 7.91), (8.32, 11.02), (11.42, 14.26), (14.60, 21.17), (21.55, 24.12)]
GSTART = [[0.0, 1.58, 2.18, 3.2], [4.43, 6.18, 7.5], [8.33, 9.7, 10.4], [11.43, 12.68, 13.4], [14.61, 15.2, 17.53, 19.29], [21.56, 22.6, 23.25]]

CSS = FIGCSS + '''
#sub{left:60px;width:850px}
.endc .c{font-size:84px;white-space:nowrap}
.calp{position:absolute;width:420px;height:440px;background:#fff;border:7px solid #111;border-radius:30px;box-shadow:12px 14px 0 #111;text-align:center;overflow:hidden}
.calp .top{height:110px;background:#e63946;border-bottom:7px solid #111;color:#fff;font:900 56px Inter;display:flex;align-items:center;justify-content:center;letter-spacing:4px}
.calp .d{font:900 200px/1.1 Inter}
.calp .h{font:900 46px Inter;color:#e63946}
.bigN{position:absolute;font:900 200px/1 Inter;letter-spacing:-6px;white-space:nowrap}
.lst{position:absolute;left:70px;width:800px;padding:24px 34px}
.lst .r{display:flex;align-items:center;gap:22px;font:800 46px Inter;white-space:nowrap;height:120px}
.lst .r .p{margin-left:auto;font:900 60px Inter;padding-right:6px}
.cardd{display:inline-block;width:120px;height:78px;border:6px solid #111;border-radius:12px;background:#fff;position:relative;flex:none}
.cardd:after{content:'';position:absolute;left:12px;top:16px;width:30px;height:22px;border-radius:5px;background:#111}
.err{position:absolute;left:70px;top:330px;font:900 44px Inter;color:#fff;background:#e63946;padding:8px 26px;border-radius:14px;letter-spacing:2px;transform:rotate(-2deg)}
.xx{position:absolute;font:900 220px/1 Inter;color:#e63946}
'''

STOP = ('<svg class="abs" style="left:520px;top:520px" width="380" height="380" viewBox="0 0 380 380">'
        '<polygon points="111,6 269,6 374,111 374,269 269,374 111,374 6,269 6,111" style="fill:#e63946;stroke:#111;stroke-width:9"/>'
        '<polygon points="122,30 258,30 350,122 350,258 258,350 122,350 30,258 30,122" style="fill:none;stroke:#fff;stroke-width:8"/>'
        '<text x="190" y="226" text-anchor="middle" style="font:900 100px Inter;fill:#fff">STOP</text></svg>')

BODY = '''
  <div class="scene" data-s="0">''' + title('Parrainage<br><mark>Fortuneo</mark>', 210, size=86) + \
    guy(110, 600, 'cap', 'open', 'up', 0.95) + STOP + '''
   <div class="note" style="left:470px;top:1000px;font-size:62px;transform:rotate(-4deg)" data-g="0.2" data-fx="stamp">3 ERREURS</div>
   <div class="note" style="left:470px;top:1090px;font-size:44px;color:#111;transform:rotate(-4deg)" data-g="0.3" data-fx="pop">= prime perdue</div></div>
  <div class="scene" data-s="1" data-in="right"><div class="err">ERREUR N°1</div>''' + title('le <mark>code parrain</mark>', 420, size=78) + '''
   <div class="phone" style="left:470px;top:560px"><div class="scr"><div class="tt">Ouverture</div><div class="ln"></div><div class="ln" style="width:70%"></div>
    <div class="fl">Code parrain : ______</div><div class="bt">Valider</div><div class="ln" style="margin-top:40px"></div><div class="ln" style="width:55%"></div></div></div>''' + \
    circle(480, 760, 420, 150, '1.0') + guy(90, 700, 'curly', 'sad', 'shrug', 0.95) + '''
   <div class="note" style="left:40px;top:1170px;font-size:46px;transform:rotate(-3deg)" data-g="1.1" data-fx="pop">PENDANT<br>l'ouverture</div>
   <div class="note" style="left:90px;top:1300px;font-size:44px;color:#111;transform:rotate(-3deg)" data-g="1.2" data-fx="pop">(pas après !)</div></div>
  <div class="scene" data-s="2" data-in="right"><div class="err">ERREUR N°2</div>''' + title('le 1<sup>er</sup> versement', 420, size=78) + '''
   <div class="bigN" style="left:120px;top:600px" data-g="2.1" data-fx="stamp">300 €</div>''' + underline2(130, 810, 560, '2.1') + '''
   <div class="calp" style="left:560px;top:880px;width:360px;height:380px"><div class="top">DÉLAI</div><div class="d" style="font-size:170px">6</div><div class="h">jours</div></div>''' + \
    circle(530, 900, 420, 360, '2.2', 4) + guy(140, 880, 'spiky', 'flat', 'point', 0.8) + '''</div>
  <div class="scene" data-s="3" data-in="up"><div class="err">ERREUR N°3</div>''' + title('<em>attendre</em>', 420, size=96) + '''
   <div class="calp" style="left:480px;top:600px"><div class="top">NOVEMBRE</div><div class="d">30</div><div class="h">fin de l'offre</div></div>''' + \
    circle(450, 680, 480, 380, '3.2', 4) + guy(90, 680, 'bun', 'open', 'up', 0.95) + '''
   <div class="note" style="left:470px;top:1100px;font-size:52px;transform:rotate(-4deg)" data-g="3.1" data-fx="stamp">ne traîne pas !</div></div>
  <div class="scene" data-s="4" data-in="right">''' + title('Le <mark>résultat</mark>', 220, size=86) + '''
   <div class="paper lst" style="top:400px"><div class="r" data-g="4.1" data-fx="left"><span class="cardd"></span>carte Fosfo<span class="p">80 €</span></div>
    <div class="r" data-g="4.2" data-fx="left"><span class="cardd" style="background:#ffe14d"></span>carte Gold<span class="p">150 €</span></div></div>''' + \
    circle(610, 530, 280, 130, '4.2', -3) + '''
   <div class="note" style="left:90px;top:720px;font-size:40px;width:760px;text-align:center;white-space:normal;transform:rotate(-2deg)" data-g="4.3" data-fx="pop">Gold : dès 2 200 € nets / mois</div>''' + \
    guy(380, 830, 'cap', 'smile', 'up', 0.95) + '''</div>
  <div class="scene" data-s="5" data-in="pop">
   <div class="endc" data-g="5.0" data-fx="up"><div class="k">ENVOIE-MOI EN PRIVÉ</div><div class="c">« FORTUNEO »</div><div class="d">je t'envoie mon code</div><div class="b">@htm.invest</div></div>
   <div class="note" style="left:300px;top:770px;transform:rotate(-3deg)" data-g="5.1" data-fx="pop">parrainage Fortuneo</div>''' + \
    guy(90, 850, 'cap', 'smile', 'up', 0.55) + '''
   <div class="cond" style="top:860px;left:270px;width:660px">Offre soumise aux conditions en vigueur.<br>Parrainage Fortuneo, offre du 01/11 au 30/11/2026 (dossier complet reçu au plus tard le 30/11) : 80 € avec la carte Fosfo, 150 € avec la Gold CB Mastercard (dès 2 200 € de revenus nets mensuels). Code parrain à saisir pendant la souscription, versement initial de 300 € dans les 6 jours, compte et carte gardés au moins 1 an. Prime versée au plus tard le 31/12/2026.<br>Lien de parrainage : je touche une prime.</div></div>
'''
