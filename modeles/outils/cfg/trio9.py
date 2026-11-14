import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# 3 banques, 14/11/2026 21:00 - style v3 nuit & or, accent émeraude. Plus de 700 € cumulés (770 € max) :
# Hello bank jusqu'à 330 € (80 € + 50 € Hello Prime + 200 € bon d'achat Hello Start +, demande validée au plus tard le 08/12/2026 ; moneyvox.fr 05/11/2026)
# + Fortuneo jusqu'à 260 € (carte Gold : 160 € + 80 € mobilité + 20 € Livret +, jusqu'au 20/12/2026 ; selectra.info)
# + BoursoBank jusqu'à 180 € pour le filleul (boursobank.com, page parrainage).
# Voix : Speko (speechify, voix par défaut), réplique 1 refaite seule (« trois banques » mal prononcé).
# Trois coffres fermés -> histogramme qui se remplit barre par barre (3 scènes) -> étiquettes de dates -> ticket total 770 € -> appel à l'action.
NAME = 'trio9'
TITLE = '3 banques emeraude'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Plus de sept cents euros t'attendent, chez trois banques.", [("Plus de 700 €", None), ("t'attendent,", None), ("chez 3 banques.", None)]),
 ("Hello bank : jusqu'à trois cent trente euros.", [("Hello bank :", None), ("jusqu'à 330 €.", None)]),
 ("Fortunéo : jusqu'à deux cent soixante euros.", [("Fortuneo :", None), ("jusqu'à 260 €.", None)]),
 ("Bourso Bank : jusqu'à cent quatre-vingts euros.", [("BoursoBank :", None), ("jusqu'à 180 €.", None)]),
 ("Deux dates à retenir : le huit et le vingt décembre.", [("Deux dates à retenir :", None), ("le 8", None), ("et le 20 décembre.", None)]),
 ("Au total, sept cent soixante-dix euros maximum.", [("Au total,", None), ("770 €", None), ("maximum.", None)]),
 ("Envoie-moi PARRAINAGE en privé, je t'envoie les trois liens.", [("Envoie-moi", None), ("PARRAINAGE", None), ("en privé,", None), ("je t'envoie les 3 liens.", None)]),
]
SPLITS = [(0.0, 2.37), (2.83, 4.68), (5.21, 7.02), (7.42, 9.31), (9.85, 12.28), (12.74, 14.60), (15.14, 17.10)]
GSTART = [[0.1, 1.0, 1.73], [2.83, 3.59], [5.21, 5.98], [7.42, 8.29], [9.85, 10.97, 11.61], [12.74, 13.32, 14.22], [15.14, 15.42, 15.92, 16.42]]
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
.em{color:#4fe3a4;text-shadow:0 0 18px rgba(61,220,151,.5)}
.vault{position:absolute;top:900px;width:260px;height:300px;border-radius:24px;background:linear-gradient(160deg,#2c2a24,#121110);border:5px solid #d9a24c;box-shadow:0 30px 70px rgba(0,0,0,.7)}
.vault .w{position:absolute;left:55px;top:75px;width:150px;height:150px;border-radius:50%;border:8px solid #8a7f69;background:radial-gradient(circle,#24221d,#0e0d0b)}
.vault .w:before,.vault .w:after{content:'';position:absolute;left:67px;top:-4px;width:8px;height:150px;background:#8a7f69}
.vault .w:after{transform:rotate(90deg)}
.vault .q{position:absolute;left:0;top:-80px;width:100%;text-align:center;font:900 64px 'DejaVu Serif',serif}
.ch2{position:absolute;left:150px;top:640px;width:780px;height:800px}
.ch2 .ax{position:absolute;left:0;bottom:90px;width:780px;height:8px;background:#d9a24c;border-radius:4px}
.bar{position:absolute;bottom:98px;width:200px;border-radius:18px 18px 0 0;background:linear-gradient(180deg,#3a3a33,#1c1b18);border:3px solid #514a40;border-bottom:0;transform-origin:50% 100%}
.bar.on{background:linear-gradient(180deg,#5ff0b2,#1d8a5c);border-color:#f3c766;box-shadow:0 0 50px rgba(61,220,151,.45)}
.bar.done{background:linear-gradient(180deg,#2f6e53,#173a2b);border-color:#8a7f69}
.bv{position:absolute;width:200px;text-align:center;font:900 54px 'DejaVu Serif',serif;white-space:nowrap}
.bn{position:absolute;bottom:20px;width:200px;text-align:center;font:800 27px Inter;letter-spacing:1px;color:#e9e4da;white-space:nowrap}
.tag{position:absolute;width:360px;height:300px;border-radius:22px 22px 22px 22px;background:#f4efe4;color:#1c1310;text-align:center;box-shadow:0 30px 70px rgba(0,0,0,.7)}
.tag:before{content:'';position:absolute;left:160px;top:22px;width:40px;height:40px;border-radius:50%;background:#07060a;border:4px solid #d9a24c}
.tag .d{margin-top:76px;font:900 120px 'DejaVu Serif',serif;line-height:1;color:#1d8a5c}
.tag .m{font:800 30px Inter;letter-spacing:5px;color:#6d5f55;margin-top:6px}
.tag .b{font:900 36px Inter;margin-top:10px}
.str{position:absolute;width:6px;background:#d9a24c;transform-origin:50% 0}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
BANKS = [('Hello bank', 330), ('Fortuneo', 260), ('BoursoBank', 180)]
BX = [20, 290, 560]


def chart(k, g):
    """Histogramme : barre k (0..2) qui monte au groupe g, barres précédentes déjà remplies."""
    out = '<div class="ch2"><div class="ax"></div>'
    for i, (n, v) in enumerate(BANKS):
        h = int(v * 1.6)
        if i < k:
            cls, a = 'bar done', ''
        elif i == k:
            cls, a = 'bar on', f' data-g="{g}" data-fx="growY"'
        else:
            cls, a = 'bar', ' style="opacity:.0"'
        st = f'left:{BX[i]}px;height:{h}px'
        out += f'<div class="{cls}"{a} style="{st}"></div>' if i <= k else f'<div class="bar" style="{st};opacity:.25"></div>'
        if i <= k:
            va = f' data-g="{g}" data-fx="pop"' if i == k else ''
            col = 'gold' if i == k else ''
            sty = '' if i == k else 'color:#9a917f;'
            out += f'<div class="bv {col}"{va} style="{sty}left:{BX[i]}px;bottom:{98 + h + 14}px">{v} €</div>'
        out += f'<div class="bn" style="left:{BX[i]}px">{n}</div>'
    return out + '</div>'


VAULTS = ''.join(f'<div class="vault" style="left:{x}px;transform:rotate({r}deg)"><div class="q gold">?</div><div class="w"></div></div>' for x, r in [(80, -5), (410, 0), (740, 5)])
BODY = hud('FRANCE · 3 BANQUES', 'CUMUL') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(210, [('it gold', 'Plus de', None, 'font-size:64px'), ('big gold', '700 €', None, 'font-size:170px'), ('h1 s', "T'ATTENDENT,", None, ''), ('it em', 'chez 3 banques.', None, 'font-size:70px')]) + '''
   ''' + VAULTS.replace('left:740px', 'left:720px') + '''</div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1 em', 'HELLO BANK :', '1.0', ''), ('it gold', "jusqu'à 330 €.", '1.1', '')]) + chart(0, '1.1') + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 em', 'FORTUNEO :', '2.0', ''), ('it gold', "jusqu'à 260 €.", '2.1', '')]) + chart(1, '2.1') + '''</div>
  <div class="scene" data-s="3" data-in="right">''' + hd(230, [('h1 em', 'BOURSOBANK :', '3.0', ''), ('it gold', "jusqu'à 180 €.", '3.1', '')]) + chart(2, '3.1') + '''</div>
  <div class="scene" data-s="4" data-in="up">''' + hd(230, [('h1 s', 'DEUX DATES À RETENIR :', '4.0', ''), ('it gold', 'le 8 et le 20 décembre.', '4.1', '')]) + '''
   <div class="abs" style="left:100px;top:620px;width:880px;height:8px;background:#8a7f69;border-radius:4px"></div>
   <div class="str" style="left:297px;top:624px;height:110px"></div><div class="str" style="left:777px;top:624px;height:150px"></div>
   <div class="tag" style="left:120px;top:730px;transform:rotate(-6deg)" data-g="4.1" data-fx="up"><div class="d">08</div><div class="m">DÉCEMBRE</div><div class="b">Hello bank</div></div>
   <div class="tag" style="left:600px;top:770px;transform:rotate(5deg)" data-g="4.2" data-fx="up"><div class="d">20</div><div class="m">DÉCEMBRE</div><div class="b">Fortuneo</div></div>
   <div class="abs" style="left:0;top:1190px;width:1080px;text-align:center;font:800 30px Inter;letter-spacing:4px;color:#e9e4da" data-g="4.2" data-fx="fade">BOURSOBANK : PAS DE DATE ANNONCÉE</div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="rays" style="top:780px"></div>''' + hd(230, [('h1', 'AU TOTAL,', '5.0', ''), ('it gold', 'maximum.', '5.2', 'font-size:64px')]) + '''
   <div class="rcpt" style="top:500px;left:240px;width:600px" data-g="5.0" data-fx="up"><div class="t">TICKET DU CUMUL</div><div class="s">offres de bienvenue · nov. 2026</div><hr>
    <div class="row"><span>Hello bank</span><span>330 €</span></div><div class="row"><span>Fortuneo</span><span>260 €</span></div><div class="row"><span>BoursoBank</span><span>180 €</span></div><hr>
    <div class="row tot" data-g="5.1" data-fx="stamp" data-slow="5.1" data-count="770"><span>TOTAL MAX</span><span class="v" style="color:#1d8a5c">0 €</span></div></div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« PARRAINAGE »', '6.1', 'font-size:100px'), ('it gold', 'en privé,', '6.2', '')]) + '''
   <div class="pill" style="top:740px;border-color:rgba(61,220,151,.8)" data-g="6.3" data-fx="up"><div class="pin" style="background:#3ddc97">3</div><div><b>JE T'ENVOIE LES 3 LIENS</b><span>Hello bank · Fortuneo · BoursoBank</span></div></div>
   <div class="search" style="top:880px" data-g="6.3" data-fx="fade">''' + SEARCH + '''<span data-g="6.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1020px">Offres soumises aux conditions en vigueur<br>montants maximum, nouveaux clients<br>Hello bank : dont 200 € en bon d'achat, demande validée au plus tard le 08/12<br>Fortuneo : carte Gold, jusqu'au 20/12 · BoursoBank : offre de parrainage</div></div>
'''
