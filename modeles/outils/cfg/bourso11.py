import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# BoursoBank, 16/11/2026 21:00 - style v3 nuit & or, accent fuchsia. Offre filleul jusqu'à 180 €
# (boursobank.com/bon-plan/parrainage-boursobank, consultée le 16/11/2026, pas de date de fin ; comparabanques.fr mis à jour le 12/11) :
# 20 € ouverture + jusqu'à 40 € 1er versement (40 € dès 300 €) + jusqu'à 40 € paiements carte sur 3 mois + 80 € mobilité EasyMove.
# Voix : Speko (speechify, voix par défaut ; voix clonée refusée 402).
# Grille de 4 tuiles (2 x 2) éteintes -> chaque étape allume sa tuile (ouverture / virement / carte 3 mois / EasyMove)
# -> les 4 tuiles se rassemblent en un total 180 € (ralenti) -> appel à l'action.
NAME = 'bourso11'
TITLE = 'BoursoBank 4 etapes fuchsia'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Quatre étapes, cent quatre-vingts euros. Je t'explique.", [("4 étapes,", None), ("180 €.", None), ("Je t'explique.", None)]),
 ("Un : tu ouvres ton compte Bourso Bank. Vingt euros.", [("Un :", None), ("tu ouvres ton compte", None), ("BoursoBank.", None), ("20 €.", None)]),
 ("Deux : un premier versement de trois cents euros. Quarante euros.", [("Deux :", None), ("un premier versement", None), ("de 300 €.", None), ("40 €.", None)]),
 ("Trois : tu paies avec ta carte pendant trois mois. Jusqu'à quarante.", [("Trois :", None), ("tu paies avec ta carte", None), ("pendant 3 mois.", None), ("Jusqu'à 40.", None)]),
 ("Quatre : le transfert EasyMove. Quatre-vingts euros.", [("Quatre :", None), ("le transfert", None), ("EasyMove.", None), ("80 €.", None)]),
 ("Au total, jusqu'à cent quatre-vingts euros pour le filleul.", [("Au total,", None), ("jusqu'à 180 €", None), ("pour le filleul.", None)]),
 ("Envoie-moi BOURSO en privé, je t'envoie mon lien.", [("Envoie-moi", None), ("BOURSO", None), ("en privé,", None), ("je t'envoie mon lien.", None)]),
]
SPLITS = [(0.0, 2.74), (3.09, 5.67), (6.23, 8.92), (9.50, 12.53), (13.06, 15.35), (15.90, 18.08), (18.58, 20.29)]
GSTART = [[0.1, 0.9, 2.17], [3.1, 3.7, 4.4, 5.2], [6.23, 6.7, 7.5, 8.5], [9.5, 10.0, 10.8, 11.92], [13.1, 13.5, 14.0, 14.8], [15.9, 16.5, 17.5], [18.6, 18.9, 19.2, 19.7]]
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
.fu{color:#ff7cc6;text-shadow:0 0 18px rgba(255,95,184,.5)}
.tile{position:absolute;width:380px;height:280px;border-radius:30px;background:#16121a;border:4px solid #3b3442;text-align:center;padding-top:26px}
.tile .n{font:900 30px Inter;letter-spacing:5px;color:#5b544a;text-align:left;padding-left:30px}
.tile .ic{font:400 84px 'DejaVu Sans';line-height:1.25;color:#3b3442}
.tile .l{font:800 28px Inter;color:#5b544a;white-space:nowrap}
.tile .a{position:absolute;right:26px;top:16px;font:900 44px 'DejaVu Serif',serif;color:transparent}
.tile.on{background:linear-gradient(160deg,#3a1030,#1a0816);border-color:#ff5fb8;box-shadow:0 0 50px rgba(255,95,184,.4)}
.tile.on .n{color:#ffb3dd}.tile.on .ic{color:#ff7cc6}.tile.on .l{color:#fff}.tile.on .a{color:#f3c766}
.tile.done{border-color:#d9a24c;background:#1c1610}
.tile.done .n{color:#c9a46a}.tile.done .ic{color:#d9a24c}.tile.done .l{color:#e9e4da}.tile.done .a{color:#d9a24c}
.tile .q{position:absolute;left:0;top:100px;width:100%;font:900 90px Inter;color:#3b3442}
.sum{position:absolute;left:0;top:760px;width:1080px;text-align:center}
.sum .v{font:900 230px 'DejaVu Serif',serif;line-height:1.1}
.chips{position:absolute;left:150px;top:1080px;width:780px;display:flex;flex-wrap:wrap;gap:18px;justify-content:center}
.chips div{padding:14px 26px;border-radius:40px;border:3px solid #ff5fb8;font:800 30px Inter;color:#ffd6ee;white-space:nowrap;background:rgba(255,95,184,.08)}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
TILES = [('⌂', 'Ouverture', '20 €'), ('⇩', '1er versement', '40 €'), ('▭', 'Carte · 3 mois', '40 €'), ('⇄', 'EasyMove', '80 €')]
TX = [140, 560, 140, 560]
TY = [740, 740, 1060, 1060]


def grid(k, sid=None, hook=False):
    out = ''
    for i, (ic, l, a) in enumerate(TILES):
        st = f'left:{TX[i]}px;top:{TY[i]}px'
        if hook:
            out += f'<div class="tile" style="{st}"><div class="n">ÉTAPE {i + 1}</div><div class="q">?</div></div>'
            continue
        cls = 'tile done' if i < k else ('tile on' if i == k else 'tile')
        g = f' data-g="{sid}.0" data-fx="stamp"' if i == k else ''
        av = f'<div class="a" data-g="{sid}.3" data-fx="pop">{a}</div>' if i == k else f'<div class="a">{a if i < k else ""}</div>'
        out += f'<div class="{cls}" style="{st}"{g}>{av}<div class="n">ÉTAPE {i + 1}</div><div class="ic">{ic}</div><div class="l">{l}</div></div>'
    return out


BODY = hud('FRANCE · BANQUE EN LIGNE', '4 ÉTAPES') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(210, [('h1 fu', '4 ÉTAPES,', None, 'font-size:96px'), ('big gold', '180 €.', None, 'font-size:170px'), ('it gold', "Je t'explique.", None, 'font-size:72px')]) + grid(0, hook=True).replace('top:740px', 'top:780px').replace('top:1060px', 'top:1100px') + '''</div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1 fu', 'UN :', '1.0', 'font-size:84px'), ('it gold', 'tu ouvres ton compte', '1.1', 'font-size:70px'), ('h1', 'BOURSOBANK.', '1.2', 'font-size:70px'), ('big gold', '20 €.', '1.3', 'font-size:100px')]) + grid(0, 1).replace('top:740px', 'top:800px').replace('top:1060px', 'top:1110px') + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 fu', 'DEUX :', '2.0', 'font-size:84px'), ('it gold', 'un premier versement', '2.1', 'font-size:70px'), ('it gold', 'de 300 €.', '2.2', 'font-size:70px'), ('big gold', '40 €.', '2.3', 'font-size:100px')]) + grid(1, 2).replace('top:740px', 'top:800px').replace('top:1060px', 'top:1110px') + '''</div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('h1 fu', 'TROIS :', '3.0', 'font-size:84px'), ('it gold', 'tu paies avec ta carte', '3.1', 'font-size:66px'), ('it gold', 'pendant 3 mois.', '3.2', 'font-size:66px'), ('big gold', "Jusqu'à 40.", '3.3', 'font-size:90px')]) + grid(2, 3).replace('top:740px', 'top:800px').replace('top:1060px', 'top:1110px') + '''</div>
  <div class="scene" data-s="4" data-in="right">''' + hd(230, [('h1 fu', 'QUATRE :', '4.0', 'font-size:84px'), ('it gold', 'le transfert', '4.1', 'font-size:70px'), ('h1', 'EASYMOVE.', '4.2', 'font-size:70px'), ('big gold', '80 €.', '4.3', 'font-size:100px')]) + grid(3, 4).replace('top:740px', 'top:800px').replace('top:1060px', 'top:1110px') + '''</div>
  <div class="scene" data-s="5" data-in="pop"><div class="rays" style="top:640px"></div>''' + hd(230, [('h1', 'AU TOTAL,', '5.0', ''), ('it gold', 'pour le filleul.', '5.2', 'font-size:72px')]) + '''
   <div class="sum" data-g="5.1" data-fx="stamp" data-slow="5.1" data-count="180"><div class="it fu" style="font-size:66px">jusqu'à</div><div class="v gold">0 €</div></div>
   <div class="chips" style="top:1150px"><div data-g="5.0" data-fx="pop">20 ouverture</div><div data-g="5.0" data-fx="pop">40 versement</div><div data-g="5.0" data-fx="pop">40 carte</div><div data-g="5.0" data-fx="pop">80 EasyMove</div></div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« BOURSO »', '6.1', 'font-size:120px'), ('it gold', 'en privé,', '6.2', '')]) + '''
   <div class="pill" style="top:760px;border-color:rgba(255,95,184,.8)" data-g="6.3" data-fx="up"><div class="pin" style="background:#ff5fb8;color:#fff">✉</div><div><b>JE T'ENVOIE MON LIEN</b><span>jusqu'à 180 € pour le filleul</span></div></div>
   <div class="search" style="top:900px" data-g="6.3" data-fx="fade">''' + SEARCH + '''<span data-g="6.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1040px">Offre soumise aux conditions en vigueur<br>jusqu'à 180 € pour le filleul (nouveau client, compte individuel) :<br>20 € ouverture + jusqu'à 40 € 1er versement (40 € dès 300 €)<br>+ jusqu'à 40 € paiements carte sur 3 mois + 80 € EasyMove</div></div>
'''
