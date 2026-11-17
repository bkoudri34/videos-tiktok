import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Fortuneo, 17/11/2026 21:00 - style v3 nuit & or, accent vert émeraude. Offre de bienvenue (1re ouverture, du 02/11 au 20/12/2026) :
# carte Gold CB Mastercard (sous conditions de revenus) jusqu'à 260 € = 160 € après 5 paiements en 90 jours + 80 € mobilité + 20 € Livret + ;
# carte Fosfo (sans condition de revenus) jusqu'à 150 € = 50 € + 80 € + 20 €
# (sources : top10banques.com, article du 03/11/2026 ; moneyvox.fr). Voix : Speko (speechify, voix par défaut ; voix clonée refusée 402),
# réplique 1 refaite seule. Format « comparatif des deux cartes » : deux cartes retournées -> Fosfo 150 € -> barres Fosfo / Gold 260 € (ralenti)
# -> frise 5 paiements sur 90 jours -> tuiles +80 € / +20 € -> compte à rebours J-33 -> appel à l'action.
NAME = 'fortuneo10'
TITLE = 'Fortuneo deux cartes émeraude'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Chez Fortunéo, la carte que tu choisis change tout.", [("Chez Fortuneo,", None), ("la carte que tu choisis", None), ("change tout.", None)]),
 ("Avec la Fosfo, sans condition de revenus : jusqu'à cent cinquante euros.", [("Avec la Fosfo,", None), ("sans condition de revenus :", None), ("jusqu'à 150 €.", None)]),
 ("Avec la Gold, sous conditions de revenus : jusqu'à deux cent soixante euros.", [("Avec la Gold,", None), ("sous conditions de revenus :", None), ("jusqu'à 260 €.", None)]),
 ("Dans les deux cas : cinq paiements en quatre-vingt-dix jours.", [("Dans les deux cas :", None), ("5 paiements", None), ("en 90 jours.", None)]),
 ("Plus quatre-vingts euros si tu changes de banque, et vingt avec le Livret plus.", [("Plus 80 €", None), ("si tu changes de banque,", None), ("et 20 €", None), ("avec le Livret +.", None)]),
 ("C'est valable jusqu'au vingt décembre.", [("C'est valable", None), ("jusqu'au 20 décembre.", None)]),
 ("Envoie-moi FORTUNÉO en privé, je t'envoie le lien.", [("Envoie-moi", None), ("FORTUNEO", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 2.18), (2.71, 5.46), (5.90, 9.04), (9.53, 11.73), (12.18, 15.14), (15.64, 16.92), (17.49, 19.37)]
GSTART = [[0.1, 0.85, 1.7], [2.8, 3.62, 4.52], [6.0, 6.62, 7.72], [9.7, 10.52, 11.02], [12.18, 12.92, 13.92, 14.32], [15.66, 16.22], [17.52, 17.92, 18.32, 18.82]]
MINLEN = 1.9
GAP = 0.34
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
.cb{position:absolute;width:400px;height:252px;border-radius:24px;box-shadow:0 30px 80px rgba(0,0,0,.7);padding:26px 30px;font:900 30px Inter;letter-spacing:4px}
.cb i{position:absolute;left:30px;top:96px;width:76px;height:58px;border-radius:10px;background:linear-gradient(135deg,#fff1c4,#b98a3a)}
.cb em{position:absolute;left:30px;bottom:26px;font:700 24px 'DejaVu Sans Mono',monospace;letter-spacing:4px;font-style:normal}
.cb.fo{background:linear-gradient(135deg,#1d6b4c,#0f3a2a 60%,#08231a);color:#c9f5df;border:3px solid #3ddc97}
.cb.go{background:linear-gradient(135deg,#f6dc8e 0%,#d6a347 45%,#8a5a18 100%);color:#2a1a05}
.cb.bk{background:repeating-linear-gradient(45deg,#14201b 0 18px,#101914 18px 36px);border:3px solid #3a5a4c;display:flex;align-items:center;justify-content:center;font:900 130px 'DejaVu Serif',serif;color:#3ddc97}
.chart{position:absolute;left:200px;top:700px;width:680px;height:720px}
.chart .base{position:absolute;left:0;bottom:120px;width:680px;height:6px;background:#3a5a4c}
.bar{position:absolute;bottom:126px;width:220px;border-radius:20px 20px 0 0;transform-origin:50% 100%}
.bar.f{left:60px;height:240px;background:linear-gradient(180deg,#3ddc97,#13573b)}
.bar.g{left:400px;height:416px;background:linear-gradient(180deg,#f6dc8e,#a8701f)}
.bar b{position:absolute;left:0;top:-110px;width:220px;text-align:center;font:900 76px 'DejaVu Serif',serif;color:#f3c766;white-space:nowrap}
.bar.f b{color:#7ff0bf}
.chart .lb{position:absolute;bottom:40px;width:220px;text-align:center;font:800 34px Inter;letter-spacing:4px;color:#e9e4da}
.chart .sm{position:absolute;bottom:0;width:220px;text-align:center;font:600 24px 'DejaVu Sans Mono',monospace;color:#8f9a95;white-space:nowrap}
.tl{position:absolute;left:140px;top:960px;width:800px;height:10px;border-radius:5px;background:rgba(255,255,255,.14)}
.tl .p{position:absolute;left:0;top:0;width:800px;height:10px;border-radius:5px;background:linear-gradient(90deg,#3ddc97,#f3c766);transform-origin:0 50%}
.tl .cn{position:absolute;top:-56px;width:110px;height:110px;margin-left:-55px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#fff0c0,#e9b456 50%,#a8701f);box-shadow:0 10px 0 #7a5016,0 0 30px rgba(240,180,80,.4);font:900 46px Inter;color:#3a2606;display:flex;align-items:center;justify-content:center}
.tl .l{position:absolute;top:80px;font:800 32px 'DejaVu Sans Mono',monospace;color:#e9e4da;white-space:nowrap}
.tile{position:absolute;left:170px;width:740px;height:200px;border-radius:30px;background:#0d1612;border:4px solid #3ddc97;display:flex;align-items:center;gap:30px;padding:0 40px;box-shadow:0 26px 70px rgba(0,0,0,.6);white-space:nowrap}
.tile .a{font:900 92px 'DejaVu Serif',serif;color:#f3c766;width:290px}
.tile .x b{display:block;font:800 38px Inter;color:#e9e4da}.tile .x span{font:600 26px Inter;color:#8f9a95}
.flip{position:absolute;left:220px;top:760px;width:640px;display:flex;gap:24px;justify-content:center}
.flip div{width:250px;height:330px;border-radius:24px;background:linear-gradient(180deg,#1a2a23 0 49.5%,#0b130f 50.5% 100%);border:3px solid #3a5a4c;font:900 250px 'DejaVu Serif',serif;color:#3ddc97;display:flex;align-items:center;justify-content:center;box-shadow:0 30px 80px rgba(0,0,0,.6)}
.fl{position:absolute;left:0;top:1130px;width:1080px;text-align:center;font:900 46px Inter;letter-spacing:10px;color:#e9e4da}
.fl small{display:block;margin-top:14px;font:700 28px 'DejaVu Sans Mono',monospace;letter-spacing:3px;color:#8f9a95}
'''


def card(kind, st, a='', label=''):
    if kind == 'bk':
        return f'<div class="cb bk" style="{st}"{a}>?</div>'
    return f'<div class="cb {kind}" style="{st}"{a}>{label}<i></i><em>•••• 2026</em></div>'


BODY = hud('FRANCE · DEUX CARTES', 'COMPARATIF') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(210, [('h1 em', 'CHEZ FORTUNEO,', None, 'font-size:84px'), ('it gold', 'la carte que tu choisis', None, 'font-size:74px'), ('it gold', 'change tout.', None, 'font-size:92px')]) + \
    card('bk', 'left:110px;top:860px;transform:rotate(-8deg)') + card('bk', 'left:560px;top:900px;transform:rotate(6deg)') + '''</div>
  <div class="scene" data-s="1" data-in="left">''' + hd(230, [('h1 em', 'AVEC LA FOSFO,', '1.0', ''), ('it gold', 'sans condition de revenus :', '1.1', 'font-size:64px'), ('it gold', "jusqu'à 150 €.", '1.2', 'font-size:80px')]) + \
    card('fo', 'left:340px;top:720px;transform:rotate(-5deg)', ' data-g="1.0" data-fx="pop"', 'FOSFO') + '''
   <div class="tile" style="top:1100px" data-g="1.2" data-fx="up"><div class="a">150 €</div><div class="x"><b>max. avec la Fosfo</b><span>50 € carte + 80 € + 20 €</span></div></div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 em', 'AVEC LA GOLD,', '2.0', ''), ('it gold', 'sous conditions de revenus :', '2.1', 'font-size:62px'), ('it gold', "jusqu'à 260 €.", '2.2', 'font-size:80px')]) + '''
   <div class="chart"><div class="base"></div>
    <div class="bar f"><b>150 €</b></div>
    <div class="bar g" data-g="2.2" data-fx="up" data-slow="2.2" data-count="260"><b class="v">0 €</b></div>
    <div class="lb" style="left:60px">FOSFO</div><div class="lb" style="left:400px;color:#f3c766" data-g="2.0" data-fx="pop">GOLD</div>
    <div class="sm" style="left:60px">50+80+20</div><div class="sm" style="left:400px" data-g="2.1" data-fx="fade">160+80+20</div></div></div>
  <div class="scene" data-s="3" data-in="up">''' + hd(230, [('h1', 'DANS LES DEUX CAS :', '3.0', 'font-size:72px'), ('h1 em', '5 PAIEMENTS', '3.1', 'font-size:84px'), ('it gold', 'en 90 jours.', '3.2', 'font-size:80px')]) + '''
   <div class="tl"><div class="p" data-g="3.2" data-fx="grow"></div>''' + ''.join(
    f'<div class="cn" style="left:{x}px" data-g="3.1" data-fx="pop">{k + 1}</div>' for k, x in enumerate((70, 210, 360, 500, 640))) + '''
    <div class="l" style="left:-20px">J0</div><div class="l" style="left:720px" data-g="3.2" data-fx="up">J90</div></div>
   ''' + card('fo', 'left:170px;top:1150px;transform:rotate(-6deg) scale(.8)') + card('go', 'left:510px;top:1150px;transform:rotate(5deg) scale(.8)', '', 'GOLD') + '''</div>
  <div class="scene" data-s="4" data-in="pop">''' + hd(230, [('h1 em', 'PLUS 80 €', '4.0', 'font-size:90px'), ('it gold', 'si tu changes de banque,', '4.1', 'font-size:66px'), ('it gold', 'et 20 € avec le Livret +.', '4.2', 'font-size:64px')]) + '''
   <div class="tile" style="top:780px" data-g="4.1" data-fx="left"><div class="a">+80 €</div><div class="x"><b>Mobilité bancaire</b><span>tu changes de banque</span></div></div>
   <div class="tile" style="top:1020px" data-g="4.3" data-fx="right"><div class="a">+20 €</div><div class="x"><b>Livret +</b><span>ouvert en même temps</span></div></div></div>
  <div class="scene" data-s="5" data-in="up">''' + hd(230, [('h1', "C'EST VALABLE", '5.0', ''), ('it gold', "jusqu'au 20 décembre.", '5.1', 'font-size:74px')]) + '''
   <div class="flip" data-g="5.0" data-fx="up"><div>3</div><div>3</div></div>
   <div class="fl" data-g="5.1" data-fx="stamp">JOURS RESTANTS<small>17/11 → 20/12/2026</small></div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« FORTUNEO »', '6.1', 'font-size:96px'), ('it gold', 'en privé,', '6.2', '')]) + '''
   <div class="pill" style="top:740px;border-color:rgba(61,220,151,.8)" data-g="6.3" data-fx="up"><div class="pin" style="background:#3ddc97;color:#06120c">✉</div><div><b>JE T'ENVOIE LE LIEN</b><span>offre valable jusqu'au 20/12</span></div></div>
   <div class="cond" style="top:900px">Offre soumise aux conditions en vigueur<br>1re ouverture de compte, jusqu'au 20/12/2026<br>Gold (sous conditions de revenus) : jusqu'à 260 €<br>Fosfo : jusqu'à 150 €<br>prime carte après 5 paiements en 90 jours<br>+ 80 € mobilité bancaire + 20 € Livret +</div></div>
'''
