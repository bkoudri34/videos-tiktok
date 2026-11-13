import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°2 du 13/11/2026 - style v3 nuit & or, accent bleu roi, « avant / après le code » en écran partagé :
# mug 9,90 € + bougie 10,10 € = 20,00 € -> 17,20 € avec le code promo Hacoo hzklink (-14 %, prix d'exemple). Voix : Speko (speechify, voix par défaut).
NAME = 'hacoo21'
TITLE = 'Hacoo avant apres bleu roi'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Avant ou après le code Hacou ? Devine.", [("Avant ou après", None), ("le code Hacoo ?", None), ("Devine.", None)]),
 ("Avant : un mug et une bougie, vingt euros.", [("Avant :", None), ("un mug et une bougie,", None), ("20 €.", None)]),
 ("Après le code promo Hacou : H Z K link.", [("Après le code promo Hacoo :", None), ("hzklink.", None)]),
 ("Dix-sept euros vingt. Même panier.", [("17,20 €.", None), ("Même panier.", None)]),
 ("Moins quatorze pour cent, en prix d'exemple.", [("-14 %,", None), ("en prix d'exemple.", None)]),
 ("Les liens des articles tendance sont dans ma bio.", [("Les liens des articles tendance", None), ("sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 2.33), (2.79, 4.88), (5.56, 7.81), (8.07, 9.67), (10.26, 11.89), (12.56, 14.14)]
GSTART = [[0.05, 0.7, 1.9], [2.79, 3.3, 4.4], [5.56, 7.0], [8.07, 9.1], [10.26, 11.3], [12.56, 13.7]]
MINLEN = 2.2
GAP = 0.34
TAIL = 2.2
CSS = '''
.br{color:#7d97ff;text-shadow:0 0 18px rgba(109,139,255,.55)}
.col{position:absolute;top:640px;width:420px;height:820px;border-radius:30px;border:4px solid #d9a24c;background:linear-gradient(180deg,rgba(25,28,48,.85),rgba(10,10,18,.9));text-align:center;overflow:hidden}
.col .h{height:100px;font:900 46px Inter;letter-spacing:6px;line-height:100px;color:#07060a}
.col .q{font:900 220px 'DejaVu Serif',serif;color:rgba(125,151,255,.35);margin-top:150px}
.col .it2{display:flex;justify-content:center;gap:10px;margin-top:40px}
.col .it2 div{width:180px;height:180px;border-radius:26px;background:#141833;border:3px solid #6d8bff;display:flex;align-items:center;justify-content:center}
.col .lb{font:700 22px Inter;color:#cfd6f5;margin-top:22px;white-space:nowrap}
.col .tt{font:900 74px 'DejaVu Serif',serif;margin-top:40px;white-space:nowrap}
.col .st{font:700 24px Inter;letter-spacing:4px;color:#8f877a}
.vs{position:absolute;left:470px;top:960px;width:140px;height:140px;border-radius:50%;background:#6d8bff;color:#07060a;font:900 50px Inter;display:flex;align-items:center;justify-content:center;box-shadow:0 0 40px rgba(109,139,255,.6)}
.chip{position:absolute;left:190px;top:500px;width:700px;height:120px;border-radius:60px;background:#fff;color:#111;display:flex;align-items:center;justify-content:center;gap:20px;font:900 52px 'DejaVu Sans Mono',monospace;white-space:nowrap;border:5px solid #6d8bff;box-shadow:0 30px 70px rgba(0,0,0,.7)}
.chip small{font:800 26px Inter;letter-spacing:3px;color:#3b4fb0}
.pct{position:absolute;left:340px;top:930px;width:400px;height:400px;border-radius:50%;background:radial-gradient(circle,#2a3470,#10132a);border:6px solid #6d8bff;display:flex;flex-direction:column;align-items:center;justify-content:center}
.pct b{font:900 100px 'DejaVu Serif',serif;color:#fff;white-space:nowrap}
.pct span{font:800 24px Inter;letter-spacing:4px;color:#cfd6f5}
'''
L_EMPTY = '<div class="q">?</div>'


def col(x, title, color, inner, g=None, fx='up'):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    return f'<div class="col" style="left:{x}px"{a}><div class="h" style="background:{color}">{title}</div>{inner}</div>'


def filled(total, g=None, slow=False, struck=False):
    a = f' data-g="{g}" data-fx="stamp"' + (f' data-slow="{g}"' if slow else '') if g else ''
    style = ' style="color:#8f877a;text-decoration:line-through;text-decoration-color:#e74c3c"' if struck else ' class="gold"'
    return ('<div class="it2"><div>' + icon('Mug', 150) + '</div><div>' + icon('Bougie', 150) + '</div></div><div class="lb">mug 9,90 € + bougie 10,10 €</div>'
            + f'<div{a}><div class="tt"><span{style}>{total}</span></div><div class="st">PRIX D\'EXEMPLE</div></div>')


BODY = hud('FRANCE · AVANT / APRÈS', 'HACOO') + '''
  <div class="scene" data-s="0">''' + head(220, [('h1', 'AVANT OU APRÈS', None), ('it gold', 'le code Hacoo ?', None), ('h1 br s', 'DEVINE.', None)]).replace('class="it gold"', 'class="it gold" style="font-size:90px"') + col(90, 'AVANT', '#d9a24c', L_EMPTY) + col(570, 'APRÈS', '#6d8bff', L_EMPTY) + '''<div class="vs">VS</div></div>
  <div class="scene" data-s="1" data-in="left">''' + head(230, [('h1', 'AVANT :', '1.0'), ('it gold', 'un mug et une bougie,', '1.1'), ('big gold', '20 €.', '1.2')]).replace('class="it gold"', 'class="it gold" style="font-size:64px"').replace('class="big gold"', 'class="big gold" style="font-size:90px"').replace('top:230px', 'top:210px') + col(90, 'AVANT', '#d9a24c', filled('20,00 €', '1.2'), '1.1') + col(570, 'APRÈS', '#6d8bff', L_EMPTY) + '''</div>
  <div class="scene" data-s="2" data-in="pop">''' + head(230, [('h1 s', 'APRÈS LE CODE PROMO HACOO :', '2.0'), ('big gold', 'hzklink', '2.1')]).replace('class="h1 s"', 'class="h1 s" style="font-size:54px"').replace('class="big gold"', 'class="big gold" style="font-size:140px"') + col(90, 'AVANT', '#d9a24c', filled('20,00 €')) + col(570, 'APRÈS', '#6d8bff', L_EMPTY) + '''
   <div class="chip" data-g="2.0" data-fx="up"><small>CODE HACOO :</small><span data-g="2.1" data-fx="type">hzklink</span></div></div>
  <div class="scene" data-s="3" data-in="right">''' + head(230, [('big gold', '17,20 €.', '3.0'), ('it gold', 'Même panier.', '3.1')]).replace('class="big gold"', 'class="big gold" style="font-size:130px"') + col(90, 'AVANT', '#d9a24c', filled('20,00 €', struck=True)).replace('top:640px', 'top:700px') + col(570, 'APRÈS', '#6d8bff', filled('17,20 €', '3.0', slow=True), '3.0', 'pop').replace('top:640px', 'top:700px') + '''</div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:880px"></div>''' + head(230, [('big gold', '-14 %,', '4.0'), ('it gold', "en prix d'exemple.", '4.1')]).replace('class="big gold"', 'class="big gold" style="font-size:150px"') + '''
   <div class="abs" style="left:90px;top:700px;width:900px;display:flex;justify-content:space-between;font:900 80px 'DejaVu Serif',serif;white-space:nowrap"><span style="color:#8f877a">20,00 €</span><span class="br">→</span><span class="gold">17,20 €</span></div>
   <div class="pct" data-g="4.0" data-fx="stamp"><b>-14 %</b><span>CODE HACOO hzklink</span></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', 'CODE PROMO HACOO', '5.0'), ('big gold', 'hzklink', '5.0'), ('it gold', "-14 % sur l'appli Hacoo", '5.0')]).replace('class="big gold"', 'class="big gold" style="font-size:150px"').replace('class="it gold"', 'class="it gold" style="font-size:60px"') + '''
   <div class="pill" style="top:730px;border-color:rgba(109,139,255,.85)" data-g="5.0" data-fx="up"><div class="pin" style="background:#6d8bff">★</div><div><b>LES LIENS DES ARTICLES TENDANCE</b><span data-g="5.1" data-fx="fade">sont dans ma bio</span></div></div>
   <div class="cond" style="top:880px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
