import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from tuto import *
from qg_figs import *
# Vidéos QG du 19/11/2026, vidéo 2 : Hello bank. Style T « tuto illustré » (personnages blancs animés).
# Format F12 « info choc / actu » : la date de fin vérifiée du jour (invitation à utiliser avant le 30/11/2026 à 15 h).
# Source : https://www.hellobank.fr/fr/votre-offre-parrainage/ (consultée le 19/11/2026) : demande d'ouverture via le lien
# d'invitation avant le 30/11/2026 à 15h (sous réserve d'évolution de la date de fin) ; Hello Prime : 80 € + 50 € au 13e mois
# (5 paiements ou retraits par mois pendant les 12 premiers mois), dès 1 500 € nets/mois ; Hello One : 80 € ;
# bon d'achat 200 € pour la mobilité Hello Start+ (souscrite entre le 10/08/2026 et le 11/01/2027).
# Voix : Manon (cartesia sonic-3.5, voice 2f8e82c4-…), speed 1.15.
NAME = 'qg_hellobank1'
TITLE = 'QG Hello bank fin le 30 novembre'
JS = 'const CAM=0.6, PUSH=0.010;' + FIGJS
GAP = 0.3
TAIL = 1.7
MINLEN = 1.8
LINES = [
 ("Parrainage Hello bank : attention, l'offre s'arrête le 30 novembre, à quinze heures.", [("<em>Parrainage Hello bank</em> :", None), ("<i>attention</i>,", None), ("l'offre s'arrête le <em>30 novembre</em>,", None), ("à <i>15 h</i>.", None)]),
 ("Jusque-là, c'est jusqu'à 330 € pour toi.", [("Jusque-là,", None), ("c'est jusqu'à <em>330 €</em>", None), ("pour toi.", None)]),
 ("80 € à l'ouverture avec Hello Prime, et 50 € au treizième mois si tu utilises ta carte.", [("<em>80 €</em> à l'ouverture", None), ("avec Hello Prime,", None), ("et <em>50 €</em> au 13e mois", None), ("si tu utilises ta carte.", None)]),
 ("Plus un bon d'achat de 200 € si tu transfères ton compte avec Hello Start plus.", [("Plus un <em>bon d'achat</em>", None), ("de <em>200 €</em>", None), ("si tu transfères ton compte", None), ("avec Hello Start+.", None)]),
 ("La condition : ouvrir depuis un lien d'invitation, avant la date limite.", [("La condition :", None), ("ouvrir depuis un <em>lien d'invitation</em>,", None), ("avant la <i>date limite</i>.", None)]),
 ("Envoie-moi Hello en privé, je t'envoie le lien.", [("Envoie-moi <em>HELLO</em>", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 4.70), (5.04, 7.76), (8.16, 13.46), (13.79, 18.07), (18.31, 21.78), (22.0, 24.32)]
GSTART = [[0.0, 1.3, 2.2, 4.1], [5.05, 5.9, 7.3], [8.17, 9.3, 10.5, 12.3], [13.8, 14.6, 15.7, 16.8], [18.32, 18.9, 20.7], [22.01, 22.7, 23.4]]

CSS = FIGCSS + '''
#sub{left:60px;width:850px}
.calp{position:absolute;width:420px;height:440px;background:#fff;border:7px solid #111;border-radius:30px;box-shadow:12px 14px 0 #111;text-align:center;overflow:hidden}
.calp .top{height:110px;background:#e63946;border-bottom:7px solid #111;color:#fff;font:900 60px Inter;display:flex;align-items:center;justify-content:center;letter-spacing:4px}
.calp .d{font:900 200px/1.1 Inter}
.calp .h{font:900 56px Inter;color:#e63946}
.bigN{position:absolute;font:900 230px/1 Inter;letter-spacing:-6px;white-space:nowrap}
.lst{position:absolute;left:70px;width:800px;padding:24px 34px}
.lst .r{display:flex;align-items:center;gap:22px;font:800 46px Inter;white-space:nowrap;height:110px}
.lst .r .p{margin-left:auto;font:900 54px Inter;padding-right:6px}
.vch{position:absolute;width:560px;height:280px;background:#ffe14d;border:7px dashed #111;border-radius:26px;text-align:center;padding-top:34px;box-shadow:12px 14px 0 #111}
.vch .k{font:900 44px Inter;letter-spacing:3px}
.vch .v{font:900 130px/1.1 Inter}
.hs{position:absolute;width:250px;height:200px;border:7px solid #111;border-radius:22px;background:#fff;font:900 34px Inter;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1.15;box-shadow:8px 9px 0 #111}
'''

BODY = '''
  <div class="scene" data-s="0">''' + title('Parrainage<br><mark>Hello bank</mark><br><em>fin le 30/11 à 15 h</em>', 210, size=72) + \
    guy(90, 640, 'spiky', 'open', 'up', 0.95) + '''
   <div class="calp" style="left:480px;top:560px"><div class="top">NOVEMBRE</div><div class="d">30</div><div class="h">à 15 h 00</div></div>''' + \
    circle(450, 640, 480, 380, '0.2', 4) + '''
   <div class="note" style="left:470px;top:1060px;font-size:58px;transform:rotate(-4deg)" data-g="0.1" data-fx="stamp">ATTENTION !</div></div>
  <div class="scene" data-s="1" data-in="up">''' + title('Jusque-là', 220, size=84) + '''
   <div class="bigN" style="left:190px;top:470px" data-g="1.1" data-fx="stamp">330 €</div>''' + underline2(200, 720, 660, '1.1') + \
    guy(110, 830, 'curly', 'smile', 'point', 0.95) + '''
   <div class="note" style="left:470px;top:900px;font-size:56px;transform:rotate(-3deg)" data-g="1.2" data-fx="pop">pour toi</div>
   <div class="note" style="left:470px;top:1000px;font-size:40px;color:#111;transform:rotate(-3deg)" data-g="1.2" data-fx="pop">(au maximum)</div></div>
  <div class="scene" data-s="2" data-in="right">''' + title('Avec <mark>Hello Prime</mark>', 220, size=84) + '''
   <div class="note" style="left:0;width:930px;text-align:center;top:330px;font-size:40px;color:#111" data-g="2.1" data-fx="pop">(dès 1 500 € nets / mois)</div>
   <div class="paper lst" style="top:430px"><div class="r" data-g="2.0" data-fx="left"><span class="num" style="position:static;width:86px;height:86px;font-size:50px">1</span>à l'ouverture<span class="p">80 €</span></div>
    <div class="r" data-g="2.2" data-fx="left"><span class="num" style="position:static;width:86px;height:86px;font-size:50px">2</span>au 13e mois<span class="p">+ 50 €</span></div></div>''' + \
    circle(630, 560, 250, 115, '2.2', -3) + '''
   <div class="note" style="left:90px;top:740px;font-size:40px;line-height:1.15;white-space:normal;width:760px;text-align:center;transform:rotate(-2deg)" data-g="2.3" data-fx="pop">si 5 paiements ou retraits par mois<br>pendant 12 mois</div>''' + \
    guy(410, 880, 'spiky', 'smile', 'hip', 0.8) + '''</div>
  <div class="scene" data-s="3" data-in="right">''' + title('+ un bon d’achat', 220, size=84) + '''
   <div class="vch" style="left:250px;top:420px;transform:rotate(-3deg)" data-g="3.1" data-fx="stamp"><div class="k">BON D'ACHAT</div><div class="v">200 €</div></div>
   <div class="hs" style="left:100px;top:830px" data-g="3.2" data-fx="up">ton ancienne<br>banque</div>
   <div class="hs" style="left:640px;top:830px" data-g="3.2" data-fx="up">Hello bank</div>''' + \
    arrow(360, 880, 280, 100, 'M10 50 Q140 0 270 50 M240 22 L270 50 L236 74', '3.2') + '''
   <div class="note" style="left:270px;top:1080px;font-size:46px;transform:rotate(-3deg)" data-g="3.3" data-fx="pop">mobilité Hello Start+</div></div>
  <div class="scene" data-s="4" data-in="up">''' + title('La condition', 220, size=84) + '''
   <div class="phone" style="left:470px;top:430px"><div class="scr"><div class="tt">Invitation reçue</div><div class="ln"></div><div class="ln" style="width:70%"></div>
    <div class="fl" data-g="4.1" data-fx="left">lien d'invitation ✓</div><div class="bt">Ouvrir mon compte</div><div class="ln" style="margin-top:40px"></div><div class="ln" style="width:55%"></div></div></div>''' + \
    circle(480, 640, 420, 150, '4.1') + guy(90, 640, 'curly', 'smile', 'point', 0.95) + '''
   <div class="note" style="left:60px;top:1262px;font-size:46px;transform:rotate(-3deg)" data-g="4.2" data-fx="pop">avant le 30/11 à 15 h</div></div>
  <div class="scene" data-s="5" data-in="pop">
   <div class="endc" data-g="5.0" data-fx="up"><div class="k">ENVOIE-MOI EN PRIVÉ</div><div class="c">« HELLO »</div><div class="d">je t'envoie le lien</div><div class="b">@htm.invest</div></div>
   <div class="note" style="left:300px;top:770px;transform:rotate(-3deg)" data-g="5.1" data-fx="pop">parrainage Hello bank</div>''' + \
    guy(90, 850, 'spiky', 'smile', 'up', 0.55) + '''
   <div class="cond" style="top:860px;left:270px;width:660px">Offre soumise aux conditions en vigueur.<br>Parrainage Hello bank : ouverture via le lien d'invitation avant le 30/11/2026 à 15 h (date susceptible d'évoluer). Hello Prime (dès 1 500 € nets/mois) : 80 € + 50 € au 13<sup>e</sup> mois (5 paiements ou retraits par mois pendant 12 mois). Hello One : 80 €. Bon d'achat de 200 € avec la mobilité Hello Start+.<br>Lien de parrainage : je touche une prime.</div></div>
'''
