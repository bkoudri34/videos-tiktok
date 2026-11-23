import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# BoursoBank, 23/11/2026 18:00 - style v3 nuit & or, accent violet améthyste. Format F8 « résultat d'abord » :
# relevé de compte illustré « +260,00 € » dès la 1re image -> le relevé se remplit ligne par ligne (20 € ouverture,
# 80 € versement >= 300 €, 80 € carte 3 mois, 80 € EasyMove) avec le solde qui monte -> total 260 € (ralenti) -> appel à l'action.
# Offre parrainage filleul jusqu'à 260 € (boursobank.com/bon-plan/parrainage-boursobank, consultée le 23/11/2026) :
# 20 € ouverture + 80 € 1er versement >= 300 € (dans les 30 jours) + 80 € carte (20 + 30 + 30 sur 3 mois) + 80 € 1re mobilité EasyMove.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'bourso15'
TITLE = 'BoursoBank releve amethyste'
ROOT = ':root{--bg:#07050c}'
LINES = [
 ("Parrainage Bourso Bank : deux cent soixante euros, voilà le résultat.", [("Parrainage BoursoBank :", None), ("260 €,", None), ("voilà le résultat.", None)]),
 ("Vingt euros, juste pour ouvrir ton compte.", [("20 €,", None), ("juste pour ouvrir ton compte.", None)]),
 ("Quatre-vingts euros si tu verses au moins trois cents euros.", [("80 €", None), ("si tu verses au moins 300 €.", None)]),
 ("Quatre-vingts euros avec un paiement par carte chaque mois, pendant trois mois.", [("80 €", None), ("avec un paiement par carte", None), ("chaque mois, pendant 3 mois.", None)]),
 ("Et quatre-vingts euros avec la mobilité Easy Move.", [("Et 80 €", None), ("avec la mobilité EasyMove.", None)]),
 ("Total : deux cent soixante euros pour le filleul.", [("Total :", None), ("260 €", None), ("pour le filleul.", None)]),
 ("Envoie-moi BOURSO en privé, je t'envoie le lien.", [("Envoie-moi", None), ("BOURSO", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 2.92), (3.47, 5.06), (5.53, 7.47), (7.95, 10.70), (11.20, 13.29), (13.75, 15.74), (16.29, 18.0)]
GSTART = [[0.0, 1.2, 2.3], [3.5, 4.0], [5.55, 6.2], [7.97, 8.6, 9.6], [11.22, 12.0], [13.77, 14.45, 15.2], [16.3, 16.6, 17.0, 17.4]]
MINLEN = 1.9
GAP = 0.3
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px;left:90px;width:840px">' + ''.join(out) + '</div>'


CSS = '''
.am{color:#c49bff;text-shadow:0 0 18px rgba(170,110,255,.55)}
.rel{position:absolute;left:150px;width:760px;border-radius:34px;background:#f4f1fa;color:#1d1430;padding:30px 40px 26px;box-shadow:0 30px 80px rgba(0,0,0,.7),0 0 0 5px rgba(196,155,255,.55);white-space:nowrap}
.rel .t{display:flex;justify-content:space-between;align-items:center;font:800 28px Inter;color:#5b4a7a;letter-spacing:2px}
.rel .t i{font-style:normal;font:700 22px 'DejaVu Sans Mono',monospace;color:#8a7aa8}
.rel .row{display:flex;justify-content:space-between;align-items:center;height:74px;border-bottom:2px dashed #cfc5e4;font:700 30px Inter}
.rel .row b{font:900 38px 'DejaVu Serif',serif;color:#1f9a63}
.rel .row.hi{background:#ece2ff;padding:0 14px;border-radius:14px}
.rel .bal{display:flex;justify-content:space-between;align-items:center;margin-top:14px;font:800 30px Inter;color:#5b4a7a}
.rel .bal b{font:900 64px 'DejaVu Serif',serif;color:#1d1430}
.ntf{position:absolute;left:170px;width:720px;height:120px;border-radius:32px;background:#1a1030;border:4px solid #c49bff;display:flex;align-items:center;gap:22px;padding:0 30px;white-space:nowrap;color:#f2ecff}
.ntf .ic{flex:none;width:68px;height:68px;border-radius:18px;background:#7d4dd6;display:flex;align-items:center;justify-content:center;font:900 38px Inter}
.ntf .tx{flex:1;font:800 32px Inter}.ntf .tx span{display:block;font:600 22px Inter;color:#b9a8dc}
.ntf .v{font:900 46px 'DejaVu Serif',serif;color:#7ff0b0}
.tot{position:absolute;left:0;width:1080px;text-align:center}
.tot .v{font:900 200px 'DejaVu Serif',serif;line-height:1}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:700 24px Inter;color:#a99cc4;letter-spacing:3px}
.ring{position:absolute;left:390px;top:800px;width:300px;height:300px}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
ROWS = [('Prime ouverture', 20), ('1er versement ≥ 300 €', 80), ('Carte · 3 mois', 80), ('Mobilité EasyMove', 80)]


def rel(top, n, gi=None, final=False):
    """statement with n rows visible; row n-1 animated at group gi.1 when gi given"""
    rows = ''
    bal = 0
    for k, (lab, v) in enumerate(ROWS[:n]):
        bal += v
        cls = 'row hi' if (k == n - 1 and not final) else 'row'
        a = f' data-g="{gi}.0" data-fx="left"' if (gi is not None and k == n - 1) else ''
        rows += f'<div class="{cls}"{a}><span>{lab}</span><b>+{v},00 €</b></div>'
    ba = f' data-g="{gi}.0" data-fx="tick"' if gi is not None else ''
    return (f'<div class="rel" style="top:{top}px"><div class="t">RELEVÉ · FILLEUL<i>ILLUSTRATION</i></div>{rows}'
            f'<div class="bal"><span>Primes cumulées</span><b{ba}>{bal},00 €</b></div></div>')


BODY = hud('FRANCE · RELEVÉ FILLEUL', 'BOURSOBANK') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(205, [('h1 am', 'PARRAINAGE BOURSOBANK :', None, 'font-size:52px'), ('big gold', '260 €,', None, 'font-size:150px'), ('it gold', 'voilà le résultat.', None, 'font-size:70px')]) + '''
   ''' + rel(700, 4, final=True) + '''</div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('big gold', '20 €,', '1.0', 'font-size:130px'), ('it am', 'juste pour ouvrir ton compte.', '1.1', 'font-size:60px')]) + rel(640, 1, 1) + '''
   <div class="ntf" style="top:1000px" data-g="1.1" data-fx="up"><div class="ic">✓</div><div class="tx">Compte ouvert<span>1re ouverture · compte individuel</span></div><div class="v">+20 €</div></div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('big gold', '80 €', '2.0', 'font-size:130px'), ('it am', 'si tu verses au moins 300 €.', '2.1', 'font-size:60px')]) + rel(640, 2, 2) + '''
   <div class="ex" style="top:1090px" data-g="2.1" data-fx="fade">1er versement dans les 30 jours après l'ouverture</div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('big gold', '80 €', '3.0', 'font-size:130px'), ('it am', 'avec un paiement par carte', '3.1', 'font-size:58px'), ('it gold', 'chaque mois, pendant 3 mois.', '3.2', 'font-size:56px')]) + rel(720, 3, 3) + '''
   <div class="ex" style="top:1240px" data-g="3.2" data-fx="fade">20 € + 30 € + 30 € · 1 opération carte par mois</div></div>
  <div class="scene" data-s="4" data-in="up">''' + hd(230, [('big gold', 'Et 80 €', '4.0', 'font-size:130px'), ('it am', 'avec la mobilité EasyMove.', '4.1', 'font-size:60px')]) + rel(640, 4, 4) + '''
   <div class="ex" style="top:1170px" data-g="4.1" data-fx="fade">changement de banque · 1re utilisation d'EasyMove</div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="rays" style="top:640px"></div>''' + hd(230, [('h1 am', 'TOTAL :', '5.0', 'font-size:80px')]) + '''
   <div class="tot" style="top:420px" data-g="5.1" data-fx="stamp" data-slow="5.1" data-count="260"><div class="v gold">0 €</div></div>
   <div class="hd" style="top:660px;left:90px;width:840px"><div class="it am" style="font-size:72px" data-g="5.2" data-fx="tw">pour le filleul.</div></div>
   <div class="ex" style="top:800px;font-size:26px" data-g="5.2" data-fx="fade">20 + 80 + 80 + 80 € · conditions remplies</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« BOURSO »', '6.1', 'font-size:110px'), ('it am', 'en privé,', '6.2', ''), ('it gold', "je t'envoie le lien.", '6.3', 'font-size:64px')]) + '''
   <div class="search" style="top:720px" data-g="6.3" data-fx="fade">''' + SEARCH + '''<span data-g="6.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:860px;font-size:24px">Offre soumise aux conditions en vigueur<br>Jusqu'à 260 € pour le filleul : 1re ouverture d'un compte individuel,<br>1er versement d'au moins 300 € sous 30 jours, 1 opération carte<br>par mois pendant 3 mois, 1re mobilité EasyMove</div>
   <div class="ntf" style="top:1080px" data-g="6.3" data-fx="up"><div class="ic">€</div><div class="tx">Primes cumulées<span>illustration · relevé filleul</span></div><div class="v">+260 €</div></div></div>
'''
