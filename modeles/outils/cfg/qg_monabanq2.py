import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qg_ecran import *
# Vidéos QG du 20/11/2026, vidéo 1 : Monabanq. Style E « écran d'appli en gros plan ».
# Format F8 « résultat d'abord » : notification « Virement reçu +80,00 € · prime de bienvenue » (exemple) dès la 1re image,
# puis les 4 étapes qui mènent à 280 € (20 + 60 + 60 + 80 + 60 de fidélité au 13e mois), total, appel à l'action.
# Source : https://www.monabanq.com/fr/parrainage.html (consultée le 20/11/2026) : offre de bienvenue filleul « jusqu'à 280 € »,
# valable depuis le 01/07/2026 : 20 € à l'ouverture (versés le 16 du mois suivant) + 60 € si au moins 300 € versés dans le mois
# suivant l'ouverture + 60 € pour une carte Visa et au moins 30 paiements carte dans les 2 mois + 80 € mobilité bancaire
# (mandat signé en ligne dans le mois) + 60 € de fidélité le 13e mois (compte conservé + 2 autres produits dont 1 d'épargne) ;
# primes reprises si clôture à l'initiative du client dans les 12 mois.
# Voix : Manon (smallest lightning_v3.1_pro, voice « manon »), 1re utilisation, ≈ 170 mots/min.
NAME = 'qg_monabanq2'
TITLE = 'QG Monabanq resultat d abord'
TAIL = 2.0
LINES = [
 ("Parrainage Monabanq : cette notif, c'est 80 € de prime. Et ça monte jusqu'à 280 €.", [("<em>Parrainage Monabanq</em> :", None), ("cette notif,", None), ("c'est <em>80 €</em> de prime.", None), ("Et ça monte", None), ("jusqu'à <em>280 €</em>.", None)]),
 ("Un : tu ouvres ton compte. 20 €.", [("Un : tu ouvres ton compte.", None), ("<em>20 €</em>", None)]),
 ("Deux : tu verses 300 € dans le mois. 60 €.", [("Deux : tu verses <em>300 €</em>", None), ("dans le mois.", None), ("<em>60 €</em>", None)]),
 ("Trois : trente paiements par carte en deux mois. Encore 60 €.", [("Trois : <em>30 paiements</em> carte", None), ("en 2 mois.", None), ("Encore <em>60 €</em>", None)]),
 ("Quatre : la mobilité bancaire, 80 €. Et 60 € de fidélité au treizième mois.", [("Quatre : la mobilité bancaire,", None), ("<em>80 €</em>.", None), ("Et <em>60 €</em> de fidélité", None), ("au 13<sup>e</sup> mois.", None)]),
 ("Envoie-moi Monabanq en privé, je t'envoie le lien.", [("Envoie-moi <em>MONABANQ</em>", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 5.87), (6.13, 8.01), (8.31, 11.28), (11.75, 14.77), (15.26, 20.15), (20.31, 22.84)]
GSTART = [[0.0, 1.0, 2.43, 4.0, 4.5], [6.14, 7.4], [8.32, 9.8, 10.5], [11.76, 13.0, 13.82], [15.27, 16.92, 17.97, 19.3], [20.32, 21.5, 22.1]]

CSS = '''
.lk{text-align:center;font:800 32px Inter;color:#64748b;margin-top:0}
.lk b{display:block;font:900 160px/1 Inter;color:#0f172a;letter-spacing:-4px;margin-bottom:6px}
.ntf{margin-top:46px;border-radius:34px;background:#f1f5f9;border:3px solid #e2e8f0;padding:24px 28px;box-shadow:0 16px 30px rgba(15,23,42,.16)}
.ntf .t{display:flex;align-items:center;gap:16px;font:800 28px Inter;color:#64748b}
.ntf .t i{width:52px;height:52px;border-radius:14px;background:linear-gradient(135deg,#2563eb,#60a5fa);display:block;flex:none}
.ntf .t span{margin-left:auto}
.ntf .h{font:900 40px Inter;margin-top:16px}
.ntf .a{font:900 92px/1.05 Inter;color:#16a34a;margin-top:4px;letter-spacing:-2px}
.ntf .s{font:700 30px Inter;color:#475569}
.ex{position:absolute;padding:6px 18px;border-radius:12px;background:#0f172a;color:#fff;font:800 26px Inter;letter-spacing:2px;z-index:7}
.ctr{text-align:center;margin-top:24px}
.ctr .v{font:900 150px/1 Inter;letter-spacing:-4px}
.ctr .k{font:800 34px Inter;color:#64748b;margin-top:8px}
.pb{height:44px;border-radius:22px;background:#e2e8f0;overflow:hidden;margin-top:34px}
.pb i{display:block;height:100%;width:100%;background:#16a34a;transform-origin:0 50%}
.m13{width:250px;height:250px;border-radius:30px;border:5px solid #0f172a;background:#fff;text-align:center;overflow:hidden;box-shadow:10px 10px 0 #0f172a}
.m13 .t{height:70px;background:#2563eb;color:#fff;font:900 34px/70px Inter;letter-spacing:2px}
.m13 .n{font:900 120px/1.4 Inter}
.ap .tot .r{display:flex;justify-content:space-between;font:800 36px Inter;height:76px;align-items:center;border-bottom:3px solid #eef2f7}
.ap .tot .r b{color:#16a34a;font:900 38px Inter}
'''

NOTIF = '''<div class="lk"><b>9:41</b>vendredi 20 novembre</div>
     <div class="ntf"><div class="t"><i></i>BANQUE<span>maintenant</span></div><div class="h">Virement reçu</div><div class="a">+80,00 €</div><div class="s">Prime de bienvenue (20 € + 60 €)</div></div>
     <div class="gl" style="margin-top:40px"></div><div class="gl" style="width:60%"></div>'''

TOT = ''.join(f'<div class="r">{l}<b>{v}</b></div>' for l, v in [('Ouverture', '20 €'), ('300 € versés', '60 €'), ('30 paiements', '60 €'), ('Mobilité', '80 €'), ('13<sup>e</sup> mois', '60 €')])

BODY = search('parrainage monabanq') + '''
  <div class="scene" data-s="0">
   <div class="zm" data-zg="0.1" data-zs="1.12" style="transform-origin:470px 860px">''' + phone(NOTIF) + hand(650, 830, '0.1') + '''</div>
   <div class="ex" style="left:640px;top:690px;transform:rotate(4deg)">EXEMPLE</div>
   <div class="gain" style="left:420px;top:1150px;font-size:84px" data-g="0.2" data-fx="stamp">+80 €</div>
   <div class="stk" style="left:150px;top:420px;transform:rotate(-4deg)" data-g="0.4" data-fx="stamp">jusqu'à 280 €</div></div>
  <div class="scene" data-s="1" data-in="right">''' + step(1, 4, 'OUVERTURE') + '''
   <div class="zm" data-zg="1.0" data-zs="1.12" style="transform-origin:470px 900px">''' + phone('''<div class="hd"><span class="bk">‹</span>Ouvrir un compte</div>
     <div class="lb">Parrainage</div><div class="fd on">Lien d'invitation<span class="ok">✓</span></div>
     <div class="lb">Compte</div><div class="fd">Compte courant</div>
     <div class="btn">Ouvrir mon compte</div><div class="gl"></div><div class="gl" style="width:60%"></div>''') + hand(470, 980, '1.0') + '''</div>
   <div class="gain" style="left:520px;top:1150px" data-g="1.1" data-fx="stamp">+20 €</div></div>
  <div class="scene" data-s="2" data-in="right">''' + step(2, 4, '1ER VERSEMENT') + '''
   <div class="zm" data-zg="2.0" data-zs="1.15" style="transform-origin:470px 770px">''' + phone('''<div class="hd"><span class="bk">‹</span>Alimenter</div>
     <div class="lb">Montant</div><div class="fd on" style="height:130px;font-size:64px"><span data-g="2.0" data-fx="type">300,00 €</span></div>
     <div class="lb">au moins 300 €, en une ou plusieurs fois</div>
     <div class="btn">Valider</div><div class="gl"></div><div class="gl" style="width:60%"></div>''') + hand(470, 1010, '2.1') + '''</div>
   <div class="stk" style="left:430px;top:420px;transform:rotate(4deg)" data-g="2.1" data-fx="pop">dans le mois</div>
   <div class="gain" style="left:520px;top:1150px" data-g="2.2" data-fx="stamp">+60 €</div></div>
  <div class="scene" data-s="3" data-in="right">''' + step(3, 4, 'CARTE') + '''
   <div class="zm" data-zg="3.0" data-zs="1.1" style="transform-origin:470px 800px">''' + phone('''<div class="hd"><span class="bk">‹</span>Paiements carte</div>
     <div class="ctr" data-g="3.0" data-fx="tick" data-count="30" data-suf=" / 30"><div class="v">0 / 30</div><div class="k">paiements</div></div>
     <div class="pb"><i data-g="3.0" data-fx="grow"></i></div>
     <div class="cal"><div class="m">Mois 1<b>✓</b></div><div class="m">Mois 2<b data-g="3.1" data-fx="pop">✓</b></div></div>''') + '''</div>
   <div class="stk" style="left:470px;top:420px;transform:rotate(4deg)" data-g="3.1" data-fx="pop">en 2 mois</div>
   <div class="gain" style="left:520px;top:1150px" data-g="3.2" data-fx="stamp">+60 €</div></div>
  <div class="scene" data-s="4" data-in="right">''' + step(4, 4, 'MOBILITÉ + FIDÉLITÉ') + '''
   <div class="zm" data-zg="4.0" data-zs="1.1" style="transform-origin:600px 720px">''' + phone('''<div class="hd"><span class="bk">‹</span>Mobilité bancaire</div>
     <div class="row" style="height:130px;font-size:44px">Changer de banque<span class="tg" style="display:block"><i></i>
       <span data-g="4.0" data-fx="fade" style="position:absolute;inset:0;border-radius:34px;background:#16a34a;display:block"><i style="left:58px"></i></span></span></div>
     <div class="lb">On prévient tes prélèvements et virements pour toi</div><div class="gl"></div><div class="gl" style="width:70%"></div>''') + hand(690, 705, '4.0') + '''</div>
   <div class="gain" style="left:150px;top:1060px" data-g="4.1" data-fx="stamp">+80 €</div>
   <div class="m13 abs" style="left:560px;top:930px;transform:rotate(3deg)" data-g="4.2" data-fx="pop"><div class="t">MOIS</div><div class="n">13</div></div>
   <div class="gain" style="left:560px;top:1210px;font-size:60px" data-g="4.3" data-fx="stamp">+60 €</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + phone('''<div class="hd">Mes primes</div><div class="big" style="font-size:120px">280 €</div>''') + '''
   <div class="endc" data-g="5.0" data-fx="up"><div class="k">ENVOIE-MOI EN PRIVÉ</div><div class="c">« MONABANQ »</div><div class="d">je t'envoie le lien</div><div class="b">@htm.invest</div></div>
   <div class="gain" style="left:290px;top:770px;font-size:60px" data-g="5.0" data-fx="stamp">TOTAL : 280 €</div>
   <div class="cond" style="top:925px" data-g="5.1" data-fx="fade">Offre soumise aux conditions en vigueur.<br>Offre de bienvenue Monabanq (1<sup>er</sup> compte courant, depuis le 01/07/2026), jusqu'à 280 € : 20 € à l'ouverture + 60 € si 300 € versés dans le mois + 60 € (carte Visa, 30 paiements en 2 mois) + 80 € (mobilité bancaire signée dans le mois) + 60 € au 13<sup>e</sup> mois (compte conservé et 2 autres produits dont 1 d'épargne). Primes reprises en cas de clôture sous 12 mois. Notification : exemple.<br>Lien de parrainage : je touche une prime.</div></div>
'''
