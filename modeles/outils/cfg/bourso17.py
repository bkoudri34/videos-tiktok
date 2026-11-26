import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parraine import *
# BoursoBank, 26/11/2026 (vidéo C) - style v3 nuit & or, accent bleu glacier. Format F18 « Parraine à ton tour » (règles de Badr du 26/11) :
# décor de guichet (mur à lampes + comptoir), mascotte bleu glacier à casquette dorée -> 1 je t'envoie mon invitation en privé
# -> 2 tu ouvres ton compte (téléphone + étapes de la prime de bienvenue) -> 3 une fois client avec une carte active, tu parraines à ton tour
# -> 4 tu invites tes amis (un seul niveau, plafond fixé par la banque, ralenti) -> « je ne touche rien sur les amis de mes filleuls »
# -> appel à l'action discret. AUCUN montant écrit : montants à l'oral seulement.
# Source (boursobank.com/bon-plan/parrainage-boursobank, consultée le 26/11/2026) : filleul « prime maximale de 300 € » (60 € ouverture,
# jusqu'à 80 € 1er versement >= 300 €, 80 € carte 3 mois, 80 € EasyMove sous 1 mois) ; parrain : récompense « de l'offre en cours »
# (montant non publié sur la page, visible dans l'appli), limite de 20 primes parrainage sur 12 mois glissants, parrain = client avec
# notamment une carte active. Pas de total annoncé (prime parrain non publiée sur le site officiel).
# Voix : Speko (voix par défaut), speed 1.08, atempo 1.14, silences internes plafonnés à 0,22 s ; réplique 1 refaite (nouvelle accroche).
NAME = 'bourso17'
TITLE = 'BoursoBank parraine a ton tour glacier'
ROOT = ':root{--bg:#03070b;--ac:#8fd8ff}'
LINES = [
 ("Parrainage Bourso Bank : et après, toi, tu parraines qui ?", [("Parrainage BoursoBank :", None), ("et après, toi,", None), ("tu parraines qui ?", None)]),
 ("Un : je t'envoie mon invitation, en privé.", [("1 :", None), ("je t'envoie mon invitation,", None), ("en privé.", None)]),
 ("Deux : tu ouvres ton compte. Jusqu'à trois cents euros de prime de bienvenue, si tu remplis les conditions.", [("2 : tu ouvres ton compte.", None), ("Jusqu'à … de prime de bienvenue,", None), ("si tu remplis les conditions.", None)]),
 ("Trois : une fois client, avec ta carte active, tu peux parrainer à ton tour.", [("3 : une fois client,", None), ("avec ta carte active,", None), ("tu peux parrainer à ton tour.", None)]),
 ("Quatre : tu invites tes amis. La banque prévoit une prime pour chaque ami qui remplit les conditions. Le montant est dans son appli, avec un plafond de vingt primes sur douze mois.", [("4 : tu invites tes amis.", None), ("une prime pour chaque ami", None), ("qui remplit les conditions.", None), ("Le montant est dans son appli,", None), ("plafond fixé par la banque.", None)]),
 ("Un seul niveau : je ne touche rien sur les amis de mes filleuls.", [("Un seul niveau :", None), ("je ne touche rien", None), ("sur les amis de mes filleuls.", None)]),
 ("Si tu veux que je te parraine, écris-moi en privé.", [("Si tu veux", None), ("que je te parraine,", None), ("écris-moi en privé.", None)]),
]
SPLITS = [(0.2, 2.45), (2.9, 4.64), (5.09, 8.86), (9.31, 12.12), (12.57, 18.76), (19.21, 21.41), (21.86, 23.48)]
MINLEN = 1.6
GAP = 0.3
TAIL = 1.9

CSS = PCSS + '''
.gl{color:#8fd8ff;text-shadow:0 0 18px rgba(120,200,255,.55)}
.wall{background:repeating-linear-gradient(90deg,rgba(140,210,255,0) 0 178px,rgba(140,210,255,.08) 178px 181px)}
.lamp{background:#bfe8ff;box-shadow:0 0 30px 10px rgba(140,210,255,.4)}
.counter{top:1180px;background:repeating-linear-gradient(90deg,#0b1016 0 150px,#121a22 150px 154px);border-top:14px solid #dfeaf2}
.ph{position:absolute;width:360px;height:640px;border-radius:52px;background:#0c1116;border:9px solid #2a3440;box-shadow:0 0 0 2px #4d5d6e,0 30px 80px rgba(0,0,0,.7);overflow:hidden;text-align:center;color:#eaf6ff}
.ph .top{height:26px;width:120px;margin:0 auto;background:#000;border-radius:0 0 16px 16px}
.ph .ok{margin-top:60px;width:130px;height:130px;border-radius:50%;margin-left:115px;background:#8fd8ff;color:#08131c;font:900 80px Inter;line-height:130px}
.ph .tt{margin-top:26px;font:900 34px Inter}
.ph .row{margin:16px 18px 0;padding:14px 8px;border-radius:16px;background:#16212b;font:700 21px Inter;text-align:left;white-space:nowrap}
.ph .row i{font-style:normal;color:#8fd8ff;margin-right:10px}
.bcard{position:absolute;width:420px;height:262px;border-radius:26px;background:linear-gradient(135deg,#1b2a38,#0e1822 60%,#24384a);border:3px solid #8fd8ff;box-shadow:0 30px 70px rgba(0,0,0,.6);transform:rotate(7deg)}
.bcard:before{content:'';position:absolute;left:40px;top:80px;width:74px;height:56px;border-radius:10px;background:linear-gradient(135deg,#e9e2cf,#a89d82)}
.bcard b{position:absolute;left:40px;bottom:34px;font:900 30px Inter;color:#8fd8ff;letter-spacing:3px}
.badge{position:absolute;padding:16px 34px;border-radius:22px;border:4px solid #f3c766;color:#f3c766;font:900 44px Inter;letter-spacing:3px;transform:rotate(-6deg);background:rgba(20,16,8,.8);white-space:nowrap}
.env{position:absolute;width:220px;height:150px;border-radius:14px;background:#eaf6ff;box-shadow:0 20px 50px rgba(0,0,0,.6)}
.env:before{content:'';position:absolute;left:0;top:0;border-left:110px solid transparent;border-right:110px solid transparent;border-top:86px solid #bfe0f5}
'''
ME = '#8fd8ff'
DECOR = '<div class="wall"></div><div class="lamp" style="left:120px;top:960px"></div><div class="lamp" style="left:520px;top:940px"></div><div class="lamp" style="left:930px;top:960px"></div><div class="counter"></div>'

BODY = hud('FRANCE · GUICHET DU PARRAINAGE', 'BOURSOBANK') + BANNER + '''
  <div class="scene" data-s="0">''' + DECOR + hdx(230, [('h1 gl', 'PARRAINAGE BOURSOBANK :', None, 'font-size:60px'), ('it gold', 'et après, toi,', None, 'font-size:76px'), ('it gold', 'tu parraines qui ?', None, 'font-size:76px')]) + mascot(560, 760, 400, ME, 'cap') + friend(150, 860, 150, '#f3c766') + friend(330, 900, 130, '#f3c766') + '''
   <div class="bubble2" style="left:180px;top:700px;transform:rotate(-5deg)">et toi ?</div></div>
  <div class="scene" data-s="1" data-in="left">''' + DECOR + '<div class="num" style="left:465px;top:230px" data-g="1.0" data-fx="stamp">1</div>' + hdx(410, [('h1', "JE T'ENVOIE", '1.1', 'font-size:70px'), ('it gl', 'mon invitation, en privé.', '1.2', 'font-size:62px')]) + mascot(100, 820, 340, ME, 'cap') + friend(720, 880, 220, '#f3c766', g='1.2') + '''
   <div class="env" style="left:440px;top:800px" data-g="1.1" data-fx="right"></div></div>
  <div class="scene" data-s="2" data-in="up">''' + '<div class="num" style="left:110px;top:230px" data-g="2.0" data-fx="stamp">2</div>' + hdx(250, [('h1', 'TU OUVRES', '2.0', 'font-size:66px'), ('h1', 'TON COMPTE', '2.0', 'font-size:66px')], left=280, width=650) + '''
   <div class="ph" style="left:360px;top:450px" data-g="2.0" data-fx="up"><div class="top"></div><div class="ok">✓</div><div class="tt">Compte ouvert</div>
    <div class="row" data-g="2.1" data-fx="fade"><i>●</i>1er versement</div><div class="row" data-g="2.1" data-fx="fade"><i>●</i>carte utilisée 3 mois</div><div class="row" data-g="2.2" data-fx="fade"><i>●</i>EasyMove sous 30 jours</div></div>
   <div class="tagp" style="left:250px;top:1120px" data-g="2.2" data-fx="pop">si tu remplis les conditions</div></div>
  <div class="scene" data-s="3" data-in="right">''' + DECOR + '<div class="num" style="left:465px;top:230px" data-g="3.0" data-fx="stamp">3</div>' + hdx(410, [('h1', 'UNE FOIS CLIENT,', '3.0', 'font-size:66px'), ('it gl', 'avec ta carte active,', '3.1', 'font-size:62px')]) + '''
   <div class="bcard" style="left:150px;top:640px" data-g="3.1" data-fx="pop"><b>CARTE ACTIVE</b></div>''' + mascot(620, 720, 300, ME, 'cap') + '''
   <div class="badge" style="left:610px;top:590px" data-g="3.2" data-fx="stamp">PARRAIN</div></div>
  <div class="scene" data-s="4" data-in="pop">''' + '<div class="num" style="left:110px;top:230px" data-g="4.0" data-fx="stamp">4</div>' + hdx(260, [('h1', 'TU INVITES', '4.0', 'font-size:66px'), ('it gl', 'tes amis.', '4.0', 'font-size:66px')], left=280, width=650) + \
    link(540, 700, 230, 900, '4.1') + link(540, 700, 540, 940, '4.1') + link(540, 700, 850, 900, '4.1') + \
    mascot(440, 520, 200, ME, 'cap') + friend(150, 880, 160, '#f3c766', g='4.1') + friend(460, 920, 160, '#f3c766', g='4.1') + friend(770, 880, 160, '#f3c766', g='4.1') + '''
   <div class="cond" style="top:1100px;color:#bcd6e6;font-size:28px" data-g="4.2" data-fx="fade">une prime pour chaque ami qui remplit les conditions</div>
   <div class="tagp" style="left:120px;top:1170px" data-g="4.3" data-fx="pop">montant dans l'appli de la banque</div>
   <div class="tagp" style="left:200px;top:1280px;background:#f3c766" data-g="4.4" data-fx="stamp" data-slow="4.4">plafond fixé par la banque</div></div>
  <div class="scene" data-s="5" data-in="up">''' + DECOR + hdx(230, [('h1 gl', 'UN SEUL NIVEAU', '5.0', 'font-size:72px'), ('it gold', 'je ne touche rien sur', '5.1', 'font-size:60px'), ('it gold', 'les amis de mes filleuls.', '5.2', 'font-size:60px')]) + \
    mascot(120, 600, 220, ME, 'cap') + link(340, 720, 480, 720) + friend(480, 640, 170, '#f3c766') + link(560, 810, 520, 930, '5.2') + link(600, 810, 760, 930, '5.2') + friend(440, 930, 130, '#9a8fae', g='5.2', cls='grey') + friend(720, 930, 130, '#9a8fae', g='5.2', cls='grey') + '''
   <div class="x" style="left:470px;top:910px" data-g="5.2" data-fx="stamp">✕</div><div class="x" style="left:750px;top:910px" data-g="5.2" data-fx="stamp">✕</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + DECOR + hdx(230, [('h1', 'SI TU VEUX QUE', '6.0', 'font-size:68px'), ('h1', 'JE TE PARRAINE,', '6.1', 'font-size:68px'), ('it gl', 'écris-moi en privé.', '6.2', 'font-size:72px')]) + mascot(560, 760, 340, ME, 'cap', g='6.2') + friend(170, 860, 150, '#f3c766') + '''
   <div class="cond" style="top:1240px;font-size:24px;color:#9fb2c0">Offres soumises aux conditions en vigueur · 1re ouverture d'un compte<br>individuel, via une invitation de parrainage</div></div>
'''
