import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Fortuneo, 11/11/2026 16:00 - style v3 nuit & or, accent rubis. Offre de bienvenue jusqu'à 260 € (carte Gold : 160 € après 5 paiements en 90 jours
# + 80 € mobilité neoChange + 20 € Livret +), code FTN1126, du 02/11 au 20/12/2026 (sources : top10banques.com 03/11/2026, moneyvox.fr).
# Balance -> frise de l'offre -> carte tamponnée -> 5 paiements sur le téléphone -> colonnes -> appel à l'action.
NAME = 'fortuneo6'
TITLE = 'Fortuneo 260 euros rubis'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Un compte qui te rapporte deux cent soixante euros ?", [("Un compte qui", None), ("te rapporte", None), ("260 € ?", None)]),
 ("C'est l'offre de bienvenue Fortuneo, valable jusqu'au vingt décembre.", [("C'est l'offre de bienvenue", None), ("Fortuneo,", None), ("valable jusqu'au 20 décembre.", None)]),
 ("Le gros morceau : cent soixante euros avec la carte Gold.", [("Le gros morceau :", None), ("160 €", None), ("avec la carte Gold.", None)]),
 ("Cinq paiements en quatre-vingt-dix jours, et c'est validé.", [("5 paiements", None), ("en 90 jours,", None), ("et c'est validé.", None)]),
 ("Plus quatre-vingts euros si tu changes de banque, et vingt avec le Livret plus.", [("+ 80 €", None), ("si tu changes de banque,", None), ("et 20 avec le Livret +.", None)]),
 ("Envoie-moi FORTUNEO en privé, je t'envoie le lien.", [("Envoie-moi", None), ("FORTUNEO", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 2.623), (2.817, 5.940), (6.273, 9.090), (9.490, 11.972), (12.435, 15.846), (16.314, 18.80)]
GSTART = [[0.1, 0.8, 1.3], [2.82, 3.8, 4.5], [6.28, 7.2, 8.0], [9.5, 10.2, 11.36], [12.44, 13.3, 14.5], [16.32, 16.8, 17.4, 18.0]]
MINLEN = 2.4
GAP = 0.36
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.rb{color:#ff5a76;text-shadow:0 0 18px rgba(255,90,118,.45)}
.beam{position:absolute;left:150px;top:1010px;width:780px;height:16px;border-radius:8px;background:linear-gradient(90deg,#f3c766,#a8701f);transform:rotate(9deg);transform-origin:50% 50%}
.post{position:absolute;left:530px;top:1010px;width:20px;height:420px;background:linear-gradient(#f3c766,#7a5016)}
.base{position:absolute;left:400px;top:1420px;width:280px;height:30px;border-radius:15px;background:#c8892c}
.plate{position:absolute;width:300px;height:40px;border-radius:0 0 150px 150px;background:linear-gradient(#e9b456,#7a5016);text-align:center}
.plate .lb{position:absolute;left:-40px;width:380px;top:56px;font:800 30px Inter;letter-spacing:3px;color:#e9e4da;white-space:nowrap}
.tl{position:absolute;left:130px;top:960px;width:820px;height:10px;border-radius:5px;background:linear-gradient(90deg,#d9a24c,#ff5a76);transform-origin:0 50%}
.tdot{position:absolute;width:44px;height:44px;border-radius:50%;border:6px solid #d9a24c;background:#07060a}
.tlab{position:absolute;width:300px;text-align:center;font:800 34px Inter;letter-spacing:2px;white-space:nowrap}
.tlab small{display:block;font:600 24px Inter;color:#9a917f;letter-spacing:3px;margin-top:6px}
.card{position:absolute;left:190px;top:820px;width:700px;height:440px;border-radius:36px;background:linear-gradient(135deg,#f6dc8e 0%,#d6a347 40%,#8a5a18 100%);box-shadow:0 40px 90px rgba(0,0,0,.7),0 0 60px rgba(240,180,80,.35);color:#2a1a05;padding:44px 50px;transform:rotate(-5deg)}
.card .chip{width:100px;height:76px;border-radius:14px;background:linear-gradient(135deg,#fff1c4,#b98a3a);margin-top:40px}
.card .num{font:700 44px 'DejaVu Sans Mono',monospace;letter-spacing:4px;margin-top:40px}
.card .nm{font:900 40px Inter;letter-spacing:3px}
.stmp{position:absolute;left:400px;top:1150px;padding:10px 34px;border:8px solid #ff5a76;border-radius:22px;color:#ff5a76;font:900 110px 'DejaVu Serif',serif;transform:rotate(-12deg);background:rgba(20,4,8,.55);white-space:nowrap}
.prow{display:flex;justify-content:space-between;align-items:center;margin:0 26px;padding:16px 6px;border-bottom:2px solid #26221c;font:600 31px Inter;color:#ddd;white-space:nowrap}
.prow b{color:#ff5a76;font:900 32px Inter}
.ok{position:absolute;left:380px;top:1290px;width:320px;padding:14px 0;text-align:center;border-radius:40px;background:#ff5a76;color:#1d0509;font:900 44px Inter;letter-spacing:4px}
.cols{position:absolute;left:170px;top:760px;width:740px;height:560px;border-bottom:4px solid #d9a24c}
.col{position:absolute;bottom:0;width:190px;border-radius:18px 18px 0 0;transform-origin:50% 100%;text-align:center;font:900 46px 'DejaVu Serif',serif;color:#1a1408;padding-top:18px}
.cl{position:absolute;top:1340px;width:260px;text-align:center;font:800 26px Inter;letter-spacing:2px;color:#e9e4da;white-space:nowrap}
'''
COINS = ''.join(f'<div class="coin" style="left:{x}px;top:{y}px;width:220px;height:66px"></div>' for x, y in [(670, 1050), (670, 1005), (670, 960), (670, 915)])
PAYS = ''.join(f'<div class="prow" data-g="3.{g}" data-fx="left"><span>Paiement carte n°{k}</span><b>✓</b></div>' for k, g in [(1, 0), (2, 0), (3, 1), (4, 1), (5, 2)])
BODY = hud('FRANCE · BANQUE EN LIGNE', 'BIENVENUE') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('h1', 'UN COMPTE QUI', None, ''), ('it gold', 'te rapporte', None, 'font-size:72px'), ('big gold', '260 € ?', None, 'font-size:180px')]) + '''
   <div class="post"></div><div class="base"></div><div class="beam"></div>
   <div class="plate" style="left:150px;top:985px"><div class="lb">AUTRE COMPTE · 0 €</div></div>
   <div class="plate" style="left:630px;top:1105px"><div class="lb rb">+ 260 €</div></div>''' + COINS + '''</div>
  <div class="scene" data-s="1" data-in="right">''' + hd(230, [('h1 s', "C'EST L'OFFRE DE BIENVENUE", '1.0', 'font-size:56px'), ('h1', 'FORTUNEO,', '1.1', ''), ('it gold', "valable jusqu'au 20 décembre.", '1.2', 'font-size:60px')]) + '''
   <div class="tl" data-g="1.0" data-fx="grow"></div>
   <div class="tdot" style="left:118px;top:943px"></div><div class="tlab" style="left:-10px;top:1020px">02/11<small>DÉBUT</small></div>
   <div class="tdot" style="left:410px;top:943px;border-color:#fff" data-g="1.1" data-fx="pop"></div><div class="tlab" style="left:282px;top:1020px" data-g="1.1" data-fx="up">11/11<small>AUJOURD'HUI</small></div>
   <div class="tdot" style="left:910px;top:943px;border-color:#ff5a76" data-g="1.2" data-fx="pop"></div><div class="tlab rb" style="left:640px;top:1020px" data-g="1.2" data-fx="up">20/12<small>FIN DE L'OFFRE</small></div>
   <div class="abs gold" style="left:0;top:1180px;width:1080px;text-align:center;font:700 italic 60px 'Liberation Serif',serif" data-g="1.2" data-fx="fade">encore quelques semaines</div></div>
  <div class="scene" data-s="2" data-in="pop"><div class="rays" style="top:700px;left:290px"></div>''' + hd(230, [('h1', 'LE GROS MORCEAU :', '2.0', 'font-size:70px'), ('it gold', 'avec la carte Gold.', '2.2', '')]) + '''
   <div class="card" data-g="2.0" data-fx="up"><div class="nm">CARTE GOLD</div><div class="chip"></div><div class="num">•••• •••• •••• 1126</div></div>
   <div class="stmp" data-g="2.1" data-fx="stamp" data-slow="2.1">160 €</div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('h1', '5 PAIEMENTS', '3.0', ''), ('it gold', "en 90 jours, et c'est validé.", '3.1', 'font-size:62px')]) + '''
   <div class="orb" style="left:200px;top:560px;width:680px;height:1000px"></div>
   <div class="phone" style="top:520px;height:820px"><div class="notch"></div><div style="font:900 34px Inter;margin:30px 0 18px;letter-spacing:3px">MES PAIEMENTS</div>''' + PAYS + '''</div>
   <div class="ok" data-g="3.2" data-fx="stamp">VALIDÉ ✓</div></div>
  <div class="scene" data-s="4" data-in="up"><div class="floor"></div>''' + hd(230, [('h1', '+ 80 € MOBILITÉ', '4.0', ''), ('it gold', '+ 20 € avec le Livret +', '4.2', 'font-size:66px')]) + '''
   <div class="cols"><div class="col" style="left:20px;height:480px;background:linear-gradient(#fff1c4,#c8892c)">160</div>
    <div class="col" style="left:275px;height:240px;background:linear-gradient(#ffb3c0,#ff5a76)" data-g="4.0" data-fx="up">80</div>
    <div class="col" style="left:530px;height:100px;background:linear-gradient(#ffe2a8,#d9a24c);font-size:40px" data-g="4.2" data-fx="up">20</div></div>
   <div class="cl" style="left:150px">CARTE GOLD</div><div class="cl" style="left:405px" data-g="4.1" data-fx="fade">MOBILITÉ</div><div class="cl" style="left:660px" data-g="4.2" data-fx="fade">LIVRET +</div>
   <div class="abs gold" style="left:640px;top:820px;font:900 70px 'DejaVu Serif',serif;white-space:nowrap" data-g="4.2" data-fx="pop">= 260 €</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« FORTUNEO »', '5.1', 'font-size:112px'), ('it gold', 'en privé.', '5.2', '')]) + '''
   <div class="pill" style="top:700px" data-g="5.2" data-fx="up"><div class="pin" style="background:#ff5a76">€</div><div><b>JUSQU'À 260 €</b><span>offre de bienvenue · jusqu'au 20/12</span></div></div>
   <div class="pill" style="top:825px" data-g="5.3" data-fx="up"><div class="pin">✉</div><div><b>JE T'ENVOIE LE LIEN</b><span>en privé sur @htm.invest</span></div></div>
   <div class="cond" style="top:980px">Offre soumise aux conditions en vigueur<br>Fortuneo : 1re ouverture de compte, carte Gold (sous conditions<br>de revenus), montant maximum · jusqu'au 20/12/2026</div></div>
'''
