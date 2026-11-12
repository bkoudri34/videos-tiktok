import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Hello bank, 12/11/2026 16:00 - style v3 nuit & or, accent bleu azur. Offre de bienvenue jusqu'à 330 € = 80 € à l'ouverture (Hello One ou Hello Prime)
# + 200 € en bon d'achat (Hello Start+, mobilité bancaire) + 50 € au bout de 12 mois (Hello Prime), demande validée au plus tard le 08/12/2026
# (source : moneyvox.fr, 05/11/2026). Porte qui s'ouvre -> carte « bienvenue » -> téléphone solde -> sac + étiquette -> 12 mois -> appel à l'action.
NAME = 'hellobank8'
TITLE = 'Hello bank 330 euros azur'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Trois cent trente euros, juste pour ouvrir un compte.", [("330 €", None), ("juste pour ouvrir", None), ("un compte.", None)]),
 ("Oui, c'est l'offre de bienvenue de Hello bank.", [("Oui,", None), ("c'est l'offre de bienvenue", None), ("de Hello bank.", None)]),
 ("Quatre-vingts euros dès l'ouverture, avec Hello One ou Hello Prime.", [("80 €", None), ("dès l'ouverture,", None), ("avec Hello One", None), ("ou Hello Prime.", None)]),
 ("Deux cents euros en bon d'achat, si tu passes par Hello Start plus.", [("200 €", None), ("en bon d'achat,", None), ("si tu passes", None), ("par Hello Start +.", None)]),
 ("Et cinquante euros au bout d'un an, avec Hello Prime.", [("Et 50 €", None), ("au bout d'un an,", None), ("avec Hello Prime.", None)]),
 ("Envoie-moi HELLO en privé, je t'explique tout.", [("Envoie-moi", None), ("HELLO", None), ("en privé,", None), ("je t'explique tout.", None)]),
]
SPLITS = [(0.0, 2.229), (2.498, 4.357), (4.82, 8.109), (8.402, 11.736), (12.118, 14.62), (15.006, 17.203)]
GSTART = [[0.1, 1.1, 1.9], [2.5, 2.68, 3.78], [4.82, 5.51, 6.31, 7.31], [8.41, 9.11, 9.81, 10.31], [12.12, 12.91, 13.71], [15.01, 15.51, 15.71, 16.41]]
MINLEN = 2.3
GAP = 0.36
TAIL = 2.0
CSS = '''
.az{color:#6cb4ff;text-shadow:0 0 18px rgba(108,180,255,.45)}
.door{position:absolute;left:330px;top:760px;width:420px;height:640px;border:12px solid #d9a24c;border-bottom:0;border-radius:10px 10px 0 0;background:radial-gradient(70% 60% at 50% 55%,#fff3cf,#f3c766 45%,#8a5a18 100%);box-shadow:0 0 90px rgba(245,190,90,.55)}
.leaf{position:absolute;left:342px;top:772px;width:396px;height:628px;background:linear-gradient(90deg,#1a2a44,#0e1828);border-right:6px solid #6cb4ff;transform-origin:0 50%;transform:perspective(900px) rotateY(-58deg)}
.leaf i{position:absolute;right:30px;top:320px;width:20px;height:20px;border-radius:50%;background:#f3c766}
.wcard{position:absolute;left:170px;top:720px;width:740px;height:470px;border-radius:30px;background:#f4efe4;color:#151a22;text-align:center;box-shadow:0 40px 90px rgba(0,0,0,.7);transform:rotate(-3deg);padding-top:50px;overflow:hidden}
.wcard .k{font:800 30px Inter;letter-spacing:8px;color:#5b6b80}
.wcard .t{font:700 italic 92px 'Liberation Serif',serif;color:#14243b;margin-top:16px}
.wcard .d{display:inline-block;margin-top:34px;padding:12px 30px;border-radius:30px;background:#14243b;color:#9fd0ff;font:800 30px Inter;letter-spacing:2px}
.wcard:after{content:'';position:absolute;left:0;right:0;bottom:0;height:22px;background:repeating-linear-gradient(90deg,#6cb4ff 0 40px,#d9a24c 40px 80px)}
.bal{font:900 96px 'DejaVu Serif',serif;margin-top:60px}
.ln{display:flex;justify-content:space-between;margin:0 30px;padding:18px 4px;border-bottom:2px solid #26221c;font:600 28px Inter;color:#ddd;white-space:nowrap}
.ln b{color:#6cb4ff}
.bag{position:absolute;left:150px;top:820px;width:440px;height:460px;border-radius:20px 20px 40px 40px;background:linear-gradient(160deg,#1d3354,#0b1424);border:4px solid #6cb4ff;box-shadow:0 40px 90px rgba(0,0,0,.7)}
.bag:before{content:'';position:absolute;left:110px;top:-110px;width:200px;height:150px;border:14px solid #d9a24c;border-bottom:0;border-radius:100px 100px 0 0}
.bag .bt{position:absolute;left:0;top:120px;width:100%;text-align:center;font:800 34px Inter;letter-spacing:6px;color:#9fd0ff}
.tag{position:absolute;left:520px;top:960px;width:420px;white-space:nowrap;height:190px;border-radius:20px 60px 60px 20px;background:linear-gradient(135deg,#fff1c4,#e9b456 50%,#a8701f);color:#2a1a05;text-align:center;transform:rotate(14deg);box-shadow:0 20px 50px rgba(0,0,0,.6)}
.tag:before{content:'';position:absolute;right:34px;top:78px;width:30px;height:30px;border-radius:50%;background:#07060a}
.tag .a{font:900 84px 'DejaVu Serif',serif;line-height:1;margin-top:26px;margin-right:50px}
.tag .s{font:800 22px Inter;letter-spacing:3px;margin-right:50px}
.months{position:absolute;left:150px;top:760px;width:780px;display:grid;grid-template-columns:repeat(6,1fr);gap:18px}
.months div{height:120px;border-radius:16px;border:3px solid #d9a24c;display:flex;align-items:center;justify-content:center;font:800 34px Inter;color:#e9e4da;background:rgba(108,180,255,.18)}
.months div.l{background:#6cb4ff;color:#07101e;border-color:#6cb4ff}
.plus{position:absolute;left:0;top:1080px;width:1080px;text-align:center}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
MONTHS = ''.join(f'<div{" class=\"l\"" if k == 12 else ""} data-g="4.{0 if k < 7 else 1}" data-fx="pop">{k}</div>' for k in range(1, 13))
BODY = hud('FRANCE · BANQUE EN LIGNE', 'BIENVENUE') + '''
  <div class="scene" data-s="0"><div class="floor"></div><div class="rays" style="top:780px"></div>''' + head(220, [('big gold', '330 €', None), ('h1', 'JUSTE POUR OUVRIR', None), ('it gold', 'un compte.', None)]).replace('class="big gold"', 'class="big gold" style="font-size:190px"') + '''
   <div class="door"></div><div class="leaf"><i></i></div></div>
  <div class="scene" data-s="1" data-in="right">''' + head(230, [('h1', 'OUI :', '1.0'), ('it gold', "l'offre de bienvenue", '1.1'), ('h1 s az" style="margin-top:18px', 'DE HELLO BANK', '1.2')]) + '''
   <div class="wcard" style="top:760px" data-g="1.1" data-fx="up"><div class="k">NOUVEAU CLIENT</div><div class="t">Bienvenue</div><div class="d" data-g="1.2" data-fx="pop">OUVERTURE AVANT LE 08/12</div></div></div>
  <div class="scene" data-s="2" data-in="pop">''' + head(230, [('big gold', '80 €', '2.0'), ('it gold', "dès l'ouverture,", '2.1')]).replace('class="big gold"', 'class="big gold" style="font-size:150px"') + '''
   <div class="orb" style="left:200px;top:620px;width:680px;height:960px"></div>
   <div class="phone" style="top:660px;height:780px"><div class="notch"></div><div style="font:800 28px Inter;letter-spacing:4px;color:#9fd0ff;margin-top:44px">MON COMPTE</div>
    <div class="bal gold" data-g="2.0" data-fx="tick" data-count="80" data-suf=" €"><span class="v">80 €</span></div>
    <div style="margin-top:40px"><div class="ln" data-g="2.2" data-fx="left"><span>Hello One</span><b>✓</b></div><div class="ln" data-g="2.3" data-fx="left"><span>ou Hello Prime</span><b>✓</b></div></div></div></div>
  <div class="scene" data-s="3" data-in="left"><div class="floor"></div>''' + head(230, [('h1', "200 € EN BON D'ACHAT", '3.1'), ('it gold', 'avec Hello Start +', '3.3')]).replace('class="h1"', 'class="h1 s"') + '''
   <div class="bag" data-g="3.0" data-fx="up"><div class="bt">SHOPPING</div></div>
   <div class="tag" data-g="3.0" data-fx="stamp"><div class="a">200 €</div><div class="s">BON D'ACHAT</div></div>
   <div class="abs az" style="left:0;top:1330px;width:1080px;text-align:center;font:800 32px Inter;letter-spacing:4px" data-g="3.2" data-fx="fade">SI TU CHANGES DE BANQUE</div></div>
  <div class="scene" data-s="4" data-in="up">''' + head(230, [('h1', '+ 50 € AU BOUT D\'UN AN', '4.0'), ('it gold', 'avec Hello Prime.', '4.2')]).replace('class="h1"', 'class="h1 s"') + '''
   <div class="months">''' + MONTHS + '''</div>
   <div class="plus" data-g="4.2" data-fx="stamp" data-slow="4.2"><div style="font:800 36px Inter;letter-spacing:6px;color:#e9e4da">TOTAL : JUSQU'À</div><div class="gold" style="font:900 160px 'DejaVu Serif',serif;line-height:1.2">330 €</div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', 'ENVOIE-MOI', '5.0'), ('big gold', '« HELLO »', '5.1'), ('it gold', 'en privé.', '5.2')]).replace('class="big gold"', 'class="big gold" style="font-size:130px"') + '''
   <div class="pill" style="top:720px" data-g="5.3" data-fx="up"><div class="pin" style="background:#6cb4ff">✉</div><div><b>JE T'EXPLIQUE TOUT</b><span>et je t'envoie le lien</span></div></div>
   <div class="search" style="top:860px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1000px">Offre soumise aux conditions en vigueur · jusqu'à 330 €<br>= 80 € à l'ouverture (Hello One ou Hello Prime) + 200 € en bon<br>d'achat (Hello Start+) + 50 € au bout de 12 mois (Hello Prime)<br>· demande d'ouverture validée au plus tard le 08/12/2026</div></div>
'''
