import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Vidéos QG, 18/11/2026, vidéo 2 : Fortuneo. Style v3 nuit & or, accent violet améthyste. Format F8 « résultat d'abord » :
# notification « Virement reçu +80,00 € · prime de parrainage » (exemple) + solde 300 € -> 380 € dès la 1re image
# -> champ « code parrain » -> carte Fosfo -> calendrier 6 jours / 300 € -> duel Fosfo 80 € / Gold 150 € (ralenti) -> appel à l'action.
# Offre : fortuneo.fr/parrainage/cartes-bancaires consulté le 18/11/2026 (offre du 01/11 au 30/11/2026).
# Voix : Speko (speechify simba-3.5, voix par défaut, ElevenLabs/voix-htm-luxe refusé : 402 top-up), speed 1.08.
NAME = 'qg_fortuneo1'
TITLE = 'QG Fortuneo resultat d abord'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Parrainage Fortuneo : quatre-vingts euros versés sur ton compte.", [("Parrainage Fortuneo :", None), ("+80 €", None), ("versés sur ton compte.", None)]),
 ("Le secret : le code parrain, au moment de l'inscription.", [("Le secret :", None), ("le code parrain,", None), ("au moment de l'inscription.", None)]),
 ("Tu ouvres ton compte avec la carte Fosfo, sans condition de revenus.", [("Tu ouvres ton compte", None), ("avec la carte Fosfo,", None), ("sans condition de revenus.", None)]),
 ("Et tu verses trois cents euros dans les six jours.", [("Et tu verses 300 €", None), ("dans les 6 jours.", None)]),
 ("Avec la carte Gold, c'est cent cinquante euros, sous conditions de revenus.", [("Avec la carte Gold,", None), ("c'est 150 €,", None), ("sous conditions de revenus.", None)]),
 ("C'est jusqu'au trente novembre. Envoie-moi FORTUNEO en privé.", [("C'est jusqu'au 30 novembre.", None), ("Envoie-moi", None), ("FORTUNEO", None), ("en privé.", None)]),
]
SPLITS = [(0.0, 2.80), (3.11, 5.54), (6.17, 8.90), (9.44, 10.88), (11.42, 14.28), (14.77, 17.35)]
GSTART = [[0.0, 1.26, 1.8], [3.11, 3.86, 4.7], [6.17, 6.8, 8.02], [9.44, 10.4], [11.42, 12.5, 13.47], [14.77, 16.22, 16.5, 16.9]]
MINLEN = 2.0
GAP = 0.42
TAIL = 2.6


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.vi{color:#d3b0ff;text-shadow:0 0 18px rgba(190,140,255,.55)}
.notif{position:absolute;left:90px;top:700px;width:840px;height:200px;border-radius:40px;background:rgba(245,243,250,.96);color:#16141c;display:flex;align-items:center;gap:22px;padding:0 30px;box-shadow:0 30px 90px rgba(0,0,0,.65),0 0 60px rgba(190,140,255,.25)}
.notif .ic{flex:none;width:110px;height:110px;border-radius:28px;background:linear-gradient(135deg,#6d4bb8,#2a1b4a);color:#f3c766;font:900 64px 'DejaVu Serif',serif;display:flex;align-items:center;justify-content:center}
.notif .tx{flex:1;white-space:nowrap}
.notif .tx small{display:block;font:700 26px Inter;color:#6f6a7a;letter-spacing:2px}
.notif .tx b{display:block;font:800 36px Inter;margin-top:6px}
.notif .tx span{font:600 30px Inter;color:#4b4658}
.notif .am{font:900 54px 'DejaVu Serif',serif;color:#1b7a46;white-space:nowrap}
.ex{position:absolute;left:760px;top:676px;padding:6px 16px;border-radius:12px;background:#2a1b4a;color:#d3b0ff;font:800 22px Inter;letter-spacing:3px}
.bal{position:absolute;left:90px;top:960px;width:840px;height:300px;border-radius:30px;background:#14111c;border:3px solid rgba(211,176,255,.45);text-align:center;padding-top:34px}
.bal small{display:block;font:700 28px Inter;color:#9a92aa;letter-spacing:5px}
.bal .r{font:900 104px 'DejaVu Serif',serif;white-space:nowrap;margin-top:16px}
.bal .r s{color:#7d7590;font-size:74px;text-decoration-thickness:6px}
.form{position:absolute;left:150px;top:700px;width:780px;height:560px;border-radius:34px;background:#f5f3fa;color:#16141c;padding:44px 50px;box-shadow:0 30px 90px rgba(0,0,0,.6)}
.form .lb{font:800 28px Inter;letter-spacing:4px;color:#6f6a7a;margin:18px 0 12px}
.form .fl{height:96px;border-radius:20px;border:4px solid #d6d1e0;font:700 40px 'DejaVu Sans Mono';display:flex;align-items:center;padding:0 28px;color:#b3adbf;white-space:nowrap}
.form .fl.on{border-color:#7a52d1;color:#16141c;background:#efe8ff}
.ok{position:absolute;left:770px;top:1040px;width:110px;height:110px;border-radius:50%;background:#1fa463;color:#fff;font:900 70px Inter;display:flex;align-items:center;justify-content:center;box-shadow:0 0 40px rgba(31,164,99,.6)}
.cardx{position:absolute;width:560px;height:350px;border-radius:34px;box-shadow:0 30px 90px rgba(0,0,0,.65)}
.cardx i{position:absolute;left:50px;top:110px;width:100px;height:76px;border-radius:14px;background:linear-gradient(135deg,#f6d27a,#c8892c)}
.cardx span{position:absolute;left:50px;bottom:44px;font:600 36px 'DejaVu Sans Mono';letter-spacing:4px;color:rgba(255,255,255,.85)}
.cardx em{position:absolute;right:44px;top:40px;font:900 italic 44px 'Liberation Serif',serif;color:#fff}
.lbl2{position:absolute;left:0;width:1080px;text-align:center;font:800 40px Inter;color:#e9e4da;white-space:nowrap}
.cal{position:absolute;width:380px;height:400px;border-radius:30px;background:#f4f2ee;color:#1a1814;overflow:hidden;text-align:center;box-shadow:0 30px 80px rgba(0,0,0,.6)}
.cal .top{height:100px;background:#b48cf0;color:#1a0f30;font:900 40px Inter;display:flex;align-items:center;justify-content:center;letter-spacing:3px}
.cal .d{font:900 170px 'DejaVu Serif',serif;line-height:1.3}
.cal small{display:block;font:700 30px Inter;color:#6b665e;margin-top:-10px}
.bill{position:absolute;width:400px;height:200px;border-radius:18px;background:linear-gradient(135deg,#b48cf0,#efe2ff 55%,#b48cf0);border:6px solid #6d4bb8;color:#1a0f30;text-align:center;font:900 100px 'DejaVu Serif',serif;line-height:188px;box-shadow:0 30px 80px rgba(0,0,0,.6)}
.duel{position:absolute;top:700px;width:420px;height:560px;border-radius:30px;text-align:center;padding-top:40px}
.duel small{display:block;font:800 30px Inter;letter-spacing:4px}
.duel .v{font:900 130px 'DejaVu Serif',serif;margin-top:40px;white-space:nowrap}
.duel p{font:600 28px Inter;color:#cfc8dc;margin-top:30px;line-height:1.35}
.vs{position:absolute;left:490px;top:930px;width:100px;height:100px;border-radius:50%;background:#07060a;border:4px solid #d9a24c;font:900 38px Inter;color:#f3c766;display:flex;align-items:center;justify-content:center}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'

NOTIF = '''<div class="notif"><div class="ic">€</div><div class="tx"><small>BANQUE · MAINTENANT</small><b>Virement reçu</b><span>Prime de parrainage</span></div><div class="am">+80,00 €</div></div><div class="ex">EXEMPLE</div>'''

BODY = hud('FRANCE · FORTUNEO', 'RÉSULTAT') + '''
  <div class="scene" data-s="0">''' + hd(215, [('h1', 'PARRAINAGE FORTUNEO', None, 'font-size:66px'), ('big gold', '+80 €', None, 'font-size:170px'), ('it vi', 'versés sur ton compte', None, 'font-size:66px')]) + NOTIF + '''
   <div class="bal"><small>SOLDE</small><div class="r"><s>300 €</s> <span class="gold">→ 380 €</span></div></div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1', 'LE SECRET :', '1.0', ''), ('it vi', 'le code parrain', '1.1', ''), ('it gold', "au moment de l'inscription", '1.2', 'font-size:58px')]) + '''
   <div class="form" data-g="1.0" data-fx="fade"><div class="lb">NOM</div><div class="fl">••••••••</div><div class="lb">CODE PARRAIN</div><div class="fl on" data-g="1.1" data-fx="type">CODE-REÇU-EN-PRIVÉ</div><div class="lb">OUVERTURE</div><div class="fl">compte + carte</div></div>
   <div class="ok" data-g="1.2" data-fx="stamp">✓</div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1', 'TU OUVRES TON COMPTE', '2.0', 'font-size:64px'), ('it vi', 'avec la carte Fosfo', '2.1', ''), ('it gold', 'sans condition de revenus', '2.2', 'font-size:58px')]) + '''
   <div class="cardx" style="left:260px;top:760px;background:linear-gradient(135deg,#3a2a5c,#16101f);border:3px solid #b48cf0;transform:rotate(-5deg)" data-g="2.1" data-fx="pop"><em>Fosfo</em><i></i><span>•••• 2026</span></div>
   <div class="lbl2" style="top:1190px" data-g="2.2" data-fx="up">filleul : 80 € · aucune condition de revenus</div></div>
  <div class="scene" data-s="3" data-in="right">''' + hd(230, [('h1', 'ET TU VERSES 300 €', '3.0', 'font-size:66px'), ('it vi', 'dans les 6 jours', '3.1', '')]) + '''
   <div class="bill" style="left:110px;top:800px;transform:rotate(-6deg)" data-g="3.0" data-fx="left">300 €</div>
   <div class="cal" style="left:590px;top:740px" data-g="3.1" data-fx="pop"><div class="top">DÉLAI</div><div class="d">6</div><small>jours après l'ouverture</small></div></div>
  <div class="scene" data-s="4" data-in="pop">''' + hd(230, [('h1', 'AVEC LA CARTE GOLD', '4.0', 'font-size:66px'), ('it gold', "c'est 150 €", '4.1', ''), ('it vi', 'sous conditions de revenus', '4.2', 'font-size:58px')]) + '''
   <div class="duel" style="left:70px;background:#16101f;border:3px solid #b48cf0" data-g="4.0" data-fx="left"><small style="color:#d3b0ff">FOSFO</small><div class="v vi">80 €</div><p>sans condition<br>de revenus</p></div>
   <div class="duel" style="left:590px;background:#1c160b;border:3px solid #e0ac55" data-g="4.1" data-fx="stamp" data-slow="4.1"><small style="color:#f3c766">GOLD</small><div class="v gold">150 €</div><p>dès 2 200 € nets<br>par mois</p></div>
   <div class="vs" data-g="4.0" data-fx="pop">VS</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(215, [('h1 vi', "JUSQU'AU 30 NOVEMBRE", '5.0', 'font-size:58px'), ('h1', 'ENVOIE-MOI', '5.1', ''), ('big gold', '« FORTUNEO »', '5.2', 'font-size:104px'), ('it gold', 'en privé', '5.3', '')]) + '''
   <div class="pill" style="top:800px;border-color:rgba(180,140,240,.85)" data-g="5.3" data-fx="up"><div class="pin" style="background:#b48cf0;color:#1a0f30">✉</div><div><b>JE T'ENVOIE MON CODE</b><span>80 € Fosfo · 150 € Gold · avant le 30/11</span></div></div>
   <div class="search" style="top:940px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1080px;left:70px;width:940px;font-size:24px">Offre soumise aux conditions en vigueur · offre Fortuneo du 01/11 au 30/11/2026<br>1re ouverture de compte avec code parrain + 300 € versés sous 6 jours<br>80 € avec Fosfo CB Mastercard · 150 € avec Gold CB Mastercard<br>(dès 2 200 € nets/mois) · prime versée au plus tard le 31/12/2026<br>compte et carte à garder 1 an · notification et solde : exemple</div></div>
'''
