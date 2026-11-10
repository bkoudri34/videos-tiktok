import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Hello bank, 10/11/2026 18:00 - style v3 nuit & or, accent turquoise. Parrainage : filleul jusqu'à 330 € d'avantages = 80 € ouverture + 200 € bon d'achat
# (mobilité bancaire, Hello Start+) + 50 € au 13e mois (Hello Prime), invitation avant le 30/11/2026 15h (source : hellobank.fr/fr/votre-offre-parrainage, lu le 10/11/2026).
# Table -> notification -> bon d'achat -> ticket total -> chrono -> appel à l'action.
NAME = 'hellobank7'
TITLE = 'Hello bank 330 euros turquoise'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Hello bank remet jusqu'à trois cent trente euros sur la table.", [("Hello bank remet", None), ("jusqu'à 330 €", None), ("sur la table.", None)]),
 ("Quatre-vingts euros à l'ouverture de ton compte, avec une invitation.", [("80 €", None), ("à l'ouverture de ton compte,", None), ("avec une invitation.", None)]),
 ("Deux cents euros en bon d'achat, si tu changes de banque.", [("200 €", None), ("en bon d'achat,", None), ("si tu changes de banque.", None)]),
 ("Et cinquante euros de plus au treizième mois, avec Hello Prime.", [("Et 50 € de plus", None), ("au 13e mois,", None), ("avec Hello Prime.", None)]),
 ("Attention, c'est jusqu'au trente novembre.", [("Attention,", None), ("c'est jusqu'au", None), ("30 novembre.", None)]),
 ("Envoie-moi HELLO en privé, je t'envoie l'invitation.", [("Envoie-moi", None), ("HELLO", None), ("en privé,", None), ("je t'envoie l'invitation.", None)]),
]
SPLITS = [(0.0, 3.074), (3.469, 6.349), (6.563, 9.046), (9.364, 12.027), (12.358, 14.225), (14.753, 17.106)]
GSTART = [[0.1, 1.2, 2.4], [3.47, 4.1, 5.3], [6.57, 7.2, 8.1], [9.37, 10.1, 11.2], [12.36, 13.2, 13.6], [14.76, 15.2, 15.5, 16.2]]
MINLEN = 2.5
GAP = 0.4
TAIL = 2.0
TICKS = ''.join(f'<div class="tk" style="transform:rotate({k*6}deg);height:{30 if k%5==0 else 16}px"></div>' for k in range(60))
CSS = '''
.tq{color:#4fd8e8;text-shadow:0 0 18px rgba(79,216,232,.45)}
.ntf{position:absolute;left:150px;width:780px;height:130px;border-radius:30px;background:rgba(245,240,230,.96);color:#141210;display:flex;align-items:center;gap:22px;padding:0 26px;box-shadow:0 20px 50px rgba(0,0,0,.55);white-space:nowrap}
.ntf .ic{flex:none;width:74px;height:74px;border-radius:18px;background:#0d3a40;color:#4fd8e8;font:900 36px Inter;display:flex;align-items:center;justify-content:center}
.ntf b{display:block;font:800 31px Inter}.ntf span{font:500 25px Inter;color:#555}
.ntf .amt{margin-left:auto;font:900 44px 'DejaVu Serif',serif;color:#0f7f8c}
.stack{position:absolute;width:200px}
.stack .coin{position:absolute;left:0;width:200px;height:62px}
.voucher{position:absolute;left:170px;top:700px;width:740px;height:420px;border-radius:28px;background:linear-gradient(135deg,#0f3d44,#06181b);border:4px solid #4fd8e8;box-shadow:0 40px 90px rgba(0,0,0,.7),0 0 50px rgba(79,216,232,.25);text-align:center;overflow:hidden}
.voucher:before,.voucher:after{content:'';position:absolute;top:180px;width:60px;height:60px;border-radius:50%;background:#0b0907}
.voucher:before{left:-34px}.voucher:after{right:-34px}
.voucher .k{font:900 40px Inter;letter-spacing:8px;margin-top:56px;color:#e9e4da}
.voucher .a{font:900 150px 'DejaVu Serif',serif;line-height:1.3}
.voucher .c{font:700 26px Inter;letter-spacing:3px;color:#9fdbe3}
.dial .ct{position:absolute;left:0;top:318px;width:592px;text-align:center}
.dial .nd{top:150px;height:150px;transform-origin:2px 150px}
.dial .tk{background:#4fd8e8}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
def stack(x, n, g=None):
    a = f' data-g="{g}" data-fx="up"' if g else ''
    return f'<div class="stack" style="left:{x}px;top:{1170 - 44 * n}px;height:{44 * n + 62}px"{a}>' + ''.join(f'<div class="coin" style="top:{44 * k}px"></div>' for k in range(n)) + '</div>'
BODY = hud('FRANCE · PARRAINAGE', "JUSQU'AU 30/11") + '''
  <div class="scene" data-s="0"><div class="wall"></div><div class="lamp" style="left:160px;top:960px"></div><div class="lamp" style="left:900px;top:960px"></div>''' + head(230, [('h1', 'HELLO BANK REMET', None), ('h1 s', "JUSQU'À", None), ('big gold', '330 €', None), ('it gold', 'sur la table.', None)]).replace('class="big gold"', 'class="big gold" style="font-size:180px"') + '''
   <div class="counter"></div>''' + stack(200, 3) + stack(440, 6) + stack(680, 2) + '''
   <div class="abs" style="left:250px;top:1260px;width:580px;text-align:center;font:800 26px Inter;letter-spacing:4px;color:#9fdbe3">80 € · 200 € · 50 €</div></div>
  <div class="scene" data-s="1" data-in="pop"><div class="floor"></div>''' + head(230, [('big gold', '80 €', '1.0'), ('it gold', "à l'ouverture du compte,", '1.1')]).replace('class="big gold"', 'class="big gold" style="font-size:170px"').replace('class="it gold"', 'class="it gold" style="font-size:62px"') + '''
   <div class="ntf" style="top:700px" data-g="1.1" data-fx="up"><div class="ic">€</div><div><b>Prime de bienvenue</b><span>Hello bank · filleul</span></div><div class="amt">+80 €</div></div>
   <div class="pill" style="top:880px;border-color:rgba(79,216,232,.8)" data-g="1.2" data-fx="up"><div class="pin" style="background:#4fd8e8">✉</div><div><b class="tq">AVEC UNE INVITATION</b><span>envoyée depuis l'appli du parrain</span></div></div></div>
  <div class="scene" data-s="2" data-in="right"><div class="rays" style="top:660px"></div>''' + head(230, [('h1', "200 € EN BON D'ACHAT", '2.0'), ('it gold', 'si tu changes de banque.', '2.2')]).replace('class="h1"', 'class="h1 s"').replace('class="it gold"', 'class="it gold" style="font-size:66px"') + '''
   <div class="voucher" data-g="2.0" data-fx="up"><div class="k">BON D'ACHAT</div><div class="a gold" data-g="2.1" data-fx="pop">200 €</div><div class="c" data-g="2.2" data-fx="fade">MOBILITÉ BANCAIRE · HELLO START+</div></div></div>
  <div class="scene" data-s="3" data-in="left">''' + head(230, [('h1', '+ 50 € AU 13E MOIS', '3.0'), ('it gold', 'avec Hello Prime.', '3.2')]) + '''
   <div class="rcpt" style="top:560px;transform:rotate(3deg)"><div class="t">AVANTAGES FILLEUL</div><div class="s">parrainage Hello bank</div><hr>
    <div class="row" data-g="3.0" data-fx="left"><span>Ouverture</span><span>80 €</span></div><div class="row" data-g="3.0" data-fx="left"><span>Bon d'achat</span><span>200 €</span></div><div class="row" data-g="3.1" data-fx="left"><span>13e mois</span><span>50 €</span></div><hr>
    <div class="row tot" data-g="3.2" data-fx="stamp" data-slow="3.2"><span>JUSQU'À</span><span style="color:#0f7f8c">330 €</span></div></div></div>
  <div class="scene" data-s="4" data-in="pop">''' + head(230, [('h1', 'ATTENTION :', '4.0'), ('it gold', "jusqu'au 30 novembre.", '4.1')]) + '''
   <div class="dial" style="top:600px">''' + TICKS + '''<div class="nd" data-g="4.0" data-fx="sweep"></div>
    <div class="ct"><div class="gold" style="font:900 104px 'DejaVu Serif',serif;line-height:1.3" data-g="4.2" data-fx="stamp">30/11</div><div class="tq" style="font:800 34px Inter;letter-spacing:6px">AVANT 15H</div></div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', 'ENVOIE-MOI', '5.0'), ('big gold', '« HELLO »', '5.1'), ('it gold', 'en privé.', '5.2')]).replace('class="big gold"', 'class="big gold" style="font-size:130px"') + '''
   <div class="pill" style="top:720px" data-g="5.3" data-fx="up"><div class="pin">✉</div><div><b>L'INVITATION</b><span>je te l'envoie depuis l'appli</span></div></div>
   <div class="search" style="top:860px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1000px">Offre soumise aux conditions en vigueur · avantages filleul<br>jusqu'à 330 € = 80 € à l'ouverture + 200 € en bon d'achat<br>(mobilité bancaire, Hello Start+) + 50 € au 13e mois<br>(Hello Prime) · invitation avant le 30/11/2026 à 15h</div></div>
'''
