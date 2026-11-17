import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°1 du 17/11/2026 - style v3 nuit & or, accent lavande, « le panier juste avant de payer » :
# casque audio 16,00 € + bouillotte 9,00 € = 25,00 € -> 21,50 € quand on tape le code promo Hacoo hzklink (-14 %, prix d'exemple).
# Écran panier -> fiche casque -> fiche bouillotte -> total 25 € -> champ « Code promo Hacoo » qui se tape -> total qui baisse (ralenti) -> fin.
# Voix : Speko (speechify, voix par défaut ; voix clonée refusée 402).
NAME = 'hacoo28'
TITLE = 'Hacoo panier lavande'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Ton panier Hacou, juste avant de payer.", [("Ton panier Hacoo,", None), ("juste avant de payer.", None)]),
 ("Un casque audio : seize euros, prix d'exemple.", [("Un casque audio :", None), ("16 €,", None), ("prix d'exemple.", None)]),
 ("Une bouillotte toute douce : neuf euros.", [("Une bouillotte toute douce :", None), ("9 €.", None)]),
 ("Total : vingt-cinq euros.", [("Total :", None), ("25 €.", None)]),
 ("Là, tu tapes le code promo Hacou H Z K link.", [("Là, tu tapes", None), ("le code promo Hacoo", None), ("hzklink.", None)]),
 ("Et hop : vingt et un euros cinquante.", [("Et hop :", None), ("21,50 €.", None)]),
 ("Les articles tendance ? Les liens sont dans ma bio.", [("Les articles tendance ?", None), ("Les liens sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 1.76), (2.17, 4.07), (4.40, 5.88), (6.32, 7.48), (8.15, 10.53), (10.90, 12.30), (12.70, 14.65)]
GSTART = [[0.1, 1.0], [2.2, 2.9, 3.6], [4.4, 5.43], [6.32, 6.8], [8.15, 8.7, 9.7], [10.9, 11.4], [12.7, 13.9]]
MINLEN = 1.9
GAP = 0.32
TAIL = 2.2


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.lv{color:#c4b2ff;text-shadow:0 0 18px rgba(180,156,255,.5)}
.cart{position:absolute;left:190px;top:700px;width:700px;border-radius:40px;background:#0f0d16;border:6px solid #2f2a3d;box-shadow:0 0 0 2px #4b4560,0 30px 90px rgba(0,0,0,.7);padding:30px 36px}
.cart .t{font:800 26px Inter;letter-spacing:6px;color:#c4b2ff;text-align:center;margin-bottom:18px}
.cart .r{display:flex;align-items:center;gap:22px;height:140px;border-bottom:2px solid rgba(255,255,255,.07);font:800 36px Inter;color:#eee9f7;white-space:nowrap}
.cart .r .i{flex:none;width:120px;height:120px;border-radius:22px;background:#f4efe4;display:flex;align-items:center;justify-content:center}
.cart .r span{flex:1}.cart .r b{font:900 40px 'DejaVu Serif',serif;color:#f3c766}
.cart .cf{margin-top:22px;height:92px;border-radius:22px;border:4px dashed #6c5fa0;display:flex;align-items:center;justify-content:space-between;padding:0 24px;font:700 28px Inter;color:#9c93b8;white-space:nowrap}
.cart .cf.on{border:4px solid #b49cff;background:rgba(180,156,255,.08);color:#fff}
.cart .cf em{font:900 40px 'DejaVu Sans Mono',monospace;color:#fff;font-style:normal}
.cart .tt{display:flex;justify-content:space-between;align-items:center;margin-top:22px;font:900 40px Inter;color:#eee9f7;white-space:nowrap}
.cart .tt b{font:900 64px 'DejaVu Serif',serif;color:#f3c766}
.card{position:absolute;left:240px;top:700px;width:600px;height:640px;border-radius:40px;background:#f4efe4;box-shadow:0 30px 90px rgba(0,0,0,.7),0 0 80px rgba(180,156,255,.25);text-align:center;padding-top:40px}
.card .k{font:800 28px Inter;letter-spacing:6px;color:#5c4aa8}
.card .n{font:900 46px Inter;color:#1c1626;margin-top:6px}
.tag{position:absolute;left:660px;top:1180px;width:260px;padding:16px 0;border-radius:22px;background:#b49cff;color:#140f22;text-align:center;transform:rotate(-7deg);box-shadow:0 20px 50px rgba(0,0,0,.6)}
.tag b{display:block;font:900 72px 'DejaVu Serif',serif;line-height:1.05}
.tag span{font:800 18px Inter;letter-spacing:2px}
.sum{position:absolute;left:0;top:1030px;width:1080px;text-align:center}
.sum .o{font:900 80px 'DejaVu Serif',serif;color:#8f877a;text-decoration:line-through;text-decoration-color:#b49cff;text-decoration-thickness:7px}
.sum .n{font:900 190px 'DejaVu Serif',serif;line-height:1.05}
.sum .x{font:800 26px Inter;letter-spacing:4px;color:#e9e4da}
.save{position:absolute;left:330px;top:1440px;width:420px;height:84px;border-radius:42px;background:#b49cff;color:#140f22;font:900 38px Inter;display:flex;align-items:center;justify-content:center}
.chip{position:absolute;left:170px;width:740px;height:130px;border-radius:65px;background:#151020;border:5px solid #b49cff;display:flex;align-items:center;justify-content:center;gap:24px;white-space:nowrap;box-shadow:0 0 50px rgba(180,156,255,.35)}
.chip .k{font:800 30px Inter;letter-spacing:3px;color:#c4b2ff}
.chip .c{font:900 64px 'DejaVu Sans Mono',monospace;color:#fff}
'''


def cart(top, code=False, total='25,00 €', a='', g_code=None):
    cf = (f'<div class="cf on">Code promo Hacoo<em{f" data-g={chr(34)}{g_code}{chr(34)} data-fx={chr(34)}type{chr(34)}" if g_code else ""}>hzklink</em></div>' if code else
          '<div class="cf">Code promo Hacoo<span>+ ajouter</span></div>')
    return (f'<div class="cart" style="top:{top}px"{a}><div class="t">MON PANIER HACOO</div>'
            f'<div class="r"><div class="i">{icon("Casque", 100)}</div><span>Casque audio</span><b>16,00 €</b></div>'
            f'<div class="r"><div class="i">{icon("Bouillotte", 100)}</div><span>Bouillotte</span><b>9,00 €</b></div>'
            f'{cf}<div class="tt"><span>TOTAL</span><b>{total}</b></div></div>')


BODY = hud('FRANCE · PANIER', 'HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(210, [('h1', 'TON PANIER', None, 'font-size:90px'), ('h1 lv', 'HACOO,', None, 'font-size:110px'), ('it gold', 'juste avant de payer.', None, 'font-size:72px')]) + cart(720) + '''</div>
  <div class="scene" data-s="1" data-in="right">''' + hd(230, [('h1 lv', 'UN CASQUE AUDIO :', '1.0', 'font-size:72px'), ('it gold', '16 €,', '1.1', 'font-size:100px'), ('it gold', "prix d'exemple.", '1.2', 'font-size:64px')]) + '''
   <div class="card" style="top:760px" data-g="1.0" data-fx="pop"><div class="k">ARTICLE 1</div><div class="n">Casque audio</div>''' + icon('Casque', 380) + '''</div>
   <div class="tag" data-g="1.1" data-fx="stamp"><b>16 €</b><span>PRIX D'EXEMPLE</span></div></div>
  <div class="scene" data-s="2" data-in="left">''' + hd(230, [('h1 lv', 'UNE BOUILLOTTE', '2.0', 'font-size:76px'), ('it gold', 'toute douce :', '2.0', 'font-size:76px'), ('it gold', '9 €.', '2.1', 'font-size:100px')]) + '''
   <div class="card" style="top:780px" data-g="2.0" data-fx="pop"><div class="k">ARTICLE 2</div><div class="n">Bouillotte</div>''' + icon('Bouillotte', 380) + '''</div>
   <div class="tag" style="left:150px;transform:rotate(7deg)" data-g="2.1" data-fx="stamp"><b>9 €</b><span>PRIX D'EXEMPLE</span></div></div>
  <div class="scene" data-s="3" data-in="up">''' + hd(230, [('h1', 'TOTAL :', '3.0', 'font-size:96px'), ('big gold', '25 €.', '3.1', 'font-size:150px')]) + cart(640, a=' data-g="3.0" data-fx="up"') + '''</div>
  <div class="scene" data-s="4" data-in="pop">''' + hd(230, [('h1', 'LÀ, TU TAPES', '4.0', ''), ('h1 lv', 'LE CODE PROMO HACOO', '4.1', 'font-size:66px'), ('big gold', 'hzklink.', '4.2', 'font-size:120px')]) + cart(700, code=True, g_code='4.2') + '''</div>
  <div class="scene" data-s="5" data-in="pop"><div class="rays" style="top:780px"></div>''' + hd(230, [('h1 lv', 'ET HOP :', '5.0', 'font-size:110px')]) + '''
   <div class="chip" style="top:620px" data-g="5.0" data-fx="up"><span class="k">CODE HACOO :</span><span class="c">hzklink</span></div>
   <div class="sum" style="top:820px"><div class="o" data-g="5.0" data-fx="fade">25,00 €</div><div class="n gold" data-g="5.1" data-fx="stamp" data-slow="5.1">21,50 €</div><div class="x" data-g="5.1" data-fx="fade">PRIX D'EXEMPLE · -14 % AVEC LE CODE</div></div>
   <div class="save" style="top:1280px" data-g="5.1" data-fx="pop">- 3,50 €</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'CODE PROMO HACOO', '6.0', ''), ('big gold', 'hzklink', '6.0', 'font-size:150px'), ('it gold', "-14 % sur l'appli Hacoo", '6.0', 'font-size:60px')]) + '''
   <div class="pill" style="top:730px;border-color:rgba(180,156,255,.85)" data-g="6.0" data-fx="up"><div class="pin" style="background:#b49cff;color:#140f22">★</div><div><b>LES ARTICLES TENDANCE ?</b><span data-g="6.1" data-fx="fade">les liens sont dans ma bio</span></div></div>
   <div class="cond" style="top:880px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
