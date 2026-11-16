import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# 3 banques, 16/11/2026 18:00 - style v3 nuit & or, accent rouge corail. Plus de 700 € cumulés (770 € max) :
# Hello bank jusqu'à 330 € (80 € + 50 € Hello Prime + 200 € bon d'achat Hello Start +, demande validée au plus tard le 08/12/2026 ; moneyvox.fr 05/11/2026)
# + Fortuneo jusqu'à 260 € (carte Gold : 160 € + 80 € mobilité + 20 € Livret +, jusqu'au 20/12/2026 ; selectra.info, moneyvox.fr)
# + BoursoBank jusqu'à 180 € pour le filleul (boursobank.com, page parrainage consultée le 16/11/2026, pas de date de fin).
# Voix : Speko (speechify, voix par défaut ; voix clonée refusée 402), dernière réplique refaite seule (« le mot parrainage »).
# Carte routière avec 3 étapes (repères numérotés qui s'allument un par un) -> bocal qui se remplit en 3 couches (770 €, ralenti) -> appel à l'action.
NAME = 'trio10'
TITLE = '3 banques corail'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Plus de sept cents euros de primes. Voici le plan.", [("Plus de 700 €", None), ("de primes.", None), ("Voici le plan.", None)]),
 ("Un : Hello bank, jusqu'à trois cent trente euros, avant le huit décembre.", [("Un :", None), ("Hello bank,", None), ("jusqu'à 330 €,", None), ("avant le 8 décembre.", None)]),
 ("Deux : Fortunéo, jusqu'à deux cent soixante euros, avant le vingt décembre.", [("Deux :", None), ("Fortuneo,", None), ("jusqu'à 260 €,", None), ("avant le 20 décembre.", None)]),
 ("Trois : Bourso Bank, jusqu'à cent quatre-vingts euros.", [("Trois :", None), ("BoursoBank,", None), ("jusqu'à 180 €.", None)]),
 ("Le bocal se remplit : sept cent soixante-dix euros au maximum.", [("Le bocal se remplit :", None), ("770 €", None), ("au maximum.", None)]),
 ("Envoie-moi le mot parrainage en privé, je t'envoie les trois liens.", [("Envoie-moi", None), ("le mot", None), ("PARRAINAGE", None), ("en privé,", None), ("je t'envoie les 3 liens.", None)]),
]
SPLITS = [(0.0, 2.45), (3.03, 6.45), (7.00, 10.55), (11.06, 13.34), (13.94, 16.67), (17.47, 20.09)]
GSTART = [[0.1, 1.2, 1.9], [3.05, 3.7, 4.4, 5.7], [7.0, 7.6, 8.3, 9.7], [11.1, 11.6, 12.3], [13.94, 15.0, 16.2], [17.5, 17.8, 18.0, 18.7, 19.4]]
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
.co{color:#ff8a7a;text-shadow:0 0 18px rgba(255,107,90,.5)}
.map{position:absolute;left:110px;top:760px;width:820px;height:700px;border-radius:30px;background:#14100d;border:4px solid rgba(217,162,76,.55);box-shadow:0 30px 80px rgba(0,0,0,.7);overflow:hidden}
.map:before{content:'';position:absolute;inset:0;background:linear-gradient(rgba(217,162,76,.08) 2px,transparent 2px) 0 0/100% 60px,linear-gradient(90deg,rgba(217,162,76,.08) 2px,transparent 2px) 0 0/60px 100%}
.road{position:absolute;left:118px;top:40px;width:0;height:620px;border-left:8px dashed rgba(217,162,76,.6)}
.pinp{position:absolute;left:70px;width:104px;height:104px;border-radius:50%;background:#2a241c;border:5px solid #8a7f69;color:#9a917f;font:900 54px Inter;display:flex;align-items:center;justify-content:center}
.pinp.on{background:#ff6b5a;border-color:#f3c766;color:#fff;box-shadow:0 0 40px rgba(255,107,90,.7)}
.pinp.done{background:#5a2a24;border-color:#d9a24c;color:#f3c766}
.stp{position:absolute;left:210px;width:570px;height:170px;border-radius:24px;background:rgba(255,255,255,.04);border:3px solid rgba(255,255,255,.08);padding:20px 28px;white-space:nowrap}
.stp.on{background:rgba(255,107,90,.14);border-color:#ff6b5a}
.stp.done{opacity:.6}
.stp b{display:block;font:900 44px Inter;color:#fff}
.stp .a{font:900 54px 'DejaVu Serif',serif}
.stp small{font:700 26px Inter;color:#ff8a7a;letter-spacing:2px;margin-left:14px}
.stp.off b{color:#5b544a}
.jar{position:absolute;left:330px;top:720px;width:420px;height:620px}
.jar .neck{position:absolute;left:70px;top:0;width:280px;height:60px;border-radius:14px;background:#2c2925;border:5px solid #d9a24c}
.jar .gl{position:absolute;left:0;top:50px;width:420px;height:570px;border-radius:60px 60px 70px 70px;border:6px solid rgba(240,230,210,.6);background:rgba(255,255,255,.04);overflow:hidden;box-shadow:inset 0 0 40px rgba(255,255,255,.08)}
.lay{position:absolute;left:0;width:100%;transform-origin:50% 100%;font:900 34px Inter;color:#1a0e0b;display:flex;align-items:center;justify-content:center;white-space:nowrap}
.jl{position:absolute;left:790px;font:800 30px Inter;color:#e9e4da;white-space:nowrap}
.jl b{display:block;font:900 40px 'DejaVu Serif',serif}
.tot7{position:absolute;left:0;top:1360px;width:1080px;text-align:center}
.tot7 .v{font:900 150px 'DejaVu Serif',serif;line-height:1}
.fold{position:absolute;left:150px;top:900px;width:780px;height:480px;display:flex;transform:rotate(-3deg)}
.fold div{flex:1;background:#1a1510;border:3px solid rgba(217,162,76,.5)}
.fold div:nth-child(2){background:#221b14;transform:skewY(-4deg)}
.fold .q{position:absolute;width:110px;height:110px;border-radius:50%;background:#ff6b5a;color:#fff;font:900 64px Inter;display:flex;align-items:center;justify-content:center;border:5px solid #f3c766}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
STEPS = [('Hello bank', "jusqu'à 330 €", 'avant le 08/12'), ('Fortuneo', "jusqu'à 260 €", 'avant le 20/12'), ('BoursoBank', "jusqu'à 180 €", 'parrainage')]
PY = [60, 280, 500]


def roadmap(k, sid):
    out = '<div class="map"><div class="road"></div>'
    for i, (b, a, d) in enumerate(STEPS):
        if i < k:
            pc, sc, ga, gb = 'pinp done', 'stp done', '', ''
        elif i == k:
            pc, sc = 'pinp on', 'stp on'
            ga = f' data-g="{sid}.0" data-fx="stamp"'
            gb = f' data-g="{sid}.1" data-fx="right"'
        else:
            pc, sc, ga, gb = 'pinp', 'stp off', '', ''
        out += f'<div class="{pc}" style="top:{PY[i] + 30}px"{ga}>{i + 1}</div>'
        if i <= k:
            out += f'<div class="{sc}" style="top:{PY[i]}px"{gb}><b>{b}<small>{d}</small></b><span class="a gold">{a}</span></div>'
        else:
            out += f'<div class="{sc}" style="top:{PY[i]}px"><b>étape {i + 1}</b></div>'
    return out + '</div>'


BODY = hud('FRANCE · 3 BANQUES', 'LE PLAN') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(210, [('it gold', 'Plus de', None, 'font-size:64px'), ('big gold', '700 €', None, 'font-size:170px'), ('h1', 'DE PRIMES.', None, ''), ('it co', 'Voici le plan.', None, 'font-size:72px')]) + '''
   <div class="fold"><div></div><div></div><div></div><div class="q" style="left:90px;top:80px">1</div><div class="q" style="left:340px;top:220px">2</div><div class="q" style="left:590px;top:110px">3</div></div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1 co', 'UN :', '1.0', 'font-size:90px'), ('h1', 'HELLO BANK,', '1.1', ''), ('it gold', "jusqu'à 330 €,", '1.2', 'font-size:72px'), ('it gold', 'avant le 8 décembre.', '1.3', 'font-size:64px')]) + roadmap(0, 1) + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 co', 'DEUX :', '2.0', 'font-size:90px'), ('h1', 'FORTUNEO,', '2.1', ''), ('it gold', "jusqu'à 260 €,", '2.2', 'font-size:72px'), ('it gold', 'avant le 20 décembre.', '2.3', 'font-size:64px')]) + roadmap(1, 2) + '''</div>
  <div class="scene" data-s="3" data-in="right">''' + hd(230, [('h1 co', 'TROIS :', '3.0', 'font-size:90px'), ('h1', 'BOURSOBANK,', '3.1', ''), ('it gold', "jusqu'à 180 €.", '3.2', 'font-size:72px')]) + roadmap(2, 3) + '''</div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:760px"></div>''' + hd(230, [('h1', 'LE BOCAL', '4.0', ''), ('h1', 'SE REMPLIT :', '4.0', ''), ('it gold', 'au maximum.', '4.2', 'font-size:66px')]) + '''
   <div class="jar" style="left:200px"><div class="neck"></div><div class="gl">
    <div class="lay" style="bottom:0;height:257px;background:linear-gradient(180deg,#ff8a7a,#d94a3a)" data-g="4.0" data-fx="growY">330</div>
    <div class="lay" style="bottom:257px;height:202px;background:linear-gradient(180deg,#f6d27a,#c8892c)" data-g="4.1" data-fx="growY">260</div>
    <div class="lay" style="bottom:459px;height:140px;background:linear-gradient(180deg,#ffd0c4,#e9a090)" data-g="4.1" data-fx="growY">180</div></div></div>
   <div class="jl" style="left:670px;top:1160px" data-g="4.0" data-fx="left"><b class="co">330 €</b>Hello bank</div>
   <div class="jl" style="left:670px;top:960px" data-g="4.1" data-fx="left"><b class="gold">260 €</b>Fortuneo</div>
   <div class="jl" style="left:670px;top:790px" data-g="4.1" data-fx="left"><b style="color:#ffd0c4">180 €</b>BoursoBank</div>
   <div class="tot7" data-g="4.1" data-fx="stamp" data-slow="4.1" data-count="770"><div class="v gold">0 €</div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('it gold', 'le mot', '5.1', 'font-size:60px'), ('big gold', '« PARRAINAGE »', '5.2', 'font-size:88px'), ('it gold', 'en privé,', '5.3', '')]) + '''
   <div class="pill" style="top:800px;border-color:rgba(255,107,90,.8)" data-g="5.4" data-fx="up"><div class="pin" style="background:#ff6b5a;color:#fff">3</div><div><b>JE T'ENVOIE LES 3 LIENS</b><span>Hello bank · Fortuneo · BoursoBank</span></div></div>
   <div class="search" style="top:940px" data-g="5.4" data-fx="fade">''' + SEARCH + '''<span data-g="5.4" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1080px">Offres soumises aux conditions en vigueur · montants maximum, nouveaux clients<br>Hello bank : jusqu'à 330 € dont 200 € en bon d'achat, demande validée au plus tard le 08/12<br>Fortuneo : jusqu'à 260 € avec la carte Gold (sous conditions de revenus), jusqu'au 20/12<br>BoursoBank : jusqu'à 180 € pour le filleul (offre de parrainage)</div></div>
'''
