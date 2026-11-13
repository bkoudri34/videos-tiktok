import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°1 du 13/11/2026 - style v3 nuit & or, accent menthe, « le panier qui fond » : bonnet + gants + plaid = 40,00 €
# -> on tape le code promo Hacoo hzklink -> 34,40 € (-14 %, prix d'exemple). Voix : Speko (speechify, voix par défaut).
NAME = 'hacoo20'
TITLE = 'Hacoo panier qui fond menthe'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Ton panier Hacou va fondre. Regarde.", [("Ton panier Hacoo", None), ("va fondre.", None), ("Regarde.", None)]),
 ("Un bonnet, des gants et un plaid tout doux.", [("Un bonnet,", None), ("des gants", None), ("et un plaid tout doux.", None)]),
 ("Quarante euros pile, en prix d'exemple.", [("40 € pile,", None), ("en prix d'exemple.", None)]),
 ("Tu tapes le code promo Hacou : H Z K link.", [("Tu tapes le code promo Hacoo :", None), ("hzklink.", None)]),
 ("Et hop, trente-quatre euros quarante.", [("Et hop,", None), ("34,40 €.", None)]),
 ("Code promo Hacou H Z K link, les liens sont dans ma bio.", [("Code promo Hacoo hzklink,", None), ("les liens sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 1.85), (2.36, 3.95), (4.54, 5.87), (6.29, 8.33), (8.76, 10.09), (10.54, 12.90)]
GSTART = [[0.05, 0.7, 1.5], [2.36, 2.9, 3.3], [4.54, 5.3], [6.29, 7.6], [8.76, 9.0], [10.54, 12.2]]
MINLEN = 2.2
GAP = 0.34
TAIL = 2.2
CSS = '''
.mt{color:#5fe0a8;text-shadow:0 0 18px rgba(95,224,168,.5)}
.cart{position:absolute;left:250px;top:780px}
.drip{position:absolute;width:26px;border-radius:0 0 13px 13px;background:#5fe0a8}
.ic{position:absolute;left:130px;width:200px;height:200px;border-radius:30px;background:#0f1d18;border:3px solid #5fe0a8;display:flex;align-items:center;justify-content:center}
.et{position:absolute;left:520px;padding:12px 26px;border-radius:14px;background:#f2f6f3;color:#10201a;font:800 34px Inter;white-space:nowrap}
.et b{display:block;font:900 44px 'DejaVu Serif',serif;color:#1f8a5e}
.bill{position:absolute;left:190px;top:720px;width:700px;border-radius:30px;background:#f2f6f3;color:#10201a;padding:36px 50px 40px;box-shadow:0 40px 90px rgba(0,0,0,.7)}
.bill .k{font:800 26px 'DejaVu Sans Mono',monospace;letter-spacing:6px;color:#1f8a5e;text-align:center}
.bill .r{display:flex;justify-content:space-between;font:700 34px Inter;padding:14px 0;border-bottom:2px dashed rgba(16,32,26,.25);white-space:nowrap}
.bill .t{display:flex;justify-content:space-between;align-items:center;margin-top:18px;font:900 40px Inter;white-space:nowrap}
.bill .t b{font:900 76px 'DejaVu Serif',serif;color:#10201a}
.bill .x{font:700 22px Inter;letter-spacing:4px;color:#6d7b75;text-align:center;margin-top:14px}
.inl{position:absolute;left:190px;top:700px;font:800 28px Inter;letter-spacing:5px;color:#5fe0a8}
.inp{position:absolute;left:150px;top:750px;width:780px;height:120px;border-radius:60px;background:#fff;color:#111;display:flex;align-items:center;padding:0 40px;font:900 64px 'DejaVu Sans Mono',monospace;white-space:nowrap;border:5px solid #5fe0a8}
.mini{position:absolute;left:290px;top:960px;width:500px;height:300px;border-radius:30px;border:4px solid #5fe0a8;background:rgba(14,40,30,.7);text-align:center;padding-top:40px}
.mini .k{font:800 28px Inter;letter-spacing:6px;color:#e9e4da}
.mini .o{font:900 100px 'DejaVu Serif',serif;position:relative;display:inline-block;margin-top:10px}
.mini .ln{position:absolute;left:-10px;right:-10px;top:50%;height:8px;background:#e74c3c;transform-origin:0 50%}
.big2{position:absolute;left:0;top:1000px;width:1080px;text-align:center}
'''
ITEMS = [('Bonnet', '8,90 €', 560, 0), ('Gants', '6,10 €', 810, 1), ('Plaid', '25,00 €', 1060, 2)]
SC1 = ''.join(f'<div class="ic" style="top:{y}px" data-g="1.{g}" data-fx="up">' + icon(n, 170) + f'</div><div class="ldr" style="left:340px;top:{y + 100}px;width:170px" data-g="1.{g}" data-fx="grow"></div><div class="et" style="top:{y + 50}px" data-g="1.{g}" data-fx="left">{n}<b>{p}</b></div>' for n, p, y, g in ITEMS)
CART = '''<svg class="cart" width="580" height="460" viewBox="0 0 580 460"><path d="M20 40 L110 40 L170 320 L500 320 L550 120 L140 120" fill="none" stroke="#e0ac55" stroke-width="18" stroke-linejoin="round" stroke-linecap="round"/>
 <circle cx="200" cy="400" r="34" fill="#e0ac55"/><circle cx="460" cy="400" r="34" fill="#e0ac55"/><rect x="170" y="150" width="340" height="140" rx="20" fill="#5fe0a8" opacity=".85"/></svg>'''
BODY = hud('FRANCE · PANIER HACOO', 'HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + head(220, [('h1', 'TON PANIER HACOO', None), ('it gold', 'va fondre.', None), ('h1 mt s', 'REGARDE.', None)]).replace('class="it gold"', 'class="it gold" style="font-size:96px"') + CART + '''
   <div class="drip" style="left:470px;top:1070px;height:70px"></div><div class="drip" style="left:560px;top:1070px;height:110px"></div><div class="drip" style="left:660px;top:1070px;height:50px"></div>
   <div class="abs" style="left:0;top:1300px;width:1080px;text-align:center;font:900 72px 'DejaVu Serif',serif;color:#f3c766">40,00 € → ?</div></div>
  <div class="scene" data-s="1" data-in="right">''' + head(230, [('h1', 'UN BONNET,', '1.0'), ('it gold', 'des gants et un plaid tout doux.', '1.1')]).replace('class="it gold"', 'class="it gold" style="font-size:58px"') + SC1 + '''</div>
  <div class="scene" data-s="2" data-in="pop">''' + head(230, [('h1', '40 € PILE,', '2.0'), ('it gold', "en prix d'exemple.", '2.1')]) + '''
   <div class="bill" data-g="2.0" data-fx="up"><div class="k">MON PANIER HACOO</div><div class="r"><span>Bonnet</span><span>8,90 €</span></div><div class="r"><span>Gants</span><span>6,10 €</span></div><div class="r"><span>Plaid</span><span>25,00 €</span></div>
    <div class="t"><span>TOTAL</span><b>40,00 €</b></div><div class="x" data-g="2.1" data-fx="fade">PRIX D'EXEMPLE</div></div></div>
  <div class="scene" data-s="3" data-in="left">''' + head(230, [('h1 s', 'TU TAPES LE CODE PROMO HACOO :', '3.0'), ('big gold', 'hzklink', '3.1')]).replace('class="h1 s"', 'class="h1 s" style="font-size:50px"').replace('class="big gold"', 'class="big gold" style="font-size:140px"') + '''
   <div class="inl" data-g="3.0" data-fx="fade">CODE PROMO HACOO</div>
   <div class="inp" data-g="3.0" data-fx="up"><span data-g="3.1" data-fx="type">hzklink</span></div>
   <div class="mini" data-g="3.0" data-fx="up"><div class="k">TOTAL DU PANIER</div><div class="o gold">40,00 €</div></div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:640px"></div>''' + head(230, [('h1 mt', 'ET HOP,', '4.0'), ('big gold', '34,40 €', '4.1')]).replace('class="big gold"', 'class="big gold" style="font-size:150px"') + '''
   <div class="mini" style="top:720px"><div class="k">AVANT LE CODE</div><div class="o" style="color:#8f877a">40,00 €<div class="ln" data-g="4.0" data-fx="strike"></div></div></div>
   <div class="big2" style="top:1080px" data-g="4.1" data-fx="stamp" data-slow="4.1"><div style="font:900 64px Inter;color:#5fe0a8">- 5,60 € · -14 %</div><div style="font:700 26px Inter;letter-spacing:4px;color:#bba98a;margin-top:14px">AVEC LE CODE PROMO HACOO hzklink<br>PRIX D'EXEMPLE</div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', 'CODE PROMO HACOO', '5.0'), ('big gold', 'hzklink', '5.0'), ('it gold', "-14 % sur l'appli Hacoo", '5.1')]).replace('class="big gold"', 'class="big gold" style="font-size:150px"').replace('class="it gold"', 'class="it gold" style="font-size:60px"') + '''
   <div class="pill" style="top:730px;border-color:rgba(95,224,168,.85)" data-g="5.1" data-fx="up"><div class="pin" style="background:#5fe0a8">★</div><div><b>LIENS DES ARTICLES TENDANCE</b><span>tout est dans ma bio</span></div></div>
   <div class="cond" style="top:880px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
