import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°2 du 15/11/2026 - style v3 nuit & or, accent cuivre, « avant / après le code » en deux colonnes :
# doudoune 32,00 € + gants 6,00 € = 38,00 € -> 32,68 € avec le code promo Hacoo hzklink (-14 %, 5,32 € d'économie, prix d'exemple).
# Voix : Speko (speechify, voix par défaut ; voix clonée refusée 402).
NAME = 'hacoo25'
TITLE = 'Hacoo avant apres cuivre'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Avant ou après le code Hacou ? Regarde la différence.", [("Avant ou après", None), ("le code Hacoo ?", None), ("Regarde la différence.", None)]),
 ("Une doudoune et des gants : trente-huit euros, prix d'exemple.", [("Une doudoune et des gants :", None), ("38 €,", None), ("prix d'exemple.", None)]),
 ("Maintenant, le code promo Hacou H Z K link.", [("Maintenant,", None), ("le code promo Hacoo", None), ("hzklink.", None)]),
 ("Après : trente-deux euros soixante-huit.", [("Après :", None), ("32,68 €.", None)]),
 ("Cinq euros trente-deux d'économie, soit moins quatorze pour cent.", [("5,32 € d'économie,", None), ("soit -14 %.", None)]),
 ("Les liens des articles tendance sont dans ma bio.", [("Les liens des articles tendance", None), ("sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 2.85), (3.08, 5.33), (5.89, 8.43), (8.78, 10.57), (10.96, 13.50), (14.12, 15.93)]
GSTART = [[0.1, 0.7, 1.95], [3.1, 4.1, 4.8], [5.89, 6.4, 7.6], [8.78, 9.5], [10.96, 12.4], [14.12, 15.4]]
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
.cu{color:#ff9a66;text-shadow:0 0 18px rgba(232,131,79,.5)}
.col{position:absolute;top:640px;width:380px;height:760px;border-radius:30px;box-sizing:border-box;padding:28px 24px;text-align:center}
.col.av{left:90px;background:#1a1612;border:4px solid #5b544a}
.col.ap{left:530px;background:#221208;border:4px solid #e8834f;box-shadow:0 0 50px rgba(232,131,79,.3)}
.col .h{font:900 44px Inter;letter-spacing:6px;color:#e9e4da}
.col.ap .h{color:#ff9a66}
.col .sb{font:700 22px Inter;letter-spacing:3px;color:#9a917f;margin-top:4px}
.col .ics{display:flex;justify-content:center;gap:10px;margin-top:30px}
.col .ic{width:150px;height:150px;border-radius:22px;background:#f4efe4;display:flex;align-items:center;justify-content:center}
.col .l{font:700 26px Inter;color:#cfc7b8;margin-top:14px;white-space:nowrap}
.col .p{font:900 76px 'DejaVu Serif',serif;margin-top:60px;white-space:nowrap}
.col.av .p{color:#e9e4da}
.col .q{font:900 150px 'DejaVu Serif',serif;color:#5b544a;margin-top:120px}
.col .x{font:700 22px Inter;letter-spacing:3px;color:#9a917f;margin-top:6px}
.vs{position:absolute;left:470px;top:960px;width:60px;text-align:center;font:900 italic 44px 'Liberation Serif',serif;color:#f3c766}
.chip2{position:absolute;left:190px;width:700px;height:120px;border-radius:60px;background:#120a05;border:4px solid #e8834f;display:flex;align-items:center;gap:22px;padding:0 34px;box-sizing:border-box;white-space:nowrap}
.chip2 .k{font:800 26px Inter;letter-spacing:3px;color:#ff9a66}
.chip2 .c{font:900 60px 'DejaVu Sans Mono',monospace;color:#fff}
.sav{position:absolute;left:190px;top:700px;width:700px;height:300px;border-radius:30px;background:linear-gradient(135deg,#ffc29a,#e8834f);color:#2a1206;text-align:center;box-shadow:0 30px 80px rgba(0,0,0,.6);transform:rotate(-3deg)}
.sav .k{font:800 26px 'DejaVu Sans Mono',monospace;letter-spacing:6px;margin-top:40px}
.sav .a{font:900 130px 'DejaVu Serif',serif;line-height:1.15}
.ring{position:absolute;left:390px;top:1100px;width:300px;height:300px;border-radius:50%;border:6px solid #e8834f;display:flex;flex-direction:column;align-items:center;justify-content:center;background:radial-gradient(circle,#3a1c0c,#120a05)}
.ring b{font:900 92px 'DejaVu Serif',serif;color:#fff}.ring span{font:800 20px Inter;letter-spacing:3px;color:#ffc29a}
'''


def cols(left_p=None, right=None, g_left=None, g_right=None, slow=False):
    ics = f'<div class="ics"><div class="ic">{icon("Doudoune", 130)}</div></div><div class="ics" style="margin-top:12px"><div class="ic" style="width:110px;height:110px">{icon("Gants", 96)}</div></div>'
    gl = f' data-g="{g_left}" data-fx="stamp"' if g_left else ''
    lp = f'<div class="p"{gl}>{left_p}</div><div class="x">PRIX D\'EXEMPLE</div>' if left_p else '<div class="p" style="color:#5b544a">…</div>'
    if right:
        gr = f' data-g="{g_right}" data-fx="stamp"' + (f' data-slow="{g_right}"' if slow else '') if g_right else ''
        rp = ics + f'<div class="p gold"{gr}>{right}</div><div class="x">CODE HACOO hzklink</div>'
    else:
        rp = '<div class="q">?</div><div class="x">CODE PROMO HACOO</div>'
    return (f'<div class="col av"><div class="h">AVANT</div><div class="sb">SANS CODE</div>{ics}{lp}</div>'
            f'<div class="vs">vs</div>'
            f'<div class="col ap"><div class="h">APRÈS</div><div class="sb">AVEC LE CODE</div>{rp}</div>')


BODY = hud('FRANCE · AVANT / APRÈS', 'HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('h1', 'AVANT OU APRÈS', None, ''), ('it gold', 'le code Hacoo ?', None, 'font-size:84px'), ('h1 cu s', 'REGARDE LA DIFFÉRENCE.', None, 'font-size:56px')]) + cols() + '''</div>
  <div class="scene" data-s="1" data-in="left">''' + hd(230, [('h1 s', 'UNE DOUDOUNE ET DES GANTS :', '1.0', 'font-size:50px'), ('it gold', '38 €,', '1.1', 'font-size:90px'), ('it gold', "prix d'exemple.", '1.2', 'font-size:70px')]) + cols('38,00 €', None, '1.1') + '''</div>
  <div class="scene" data-s="2" data-in="up">''' + hd(230, [('h1 cu', 'MAINTENANT,', '2.0', ''), ('it gold', 'le code promo Hacoo', '2.1', 'font-size:80px'), ('big gold', 'hzklink.', '2.2', 'font-size:110px')]) + '''
   <div class="chip2" style="top:760px" data-g="2.0" data-fx="up"><span class="k">CODE PROMO HACOO</span><span class="c" data-g="2.2" data-fx="type">hzklink</span></div>
   <div class="abs" style="left:0;top:940px;width:1080px;text-align:center;font:800 30px Inter;letter-spacing:4px;color:#e9e4da" data-g="2.2" data-fx="fade">-14 % SUR L'APPLI HACOO</div></div>
  <div class="scene" data-s="3" data-in="pop"><div class="rays" style="top:700px;left:450px"></div>''' + hd(230, [('h1 cu', 'APRÈS :', '3.0', 'font-size:96px'), ('it gold', '32,68 €.', '3.1', 'font-size:90px')]) + cols('38,00 €', '32,68 €', None, '3.1', True) + '''</div>
  <div class="scene" data-s="4" data-in="right">''' + hd(230, [('it gold', "5,32 € d'économie,", '4.0', 'font-size:84px'), ('h1 cu', 'SOIT -14 %.', '4.1', 'font-size:96px')]) + '''
   <div class="sav" data-g="4.0" data-fx="up"><div class="k">ÉCONOMIE</div><div class="a">5,32 €</div></div>
   <div class="ring" data-g="4.1" data-fx="stamp"><b>-14 %</b><span>CODE hzklink</span></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'CODE PROMO HACOO', '5.0', ''), ('big gold', 'hzklink', '5.0', 'font-size:150px'), ('it gold', "-14 % sur l'appli Hacoo", '5.0', 'font-size:60px')]) + '''
   <div class="pill" style="top:730px;border-color:rgba(232,131,79,.85)" data-g="5.0" data-fx="up"><div class="pin" style="background:#e8834f">★</div><div><b>LES LIENS DES ARTICLES TENDANCE</b><span data-g="5.1" data-fx="fade">sont dans ma bio</span></div></div>
   <div class="cond" style="top:880px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
