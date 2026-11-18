import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# BoursoBank, 18/11/2026 18:00 - style v3 nuit & or, accent rouge rubis. Format F1 « STOP / erreur à éviter » :
# panneau STOP dès la 1re image -> formulaire d'inscription sans lien = prime filleul 0 € -> avant / après l'inscription
# -> total 180 € (ralenti) -> tuiles 20 + 40 puis 40 + 80 -> appel à l'action.
# Offre filleul jusqu'à 180 € (boursobank.com/bon-plan/parrainage-boursobank, consultée le 18/11/2026, pas de date de fin) :
# 20 € ouverture + jusqu'à 40 € 1er versement (40 € dès 300 €) + jusqu'à 40 € carte sur 3 mois + 80 € mobilité EasyMove.
# « Si votre filleul n'a pas utilisé votre invitation de parrainage [...] les récompenses filleul et parrain ne seront pas versées » (même page).
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'bourso12'
TITLE = 'BoursoBank STOP rubis'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Stop ! Parrainage Bourso Bank : ne rate pas cette étape.", [("STOP !", None), ("Parrainage BoursoBank :", None), ("ne rate pas cette étape.", None)]),
 ("Sans lien de parrainage, pas de prime filleul.", [("Sans lien de parrainage,", None), ("pas de prime filleul.", None)]),
 ("Le lien, c'est avant de commencer l'inscription. Pas après.", [("Le lien,", None), ("c'est avant de commencer l'inscription.", None), ("Pas après.", None)]),
 ("Avec le lien, jusqu'à cent quatre-vingts euros pour toi.", [("Avec le lien,", None), ("jusqu'à 180 €", None), ("pour toi.", None)]),
 ("Vingt à l'ouverture, quarante au premier versement.", [("20 € à l'ouverture,", None), ("40 € au 1er versement.", None)]),
 ("Quarante avec ta carte, quatre-vingts avec EasyMove.", [("40 € avec ta carte,", None), ("80 € avec EasyMove.", None)]),
 ("Envoie-moi BOURSO en privé, je t'envoie mon lien.", [("Envoie-moi", None), ("BOURSO", None), ("en privé,", None), ("je t'envoie mon lien.", None)]),
]
SPLITS = [(0.0, 3.08), (3.53, 5.32), (5.81, 8.06), (8.42, 10.47), (10.84, 12.76), (13.22, 15.27), (15.69, 17.73)]
GSTART = [[0.0, 0.8, 2.1], [3.55, 4.6], [5.81, 6.2, 7.6], [8.42, 9.0, 10.2], [10.84, 11.7], [13.22, 14.3], [15.7, 16.1, 16.4, 16.9]]
MINLEN = 2.0
GAP = 0.3
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.rb{color:#ff5a6a;text-shadow:0 0 18px rgba(255,60,80,.55)}
.stopw{position:absolute;left:290px;top:760px;width:500px;height:500px}
.form{position:absolute;left:150px;top:720px;width:780px;border-radius:40px;background:#f4f2ee;color:#1b1a18;padding:44px 50px;box-shadow:0 30px 90px rgba(0,0,0,.7)}
.form .t{font:900 44px Inter;letter-spacing:1px}
.form .f{margin-top:26px;font:700 26px Inter;color:#6b665e;letter-spacing:2px}
.form .in{margin-top:10px;height:96px;border-radius:20px;border:4px solid #c9c4ba;background:#fff;font:600 36px Inter;color:#9a958c;display:flex;align-items:center;padding:0 26px;white-space:nowrap}
.form .in.bad{border-color:#ff3b4f;color:#ff3b4f}
.zero{position:absolute;left:0;top:1260px;width:1080px;text-align:center;font:900 64px Inter;color:#fff;white-space:nowrap}
.zero b{font:900 120px 'DejaVu Serif',serif;color:#ff4d5e;text-shadow:0 0 30px rgba(255,60,80,.6)}
.x{position:absolute;width:150px;height:150px;border-radius:50%;background:#ff3b4f;color:#fff;font:900 100px Inter;display:flex;align-items:center;justify-content:center;border:6px solid #fff;box-shadow:0 0 40px rgba(255,60,80,.7)}
.av{position:absolute;left:110px;width:860px;height:200px;border-radius:34px;display:flex;align-items:center;gap:30px;padding:0 40px;white-space:nowrap}
.av.ok{top:760px;background:rgba(217,162,76,.14);border:4px solid #d9a24c}
.av.ko{top:1020px;background:rgba(255,77,94,.10);border:4px solid #ff4d5e}
.av .n{flex:none;width:110px;height:110px;border-radius:50%;font:900 64px Inter;display:flex;align-items:center;justify-content:center}
.av.ok .n{background:#d9a24c;color:#1a1408}.av.ko .n{background:#ff4d5e;color:#fff}
.av b{display:block;font:900 50px Inter}.av span{font:600 32px Inter;color:#cfc8ba}
.av .sk{position:absolute;left:30px;right:30px;top:96px;height:8px;background:#ff4d5e;transform-origin:0 50%}
.t180{position:absolute;left:0;top:860px;width:1080px;text-align:center}
.t180 .v{font:900 230px 'DejaVu Serif',serif;line-height:1}
.t180 small{display:block;font:800 40px Inter;color:#e9e4da;letter-spacing:4px;margin-top:20px}
.tl2{position:absolute;width:420px;height:400px;top:760px;border-radius:36px;background:#17110f;border:4px solid #ff4d5e;text-align:center;padding-top:50px}
.tl2 .v{font:900 130px 'DejaVu Serif',serif;line-height:1.1}
.tl2 b{display:block;font:900 40px Inter;margin-top:20px;color:#fff}
.tl2 span{display:block;font:600 28px Inter;color:#b7ae9e;margin-top:10px}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
STOP = '''<svg class="stopw" viewBox="0 0 500 500"><polygon points="146,10 354,10 490,146 490,354 354,490 146,490 10,354 10,146" fill="#d61f33" stroke="#fff" stroke-width="16"/>
 <text x="250" y="300" text-anchor="middle" font-family="Inter" font-weight="900" font-size="150" fill="#fff">STOP</text></svg>'''


def tile(left, g, amt, b, s):
    return f'<div class="tl2" style="left:{left}px" data-g="{g}" data-fx="pop"><div class="v gold">{amt}</div><b>{b}</b><span>{s}</span></div>'


BODY = hud('FRANCE · BOURSOBANK', 'ATTENTION') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(215, [('big rb', 'STOP !', None, 'font-size:120px'), ('h1', 'PARRAINAGE BOURSOBANK :', None, 'font-size:62px'), ('it gold', 'ne rate pas cette étape.', None, 'font-size:68px')]) + STOP + '''</div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1', 'SANS LIEN', '1.0', ''), ('h1', 'DE PARRAINAGE,', '1.0', ''), ('it rb', 'pas de prime filleul.', '1.1', 'font-size:70px')]) + '''
   <div class="form" style="top:640px"><div class="t">Inscription</div><div class="f">LIEN DE PARRAINAGE</div><div class="in bad">aucun lien</div><div class="f">PRIME FILLEUL</div><div class="in">—</div></div>
   <div class="x" style="left:800px;top:700px" data-g="1.1" data-fx="stamp">✕</div>
   <div class="zero" data-g="1.1" data-fx="pop">prime filleul : <b>0 €</b></div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1', 'LE LIEN,', '2.0', ''), ('it gold', "c'est avant de commencer", '2.1', 'font-size:62px'), ('it gold', "l'inscription.", '2.1', 'font-size:62px')]) + '''
   <div class="av ok" data-g="2.0" data-fx="right"><div class="n">1</div><div><b>LE LIEN D'ABORD</b><span>puis tu commences l'inscription</span></div></div>
   <div class="av ko" data-g="2.2" data-fx="left"><div class="n">✕</div><div><b>PAS APRÈS</b><span>inscription déjà commencée</span></div><div class="sk" data-g="2.2" data-fx="strike"></div></div></div>
  <div class="scene" data-s="3" data-in="pop"><div class="rays" style="top:700px"></div>''' + hd(230, [('h1', 'AVEC LE LIEN,', '3.0', ''), ('it gold', 'pour toi.', '3.2', 'font-size:70px')]) + '''
   <div class="t180" data-g="3.1" data-fx="stamp" data-slow="3.1" data-count="180"><div class="v gold">0 €</div><small>JUSQU'À · POUR LE FILLEUL</small></div></div>
  <div class="scene" data-s="4" data-in="right">''' + hd(230, [('h1', "À L'OUVERTURE", '4.0', 'font-size:66px'), ('h1 rb', '+ 1ER VERSEMENT', '4.1', 'font-size:66px')]) + tile(90, '4.0', '20 €', 'OUVERTURE', 'du compte') + tile(570, '4.1', '40 €', '1ER VERSEMENT', 'dès 300 € versés') + '''</div>
  <div class="scene" data-s="5" data-in="right">''' + hd(230, [('h1', 'TA CARTE', '5.0', 'font-size:66px'), ('h1 rb', '+ EASYMOVE', '5.1', 'font-size:66px')]) + tile(90, '5.0', '40 €', 'CARTE', 'utilisée 3 mois') + tile(570, '5.1', '80 €', 'EASYMOVE', 'changement de banque') + '''</div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« BOURSO »', '6.1', 'font-size:110px'), ('it gold', 'en privé,', '6.2', '')]) + '''
   <div class="pill" style="top:780px;border-color:rgba(255,77,94,.85)" data-g="6.3" data-fx="up"><div class="pin" style="background:#ff4d5e;color:#fff">✉</div><div><b>JE T'ENVOIE MON LIEN</b><span>avant que tu commences l'inscription</span></div></div>
   <div class="search" style="top:920px" data-g="6.3" data-fx="fade">''' + SEARCH + '''<span data-g="6.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1060px">Offre soumise aux conditions en vigueur<br>jusqu'à 180 € pour le filleul (nouveau client, compte individuel) :<br>20 € ouverture + jusqu'à 40 € 1er versement (40 € dès 300 €)<br>+ jusqu'à 40 € paiements carte sur 3 mois + 80 € EasyMove</div></div>
'''
