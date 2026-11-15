import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°1 du 15/11/2026 - style v3 nuit & or, accent saphir, « le panier qui fond en direct » :
# bougie 9,90 € + mug 7,50 € + guirlande 11,60 € = 29,00 € -> 24,94 € avec le code promo Hacoo hzklink (-14 %, prix d'exemple).
# Voix : Speko (speechify, voix par défaut ; voix clonée refusée 402).
NAME = 'hacoo24'
TITLE = 'Hacoo panier saphir'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Ton panier Hacou va fondre en direct.", [("Ton panier Hacoo", None), ("va fondre", None), ("en direct.", None)]),
 ("Une bougie, un mug, une guirlande.", [("Une bougie,", None), ("un mug,", None), ("une guirlande.", None)]),
 ("Total : vingt-neuf euros, en prix d'exemple.", [("Total : 29 €,", None), ("en prix d'exemple.", None)]),
 ("Tu tapes le code promo Hacou H Z K link.", [("Tu tapes", None), ("le code promo Hacoo", None), ("hzklink.", None)]),
 ("Et hop : vingt-quatre euros quatre-vingt-quatorze.", [("Et hop :", None), ("24,94 €.", None)]),
 ("Moins quatorze pour cent. Les liens des articles tendance sont dans ma bio.", [("-14 %.", None), ("Les liens des articles tendance", None), ("sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 1.76), (1.98, 3.77), (3.93, 5.83), (6.23, 8.37), (8.68, 10.99), (11.35, 14.14)]
GSTART = [[0.1, 0.8, 1.2], [1.98, 2.7, 3.2], [3.93, 5.2], [6.23, 6.6, 7.7], [8.68, 9.4], [11.35, 12.4, 13.7]]
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
.sa{color:#7fa8ff;text-shadow:0 0 18px rgba(108,156,255,.5)}
.cart{position:absolute;left:150px;width:780px;border-radius:34px;background:#f3f1ec;color:#141824;padding:30px 36px 26px;box-sizing:border-box;box-shadow:0 40px 100px rgba(0,0,0,.75)}
.cart .t{display:flex;justify-content:space-between;font:800 28px 'DejaVu Sans Mono',monospace;letter-spacing:5px;color:#3d5fb8;margin-bottom:8px}
.cart .it{display:flex;align-items:center;gap:22px;padding:14px 0;border-bottom:2px dashed rgba(20,24,36,.18);white-space:nowrap}
.cart .ic{flex:none;width:110px;height:110px;border-radius:20px;background:#1a2033;display:flex;align-items:center;justify-content:center}
.cart .nm{flex:1;font:800 36px Inter}
.cart .pr{font:900 44px 'DejaVu Serif',serif}
.cart .tt{display:flex;justify-content:space-between;align-items:baseline;padding-top:18px;font:900 40px Inter;white-space:nowrap}
.cart .tt b{font:900 64px 'DejaVu Serif',serif;color:#2d4fa6}
.cart .ex{font:700 22px Inter;letter-spacing:3px;color:#7a7f8c;text-align:right}
.field{position:absolute;left:150px;width:780px;height:250px;border-radius:30px;background:#0e1220;border:4px solid #6c9cff;box-shadow:0 0 50px rgba(108,156,255,.3)}
.field .lb{position:absolute;left:40px;top:28px;font:800 28px Inter;letter-spacing:4px;color:#9dbbff}
.field .in{position:absolute;left:40px;top:84px;width:700px;height:120px;border-radius:20px;background:#fff;color:#111;font:900 72px 'DejaVu Sans Mono',monospace;line-height:120px;padding-left:34px;box-sizing:border-box;white-space:nowrap}
.mtot{position:absolute;left:150px;width:780px;display:flex;justify-content:space-between;align-items:baseline;font:900 38px Inter;color:#e9e4da;white-space:nowrap}
.mtot b{font:900 80px 'DejaVu Serif',serif;color:#f3f1ec}
.old{position:absolute;left:0;width:1080px;text-align:center;font:900 96px 'DejaVu Serif',serif;color:#8f877a;text-decoration:line-through;text-decoration-color:#ff5a5a}
.drip{position:absolute;width:26px;border-radius:0 0 13px 13px;background:linear-gradient(#6c9cff,#3d5fb8)}
.bdg{position:absolute;left:390px;top:1120px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle,#18264a,#0a0f1e);border:6px solid #6c9cff;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 0 50px rgba(108,156,255,.45)}
.bdg b{font:900 90px 'DejaVu Serif',serif;color:#fff}.bdg span{font:800 20px Inter;letter-spacing:3px;color:#c4d6ff}
'''
ITEMS = [('Bougie', 'Bougie', '9,90 €'), ('Mug', 'Mug', '7,50 €'), ('Guirlande', 'Guirlande', '11,60 €')]


def cart(top, gs=None, total='29,00 €', g_tot=None):
    rows = ''
    for k, (ic, nm, pr) in enumerate(ITEMS):
        a = f' data-g="{gs[k]}" data-fx="right"' if gs else ''
        rows += f'<div class="it"{a}><div class="ic">{icon(ic, 96)}</div><div class="nm">{nm}</div><div class="pr">{pr}</div></div>'
    ta = f' data-g="{g_tot}" data-fx="tick"' if g_tot else ''
    return (f'<div class="cart" style="top:{top}px"><div class="t"><span>MON PANIER HACOO</span><span>3 ARTICLES</span></div>{rows}'
            f'<div class="tt"{ta}><span>TOTAL</span><b>{total}</b></div><div class="ex">PRIX D\'EXEMPLE</div></div>')


BODY = hud('FRANCE · PANIER', 'HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('h1', 'TON PANIER HACOO', None, ''), ('it gold', 'va fondre', None, 'font-size:92px'), ('h1 sa', 'EN DIRECT.', None, 'font-size:90px')]) + cart(700) + '''
   <div class="drip" style="left:300px;top:1318px;height:60px"></div><div class="drip" style="left:520px;top:1318px;height:95px"></div><div class="drip" style="left:760px;top:1318px;height:45px"></div></div>
  <div class="scene" data-s="1" data-in="right">''' + hd(230, [('h1 sa', 'UNE BOUGIE,', '1.0', ''), ('it gold', 'un mug,', '1.1', 'font-size:84px'), ('it gold', 'une guirlande.', '1.2', 'font-size:84px')]) + cart(640, ['1.0', '1.1', '1.2'], '…', None).replace('<div class="tt">', '<div class="tt" style="opacity:.25">') + '''</div>
  <div class="scene" data-s="2" data-in="up">''' + hd(230, [('h1', 'TOTAL : 29 €,', '2.0', 'font-size:90px'), ('it gold', "en prix d'exemple.", '2.1', 'font-size:80px')]) + cart(640, None, '29,00 €', '2.0') + '''</div>
  <div class="scene" data-s="3" data-in="pop">''' + hd(230, [('h1', 'TU TAPES', '3.0', ''), ('it gold', 'le code promo Hacoo', '3.1', 'font-size:80px'), ('big gold', 'hzklink.', '3.2', 'font-size:110px')]) + '''
   <div class="field" style="top:760px" data-g="3.0" data-fx="up"><div class="lb">CODE PROMO HACOO</div><div class="in"><span data-g="3.2" data-fx="type">hzklink</span></div></div>
   <div class="mtot" style="top:1080px" data-g="3.0" data-fx="fade"><span>TOTAL DU PANIER</span><b>29,00 €</b></div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:640px"></div>''' + hd(230, [('h1 sa', 'ET HOP :', '4.0', 'font-size:96px')]) + '''
   <div class="old" style="top:420px" data-g="4.0" data-fx="fade">29,00 €</div>
   <div class="abs" style="left:0;top:600px;width:1080px;text-align:center" data-g="4.1" data-fx="stamp" data-slow="4.1"><div style="font:800 34px Inter;letter-spacing:6px;color:#e9e4da">NOUVEAU TOTAL</div><div class="gold" style="font:900 200px 'DejaVu Serif',serif;line-height:1.1">24,94 €</div></div>
   <div class="abs" style="left:0;top:930px;width:1080px;text-align:center;font:800 30px Inter;letter-spacing:4px;color:#9dbbff" data-g="4.1" data-fx="fade">✓ CODE PROMO HACOO hzklink APPLIQUÉ</div>
   <div class="bdg" data-g="4.1" data-fx="pop"><b>-14 %</b><span>PRIX D'EXEMPLE</span></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'CODE PROMO HACOO', '5.0', ''), ('big gold', 'hzklink', '5.0', 'font-size:150px'), ('it gold', "-14 % sur l'appli Hacoo", '5.0', 'font-size:60px')]) + '''
   <div class="pill" style="top:730px;border-color:rgba(108,156,255,.85)" data-g="5.1" data-fx="up"><div class="pin" style="background:#6c9cff">★</div><div><b>LES LIENS DES ARTICLES TENDANCE</b><span data-g="5.2" data-fx="fade">sont dans ma bio</span></div></div>
   <div class="cond" style="top:880px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
