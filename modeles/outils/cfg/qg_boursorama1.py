import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qg_ecran import *
# Vidéos QG du 19/11/2026, vidéo 1 : Boursorama (BoursoBank). Style E « écran d'appli en gros plan » (1re utilisation).
# Format F7 « tuto écran 1-2-3 » : barre de recherche « parrainage boursorama » dès 0 s, téléphone dessiné sans logo,
# 4 étapes = 4 écrans, doigt qui tape, zoom punch sur la case importante, gain qui surgit à chaque étape, total 260 €.
# Source : https://www.boursobank.com/bon-plan/parrainage-boursobank (consultée le 19/11/2026) : prime filleul max 260 € =
# 20 € ouverture + 80 € 1er versement >= 300 € + 80 € carte (20 € puis 30 € puis 30 €, 1 opération/mois pendant 3 mois)
# + 80 € EasyMove (formulaire signé dans le mois suivant l'ouverture) ; primes reprises en cas de clôture sous 24 mois.
# Voix : Etienne (cartesia sonic-3.5, voice c6ccfe32-…), speed 1.2.
NAME = 'qg_boursorama1'
TITLE = 'QG Boursorama 260 euros en 4 etapes'
LINES = [
 ("Parrainage Boursorama : 260 €, en 4 étapes.", [("<em>Parrainage Boursorama</em> :", None), ("<em>260 €</em>,", None), ("en 4 étapes.", None)]),
 ("Un : tu ouvres ton compte via le lien d'invitation. 20 €.", [("Un : tu ouvres ton compte", None), ("via le <em>lien d'invitation</em>.", None), ("<em>20 €</em>", None)]),
 ("Deux : un premier versement de 300 € minimum. 80 €.", [("Deux : un premier versement", None), ("de <em>300 €</em> minimum.", None), ("<em>80 €</em>", None)]),
 ("Trois : un paiement carte par mois, pendant 3 mois. 80 €.", [("Trois : un paiement carte", None), ("par mois, pendant <em>3 mois</em>.", None), ("<em>80 €</em>", None)]),
 ("Quatre : EasyMove dans le mois. Encore 80 €.", [("Quatre : <em>EasyMove</em>", None), ("dans le mois.", None), ("Encore <em>80 €</em>", None)]),
 ("Envoie-moi Boursorama en privé, je t'envoie mon invitation.", [("Envoie-moi <em>BOURSORAMA</em>", None), ("en privé,", None), ("je t'envoie mon invitation.", None)]),
]
SPLITS = [(0.0, 3.29), (3.63, 7.15), (7.53, 11.48), (11.83, 15.77), (16.13, 19.24), (19.50, 22.45)]
GSTART = [[0.0, 1.2, 2.5], [3.65, 5.1, 6.6], [7.55, 9.1, 10.7], [11.85, 13.3, 15.0], [16.15, 17.3, 18.1], [19.52, 20.7, 21.3]]

CSS = '''
.ap .rw2{display:flex;align-items:center;gap:18px;height:96px;border-bottom:3px solid #eef2f7;font:800 36px Inter;white-space:nowrap}
.ap .rw2 .n{width:58px;height:58px;border-radius:29px;background:#0f172a;color:#fff;display:flex;align-items:center;justify-content:center;font:900 30px Inter;flex:none}
.ap .rw2 .q{margin-left:auto;font:900 40px Inter;color:#94a3b8}
.ap .rw2 .v{margin-left:auto;font:900 40px Inter;color:#16a34a}
.card{height:250px;border-radius:30px;background:linear-gradient(135deg,#1e293b,#334155);color:#fff;padding:30px 34px;position:relative;margin-top:10px}
.card .chip{width:80px;height:60px;border-radius:12px;background:#fbbf24}
.card .nb{position:absolute;left:34px;bottom:34px;font:800 38px 'DejaVu Sans Mono',monospace;letter-spacing:3px}
'''

ROWS0 = ''.join(f'<div class="rw2"><span class="n">{n}</span>{l}<span class="q">? €</span></div>' for n, l in [(1, 'Ouverture'), (2, '1er versement'), (3, 'Carte 3 mois'), (4, 'EasyMove')])

BODY = search('parrainage boursorama') + '''
  <div class="scene" data-s="0">''' + phone('''<div class="hd">Prime filleul</div><div class="lb">jusqu'à</div><div class="big">260 €</div>''' + ROWS0) + '''
   <div class="stk" style="left:470px;top:345px;transform:rotate(4deg)">ATTENDS !</div>
   <div class="stk" style="left:560px;top:650px;transform:rotate(-5deg);background:#fff" data-g="0.2" data-fx="stamp">4 ÉTAPES</div></div>
  <div class="scene" data-s="1" data-in="right">''' + step(1, 4, 'OUVERTURE') + '''
   <div class="zm" data-zg="1.1" data-zs="1.18" style="transform-origin:470px 760px">''' + phone('''<div class="hd"><span class="bk">‹</span>Ouvrir un compte</div>
     <div class="lb">Parrainage</div><div class="fd on">Invitation reçue<span class="ok">✓</span></div>
     <div class="lb">Prénom</div><div class="fd" style="color:#94a3b8">Ton prénom</div>
     <div class="btn">Commencer</div><div class="gl"></div><div class="gl" style="width:60%"></div>''') + hand(600, 760, '1.1') + '''</div>
   <div class="gain" style="left:520px;top:1150px" data-g="1.2" data-fx="stamp">+20 €</div></div>
  <div class="scene" data-s="2" data-in="right">''' + step(2, 4, '1ER VERSEMENT') + '''
   <div class="zm" data-zg="2.1" data-zs="1.15" style="transform-origin:470px 770px">''' + phone('''<div class="hd"><span class="bk">‹</span>1er versement</div>
     <div class="lb">Montant</div><div class="fd on" style="height:130px;font-size:64px"><span data-g="2.1" data-fx="type">300,00 €</span></div>
     <div class="lb">minimum 300 € pour la prime maximale</div>
     <div class="btn">Valider</div><div class="gl"></div><div class="gl" style="width:60%"></div>''') + hand(470, 1010, '2.2') + '''</div>
   <div class="gain" style="left:520px;top:1150px" data-g="2.2" data-fx="stamp">+80 €</div></div>
  <div class="scene" data-s="3" data-in="right">''' + step(3, 4, 'CARTE') + '''
   <div class="zm" data-zg="3.1" data-zs="1.1" style="transform-origin:470px 1000px">''' + phone('''<div class="hd"><span class="bk">‹</span>Ma carte</div>
     <div class="card"><div class="chip"></div><div class="nb">•••• 4821</div></div>
     <div class="lb">1 paiement par mois</div>
     <div class="cal"><div class="m">Mois 1<b data-g="3.1" data-fx="pop">+20 €</b></div><div class="m">Mois 2<b data-g="3.1" data-fx="pop">+30 €</b></div><div class="m">Mois 3<b data-g="3.2" data-fx="pop">+30 €</b></div></div>''') + hand(300, 1040, '3.1') + '''</div>
   <div class="gain" style="left:520px;top:1190px" data-g="3.2" data-fx="stamp">+80 €</div></div>
  <div class="scene" data-s="4" data-in="right">''' + step(4, 4, 'MOBILITÉ') + '''
   <div class="zm" data-zg="4.1" data-zs="1.18" style="transform-origin:600px 720px">''' + phone('''<div class="hd"><span class="bk">‹</span>Mobilité bancaire</div>
     <div class="rw2" style="height:130px;font-size:44px">EasyMove<span class="tg" style="margin-left:auto;width:120px;height:68px;border-radius:34px;background:#cbd5e1;position:relative;flex:none;display:block"><i style="position:absolute;left:6px;top:6px;width:56px;height:56px;border-radius:28px;background:#fff"></i>
       <span data-g="4.1" data-fx="fade" style="position:absolute;inset:0;border-radius:34px;background:#16a34a;display:block"><i style="position:absolute;left:58px;top:6px;width:56px;height:56px;border-radius:28px;background:#fff"></i></span></span></div>
     <div class="lb">On prévient ton ancienne banque et tes prélèvements pour toi</div><div class="gl"></div><div class="gl" style="width:70%"></div><div class="gl" style="width:50%"></div>''') + hand(690, 700, '4.1') + '''</div>
   <div class="stk" style="left:150px;top:1000px;transform:rotate(-4deg)" data-g="4.1" data-fx="pop">dans le mois</div>
   <div class="gain" style="left:520px;top:1150px" data-g="4.2" data-fx="stamp">+80 €</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + phone('''<div class="hd">Mes primes</div><div class="big" style="font-size:120px">260 €</div>''') + '''
   <div class="endc" data-g="5.0" data-fx="up"><div class="k">ENVOIE-MOI EN PRIVÉ</div><div class="c">« BOURSORAMA »</div><div class="d">je t'envoie mon invitation</div><div class="b">@htm.invest</div></div>
   <div class="cond" style="top:900px" data-g="5.1" data-fx="fade">Offre soumise aux conditions en vigueur.<br>Parrainage BoursoBank, prime filleul jusqu'à 260 € : 20 € à l'ouverture + 80 € (1er versement d'au moins 300 €) + 80 € (1 opération carte par mois pendant 3 mois : 20 + 30 + 30 €) + 80 € (EasyMove signé dans le mois). Ouverture via l'invitation de parrainage ; primes reprises si le compte est clôturé sous 24 mois.<br>Lien de parrainage : je touche une prime.</div></div>
'''
