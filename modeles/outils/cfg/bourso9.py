import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# BoursoBank, 13/11/2026 18:00 - style v3 nuit & or, accent turquoise. Offre de parrainage filleul jusqu'à 180 €
# (comparabanques.fr, page mise à jour le 10/11/2026 : offre continue, étapes ouverture + 1er versement, carte 3 mois, mobilité EasyMove).
# Pas de détail par étape à l'écran (montants variables selon le 1er versement). Voix : Speko (speechify, voix par défaut).
# Coffret vide « ta banque » -> coffret BoursoBank 180 € -> checklist 3 étapes cochées une par une -> appel à l'action.
NAME = 'bourso9'
TITLE = 'BoursoBank 180 euros turquoise'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Ta banque actuelle t'a déjà offert quelque chose ?", [("Ta banque actuelle", None), ("t'a déjà offert", None), ("quelque chose ?", None)]),
 ("Bourso Bank, elle, offre jusqu'à cent quatre-vingts euros.", [("BoursoBank, elle,", None), ("offre jusqu'à", None), ("180 €.", None)]),
 ("Étape un : tu ouvres ton compte et tu fais ton premier versement.", [("Étape 1 :", None), ("tu ouvres ton compte", None), ("et tu fais ton premier versement.", None)]),
 ("Étape deux : tu utilises ta carte chaque mois, pendant trois mois.", [("Étape 2 :", None), ("tu utilises ta carte", None), ("chaque mois, pendant 3 mois.", None)]),
 ("Étape trois : tu transfères ton ancien compte avec EasyMove.", [("Étape 3 :", None), ("tu transfères ton ancien compte", None), ("avec EasyMove.", None)]),
 ("Envoie-moi BOURSO en privé, je t'envoie mon lien.", [("Envoie-moi", None), ("BOURSO", None), ("en privé,", None), ("je t'envoie mon lien.", None)]),
]
SPLITS = [(0.0, 1.86), (2.27, 4.73), (5.25, 8.40), (8.89, 11.69), (12.15, 14.62), (14.88, 16.61)]
GSTART = [[0.05, 0.7, 1.3], [2.27, 3.3, 3.9], [5.25, 6.0, 7.2], [8.89, 9.6, 10.4], [12.15, 12.8, 13.9], [14.88, 15.2, 15.5, 16.0]]
MINLEN = 2.2
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
.tq{color:#2ed3c6;text-shadow:0 0 18px rgba(46,211,198,.45)}
.bx{position:absolute;left:290px;width:500px;height:360px;border-radius:14px;background:linear-gradient(160deg,#1e2a2a,#0c1212);border:5px solid #d9a24c;box-shadow:0 40px 90px rgba(0,0,0,.7)}
.bx .rb{position:absolute;left:225px;top:0;width:50px;height:100%;background:linear-gradient(90deg,#1b9d93,#2ed3c6,#1b9d93)}
.lid{position:absolute;left:270px;width:540px;height:90px;border-radius:12px;background:linear-gradient(160deg,#2a3838,#121a1a);border:5px solid #d9a24c;transform-origin:0 100%}
.lid .rb{position:absolute;left:245px;top:0;width:50px;height:100%;background:#2ed3c6}
.tagz{position:absolute;left:330px;top:1340px;width:420px;text-align:center;font:900 64px 'DejaVu Sans Mono',monospace;color:#7d7466}
.tagz small{display:block;font:700 26px Inter;letter-spacing:5px;color:#7d7466}
.dust{position:absolute;color:#6a6255;font:400 30px 'DejaVu Sans'}
.ck{position:absolute;left:130px;top:700px;width:820px;border-radius:34px;background:#f2f6f5;color:#0e1a1a;padding:34px 40px 30px;box-shadow:0 40px 100px rgba(0,0,0,.75)}
.ck .t{font:800 26px 'DejaVu Sans Mono',monospace;letter-spacing:6px;color:#178a81;margin-bottom:10px}
.ck .r{display:flex;align-items:center;gap:26px;padding:24px 0;border-bottom:2px dashed rgba(14,26,26,.2);white-space:nowrap}
.ck .r:last-child{border-bottom:0}
.ck .b{flex:none;width:70px;height:70px;border-radius:18px;border:5px solid #178a81;display:flex;align-items:center;justify-content:center;font:900 46px Inter;color:#fff}
.ck .b i{display:flex;width:100%;height:100%;align-items:center;justify-content:center;background:#178a81;border-radius:10px;font-style:normal}
.ck .x b{display:block;font:800 36px Inter}
.ck .x span{font:600 26px Inter;color:#5d6b6a}
.ck .r.on{background:rgba(46,211,198,.16);border-radius:16px;margin:0 -14px;padding-left:14px;padding-right:14px}
.dots{display:flex;gap:16px;justify-content:center;margin-top:30px}
.dots div{width:150px;height:62px;border-radius:31px;border:3px solid #2ed3c6;font:800 26px Inter;color:#2ed3c6;display:flex;align-items:center;justify-content:center}
'''

STEPS = [("Ouvrir le compte", "+ 1er versement"), ("Utiliser la carte", "1 opération / mois · 3 mois"), ("EasyMove", "transfert de ton ancien compte")]


def checklist(k, g):
    rows = ''
    for i, (a, b) in enumerate(STEPS):
        if i < k:
            box = '<div class="b"><i>✓</i></div>'
        elif i == k:
            box = f'<div class="b"><i data-g="{g}.2" data-fx="stamp">✓</i></div>'
        else:
            box = '<div class="b"></div>'
        on = ' on' if i == k else ''
        rows += f'<div class="r{on}">{box}<div class="x"><b>{a}</b><span>{b}</span></div></div>'
    return f'<div class="ck" data-g="{g}.0" data-fx="up"><div class="t">MA CHECKLIST · BOURSOBANK</div>{rows}</div>'


BODY = hud('FRANCE · BANQUE EN LIGNE', 'BIENVENUE') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('h1', 'TA BANQUE ACTUELLE', None, ''), ('it gold', "t'a déjà offert", None, 'font-size:84px'), ('h1 tq', 'QUELQUE CHOSE ?', None, 'margin-top:10px')]) + '''
   <div class="lid" style="top:820px;transform:rotate(-24deg)"><div class="rb"></div></div>
   <div class="bx" style="top:960px;background:linear-gradient(160deg,#1a1814,#0b0a08)"></div>
   <div class="dust" style="left:500px;top:900px">·  ·</div>
   <div class="tagz">0,00 €<small>CADEAU REÇU</small></div></div>
  <div class="scene" data-s="1" data-in="pop"><div class="rays" style="top:560px"></div>''' + hd(230, [('h1', 'BOURSOBANK, ELLE,', '1.0', ''), ('it gold', "offre jusqu'à", '1.1', 'font-size:80px')]) + '''
   <div class="lid" style="top:1420px;transform:rotate(-4deg)"><div class="rb"></div></div>
   <div class="abs" style="left:0;top:760px;width:1080px;text-align:center" data-g="1.2" data-fx="stamp" data-slow="1.2" data-count="180" data-suf=" €"><div class="v gold" style="font:900 170px 'DejaVu Serif',serif;line-height:1.2">0 €</div></div>
   <div class="bx" style="top:1040px" data-g="1.0" data-fx="up"><div class="rb"></div></div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 tq', 'ÉTAPE 1 :', '2.0', ''), ('it gold', 'tu ouvres ton compte', '2.1', 'font-size:70px'), ('it gold', 'et tu fais ton premier versement.', '2.2', 'font-size:52px')]) + checklist(0, 2) + '''</div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('h1 tq', 'ÉTAPE 2 :', '3.0', ''), ('it gold', 'tu utilises ta carte', '3.1', 'font-size:70px'), ('it gold', 'chaque mois, pendant 3 mois.', '3.2', 'font-size:56px')]) + checklist(1, 3).replace('</div></div></div><div class="r">', '</div></div></div><div class="r">', 1) + '''
   <div class="dots abs" style="left:0;top:1330px;width:1080px"><div data-g="3.2" data-fx="pop">MOIS 1</div><div data-g="3.2" data-fx="pop">MOIS 2</div><div data-g="3.2" data-fx="pop">MOIS 3</div></div></div>
  <div class="scene" data-s="4" data-in="right">''' + hd(230, [('h1 tq', 'ÉTAPE 3 :', '4.0', ''), ('it gold', 'tu transfères ton ancien compte', '4.1', 'font-size:58px'), ('it gold', 'avec EasyMove.', '4.2', 'font-size:70px')]) + checklist(2, 4) + '''</div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« BOURSO »', '5.1', 'font-size:130px'), ('it gold', 'en privé,', '5.2', '')]) + '''
   <div class="pill" style="top:740px;border-color:rgba(46,211,198,.8)" data-g="5.3" data-fx="up"><div class="pin" style="background:#2ed3c6">✉</div><div><b>JE T'ENVOIE MON LIEN</b><span>jusqu'à 180 € · nouveaux clients</span></div></div>
   <div class="cond" style="top:900px">Offre soumise aux conditions en vigueur<br>jusqu'à 180 € pour le filleul selon les étapes validées :<br>ouverture + 1er versement, carte utilisée chaque mois pendant 3 mois,<br>mobilité bancaire EasyMove · nouveaux clients majeurs</div></div>
'''
