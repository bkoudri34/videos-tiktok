import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°2 du 17/11/2026 - style v3 nuit & or, accent bleu électrique, « carte à gratter » :
# pinces à cheveux 6,00 € + carnet 8,00 € + porte-clés 4,00 € = 18,00 € -> 15,48 € avec le code promo Hacoo hzklink (-14 %, prix d'exemple).
# Carte à gratter fermée -> 3 cases d'étagère qui se remplissent une par une -> la case grattée révèle le code -> étiquettes recalculées
# + total 15,48 € (ralenti) -> fin. Voix : Speko (speechify, voix par défaut ; voix clonée refusée 402), répliques 1 et 5 refaites seules.
NAME = 'hacoo29'
TITLE = 'Hacoo carte à gratter bleu'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Gratte cette case avant ta commande Hacou.", [("Gratte cette case", None), ("avant ta commande Hacoo.", None)]),
 ("Des pinces à cheveux : six euros.", [("Des pinces à cheveux :", None), ("6 €.", None)]),
 ("Un carnet : huit euros.", [("Un carnet :", None), ("8 €.", None)]),
 ("Un porte-clés : quatre euros. Prix d'exemple.", [("Un porte-clés :", None), ("4 €.", None), ("Prix d'exemple.", None)]),
 ("Et sous la case : le code promo Hacou, H Z K link.", [("Et sous la case :", None), ("le code promo Hacoo", None), ("hzklink.", None)]),
 ("Moins quatorze pour cent : quinze euros quarante-huit au lieu de dix-huit.", [("-14 % :", None), ("15,48 €", None), ("au lieu de 18 €.", None)]),
 ("Enregistre la vidéo, les liens sont dans ma bio.", [("Enregistre la vidéo,", None), ("les liens sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 1.79), (2.22, 3.60), (3.99, 5.10), (5.49, 7.58), (8.04, 11.27), (11.70, 14.39), (14.87, 16.53)]
GSTART = [[0.1, 0.9], [2.24, 3.14], [3.99, 4.68], [5.49, 6.30, 7.06], [8.04, 8.78, 10.18], [11.70, 12.74, 13.64], [14.87, 15.74]]
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
.be{color:#7fa4ff;text-shadow:0 0 18px rgba(91,140,255,.55)}
.sc{position:absolute;left:190px;top:760px;width:700px;height:440px;border-radius:34px;background:linear-gradient(140deg,#1b2a5a,#0d1430);border:5px solid #5b8cff;box-shadow:0 30px 90px rgba(0,0,0,.7),0 0 60px rgba(91,140,255,.25);text-align:center;padding-top:30px}
.sc .k{font:800 28px Inter;letter-spacing:6px;color:#bcd0ff}
.sc .z{position:absolute;left:70px;top:110px;width:560px;height:260px;border-radius:22px;background:repeating-linear-gradient(135deg,#c7ccd6 0 14px,#aeb4c0 14px 28px);display:flex;align-items:center;justify-content:center;font:900 140px 'DejaVu Serif',serif;color:#7d8494;overflow:hidden}
.sc .r{position:absolute;left:70px;top:110px;width:560px;height:260px;border-radius:22px;background:#f4efe4;color:#14203f;display:flex;flex-direction:column;align-items:center;justify-content:center}
.sc .r small{font:800 26px Inter;letter-spacing:5px;color:#3a5ad1}
.sc .r b{font:900 96px 'DejaVu Sans Mono',monospace;line-height:1.1}
.sc .r span{font:900 40px Inter;color:#c41f3e}
.coin{position:absolute;width:150px;height:150px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#fff0c0,#e9b456 50%,#a8701f);box-shadow:0 10px 0 #7a5016,0 0 30px rgba(240,180,80,.45)}
.shelf{position:absolute;left:90px;top:1180px;width:900px;height:22px;border-radius:6px;background:linear-gradient(180deg,#5b8cff,#2a4aa8);box-shadow:0 14px 40px rgba(0,0,0,.6)}
.slot{position:absolute;top:840px;width:270px;height:340px;text-align:center}
.slot .ic{width:270px;height:250px;display:flex;align-items:flex-end;justify-content:center}
.slot .pt{display:inline-block;margin-top:14px;padding:6px 22px;border-radius:14px;background:#f4efe4;color:#14203f;font:900 52px 'DejaVu Serif',serif;white-space:nowrap}
.slot .pt s{color:#8f877a;font-size:34px;text-decoration-color:#ff4d6d;margin-right:8px}
.slot.e .ic{opacity:.15}
.ex{position:absolute;left:0;top:1260px;width:1080px;text-align:center;font:800 28px Inter;letter-spacing:5px;color:#9a917f}
.tot{position:absolute;left:0;top:600px;width:1080px;text-align:center}
.tot .n{font:900 200px 'DejaVu Serif',serif;line-height:1.05}
.tot .o{font:900 76px 'DejaVu Serif',serif;color:#8f877a;text-decoration:line-through;text-decoration-color:#ff4d6d;text-decoration-thickness:7px}
.chip{position:absolute;left:170px;width:740px;height:130px;border-radius:65px;background:#0d1430;border:5px solid #5b8cff;display:flex;align-items:center;justify-content:center;gap:24px;white-space:nowrap;box-shadow:0 0 50px rgba(91,140,255,.35)}
.chip .k{font:800 30px Inter;letter-spacing:3px;color:#a9c0ff}
.chip .c{font:900 64px 'DejaVu Sans Mono',monospace;color:#fff}
'''
ITEMS = [('Pinces', '6 €', '5,16 €'), ('Carnet', '8 €', '6,88 €'), ('Porte-clés', '4 €', '3,44 €')]
XS = [110, 405, 700]


def shelf(filled, gnew=None, after=False):
    out = '<div class="shelf"></div>'
    for k, ((ic, pr, npr), x) in enumerate(zip(ITEMS, XS)):
        if k < filled:
            a = f' data-g="{gnew}" data-fx="pop"' if (gnew and k == filled - 1) else ''
            price = npr if after else pr
            pa = f' data-g="{gnew}" data-fx="stamp"' if (gnew and k == filled - 1) else ''
            out += f'<div class="slot" style="left:{x}px"><div class="ic"{a}>{icon(ic, 230)}</div><div class="pt"{pa}>{price}</div></div>'
        else:
            out += f'<div class="slot e" style="left:{x}px"><div class="ic"><div style="font:900 160px \'DejaVu Serif\',serif;color:#fff">?</div></div></div>'
    return out


def card(top, revealed=False, g=None):
    a = f' data-g="{g}" data-fx="fade"' if g else ''
    rv = f'<div class="r"{a}><small>CODE PROMO HACOO</small><b>hzklink</b><span>-14 %</span></div>' if revealed else ''
    return f'<div class="sc" style="top:{top}px"><div class="k">CARTE À GRATTER · HACOO</div><div class="z">?</div>{rv}</div>'


BODY = hud('FRANCE · CARTE À GRATTER', 'HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(210, [('h1', 'GRATTE CETTE CASE', None, 'font-size:84px'), ('it gold', 'avant ta commande', None, 'font-size:80px'), ('h1 be', 'HACOO.', None, 'font-size:110px')]) + card(780) + '''
   <div class="coin" style="left:770px;top:1130px"></div></div>
  <div class="scene" data-s="1" data-in="right">''' + hd(230, [('h1 be', 'DES PINCES À CHEVEUX :', '1.0', 'font-size:66px'), ('big gold', '6 €.', '1.1', 'font-size:140px')]) + shelf(1, '1.1') + '''
   <div class="ex">PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 be', 'UN CARNET :', '2.0', 'font-size:84px'), ('big gold', '8 €.', '2.1', 'font-size:140px')]) + shelf(2, '2.1') + '''
   <div class="ex">PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="3" data-in="right">''' + hd(230, [('h1 be', 'UN PORTE-CLÉS :', '3.0', 'font-size:80px'), ('big gold', '4 €.', '3.1', 'font-size:140px'), ('it gold', "Prix d'exemple.", '3.2', 'font-size:64px')]).replace('top:230px', 'top:210px') + shelf(3, '3.1') + '''
   <div class="ex" data-g="3.2" data-fx="fade">TOTAL : 18,00 € · PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="4" data-in="up">''' + hd(230, [('h1', 'ET SOUS LA CASE :', '4.0', 'font-size:80px'), ('h1 be', 'LE CODE PROMO HACOO', '4.1', 'font-size:66px'), ('big gold', 'hzklink.', '4.2', 'font-size:120px')]) + card(760, True, '4.2') + '''
   <div class="coin" style="left:770px;top:1100px" data-g="4.0" data-fx="left"></div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="rays" style="top:560px"></div>''' + hd(230, [('h1 be', '-14 % :', '5.0', 'font-size:110px')]) + '''
   <div class="tot"><div class="n gold" data-g="5.1" data-fx="stamp" data-slow="5.1">15,48 €</div><div class="o" data-g="5.2" data-fx="fade">18,00 €</div></div>
   ''' + shelf(3, None, True).replace('class="shelf"', 'class="shelf" style="top:1340px"').replace('<div class="slot" style="', '<div class="slot" data-g="5.0" data-fx="up" style="top:1000px;') + '''
   <div class="ex" style="top:1410px" data-g="5.1" data-fx="fade">PRIX D'EXEMPLE · CODE PROMO HACOO hzklink</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'CODE PROMO HACOO', '6.0', ''), ('big gold', 'hzklink', '6.0', 'font-size:150px'), ('it gold', "-14 % sur l'appli Hacoo", '6.0', 'font-size:60px')]) + '''
   <div class="pill" style="top:730px;border-color:rgba(91,140,255,.85)" data-g="6.0" data-fx="up"><div class="pin" style="background:#5b8cff;color:#fff">★</div><div><b>ENREGISTRE LA VIDÉO</b><span data-g="6.1" data-fx="fade">liens des articles tendance en bio</span></div></div>
   <div class="cond" style="top:880px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
