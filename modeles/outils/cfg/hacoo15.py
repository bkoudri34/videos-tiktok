import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°2 du 10/11/2026 - style v3 nuit & or, accent framboise, « le colis » : gourde 8,90 + chaussons 11,50 + guirlande 4,60 = 25,00 € -> 21,50 € avec hzklink (-14 %, prix d'exemple).
NAME = 'hacoo15'
TITLE = 'Hacoo colis framboise'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Ton prochain colis, quatorze pour cent moins cher.", [("Ton prochain colis,", None), ("14 % moins cher.", None)]),
 ("Dedans : une gourde, des chaussons et une guirlande.", [("Dedans :", None), ("une gourde, des chaussons", None), ("et une guirlande.", None)]),
 ("Sans code, le total fait vingt-cinq euros.", [("Sans code,", None), ("le total fait", None), ("25 €.", None)]),
 ("Avec H Z K link, il passe à vingt et un euros cinquante.", [("Avec", None), ("hzklink,", None), ("il passe à 21,50 €.", None)]),
 ("Moins quatorze pour cent, sur tout le colis.", [("-14 %,", None), ("sur tout le colis.", None)]),
 ("Les liens des articles tendance sont dans ma bio.", [("Les liens", None), ("des articles tendance", None), ("sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 2.302), (2.649, 5.611), (5.973, 8.311), (8.692, 12.253), (12.781, 14.733), (15.334, 17.74)]
GSTART = [[0.1, 1.0], [2.65, 3.4, 4.9], [5.98, 6.8, 7.5], [8.7, 9.1, 10.73], [12.79, 14.07], [15.34, 15.9, 17.1]]
MINLEN = 2.4
GAP = 0.4
TAIL = 2.0
CSS = '''
.fr{color:#ff5fa5;text-shadow:0 0 18px rgba(255,79,154,.45)}
.box{position:absolute;left:270px;top:820px;width:540px;height:400px;border-radius:14px;background:linear-gradient(180deg,#3b2b1c,#1c140c);border:4px solid #d9a24c;box-shadow:0 40px 90px rgba(0,0,0,.7),0 0 50px rgba(240,180,80,.18)}
.box:before{content:'';position:absolute;left:236px;top:0;width:60px;height:100%;background:rgba(217,162,76,.55)}
.flap{position:absolute;top:780px;width:270px;height:60px;background:#2c2015;border:4px solid #d9a24c;border-radius:10px}
.stk{position:absolute;padding:14px 26px;border-radius:16px;background:#ff4f9a;color:#fff;font:900 46px Inter;white-space:nowrap;box-shadow:0 10px 30px rgba(255,79,154,.4)}
.it3{position:absolute;width:190px;height:190px;border-radius:30px;background:#1f1218;border:3px solid #ff4f9a;display:flex;align-items:center;justify-content:center}
.ship{position:absolute;left:190px;top:600px;width:700px;background:#f4efe4;color:#1c1712;border-radius:18px;padding:36px 44px 40px;box-shadow:0 40px 90px rgba(0,0,0,.7);transform:rotate(-2deg)}
.ship .t{font:900 36px Inter;letter-spacing:6px}
.ship .bc{height:60px;margin:18px 0;background:repeating-linear-gradient(90deg,#1c1712 0 4px,transparent 4px 9px,#1c1712 9px 15px,transparent 15px 19px)}
.ship .row{display:flex;justify-content:space-between;font:600 32px 'DejaVu Sans Mono',monospace;line-height:1.7;white-space:nowrap}
.ship hr{border:0;border-top:3px dashed #b9ae9c;margin:14px 0}
.ship .tot{font-weight:700;font-size:38px}
.ship .x{font:600 22px Inter;letter-spacing:3px;color:#7a6f60;text-align:center;margin-top:8px}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
SHIP = '''<div class="t">COLIS · HACOO</div><div class="bc"></div>
    <div class="row"><span>Gourde</span><span>8,90</span></div><div class="row"><span>Chaussons</span><span>11,50</span></div><div class="row"><span>Guirlande</span><span>4,60</span></div><hr>'''
BODY = hud('FRANCE · LIVRAISON', 'COLIS') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + head(240, [('h1', 'TON PROCHAIN COLIS,', None), ('it gold', '14 % moins cher.', None)]).replace('class="h1"', 'class="h1 s"').replace('class="it gold"', 'class="it gold" style="font-size:96px"') + '''
   <div class="box"></div>
   <div class="stk" style="left:600px;top:760px;transform:rotate(8deg)">-14 %</div></div>
  <div class="scene" data-s="1" data-in="pop"><div class="rays" style="top:520px"></div>''' + head(230, [('h1', 'DEDANS :', '1.0'), ('it gold', 'gourde, chaussons, guirlande.', '1.1')]).replace('class="it gold"', 'class="it gold" style="font-size:58px"') + '''
   <div class="box" style="top:1020px;height:300px"></div><div class="flap" style="left:250px;top:990px;transform:rotate(-14deg)"></div><div class="flap" style="left:560px;top:990px;transform:rotate(14deg)"></div>
   <div class="it3" style="left:150px;top:560px" data-g="1.1" data-fx="up">''' + icon('Gourde', 150) + '''</div>
   <div class="it3" style="left:445px;top:500px" data-g="1.1" data-fx="up">''' + icon('Chaussons', 150) + '''</div>
   <div class="it3" style="left:740px;top:560px" data-g="1.2" data-fx="up">''' + icon('Guirlande', 150) + '''</div>
   <div class="abs" style="left:150px;top:780px;width:190px;text-align:center;font:800 30px Inter;line-height:1.3" data-g="1.1" data-fx="fade">Gourde<br><span class="fr">8,90 €</span></div>
   <div class="abs" style="left:445px;top:720px;width:190px;text-align:center;font:800 30px Inter;line-height:1.3" data-g="1.1" data-fx="fade">Chaussons<br><span class="fr">11,50 €</span></div>
   <div class="abs" style="left:740px;top:780px;width:190px;text-align:center;font:800 30px Inter;line-height:1.3" data-g="1.2" data-fx="fade">Guirlande<br><span class="fr">4,60 €</span></div>
   <div class="abs" style="left:240px;top:1360px;width:600px;text-align:center;font:700 24px Inter;letter-spacing:4px;color:#bba98a">PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="2" data-in="right">''' + head(230, [('h1', 'SANS CODE,', '2.0'), ('it gold', 'le total fait 25 €.', '2.1')]) + '''
   <div class="ship" data-g="2.0" data-fx="up">''' + SHIP + '''<div class="row tot" data-g="2.2" data-fx="stamp"><span>TOTAL</span><span>25,00 €</span></div><div class="x">PRIX D'EXEMPLE · SANS CODE</div></div></div>
  <div class="scene" data-s="3" data-in="left">''' + head(230, [('h1', 'AVEC HZKLINK,', '3.0'), ('it gold', 'il passe à 21,50 €.', '3.2')]) + '''
   <div class="ship" style="transform:rotate(2deg)">''' + SHIP + '''<div class="row tot"><span>TOTAL</span><span style="color:#8f877a;text-decoration:line-through">25,00 €</span></div><div class="row tot" data-g="3.2" data-fx="stamp" data-slow="3.2" style="font-size:52px;color:#d6246f"><span>AVEC CODE</span><span>21,50 €</span></div><div class="x">PRIX D'EXEMPLE</div></div>
   <div class="stk" style="left:560px;top:560px;transform:rotate(-6deg);font-size:40px" data-g="3.1" data-fx="stamp">CODE hzklink</div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="floor"></div><div class="rays"></div><div class="emb" data-g="4.0" data-fx="pop"><span class="gold" style="font:900 82px 'DejaVu Serif',serif">-14%</span></div>
   ''' + head(720, [('big gold', '-14 %', '4.0'), ('h1 s', 'SUR TOUT LE COLIS', '4.1')]).replace('class="big gold"', 'class="big gold" style="font-size:160px"') + '''
   <div class="box" style="left:390px;top:1060px;width:300px;height:200px" data-g="4.1" data-fx="up"></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', 'LES LIENS', '5.0'), ('it gold', 'des articles tendance', '5.1'), ('h1', 'DANS MA BIO', '5.2')]).replace('class="it gold"', 'class="it gold" style="font-size:64px"') + '''
   <div class="pill" style="top:620px;border-color:rgba(255,79,154,.85)" data-g="5.1" data-fx="up"><div class="pin" style="background:#ff4f9a;color:#fff">%</div><div><b class="fr">-14 % AVEC HZKLINK</b><span>sur tout ton panier Hacoo</span></div></div>
   <div class="search" style="top:770px" data-g="5.1" data-fx="fade">''' + SEARCH + '''<span data-g="5.1" data-fx="type">hzklink</span></div>
   <div class="pill" style="top:910px" data-g="5.2" data-fx="up"><div class="pin">★</div><div><b>ARTICLES TENDANCE</b><span>tous les liens sont en bio</span></div></div>
   <div class="cond" style="top:1070px">Prix d'exemple · -14 % avec le code hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
