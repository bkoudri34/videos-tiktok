import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# 3 banques, 09/11/2026 21:00 - style v3 nuit & or, accent rouge. Fortuneo jusqu'à 260 € (carte Gold, jusqu'au 20/12) + BoursoBank jusqu'à 180 € (offre de bienvenue)
# + Hello bank selon l'offre en cours (offre parrainage 330 € terminée le 09/11 à 15h, nouvelle offre non vérifiable) => « plus de 400 € » en cumulé.
NAME = 'trio6'
TITLE = '3 banques nuit et or'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Trois banques, plus de quatre cents euros à récupérer.", [("Trois banques,", None), ("plus de 400 €", None), ("à récupérer.", None)]),
 ("Fortuneo : jusqu'à deux cent soixante euros avec la carte Gold.", [("Fortuneo :", None), ("jusqu'à 260 €", None), ("avec la carte Gold.", None)]),
 ("BoursoBank : jusqu'à cent quatre-vingts euros en offre de bienvenue.", [("BoursoBank :", None), ("jusqu'à 180 €", None), ("en offre de bienvenue.", None)]),
 ("Et Hello bank : regarde l'offre en cours, elle change souvent.", [("Et Hello bank :", None), ("regarde l'offre en cours,", None), ("elle change souvent.", None)]),
 ("Tu additionnes, ça dépasse les quatre cents euros.", [("Tu additionnes,", None), ("ça dépasse", None), ("les 400 €.", None)]),
 ("Envoie-moi PARRAINAGE en privé, je t'envoie les liens.", [("Envoie-moi", None), ("PARRAINAGE", None), ("en privé,", None), ("je t'envoie les liens.", None)]),
]
SPLITS = [(0.0, 2.567), (2.923, 6.392), (6.713, 10.339), (10.771, 13.902), (14.263, 16.312), (16.769, 19.59)]
GSTART = [[0.1, 0.8, 2.0], [2.93, 3.8, 5.2], [6.72, 7.7, 9.3], [10.78, 11.8, 13.1], [14.27, 15.1, 15.7], [16.78, 17.3, 18.1, 18.8]]
MINLEN = 2.6
GAP = 0.38
TAIL = 2.0
CSS = '''
.bar{position:absolute;bottom:0;width:200px;border-radius:16px 16px 0 0;background:linear-gradient(180deg,#f3c766,#8a5a18);box-shadow:0 0 40px rgba(240,180,80,.3)}
.bar.r{background:linear-gradient(180deg,#ff7a6b,#7a1d18);box-shadow:0 0 40px rgba(224,72,72,.35)}
.bars{position:absolute;left:150px;top:860px;width:780px;height:420px;border-bottom:4px solid #d9a24c}
.bl{position:absolute;top:1300px;width:260px;text-align:center;font:800 26px Inter;letter-spacing:2px;color:#e9e4da}
.tag{position:absolute;left:250px;top:780px;width:580px;height:420px;border-radius:30px 30px 30px 30px;background:#f4efe4;color:#1c1712;text-align:center;box-shadow:0 40px 90px rgba(0,0,0,.7);transform-origin:50% -80px}
.tag:before{content:'';position:absolute;left:265px;top:26px;width:50px;height:50px;border-radius:50%;background:#0b0907;border:6px solid #d9a24c}
.tag .n{font:900 46px Inter;letter-spacing:4px;margin-top:100px}
.tag .a{font:900 130px 'DejaVu Serif',serif;color:#b0302a;line-height:1.15}
.tag .c{font:700 28px Inter;letter-spacing:3px;color:#6b5f4f}
.str{position:absolute;left:538px;top:620px;width:4px;height:190px;background:#d9a24c}
'''
BODY = hud('FRANCE · 3 BANQUES', 'BONS PLANS') + '''
  <div class="scene" data-s="0">''' + head(230, [('h1', '3 BANQUES', None), ('big gold', '+ de 400 €', None), ('it gold', 'à récupérer.', '0.2')]).replace('class="big gold"', 'class="big gold" style="font-size:128px"') + '''
   <div class="bars"><div class="bar" style="left:20px;height:380px"></div><div class="bar r" style="left:290px;height:270px"></div><div class="bar" style="left:560px;height:200px;opacity:.55;border:3px dashed #f3c766;background:none"></div></div>
   <div class="bl" style="left:120px">FORTUNEO</div><div class="bl" style="left:390px">BOURSOBANK</div><div class="bl" style="left:660px">HELLO BANK</div></div>
  <div class="scene" data-s="1" data-in="pop"><div class="rays" style="top:700px"></div>''' + head(230, [('h1', 'FORTUNEO :', '1.0'), ('it gold', "jusqu'à 260 €", '1.1')]) + '''
   <div class="str" data-g="1.0" data-fx="fade"></div>
   <div class="tag" data-g="1.0" data-fx="up"><div class="n">FORTUNEO</div><div class="a" data-g="1.1" data-fx="pop">260 €</div><div class="c" data-g="1.2" data-fx="fade">MAX · CARTE GOLD</div></div></div>
  <div class="scene" data-s="2" data-in="right"><div class="floor"></div>''' + head(230, [('h1', 'BOURSOBANK :', '2.0'), ('it gold', "jusqu'à 180 €", '2.1')]) + '''
   <div class="str" data-g="2.0" data-fx="fade"></div>
   <div class="tag" style="transform:rotate(-3deg)" data-g="2.0" data-fx="up"><div class="n">BOURSOBANK</div><div class="a" data-g="2.1" data-fx="pop">180 €</div><div class="c" data-g="2.2" data-fx="fade">MAX · OFFRE DE BIENVENUE</div></div></div>
  <div class="scene" data-s="3" data-in="left">''' + head(230, [('h1', 'ET HELLO BANK :', '3.0'), ('it gold', "l'offre en cours", '3.1')]) + '''
   <div class="search" style="top:720px" data-g="3.0" data-fx="fade"><svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg><span data-g="3.0" data-fx="type">offre Hello bank</span></div>
   <div class="pill" style="top:880px" data-g="3.1" data-fx="up"><div class="pin">?</div><div><b>MONTANT</b><span>selon l'offre en cours</span></div></div>
   <div class="pill" style="top:1005px;border-color:rgba(224,72,72,.8)" data-g="3.2" data-fx="up"><div class="pin" style="background:#e04848;color:#fff">↻</div><div><b style="color:#ff8a7d">ÇA CHANGE SOUVENT</b><span>je te dis ce qui est dispo</span></div></div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="floor"></div><div class="rays" style="top:560px"></div>''' + head(230, [('h1', 'TU ADDITIONNES…', '4.0'), ('it gold', 'ça dépasse', '4.1')]) + '''
   <div class="abs" style="left:60px;top:560px;width:960px;text-align:center" data-g="4.2" data-fx="stamp" data-slow="4.2"><div class="gold" style="font:900 108px 'DejaVu Serif',serif;line-height:1.4">+ de 400 €</div><div style="font:700 30px Inter;letter-spacing:5px;color:#bba98a">260 + 180 + HELLO BANK</div></div>
   <div class="coin" style="left:150px;top:1120px" data-g="4.1" data-fx="pop"></div><div class="coin" style="left:150px;top:1010px" data-g="4.1" data-fx="pop"></div>
   <div class="coin" style="left:610px;top:1120px" data-g="4.2" data-fx="pop"></div><div class="coin" style="left:610px;top:1010px" data-g="4.2" data-fx="pop"></div><div class="coin" style="left:610px;top:900px" data-g="4.2" data-fx="pop"></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', 'ENVOIE-MOI', '5.0'), ('big gold', '« PARRAINAGE »', '5.1'), ('it gold', 'en privé.', '5.2')]).replace('class="big gold"', 'class="big gold" style="font-size:96px"') + '''
   <div class="pill" style="top:700px" data-g="5.2" data-fx="up"><div class="pin">✉</div><div><b>LES 3 LIENS</b><span>je te les envoie en privé</span></div></div>
   <div class="search" style="top:840px" data-g="5.3" data-fx="fade"><svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg><span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:990px">Offres soumises aux conditions en vigueur · montants maximum<br>Fortuneo : jusqu'à 260 € (carte Gold, jusqu'au 20/12/2026)<br>BoursoBank : jusqu'à 180 € (offre de bienvenue)<br>Hello bank : selon l'offre en cours</div></div>
'''
