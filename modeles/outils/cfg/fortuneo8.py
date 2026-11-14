import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Fortuneo, 14/11/2026 18:00 - style v3 nuit & or, accent rubis. Offre de bienvenue jusqu'à 260 € avec la carte Gold CB Mastercard
# (sous conditions de revenus) : 160 € après 5 paiements en 90 jours + 80 € mobilité bancaire + 20 € Livret +, code FTN1126, jusqu'au 20/12/2026
# (sources : selectra.info, moneyvox.fr). Voix : Speko (speechify, voix par défaut).
# Escalier de 3 marches vide -> marche 1 (carte Gold) -> 5 tickets + cadran 90 jours -> marche 2 (mobilité) -> marche 3 (Livret +, total 260 €)
# -> panneau compte à rebours J-36 -> appel à l'action.
NAME = 'fortuneo8'
TITLE = 'Fortuneo escalier rubis'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Fortunéo te donne jusqu'à deux cent soixante euros. Voici comment.", [("Fortuneo te donne", None), ("jusqu'à 260 €.", None), ("Voici comment.", None)]),
 ("Marche un : cent soixante euros avec la carte Gold.", [("Marche 1 :", None), ("160 €", None), ("avec la carte Gold.", None)]),
 ("Il suffit de cinq paiements en quatre-vingt-dix jours.", [("Il suffit de", None), ("5 paiements", None), ("en 90 jours.", None)]),
 ("Marche deux : quatre-vingts euros si tu changes de banque.", [("Marche 2 :", None), ("80 €", None), ("si tu changes de banque.", None)]),
 ("Marche trois : vingt euros avec le Livret plus.", [("Marche 3 :", None), ("20 €", None), ("avec le Livret +.", None)]),
 ("L'offre court jusqu'au vingt décembre.", [("L'offre court", None), ("jusqu'au 20 décembre.", None)]),
 ("Envoie-moi FORTUNÉO en privé, je t'envoie le lien.", [("Envoie-moi", None), ("FORTUNEO", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 3.02), (3.61, 6.07), (6.49, 8.41), (9.12, 11.35), (12.03, 14.35), (15.05, 16.31), (16.73, 18.52)]
GSTART = [[0.1, 0.8, 2.55], [3.61, 4.43, 5.2], [6.49, 7.0, 7.6], [9.12, 9.86, 10.6], [12.03, 12.78, 13.45], [15.05, 15.6], [16.73, 17.0, 17.5, 17.9]]
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
.rb{color:#ff6f8c;text-shadow:0 0 18px rgba(255,90,122,.5)}
.st{position:absolute;width:250px;border:4px solid #d9a24c;border-bottom:0;background:linear-gradient(180deg,#2a1218,#120709);text-align:center}
.st.on{background:linear-gradient(180deg,#ff5a7a,#8e1f37);border-color:#f3c766;box-shadow:0 0 50px rgba(255,90,122,.45)}
.st .n{font:800 26px Inter;letter-spacing:4px;color:#9a917f;margin-top:22px}
.st.on .n{color:#ffe3ea}
.st .v{font:900 64px 'DejaVu Serif',serif;color:#f3c766;margin-top:6px;white-space:nowrap}
.st.on .v{color:#fff}
.base{position:absolute;left:150px;top:1430px;width:780px;height:10px;background:#d9a24c;border-radius:5px}
.qm{position:absolute;left:680px;top:760px;width:250px;text-align:center;font:900 120px 'DejaVu Serif',serif}
.gc{position:absolute;width:300px;height:186px;border-radius:18px;background:linear-gradient(135deg,#f6dc8e 0%,#d6a347 40%,#8a5a18 100%);box-shadow:0 20px 50px rgba(0,0,0,.7);color:#2a1a05;padding:20px 24px;font:900 22px Inter;letter-spacing:2px}
.gc i{display:block;width:54px;height:40px;border-radius:8px;background:linear-gradient(135deg,#fff1c4,#b98a3a);margin-top:22px}
.tk{position:absolute;top:760px;width:150px;height:200px;background:#f8f6f1;color:#1f1d1a;border-radius:6px;text-align:center;font:700 22px 'DejaVu Sans Mono',monospace;padding-top:22px;box-shadow:0 20px 40px rgba(0,0,0,.6)}
.tk b{display:block;font:900 54px Inter;color:#c2203f;margin:10px 0 4px}
.dl{position:absolute;left:340px;top:1030px;width:400px;height:400px;border-radius:50%;border:6px solid #d9a24c;background:radial-gradient(circle,#2a1218,#0c0507 70%);box-shadow:0 0 50px rgba(255,90,122,.3)}
.dl .ar{position:absolute;inset:18px;border-radius:50%;background:conic-gradient(#ff5a7a 0 250deg,rgba(255,90,122,.15) 250deg);-webkit-mask:radial-gradient(circle,transparent 62%,#000 63%);transform-origin:50% 50%}
.dl .c{position:absolute;left:0;top:118px;width:100%;text-align:center;font:900 100px 'DejaVu Serif',serif;color:#f3c766;line-height:1}
.dl .c small{display:block;font:800 28px Inter;letter-spacing:6px;color:#e9e4da;margin-top:10px}
.hs{position:absolute;top:640px;width:150px;text-align:center;font:400 150px 'DejaVu Sans';line-height:1}
.tot{position:absolute;left:150px;top:640px;width:300px;padding:16px 0;border:6px solid #f3c766;border-radius:22px;text-align:center;background:rgba(40,10,16,.75)}
.tot .k{font:800 26px Inter;letter-spacing:5px;color:#e9e4da}.tot .v{font:900 86px 'DejaVu Serif',serif;line-height:1.1}
.cd{position:absolute;left:190px;top:700px;width:700px;height:520px;border-radius:40px;background:#140a0c;border:5px solid #d9a24c;box-shadow:0 40px 90px rgba(0,0,0,.7),inset 0 0 60px rgba(255,90,122,.15);text-align:center}
.cd .l1{font:800 32px Inter;letter-spacing:8px;color:#9a917f;margin-top:48px}
.cd .j{font:900 210px 'DejaVu Sans Mono',monospace;color:#ff5a7a;text-shadow:0 0 40px rgba(255,90,122,.7);line-height:1.15;margin-top:10px}
.cd .l2{font:800 40px Inter;letter-spacing:4px;color:#f3c766}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
H = [170, 330, 490]
X = [160, 415, 670]


def stairs(lit, g=None, show_vals=(False, False, False)):
    """3 marches ; lit = indices allumées ; g = groupe d'apparition de la dernière marche allumée."""
    out = ''
    vals = ['160 €', '+ 80 €', '+ 20 €']
    for k in range(3):
        on = ' on' if k in lit else ''
        a = f' data-g="{g}" data-fx="growY" style="transform-origin:50% 100%;' if (g and k == max(lit)) else ' style="'
        v = f'<div class="v">{vals[k]}</div>' if show_vals[k] else ''
        out += f'<div class="st{on}"{a}left:{X[k]}px;top:{1430 - H[k]}px;height:{H[k]}px"><div class="n">MARCHE {k + 1}</div>{v}</div>'
    return out + '<div class="base"></div>'


BODY = hud('FRANCE · CARTE GOLD', "JUSQU'AU 20/12") + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(210, [('h1 s', 'FORTUNEO TE DONNE', None, ''), ('it gold', "jusqu'à", None, 'font-size:60px'), ('big gold', '260 €', None, 'font-size:170px'), ('it gold', 'voici comment.', None, 'font-size:64px')]) + '''
   ''' + stairs([], None) + '''<div class="qm gold" style="top:780px">?</div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1 rb', 'MARCHE 1 :', '1.0', ''), ('big gold', '160 €', '1.1', 'font-size:150px'), ('it gold', 'avec la carte Gold.', '1.2', 'font-size:64px')]) + '''
   ''' + stairs([0], '1.0', (True, False, False)) + '''<div class="gc" style="left:130px;top:1020px;transform:rotate(-8deg)" data-g="1.2" data-fx="up">CARTE GOLD<i></i></div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1', 'IL SUFFIT DE', '2.0', ''), ('h1 rb', '5 PAIEMENTS', '2.1', 'font-size:96px'), ('it gold', 'en 90 jours.', '2.2', '')]) + ''.join(
    f'<div class="tk" style="left:{70 + 190 * k}px;top:{620 + (k % 2) * 30}px;transform:rotate({(-6, 4, -3, 5, -4)[k]}deg)" data-g="2.1" data-fx="pop">PAIEMENT<b>{k + 1}</b>✓</div>' for k in range(5)) + '''
   <div class="dl" data-g="2.2" data-fx="pop"><div class="ar" data-g="2.2" data-fx="sweep"></div><div class="c">90<small>JOURS</small></div></div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('h1 rb', 'MARCHE 2 :', '3.0', ''), ('big gold', '+ 80 €', '3.1', 'font-size:150px'), ('it gold', 'si tu changes de banque.', '3.2', 'font-size:62px')]) + '''
   ''' + stairs([0, 1], '3.0', (True, True, False)) + '''
   <div class="hs" style="left:470px;top:700px;color:#6f6553" data-g="3.2" data-fx="left">⌂</div><div class="hs gold" style="left:640px;top:700px" data-g="3.2" data-fx="right">⌂</div>
   <div class="abs" style="left:585px;top:740px;font:900 60px Inter;color:#ff6f8c" data-g="3.2" data-fx="pop">→</div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:560px;left:520px"></div>''' + hd(230, [('h1 rb', 'MARCHE 3 :', '4.0', ''), ('big gold', '+ 20 €', '4.1', 'font-size:150px'), ('it gold', 'avec le Livret +.', '4.2', 'font-size:64px')]) + '''
   ''' + stairs([0, 1, 2], '4.0', (True, True, True)) + '''
   <div class="tot" data-g="4.2" data-fx="stamp" data-slow="4.2" data-count="260"><div class="k">JUSQU'À</div><div class="v gold">0 €</div></div></div>
  <div class="scene" data-s="5" data-in="up">''' + hd(230, [('h1', "L'OFFRE COURT", '5.0', ''), ('it gold', "jusqu'au 20 décembre.", '5.1', '')]) + '''
   <div class="cd" data-g="5.0" data-fx="pop"><div class="l1">IL RESTE</div><div class="j">J-36</div><div class="l2">FIN LE 20/12/2026</div></div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« FORTUNEO »', '6.1', 'font-size:112px'), ('it gold', 'en privé,', '6.2', '')]) + '''
   <div class="pill" style="top:740px;border-color:rgba(255,90,122,.8)" data-g="6.3" data-fx="up"><div class="pin" style="background:#ff5a7a;color:#fff">✉</div><div><b>JE T'ENVOIE LE LIEN</b><span>offre valable jusqu'au 20/12</span></div></div>
   <div class="search" style="top:880px" data-g="6.3" data-fx="fade">''' + SEARCH + '''<span data-g="6.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1020px">Offre soumise aux conditions en vigueur · 1re ouverture de compte<br>jusqu'à 260 € avec la carte Gold (sous conditions de revenus) :<br>160 € après 5 paiements en 90 jours + 80 € mobilité + 20 € Livret +<br>· jusqu'au 20/12/2026</div></div>
'''
