import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qg_explainer import *
# Vidéos QG du 26/11/2026, vidéo 1 : Hello bank. Style X « Explainer mascotte », format F8 « Résultat d'abord » :
# notification « Virement reçu +80 € » dès la 1re image (« prime filleul si conditions remplies » dessous), puis d'où ça vient :
# lien de parrainage avant le 30/11 15 h -> 80 € à l'ouverture (Hello One ou Hello Prime) -> +50 € au 13e mois (Hello Prime,
# 5 paiements ou retraits carte par mois) -> +200 € en bon d'achat avec Hello Start+ -> jusqu'à 330 € -> fausse conversation.
# Source : https://www.hellobank.fr/fr/votre-offre-parrainage (consultée le 26/11/2026) : filleul 80 € (Hello One ou Hello Prime)
# + 50 € versés le 13e mois avec Hello Prime (au moins 5 paiements ou retraits par mois pendant les 12 premiers mois) + bon d'achat
# 200 € avec Hello Start+ (mobilité bancaire, ouverture entre le 10/08/2026 et le 11/01/2027) : jusqu'à 330 € ; parrain 150 € ;
# demande via le lien avant le 30/11/2026 à 15 h (sous réserve d'évolution), ouverture définitive au plus tard le 30/12/2026 ;
# compte et carte à garder au moins 1 an ; filleul sans compte Hello bank.
# Voix : Leo (xai), une synthèse par réplique ; « Parrainage Hello bank » compris « et LSBanque » au 1er essai -> écrit
# « Parrainage, Hello banque ! » ; silences internes ramenés à 0,16 s, niveaux à -19 dB, atempo 0.94 sur les répliques 2 et 5.
NAME = 'qg_hellobank4'
TITLE = 'QG Hello bank résultat d abord'
GAP = 0.22
TAIL = 1.15
LINES = [
 ("Parrainage, Hello banque ! Ce virement de 80 €, il peut être pour toi.",
  [("<em>Parrainage Hello bank</em> !", None), ("Ce virement de <em>80 €</em>,", None), ("il peut être pour <em>toi</em>.", None)]),
 ("Ouvre ton compte avec un lien de parrainage, avant le trente novembre.",
  [("Ouvre ton compte", None), ("avec un lien", None), ("de <em>parrainage</em>,", None), ("avant le <em>30 novembre</em>.", None)]),
 ("80 € à l'ouverture, avec Hello One ou Hello Prime.",
  [("<em>80 €</em> à l'ouverture,", None), ("avec Hello One", None), ("ou Hello Prime.", None)]),
 ("Avec Hello Prime, 50 € de plus au treizième mois, sous conditions.",
  [("Avec <em>Hello Prime</em>,", None), ("<em>50 €</em> de plus", None), ("au 13e mois,", None), ("sous <em>conditions</em>.", None)]),
 ("Et 200 € en bon d'achat, si tu changes de banque avec Hello Start plus.",
  [("Et <em>200 €</em> en bon d'achat,", None), ("si tu changes de banque", None), ("avec <em>Hello Start+</em>.", None)]),
 ("Envoie-moi le mot Hello en privé, et je te parraine.",
  [("Envoie-moi le mot", None), ("<em>HELLO</em> en privé,", None), ("et je te <em>parraine</em>.", None)]),
]
SPLITS = [(0.15, 5.061), (5.361, 9.342), (9.642, 13.43), (13.73, 18.139), (18.439, 22.811), (23.111, 26.565)]

CSS = '''
.qm{position:absolute;font:400 120px/1 Anton;color:#d4af37}
.cal{position:absolute;left:300px;top:560px;width:330px;border-radius:34px;overflow:hidden;background:#f4efe4;color:#16130f;text-align:center;box-shadow:0 18px 40px rgba(0,0,0,.5)}
.cal .h{background:#d4af37;font:400 46px/1.6 Anton;letter-spacing:3px}
.cal .d{font:400 170px/1.1 Anton}
.cal .s{font:800 34px Inter;padding-bottom:18px}
.big{position:absolute;left:0;width:930px;text-align:center;font:400 230px/1 Anton;color:#d4af37;text-shadow:0 14px 40px rgba(0,0,0,.6)}
.steps{width:820px}
.steps .r{font-size:33px}
.steps .r b{min-width:170px}
'''

COND = ('<b>Offre soumise aux conditions en vigueur.</b> Parrainage Hello bank, offre vérifiée le 26/11/2026 sur hellobank.fr : filleul 80 € '
        '(Hello One ou Hello Prime) ; + 50 € au 13e mois avec Hello Prime si 5 paiements ou retraits carte par mois pendant 12 mois ; '
        '+ bon d\'achat de 200 € avec Hello Start+ (mobilité bancaire) : jusqu\'à 330 €. Demande via le lien avant le 30/11/2026 à 15 h, '
        'sous réserve d\'évolution ; compte à garder 1 an ; sous réserve d\'acceptation du dossier. <b>Lien de parrainage : je touche une prime.</b>')

BODY = '''
  <div class="scene" data-s="0">''' + xtitle('Parrainage Hello bank', 'ce virement pour toi ?', 230, g_line='0.1', s1=92, s2=84, uw=680) + \
    notif(520, '80 €', 'Virement reçu', 'Prime de bienvenue') + '''
   <div class="cnote" style="top:725px">prime filleul si conditions remplies</div>''' + \
    mascot(330, 820, 1.0, 'open', 'up', 'jump', 'up') + '''
   <div class="pill" style="left:250px;top:1190px">jusqu'à 330 € pour toi*</div>
   <div class="lab" style="left:0;width:930px;top:1290px;font:700 28px Inter;color:#b9ad93">* offre soumise à conditions · Hello One ou Hello Prime</div></div>
  <div class="scene" data-s="1" data-in="right">''' + icon('phone', 110, 300, 230, '1.0', 'pop', -8) + '''
   <div class="lab" style="left:360px;top:330px;width:520px;font-size:44px;text-align:left;white-space:normal" data-g="1.1" data-fx="left">avec un <em>lien de parrainage</em></div>
   <div class="cal" data-g="1.1" data-fx="stamp"><div class="h">NOVEMBRE</div><div class="d">30</div><div class="s">avant 15 h</div></div>''' + \
    mascot(640, 900, 0.7, 'o', 'pointl', 'idle', 'up', '1.1', 'pop') + '''
   <div class="pill dk" style="left:110px;top:1000px" data-g="1.2" data-fx="up">⏳ jusqu'au 30/11, 15 h</div></div>
  <div class="scene" data-s="2" data-in="up">
   <div class="lab" style="left:0;width:930px;top:270px;font-size:44px" data-g="2.0" data-fx="fade">à l'ouverture du compte</div>
   <div class="big" style="top:360px" data-g="2.0" data-fx="stamp">80 €</div>
   <div class="fly" style="position:absolute;left:90px;top:640px">''' + icon('bill', 0, 0, 170, '2.0', 'left', -18) + '''</div>
   <div class="fly" style="position:absolute;left:670px;top:640px">''' + icon('bill', 0, 0, 170, '2.0', 'right', 16) + '''</div>
   <div class="card" style="left:110px;top:860px;width:340px;text-align:center" data-g="2.1" data-fx="up"><div class="t">OFFRE</div><div class="v">HELLO ONE</div><div class="s">sans condition de revenus</div></div>
   <div class="card" style="left:490px;top:860px;width:340px;text-align:center" data-g="2.2" data-fx="up"><div class="t">OU OFFRE</div><div class="v">HELLO PRIME</div><div class="s">dès 1 500 € nets / mois</div></div></div>
  <div class="scene" data-s="3" data-in="right">''' + mascot(80, 700, 1.0, 'open', 'hip', 'idle', 'up') + '''
   <div class="bd" style="left:90px;top:300px;--tx:150px" data-g="3.0" data-fx="pop">Avec Hello Prime :<br><em>+50 € en plus</em></div>''' + \
    icon('card', 520, 660, 190, '3.1', 'pop', -8) + '''
   <div class="card" style="left:470px;top:880px;width:420px;text-align:center" data-g="3.2" data-fx="up"><div class="t">AU 13e MOIS</div><div class="v">+50 €</div><div class="s">si 5 paiements ou retraits carte / mois pendant 12 mois</div></div></div>
  <div class="scene" data-s="4" data-in="up">
   <div class="steps" style="top:300px">
    <div class="r" data-g="4.0" data-fx="left"><b>80 €</b>ouverture du compte</div>
    <div class="r" data-g="4.0" data-fx="left"><b>+50 €</b>13e mois · Hello Prime</div>
    <div class="r" data-g="4.0" data-fx="left"><b>+200 €</b>bon d'achat · Hello Start+</div>
    <div class="tot" data-g="4.2" data-fx="stamp" data-slow="4.2">= jusqu'à 330 €</div></div>
   <div class="lab" style="left:80px;top:770px;width:820px;font-size:30px;color:#b9ad93;text-align:left;white-space:normal" data-g="4.1" data-fx="fade">Hello Start+ : le service gratuit de changement de banque (tes virements et prélèvements suivent)</div>''' + \
    icon('piggy', 150, 1010, 210, '4.1', 'pop', -6) + mascot(560, 980, 0.95, 'open', 'up', 'jump', 'up', '4.2', 'pop') + '''</div>
  <div class="scene" data-s="5" data-in="up">
   <div class="chat" style="top:220px;height:800px"><div class="hd"><div class="av"></div><div><div class="nm">@htm.invest</div><div class="st">parrainage Hello bank</div></div></div>
    <div class="msg me" style="top:180px" data-g="5.1" data-fx="pop">HELLO<span class="tm">lu ✓✓</span></div>
    <div class="dots" style="top:330px" data-g="5.1" data-fx="pop"><i></i><i></i><i></i></div>
    <div class="msg you" style="top:330px" data-g="5.2" data-fx="pop">je te parraine 🤝</div>
    <div class="pill dk sm" style="left:50px;top:510px;font-size:27px" data-g="5.2" data-fx="up">⏳ offre Hello bank jusqu'au 30/11/2026, 15 h</div>
   </div>''' + mascot(650, 760, 0.5, 'smile', 'point', 'idle', '', '5.0', 'pop') + '''
   <div class="cond" style="top:1045px">''' + COND + '''</div></div>
'''
