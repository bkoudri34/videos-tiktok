import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°2 du 11/11/2026 - style v3 nuit & or, accent cuivre, « le calcul » : doudoune 49,90 + bottines 38,60 + écharpe 11,50 = 100,00 € -> 86,00 € avec le code promo Hacoo hzklink
# (-14 %, prix d'exemple) ; tableau 20 € -> 2,80 € / 50 € -> 7,00 € / 100 € -> 14,00 € d'économie.
NAME = 'hacoo17'
TITLE = 'Hacoo calcul cuivre'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Cent euros de panier Hacou, quatorze euros pour toi.", [("100 € de panier Hacoo,", None), ("14 € pour toi.", None)]),
 ("Une doudoune, des bottines et une écharpe.", [("Une doudoune,", None), ("des bottines", None), ("et une écharpe.", None)]),
 ("Avec le code promo Hacou H Z K link, c'est moins quatorze pour cent.", [("Avec le code promo Hacoo", None), ("hzklink,", None), ("c'est -14 %.", None)]),
 ("Sur cinquante euros, t'économises déjà sept euros.", [("Sur 50 €,", None), ("t'économises déjà 7 €.", None)]),
 ("Sur cent euros, tu ne paies que quatre-vingt-six.", [("Sur 100 €,", None), ("tu ne paies que 86 €.", None)]),
 ("Les liens des articles sont dans ma bio.", [("Les liens des articles", None), ("sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 2.742), (3.180, 5.452), (5.798, 10.152), (10.539, 12.988), (13.339, 15.844), (16.267, 17.857)]
GSTART = [[0.1, 1.69], [3.18, 3.96, 4.82], [5.8, 7.35, 9.04], [10.54, 11.72], [13.34, 14.38], [16.27, 17.2]]
MINLEN = 2.4
GAP = 0.36
TAIL = 2.2


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.cu{color:#ff9a4d;text-shadow:0 0 18px rgba(255,154,77,.45)}
.bag{position:absolute;left:330px;top:820px;width:420px;height:440px;border-radius:26px 26px 40px 40px;background:linear-gradient(180deg,#3b2414,#1a0f08);border:5px solid #d9a24c;box-shadow:0 40px 90px rgba(0,0,0,.7)}
.bag:before{content:'';position:absolute;left:120px;top:-110px;width:170px;height:150px;border:12px solid #d9a24c;border-bottom:0;border-radius:90px 90px 0 0}
.tag{position:absolute;padding:16px 30px;border-radius:18px;background:#ff9a4d;color:#2a1405;font:900 64px 'DejaVu Serif',serif;white-space:nowrap;box-shadow:0 14px 40px rgba(255,154,77,.4)}
.ic{position:absolute;left:130px;width:200px;height:200px;border-radius:30px;background:#1a120c;border:3px solid #ff9a4d;display:flex;align-items:center;justify-content:center}
.et{position:absolute;left:520px;padding:12px 26px;border-radius:14px;background:#f4efe4;color:#1c1712;font:800 34px Inter;white-space:nowrap}
.et b{display:block;font:900 44px 'DejaVu Serif',serif;color:#b8571c}
.inp{position:absolute;left:150px;top:650px;width:780px;height:120px;border-radius:60px;background:#fff;color:#111;display:flex;align-items:center;padding:0 40px;font:900 64px 'DejaVu Sans Mono',monospace;white-space:nowrap}
.inl{position:absolute;left:190px;top:600px;font:800 28px Inter;letter-spacing:5px;color:#ff9a4d}
.tb{position:absolute;left:150px;top:640px;width:780px;border-radius:26px;overflow:hidden;border:3px solid #d9a24c;background:rgba(26,18,12,.9)}
.tb .r{display:flex;justify-content:space-between;padding:26px 44px;font:800 44px Inter;color:#e9e4da;border-bottom:2px solid rgba(217,162,76,.3);white-space:nowrap}
.tb .r b{font:900 50px 'DejaVu Serif',serif;color:#ff9a4d}
.tb .h{font:800 26px Inter;letter-spacing:4px;color:#9a917f;padding:20px 44px}
.pt{position:absolute;left:190px;top:700px;width:700px;height:420px;border-radius:30px;background:#f4efe4;color:#1c1712;text-align:center;box-shadow:0 40px 90px rgba(0,0,0,.7);transform:rotate(-3deg)}
.pt .o{font:800 60px 'DejaVu Serif',serif;color:#8f877a;margin-top:50px;position:relative;display:inline-block}
.pt .ln{position:absolute;left:-10px;right:-10px;top:50%;height:8px;background:#c0392b;transform-origin:0 50%}
.pt .n{font:900 150px 'DejaVu Serif',serif;color:#b8571c;line-height:1.2}
.pt .x{font:700 24px Inter;letter-spacing:4px;color:#7a6f60}
'''
BODY = hud('FRANCE · CALCUL', 'PANIER') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('h1 s', '100 € DE PANIER HACOO,', None, 'font-size:58px'), ('big gold', '14 €', None, 'font-size:190px'), ('it gold', 'pour toi.', '0.1', 'font-size:76px')]) + '''
   <div class="bag"></div><div class="tag" style="left:560px;top:1000px;transform:rotate(8deg)">-14 €</div></div>
  <div class="scene" data-s="1" data-in="right">''' + hd(230, [('h1', 'UNE DOUDOUNE,', '1.0', ''), ('it gold', 'des bottines et une écharpe.', '1.1', 'font-size:60px')]) + '''
   <div class="ic" style="top:560px" data-g="1.0" data-fx="up">''' + icon('Doudoune', 170) + '''</div><div class="ldr" style="left:340px;top:660px;width:170px" data-g="1.0" data-fx="grow"></div><div class="et" style="top:610px" data-g="1.0" data-fx="left">Doudoune<b>49,90 €</b></div>
   <div class="ic" style="top:810px" data-g="1.1" data-fx="up">''' + icon('Bottines', 170) + '''</div><div class="ldr" style="left:340px;top:910px;width:170px" data-g="1.1" data-fx="grow"></div><div class="et" style="top:860px" data-g="1.1" data-fx="left">Bottines<b>38,60 €</b></div>
   <div class="ic" style="top:1060px" data-g="1.2" data-fx="up">''' + icon('Écharpe', 170) + '''</div><div class="ldr" style="left:340px;top:1160px;width:170px" data-g="1.2" data-fx="grow"></div><div class="et" style="top:1110px" data-g="1.2" data-fx="left">Écharpe<b>11,50 €</b></div>
   <div class="abs" style="left:240px;top:1310px;width:600px;text-align:center;font:700 26px Inter;letter-spacing:4px;color:#bba98a" data-g="1.2" data-fx="fade">TOTAL 100,00 € · PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="2" data-in="pop"><div class="rays" style="top:760px"></div>''' + hd(230, [('h1 s', 'AVEC LE CODE PROMO HACOO', '2.0', 'font-size:58px')]) + '''
   <div class="inl" data-g="2.0" data-fx="fade">CODE PROMO HACOO</div>
   <div class="inp" data-g="2.0" data-fx="up"><span data-g="2.1" data-fx="type">hzklink</span></div>
   <div class="abs gold" style="left:0;top:880px;width:1080px;text-align:center;font:900 220px 'DejaVu Serif',serif" data-g="2.2" data-fx="stamp" data-slow="2.2">-14 %</div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('h1', 'SUR 50 €,', '3.0', ''), ('it gold', "t'économises déjà 7 €.", '3.1', 'font-size:66px')]) + '''
   <div class="tb" data-g="3.0" data-fx="up"><div class="h">PANIER → ÉCONOMIE (-14 %)</div>
    <div class="r"><span>20 €</span><b>2,80 €</b></div>
    <div class="r" style="background:rgba(255,154,77,.18)" data-g="3.1" data-fx="tick"><span>50 €</span><b>7,00 €</b></div>
    <div class="r"><span>100 €</span><b>14,00 €</b></div></div></div>
  <div class="scene" data-s="4" data-in="up">''' + hd(230, [('h1', 'SUR 100 €,', '4.0', ''), ('it gold', 'tu ne paies que 86 €.', '4.1', 'font-size:66px')]) + '''
   <div class="pt" data-g="4.0" data-fx="up"><div class="o">100,00 €<div class="ln" data-g="4.1" data-fx="strike"></div></div><div class="n" data-g="4.1" data-fx="stamp">86,00 €</div><div class="x">AVEC hzklink · PRIX D'EXEMPLE</div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'CODE PROMO HACOO', '5.0', ''), ('big gold', 'hzklink', '5.0', 'font-size:150px'), ('it gold', "-14 % sur l'appli Hacoo", '5.1', 'font-size:60px')]) + '''
   <div class="pill" style="top:730px;border-color:rgba(255,154,77,.85)" data-g="5.1" data-fx="up"><div class="pin" style="background:#ff9a4d">★</div><div><b>LIENS DES ARTICLES</b><span>tout est dans ma bio</span></div></div>
   <div class="cond" style="top:880px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
