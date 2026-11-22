import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qg_explainer import *
# Vidéos QG du 22/11/2026, vidéo 1 : Monabanq. Style X « Explainer mascotte » (1re utilisation), format F14 « Pourquoi la banque te paie ».
# Question -> « arnaque ? non » -> trouver un client coûte cher (pubs, affiches, influenceurs) -> avec le parrainage elle donne
# cet argent au filleul et au parrain -> elle espère un client fidèle qui prendra d'autres services -> gagnant-gagnant -> messagerie.
# Aucun chiffre de coût de pub ni de « coût d'acquisition » (pas de source officielle).
# Source : https://www.monabanq.com/fr/parrainage.html (consultée le 22/11/2026) : filleul jusqu'à 280 € (offre de bienvenue valable
# depuis le 01/07/2026 : 20 € à l'ouverture + 60 € si 300 € versés dans le mois suivant + 60 € pour 30 paiements carte dans les 2 mois
# (carte Visa) + 80 € de mobilité bancaire + 60 € de fidélité au 13e mois avec 2 autres produits dont 1 épargne) ; parrain 30 € (Pratiq+,
# Uniq) ou 50 € (Uniq+) pour les parrainages à partir du 16/11/2026, versés 60 jours après l'ouverture. Pas de date de fin publiée.
# QC 1 (83/100, bloquant : pastille sur les mentions 22,5-26 s) -> chat et mentions remontés, pièce qui saute dès 0 s, « jusqu'à 280 € » à 1,2 s.
# Voix : Manon (smallest, lightning_v3.1_pro), une réplique par synthèse, -5 dB, atempo 0.97.
NAME = 'qg_monabanq3'
TITLE = 'QG Monabanq pourquoi la banque te paie'
LINES = [
 ("Parrainage Monabanque : pourquoi la banque te paie pour ouvrir un compte ?",
  [("<em>Parrainage Monabanq</em> :", None), ("pourquoi la banque", None), ("te <em>paie</em>", None), ("pour ouvrir un compte ?", None)]),
 ("Une arnaque ? Non. Trouver un client, ça lui coûte cher : des pubs, des affiches, des influenceurs.",
  [("Une <em>arnaque</em> ?", None), ("<em>Non.</em>", None), ("Trouver un client,", None), ("ça lui coûte <em>cher</em> :", None),
   ("des <em>pubs</em>,", None), ("des <em>affiches</em>,", None), ("des <em>influenceurs</em>.", None)]),
 ("Avec le parrainage, elle donne cet argent à toi, et à ton parrain.",
  [("Avec le <em>parrainage</em>,", None), ("elle donne cet argent", None), ("à <em>toi</em>", None), ("et à ton <em>parrain</em>.", None)]),
 ("Et elle y gagne quoi ? Un client fidèle, qui prendra d'autres services.",
  [("Et elle y gagne <em>quoi</em> ?", None), ("Un client <em>fidèle</em>,", None), ("qui prendra d'autres services.", None)]),
 ("Toi, tu touches ta prime par étapes, si tu remplis les conditions. Gagnant-gagnant.",
  [("Toi, tu touches <em>ta prime</em>", None), ("par étapes,", None), ("si tu remplis <em>les conditions</em>.", None), ("<em>Gagnant-gagnant</em>.", None)]),
 ("Envoie-moi le mot Monabanque en privé, et je te parraine.",
  [("Envoie-moi le mot", None), ("<em>MONABANQ</em>", None), ("en privé,", None), ("et je te <em>parraine</em>.", None)]),
]
SPLITS = [(0.105, 3.197), (3.942, 10.058), (10.656, 13.94), (14.61, 18.152), (19.027, 23.437), (24.243, 27.015)]
GSTART = [[0.1, 1.24, 1.86, 2.27], [3.94, 4.97, 5.8, 6.83, 7.55, 8.17, 9.1], [10.66, 11.58, 12.51, 13.13], [14.61, 15.64, 16.88],
          [19.03, 20.37, 21.19, 22.84], [24.24, 24.96, 25.58, 26.3]]

CSS = '''
.qm{position:absolute;font:400 120px/1 Anton;color:#d4af37}
'''

COND = ('<b>Offre soumise aux conditions en vigueur.</b> Parrainage Monabanq, offre vérifiée le 22/11/2026 sur monabanq.com : filleul jusqu\'à 280 € '
        '(offre de bienvenue : 20 € à l\'ouverture + 60 € si 300 € versés dans le mois + 60 € pour 30 paiements carte en 2 mois + 80 € avec la '
        'mobilité bancaire + 60 € au 13e mois avec 2 autres produits dont 1 épargne) ; parrain 30 € ou 50 € selon le compte ouvert. '
        'Nouveaux clients majeurs résidant en France, sous réserve d\'acceptation du dossier. <b>Lien de parrainage : je touche une prime.</b>')

BODY = '''
  <div class="scene" data-s="0">''' + xtitle('Parrainage Monabanq', 'pourquoi elle te paie ?', 240, g_line='0.1', s1=104, s2=96, uw=700) + \
    mascot(310, 600, 1.25, 'o', 'up', 'jump', 'up') + '''
   <div class="qm" style="left:190px;top:600px;rotate:-14deg" data-g="0.1" data-fx="pop">?</div>
   <div class="qm" style="left:730px;top:560px;rotate:12deg;font-size:150px" data-g="0.2" data-fx="pop">?</div>
   <div class="pill" style="left:255px;top:1060px" data-g="0.1" data-fx="pop">jusqu'à 280 € pour toi*</div>
   <div class="lab" style="left:0;width:930px;top:1160px;font:700 28px Inter;color:#b9ad93" data-g="0.1" data-fx="fade">* prime filleul si conditions remplies · offre soumise à conditions</div></div>
  <div class="scene" data-s="1" data-in="right">
   <div class="stampx" style="left:180px;top:250px;rotate:-5deg" data-g="1.0" data-fx="stamp">ARNAQUE ?</div>
   <div class="pill" style="left:600px;top:470px;font:400 80px Anton;padding:6px 40px" data-g="1.1" data-fx="stamp">NON</div>''' + \
    icon('bank', 365, 600, 230, '1.2', 'pop') + '''
   <div class="lab" style="left:0;width:930px;top:850px" data-g="1.3" data-fx="up">1 nouveau client = <em>très cher</em></div>''' + \
    icon('tv', 90, 950, 210, '1.4', 'pop', -6) + icon('pub', 370, 950, 210, '1.5', 'pop', 4) + icon('phone', 650, 950, 210, '1.6', 'pop', 6) + '''
   <div class="lab" style="left:95px;top:1170px;font-size:32px;width:200px" data-g="1.4" data-fx="fade">pubs</div>
   <div class="lab" style="left:375px;top:1170px;font-size:32px;width:200px" data-g="1.5" data-fx="fade">affiches</div>
   <div class="lab" style="left:655px;top:1170px;font-size:32px;width:200px" data-g="1.6" data-fx="fade">influenceurs</div>''' + \
    mascot(80, 560, 0.62, 'flat', 'point', 'idle', '', '1.2', 'pop') + '''</div>
  <div class="scene" data-s="2" data-in="up">''' + icon('bank', 365, 230, 220) + '''
   <div class="lab" style="left:0;width:930px;top:470px;font-size:44px" data-g="2.0" data-fx="pop">le <em>parrainage</em></div>
   <div class="fly" style="position:absolute;left:180px;top:560px">''' + icon('bill', 0, 0, 170, '2.1', 'left', -18) + '''</div>
   <div class="fly" style="position:absolute;left:590px;top:560px">''' + icon('bill', 0, 0, 170, '2.1', 'right', 16) + '''</div>
   <div class="card" style="left:70px;top:760px;width:380px;text-align:center" data-g="2.2" data-fx="up"><div class="t">TOI · FILLEUL</div><div class="v">280 €</div><div class="s">maximum, par étapes</div></div>
   <div class="card" style="left:500px;top:760px;width:380px;text-align:center" data-g="2.3" data-fx="up"><div class="t">TON PARRAIN</div><div class="v">30-50 €</div><div class="s">selon le compte</div></div>
   <div class="emo" style="left:410px;top:1080px" data-g="2.3" data-fx="pop">🤝</div></div>
  <div class="scene" data-s="3" data-in="pop">''' + mascot(90, 640, 1.15, 'open', 'hip', 'idle', 'up') + '''
   <div class="bd" style="left:110px;top:300px;--tx:160px" data-g="3.0" data-fx="pop">Et elle y gagne<br><em>quoi ?</em></div>''' + \
    icon('client', 560, 600, 200, '3.1', 'pop') + '''
   <div class="lab" style="left:520px;top:810px;width:290px;font-size:34px" data-g="3.1" data-fx="fade">un client <em>fidèle</em></div>''' + \
    icon('card', 480, 900, 170, '3.2', 'pop', -8) + icon('piggy', 680, 900, 170, '3.2', 'pop', 6) + '''
   <div class="lab" style="left:470px;top:1080px;width:400px;font-size:32px" data-g="3.2" data-fx="fade">+ d'autres <em>services</em></div></div>
  <div class="scene" data-s="4" data-in="right">''' + notif(250, '60 €', 'Virement reçu', 'Prime de bienvenue', '4.0', 'up') + '''
   <div class="cnote" style="top:455px" data-g="4.0" data-fx="fade">prime filleul si conditions remplies</div>
   <div class="steps" style="top:540px">
    <div class="r" data-g="4.1" data-fx="left"><b>20 €</b>ouverture</div>
    <div class="r" data-g="4.1" data-fx="left"><b>60 €</b>300 € versés</div>
    <div class="r" data-g="4.2" data-fx="left"><b>60 €</b>30 paiements carte</div>
    <div class="r" data-g="4.2" data-fx="left"><b>80 €</b>mobilité bancaire</div>
    <div class="r" data-g="4.2" data-fx="left"><b>60 €</b>fidélité 13e mois</div>
    <div class="tot" data-g="4.3" data-fx="stamp">= jusqu'à 280 €</div></div>''' + \
    mascot(620, 820, 0.92, 'open', 'up', 'jump', 'up') + '''
   <div class="pill dk" style="left:220px;top:1230px;font:400 64px Anton;color:#d4af37" data-g="4.3" data-fx="stamp">GAGNANT-GAGNANT</div></div>
  <div class="scene" data-s="5" data-in="up">
   <div class="chat" style="top:220px;height:820px"><div class="hd"><div class="av"></div><div><div class="nm">@htm.invest</div><div class="st">parrainage Monabanq</div></div></div>
    <div class="msg me" style="top:190px" data-g="5.1" data-fx="pop">MONABANQ<span class="tm">lu ✓✓</span></div>
    <div class="dots" style="top:340px" data-g="5.2" data-fx="pop"><i></i><i></i><i></i></div>
    <div class="msg you" style="top:340px" data-g="5.3" data-fx="pop">je te parraine 🤝</div>
    <div class="pill dk sm" style="left:60px;top:520px;font-size:28px" data-g="5.3" data-fx="up">⏳ offre Monabanq en cours · vérifiée le 22/11/2026</div>
   </div>''' + mascot(620, 850, 0.55, 'smile', 'point', 'idle', '', '5.0', 'pop') + '''
   <div class="cond" style="top:1065px">''' + COND + '''</div></div>
'''
