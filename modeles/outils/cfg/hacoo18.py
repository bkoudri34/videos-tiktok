import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°1 du 12/11/2026 - style v3 nuit & or, accent prune, « la liste de Noël » : lampe 12,90 + pyjama 16,50 + trousse 5,60 = 35,00 € -> 30,10 € avec le code promo Hacoo hzklink
# (-14 %, prix d'exemple). Liste cochée -> 3 articles + étiquettes -> total -> saisie du code -> total barré -> écran de fin.
NAME = 'hacoo18'
TITLE = 'Hacoo liste de Noel prune'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Ta liste de Noël sur Hacou, en moins cher.", [("Ta liste de Noël", None), ("sur Hacoo,", None), ("en moins cher.", None)]),
 ("Une lampe, un pyjama et une trousse.", [("Une lampe,", None), ("un pyjama", None), ("et une trousse.", None)]),
 ("Trente-cinq euros au total, en prix d'exemple.", [("35 € au total,", None), ("en prix d'exemple.", None)]),
 ("Tu tapes le code promo Hacou H Z K link.", [("Tu tapes le code promo Hacoo", None), ("hzklink.", None)]),
 ("Et le total descend à trente euros dix.", [("Et le total descend", None), ("à 30,10 €.", None)]),
 ("Les liens des articles tendance sont dans ma bio.", [("Les liens des articles tendance", None), ("sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 2.69), (3.029, 5.545), (5.894, 8.146), (8.504, 11.884), (12.182, 14.266), (14.625, 16.849)]
GSTART = [[0.1, 1.0, 2.0], [3.03, 3.9, 4.8], [5.9, 7.4], [8.51, 10.1], [12.19, 13.2], [14.63, 16.1]]
MINLEN = 2.3
GAP = 0.36
TAIL = 2.2
CSS = '''
.pr{color:#e48ae8;text-shadow:0 0 18px rgba(211,107,216,.5)}
.list{position:absolute;left:220px;top:690px;width:640px;height:720px;background:#f4efe4;color:#2a1a2c;border-radius:10px;box-shadow:0 40px 90px rgba(0,0,0,.7);transform:rotate(-3deg);padding:50px 56px}
.list .t{font:700 italic 66px 'Liberation Serif',serif;color:#7a2a80;text-align:center}
.list .r{display:flex;align-items:center;gap:22px;margin-top:40px;font:700 40px Inter;white-space:nowrap}
.list .r i{width:46px;height:46px;border:4px solid #7a2a80;border-radius:10px;display:flex;align-items:center;justify-content:center;font:900 34px Inter;font-style:normal;color:#d36bd8}
.ribbon{position:absolute;left:470px;top:640px;width:140px;height:110px;background:#d36bd8;clip-path:polygon(0 0,100% 0,100% 100%,50% 75%,0 100%)}
.ic{position:absolute;left:130px;width:200px;height:200px;border-radius:30px;background:#1c1020;border:3px solid #d36bd8;display:flex;align-items:center;justify-content:center}
.et{position:absolute;left:520px;padding:12px 26px;border-radius:14px;background:#f4efe4;color:#1c1712;font:800 34px Inter;white-space:nowrap}
.et b{display:block;font:900 44px 'DejaVu Serif',serif;color:#8a2f90}
.tot{position:absolute;left:190px;top:720px;width:700px;height:460px;border-radius:30px;border:4px solid #d36bd8;background:rgba(40,16,44,.7);text-align:center;padding-top:50px}
.tot .k{font:800 34px Inter;letter-spacing:8px;color:#e9e4da}
.tot .v{font:900 150px 'DejaVu Serif',serif;line-height:1.3;white-space:nowrap}
.tot .x{font:700 26px Inter;letter-spacing:5px;color:#bba98a}
.inp{position:absolute;left:150px;top:760px;width:780px;height:120px;border-radius:60px;background:#fff;color:#111;display:flex;align-items:center;padding:0 40px;font:900 64px 'DejaVu Sans Mono',monospace;white-space:nowrap}
.inl{position:absolute;left:190px;top:700px;font:800 28px Inter;letter-spacing:5px;color:#e48ae8}
.btn{position:absolute;left:330px;top:940px;width:420px;height:100px;border-radius:50px;background:#d36bd8;color:#22082a;text-align:center;font:900 40px Inter;line-height:100px;letter-spacing:3px}
.pt{position:absolute;left:190px;top:700px;width:700px;height:440px;border-radius:30px;background:#f4efe4;color:#1c1712;text-align:center;box-shadow:0 40px 90px rgba(0,0,0,.7);transform:rotate(3deg)}
.pt .o{font:800 64px 'DejaVu Serif',serif;color:#8f877a;margin-top:50px;position:relative;display:inline-block}
.pt .ln{position:absolute;left:-10px;right:-10px;top:50%;height:8px;background:#c0392b;transform-origin:0 50%}
.pt .n{font:900 150px 'DejaVu Serif',serif;color:#8a2f90;line-height:1.2}
.pt .x{font:700 24px Inter;letter-spacing:4px;color:#7a6f60}
'''
ITEMS = [('Lampe', '12,90 €', 560, 0), ('Pyjama', '16,50 €', 810, 1), ('Trousse', '5,60 €', 1060, 2)]
SC1 = ''.join(f'<div class="ic" style="top:{y}px" data-g="1.{g}" data-fx="up">' + icon(n, 170) + f'</div><div class="ldr" style="left:340px;top:{y + 100}px;width:170px" data-g="1.{g}" data-fx="grow"></div><div class="et" style="top:{y + 50}px" data-g="1.{g}" data-fx="left">{n}<b>{p}</b></div>' for n, p, y, g in ITEMS)
BODY = hud('FRANCE · LISTE DE NOËL', 'HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + head(220, [('h1', 'TA LISTE DE NOËL', None), ('h1 pr', 'SUR HACOO,', None), ('it gold', 'en moins cher.', None)]) + '''
   <div class="list"><div class="t">Ma liste</div><div class="r"><i>✓</i>Lampe</div><div class="r"><i>✓</i>Pyjama</div><div class="r"><i>✓</i>Trousse</div><div class="r" style="color:#8a2f90"><i>%</i>code promo Hacoo</div></div><div class="ribbon"></div></div>
  <div class="scene" data-s="1" data-in="right">''' + head(230, [('h1', 'UNE LAMPE,', '1.0'), ('it gold', 'un pyjama et une trousse.', '1.1')]).replace('class="it gold"', 'class="it gold" style="font-size:64px"') + SC1 + '''</div>
  <div class="scene" data-s="2" data-in="pop"><div class="rays" style="top:700px"></div>''' + head(230, [('h1', '35 € AU TOTAL,', '2.0'), ('it gold', "en prix d'exemple.", '2.1')]) + '''
   <div class="tot" data-g="2.0" data-fx="up"><div class="k">MON PANIER</div><div class="v gold">35,00 €</div><div class="x" data-g="2.1" data-fx="fade">PRIX D'EXEMPLE · 3 ARTICLES</div></div></div>
  <div class="scene" data-s="3" data-in="left">''' + head(230, [('h1 s', 'TU TAPES LE CODE PROMO HACOO', '3.0'), ('big gold', 'hzklink', '3.1')]).replace('class="h1 s"', 'class="h1 s" style="font-size:54px"').replace('class="big gold"', 'class="big gold" style="font-size:140px"') + '''
   <div class="inl" data-g="3.0" data-fx="fade">CODE PROMO HACOO</div>
   <div class="inp" data-g="3.0" data-fx="up"><span data-g="3.1" data-fx="type">hzklink</span></div>
   <div class="btn" data-g="3.1" data-fx="pop">APPLIQUER</div></div>
  <div class="scene" data-s="4" data-in="up">''' + head(230, [('h1', 'LE TOTAL DESCEND', '4.0'), ('it gold', 'à 30,10 €.', '4.1')]) + '''
   <div class="pt" data-g="4.0" data-fx="up"><div class="o">35,00 €<div class="ln" data-g="4.1" data-fx="strike"></div></div><div class="n" data-g="4.1" data-fx="stamp" data-slow="4.1">30,10 €</div><div class="x">-14 % AVEC hzklink · PRIX D'EXEMPLE</div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', 'CODE PROMO HACOO', '5.0'), ('big gold', 'hzklink', '5.0'), ('it gold', "-14 % sur l'appli Hacoo", '5.1')]).replace('class="big gold"', 'class="big gold" style="font-size:150px"').replace('class="it gold"', 'class="it gold" style="font-size:60px"') + '''
   <div class="pill" style="top:730px;border-color:rgba(211,107,216,.85)" data-g="5.1" data-fx="up"><div class="pin" style="background:#d36bd8">★</div><div><b>LIENS DES ARTICLES TENDANCE</b><span>tout est dans ma bio</span></div></div>
   <div class="cond" style="top:880px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
