import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# BoursoBank, 11/11/2026 21:00 - style v3 nuit & or, accent saphir. Offre de bienvenue jusqu'à 180 € (code BBKOPE180, boursobank.com consulté le 11/11/2026) :
# 20 € ouverture + jusqu'à 40 € selon le 1er versement (40 € dès 300 €) + jusqu'à 40 € carte (1 opération/mois pendant 3 mois) + 80 € EasyMove.
# Tour de briques qui se construit étape par étape -> appel à l'action.
NAME = 'bourso8'
TITLE = 'BoursoBank 180 euros saphir'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Cent quatre-vingts euros, en quatre petites étapes.", [("180 €,", None), ("en 4 petites étapes.", None)]),
 ("Vingt euros dès que ton compte BoursoBank est ouvert.", [("20 €", None), ("dès que ton compte", None), ("BoursoBank est ouvert.", None)]),
 ("Jusqu'à quarante euros selon ton premier versement.", [("Jusqu'à 40 €", None), ("selon ton", None), ("premier versement.", None)]),
 ("Encore quarante euros si tu utilises ta carte pendant trois mois.", [("Encore 40 €", None), ("si tu utilises ta carte", None), ("pendant 3 mois.", None)]),
 ("Et quatre-vingts euros avec le changement de banque EasyMove.", [("Et 80 €", None), ("avec le changement de banque", None), ("EasyMove.", None)]),
 ("Envoie-moi BOURSO en privé, je t'envoie le lien.", [("Envoie-moi", None), ("BOURSO", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 2.319), (2.80, 4.922), (5.34, 7.645), (7.994, 10.935), (11.299, 13.938), (14.312, 16.726)]
GSTART = [[0.1, 1.35], [2.81, 3.2, 3.9], [5.35, 6.3, 6.8], [8.0, 9.1, 10.2], [11.3, 12.1, 13.3], [14.32, 14.8, 15.3, 15.94]]
MINLEN = 2.4
GAP = 0.36
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.sa{color:#6fa8ff;text-shadow:0 0 18px rgba(111,168,255,.45)}
.tw{position:absolute;left:290px;top:860px;width:500px;height:580px;border-bottom:8px solid #d9a24c}
.slot{position:absolute;left:0;width:500px;border:3px dashed rgba(217,162,76,.45);border-radius:14px;display:flex;align-items:center;justify-content:center;font:900 60px 'DejaVu Serif',serif;color:rgba(217,162,76,.5)}
.bk{position:absolute;left:0;width:500px;border-radius:14px;display:flex;align-items:center;justify-content:space-between;padding:0 30px;white-space:nowrap;box-shadow:0 16px 40px rgba(0,0,0,.6)}
.bk b{font:900 54px 'DejaVu Serif',serif}
.bk span{font:800 26px Inter;letter-spacing:3px}
.b1{background:linear-gradient(180deg,#fff1c4,#c8892c);color:#2a1a05}
.b2{background:linear-gradient(180deg,#a9cbff,#3d6fd1);color:#07142e}
.b3{background:linear-gradient(180deg,#f6dc8e,#a8701f);color:#2a1a05}
.b4{background:linear-gradient(180deg,#8fbaff,#244a9a);color:#fff}
.tot{position:absolute;left:250px;top:700px;width:580px;text-align:center;white-space:nowrap}
'''
# tower geometry (inside .tw, bottom = 580): heights 70/120/120/240
GEO = [(510, 70, '20 €', 'OUVERTURE', 'b1'), (390, 120, '40 €', '1ER VERSEMENT', 'b2'), (270, 120, '40 €', 'CARTE · 3 MOIS', 'b3'), (30, 240, '80 €', 'EASYMOVE', 'b4')]


def tower(upto, g=None, slow=False):
    h = '<div class="tw">'
    for k, (top, ht, v, lab, c) in enumerate(GEO):
        if k < upto:
            h += f'<div class="bk {c}" style="top:{top}px;height:{ht}px"><b>{v}</b><span>{lab}</span></div>'
        elif k == upto and g:
            sl = f' data-slow="{g}"' if slow else ''
            h += f'<div class="bk {c}" style="top:{top}px;height:{ht}px" data-g="{g}" data-fx="stamp"{sl}><b>{v}</b><span>{lab}</span></div>'
        else:
            h += f'<div class="slot" style="top:{top}px;height:{ht}px">?</div>'
    return h + '</div>'


BODY = hud('FRANCE · BANQUE EN LIGNE', 'BIENVENUE') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('big gold', '180 €', None, 'font-size:190px'), ('it gold', 'en 4 petites étapes.', None, 'font-size:76px')]) + tower(0) + '''</div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('big gold', '20 €', '1.0', 'font-size:140px'), ('h1 s', 'DÈS QUE TON COMPTE', '1.1', ''), ('it gold', 'BoursoBank est ouvert.', '1.2', 'font-size:66px')]) + tower(0, '1.0') + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('big gold', "jusqu'à 40 €", '2.0', 'font-size:120px'), ('h1 s', 'SELON TON', '2.1', ''), ('it gold', 'premier versement.', '2.2', 'font-size:66px')]) + tower(1, '2.0') + '''</div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('big gold', 'encore 40 €', '3.0', 'font-size:120px'), ('h1 s', 'SI TU UTILISES TA CARTE', '3.1', 'font-size:58px'), ('it gold', 'pendant 3 mois.', '3.2', 'font-size:66px')]) + tower(2, '3.0') + '''</div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:560px"></div>''' + hd(230, [('big gold', 'et 80 €', '4.0', 'font-size:120px'), ('h1 s', 'CHANGEMENT DE BANQUE', '4.1', 'font-size:58px'), ('it gold', 'EasyMove.', '4.2', 'font-size:66px')]) + tower(3, '4.0', True).replace('class="tw"', 'class="tw" style="top:900px"') + '''
   <div class="abs sa" style="left:0;top:640px;width:1080px;text-align:center;font:900 46px Inter;letter-spacing:4px" data-g="4.2" data-fx="pop">= 180 € MAX</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« BOURSO »', '5.1', 'font-size:130px'), ('it gold', 'en privé.', '5.2', '')]) + '''
   <div class="pill" style="top:720px;border-color:rgba(111,168,255,.85)" data-g="5.2" data-fx="up"><div class="pin" style="background:#6fa8ff">€</div><div><b>JUSQU'À 180 €</b><span>offre de bienvenue · 4 étapes</span></div></div>
   <div class="pill" style="top:845px" data-g="5.3" data-fx="up"><div class="pin">✉</div><div><b>JE T'ENVOIE LE LIEN</b><span>en privé sur @htm.invest</span></div></div>
   <div class="cond" style="top:1000px">Offre soumise aux conditions en vigueur<br>BoursoBank : nouveaux clients, montant maximum<br>(40 € pour un 1er versement de 300 € ou plus)</div></div>
'''
