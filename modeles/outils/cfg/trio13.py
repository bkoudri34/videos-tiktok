import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# 3 banques, 21/11/2026 18:00 - style v3 nuit & or, accent bleu saphir. Format F8 « résultat d'abord » :
# tour des 3 primes cumulées « + de 700 € » dès la 1re image -> BoursoBank 260 € (jauge 260) -> Fortuneo 260 € (jauge 520)
# -> Hello bank 330 € dont 200 € en bon d'achat (jauge 850) -> total 850 € (ralenti) -> appel à l'action.
# Hello bank jusqu'à 330 € d'avantages pour le filleul (80 € + 50 € Hello Prime + bon d'achat 200 € mobilité Hello Start+),
#   avant le 30/11/2026 à 15h (hellobank.fr/fr/votre-offre-parrainage, consultée le 21/11/2026)
# + BoursoBank jusqu'à 260 € pour le filleul (boursobank.com/bon-plan/parrainage-boursobank, consultée le 21/11/2026)
# + Fortuneo jusqu'à 260 € avec la carte Gold, jusqu'au 20/12/2026 (moneyvox.fr, article du 12/11/2026, consulté le 21/11/2026).
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'trio13'
TITLE = '3 banques jauge saphir'
ROOT = ':root{--bg:#05070c}'
LINES = [
 ("Parrainage banque : voilà plus de sept cents euros, en cumulé.", [("Parrainage banque :", None), ("voilà + de 700 €", None), ("en cumulé.", None)]),
 ("Bourso Bank : jusqu'à deux cent soixante euros pour le filleul.", [("BoursoBank :", None), ("jusqu'à 260 €", None), ("pour le filleul.", None)]),
 ("Fortunéo : jusqu'à deux cent soixante euros avec la carte Gold.", [("Fortuneo :", None), ("jusqu'à 260 €", None), ("avec la carte Gold.", None)]),
 ("Hello bank : jusqu'à trois cent trente euros d'avantages, avant le trente novembre.", [("Hello bank :", None), ("jusqu'à 330 € d'avantages,", None), ("avant le 30 novembre.", None)]),
 ("Trois comptes, trois primes : jusqu'à huit cent cinquante euros, sous conditions.", [("3 comptes, 3 primes :", None), ("jusqu'à 850 €,", None), ("sous conditions.", None)]),
 ("Envoie-moi PARRAINAGE en privé, je t'envoie les trois liens.", [("Envoie-moi", None), ("PARRAINAGE", None), ("en privé,", None), ("je t'envoie les 3 liens.", None)]),
]
SPLITS = [(0.0, 2.95), (3.59, 6.1), (6.63, 9.59), (10.19, 13.51), (14.03, 17.54), (18.05, 19.85)]
GSTART = [[0.0, 1.0, 2.5], [3.59, 4.3, 5.7], [6.63, 7.5, 8.8], [10.19, 11.0, 12.8], [14.03, 15.5, 16.9], [18.05, 18.3, 18.7, 19.1]]
MINLEN = 2.0
GAP = 0.32
TAIL = 2.1


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.sa{color:#7fb2ff;text-shadow:0 0 18px rgba(80,140,255,.55)}
.tower{position:absolute;left:220px;top:760px;width:640px}
.tower .b{height:170px;margin-bottom:18px;border-radius:30px;display:flex;align-items:center;justify-content:space-between;padding:0 44px;font:800 46px Inter;white-space:nowrap;color:#eef3ff}
.tower .b b{font:900 76px 'DejaVu Serif',serif}
.b1{background:#13213d;border:4px solid #4a78c8}
.b2{background:#1b1630;border:4px solid #7d6bd0}
.b3{background:#2a2110;border:4px solid #e0ac55}
.tower .ex{display:block;text-align:center;font:700 24px Inter;color:#8fa3c8;letter-spacing:3px;margin-top:10px}
.bkc{position:absolute;left:190px;top:720px;width:700px;height:300px;border-radius:40px;background:linear-gradient(160deg,#121d33,#070b14);border:5px solid #7fb2ff;text-align:center;box-shadow:0 30px 80px rgba(0,0,0,.7),0 0 50px rgba(80,140,255,.25)}
.bkc .n{margin-top:40px;font:900 64px Inter;color:#eef3ff;letter-spacing:4px;white-space:nowrap}
.bkc .v{font:900 120px 'DejaVu Serif',serif;line-height:1.15;white-space:nowrap}
.bkc .s{position:absolute;left:0;right:0;bottom:-58px;font:700 30px Inter;color:#a9bde0;white-space:nowrap}
.gauge{position:absolute;left:150px;top:1150px;width:780px}
.gauge .t{display:flex;justify-content:space-between;font:800 30px Inter;color:#a9bde0;letter-spacing:2px;margin-bottom:14px;white-space:nowrap}
.gauge .t b{color:#f3c766;font:900 38px 'DejaVu Serif',serif}
.gauge .tr{height:50px;border-radius:25px;background:#0f1626;border:3px solid #2b3a5a;overflow:hidden;position:relative}
.gauge .f{position:absolute;left:0;top:0;bottom:0;border-radius:25px;background:linear-gradient(90deg,#3d6fd0,#7fb2ff 60%,#f3c766);transform-origin:0 50%}
.gauge .f0{position:absolute;left:0;top:0;bottom:0;border-radius:25px;background:#3a5590}
.stk{position:absolute;left:190px;width:700px}
.stk .r{height:100px;border-radius:28px;background:#0d1422;border:4px solid #2b3a5a;margin-bottom:16px;display:flex;align-items:center;justify-content:space-between;padding:0 40px;font:800 38px Inter;color:#eef3ff;white-space:nowrap}
.stk .r b{font:900 52px 'DejaVu Serif',serif;color:#7fb2ff}
.tot{position:absolute;left:0;width:1080px;text-align:center}
.tot .v{font:900 200px 'DejaVu Serif',serif;line-height:1}
.cal{position:absolute;left:300px;width:480px;height:100px;border-radius:24px;background:#eef3ff;color:#0e1a33;display:flex;align-items:center;justify-content:center;font:900 40px Inter;white-space:nowrap;box-shadow:0 0 0 5px #4a78c8}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'


def gauge(prev, now, g):
    p0 = round(780 * prev / 850); p1 = round(780 * now / 850)
    return (f'<div class="gauge"><div class="t"><span>CUMUL</span><b data-g="{g}" data-fx="pop">{now} € / 850 €</b></div><div class="tr">'
            f'<div class="f" style="width:{p1}px" data-g="{g}" data-fx="grow"></div><div class="f0" style="width:{p0}px"></div></div></div>')


def bkc(name, val, sub, gi):
    return (f'<div class="bkc" data-g="{gi}.0" data-fx="pop"><div class="n">{name}</div>'
            f'<div class="v gold" data-g="{gi}.1" data-fx="stamp">{val}</div><div class="s" data-g="{gi}.2" data-fx="fade">{sub}</div></div>')


BODY = hud('FRANCE · 3 COMPTES', 'PARRAINAGE') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(205, [('h1 sa', 'PARRAINAGE BANQUE :', None, 'font-size:66px'), ('big gold', 'voilà + de 700 €', None, 'font-size:96px'), ('it gold', 'en cumulé.', None, 'font-size:76px')]) + '''
   <div class="tower" style="top:640px"><div class="b b3">Hello bank<b>330 €</b></div><div class="b b2">Fortuneo<b>260 €</b></div><div class="b b1">BoursoBank<b>260 €</b></div>
    <span class="ex">MAXIMUM CUMULÉ · SOUS CONDITIONS</span></div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1 sa', 'BOURSOBANK :', '1.0', 'font-size:70px'), ('it gold', "jusqu'à 260 €", '1.1', 'font-size:84px'), ('it gold', 'pour le filleul.', '1.2', 'font-size:70px')]) + '''
   ''' + bkc('BOURSOBANK', '260 €', '20 + 80 + 80 + 80 € · 4 étapes', 1) + gauge(0, 260, '1.1') + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 sa', 'FORTUNEO :', '2.0', 'font-size:70px'), ('it gold', "jusqu'à 260 €", '2.1', 'font-size:84px'), ('it gold', 'avec la carte Gold.', '2.2', 'font-size:70px')]) + '''
   ''' + bkc('FORTUNEO', '260 €', 'carte Gold · avant le 20/12', 2) + gauge(260, 520, '2.1') + '''</div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('h1 sa', 'HELLO BANK :', '3.0', 'font-size:70px'), ('it gold', "jusqu'à 330 € d'avantages,", '3.1', 'font-size:70px'), ('it gold', 'avant le 30 novembre.', '3.2', 'font-size:70px')]) + '''
   ''' + bkc('HELLO BANK', '330 €', "dont 200 € en bon d'achat", 3) + gauge(520, 850, '3.1') + '''</div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:860px"></div>''' + hd(215, [('h1 sa', '3 COMPTES, 3 PRIMES :', '4.0', 'font-size:64px')]) + '''
   <div class="stk" style="top:360px"><div class="r" data-g="4.0" data-fx="left">BoursoBank<b>260 €</b></div><div class="r" data-g="4.0" data-fx="right">Fortuneo<b>260 €</b></div><div class="r" data-g="4.0" data-fx="left">Hello bank<b>330 €</b></div></div>
   <div class="hd" style="top:730px"><div class="it gold" style="font-size:74px" data-g="4.1" data-fx="tw">jusqu'à</div></div>
   <div class="tot" style="top:830px" data-g="4.1" data-fx="stamp" data-slow="4.1" data-count="850"><div class="v gold">0 €</div></div>
   <div class="hd" style="top:1060px"><div class="it gold" style="font-size:66px" data-g="4.2" data-fx="tw">sous conditions.</div></div>
   <div class="cond" style="top:1180px;font-size:28px;color:#a9bde0" data-g="4.2" data-fx="fade">montants maximum · 1re ouverture dans chaque banque</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« PARRAINAGE »', '5.1', 'font-size:100px'), ('it gold', 'en privé,', '5.2', '')]) + '''
   <div class="pill" style="top:760px;border-color:rgba(80,140,255,.85)" data-g="5.3" data-fx="up"><div class="pin" style="background:#3d6fd0;color:#fff">✉</div><div><b>JE T'ENVOIE LES 3 LIENS</b><span>directement en message privé</span></div></div>
   <div class="search" style="top:900px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1040px;font-size:22px">Offres soumises aux conditions en vigueur · nouveaux clients<br>Hello bank : jusqu'à 330 € d'avantages dont 200 € en bon d'achat, avant le 30/11 ·<br>BoursoBank : jusqu'à 260 € pour le filleul · Fortuneo : jusqu'à 260 € avec la carte Gold, avant le 20/12</div></div>
'''
