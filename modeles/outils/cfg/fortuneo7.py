import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Fortuneo, 12/11/2026 21:00 - style v3 nuit & or, accent vert anis. Offre de bienvenue jusqu'à 260 € (carte Gold : 160 € après 5 paiements en 90 jours
# + 80 € mobilité neoChange + 20 € Livret +), code FTN1126, du 02/11 au 20/12/2026 (source : top10banques.com, 03/11/2026).
# Terminal de paiement -> enveloppe + carte -> frise 90 jours -> transfert de banque -> addition -> appel à l'action.
NAME = 'fortuneo7'
TITLE = 'Fortuneo 160 euros anis'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Cent soixante euros pour cinq paiements par carte.", [("160 €", None), ("pour 5 paiements", None), ("par carte.", None)]),
 ("C'est l'offre de bienvenue Fortuneo, avec la carte Gold.", [("C'est l'offre", None), ("de bienvenue Fortuneo,", None), ("avec la carte Gold.", None)]),
 ("Cinq paiements en quatre-vingt-dix jours, et la prime est validée.", [("5 paiements", None), ("en 90 jours,", None), ("et la prime", None), ("est validée.", None)]),
 ("Tu changes de banque avec eux ? Quatre-vingts euros de plus.", [("Tu changes de banque", None), ("avec eux ?", None), ("80 €", None), ("de plus.", None)]),
 ("Et vingt euros avec le Livret plus : jusqu'à deux cent soixante euros.", [("Et 20 €", None), ("avec le Livret +", None), ("jusqu'à", None), ("260 €", None)]),
 ("Envoie-moi FORTUNEO en privé, je t'envoie le lien.", [("Envoie-moi", None), ("FORTUNEO", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 1.946), (2.185, 4.923), (5.551, 8.11), (8.496, 11.04), (11.468, 14.538), (14.985, 17.277)]
GSTART = [[0.1, 1.0, 1.5], [2.25, 2.75, 3.85], [5.61, 6.11, 7.21, 7.61], [8.5, 9.21, 9.91, 10.51], [11.47, 12.01, 13.21, 13.51], [14.99, 15.41, 15.91, 16.61]]
MINLEN = 2.3
GAP = 0.36
TAIL = 2.0
CSS = '''
.an{color:#c3ea6a;text-shadow:0 0 18px rgba(182,224,90,.45)}
.tpe{position:absolute;left:340px;top:760px;width:400px;height:620px;border-radius:50px;background:linear-gradient(170deg,#2a2a26,#121210);border:4px solid #514a40;box-shadow:0 40px 90px rgba(0,0,0,.7)}
.tpe .sc{position:absolute;left:40px;top:44px;width:312px;height:170px;border-radius:16px;background:#14200a;border:3px solid #b6e05a;text-align:center;font:800 30px 'DejaVu Sans Mono',monospace;color:#c3ea6a;padding-top:30px;line-height:1.5}
.tpe .kp{position:absolute;left:52px;top:250px;width:290px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.tpe .kp i{height:56px;border-radius:12px;background:#3a3832}
.dots{position:absolute;left:250px;top:1420px;width:580px;display:flex;justify-content:space-between}
.dots div{width:86px;height:86px;border-radius:50%;border:4px solid #d9a24c;display:flex;align-items:center;justify-content:center;font:900 40px Inter;color:#14200a;background:#b6e05a}
.env{position:absolute;left:170px;top:930px;width:740px;height:420px;background:linear-gradient(170deg,#1c1c1a,#0c0c0b);border:3px solid #d9a24c;border-radius:18px;box-shadow:0 40px 90px rgba(0,0,0,.7)}
.env:before{content:'';position:absolute;left:0;top:0;width:0;height:0;border-left:367px solid transparent;border-right:367px solid transparent;border-top:200px solid #24231f}
.gcard{position:absolute;left:250px;top:700px;width:580px;height:360px;border-radius:30px;background:linear-gradient(135deg,#f6dc8e 0%,#d6a347 40%,#8a5a18 100%);box-shadow:0 30px 70px rgba(0,0,0,.7),0 0 60px rgba(240,180,80,.35);color:#2a1a05;padding:36px 40px;transform:rotate(-4deg)}
.gcard .nm{font:900 36px Inter;letter-spacing:3px}.gcard .chip{width:90px;height:68px;border-radius:12px;background:linear-gradient(135deg,#fff1c4,#b98a3a);margin-top:34px}
.gcard .num{font:700 38px 'DejaVu Sans Mono',monospace;letter-spacing:4px;margin-top:34px}
.datep{position:absolute;left:290px;top:1400px;width:500px;height:84px;border-radius:42px;background:#b6e05a;color:#14200a;text-align:center;font:900 36px Inter;line-height:84px;letter-spacing:2px}
.bar{position:absolute;left:130px;top:880px;width:820px;height:24px;border-radius:12px;background:#24221d;overflow:hidden}
.bar i{position:absolute;left:0;top:0;height:100%;width:100%;background:linear-gradient(90deg,#d9a24c,#b6e05a);transform-origin:0 50%}
.bl{position:absolute;top:930px;font:800 28px Inter;letter-spacing:3px;color:#9a917f}
.chk{position:absolute;top:760px;width:84px;height:84px;border-radius:50%;background:#b6e05a;color:#14200a;font:900 44px Inter;display:flex;align-items:center;justify-content:center;border:4px solid #f3c766}
.valid{position:absolute;left:250px;top:1110px;width:580px;padding:22px 0;border:8px solid #b6e05a;border-radius:24px;text-align:center;color:#c3ea6a;font:900 60px Inter;letter-spacing:4px;transform:rotate(-6deg);background:rgba(20,32,10,.6)}
.bk{position:absolute;top:760px;width:300px;height:300px;border-radius:30px;text-align:center;padding-top:60px}
.bk .i{font:400 100px 'DejaVu Sans';line-height:1}
.bk .n{font:800 28px Inter;letter-spacing:3px;margin-top:30px}
.arr{position:absolute;left:440px;top:860px;width:200px;height:14px;background:linear-gradient(90deg,#d9a24c,#b6e05a);transform-origin:0 50%}
.arr:after{content:'';position:absolute;right:-24px;top:-20px;border-left:34px solid #b6e05a;border-top:27px solid transparent;border-bottom:27px solid transparent}
.add{position:absolute;left:230px;top:640px;width:620px;font:800 50px 'DejaVu Sans Mono',monospace;color:#e9e4da}
.add .r{display:flex;justify-content:space-between;padding:14px 0;white-space:nowrap}
.add .r span:last-child{color:#f3c766}
.add hr{border:0;border-top:5px solid #d9a24c;margin:18px 0}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
KP = '<div class="kp">' + '<i></i>' * 12 + '</div>'
DOTS = '<div class="dots">' + ''.join(f'<div>{k}</div>' for k in range(1, 6)) + '</div>'
CHK = ''.join(f'<div class="chk" style="left:{x}px" data-g="2.{g}" data-fx="pop">✓</div>' for x, g in [(160, 0), (330, 0), (500, 1), (670, 1), (840, 2)])
BODY = hud('FRANCE · CARTE GOLD', "JUSQU'AU 20/12") + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + head(210, [('big gold', '160 €', None), ('h1', 'POUR 5 PAIEMENTS', None), ('it gold', 'par carte.', None)]).replace('class="big gold"', 'class="big gold" style="font-size:180px"') + '''
   <div class="tpe" style="top:740px"><div class="sc">PAIEMENT<br>ACCEPTÉ ✓</div>''' + KP + '''</div>''' + DOTS.replace('top:1420px', 'top:1400px') + '''</div>
  <div class="scene" data-s="1" data-in="up">''' + head(230, [('h1', "L'OFFRE DE BIENVENUE", '1.0'), ('h1 an', 'FORTUNEO', '1.1'), ('it gold', 'avec la carte Gold.', '1.2')]).replace('class="h1"', 'class="h1 s"') + '''
   <div class="env"></div><div class="gcard" data-g="1.2" data-fx="up"><div class="nm">CARTE GOLD</div><div class="chip"></div><div class="num">•••• •••• 2012</div></div>
   <div class="datep" data-g="1.2" data-fx="pop">JUSQU'AU 20/12</div></div>
  <div class="scene" data-s="2" data-in="right">''' + head(230, [('h1', '5 PAIEMENTS', '2.0'), ('it gold', 'en 90 jours,', '2.1')]) + CHK + '''
   <div class="bar"><i data-g="2.0" data-fx="grow"></i></div><div class="bl" style="left:130px">JOUR 1</div><div class="bl an" style="left:800px">JOUR 90</div>
   <div class="valid" data-g="2.3" data-fx="stamp">PRIME VALIDÉE</div></div>
  <div class="scene" data-s="3" data-in="left"><div class="floor"></div>''' + head(230, [('h1', 'TU CHANGES DE BANQUE ?', '3.0'), ('big gold', '+ 80 €', '3.2')]).replace('class="h1"', 'class="h1 s"').replace('class="big gold"', 'class="big gold" style="font-size:150px"') + '''
   <div class="bk" style="left:120px;border:3px solid #514a40;background:rgba(30,28,24,.6)" data-g="3.0" data-fx="left"><div class="i" style="color:#6f6553">⌂</div><div class="n" style="color:#9a917f">ANCIENNE</div></div>
   <div class="arr" data-g="3.1" data-fx="grow"></div>
   <div class="bk" style="left:660px;border:3px solid #b6e05a;background:rgba(20,32,10,.5)" data-g="3.1" data-fx="right"><div class="i an">⌂</div><div class="n an">FORTUNEO</div></div>
   <div class="abs" style="left:0;top:1150px;width:1080px;text-align:center;font:800 32px Inter;letter-spacing:4px;color:#e9e4da" data-g="3.3" data-fx="fade">MOBILITÉ BANCAIRE</div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:860px"></div>''' + head(230, [('h1', '+ 20 € AVEC LE LIVRET +', '4.0')]).replace('class="h1"', 'class="h1 s"') + '''
   <div class="add"><div class="r" data-g="4.0" data-fx="left"><span>Carte Gold</span><span>160 €</span></div><div class="r" data-g="4.0" data-fx="left"><span>Mobilité</span><span>80 €</span></div><div class="r" data-g="4.1" data-fx="left"><span>Livret +</span><span>20 €</span></div><hr></div>
   <div class="abs" style="left:0;top:1060px;width:1080px;text-align:center" data-g="4.2" data-fx="stamp" data-slow="4.3"><div style="font:800 40px Inter;letter-spacing:6px">JUSQU'À</div><div class="gold" style="font:900 190px 'DejaVu Serif',serif;line-height:1.15">260 €</div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', 'ENVOIE-MOI', '5.0'), ('big gold', '« FORTUNEO »', '5.1'), ('it gold', 'en privé.', '5.2')]).replace('class="big gold"', 'class="big gold" style="font-size:112px"') + '''
   <div class="pill" style="top:720px" data-g="5.3" data-fx="up"><div class="pin" style="background:#b6e05a">✉</div><div><b>JE T'ENVOIE LE LIEN</b><span>offre valable jusqu'au 20/12</span></div></div>
   <div class="search" style="top:860px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1000px">Offre soumise aux conditions en vigueur · 1re ouverture de compte<br>jusqu'à 260 € avec la carte Gold (sous conditions de revenus) :<br>160 € après 5 paiements en 90 jours + 80 € mobilité + 20 € Livret +<br>· du 02/11 au 20/12/2026</div></div>
'''
