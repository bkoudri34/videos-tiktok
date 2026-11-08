import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
NAME = 'luxe_fortuneo'
TITLE = 'Fortuneo nuit et or'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Marre de payer des frais pour ta carte bancaire ?!", [("Marre de payer", None), ("des frais", None), ("pour ta carte bancaire ?!", None)]),
 ("Le seul truc qui grossit... c'est la facture.", [("Le seul truc qui grossit…", None), ("c'est la facture.", None)]),
 ("Et si on te disait qu'il y a mieux ?", [("Et si on te disait", None), ("qu'il y a mieux ?", None)]),
 ("Fortuneo : jusqu'à 260 euros à l'ouverture de ton compte.", [("Fortuneo :", None), ("jusqu'à 260 €", "jusqu'à deux cent soixante euros"), ("à l'ouverture de ton compte.", None)]),
 ("160 euros avec la carte Gold, 80 euros avec neoChange, et 20 euros avec le Livret plus.", [("160 € carte Gold", "cent soixante euros avec la carte Gold,"), ("80 € neoChange", "quatre-vingts euros avec neoChange,"), ("20 € Livret +", "et vingt euros avec le Livret plus.")]),
 ("L'offre court jusqu'au 20 décembre.", [("L'offre court", None), ("jusqu'au 20 décembre.", "jusqu'au vingt décembre.")]),
 ("Envoie-moi FORTUNEO en privé. Et profite, sans te ruiner !", [("Envoie-moi", None), ("FORTUNEO", None), ("en privé.", None), ("Et profite,", None), ("sans te ruiner !", None)]),
]
SPLITS = [(0.0, 2.36), (2.66, 5.07), (5.38, 7.06), (7.36, 10.96), (11.25, 16.91), (17.33, 19.10), (19.47, 22.76)]
CSS = ''
STRIP = 'TOTAL    15,00\n-----------\n COTISATION\n CARTE  12,00\n CONFORT 3,00\n***********\nMERCI !\n\nTOTAL    15,00\n-----------\n COTISATION\n CARTE  12,00\n CONFORT 3,00\n***********\nMERCI !'
ticks = ''.join(f'<div class="tk" style="transform:rotate({i*6}deg);{"height:40px" if i%5==0 else "opacity:.6"}"></div>' for i in range(60))
BODY = hud('FRANCE · BANQUE EN LIGNE', 'BON PLAN') + '''
''' + counter_scene(0, 'Banque Hors de Prix', 'FRAIS DE LUXE', '15,00', 'Ça vous fera 15 € de frais,<br>s\'il vous plaît.', '0.1', '0.1', STRIP).replace('class="sign gold"', 'class="sign gold" style="top:720px"').replace('style="left:420px;top:880px"', 'style="left:410px;top:900px"') + '''
  ''' + head(230, [('h1', 'MARRE DE PAYER', None), ('big gold', '15 €', None), ('it gold', 'de frais pour ta carte ?!', '0.2')]).replace('class="hd"', 'class="hd scene" data-s="0"') + '''
  <div class="scene" data-s="1" data-in="pop">''' + head(230, [('h1', 'LE SEUL TRUC', '1.0'), ('h1', 'QUI GROSSIT…', '1.0'), ('it gold', "c'est la facture.", '1.1')]) + '''
   <div class="rcpt" style="top:700px"><div class="t">BANQUE HORS DE PRIX</div><div class="s">Agence du Portefeuille-Vide</div><hr>
    <div class="row"><span>Cotisation carte</span><span>12,00</span></div><div class="row"><span>Frais « confort »</span><span>3,00</span></div><div class="row"><span>Sourire du conseiller</span><span>0,00</span></div><hr>
    <div class="row tot"><span>TOTAL</span><span>15,00 €</span><svg class="abs" style="left:-30px;top:-26px" width="560" height="110" viewBox="0 0 560 110"><path d="M30 55 C30 10 530 5 535 50 C540 100 40 105 20 60" fill="none" stroke="#e5322d" stroke-width="6" pathLength="1" stroke-dasharray="1" data-g="1.1" data-fx="draw"/></svg></div><hr>
    <div class="s">MERCI POUR<br>VOTRE GÉNÉROSITÉ :)</div></div></div>
  <div class="scene" data-s="2" data-in="pop">''' + head(230, [('h1 s', 'ET SI ON TE DISAIT…', '2.0'), ('it gold', "qu'il y a mieux ?", '2.1')]) + '''
   <div class="orb" style="left:200px;top:560px;width:680px;height:1020px"></div><div class="orb" style="left:260px;top:620px;width:560px;height:900px;opacity:.6"></div>
   <div class="phone" data-g="2.0" data-fx="up"><div class="notch"></div>
    <div style="font:700 26px Inter;color:#bbb;margin-top:30px">Offre de bienvenue</div>
    <div style="font:900 64px Inter;margin-top:10px">Fortuneo</div>
    <div class="gold" style="font:900 120px 'DejaVu Serif',serif;margin-top:10px">260 €</div>
    <div style="font:600 26px Inter;color:#ddd">jusqu'à · nouveaux clients</div>
    <div style="display:inline-block;margin-top:26px;background:#e0ac55;color:#1a1408;font:800 32px Inter;padding:14px 40px;border-radius:30px">Découvrir</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:34px 22px 0">
     <div style="height:150px;border-radius:18px;background:linear-gradient(135deg,#3a2c14,#d9a24c);font:800 26px Inter;padding-top:96px">Carte Gold</div>
     <div style="height:150px;border-radius:18px;background:linear-gradient(135deg,#1c2a3a,#5aa0d8);font:800 26px Inter;padding-top:96px">neoChange</div>
     <div style="height:150px;border-radius:18px;background:linear-gradient(135deg,#2a1c2c,#c06aa0);font:800 26px Inter;padding-top:96px">Livret +</div>
     <div style="height:150px;border-radius:18px;background:linear-gradient(135deg,#1d2a1d,#6ac07a);font:800 26px Inter;padding-top:96px">Appli</div></div></div>
   <div class="spark" style="left:170px;top:900px" data-g="2.1" data-fx="pop">✦</div><div class="spark" style="left:860px;top:760px" data-g="2.1" data-fx="pop">✦</div><div class="spark" style="left:830px;top:1320px" data-g="2.1" data-fx="pop">✦</div></div>
  <div class="scene" data-s="3" data-in="pop"><div class="floor"></div><div class="rays"></div><div class="emb" data-g="3.0" data-fx="pop"><span class="gold" style="font:900 170px 'DejaVu Serif',serif">€</span></div>
   ''' + head(720, [('h1', 'FORTUNEO', '3.0'), ('big gold', "260 €", '3.1'), ('h1 s', "À L'OUVERTURE", '3.2')]).replace('class="big gold"', 'class="big gold" style="font-size:180px"') + '''</div>
  <div class="scene" data-s="4" data-in="pop">''' + head(230, [('h1', 'LE DÉTAIL', '4.0'), ('it gold', 'jusqu\'à 260 €', '4.0')]) + '''
   <div class="coin" style="left:130px;top:1040px" data-g="4.0" data-fx="pop"></div><div class="coin" style="left:130px;top:930px" data-g="4.1" data-fx="pop"></div><div class="coin" style="left:130px;top:820px" data-g="4.2" data-fx="pop"></div>
   <div class="ldr" style="left:450px;top:1088px;width:100px" data-g="4.0" data-fx="grow"></div><div class="lbl" style="top:1062px" data-g="4.0" data-fx="left"><b>160 €</b> · CARTE GOLD</div>
   <div class="ldr" style="left:450px;top:978px;width:100px" data-g="4.1" data-fx="grow"></div><div class="lbl" style="top:952px" data-g="4.1" data-fx="left"><b>80 €</b> · NEOCHANGE</div>
   <div class="ldr" style="left:450px;top:868px;width:100px" data-g="4.2" data-fx="grow"></div><div class="lbl" style="top:842px" data-g="4.2" data-fx="left"><b>20 €</b> · LIVRET +</div>
   <div class="abs" style="left:110px;top:1150px;width:360px;height:40px;border-radius:50%;background:radial-gradient(ellipse,rgba(255,200,110,.8),transparent 70%)"></div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="floor"></div>''' + head(230, [('h1', "L'OFFRE COURT…", '5.0'), ('it gold', 'jusqu\'au 20 décembre.', '5.1')]) + '''
   <div class="dial">''' + ticks + '''<div class="nd" data-g="5.0" data-fx="sweep"></div>
    <div class="abs" style="left:0;width:600px;top:170px;text-align:center" data-g="5.1" data-fx="stamp" data-slow="5.1"><div style="font:800 40px Inter;letter-spacing:4px">JUSQU'AU</div><div class="gold" style="font:900 150px 'DejaVu Serif',serif;line-height:1.1">20/12</div><div style="font:700 32px Inter;letter-spacing:6px;color:#bba98a">2026</div></div></div></div>
  <div class="scene" data-s="6" data-in="pop">''' + head(230, [('h1', 'ENVOIE-MOI', '6.0'), ('big gold', '« FORTUNEO »', '6.1'), ('it gold', 'en privé.', '6.2')]).replace('class="big gold"', 'class="big gold" style="font-size:120px"') + '''
   <div class="pill" style="top:690px" data-g="6.1" data-fx="up"><div class="pin">€</div><div><b>OFFRE DE BIENVENUE</b><span>jusqu'à 260 € · jusqu'au 20/12</span></div></div>
   <div class="pill" style="top:815px" data-g="6.2" data-fx="up"><div class="pin">✉</div><div><b>CODE PROMO</b><span>je te l'envoie en privé</span></div></div>
   <div class="search" style="top:950px" data-g="6.2" data-fx="fade"><svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg><span data-g="6.2" data-fx="type">@htm.invest</span></div>
   ''' + head(1090, [('h1', 'PROFITE !', '6.3'), ('it gold', 'sans te ruiner.', '6.4')]) + '''
   <div class="cond" style="top:1400px">Offre de bienvenue Fortuneo soumise aux conditions en vigueur<br>nouveaux clients · montant maximum · jusqu'au 20/12/2026</div></div>
'''
GSTART = [[0.1, 0.8, 1.2], [2.7, 4.3], [5.4, 6.3], [7.4, 8.2, 9.7], [11.3, 13.4, 15.1], [17.3, 18.0], [19.5, 19.9, 20.5, 21.4, 22.1]]
