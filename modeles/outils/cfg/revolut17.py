import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parraine import *
# Revolut, 27/11/2026 (vidéo B) - style v3 nuit & or, accent vert menthe. Format F2 « démystification » en vrai / faux :
# 3 idées reçues sur des cartes qui reçoivent un tampon (FAUX, FAUX, VRAI = le seul ralenti) -> étapes de l'invitation dans les délais
# -> loupe sur les conditions -> appel à l'action discret. Pas de mascotte (variété avec les F18 du 26/11 et la vidéo A du jour).
# AUCUN montant (ni écrit ni dit). Source : revolut.com/fr-FR/legal/referrals-terms (consultée le 27/11/2026) : récompense indiquée
# dans l'invitation à la promotion (fixe, variable ou échelonnée), nombre maximum de personnes parrainées indiqué dans l'invitation,
# l'invité ouvre un compte Revolut Personnel à l'aide du lien de parrainage et suit les étapes dans les délais indiqués.
# Pas de prime en argent pour le filleul, jamais « illimité ».
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08, une synthèse par réplique, atempo 1.15, -19 dB moyen.
NAME = 'revolut17'
TITLE = 'Revolut vrai ou faux menthe'
ROOT = ':root{--bg:#040907;--ac:#5fe3b0}'
LINES = [
 ("Parrainage Revolut : vrai ou faux ? Trois idées reçues.", [("Parrainage Revolut :", None), ("vrai ou faux ?", None), ("Trois idées reçues.", None)]),
 ("Un : le filleul touche une prime en argent. Faux. La récompense va au parrain, selon son invitation.", [("1 : le filleul touche", None), ("une prime en argent.", None), ("Faux.", None), ("La récompense va au parrain,", None), ("selon son invitation.", None)]),
 ("Deux : on peut parrainer sans limite. Faux. Le nombre maximum est indiqué dans l'invitation.", [("2 : on peut parrainer", None), ("sans limite.", None), ("Faux.", None), ("Le nombre maximum", None), ("est dans l'invitation.", None)]),
 ("Trois : il faut ouvrir son compte avec le lien de parrainage. Vrai. Sinon, ça ne compte pas.", [("3 : il faut ouvrir son compte", None), ("avec le lien de parrainage.", None), ("Vrai.", None), ("Sinon, ça ne compte pas.", None)]),
 ("Ensuite, le filleul suit les étapes de l'invitation, dans les délais.", [("Ensuite, le filleul suit", None), ("les étapes de l'invitation,", None), ("dans les délais.", None)]),
 ("Mon conseil : lis bien les conditions avant de commencer.", [("Mon conseil :", None), ("lis bien les conditions", None), ("avant de commencer.", None)]),
 ("Si tu veux que je te parraine, écris-moi en privé.", [("Si tu veux", None), ("que je te parraine,", None), ("écris-moi en privé.", None)]),
]
SPLITS = [(0.2, 2.744), (3.194, 7.591), (8.04, 11.871), (12.321, 15.967), (16.417, 19.185), (19.635, 21.708), (22.158, 23.896)]
MINLEN = 1.6
GAP = 0.3
TAIL = 1.9

CSS = PCSS + '''
.mn{color:#5fe3b0;text-shadow:0 0 18px rgba(80,220,170,.45)}
.myth{position:absolute;left:110px;width:760px;padding:34px 40px;border-radius:30px;background:#f4efe4;color:#151515;box-shadow:0 30px 70px rgba(0,0,0,.6);transform:rotate(-2deg)}
.myth small{display:block;font:800 24px Inter;letter-spacing:3px;color:#7a7266;margin-bottom:10px}
.myth b{display:block;font:900 46px Inter;line-height:1.15}
.st{position:absolute;padding:10px 34px;border:8px solid;border-radius:18px;font:900 92px Inter;letter-spacing:6px;transform:rotate(-10deg);background:rgba(10,10,10,.35)}
.st.f{color:#ff5a5a;border-color:#ff5a5a;text-shadow:0 0 22px rgba(255,70,70,.5)}
.st.v{color:#5fe3b0;border-color:#5fe3b0;text-shadow:0 0 22px rgba(80,230,170,.5)}
.note{position:absolute;left:130px;width:720px;padding:24px 30px;border-radius:24px;background:rgba(18,24,22,.92);border:3px solid #5fe3b0;color:#f3efe6;font:800 36px Inter;line-height:1.3}
.mini{position:absolute;width:300px;height:180px;border-radius:24px;background:#f4efe4;box-shadow:0 20px 50px rgba(0,0,0,.6);display:flex;align-items:center;justify-content:center;font:900 60px Inter;letter-spacing:4px}
.doc{position:absolute;left:250px;top:620px;width:440px;height:540px;border-radius:22px;background:#f4efe4;box-shadow:0 30px 70px rgba(0,0,0,.6);padding:40px 40px}
.doc i{display:block;height:16px;border-radius:8px;background:#cfc6b6;margin:18px 0}
.doc i.s{width:60%}
.lens{position:absolute;width:300px;height:300px;border-radius:50%;border:16px solid #e0ac55;background:rgba(95,227,176,.12);box-shadow:0 0 40px rgba(224,172,85,.4)}
.lens:after{content:'';position:absolute;left:250px;top:250px;width:150px;height:34px;border-radius:17px;background:#e0ac55;transform:rotate(45deg);transform-origin:0 50%}
'''
DOC = '<div class="doc">' + '<i></i><i class="s"></i><i></i><i></i><i class="s"></i><i></i><i></i><i class="s"></i><i></i><i></i>' + '</div>'

BODY = hud('FRANCE · VRAI OU FAUX', 'REVOLUT') + BANNER + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hdx(230, [('h1 mn', 'PARRAINAGE REVOLUT', None, 'font-size:70px'), ('it gold', 'vrai ou faux ?', None, 'font-size:86px')]) + '''
   <div class="mini" style="left:150px;top:720px;transform:rotate(-8deg);color:#18a978">VRAI</div>
   <div class="mini" style="left:540px;top:760px;transform:rotate(7deg);color:#e04848">FAUX</div>
   <div class="tagp" style="left:300px;top:1080px" data-g="0.2" data-fx="pop">3 idées reçues</div></div>
  <div class="scene" data-s="1" data-in="right">''' + '<div class="num" style="left:110px;top:230px" data-g="1.0" data-fx="stamp">1</div>' + hdx(270, [('h1', 'IDÉE REÇUE N°1', '1.0', 'font-size:60px')], left=290, width=640) + '''
   <div class="myth" style="top:480px" data-g="1.0" data-fx="up"><small>ON ENTEND SOUVENT</small><b>« Le filleul touche une prime en argent »</b></div>
   <div class="st f" style="left:420px;top:700px" data-g="1.2" data-fx="stamp">FAUX</div>
   <div class="note" style="top:930px" data-g="1.3" data-fx="up">La récompense va au <span class="mn">parrain</span>, selon son invitation dans l'appli.</div></div>
  <div class="scene" data-s="2" data-in="up">''' + '<div class="num" style="left:110px;top:230px" data-g="2.0" data-fx="stamp">2</div>' + hdx(270, [('h1', 'IDÉE REÇUE N°2', '2.0', 'font-size:60px')], left=290, width=640) + '''
   <div class="myth" style="top:480px;transform:rotate(2deg)" data-g="2.0" data-fx="right"><small>ON ENTEND SOUVENT</small><b>« On peut parrainer sans limite »</b></div>
   <div class="st f" style="left:180px;top:690px" data-g="2.2" data-fx="stamp">FAUX</div>
   <div class="note" style="top:930px" data-g="2.3" data-fx="up">Le nombre <span class="mn">maximum</span> de filleuls est indiqué dans l'invitation.</div></div>
  <div class="scene" data-s="3" data-in="pop"><div class="floor"></div>''' + '<div class="num" style="left:110px;top:230px" data-g="3.0" data-fx="stamp">3</div>' + hdx(270, [('h1', 'IDÉE REÇUE N°3', '3.0', 'font-size:60px')], left=290, width=640) + '''
   <div class="myth" style="top:480px" data-g="3.0" data-fx="up"><small>ON ENTEND SOUVENT</small><b>« Il faut ouvrir son compte avec le lien de parrainage »</b></div>
   <div class="st v" style="left:400px;top:760px" data-g="3.2" data-fx="stamp" data-slow="3.2">VRAI</div>
   <div class="note" style="top:1000px" data-g="3.3" data-fx="up">Sans le lien au départ, le parrainage <span class="mn">ne compte pas</span>.</div></div>
  <div class="scene" data-s="4" data-in="right">''' + hdx(260, [('h1 mn', 'ENSUITE,', '4.0', 'font-size:66px'), ('it gold', "les étapes de l'invitation", '4.1', 'font-size:58px')]) + '''
   <div class="card2" style="left:130px;top:560px;width:780px" data-g="4.0" data-fx="up"><div class="t">Côté filleul</div>
    <div class="chk"><i>✓</i>compte Revolut Personnel</div><div class="chk" data-g="4.1" data-fx="fade"><i>✓</i>ouvert avec le lien reçu</div><div class="chk" data-g="4.1" data-fx="fade"><i>✓</i>étapes de l'invitation</div><div class="chk" data-g="4.2" data-fx="fade"><i>✓</i>dans les délais indiqués</div></div>
   <div class="tagp" style="left:150px;top:1120px" data-g="4.2" data-fx="pop">pas de prime en argent pour le filleul</div></div>
  <div class="scene" data-s="5" data-in="up"><div class="floor"></div>''' + hdx(230, [('h1', 'MON CONSEIL :', '5.0', 'font-size:66px'), ('it gold', 'lis bien les conditions.', '5.1', 'font-size:62px')]) + DOC + '''
   <div class="lens" style="left:460px;top:760px" data-g="5.1" data-fx="pop"></div>
   <div class="tagp" style="left:240px;top:1230px" data-g="5.2" data-fx="pop">avant de commencer</div></div>
  <div class="scene" data-s="6" data-in="pop"><div class="floor"></div>''' + hdx(230, [('h1', 'SI TU VEUX QUE', '6.0', 'font-size:66px'), ('h1', 'JE TE PARRAINE,', '6.1', 'font-size:66px'), ('it gold', 'écris-moi en privé.', '6.2', 'font-size:72px')]) + '''
   <div class="mini" style="left:150px;top:760px;transform:rotate(-8deg);color:#18a978">VRAI</div>
   <div class="mini" style="left:540px;top:800px;transform:rotate(7deg);color:#e04848">FAUX</div>
   <div class="cond" style="top:1090px;font-size:24px">Offre soumise aux conditions en vigueur · récompense du parrain<br>indiquée dans son invitation · nouveaux clients Revolut Personnel</div></div>
'''
