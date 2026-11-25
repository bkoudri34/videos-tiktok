import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Hello bank, 25/11/2026 18:00 - style v3 nuit & or, accent vert menthe. Format F8 « résultat d'abord » :
# 3 notifications (+80 €, +50 € 13e mois, bon d'achat 200 €) et « jusqu'à 330 € » dès la 1re image + pastille « il reste 5 jours »
# -> téléphone Hello One / Hello Prime (80 €) -> frise des 12 mois avec 5 paiements par mois (+50 € le 13e mois) -> bon d'achat
# 200 € Hello Start+ (ralenti) -> calendrier 30/11 à 15h -> appel à l'action.
# Offre parrainage filleul (hellobank.fr/fr/votre-offre-parrainage, consultée le 25/11/2026) : 80 € Hello One ou Hello Prime,
# + 50 € le 13e mois avec Hello Prime (au moins 5 paiements ou retraits par mois sur les 12 premiers mois), bon d'achat 200 €
# (mobilité Hello Start+), « jusqu'à 330 € d'avantages », demande d'ouverture via l'invitation avant le 30/11/2026 à 15h.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'hellobank16'
TITLE = 'Hello bank notifications menthe'
ROOT = ':root{--bg:#030a07}'
LINES = [
 ("Parrainage Hello bank : jusqu'à trois cent trente euros d'avantages. Il reste cinq jours.", [("Parrainage Hello bank :", None), ("jusqu'à 330 € d'avantages.", None), ("Il reste 5 jours.", None)]),
 ("Quatre-vingts euros à l'ouverture, avec Hello One ou Hello Prime.", [("80 € à l'ouverture,", None), ("avec Hello One ou Hello Prime.", None)]),
 ("Avec Hello Prime, cinquante euros de plus le treizième mois, si tu paies avec ta carte au moins cinq fois par mois.", [("Avec Hello Prime,", None), ("50 € de plus le 13e mois,", None), ("si tu paies avec ta carte", None), ("au moins 5 fois par mois.", None)]),
 ("Et si tu changes de banque avec Hello Start plus, un bon d'achat de deux cents euros.", [("Et si tu changes de banque", None), ("avec Hello Start+,", None), ("un bon d'achat de 200 €.", None)]),
 ("Attention : ta demande d'ouverture doit être faite avant le trente novembre, à quinze heures.", [("Attention :", None), ("ta demande d'ouverture", None), ("doit être faite avant", None), ("le 30 novembre, à 15 h.", None)]),
 ("Envoie-moi HELLO BANK en privé, je t'envoie l'invitation.", [("Envoie-moi", None), ("HELLO BANK", None), ("en privé,", None), ("je t'envoie l'invitation.", None)]),
]
SPLITS = [(0.0, 3.95), (4.63, 7.78), (8.51, 13.34), (13.72, 17.46), (17.90, 21.65), (22.18, 24.17)]
GSTART = [[0.0, 1.2, 3.1], [4.63, 6.1], [8.51, 9.6, 11.5, 12.4], [13.9, 14.8, 16.2], [18.1, 18.7, 19.5, 20.4], [22.2, 22.5, 22.8, 23.3]]
MINLEN = 1.9
GAP = 0.26
TAIL = 1.8


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px;left:90px;width:840px">' + ''.join(out) + '</div>'


CSS = '''
.mt{color:#6ff5c0;text-shadow:0 0 18px rgba(80,240,180,.45)}
.ntf{position:absolute;left:150px;width:760px;height:116px;border-radius:30px;background:#0b1913;border:4px solid #3fae85;display:flex;align-items:center;gap:22px;padding:0 28px;white-space:nowrap;color:#eafff6;box-shadow:0 20px 50px rgba(0,0,0,.6)}
.ntf .ic{flex:none;width:66px;height:66px;border-radius:18px;background:#2bb683;color:#04140d;display:flex;align-items:center;justify-content:center;font:900 34px Inter}
.ntf .tx{flex:1;font:800 30px Inter}.ntf .tx span{display:block;font:600 21px Inter;color:#9cc9b6}
.ntf .v{font:900 44px 'DejaVu Serif',serif;color:#f3c766}
.chip{position:absolute;left:330px;width:420px;height:80px;border-radius:40px;background:#6ff5c0;color:#03150d;display:flex;align-items:center;justify-content:center;font:900 34px Inter;letter-spacing:1px;white-space:nowrap}
.ph{position:absolute;left:300px;top:700px;width:480px;height:600px;border-radius:56px;background:#0b1210;border:10px solid #26332e;box-shadow:0 30px 90px rgba(0,0,0,.7);text-align:center;color:#eafff6;white-space:nowrap}
.ph .tt{margin-top:56px;font:800 28px Inter;color:#8fc4ae;letter-spacing:2px}
.ph .op{margin:26px auto 0;width:380px;height:110px;border-radius:26px;display:flex;align-items:center;justify-content:center;font:900 40px Inter}
.ph .o1{background:#0f2a20;border:4px solid #6ff5c0}
.ph .o2{background:#2a2110;border:4px solid #e0ac55;color:#f6dc9c}
.ph .bn{margin:34px auto 0;width:300px;height:90px;border-radius:45px;background:#f3c766;color:#1a1204;display:flex;align-items:center;justify-content:center;font:900 46px 'DejaVu Serif',serif}
.months{position:absolute;left:150px;width:780px;display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.months div{height:96px;border-radius:20px;background:#0d1c16;border:3px solid #2f6b55;text-align:center;padding-top:12px;white-space:nowrap;overflow:hidden}
.months b{display:block;font:800 22px Inter;color:#8fc4ae;letter-spacing:1px}
.months i{display:block;margin-top:12px;font-style:normal;font:900 24px Inter;color:#6ff5c0;letter-spacing:3px}
.m13{position:absolute;left:290px;width:500px;height:130px;border-radius:30px;background:#2a2110;border:5px solid #e0ac55;display:flex;align-items:center;justify-content:center;gap:26px;white-space:nowrap}
.m13 span{font:800 32px Inter;color:#f6dc9c;letter-spacing:2px}.m13 b{font:900 70px 'DejaVu Serif',serif}
.vch{position:absolute;left:180px;top:800px;width:720px;height:300px;border-radius:30px;background:#14110a;border:6px dashed #e0ac55;display:flex;align-items:center;justify-content:center;gap:34px;white-space:nowrap}
.vch b{font:900 150px 'DejaVu Serif',serif}
.vch span{font:800 34px Inter;color:#f1ead9;letter-spacing:2px;line-height:1.3}
.cal{position:absolute;left:310px;top:740px;width:460px;height:480px;border-radius:40px;background:#f2fbf7;color:#06261a;text-align:center;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.7),0 0 0 6px #6ff5c0;white-space:nowrap}
.cal .top{height:110px;background:#2bb683;color:#04140d;font:900 44px Inter;display:flex;align-items:center;justify-content:center;letter-spacing:3px}
.cal .d{font:900 200px 'DejaVu Serif',serif;line-height:1.15}
.cal .h{font:900 52px Inter;color:#c0392b}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:700 24px Inter;color:#9cc9b6;letter-spacing:2px}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'


def ntf(top, ic, t, s, v, g=None, fx='left'):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    return f'<div class="ntf" style="top:{top}px"{a}><div class="ic">{ic}</div><div class="tx">{t}<span>{s}</span></div><div class="v">{v}</div></div>'


MONTHS = '<div class="months" style="top:{top}px" data-g="2.2" data-fx="up">' + ''.join(f'<div><b>MOIS {k}</b><i>●●●●●</i></div>' for k in range(1, 13)) + '</div>'

BODY = hud('FRANCE · NOTIFICATIONS', 'HELLO BANK') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(215, [('h1 mt', 'PARRAINAGE HELLO BANK :', None, 'font-size:54px'), ('it gold', "jusqu'à", None, 'font-size:60px'), ('big gold', '330 €', None, 'font-size:140px'), ('it gold', "d'avantages.", None, 'font-size:60px')]) + '''
   <div class="chip" style="top:655px" data-g="0.2" data-fx="pop">IL RESTE 5 JOURS</div>
   ''' + ntf(780, '€', 'Prime de bienvenue', 'ouverture · Hello One ou Prime', '+80 €') + ntf(920, '€', 'Prime 13e mois', 'avec Hello Prime · sous conditions', '+50 €') + ntf(1060, '🎁', "Bon d'achat", 'mobilité Hello Start+', '200 €') + '''</div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('big gold', '80 €', '1.0', 'font-size:130px'), ('it mt', "à l'ouverture,", '1.0', 'font-size:60px'), ('it gold', 'avec Hello One ou Hello Prime.', '1.1', 'font-size:54px')]) + '''
   <div class="ph" data-g="1.0" data-fx="up"><div class="tt">CHOISIS TON OFFRE</div><div class="op o1" data-g="1.1" data-fx="left">HELLO ONE</div><div class="op o2" data-g="1.1" data-fx="right">HELLO PRIME</div><div class="bn" data-g="1.1" data-fx="stamp">+80 €</div></div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 mt', 'AVEC HELLO PRIME,', '2.0', 'font-size:64px'), ('it gold', '50 € de plus le 13e mois,', '2.1', 'font-size:60px')]) + MONTHS.format(top=470) + '''
   <div class="ex" style="top:830px" data-g="2.2" data-fx="fade">● = 1 paiement ou retrait par carte</div>
   ''' + hd(890, [('it mt', 'si tu paies avec ta carte', '2.2', 'font-size:56px'), ('it gold', 'au moins 5 fois par mois.', '2.3', 'font-size:56px')]) + '''
   <div class="m13" style="top:1090px" data-g="2.3" data-fx="stamp"><span>13e MOIS</span><b class="gold">+50 €</b></div>
   <div class="ex" style="top:1240px" data-g="2.3" data-fx="fade">sur les 12 premiers mois · offre Hello Prime</div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('it gold', 'Et si tu changes de banque', '3.0', 'font-size:64px'), ('it mt', 'avec Hello Start+,', '3.1', 'font-size:64px'), ('h1', "UN BON D'ACHAT DE", '3.2', 'font-size:50px')]) + '''
   <div class="chip" style="top:620px;left:190px;width:700px;background:#0b1913;color:#eafff6;border:4px solid #6ff5c0" data-g="3.0" data-fx="up">ANCIENNE BANQUE ➜ HELLO BANK</div>
   <div class="vch" data-g="3.2" data-fx="stamp" data-slow="3.2"><b class="gold">200 €</b><span>BON<br>D'ACHAT</span></div>
   <div class="ex" style="top:1150px" data-g="3.2" data-fx="fade">service de mobilité bancaire Hello Start+</div></div>
  <div class="scene" data-s="4" data-in="up">''' + hd(215, [('h1 mt', 'ATTENTION :', '4.0', 'font-size:76px'), ('it gold', "ta demande d'ouverture", '4.1', 'font-size:58px'), ('it gold', 'doit être faite avant', '4.2', 'font-size:58px')]) + '''
   <div class="cal" data-g="4.3" data-fx="pop"><div class="top">NOVEMBRE</div><div class="d">30</div><div class="h">AVANT 15 H</div></div>
   <div class="ex" style="top:1260px" data-g="4.3" data-fx="fade">via le lien de l'invitation envoyée par la banque</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« HELLO BANK »', '5.1', 'font-size:84px'), ('it mt', 'en privé,', '5.2', ''), ('it gold', "je t'envoie l'invitation.", '5.3', 'font-size:58px')]) + '''
   <div class="search" style="top:720px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:860px;font-size:24px">Offre soumise aux conditions en vigueur · nouveaux clients<br>Demande d'ouverture via l'invitation avant le 30/11/2026 à 15h<br>80 € (Hello One ou Hello Prime) + 50 € le 13e mois (Hello Prime),<br>sous réserve d'au moins 5 paiements ou retraits par mois<br>sur les 12 premiers mois · bon d'achat 200 € avec Hello Start+</div>
   ''' + ntf(1130, '€', "Jusqu'à 330 € d'avantages", 'illustration · sous conditions', '330 €', '5.3', 'up') + '''</div>
'''
