import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# 3 banques, 19/11/2026 21:00 - style v3 nuit & or, accent rose framboise. Format F4 « argent laissé sur la table » :
# table avec 3 enveloppes fermées dès la 1re image -> enveloppe 1 Hello bank -> enveloppe 2 BoursoBank -> enveloppe 3 Fortuneo
# -> billets réunis, total 850 € (ralenti) « plus de 700 € en cumulé » -> appel à l'action.
# Hello bank jusqu'à 330 € (80 € + 50 € Hello Prime + 200 € bon d'achat Hello Start+, jusqu'au 08/12/2026 ; moneyvox.fr 13/11/2026)
# + BoursoBank jusqu'à 260 € pour le filleul (20 + 80 + 80 + 80 € EasyMove ; boursobank.com/bon-plan/parrainage-boursobank consultée le 19/11/2026)
# + Fortuneo jusqu'à 260 € avec la carte Gold (offre de bienvenue jusqu'au 20/12/2026 ; selectra.info màj 13/10/2026, consultée le 19/11).
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'trio12'
TITLE = '3 banques enveloppes framboise'
ROOT = ':root{--bg:#0a0608}'
LINES = [
 ("Parrainage banque : plus de sept cents euros laissés sur la table.", [("Parrainage banque :", None), ("plus de 700 €", None), ("laissés sur la table.", None)]),
 ("Enveloppe un : Hello bank, jusqu'à trois cent trente euros, avant le huit décembre.", [("Enveloppe 1 :", None), ("Hello bank,", None), ("jusqu'à 330 €,", None), ("avant le 8 décembre.", None)]),
 ("Enveloppe deux : Bourso Bank, jusqu'à deux cent soixante euros pour le filleul.", [("Enveloppe 2 :", None), ("BoursoBank,", None), ("jusqu'à 260 €", None), ("pour le filleul.", None)]),
 ("Enveloppe trois : Fortunéo, jusqu'à deux cent soixante euros avec la carte Gold.", [("Enveloppe 3 :", None), ("Fortuneo,", None), ("jusqu'à 260 €", None), ("avec la carte Gold.", None)]),
 ("En cumulé : jusqu'à huit cent cinquante euros, sous conditions.", [("En cumulé :", None), ("jusqu'à 850 €,", None), ("sous conditions.", None)]),
 ("Envoie-moi PARRAINAGE en privé, je t'envoie les trois liens.", [("Envoie-moi", None), ("PARRAINAGE", None), ("en privé,", None), ("je t'envoie les 3 liens.", None)]),
]
SPLITS = [(0.0, 2.77), (3.11, 6.56), (6.94, 10.02), (10.38, 14.23), (14.78, 17.67), (18.13, 20.12)]
GSTART = [[0.0, 1.0, 2.0], [3.11, 3.8, 4.5, 5.8], [6.94, 7.7, 8.5, 9.5], [10.38, 11.1, 12.0, 13.4], [14.78, 15.6, 17.0], [18.13, 18.4, 18.8, 19.4]]
MINLEN = 2.0
GAP = 0.32
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.fr{color:#ff7aa2;text-shadow:0 0 18px rgba(255,80,130,.5)}
.table{position:absolute;left:-60px;top:1060px;width:1200px;height:520px;background:linear-gradient(180deg,#3a1f1a,#1c0f0c);border-top:10px solid #5a3226;transform:perspective(900px) rotateX(38deg);transform-origin:50% 0}
.env{position:absolute;width:280px;height:240px;border-radius:14px;background:linear-gradient(180deg,#f3e6d4,#d9c4a8);box-shadow:0 20px 40px rgba(0,0,0,.6);overflow:hidden}
.env:before{content:'';position:absolute;left:0;top:0;border-left:140px solid transparent;border-right:140px solid transparent;border-top:110px solid #c9b08e}
.env .n{position:absolute;left:0;bottom:16px;width:100%;text-align:center;font:900 48px 'DejaVu Serif',serif;color:#7a1d3d}
.env .q{position:absolute;left:0;top:122px;width:100%;text-align:center;font:800 26px Inter;color:#5a3a2a;letter-spacing:2px}
.big3{position:absolute;left:150px;top:700px;width:780px;height:560px}
.big3 .bk{position:absolute;left:0;top:200px;width:780px;height:360px;border-radius:24px;background:linear-gradient(180deg,#f3e6d4,#d9c4a8);box-shadow:0 30px 90px rgba(0,0,0,.7)}
.big3 .bk:before{content:'';position:absolute;left:0;top:0;border-left:390px solid transparent;border-right:390px solid transparent;border-top:170px solid #c9b08e}
.big3 .note{position:absolute;left:70px;top:0;width:640px;height:330px;border-radius:20px;background:linear-gradient(135deg,#fff3f6,#ffd6e2);border:6px solid #ff5c8a;box-shadow:0 0 50px rgba(255,92,138,.35);text-align:center;padding-top:30px}
.big3 .note b{display:block;font:900 44px Inter;color:#3a0f1f;letter-spacing:2px;white-space:nowrap}
.big3 .note .v{font:900 80px 'DejaVu Serif',serif;color:#b0174a;line-height:1.1;white-space:nowrap}
.big3 .note span{display:block;font:700 30px Inter;color:#5a2a3a;white-space:nowrap}
.mini{position:absolute;top:1370px;height:84px;border-radius:42px;background:#ff5c8a;color:#fff;font:800 34px Inter;display:flex;align-items:center;padding:0 30px;white-space:nowrap;left:0;right:0;margin:0 auto;width:max-content}
.dots{position:absolute;left:0;top:1300px;width:1080px;display:flex;justify-content:center;gap:24px}
.dots i{width:44px;height:44px;border-radius:50%;border:4px solid #ff5c8a}
.dots i.on{background:#ff5c8a;box-shadow:0 0 20px rgba(255,92,138,.8)}
.bills{position:absolute;left:190px;top:560px;width:700px}
.bills .r{height:120px;border-radius:20px;margin-bottom:20px;background:linear-gradient(90deg,#3a2a1c,#241810);border:4px solid #c9a35a;display:flex;align-items:center;justify-content:space-between;padding:0 40px;font:800 40px Inter;color:#f1ead9;white-space:nowrap}
.bills .r b{font:900 58px 'DejaVu Serif',serif;color:#f3c766}
.tot{position:absolute;left:0;width:1080px;text-align:center}
.tot .v{font:900 200px 'DejaVu Serif',serif;line-height:1}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'


def env(left, top, n, rot):
    return f'<div class="env" style="left:{left}px;top:{top}px;transform:rotate({rot}deg)"><div class="q">PRIME</div><div class="n">{n}</div></div>'


def big(sid, n, bank, amt, det, chip):
    dots = ''.join(f'<i class="{"on" if i < n else ""}"></i>' for i in range(3))
    return f'''<div class="big3"><div class="bk"></div><div class="note" data-g="{sid}.1" data-fx="up"><b>{bank}</b><div class="v">{amt}</div><span>{det}</span></div></div>
   <div class="dots">{dots}</div><div class="mini" data-g="{sid}.3" data-fx="fade">{chip}</div>'''


BODY = hud('FRANCE · SUR LA TABLE', '3 ENVELOPPES') + '''
  <div class="scene" data-s="0"><div class="table"></div>''' + hd(210, [('h1 fr', 'PARRAINAGE BANQUE :', None, 'font-size:74px'), ('big gold', 'plus de 700 €', None, 'font-size:120px'), ('it gold', 'laissés sur la table.', None, 'font-size:76px')]) + \
    env(90, 840, '1', -8) + env(400, 800, '2', 3) + env(710, 850, '3', 9) + '''</div>
  <div class="scene" data-s="1" data-in="up">''' + hd(215, [('h1 fr', 'ENVELOPPE 1 :', '1.0', ''), ('h1', 'HELLO BANK,', '1.1', ''), ('it gold', 'avant le 8 décembre.', '1.3', 'font-size:66px')]) + big(1, 1, 'HELLO BANK', "jusqu'à 330 €", "80 € + 50 € + 200 € en bon d'achat", 'avant le 08/12') + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + hd(215, [('h1 fr', 'ENVELOPPE 2 :', '2.0', ''), ('h1', 'BOURSOBANK,', '2.1', ''), ('it gold', 'pour le filleul.', '2.3', 'font-size:66px')]) + big(2, 2, 'BOURSOBANK', "jusqu'à 260 €", '20 € + 80 € + 80 € + 80 €', 'offre de parrainage') + '''</div>
  <div class="scene" data-s="3" data-in="left">''' + hd(215, [('h1 fr', 'ENVELOPPE 3 :', '3.0', ''), ('h1', 'FORTUNEO,', '3.1', ''), ('it gold', 'avec la carte Gold.', '3.3', 'font-size:66px')]) + big(3, 3, 'FORTUNEO', "jusqu'à 260 €", 'carte Gold, sous conditions de revenus', 'avant le 20/12') + '''</div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:930px"></div>''' + hd(215, [('h1 fr', 'EN CUMULÉ :', '4.0', ''), ('it gold', 'sous conditions.', '4.2', 'font-size:66px')]) + '''
   <div class="bills" style="top:430px"><div class="r" data-g="4.0" data-fx="left">Hello bank<b>330 €</b></div><div class="r" data-g="4.0" data-fx="right">BoursoBank<b>260 €</b></div><div class="r" data-g="4.1" data-fx="left">Fortuneo<b>260 €</b></div></div>
   <div class="tot" style="top:880px" data-g="4.1" data-fx="stamp" data-slow="4.1" data-count="850"><div class="v gold">0 €</div></div>
   <div class="cond" style="top:1110px;font-size:34px;color:#ffb3c8" data-g="4.2" data-fx="up">jusqu'à 850 € au total : plus de 700 € en cumulé</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« PARRAINAGE »', '5.1', 'font-size:88px'), ('it gold', 'en privé,', '5.2', '')]) + '''
   <div class="pill" style="top:800px;border-color:rgba(255,92,138,.85)" data-g="5.3" data-fx="up"><div class="pin" style="background:#ff5c8a;color:#fff">3</div><div><b>JE T'ENVOIE LES 3 LIENS</b><span>Hello bank · BoursoBank · Fortuneo</span></div></div>
   <div class="search" style="top:940px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1080px">Offres soumises aux conditions en vigueur · montants maximum, nouveaux clients<br>Hello bank : jusqu'à 330 € dont 200 € en bon d'achat, jusqu'au 08/12<br>BoursoBank : jusqu'à 260 € pour le filleul (offre de parrainage)<br>Fortuneo : jusqu'à 260 € avec la carte Gold (revenus ≥ 2 200 €/mois), jusqu'au 20/12</div></div>
'''
