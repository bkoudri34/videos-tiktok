import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# 3 banques, 11/11/2026 18:00 - style v3 nuit & or, accent émeraude. Plus de 700 € cumulés (770 € max) :
# Hello bank jusqu'à 330 € (80 € + 50 € Hello Prime + 200 € bon d'achat Hello Start +, demande avant le 08/12/2026 ; moneyvox.fr 05/11/2026)
# + Fortuneo jusqu'à 260 € (carte Gold, jusqu'au 20/12/2026 ; top10banques.com 03/11/2026) + BoursoBank jusqu'à 180 € (boursobank.com, consulté le 11/11/2026).
# Trois casiers fermés -> casier Hello bank -> casier Fortuneo -> casier BoursoBank -> addition -> appel à l'action.
NAME = 'trio7'
TITLE = '3 banques emeraude'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Plus de sept cents euros, cachés dans trois banques.", [("Plus de 700 €,", None), ("cachés dans 3 banques.", None)]),
 ("Hello bank : jusqu'à trois cent trente euros, bon d'achat compris.", [("Hello bank :", None), ("jusqu'à 330 €,", None), ("bon d'achat compris.", None)]),
 ("Fortuneo : jusqu'à deux cent soixante euros avec la carte Gold.", [("Fortuneo :", None), ("jusqu'à 260 €", None), ("avec la carte Gold.", None)]),
 ("BoursoBank : jusqu'à cent quatre-vingts euros de bienvenue.", [("BoursoBank :", None), ("jusqu'à 180 €", None), ("de bienvenue.", None)]),
 ("Au total, plus de sept cents euros, selon les conditions.", [("Au total,", None), ("plus de 700 €,", None), ("selon les conditions.", None)]),
 ("Envoie-moi PARRAINAGE en privé, je t'envoie les trois liens.", [("Envoie-moi", None), ("PARRAINAGE", None), ("en privé,", None), ("je t'envoie les 3 liens.", None)]),
]
SPLITS = [(0.0, 2.20), (2.628, 5.455), (5.782, 8.998), (9.275, 11.908), (12.309, 14.81), (15.235, 17.556)]
GSTART = [[0.1, 1.3], [2.63, 3.36, 4.6], [5.79, 6.61, 8.1], [9.28, 10.2, 11.4], [12.31, 13.06, 14.0], [15.24, 15.6, 16.1, 16.6]]
MINLEN = 2.4
GAP = 0.36
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.em{color:#3ddc97;text-shadow:0 0 18px rgba(61,220,151,.45)}
.lk{position:absolute;width:260px;height:340px;border-radius:18px;background:linear-gradient(160deg,#2a241c,#120f0b);border:5px solid #d9a24c;box-shadow:0 30px 70px rgba(0,0,0,.7)}
.lk .no{position:absolute;left:0;top:24px;width:100%;text-align:center;font:700 26px 'DejaVu Sans Mono',monospace;color:#9a917f;letter-spacing:4px}
.lk .q{position:absolute;left:0;top:90px;width:100%;text-align:center;font:900 140px 'DejaVu Serif',serif;color:#3ddc97;text-shadow:0 0 30px rgba(61,220,151,.5)}
.lk .kh{position:absolute;left:105px;top:270px;width:50px;height:50px;border-radius:50%;background:radial-gradient(circle,#fff0c0,#a8701f)}
.box{position:absolute;left:150px;top:720px;width:780px;border-radius:30px;border:4px solid #3ddc97;background:linear-gradient(180deg,rgba(18,40,30,.9),rgba(8,14,11,.92));box-shadow:0 0 60px rgba(61,220,151,.25),0 40px 90px rgba(0,0,0,.7);padding:30px 40px 34px}
.box .tg{font:700 24px 'DejaVu Sans Mono',monospace;letter-spacing:5px;color:#3ddc97}
.box .row{display:flex;justify-content:space-between;align-items:baseline;font:700 36px Inter;color:#f1ead9;border-bottom:2px dashed rgba(217,162,76,.35);padding:18px 0;white-space:nowrap}
.box .row b{font:900 50px 'DejaVu Serif',serif;color:#f3c766}
.box .row small{font:600 24px Inter;color:#9a917f}
.add{position:absolute;left:220px;top:700px;width:640px;background:#f4efe4;color:#1c1712;border-radius:22px;padding:34px 48px 40px;box-shadow:0 40px 90px rgba(0,0,0,.7);transform:rotate(2.5deg)}
.add .r{display:flex;justify-content:space-between;font:700 40px 'DejaVu Sans Mono',monospace;line-height:1.8;white-space:nowrap}
.add hr{border:0;border-top:4px solid #1c1712;margin:14px 0}
.add .t{display:flex;justify-content:space-between;align-items:center;font:900 44px Inter;white-space:nowrap}
.add .t b{font:900 76px 'DejaVu Serif',serif;color:#138a5b}
'''


def box(tag, rows, g0):
    r = ''.join(f'<div class="row" data-g="{g}" data-fx="left"><span>{a}<br><small>{s}</small></span><b>{v}</b></div>' for a, s, v, g in rows)
    return f'<div class="box" data-g="{g0}" data-fx="up"><div class="tg">{tag}</div>{r}</div>'


BODY = hud('FRANCE · 3 BANQUES', 'CUMUL') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('it gold', 'plus de', None, 'font-size:70px'), ('big gold', '700 €', None, 'font-size:190px'), ('h1 s', 'CACHÉS DANS 3 BANQUES', None, 'font-size:60px')]) + '''
   <div class="lk" style="left:120px;top:900px"><div class="no">N° 01</div><div class="q">?</div><div class="kh"></div></div>
   <div class="lk" style="left:410px;top:880px"><div class="no">N° 02</div><div class="q">?</div><div class="kh"></div></div>
   <div class="lk" style="left:700px;top:900px"><div class="no">N° 03</div><div class="q">?</div><div class="kh"></div></div></div>
  <div class="scene" data-s="1" data-in="right">''' + hd(230, [('h1', 'HELLO BANK :', '1.0', ''), ('it gold', "jusqu'à 330 €,", '1.1', 'font-size:88px'), ('it gold', "bon d'achat compris.", '1.2', 'font-size:58px')]) + '''
   ''' + box("CASIER N° 01 · HELLO BANK", [("80 €", "à l'ouverture", "80", "1.1"), ("+ 50 €", "avec Hello Prime", "50", "1.1"), ("+ 200 €", "bon d'achat · Hello Start +", "200", "1.2")], "1.0").replace('top:720px', 'top:760px') + '''</div>
  <div class="scene" data-s="2" data-in="left">''' + hd(230, [('h1', 'FORTUNEO :', '2.0', ''), ('it gold', "jusqu'à 260 €", '2.1', 'font-size:88px'), ('it gold', 'avec la carte Gold.', '2.2', 'font-size:58px')]) + '''
   ''' + box("CASIER N° 02 · FORTUNEO", [("Carte Gold", "après 5 paiements", "160", "2.1"), ("Mobilité", "si tu changes de banque", "80", "2.1"), ("Livret +", "ouvert en même temps", "20", "2.2")], "2.0").replace('top:720px', 'top:760px') + '''</div>
  <div class="scene" data-s="3" data-in="right">''' + hd(230, [('h1', 'BOURSOBANK :', '3.0', ''), ('it gold', "jusqu'à 180 €", '3.1', 'font-size:88px'), ('it gold', 'de bienvenue.', '3.2', 'font-size:58px')]) + '''
   ''' + box("CASIER N° 03 · BOURSOBANK", [("Ouverture", "+ 1er versement", "60", "3.1"), ("Carte", "1 opération / mois, 3 mois", "40", "3.1"), ("EasyMove", "changement de banque", "80", "3.2")], "3.0").replace('top:720px', 'top:760px') + '''</div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:640px"></div>''' + hd(230, [('h1', 'AU TOTAL,', '4.0', ''), ('it gold', 'plus de 700 €,', '4.1', 'font-size:88px'), ('it gold', 'selon les conditions.', '4.2', 'font-size:58px')]) + '''
   <div class="add" data-g="4.0" data-fx="up"><div class="r"><span>Hello bank</span><span>330 €</span></div><div class="r"><span>Fortuneo</span><span>260 €</span></div><div class="r"><span>BoursoBank</span><span>180 €</span></div><hr>
    <div class="t" data-g="4.1" data-fx="stamp" data-slow="4.1"><span>TOTAL MAX</span><b>770 €</b></div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« PARRAINAGE »', '5.1', 'font-size:100px'), ('it gold', 'en privé.', '5.2', '')]) + '''
   <div class="pill" style="top:700px;border-color:rgba(61,220,151,.8)" data-g="5.2" data-fx="up"><div class="pin" style="background:#3ddc97">3</div><div><b>LES 3 LIENS</b><span>Hello bank · Fortuneo · BoursoBank</span></div></div>
   <div class="pill" style="top:825px" data-g="5.3" data-fx="up"><div class="pin">✉</div><div><b>JE T'ENVOIE TOUT</b><span>en privé sur @htm.invest</span></div></div>
   <div class="cond" style="top:975px">Offres soumises aux conditions en vigueur<br>montants maximum, nouveaux clients<br>Hello bank : dont 200 € en bon d'achat, jusqu'au 08/12<br>Fortuneo : carte Gold, jusqu'au 20/12 · BoursoBank : bienvenue</div></div>
'''
