import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# 3 banques, 24/11/2026 21:00 - style v3 nuit & or, accent cuivre. Format F6 « le chemin de ta prime / calendrier » :
# accroche « PARRAINAGE : + de 700 € à prendre, mais il reste 6 jours » + calendrier de novembre (24 = aujourd'hui, 30 entouré) dès la 1re image
# -> étape 1 Hello bank avant le 30/11 à 15 h : jusqu'à 330 € d'avantages (80 + 50 le 13e mois avec Hello Prime + bon d'achat 200 € Hello Start+)
# -> étape 2 BoursoBank jusqu'à 260 € étalés sur les premiers mois (20 + 80 + 80 + 80) -> étape 3 Fortuneo 150 € carte Gold, 300 € versés sous 6 jours
# -> total jusqu'à 740 € (ralenti) -> appel à l'action, retour au calendrier (boucle).
# Sources consultées le 24/11/2026 :
#   hellobank.fr/fr/votre-offre-parrainage : 80 € ouverture + 50 € le 13e mois (Hello Prime, 5 paiements ou retraits par mois pendant 12 mois) + bon d'achat 200 € (mobilité Hello Start+), via le lien de l'invitation avant le 30/11/2026 15h
#   boursobank.com/bon-plan/parrainage-boursobank : prime maximale 260 € filleul (20 ouverture + 80 1er versement >= 300 € + 80 carte 3 mois + 80 EasyMove)
#   fortuneo.fr/parrainage : 150 € Gold / 80 € Fosfo avec code parrain, versement de 300 € dans les 6 jours, offre du 01/11 au 30/11/2026
# Total : 330 + 260 + 150 = 740 €.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'trio15'
TITLE = '3 banques calendrier cuivre'
ROOT = ':root{--bg:#0b0705}'
LINES = [
 ("Parrainage : plus de sept cents euros à prendre, mais il reste six jours.", [("PARRAINAGE :", None), ("+ de 700 € à prendre,", None), ("mais il reste 6 jours.", None)]),
 ("Un : Hello bank, avant le trente novembre à quinze heures. Jusqu'à trois cent trente euros d'avantages.", [("1 : Hello bank,", None), ("avant le 30/11 à 15 h.", None), ("Jusqu'à 330 €", None), ("d'avantages.", None)]),
 ("Deux : Bourso Bank, jusqu'à deux cent soixante euros, étalés sur les premiers mois.", [("2 : BoursoBank,", None), ("jusqu'à 260 €,", None), ("étalés sur les premiers mois.", None)]),
 ("Trois : Fortunéo, cent cinquante euros avec la carte Gold, si tu verses trois cents euros sous six jours.", [("3 : Fortuneo,", None), ("150 € avec la carte Gold,", None), ("si tu verses 300 €", None), ("sous 6 jours.", None)]),
 ("Au total : jusqu'à sept cent quarante euros, sous conditions.", [("Au total :", None), ("jusqu'à 740 €,", None), ("sous conditions.", None)]),
 ("Envoie-moi PARRAINAGE en privé, je t'envoie les trois liens.", [("Envoie-moi", None), ("PARRAINAGE", None), ("en privé,", None), ("je t'envoie les 3 liens.", None)]),
]
SPLITS = [(0.0, 3.33), (3.87, 8.38), (8.83, 12.54), (13.17, 17.91), (18.46, 21.18), (21.69, 23.83)]
GSTART = [[0.0, 0.84, 2.3], [3.87, 5.1, 6.8, 7.9], [8.83, 10.2, 11.6], [13.17, 14.4, 16.3, 17.5], [18.46, 19.1, 20.5], [21.69, 22.0, 22.4, 23.0]]
MINLEN = 1.8
GAP = 0.22
TAIL = 1.7


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px;left:90px;width:840px">' + ''.join(out) + '</div>'


CSS = '''
.cu{color:#f0a46a;text-shadow:0 0 18px rgba(240,150,90,.5)}
.cal{position:absolute;left:170px;width:740px;border-radius:34px;background:#f5ece2;box-shadow:0 30px 80px rgba(0,0,0,.7),0 0 0 6px rgba(232,149,90,.55);color:#2a160a;overflow:visible}
.cal .top{height:92px;border-radius:34px 34px 0 0;background:linear-gradient(180deg,#c8693a,#9c4a22);color:#fff3e6;display:flex;align-items:center;justify-content:center;font:900 44px Inter;letter-spacing:6px}
.cal .dw,.cal .wk{display:grid;grid-template-columns:repeat(7,1fr);padding:0 26px}
.cal .dw{height:56px;align-items:center;font:800 24px Inter;color:#9a7a62;text-align:center}
.cal .wk{height:118px;align-items:center;text-align:center;font:800 44px 'DejaVu Serif',serif}
.cal .wk span{position:relative;font-size:50px}
.cal .past{color:#c9b6a6}
.cal .tod{display:inline-block;width:78px;height:78px;line-height:78px;border-radius:50%;background:#2a160a;color:#f5ece2}
.cal .ring{position:absolute;left:50%;top:50%;width:118px;height:118px;margin:-59px 0 0 -59px;overflow:visible}
.cal .ring circle{fill:none;stroke:#d23b1e;stroke-width:9;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:1}
.jx{position:absolute;width:250px;height:110px;border-radius:24px;background:#d23b1e;color:#fff;display:flex;align-items:center;justify-content:center;font:900 60px Inter;letter-spacing:2px;box-shadow:0 14px 40px rgba(0,0,0,.6)}
.lab{position:absolute;font:800 26px Inter;letter-spacing:2px;color:#f0a46a;white-space:nowrap}
.path{position:absolute;left:170px;width:740px;height:110px}
.path .ln{position:absolute;left:120px;right:120px;top:33px;height:8px;border-radius:4px;background:#3b2618}
.path .fill{position:absolute;left:120px;top:33px;height:8px;border-radius:4px;background:#f0a46a;transform-origin:0 50%}
.path .nd{position:absolute;top:0;width:74px;height:74px;margin-left:-37px;border-radius:50%;background:#1a100a;border:5px solid #5a3a24;color:#c9a588;display:flex;align-items:center;justify-content:center;font:900 36px Inter}
.path .nd.on{background:#f0a46a;border-color:#ffd2ae;color:#2a1408;box-shadow:0 0 30px rgba(240,160,100,.55)}
.path .nd.done{background:#3a2414;border-color:#f0a46a;color:#f0a46a}
.path .t{position:absolute;top:84px;width:240px;margin-left:-120px;text-align:center;font:800 22px Inter;letter-spacing:2px;color:#a88a72;white-space:nowrap}
.card{position:absolute;left:170px;width:740px;border-radius:34px;background:linear-gradient(180deg,#24160d,#140c07);border:5px solid #f0a46a;box-shadow:0 30px 80px rgba(0,0,0,.7);color:#f7e8da;white-space:nowrap;text-align:center}
.card .n{margin-top:30px;font:900 38px Inter;letter-spacing:5px;color:#f0a46a}
.card .v{font:900 140px 'DejaVu Serif',serif;line-height:1.15}
.card .d{font:700 30px Inter;color:#d8bfa8;margin-bottom:30px}
.chips{position:absolute;left:170px;width:740px;display:flex;justify-content:center;gap:14px;flex-wrap:wrap}
.chip{height:92px;padding:0 22px;border-radius:47px;background:#1c110a;border:4px solid #f0a46a;display:flex;align-items:center;gap:12px;font:800 29px Inter;color:#f7e8da;white-space:nowrap}
.chip b{font:900 40px 'DejaVu Serif',serif;color:#f3c766}
.clock{position:absolute;left:330px;width:420px;height:100px;border-radius:50px;background:#d23b1e;color:#fff;display:flex;align-items:center;justify-content:center;gap:16px;font:900 44px Inter;letter-spacing:2px;white-space:nowrap;box-shadow:0 14px 40px rgba(0,0,0,.6)}
.gcard{position:absolute;left:250px;width:580px;height:340px;border-radius:30px;background:linear-gradient(135deg,#fff1c4,#e9b456 45%,#a8701f);box-shadow:0 30px 80px rgba(0,0,0,.7);color:#3a2608;white-space:nowrap}
.gcard .chipi{position:absolute;left:50px;top:105px;width:90px;height:66px;border-radius:12px;background:linear-gradient(135deg,#d8d8d8,#8a8a8a)}
.gcard .t{position:absolute;right:44px;top:36px;font:900 44px Inter;letter-spacing:4px}
.gcard .v{position:absolute;right:44px;bottom:30px;font:900 110px 'DejaVu Serif',serif;color:#5a1a08}
.stk{position:absolute;left:190px;width:700px}
.stk .r{height:100px;border-radius:28px;background:#1a100a;border:4px solid #5a3a24;margin-bottom:14px;display:flex;align-items:center;justify-content:space-between;padding:0 40px;font:800 36px Inter;color:#f7e8da;white-space:nowrap}
.stk .r b{font:900 48px 'DejaVu Serif',serif;color:#f0a46a}
.tot{position:absolute;left:0;width:1080px;text-align:center}
.tot .v{font:900 190px 'DejaVu Serif',serif;line-height:1}
.ex{position:absolute;left:170px;width:740px;text-align:center;font:600 25px Inter;color:#b8987e;line-height:1.4}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'


def calendar(top, gring, gtag, scale=1.0, left=170):
    days = ''.join(f'<span>{d}</span>' for d in 'LMMJVSD')
    w1 = ''.join(f'<span class="past">{d}</span>' for d in range(16, 23))
    w2 = '<span class="past">23</span><span><b class="tod">24</b></span>' + ''.join(f'<span>{d}</span>' for d in range(25, 30))
    ring = f'<svg class="ring" viewBox="0 0 118 118"><circle cx="59" cy="59" r="52" pathLength="1"{(' data-g="' + gring + '" data-fx="draw"') if gring else ""}/></svg>'
    w3 = f'<span>30{ring}</span>' + '<span class="past">1</span><span class="past">2</span><span class="past">3</span><span class="past">4</span><span class="past">5</span><span class="past">6</span>'
    return (f'<div class="cal" style="top:{top}px;left:{left}px;transform:scale({scale});transform-origin:50% 0">'
            f'<div class="top">NOVEMBRE</div><div class="dw">{days}</div><div class="wk">{w1}</div><div class="wk">{w2}</div><div class="wk">{w3}</div></div>')


def path(top, cur):
    xs = [110, 370, 630]
    names = ['HELLO BANK', 'BOURSOBANK', 'FORTUNEO']
    w = (xs[min(cur, 2)] - 120)
    out = f'<div class="path" style="top:{top}px"><div class="ln"></div><div class="fill" style="width:{w}px" data-g="{cur + 1}.0" data-fx="grow"></div>'
    for k, (x, nm) in enumerate(zip(xs, names)):
        cls = 'on' if k == cur else ('done' if k < cur else '')
        out += f'<div class="nd {cls}" style="left:{x}px">{"✓" if k < cur else k + 1}</div><div class="t" style="left:{x}px">{nm}</div>'
    return out + '</div>'


BODY = hud('FRANCE · CALENDRIER', 'PARRAINAGE') + '''
  <div class="scene" data-s="0">''' + hd(235, [('h1 cu', 'PARRAINAGE :', None, 'font-size:84px'), ('it gold', '+ de 700 € à prendre,', None, 'font-size:76px'), ('it gold', 'mais il reste 6 jours.', None, 'font-size:68px')]) + '''
   ''' + calendar(600, '0.1', '0.2') + '''
   <div class="lab" style="left:325px;top:1180px;font-size:32px" data-g="0.1" data-fx="up">▲ AUJOURD'HUI</div>
   <div class="jx" style="left:640px;top:1150px" data-g="0.2" data-fx="stamp">J-6</div>
   <div class="ex" style="top:1320px;font-size:28px" data-g="0.2" data-fx="fade">3 banques · montants maximum cumulés · sous conditions</div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(235, [('h1 cu', '1 : HELLO BANK,', '1.0', 'font-size:70px'), ('it gold', 'avant le 30/11 à 15 h.', '1.1', 'font-size:62px'), ('it gold', "Jusqu'à 330 €", '1.2', 'font-size:66px'), ('it cu', "d'avantages.", '1.3', 'font-size:62px')]) + path(570, 0) + '''
   <div class="clock" style="top:740px" data-g="1.1" data-fx="stamp">30/11 · 15 H</div>
   <div class="card" style="top:880px" data-g="1.2" data-fx="pop"><div class="n">HELLO BANK</div><div class="v gold">330 €</div><div class="d">d'avantages maximum</div></div>
   <div class="chips" style="top:1250px"><div class="chip" data-g="1.2" data-fx="up">ouverture <b>80 €</b></div><div class="chip" data-g="1.2" data-fx="up">13e mois <b>+50 €</b></div><div class="chip" data-g="1.3" data-fx="pop">bon d'achat <b>200 €</b></div></div>
   <div class="ex" style="top:1460px;font-size:23px" data-g="1.2" data-fx="fade">via le lien de l'invitation · 50 € avec Hello Prime (5 paiements ou retraits/mois) · bon d'achat avec Hello Start+</div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(235, [('h1 cu', '2 : BOURSOBANK,', '2.0', 'font-size:70px'), ('it gold', "jusqu'à 260 €,", '2.1', 'font-size:72px'), ('it cu', 'étalés sur les premiers mois.', '2.2', 'font-size:56px')]) + path(570, 1) + '''
   <div class="card" style="top:760px" data-g="2.1" data-fx="pop"><div class="n">BOURSOBANK</div><div class="v gold">260 €</div><div class="d">pour le filleul, maximum</div></div>
   <div class="chips" style="top:1140px"><div class="chip" data-g="2.1" data-fx="up">ouverture <b>20 €</b></div><div class="chip" data-g="2.2" data-fx="up">1er versement <b>80 €</b></div><div class="chip" data-g="2.2" data-fx="up">carte 3 mois <b>80 €</b></div><div class="chip" data-g="2.2" data-fx="up">EasyMove <b>80 €</b></div></div>
   <div class="ex" style="top:1380px;font-size:25px" data-g="2.2" data-fx="fade">1er versement d'au moins 300 € · 1 paiement ou retrait par carte chaque mois pendant 3 mois</div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(235, [('h1 cu', '3 : FORTUNEO,', '3.0', 'font-size:70px'), ('it gold', '150 € avec la carte Gold,', '3.1', 'font-size:60px'), ('it gold', 'si tu verses 300 €', '3.2', 'font-size:62px'), ('it cu', 'sous 6 jours.', '3.3', 'font-size:62px')]) + path(570, 2) + '''
   <div class="gcard" style="top:750px" data-g="3.1" data-fx="right"><div class="chipi"></div><div class="t">GOLD</div><div class="v">150 €</div></div>
   <div class="chips" style="top:1140px"><div class="chip" data-g="3.2" data-fx="up">versement <b>300 €</b></div><div class="chip" data-g="3.3" data-fx="fade">sous <b>6 jours</b></div></div>
   <div class="clock" style="top:1270px;left:300px;width:480px" data-g="3.3" data-fx="pop">JUSQU'AU 30/11</div>
   <div class="ex" style="top:1405px;font-size:25px" data-g="3.3" data-fx="fade">avec le code parrain · 80 € avec la carte Fosfo</div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:780px"></div>''' + hd(250, [('h1 cu', 'AU TOTAL :', '4.0', 'font-size:72px')]) + '''
   <div class="stk" style="top:360px"><div class="r" data-g="4.0" data-fx="left">Hello bank<b>330 €</b></div><div class="r" data-g="4.0" data-fx="right">BoursoBank<b>260 €</b></div><div class="r" data-g="4.0" data-fx="left">Fortuneo · Gold<b>150 €</b></div></div
   ><div class="hd" style="top:690px;left:90px;width:840px"><div class="it gold" style="font-size:70px" data-g="4.1" data-fx="tw">jusqu'à</div></div>
   <div class="tot" style="top:790px" data-g="4.1" data-fx="stamp" data-slow="4.1" data-count="740"><div class="v gold">0 €</div></div>
   <div class="hd" style="top:1010px;left:90px;width:840px"><div class="it cu" style="font-size:64px" data-g="4.2" data-fx="tw">sous conditions.</div></div>
   <div class="clock" style="top:1160px;left:170px;width:740px;font-size:32px" data-g="4.2" data-fx="pop">Hello bank et Fortuneo : jusqu'au 30/11</div>
   <div class="ex" style="top:1290px;font-size:27px" data-g="4.2" data-fx="fade">1re ouverture dans chaque banque · dont 200 € en bon d'achat</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(235, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« PARRAINAGE »', '5.1', 'font-size:84px'), ('it cu', 'en privé,', '5.2', ''), ('it gold', "je t'envoie les 3 liens.", '5.3', 'font-size:62px')]) + '''
   <div class="pill" style="top:690px;left:170px;width:740px;border-color:rgba(240,164,106,.85)" data-g="5.3" data-fx="up"><div class="pin" style="background:#c8693a;color:#fff">✉</div><div><b>JE T'ENVOIE LES 3 LIENS</b><span>Hello bank · BoursoBank · Fortuneo</span></div></div>
   <div class="search" style="top:840px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:985px;font-size:26px;color:#b8a48e">Offres soumises aux conditions en vigueur<br>Nouveaux clients, 1re ouverture dans chaque banque<br>Hello bank : jusqu'à 330 € d'avantages dont 200 € en bon<br>d'achat (Hello Start+), avant le 30/11/2026 à 15h<br>BoursoBank : jusqu'à 260 € pour le filleul<br>Fortuneo : 150 € avec la carte Gold, 300 € versés<br>sous 6 jours, offre jusqu'au 30/11/2026</div>
   <div class="clock" style="top:1390px;left:170px;width:740px;font-size:32px" data-g="5.3" data-fx="pop">Hello bank et Fortuneo : jusqu'au 30/11</div></div>
'''
