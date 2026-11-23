import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Hello bank, 23/11/2026 21:00 - style v3 nuit & or, accent bleu glacier. Format F2 « démystification » (comment ça marche vraiment) :
# schéma en 3 étapes avec points d'interrogation dès la 1re image -> étape 1 : invitation envoyée par la banque (e-mail illustré)
# -> étape 2 : ouverture Hello One ou Hello Prime avec le lien, avant le 30/11 -> 80 € + 50 € le 13e mois (Hello Prime)
# -> bon d'achat 200 € avec Hello Start+ -> jusqu'à 330 € (ralenti) -> appel à l'action, schéma complet qui reboucle.
# Offre parrainage filleul (hellobank.fr/fr/votre-offre-parrainage, consultée le 23/11/2026) : invitation envoyée par la banque,
# ouverture en ligne via le lien, 80 € Hello One ou Hello Prime, + 50 € le 13e mois avec Hello Prime (au moins 5 paiements ou retraits
# par mois sur les 12 premiers mois), bon d'achat 200 € (mobilité Hello Start+), « jusqu'à 330 € d'avantages », avant le 30/11/2026 à 15h.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'hellobank15'
TITLE = 'Hello bank schema glacier'
ROOT = ':root{--bg:#04070b}'
LINES = [
 ("Parrainage Hello bank : comment ça marche vraiment ?", [("Parrainage Hello bank :", None), ("comment ça marche vraiment ?", None)]),
 ("Étape un : ton parrain t'envoie une invitation, directement par la banque.", [("Étape 1 :", None), ("ton parrain t'envoie une invitation,", None), ("directement par la banque.", None)]),
 ("Étape deux : tu ouvres Hello One ou Hello Prime avec ce lien, avant le trente novembre.", [("Étape 2 :", None), ("tu ouvres Hello One ou Hello Prime", None), ("avec ce lien,", None), ("avant le 30 novembre.", None)]),
 ("Quatre-vingts euros de prime. Avec Hello Prime, cinquante euros de plus le treizième mois.", [("80 € de prime.", None), ("Avec Hello Prime,", None), ("50 € de plus le 13e mois.", None)]),
 ("Tu changes de banque avec Hello Start plus ? Deux cents euros en bon d'achat.", [("Tu changes de banque", None), ("avec Hello Start+ ?", None), ("200 € en bon d'achat.", None)]),
 ("Au total : jusqu'à trois cent trente euros d'avantages, sous conditions.", [("Au total :", None), ("jusqu'à 330 € d'avantages,", None), ("sous conditions.", None)]),
 ("Envoie-moi HELLO BANK en privé, je t'envoie l'invitation.", [("Envoie-moi", None), ("HELLO BANK", None), ("en privé,", None), ("je t'envoie l'invitation.", None)]),
]
SPLITS = [(0.0, 2.04), (2.57, 5.57), (6.17, 10.12), (10.51, 14.18), (14.76, 17.71), (18.13, 20.69), (21.41, 23.25)]
GSTART = [[0.0, 1.26], [2.57, 3.29, 4.6], [6.17, 6.95, 8.4, 9.27], [10.51, 12.0, 12.8], [14.76, 15.5, 16.69], [18.13, 18.6, 20.2], [21.41, 21.75, 22.1, 22.55]]
MINLEN = 1.9
GAP = 0.28
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px;left:90px;width:840px">' + ''.join(out) + '</div>'


CSS = '''
.gl{color:#7fd6ff;text-shadow:0 0 18px rgba(90,190,255,.55)}
.flow{position:absolute;left:190px;top:700px;width:700px}
.flow .st{height:120px;margin-bottom:34px;border-radius:30px;background:#0b1520;border:4px solid #2f5f80;display:flex;align-items:center;gap:26px;padding:0 30px;font:800 36px Inter;color:#e6f4ff;white-space:nowrap;position:relative}
.flow .st i{flex:none;width:70px;height:70px;border-radius:50%;background:#7fd6ff;color:#04121c;font:900 38px Inter;font-style:normal;display:flex;align-items:center;justify-content:center}
.flow .st b{margin-left:auto;font:900 60px 'DejaVu Serif',serif;color:#f3c766}
.flow .st:not(:last-child):after{content:'';position:absolute;left:63px;bottom:-38px;width:6px;height:38px;background:#2f5f80}
.mail{position:absolute;left:170px;top:720px;width:740px;border-radius:30px;background:#f2f8fc;color:#0d1a24;padding:30px 36px;box-shadow:0 30px 80px rgba(0,0,0,.7),0 0 0 5px rgba(127,214,255,.6);white-space:nowrap}
.mail .h{display:flex;gap:20px;align-items:center}
.mail .av{width:76px;height:76px;border-radius:50%;background:#1d7fb8;color:#fff;font:900 40px Inter;display:flex;align-items:center;justify-content:center}
.mail .f{font:800 32px Inter}.mail .f span{display:block;font:600 22px Inter;color:#5a6f80}
.mail .o{margin-top:22px;font:800 31px Inter}
.mail .btn{margin-top:22px;height:84px;border-radius:42px;background:#1d7fb8;color:#fff;font:900 34px Inter;display:flex;align-items:center;justify-content:center;letter-spacing:2px}
.ph{position:absolute;left:300px;top:760px;width:480px;height:560px;border-radius:56px;background:#0b1118;border:10px solid #27313c;box-shadow:0 30px 90px rgba(0,0,0,.7);text-align:center;color:#e6f4ff;white-space:nowrap}
.ph .tt{margin-top:56px;font:800 30px Inter;color:#8fb6cf;letter-spacing:2px}
.ph .op{margin:26px auto 0;width:380px;height:110px;border-radius:26px;display:flex;align-items:center;justify-content:center;font:900 40px Inter}
.ph .o1{background:#123048;border:4px solid #7fd6ff}
.ph .o2{background:#2a2110;border:4px solid #e0ac55;color:#f6dc9c}
.ph .lk{margin-top:30px;font:700 24px 'DejaVu Sans Mono',monospace;color:#7fd6ff}
.cal{position:absolute;left:290px;width:500px;height:96px;border-radius:24px;background:#e6f4ff;color:#06202f;display:flex;align-items:center;justify-content:center;font:900 38px Inter;white-space:nowrap;box-shadow:0 0 0 5px #1d7fb8}
.tl2{position:absolute;top:740px;width:320px;height:330px;border-radius:34px;text-align:center;padding-top:40px;white-space:nowrap}
.tl2 .t{font:800 30px Inter;color:#cfe9f8;letter-spacing:2px}
.tl2 .v{margin-top:28px;font:900 84px 'DejaVu Serif',serif}
.tl2 .s{margin-top:18px;font:700 24px Inter;color:#8fb6cf}
.ta{left:170px;background:#0b1520;border:4px solid #7fd6ff}
.tb{left:580px;background:#1a150a;border:4px solid #e0ac55}
.vch{position:absolute;left:200px;top:820px;width:680px;height:260px;border-radius:30px;background:#141008;border:6px dashed #e0ac55;display:flex;align-items:center;justify-content:center;gap:34px;white-space:nowrap}
.vch b{font:900 130px 'DejaVu Serif',serif}
.vch span{font:800 34px Inter;color:#f1ead9;letter-spacing:2px;line-height:1.3}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:700 24px Inter;color:#8fb6cf;letter-spacing:2px}
.tot{position:absolute;left:0;width:1080px;text-align:center}
.tot .v{font:900 200px 'DejaVu Serif',serif;line-height:1}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'


def flow(vals, gs=None, top=700):
    labs = ['Invitation', 'Ouverture', 'Prime']
    out = f'<div class="flow" style="top:{top}px">'
    for k in range(3):
        a = f' data-g="{gs[k]}" data-fx="left"' if gs else ''
        out += f'<div class="st"{a}><i>{k + 1}</i>{labs[k]}<b>{vals[k]}</b></div>'
    return out + '</div>'


BODY = hud('FRANCE · MODE D\'EMPLOI', 'HELLO BANK') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(225, [('h1 gl', 'PARRAINAGE HELLO BANK :', None, 'font-size:54px'), ('it gold', 'comment ça marche', None, 'font-size:80px'), ('it gold', 'vraiment ?', None, 'font-size:80px')]) + flow(['?', '?', '?']) + '''</div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1 gl', 'ÉTAPE 1 :', '1.0', 'font-size:76px'), ('it gold', "ton parrain t'envoie", '1.1', 'font-size:64px'), ('it gold', 'une invitation,', '1.1', 'font-size:64px')]) + '''
   <div class="mail" data-g="1.1" data-fx="up"><div class="h"><div class="av">✉</div><div class="f">Invitation de parrainage<span>envoyée par la banque · illustration</span></div></div>
    <div class="o">Ton parrain t'invite à ouvrir un compte</div><div class="btn">OUVRIR MON COMPTE</div></div>
   <div class="hd" style="top:1180px;left:90px;width:840px"><div class="it gl" style="font-size:56px" data-g="1.2" data-fx="tw">directement par la banque.</div></div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 gl', 'ÉTAPE 2 :', '2.0', 'font-size:76px'), ('it gold', 'tu ouvres Hello One', '2.1', 'font-size:60px'), ('it gold', 'ou Hello Prime', '2.1', 'font-size:60px')]) + '''
   <div class="ph" data-g="2.1" data-fx="up"><div class="tt">CHOISIS TON OFFRE</div><div class="op o1">HELLO ONE</div><div class="op o2">HELLO PRIME</div>
    <div class="lk" data-g="2.2" data-fx="fade">✓ via le lien d'invitation</div></div>
   <div class="cal" style="top:1350px" data-g="2.3" data-fx="pop">AVANT LE 30/11 · 15H</div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('big gold', '80 €', '3.0', 'font-size:120px'), ('it gl', 'de prime.', '3.0', 'font-size:62px')]) + '''
   <div class="tl2 ta" data-g="3.0" data-fx="left"><div class="t">OUVERTURE</div><div class="v gold">80 €</div><div class="s">One ou Prime</div></div>
   <div class="tl2 tb" data-g="3.2" data-fx="right"><div class="t">13e MOIS</div><div class="v gold">+50 €</div><div class="s">avec Hello Prime</div></div>
   <div class="hd" style="top:1110px;left:90px;width:840px"><div class="it gold" style="font-size:54px" data-g="3.2" data-fx="tw">50 € de plus le 13e mois.</div></div>
   <div class="ex" style="top:1200px;left:140px;width:800px;line-height:1.4" data-g="3.2" data-fx="fade">sous conditions : au moins 5 paiements<br>ou retraits par mois, 12 premiers mois</div></div>
  <div class="scene" data-s="4" data-in="up">''' + hd(230, [('it gold', 'Tu changes de banque', '4.0', 'font-size:70px'), ('it gl', 'avec Hello Start+ ?', '4.1', 'font-size:70px')]) + '''
   <div class="vch" data-g="4.2" data-fx="stamp"><b class="gold">200 €</b><span>BON<br>D'ACHAT</span></div>
   <div class="ex" style="top:1130px" data-g="4.2" data-fx="fade">service de mobilité bancaire Hello Start+</div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="rays" style="top:300px"></div>''' + hd(215, [('h1 gl', 'AU TOTAL :', '5.0', 'font-size:72px'), ('it gold', "jusqu'à", '5.1', 'font-size:66px')]) + '''
   <div class="tot" style="top:400px" data-g="5.1" data-fx="stamp" data-slow="5.1" data-count="330"><div class="v gold">0 €</div></div>
   <div class="hd" style="top:620px;left:90px;width:840px"><div class="it gl" style="font-size:62px" data-g="5.2" data-fx="tw">sous conditions.</div></div>''' + flow(['✓', '✓', '330 €'], ['5.1', '5.1', '5.1'], 780) + '''</div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« HELLO BANK »', '6.1', 'font-size:84px'), ('it gl', 'en privé,', '6.2', ''), ('it gold', "je t'envoie l'invitation.", '6.3', 'font-size:58px')]) + '''
   <div class="search" style="top:720px" data-g="6.3" data-fx="fade">''' + SEARCH + '''<span data-g="6.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:860px;font-size:24px">Offre soumise aux conditions en vigueur · nouveaux clients<br>Invitation et demande d'ouverture avant le 30/11/2026 à 15h<br>80 € (Hello One ou Hello Prime) + 50 € le 13e mois (Hello Prime),<br>sous réserve d'au moins 5 paiements ou retraits par mois<br>sur les 12 premiers mois · bon d'achat 200 € avec Hello Start+</div>
   <div class="pill" style="top:1130px;left:160px;width:750px;border-color:rgba(127,214,255,.85)" data-g="6.3" data-fx="up"><div class="pin" style="background:#1d7fb8;color:#fff">✉</div><div><b>L'INVITATION PART DE LA BANQUE</b><span>je t'envoie le lien en privé</span></div></div></div>
'''
