import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°2 du 14/11/2026 - style v3 nuit & or, accent turquoise, « les cadeaux qu'on ouvre un par un » :
# coque 5,90 € + gourde 8,90 € + chaussons 13,20 € = 28,00 € -> 24,08 € avec le code promo Hacoo hzklink (-14 %, prix d'exemple).
# Voix : Speko (speechify, voix par défaut).
NAME = 'hacoo23'
TITLE = 'Hacoo cadeaux turquoise'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Tes cadeaux Hacou, moins chers avec un seul code.", [("Tes cadeaux Hacoo,", None), ("moins chers", None), ("avec un seul code.", None)]),
 ("Cadeau un : une coque de téléphone, cinq euros quatre-vingt-dix.", [("Cadeau 1 :", None), ("une coque de téléphone,", None), ("5,90 €.", None)]),
 ("Cadeau deux : une gourde, huit euros quatre-vingt-dix.", [("Cadeau 2 :", None), ("une gourde,", None), ("8,90 €.", None)]),
 ("Cadeau trois : des chaussons, treize euros vingt.", [("Cadeau 3 :", None), ("des chaussons,", None), ("13,20 €.", None)]),
 ("Vingt-huit euros. Et avec le code promo Hacou H Z K link ?", [("28 €.", None), ("Et avec le code promo Hacoo", None), ("hzklink ?", None)]),
 ("Vingt-quatre euros zéro huit. Prix d'exemple.", [("24,08 €.", None), ("Prix d'exemple.", None)]),
 ("Moins quatorze pour cent. Les liens des articles tendance sont dans ma bio.", [("-14 %.", None), ("Les liens des articles tendance", None), ("sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 2.18), (2.63, 5.48), (5.86, 8.36), (9.05, 10.97), (11.35, 14.98), (15.37, 17.35), (17.67, 20.96)]
GSTART = [[0.1, 0.9, 1.4], [2.63, 3.36, 4.4], [5.86, 6.7, 7.3], [9.05, 9.75, 10.43], [11.35, 12.72, 13.95], [15.37, 16.78], [17.67, 19.41, 20.5]]
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
.tq{color:#4fe6da;text-shadow:0 0 18px rgba(46,211,198,.5)}
.gb{position:absolute;border-radius:16px;background:linear-gradient(160deg,#1d4a47,#0c201f);border:4px solid #d9a24c;box-shadow:0 30px 70px rgba(0,0,0,.7)}
.gb:before{content:'';position:absolute;left:50%;top:0;width:44px;height:100%;margin-left:-22px;background:linear-gradient(#5ff0e4,#1fa79c)}
.gl{position:absolute;border-radius:14px;background:linear-gradient(160deg,#256360,#123331);border:4px solid #d9a24c}
.gl:before{content:'';position:absolute;left:50%;top:0;width:48px;height:100%;margin-left:-24px;background:linear-gradient(#5ff0e4,#1fa79c)}
.gq{position:absolute;width:100%;text-align:center;font:900 80px 'DejaVu Serif',serif}
.out{position:absolute;left:390px;top:560px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle,rgba(46,211,198,.35),rgba(46,211,198,0) 70%);display:flex;align-items:center;justify-content:center}
.ptg{position:absolute;left:640px;top:1030px;width:270px;padding:18px 0;border-radius:20px;background:#f4efe4;color:#0c201f;text-align:center;transform:rotate(5deg);box-shadow:0 20px 50px rgba(0,0,0,.6)}
.ptg b{display:block;font:900 60px 'DejaVu Serif',serif;white-space:nowrap}.ptg span{font:800 20px Inter;letter-spacing:3px;color:#1fa79c}
.dots{position:absolute;left:390px;top:1420px;width:300px;display:flex;justify-content:space-between}
.dots i{width:70px;height:16px;border-radius:8px;background:#2a2a26}.dots i.on{background:#2ed3c6;box-shadow:0 0 16px rgba(46,211,198,.7)}
.sm{position:absolute;top:640px;width:250px;height:330px;border-radius:24px;background:rgba(20,50,48,.6);border:3px solid #d9a24c;text-align:center;padding-top:20px}
.sm .p{font:900 44px 'DejaVu Serif',serif;color:#f3c766;margin-top:6px;white-space:nowrap}
.sumt{position:absolute;left:0;top:1010px;width:1080px;text-align:center;font:900 80px 'DejaVu Serif',serif;white-space:nowrap}
.chip2{position:absolute;left:150px;top:1180px;width:780px;height:120px;border-radius:60px;background:#fff;color:#111;display:flex;align-items:center;justify-content:center;gap:20px;font:900 54px 'DejaVu Sans Mono',monospace;white-space:nowrap;border:5px solid #2ed3c6;box-shadow:0 0 40px rgba(46,211,198,.4)}
.chip2 small{font:800 26px Inter;letter-spacing:3px;color:#1a8f86}
.oldp{position:absolute;left:0;top:620px;width:1080px;text-align:center;font:900 90px 'DejaVu Serif',serif;color:#8f877a;text-decoration:line-through;text-decoration-color:#e74c3c}
.newp{position:absolute;left:0;top:780px;width:1080px;text-align:center}
.rib{position:absolute;left:240px;top:1130px;width:600px;height:100px;border-radius:20px;background:#2ed3c6;color:#07211f;text-align:center;font:900 42px Inter;line-height:100px;letter-spacing:4px}
'''
GIFTS = [('Coque', 'COQUE', '5,90 €'), ('Gourde', 'GOURDE', '8,90 €'), ('Chaussons', 'CHAUSSONS', '13,20 €')]


def gift_scene(k):
    nm, lab, pr = GIFTS[k]
    g = k + 1
    dots = '<div class="dots">' + ''.join(f'<i class="{"on" if j <= k else ""}"></i>' for j in range(3)) + '</div>'
    return (f'<div class="gb" style="left:290px;top:1000px;width:500px;height:380px"></div>'
            f'<div class="abs" style="left:0;top:0" data-g="{g}.1" data-fx="up"><div class="gl" style="left:270px;top:900px;width:540px;height:100px;transform:rotate(-14deg) translate(-40px,-60px)"></div></div>'
            f'<div class="out" style="top:600px" data-g="{g}.1" data-fx="up">{icon(nm, 300)}</div>'
            f'<div class="ptg" data-g="{g}.2" data-fx="stamp"><b>{pr}</b><span>PRIX D\'EXEMPLE</span></div>' + dots)


BOXES = ''.join(f'<div class="gb" style="left:{x}px;top:{y}px;width:{w}px;height:{w - 20}px;transform:rotate({r}deg)"><div class="gq gold" style="top:{w // 2 - 70}px">?</div></div>'
                for x, y, w, r in [(90, 900, 280, -6), (400, 820, 300, 0), (730, 900, 260, 6)])
SMALL = ''.join(f'<div class="sm" style="left:{90 + 320 * j}px">{icon(GIFTS[j][0], 200)}<div class="p">{GIFTS[j][2]}</div></div>' for j in range(3))
BODY = hud('FRANCE · CADEAUX', 'HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('h1', 'TES CADEAUX', None, 'font-size:90px'), ('it gold', 'Hacoo,', None, 'font-size:100px'), ('h1 tq s', 'MOINS CHERS', None, ''), ('it gold', 'avec un seul code.', None, 'font-size:64px')]) + BOXES + '''</div>
  <div class="scene" data-s="1" data-in="right">''' + hd(230, [('h1 tq', 'CADEAU 1 :', '1.0', ''), ('it gold', 'une coque de téléphone,', '1.1', 'font-size:64px')]) + gift_scene(0) + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 tq', 'CADEAU 2 :', '2.0', ''), ('it gold', 'une gourde,', '2.1', '')]) + gift_scene(1) + '''</div>
  <div class="scene" data-s="3" data-in="right">''' + hd(230, [('h1 tq', 'CADEAU 3 :', '3.0', ''), ('it gold', 'des chaussons,', '3.1', '')]) + gift_scene(2) + '''</div>
  <div class="scene" data-s="4" data-in="up">''' + hd(230, [('big gold', '28 €.', '4.0', 'font-size:120px'), ('it gold', 'Et avec le code promo Hacoo', '4.1', 'font-size:58px')]) + SMALL + '''
   <div class="sumt gold" data-g="4.0" data-fx="tick">= 28,00 €</div>
   <div class="chip2" data-g="4.1" data-fx="up"><small>CODE PROMO HACOO :</small><span data-g="4.2" data-fx="type">hzklink</span></div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="rays" style="top:640px"></div>''' + hd(230, [('h1 tq', "PRIX D'EXEMPLE.", '5.1', '')]) + '''
   <div class="oldp" style="top:420px" data-g="5.0" data-fx="fade">28,00 €</div>
   <div class="newp" style="top:580px" data-g="5.0" data-fx="stamp" data-slow="5.0"><div style="font:800 34px Inter;letter-spacing:6px;color:#e9e4da">AVEC LE CODE HACOO</div><div class="gold" style="font:900 200px 'DejaVu Serif',serif;line-height:1.1">24,08 €</div></div>
   <div class="rib" style="top:1000px" data-g="5.0" data-fx="pop">MÊMES 3 CADEAUX</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('big gold', '-14 %', '6.0', 'font-size:120px'), ('h1 s', 'CODE PROMO HACOO', '6.0', ''), ('big gold', 'hzklink', '6.0', 'font-size:130px'), ('it gold', "sur l'appli Hacoo", '6.0', 'font-size:56px')]) + '''
   <div class="pill" style="top:860px;border-color:rgba(46,211,198,.85)" data-g="6.1" data-fx="up"><div class="pin" style="background:#2ed3c6">★</div><div><b>LES LIENS DES ARTICLES TENDANCE</b><span data-g="6.2" data-fx="fade">sont dans ma bio</span></div></div>
   <div class="cond" style="top:1010px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
