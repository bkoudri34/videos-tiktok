import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°2 du 12/11/2026 - style v3 nuit & or, accent cerise, « le code en 3 étapes » : ouvrir l'appli -> panier -> code promo Hacoo hzklink au paiement ;
# exemple : un sac cabas 22,00 € -> 18,92 € (-14 %, prix d'exemple).
NAME = 'hacoo19'
TITLE = 'Hacoo 3 etapes cerise'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Le code promo Hacou, en trois étapes.", [("Le code promo Hacoo,", None), ("en 3 étapes.", None)]),
 ("Un : tu ouvres l'appli Hacou.", [("1 :", None), ("tu ouvres l'appli Hacoo.", None)]),
 ("Deux : tu mets ton article dans le panier.", [("2 :", None), ("tu mets ton article", None), ("dans le panier.", None)]),
 ("Trois : au paiement, code promo Hacou H Z K link.", [("3 :", None), ("au paiement,", None), ("code promo Hacoo", None), ("hzklink.", None)]),
 ("Vingt-deux euros deviennent dix-huit euros quatre-vingt-douze.", [("22 €", None), ("deviennent", None), ("18,92 €.", None)]),
 ("Moins quatorze pour cent, et les liens sont dans ma bio.", [("-14 %,", None), ("et les liens", None), ("sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 2.248), (2.638, 4.36), (4.908, 6.727), (7.176, 11.166), (11.56, 13.745), (14.181, 16.434)]
GSTART = [[0.05, 1.4], [2.64, 3.2], [4.91, 5.5, 6.2], [7.18, 7.7, 8.4, 9.6], [11.56, 12.2, 12.5], [14.19, 15.3, 15.8]]
MINLEN = 2.3
GAP = 0.36
TAIL = 2.2
CSS = '''
.ce{color:#ff6a85;text-shadow:0 0 18px rgba(255,77,109,.5)}
.step{position:absolute;width:240px;height:240px;border-radius:50%;border:5px solid #d9a24c;display:flex;align-items:center;justify-content:center;font:900 130px 'DejaVu Serif',serif;background:radial-gradient(circle,#2a0f16,#0b0607)}
.step small{position:absolute;bottom:-56px;left:-60px;right:-60px;text-align:center;font:800 28px Inter;letter-spacing:3px;color:#e9e4da;white-space:nowrap}
.cart{position:absolute;left:300px;top:800px;width:480px;height:330px}
.cart .bx{position:absolute;left:40px;top:60px;width:420px;height:220px;border:10px solid #d9a24c;border-top:0;border-radius:0 0 30px 30px;background:rgba(255,77,109,.12)}
.cart .h{position:absolute;left:-40px;top:40px;width:110px;height:10px;background:#d9a24c;border-radius:5px}
.cart .w{position:absolute;top:290px;width:56px;height:56px;border-radius:50%;background:#d9a24c}
.cnt{position:absolute;left:720px;top:780px;width:90px;height:90px;border-radius:50%;background:#ff4d6d;color:#fff;font:900 50px Inter;display:flex;align-items:center;justify-content:center}
.inp{position:absolute;left:300px;top:1110px;width:320px;height:70px;border-radius:35px;background:#fff;color:#111;display:flex;align-items:center;padding:0 24px;font:900 40px 'DejaVu Sans Mono',monospace;white-space:nowrap}
.pt{position:absolute;left:190px;top:700px;width:700px;height:440px;border-radius:30px;background:#f4efe4;color:#1c1712;text-align:center;box-shadow:0 40px 90px rgba(0,0,0,.7);transform:rotate(-3deg)}
.pt .o{font:800 64px 'DejaVu Serif',serif;color:#8f877a;margin-top:50px;position:relative;display:inline-block}
.pt .ln{position:absolute;left:-10px;right:-10px;top:50%;height:8px;background:#c0392b;transform-origin:0 50%}
.pt .n{font:900 150px 'DejaVu Serif',serif;color:#c8253f;line-height:1.2;white-space:nowrap}
.pt .x{font:700 21px Inter;letter-spacing:2px;color:#7a6f60}
'''
PH = '''<div class="phone" style="top:{top}px;height:{h}px" data-g="{g}" data-fx="up"><div class="notch"></div>{inner}</div>'''
BODY = hud('FRANCE · TUTO', 'CODE HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + head(220, [('h1', 'LE CODE PROMO HACOO,', None), ('it gold', 'en 3 étapes.', None)]) + '''
   <div class="step" style="left:90px;top:760px"><span class="gold">1</span><small>L'APPLI</small></div><div class="step" style="left:420px;top:900px"><span class="gold">2</span><small>LE PANIER</small></div><div class="step" style="left:700px;top:1040px;width:220px;height:220px"><span class="gold">3</span><small class="ce">hzklink</small></div></div>
  <div class="scene" data-s="1" data-in="right">''' + head(230, [('big gold', '1', '1.0'), ('it gold', "tu ouvres l'appli Hacoo.", '1.1')]).replace('class="big gold"', 'class="big gold" style="font-size:150px"').replace('class="it gold"', 'class="it gold" style="font-size:66px"') + '''
   <div class="orb" style="left:200px;top:600px;width:680px;height:960px"></div>''' + PH.format(top=640, h=760, g='1.0', inner='<div style="margin-top:220px;font:900 78px Inter" class="ce">Hacoo</div><div style="font:600 26px Inter;color:#aaa;margin-top:12px">appli de shopping</div><div style="display:inline-block;margin-top:60px;background:#ff4d6d;color:#22060c;font:800 32px Inter;padding:14px 44px;border-radius:30px" data-g="1.1" data-fx="pop">Ouvrir</div>') + '''</div>
  <div class="scene" data-s="2" data-in="pop"><div class="floor"></div>''' + head(230, [('big gold', '2', '2.0'), ('it gold', 'ton article dans le panier.', '2.1')]).replace('class="big gold"', 'class="big gold" style="font-size:150px"').replace('class="it gold"', 'class="it gold" style="font-size:64px"') + '''
   <div class="abs" style="left:440px;top:600px" data-g="2.1" data-fx="up">''' + icon('Tote', 200) + '''</div>
   <div class="cart" data-g="2.0" data-fx="left"><div class="h"></div><div class="bx"></div><div class="w" style="left:100px"></div><div class="w" style="left:340px"></div></div>
   <div class="cnt" data-g="2.2" data-fx="stamp">1</div></div>
  <div class="scene" data-s="3" data-in="left">''' + head(230, [('big gold', '3', '3.0'), ('it gold', 'au paiement :', '3.1')]).replace('class="big gold"', 'class="big gold" style="font-size:150px"') + PH.format(top=600, h=800, g='3.0', inner='<div style="font:900 30px Inter;letter-spacing:4px;margin-top:40px">PAIEMENT</div><div style="margin:40px 26px 0;text-align:left;font:800 24px Inter;letter-spacing:3px" class="ce" data-g="3.2" data-fx="fade">CODE PROMO HACOO</div>') + '''
   <div class="inp" style="left:370px;top:840px;width:340px" data-g="3.2" data-fx="up"><span data-g="3.3" data-fx="type">hzklink</span></div>
   <div class="abs" style="left:370px;top:960px;width:340px;text-align:center;font:900 40px Inter;color:#ff6a85" data-g="3.3" data-fx="pop">-14 % ✓</div></div>
  <div class="scene" data-s="4" data-in="up"><div class="rays" style="top:700px"></div>''' + head(230, [('h1', '22 € DEVIENNENT', '4.0'), ('it gold', '18,92 €.', '4.2')]) + '''
   <div class="pt" data-g="4.0" data-fx="up"><div class="o">22,00 €<div class="ln" data-g="4.1" data-fx="strike"></div></div><div class="n" data-g="4.2" data-fx="stamp" data-slow="4.2">18,92 €</div><div class="x">SAC CABAS · AVEC hzklink · PRIX D'EXEMPLE</div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', 'CODE PROMO HACOO', '5.0'), ('big gold', 'hzklink', '5.0'), ('it gold', "-14 % sur l'appli Hacoo", '5.0')]).replace('class="big gold"', 'class="big gold" style="font-size:150px"').replace('class="it gold"', 'class="it gold" style="font-size:60px"') + '''
   <div class="pill" style="top:730px;border-color:rgba(255,77,109,.85)" data-g="5.1" data-fx="up"><div class="pin" style="background:#ff4d6d">★</div><div><b>LIENS DES ARTICLES TENDANCE</b><span>tout est dans ma bio</span></div></div>
   <div class="cond" style="top:880px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
