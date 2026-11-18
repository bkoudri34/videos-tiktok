import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Hello bank, 18/11/2026 21:00 - style v3 nuit & or, accent vert menthe. Format F4 « argent laissé sur la table » :
# table avec 3 tas (80 / 50 / bon d'achat 200) dès la 1re image -> billets 80 € -> calendrier 13e mois +50 € -> bon d'achat 200 €
# -> page de calendrier 8 décembre (ralenti) -> appel à l'action.
# Offre : jusqu'à 330 € = 80 € pour une 1re ouverture Hello Prime + 50 € versés le 13e mois si 5 opérations carte par mois pendant 12 mois
# + bon d'achat 200 € pour une mobilité bancaire avec Hello Start+, jusqu'au 08/12/2026 (hellobank.fr/fr/offre/compte-et-cartes/hello-prime consulté le 18/11 ; moneyvox.fr).
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'hellobank12'
TITLE = 'Hello bank table menthe'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Parrainage Hello bank : tu laisses peut-être trois cent trente euros sur la table.", [("Parrainage Hello bank :", None), ("tu laisses peut-être", None), ("330 €", None), ("sur la table.", None)]),
 ("Quatre-vingts euros à l'ouverture d'un compte Hello Prime.", [("80 €", None), ("à l'ouverture", None), ("d'un compte Hello Prime.", None)]),
 ("Cinquante de plus au treizième mois, si tu utilises ta carte.", [("50 de plus", None), ("au 13e mois,", None), ("si tu utilises ta carte.", None)]),
 ("Et un bon d'achat de deux cents euros avec le changement de banque.", [("Et un bon d'achat", None), ("de 200 €", None), ("avec le changement de banque.", None)]),
 ("Attention : c'est jusqu'au huit décembre.", [("Attention :", None), ("c'est jusqu'au", None), ("8 décembre.", None)]),
 ("Envoie-moi HELLO en privé, je t'envoie mon lien.", [("Envoie-moi", None), ("HELLO", None), ("en privé,", None), ("je t'envoie mon lien.", None)]),
]
SPLITS = [(0.0, 2.95), (3.29, 5.19), (5.65, 8.03), (8.38, 10.61), (11.0, 12.62), (13.12, 14.79)]
GSTART = [[0.0, 1.2, 1.8, 2.4], [3.29, 3.8, 4.3], [5.65, 6.3, 7.1], [8.38, 9.0, 9.7], [11.0, 11.8, 12.2], [13.12, 13.5, 13.6, 14.1]]
MINLEN = 2.2
GAP = 0.42
TAIL = 2.4


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.mt{color:#5ff0b0;text-shadow:0 0 18px rgba(61,220,151,.55)}
.tbl{position:absolute;left:60px;top:1180px;width:960px;height:60px;border-radius:14px;background:linear-gradient(180deg,#5a3b22,#3a2414);box-shadow:0 20px 50px rgba(0,0,0,.7)}
.tbl:before,.tbl:after{content:'';position:absolute;top:60px;width:40px;height:300px;background:#2e1c10}
.tbl:before{left:80px}.tbl:after{right:80px}
.pile{position:absolute;width:250px}
.pile i{display:block;height:26px;margin-top:-8px;border-radius:6px;background:linear-gradient(90deg,#2f9c6c,#5fe0a8 50%,#2f9c6c);border:2px solid #1c6a47}
.pile b{display:block;text-align:center;font:900 54px 'DejaVu Serif',serif;margin-bottom:14px;white-space:nowrap}
.vou{position:absolute;width:250px;height:150px;border-radius:16px;background:#f5efe0;color:#1a1408;border:4px dashed #c8892c;text-align:center;padding-top:22px;font:800 24px Inter;letter-spacing:2px}
.vou b{display:block;font:900 56px 'DejaVu Serif',serif;letter-spacing:0;color:#9a5d10}
.bill{position:absolute;width:520px;height:250px;border-radius:20px;background:linear-gradient(135deg,#2f9c6c,#7ff0c0 55%,#2f9c6c);border:6px solid #1c6a47;color:#0b2a1c;box-shadow:0 30px 80px rgba(0,0,0,.6)}
.bill .v{position:absolute;left:0;top:40px;width:100%;text-align:center;font:900 130px 'DejaVu Serif',serif}
.bill:before{content:'';position:absolute;inset:18px;border:3px solid rgba(11,42,28,.35);border-radius:12px}
.lbl2{position:absolute;left:0;width:1080px;text-align:center;font:800 40px Inter;color:#e9e4da;white-space:nowrap}
.cal{position:absolute;width:380px;height:400px;border-radius:30px;background:#f4f2ee;color:#1a1814;overflow:hidden;text-align:center;box-shadow:0 30px 80px rgba(0,0,0,.6)}
.cal .top{height:100px;background:#3ddc97;color:#06281a;font:900 40px Inter;display:flex;align-items:center;justify-content:center;letter-spacing:3px}
.cal .d{font:900 170px 'DejaVu Serif',serif;line-height:1.3}
.cal small{display:block;font:700 30px Inter;color:#6b665e;margin-top:-10px}
.plus{position:absolute;font:900 120px 'DejaVu Serif',serif;white-space:nowrap}
.cardc{position:absolute;width:360px;height:226px;border-radius:24px;background:linear-gradient(135deg,#1d2a24,#0f1512);border:3px solid #3ddc97;box-shadow:0 20px 60px rgba(0,0,0,.6)}
.cardc i{position:absolute;left:34px;top:70px;width:70px;height:52px;border-radius:10px;background:linear-gradient(135deg,#f6d27a,#c8892c)}
.cardc span{position:absolute;left:34px;bottom:30px;font:600 28px 'DejaVu Sans Mono';color:#cfe9dc;letter-spacing:3px}
.bigv{position:absolute;left:190px;top:760px;width:700px;height:420px;border-radius:30px;background:#f5efe0;color:#1a1408;border:6px dashed #c8892c;text-align:center;padding-top:60px;font:800 38px Inter;letter-spacing:4px;box-shadow:0 30px 90px rgba(0,0,0,.6)}
.bigv b{display:block;font:900 170px 'DejaVu Serif',serif;letter-spacing:0;color:#9a5d10;line-height:1.1}
.bigv small{display:block;font:700 28px Inter;color:#6b5a40;letter-spacing:1px}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'


def pile(left, n, amt, g=None):
    a = f' data-g="{g}" data-fx="up"' if g else ''
    return f'<div class="pile" style="left:{left}px;bottom:{1920 - 1186}px"{a}><b class="gold">{amt}</b>' + '<i></i>' * n + '</div>'


TABLE = '<div class="tbl"></div>' + pile(110, 9, '80 €') + pile(420, 6, '+50 €') + '<div class="vou" style="left:730px;top:1020px">BON D\'ACHAT<b>200 €</b></div>'

BODY = hud('FRANCE · HELLO BANK', 'SUR LA TABLE') + '''
  <div class="scene" data-s="0">''' + hd(215, [('h1', 'PARRAINAGE HELLO BANK :', None, 'font-size:64px'), ('it mt', 'tu laisses peut-être', None, 'font-size:66px'), ('big gold', '330 €', None, 'font-size:150px'), ('it gold', 'sur la table.', None, 'font-size:66px')]) + TABLE + '''</div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('big gold', '80 €', '1.0', 'font-size:150px'), ('h1', "À L'OUVERTURE", '1.1', 'font-size:66px'), ('it mt', "d'un compte Hello Prime.", '1.2', 'font-size:62px')]) + '''
   <div class="bill" style="left:280px;top:820px;transform:rotate(-6deg)" data-g="1.0" data-fx="pop"><div class="v">80 €</div></div>
   <div class="lbl2" style="top:1180px" data-g="1.2" data-fx="up">1re ouverture · offre Hello Prime</div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1', '50 DE PLUS', '2.0', ''), ('it gold', 'au 13e mois,', '2.1', 'font-size:66px'), ('it mt', 'si tu utilises ta carte.', '2.2', 'font-size:62px')]) + '''
   <div class="cal" style="left:130px;top:780px" data-g="2.1" data-fx="pop"><div class="top">MOIS</div><div class="d">13</div><small>versement +50 €</small></div>
   <div class="cardc" style="left:590px;top:820px;transform:rotate(5deg)" data-g="2.2" data-fx="right"><i></i><span>•••• 2026</span></div>
   <div class="lbl2" style="top:1240px" data-g="2.2" data-fx="up">5 opérations carte par mois, 12 mois</div></div>
  <div class="scene" data-s="3" data-in="right">''' + hd(230, [('h1', "ET UN BON D'ACHAT", '3.0', 'font-size:66px'), ('it mt', 'avec le changement de banque.', '3.2', 'font-size:56px')]) + '''
   <div class="bigv" data-g="3.1" data-fx="stamp">BON D'ACHAT<b>200 €</b><small>mobilité bancaire avec Hello Start+</small></div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:700px"></div>''' + hd(230, [('h1 mt', 'ATTENTION :', '4.0', 'font-size:84px'), ('it gold', "c'est jusqu'au", '4.1', 'font-size:66px')]) + '''
   <div class="cal" style="left:350px;top:720px;width:380px" data-g="4.2" data-fx="stamp" data-slow="4.2"><div class="top">DÉCEMBRE</div><div class="d">8</div><small>dernier jour · J-20</small></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« HELLO »', '5.1', 'font-size:110px'), ('it gold', 'en privé,', '5.2', '')]) + '''
   <div class="pill" style="top:780px;border-color:rgba(61,220,151,.85)" data-g="5.3" data-fx="up"><div class="pin" style="background:#3ddc97;color:#06281a">✉</div><div><b>JE T'ENVOIE MON LIEN</b><span>jusqu'à 330 € · avant le 08/12</span></div></div>
   <div class="search" style="top:920px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1060px">Offre soumise aux conditions en vigueur · jusqu'au 08/12/2026<br>jusqu'à 330 € : 80 € pour une 1re ouverture Hello Prime<br>+ 50 € le 13e mois (5 opérations carte par mois pendant 12 mois)<br>+ bon d'achat de 200 € pour une mobilité bancaire avec Hello Start+</div></div>
'''
