import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°1 du 14/11/2026 - style v3 nuit & or, accent ambre, « 3 trouvailles d'hiver, ticket à la fin » :
# bottines 24,90 € + écharpe 12,50 € + chaussettes 7,60 € = 45,00 € -> 38,70 € avec le code promo Hacoo hzklink (-14 %, prix d'exemple).
# Voix : Speko (speechify, voix par défaut).
NAME = 'hacoo22'
TITLE = 'Hacoo trouvailles ambre'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Trois trouvailles d'hiver sur Hacou. Ticket à la fin.", [("3 trouvailles d'hiver", None), ("sur Hacoo.", None), ("Ticket à la fin.", None)]),
 ("Des bottines : vingt-quatre euros quatre-vingt-dix.", [("Des bottines :", None), ("24,90 €.", None)]),
 ("Une écharpe : douze euros cinquante.", [("Une écharpe :", None), ("12,50 €.", None)]),
 ("Des chaussettes : sept euros soixante.", [("Des chaussettes :", None), ("7,60 €.", None)]),
 ("Total : quarante-cinq euros, en prix d'exemple.", [("Total : 45 €,", None), ("en prix d'exemple.", None)]),
 ("Tu tapes le code promo Hacou H Z K link.", [("Tu tapes", None), ("le code promo Hacoo", None), ("hzklink.", None)]),
 ("Trente-huit euros soixante-dix. Moins quatorze pour cent.", [("38,70 €.", None), ("-14 %.", None)]),
 ("Les liens des articles tendance sont dans ma bio.", [("Les liens des articles tendance", None), ("sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 2.23), (2.59, 4.63), (5.06, 6.58), (6.89, 8.40), (9.10, 11.01), (11.48, 13.79), (14.19, 16.59), (17.07, 18.96)]
GSTART = [[0.1, 1.0, 1.65], [2.59, 3.3], [5.06, 5.7], [6.89, 7.56], [9.1, 10.38], [11.48, 11.7, 12.47], [14.19, 15.7], [17.07, 18.5]]
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
.am{color:#ffb352;text-shadow:0 0 18px rgba(255,165,61,.5)}
.pc{position:absolute;width:250px;height:300px;border-radius:20px;background:#f4efe4;box-shadow:0 30px 70px rgba(0,0,0,.7);text-align:center;padding-top:20px}
.pc .bk{width:210px;height:210px;margin:0 auto;border-radius:14px;background:#2a2018;display:flex;align-items:center;justify-content:center;font:900 110px 'DejaVu Serif',serif;color:#ffa53d}
.pc .n{font:800 24px Inter;color:#3a2a1a;margin-top:16px;letter-spacing:2px}
.big2{position:absolute;left:100px;top:640px;width:500px;height:560px;border-radius:30px;background:#f4efe4;box-shadow:0 40px 90px rgba(0,0,0,.75);transform:rotate(-3deg);text-align:center;padding-top:40px}
.big2 .bk{width:420px;height:420px;margin:0 auto;border-radius:22px;background:radial-gradient(circle,#3a2a18,#1c140c);display:flex;align-items:center;justify-content:center}
.big2 .n{font:900 34px Inter;color:#3a2a1a;margin-top:22px;letter-spacing:3px}
.ptag{position:absolute;left:610px;top:820px;width:320px;height:180px;border-radius:20px 60px 60px 20px;background:#ffa53d;color:#1c1008;text-align:center;box-shadow:0 20px 50px rgba(0,0,0,.6);transform:rotate(6deg)}
.ptag:before{content:'';position:absolute;right:16px;top:76px;width:26px;height:26px;border-radius:50%;background:#07060a}
.ptag b{display:block;font:900 54px 'DejaVu Serif',serif;margin-top:42px;white-space:nowrap;margin-right:44px}
.ptag span{font:800 20px Inter;letter-spacing:3px;margin-right:50px}
.thr{position:absolute;left:540px;top:900px;width:110px;height:4px;background:#d9a24c;transform:rotate(-20deg)}
.mini{position:absolute;top:1300px;width:120px;height:120px;border-radius:18px;background:#f4efe4;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 30px rgba(0,0,0,.6)}
.mini.off{opacity:.25}
.field{position:absolute;left:150px;top:760px;width:780px;height:300px;border-radius:30px;background:#151109;border:4px solid #ffa53d;box-shadow:0 0 50px rgba(255,165,61,.3)}
.field .lb{position:absolute;left:40px;top:34px;font:800 28px Inter;letter-spacing:4px;color:#ffb352}
.field .in{position:absolute;left:40px;top:96px;width:700px;height:120px;border-radius:20px;background:#fff;color:#111;font:900 72px 'DejaVu Sans Mono',monospace;line-height:120px;padding-left:34px;white-space:nowrap}
.field .ok{position:absolute;right:40px;top:236px;font:800 26px Inter;color:#7be38f;letter-spacing:2px}
.btn{position:absolute;left:290px;top:1120px;width:500px;height:110px;border-radius:55px;background:#ffa53d;color:#1c1008;text-align:center;font:900 40px Inter;line-height:110px;letter-spacing:3px}
.old{position:absolute;left:0;top:640px;width:1080px;text-align:center;font:900 90px 'DejaVu Serif',serif;color:#8f877a;text-decoration:line-through;text-decoration-color:#e74c3c}
.newp{position:absolute;left:0;top:800px;width:1080px;text-align:center}
.badge{position:absolute;left:390px;top:1000px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle,#4a2c08,#1c1008);border:6px solid #ffa53d;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 0 50px rgba(255,165,61,.45)}
.badge b{font:900 90px 'DejaVu Serif',serif;color:#fff}.badge span{font:800 20px Inter;letter-spacing:3px;color:#ffd9a6}
'''
ITEMS = [('Bottines', 'BOTTINES', '24,90 €'), ('Écharpe', 'ÉCHARPE', '12,50 €'), ('Chaussettes', 'CHAUSSETTES', '7,60 €')]


def item_scene(k):
    nm, lab, pr = ITEMS[k]
    g = f'{k + 1}'
    minis = ''.join(f'<div class="mini{"" if j <= k else " off"}" style="left:{300 + 170 * j}px">{icon(ITEMS[j][0], 100)}</div>' for j in range(3))
    return (f'<div class="big2" data-g="{g}.0" data-fx="up"><div class="bk">{icon(nm, 380)}</div><div class="n">{lab}</div></div>'
            f'<div class="thr" data-g="{g}.1" data-fx="fade"></div><div class="ptag" data-g="{g}.1" data-fx="stamp"><b>{pr}</b><span>PRIX D\'EXEMPLE</span></div>' + minis)


BODY = hud('FRANCE · TROUVAILLES', 'HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('h1', "3 TROUVAILLES D'HIVER", None, 'font-size:70px'), ('it gold', 'sur Hacoo.', None, 'font-size:96px'), ('h1 am s', 'TICKET À LA FIN.', None, '')]) + '''
   <div class="pc" style="left:90px;top:780px;transform:rotate(-8deg)"><div class="bk">?</div><div class="n">N° 1</div></div>
   <div class="pc" style="left:415px;top:740px"><div class="bk">?</div><div class="n">N° 2</div></div>
   <div class="pc" style="left:740px;top:780px;transform:rotate(8deg)"><div class="bk">?</div><div class="n">N° 3</div></div>
   <div class="rcpt" style="left:340px;top:1180px;width:400px;padding:24px 30px 40px;transform:rotate(3deg)"><div class="t">TICKET</div><div class="s">à la fin de la vidéo</div></div></div>
  <div class="scene" data-s="1" data-in="right">''' + hd(230, [('h1', 'DES BOTTINES :', '1.0', ''), ('it gold', '24,90 €.', '1.1', '')]) + item_scene(0) + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1', 'UNE ÉCHARPE :', '2.0', ''), ('it gold', '12,50 €.', '2.1', '')]) + item_scene(1) + '''</div>
  <div class="scene" data-s="3" data-in="right">''' + hd(230, [('h1', 'DES CHAUSSETTES :', '3.0', ''), ('it gold', '7,60 €.', '3.1', '')]) + item_scene(2) + '''</div>
  <div class="scene" data-s="4" data-in="up">''' + hd(230, [('h1', 'TOTAL : 45 €,', '4.0', ''), ('it gold', "en prix d'exemple.", '4.1', '')]) + '''
   <div class="rcpt" style="top:560px;left:240px;width:600px" data-g="4.0" data-fx="up"><div class="t">TICKET HACOO</div><div class="s">prix d'exemple</div><hr>
    <div class="row"><span>Bottines</span><span>24,90 €</span></div><div class="row"><span>Écharpe</span><span>12,50 €</span></div><div class="row"><span>Chaussettes</span><span>7,60 €</span></div><hr>
    <div class="row tot" data-g="4.0" data-fx="tick"><span>TOTAL</span><span>45,00 €</span></div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'TU TAPES', '5.0', ''), ('it gold', 'le code promo Hacoo', '5.1', ''), ('big gold', 'hzklink', '5.2', 'font-size:120px')]) + '''
   <div class="field" style="top:700px" data-g="5.0" data-fx="up"><div class="lb">CODE PROMO HACOO</div><div class="in"><span data-g="5.2" data-fx="type">hzklink</span></div><div class="ok" data-g="5.2" data-fx="fade">✓ CODE APPLIQUÉ</div></div>
   <div class="btn" style="top:1060px" data-g="5.2" data-fx="pop">APPLIQUER</div></div>
  <div class="scene" data-s="6" data-in="pop"><div class="rays" style="top:650px"></div>''' + hd(230, [('h1 am', '-14 %.', '6.1', 'font-size:110px')]) + '''
   <div class="old" style="top:420px" data-g="6.0" data-fx="fade">45,00 €</div>
   <div class="newp" style="top:560px" data-g="6.0" data-fx="stamp" data-slow="6.0"><div style="font:800 34px Inter;letter-spacing:6px;color:#e9e4da">NOUVEAU TOTAL</div><div class="gold" style="font:900 200px 'DejaVu Serif',serif;line-height:1.1">38,70 €</div></div>
   <div class="badge" data-g="6.1" data-fx="pop"><b>-14 %</b><span>CODE HACOO hzklink</span></div></div>
  <div class="scene" data-s="7" data-in="pop">''' + hd(230, [('h1', 'CODE PROMO HACOO', '7.0', ''), ('big gold', 'hzklink', '7.0', 'font-size:150px'), ('it gold', "-14 % sur l'appli Hacoo", '7.0', 'font-size:60px')]) + '''
   <div class="pill" style="top:730px;border-color:rgba(255,165,61,.85)" data-g="7.0" data-fx="up"><div class="pin" style="background:#ffa53d">★</div><div><b>LES LIENS DES ARTICLES TENDANCE</b><span data-g="7.1" data-fx="fade">sont dans ma bio</span></div></div>
   <div class="cond" style="top:880px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
