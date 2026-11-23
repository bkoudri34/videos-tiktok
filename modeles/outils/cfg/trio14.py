import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# 3 banques, 23/11/2026 16:00 - style v3 nuit & or, accent rouge rubis. Format F4 « argent laissé sur la table » :
# tapis de jeu avec 3 enveloppes « + de 700 € » dès la 1re image -> Hello bank 330 € (80 + 50 + 200 bon d'achat)
# -> BoursoBank 260 € (20 + 80 + 80 + 80) -> Fortuneo 150 € carte Gold jusqu'au 30/11 -> total 740 € (ralenti) -> appel à l'action.
# Sources consultées le 23/11/2026 :
#   hellobank.fr/fr/votre-offre-parrainage : jusqu'à 330 € d'avantages filleul (80 € + 50 € Hello Prime le 13e mois + bon d'achat 200 € Hello Start+), avant le 30/11/2026 15h
#   boursobank.com/bon-plan/parrainage-boursobank : jusqu'à 260 € filleul (20 + 80 versement >= 300 € + 80 carte 3 mois + 80 EasyMove)
#   fortuneo.fr/parrainage : 150 € Gold / 80 € Fosfo, versement de 300 € dans les 6 jours, dossier complet du 01/11 au 30/11/2026
# Total : 330 + 260 + 150 = 740 €.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'trio14'
TITLE = '3 banques tapis rubis'
ROOT = ':root{--bg:#0a0507}'
LINES = [
 ("Parrainage banque : tu laisses plus de sept cents euros sur la table.", [("Parrainage banque :", None), ("tu laisses + de 700 €", None), ("sur la table.", None)]),
 ("Hello bank : jusqu'à trois cent trente euros d'avantages, dont deux cents en bon d'achat.", [("Hello bank :", None), ("jusqu'à 330 € d'avantages,", None), ("dont 200 € en bon d'achat.", None)]),
 ("Bourso Bank : jusqu'à deux cent soixante euros pour le filleul.", [("BoursoBank :", None), ("jusqu'à 260 €", None), ("pour le filleul.", None)]),
 ("Fortunéo : cent cinquante euros avec la carte Gold, jusqu'au trente novembre.", [("Fortuneo :", None), ("150 € avec la carte Gold,", None), ("jusqu'au 30 novembre.", None)]),
 ("Au total : jusqu'à sept cent quarante euros, sous conditions.", [("Au total :", None), ("jusqu'à 740 €,", None), ("sous conditions.", None)]),
 ("Envoie-moi PARRAINAGE en privé, je t'envoie les trois liens.", [("Envoie-moi", None), ("PARRAINAGE", None), ("en privé,", None), ("je t'envoie les 3 liens.", None)]),
]
SPLITS = [(0.0, 2.70), (3.10, 6.39), (6.94, 9.42), (9.96, 13.49), (13.97, 16.61), (17.27, 19.3)]
GSTART = [[0.0, 1.0, 2.2], [3.1, 3.8, 5.5], [6.98, 7.9, 8.9], [10.0, 10.8, 12.7], [14.0, 14.7, 16.1], [17.3, 17.6, 18.0, 18.5]]
MINLEN = 2.0
GAP = 0.3
TAIL = 2.1


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px;left:90px;width:840px">' + ''.join(out) + '</div>'


CSS = '''
.rb{color:#ff6b7d;text-shadow:0 0 18px rgba(255,70,100,.5)}
.felt{position:absolute;left:95px;top:760px;width:800px;height:600px;border-radius:60px 60px 30px 30px;background:radial-gradient(ellipse at 50% 30%,#3a0d16,#1a0509 75%);border:8px solid #6b3a1c;box-shadow:inset 0 0 80px rgba(0,0,0,.7),0 30px 80px rgba(0,0,0,.7)}
.felt:after{content:'';position:absolute;left:30px;right:30px;top:30px;bottom:30px;border:3px dashed rgba(255,190,120,.25);border-radius:40px}
.env{position:absolute;width:230px;height:300px;border-radius:18px;background:linear-gradient(170deg,#f6ead2,#d9c29a);box-shadow:0 18px 40px rgba(0,0,0,.6);text-align:center;color:#2a1a10;white-space:nowrap}
.env:before{content:'';position:absolute;left:0;right:0;top:0;height:110px;background:linear-gradient(160deg,#e9d6b0,#cdb283);clip-path:polygon(0 0,100% 0,50% 100%);border-radius:18px 18px 0 0}
.env .n{position:absolute;left:0;right:0;top:140px;font:900 26px Inter;letter-spacing:1px}
.env .v{position:absolute;left:0;right:0;top:185px;font:900 64px 'DejaVu Serif',serif;color:#8a1426}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:700 24px Inter;color:#c99aa2;letter-spacing:3px}
.bigenv{position:absolute;left:250px;top:650px;width:560px;height:330px;border-radius:30px;background:linear-gradient(170deg,#f6ead2,#d9c29a);box-shadow:0 30px 80px rgba(0,0,0,.7),0 0 0 5px rgba(255,107,125,.6);text-align:center;color:#2a1a10;white-space:nowrap}
.bigenv .n{margin-top:46px;font:900 46px Inter;letter-spacing:3px}
.bigenv .v{font:900 150px 'DejaVu Serif',serif;color:#8a1426;line-height:1.2}
.chips{position:absolute;left:130px;top:1060px;width:780px;display:flex;justify-content:center;gap:18px;flex-wrap:wrap}
.chip{height:86px;padding:0 30px;border-radius:43px;background:#1c0a0e;border:4px solid #ff6b7d;display:flex;align-items:center;gap:12px;font:800 30px Inter;color:#f6e6e8;white-space:nowrap}
.chip b{font:900 40px 'DejaVu Serif',serif;color:#f3c766}
.gcard{position:absolute;left:300px;top:640px;width:480px;height:300px;border-radius:30px;background:linear-gradient(135deg,#fff1c4,#e9b456 45%,#a8701f);box-shadow:0 30px 80px rgba(0,0,0,.7);color:#3a2608;white-space:nowrap}
.gcard .chipi{position:absolute;left:50px;top:110px;width:90px;height:66px;border-radius:12px;background:linear-gradient(135deg,#d8d8d8,#8a8a8a)}
.gcard .t{position:absolute;right:44px;top:40px;font:900 44px Inter;letter-spacing:4px}
.gcard .v{position:absolute;right:44px;bottom:36px;font:900 90px 'DejaVu Serif',serif;color:#5a1010}
.cal{position:absolute;left:290px;width:500px;height:100px;border-radius:24px;background:#f6e6e8;color:#2a0a10;display:flex;align-items:center;justify-content:center;font:900 40px Inter;white-space:nowrap;box-shadow:0 0 0 5px #ff6b7d}
.stk{position:absolute;left:190px;width:700px}
.stk .r{height:96px;border-radius:28px;background:#1a080c;border:4px solid #6a2a36;margin-bottom:16px;display:flex;align-items:center;justify-content:space-between;padding:0 40px;font:800 36px Inter;color:#f6e6e8;white-space:nowrap}
.stk .r b{font:900 50px 'DejaVu Serif',serif;color:#ff6b7d}
.tot{position:absolute;left:0;width:1080px;text-align:center}
.tot .v{font:900 190px 'DejaVu Serif',serif;line-height:1}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'


def env(x, y, rot, n, v):
    return f'<div class="env" style="left:{x}px;top:{y}px;transform:rotate({rot}deg)"><div class="n">{n}</div><div class="v">{v}</div></div>'


BODY = hud('FRANCE · 3 COMPTES', 'PARRAINAGE') + '''
  <div class="scene" data-s="0">''' + hd(210, [('h1 rb', 'PARRAINAGE BANQUE :', None, 'font-size:62px'), ('it gold', 'tu laisses + de 700 €', None, 'font-size:78px'), ('it gold', 'sur la table.', None, 'font-size:70px')]) + '''
   <div class="felt"></div>''' + env(145, 860, -8, 'HELLO BANK', '330 €') + env(395, 900, 3, 'BOURSOBANK', '260 €') + env(635, 850, 7, 'FORTUNEO', '150 €') + '''
   <div class="ex" style="top:1250px">MAXIMUM CUMULÉ · SOUS CONDITIONS</div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1 rb', 'HELLO BANK :', '1.0', 'font-size:68px'), ('it gold', "jusqu'à 330 € d'avantages,", '1.1', 'font-size:64px')]) + '''
   <div class="bigenv" data-g="1.0" data-fx="pop"><div class="n">HELLO BANK</div><div class="v" data-g="1.1" data-fx="stamp">330 €</div></div>
   <div class="chips"><div class="chip" data-g="1.1" data-fx="up">ouverture <b>80 €</b></div><div class="chip" data-g="1.1" data-fx="up">13e mois Prime <b>50 €</b></div><div class="chip" data-g="1.2" data-fx="pop">bon d'achat Hello Start+ <b>200 €</b></div></div>
   <div class="hd" style="top:1290px;left:90px;width:840px"><div class="it rb" style="font-size:54px" data-g="1.2" data-fx="tw">dont 200 € en bon d'achat.</div></div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 rb', 'BOURSOBANK :', '2.0', 'font-size:68px'), ('it gold', "jusqu'à 260 €", '2.1', 'font-size:78px')]) + '''
   <div class="bigenv" data-g="2.0" data-fx="pop"><div class="n">BOURSOBANK</div><div class="v" data-g="2.1" data-fx="stamp">260 €</div></div>
   <div class="chips"><div class="chip" data-g="2.1" data-fx="up">ouverture <b>20 €</b></div><div class="chip" data-g="2.1" data-fx="up">versement <b>80 €</b></div><div class="chip" data-g="2.2" data-fx="up">carte <b>80 €</b></div><div class="chip" data-g="2.2" data-fx="up">EasyMove <b>80 €</b></div></div>
   <div class="hd" style="top:1290px;left:90px;width:840px"><div class="it rb" style="font-size:60px" data-g="2.2" data-fx="tw">pour le filleul.</div></div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('h1 rb', 'FORTUNEO :', '3.0', 'font-size:68px'), ('it gold', '150 € avec la carte Gold,', '3.1', 'font-size:62px')]) + '''
   <div class="gcard" data-g="3.0" data-fx="right"><div class="chipi"></div><div class="t">GOLD</div><div class="v" data-g="3.1" data-fx="stamp">150 €</div></div>
   <div class="cal" style="top:1010px" data-g="3.2" data-fx="pop">JUSQU'AU 30/11</div>
   <div class="ex" style="top:1140px;font-size:26px" data-g="3.2" data-fx="fade">avec code parrain · 300 € versés sous 6 jours</div>
   <div class="hd" style="top:1220px;left:90px;width:840px"><div class="it rb" style="font-size:60px" data-g="3.2" data-fx="tw">jusqu'au 30 novembre.</div></div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:840px"></div>''' + hd(215, [('h1 rb', 'AU TOTAL :', '4.0', 'font-size:70px')]) + '''
   <div class="stk" style="top:350px"><div class="r" data-g="4.0" data-fx="left">Hello bank<b>330 €</b></div><div class="r" data-g="4.0" data-fx="right">BoursoBank<b>260 €</b></div><div class="r" data-g="4.0" data-fx="left">Fortuneo · Gold<b>150 €</b></div></div
   ><div class="hd" style="top:715px;left:90px;width:840px"><div class="it gold" style="font-size:70px" data-g="4.1" data-fx="tw">jusqu'à</div></div>
   <div class="tot" style="top:810px" data-g="4.1" data-fx="stamp" data-slow="4.1" data-count="740"><div class="v gold">0 €</div></div>
   <div class="hd" style="top:1030px;left:90px;width:840px"><div class="it rb" style="font-size:64px" data-g="4.2" data-fx="tw">sous conditions.</div></div>
   <div class="ex" style="top:1150px;font-size:26px" data-g="4.2" data-fx="fade">1re ouverture dans chaque banque · dont 200 € en bon d'achat</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« PARRAINAGE »', '5.1', 'font-size:84px'), ('it rb', 'en privé,', '5.2', ''), ('it gold', "je t'envoie les 3 liens.", '5.3', 'font-size:62px')]) + '''
   <div class="pill" style="top:660px;border-color:rgba(255,107,125,.85)" data-g="5.3" data-fx="up"><div class="pin" style="background:#c8283f;color:#fff">✉</div><div><b>JE T'ENVOIE LES 3 LIENS</b><span>Hello bank · BoursoBank · Fortuneo</span></div></div>
   <div class="search" style="top:830px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:970px;font-size:24px">Offres soumises aux conditions en vigueur · nouveaux clients<br>Hello bank : jusqu'à 330 € d'avantages dont 200 € en bon<br>d'achat (Hello Start+), avant le 30/11/2026 à 15h<br>BoursoBank : jusqu'à 260 € pour le filleul<br>Fortuneo : 150 € avec la carte Gold, 300 € versés sous 6 jours,<br>dossier complet jusqu'au 30/11/2026</div></div>
'''
