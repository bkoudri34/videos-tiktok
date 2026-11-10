import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°1 du 10/11/2026 - style v3 nuit & or, accent émeraude, « le total baisse en direct » : 4 articles 40,00 € -> 34,40 € avec hzklink (-14 %, prix d'exemple).
NAME = 'hacoo14'
TITLE = 'Hacoo total en direct emeraude'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Regarde ce total baisser en direct.", [("Regarde ce total", None), ("baisser en direct.", None)]),
 ("Quatre petits articles Hacou : quarante euros pile.", [("Quatre petits articles", None), ("Hacoo :", None), ("40 € pile.", None)]),
 ("Au paiement, tu tapes le code H Z K link.", [("Au paiement,", None), ("tu tapes le code", None), ("hzklink.", None)]),
 ("Et hop : trente-quatre euros quarante.", [("Et hop :", None), ("34,40 €.", None)]),
 ("Cinq euros soixante de gagnés, sans toucher au panier.", [("5,60 € de gagnés,", None), ("sans toucher au panier.", None)]),
 ("Moins quatorze pour cent avec le code. Les liens sont dans ma bio.", [("-14 % avec le code.", None), ("Les liens", None), ("sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 2.057), (2.439, 5.119), (5.47, 8.053), (8.399, 10.055), (10.455, 12.9), (13.246, 16.129)]
GSTART = [[0.1, 1.1], [2.44, 3.7, 4.2], [5.47, 6.1, 6.9], [8.4, 9.02], [10.46, 12.0], [13.25, 15.15, 15.5]]
MINLEN = 2.4
GAP = 0.4
TAIL = 2.0
JS = JS + '''
function extra(t){const el=document.getElementById('cd');if(!el)return;const t0=GT(3,1);const k=eo((t-t0)/1.1);const v=40-5.6*k;el.textContent=v.toFixed(2).replace('.',',')+' €';}
'''
CSS = '''
.em{color:#3fd6a0;text-shadow:0 0 18px rgba(63,214,160,.45)}
.tot{position:absolute;left:190px;top:720px;width:700px;height:400px;border-radius:34px;background:linear-gradient(160deg,#10372b,#06140f);border:4px solid #3fd6a0;text-align:center;box-shadow:0 40px 90px rgba(0,0,0,.7),0 0 60px rgba(63,214,160,.2)}
.tot .k{font:900 38px Inter;letter-spacing:8px;color:#bfeedd;margin-top:56px}
.tot .v{font:900 150px 'DejaVu Serif',serif;line-height:1.35}
.tot .s{font:700 24px Inter;letter-spacing:3px;color:#7fbfa8}
.cart{position:absolute;left:150px;top:560px;width:780px;overflow:hidden;border-radius:30px;background:#f4efe4;color:#1c1712;padding:20px 34px 26px;box-shadow:0 40px 90px rgba(0,0,0,.7)}
.cart .r{display:flex;align-items:center;gap:22px;height:132px;border-bottom:2px dashed #cfc5b3;font:700 34px Inter;white-space:nowrap}
.cart .r b{margin-left:auto;font:900 38px 'DejaVu Sans Mono',monospace}
.cart .ic{flex:none;width:110px;height:110px;border-radius:22px;background:#17241f;display:flex;align-items:center;justify-content:center}
.cart .f{display:flex;justify-content:space-between;font:900 40px Inter;margin-top:20px}
.cart .x{font:600 22px Inter;letter-spacing:3px;color:#7a6f60;text-align:center;margin-top:10px}
.mini4{position:absolute;top:1060px;width:150px;height:150px;border-radius:28px;background:#14261f;border:3px solid #3fd6a0;display:flex;align-items:center;justify-content:center}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
ITEMS = [('Mug', 'Mug isotherme', '12,90'), ('Chaussettes', 'Chaussettes douces', '7,50'), ('Bougie', 'Bougie parfumée', '9,90'), ('Coque', 'Coque de téléphone', '9,70')]
ROWS = ''.join(f'<div class="r" data-g="1.{min(k, 2)}" data-fx="left"><div class="ic">{icon(i, 96)}</div><span>{n}</span><b>{p}</b></div>' for k, (i, n, p) in enumerate(ITEMS))
BODY = hud('FRANCE · SHOPPING', 'EN DIRECT') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + head(240, [('h1', 'REGARDE CE TOTAL', None), ('it gold', 'baisser en direct.', None)]) + '''
   <div class="tot"><div class="k">TOTAL PANIER</div><div class="v gold">40,00 €</div><div class="s">PRIX D'EXEMPLE · SANS CODE</div></div>
   <div class="abs em" style="left:470px;top:1160px;font:900 120px Inter">↓</div></div>
  <div class="scene" data-s="1" data-in="pop">''' + head(230, [('h1', '4 PETITS ARTICLES', '1.0'), ('it gold', '40 € pile.', '1.2')]) + '''
   <div class="cart">''' + ROWS + '''<div class="f" data-g="1.2" data-fx="fade"><span>TOTAL</span><span>40,00 €</span></div><div class="x">PRIX D'EXEMPLE</div></div></div>
  <div class="scene" data-s="2" data-in="right">''' + head(230, [('h1', 'AU PAIEMENT,', '2.0'), ('it gold', 'tu tapes le code', '2.1')]) + '''
   <div class="search" style="top:720px;height:120px;border:5px solid #3fd6a0" data-g="2.0" data-fx="up">''' + SEARCH + '''<span style="font:600 32px Inter;color:#888">Code promo</span><span data-g="2.2" data-fx="type" style="font:900 52px Inter;color:#0f7a5a">hzklink</span></div>
   <div class="abs" style="left:390px;top:900px;background:#3fd6a0;color:#06261a;font:800 40px Inter;padding:20px 50px;border-radius:40px" data-g="2.2" data-fx="pop">Appliquer</div>
   <div class="abs" style="left:190px;top:1080px;width:700px;text-align:center;font:700 30px Inter;letter-spacing:3px;color:#bba98a" data-g="2.2" data-fx="fade">TOTAL ACTUEL : 40,00 €</div></div>
  <div class="scene" data-s="3" data-in="pop"><div class="rays" style="top:560px"></div>''' + head(230, [('h1', 'ET HOP :', '3.0')]) + '''
   <div class="abs" style="left:90px;top:400px;width:900px;text-align:center;font:900 70px 'DejaVu Serif',serif;color:#8f877a" data-g="3.0" data-fx="fade">40,00 €</div>
   <div class="abs" style="left:385px;top:445px;width:310px;height:10px;background:#3fd6a0;border-radius:5px;transform-origin:0 50%" data-g="3.1" data-fx="strike"></div>
   <div class="abs" style="left:60px;top:590px;width:960px;text-align:center" data-g="3.1" data-fx="stamp" data-slow="3.1"><div id="cd" class="gold" style="font:900 160px 'DejaVu Serif',serif;line-height:1.3;white-space:nowrap">40,00 €</div><div style="font:700 28px Inter;letter-spacing:5px;color:#bfeedd">AVEC HZKLINK · PRIX D'EXEMPLE</div></div></div>
  <div class="scene" data-s="4" data-in="left"><div class="floor"></div>''' + head(230, [('h1', '5,60 € DE GAGNÉS,', '4.0'), ('it gold', 'sans toucher au panier.', '4.1')]).replace('class="it gold"', 'class="it gold" style="font-size:66px"') + '''
   <div class="abs" style="left:300px;top:640px;padding:22px 44px;border-radius:50px;background:#10372b;border:4px solid #3fd6a0;font:900 72px Inter;white-space:nowrap" data-g="4.0" data-fx="stamp"><span class="em">− 5,60 €</span></div>
   <div class="abs" style="left:150px;top:860px;width:780px;text-align:center;font:700 30px Inter;letter-spacing:3px;color:#e9e4da" data-g="4.1" data-fx="fade">LES MÊMES 4 ARTICLES</div>
   <div class="mini4" style="left:150px" data-g="4.1" data-fx="pop">''' + icon('Mug', 120) + '''</div><div class="mini4" style="left:360px" data-g="4.1" data-fx="pop">''' + icon('Chaussettes', 120) + '''</div><div class="mini4" style="left:570px" data-g="4.1" data-fx="pop">''' + icon('Bougie', 120) + '''</div><div class="mini4" style="left:780px" data-g="4.1" data-fx="pop">''' + icon('Coque', 120) + '''</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', '-14 % AVEC LE CODE', '5.0'), ('big gold', 'hzklink', '5.0'), ('it gold', 'liens dans ma bio.', '5.1')]).replace('class="big gold"', 'class="big gold" style="font-size:140px"') + '''
   <div class="pill" style="top:760px" data-g="5.1" data-fx="up"><div class="pin">%</div><div><b>-14 % AVEC HZKLINK</b><span>sur ton panier Hacoo</span></div></div>
   <div class="pill" style="top:900px;border-color:rgba(63,214,160,.8)" data-g="5.2" data-fx="up"><div class="pin" style="background:#3fd6a0">★</div><div><b class="em">ARTICLES TENDANCE</b><span>tous les liens sont en bio</span></div></div>
   <div class="cond" style="top:1060px">Prix d'exemple · -14 % avec le code hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
