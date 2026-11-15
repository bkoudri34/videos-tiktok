import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Hello bank, 15/11/2026 18:00 - style v3 nuit & or, accent mandarine. Offre de bienvenue jusqu'à 330 € = 80 € à l'ouverture
# (Hello One ou Hello Prime) + 50 € avec Hello Prime (5 paiements ou retraits par mois pendant 12 mois) + bon d'achat 200 €
# (Hello Start+, mobilité, souscrit entre le 08/10/2026 et le 11/01/2027), demande en ligne au plus tard le 08/12/2026
# (source : moneyvox.fr, 05/11/2026). Voix : Speko (speechify, voix par défaut ; voix clonée refusée 402).
# 3 enveloppes fermées -> enveloppe 1 (80 €) -> enveloppe 2 (+50 €) -> enveloppe 3 (bon 200 €) -> total 330 € -> frise jusqu'au 08/12 -> appel à l'action.
NAME = 'hellobank10'
TITLE = 'Hello bank enveloppes mandarine'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Trois enveloppes t'attendent chez Hello bank.", [("Trois enveloppes", None), ("t'attendent", None), ("chez Hello bank.", None)]),
 ("La première : quatre-vingts euros à l'ouverture.", [("La première :", None), ("80 €", None), ("à l'ouverture.", None)]),
 ("La deuxième : cinquante euros de plus avec Hello Prime.", [("La deuxième :", None), ("50 € de plus", None), ("avec Hello Prime.", None)]),
 ("La troisième : un bon d'achat de deux cents euros, avec Hello Start plus.", [("La troisième :", None), ("un bon d'achat de 200 €,", None), ("avec Hello Start +.", None)]),
 ("Au total : jusqu'à trois cent trente euros.", [("Au total :", None), ("jusqu'à 330 €.", None)]),
 ("Ta demande en ligne, c'est avant le huit décembre.", [("Ta demande en ligne,", None), ("c'est avant", None), ("le 8 décembre.", None)]),
 ("Envoie-moi HELLO en privé, je t'envoie le lien.", [("Envoie-moi", None), ("HELLO", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 1.53), (1.91, 3.66), (3.97, 6.14), (6.52, 9.53), (9.83, 11.37), (12.06, 13.78), (14.17, 15.86)]
GSTART = [[0.1, 0.6, 0.9], [1.91, 2.6, 3.1], [3.97, 4.5, 5.4], [6.52, 7.2, 8.5], [9.83, 10.4], [12.06, 12.9, 13.2], [14.17, 14.6, 14.8, 15.3]]
MINLEN = 2.1
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
.md{color:#ff9a3c;text-shadow:0 0 18px rgba(255,154,60,.45)}
.ev{position:absolute;width:250px;height:170px}
.ev .b{position:absolute;inset:0;border-radius:14px;background:linear-gradient(160deg,#f6ead6,#e2cfae);box-shadow:0 24px 60px rgba(0,0,0,.65)}
.ev .f{position:absolute;left:0;top:0;width:250px;height:110px;background:#d8c19b;clip-path:polygon(0 0,100% 0,50% 100%)}
.ev .s{position:absolute;left:100px;top:80px;width:50px;height:50px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#ffc58a,#ff9a3c 55%,#c46412);box-shadow:0 4px 10px rgba(0,0,0,.4)}
.ev .n{position:absolute;left:0;bottom:12px;width:250px;text-align:center;font:900 30px 'DejaVu Serif',serif;color:#7a4a14}
.big-ev{position:absolute;left:190px;top:960px;width:700px;height:420px}
.big-ev .b{position:absolute;left:0;top:0;width:700px;height:420px;border-radius:24px;background:linear-gradient(160deg,#f6ead6,#e2cfae);box-shadow:0 40px 100px rgba(0,0,0,.7)}
.big-ev .f{position:absolute;left:0;top:0;width:700px;height:260px;background:#d8c19b;clip-path:polygon(0 0,100% 0,50% 100%)}
.big-ev .fo{position:absolute;left:0;top:-260px;width:700px;height:260px;background:#cdb48a;clip-path:polygon(0 100%,100% 100%,50% 0)}
.ct{position:absolute;left:250px;width:580px;height:330px;border-radius:22px;background:linear-gradient(135deg,#ffd2a6,#ff9a3c);color:#2d1606;text-align:center;box-shadow:0 30px 70px rgba(0,0,0,.55);white-space:nowrap}
.ct .k{font:800 26px 'DejaVu Sans Mono',monospace;letter-spacing:6px;margin-top:34px}
.ct .a{font:900 140px 'DejaVu Serif',serif;line-height:1.1}
.ct .s{font:800 26px Inter;letter-spacing:2px}
.chips{position:absolute;left:0;width:1080px;display:flex;gap:18px;justify-content:center}
.chips div{padding:0 30px;height:76px;border-radius:38px;border:3px solid #ff9a3c;font:900 36px 'DejaVu Serif',serif;color:#ffcf9e;display:flex;align-items:center}
.tln{position:absolute;left:150px;top:900px;width:760px;height:10px;border-radius:5px;background:rgba(255,255,255,.15)}
.tln .p{position:absolute;left:0;top:0;height:10px;width:760px;border-radius:5px;background:linear-gradient(90deg,#ff9a3c,#f3c766);transform-origin:0 50%}
.tln .d{position:absolute;top:-25px;width:60px;height:60px;border-radius:50%;border:5px solid #ff9a3c;background:#07060a}
.tln .d.e{background:#f3c766;border-color:#f3c766}
.tln .l{position:absolute;top:60px;width:240px;text-align:center;font:800 34px Inter;color:#e9e4da;white-space:nowrap}
.tln .l small{display:block;font:600 24px Inter;color:#9a917f;letter-spacing:2px}
.jj{position:absolute;left:370px;top:1120px;width:340px;height:340px;border-radius:50%;border:6px solid #ff9a3c;display:flex;flex-direction:column;align-items:center;justify-content:center;font:900 110px 'DejaVu Serif',serif;color:#ffcf9e;background:radial-gradient(circle,#2a1607,#0b0704)}
.jj small{font:800 24px Inter;letter-spacing:4px;color:#e9e4da}
'''


def ev(x, y, n, rot=0, extra=''):
    return f'<div class="ev" style="left:{x}px;top:{y}px;transform:rotate({rot}deg)"{extra}><div class="b"></div><div class="f"></div><div class="s"></div><div class="n">{n}</div></div>'


def open_scene(i, card_k, card_a, card_s):
    return f'''
   <div class="big-ev"><div class="b"></div><div class="fo" data-g="{i}.0" data-fx="fade"></div></div>
   <div class="ct" style="top:700px" data-g="{i}.1" data-fx="up"><div class="k">{card_k}</div><div class="a">{card_a}</div><div class="s">{card_s}</div></div>
   <div class="big-ev" style="pointer-events:none"><div class="f" style="top:160px;height:260px;clip-path:polygon(0 100%,100% 100%,50% 30%);background:#e9d8b9"></div></div>'''


BODY = hud('FRANCE · BANQUE EN LIGNE', 'COURRIER') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('h1', 'TROIS ENVELOPPES', None, ''), ('it gold', "t'attendent", None, 'font-size:84px'), ('h1 md', 'CHEZ HELLO BANK.', None, 'margin-top:10px')]) + \
    ev(120, 900, 'N° 1', -6) + ev(415, 860, 'N° 2', 3) + ev(700, 910, 'N° 3', 7) + '''</div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1 md', 'LA PREMIÈRE :', '1.0', ''), ('it gold', "80 € à l'ouverture.", '1.1', 'font-size:72px')]) + open_scene(1, 'ENVELOPPE N° 1', '80 €', 'OUVERTURE · HELLO ONE OU PRIME') + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 md', 'LA DEUXIÈME :', '2.0', ''), ('it gold', '50 € de plus', '2.1', 'font-size:76px'), ('it gold', 'avec Hello Prime.', '2.2', 'font-size:70px')]) + open_scene(2, 'ENVELOPPE N° 2', '+ 50 €', '5 PAIEMENTS / MOIS · 12 MOIS').replace('top:700px', 'top:760px') + '''</div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('h1 md', 'LA TROISIÈME :', '3.0', ''), ('it gold', "un bon d'achat de 200 €,", '3.1', 'font-size:62px'), ('it gold', 'avec Hello Start +.', '3.2', 'font-size:66px')]) + open_scene(3, "BON D'ACHAT", '200 €', 'HELLO START + · MOBILITÉ').replace('top:700px', 'top:760px') + '''</div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:560px"></div>''' + hd(230, [('h1', 'AU TOTAL :', '4.0', ''), ('it gold', "jusqu'à", '4.1', 'font-size:76px')]) + '''
   <div class="abs" style="left:0;top:660px;width:1080px;text-align:center" data-g="4.1" data-fx="stamp" data-slow="4.1" data-count="330" data-suf=" €"><div class="v gold" style="font:900 210px 'DejaVu Serif',serif;line-height:1.2">0 €</div></div>
   <div class="chips" style="top:1000px"><div data-g="4.1" data-fx="pop">80 €</div><div data-g="4.1" data-fx="pop">+ 50 €</div><div data-g="4.1" data-fx="pop">+ 200 €</div></div></div>
  <div class="scene" data-s="5" data-in="right">''' + hd(230, [('h1 md', 'TA DEMANDE EN LIGNE,', '5.0', 'font-size:68px'), ('it gold', "c'est avant", '5.1', 'font-size:76px'), ('it gold', 'le 8 décembre.', '5.2', 'font-size:76px')]) + '''
   <div class="tln" data-g="5.0" data-fx="fade"><div class="p" data-g="5.1" data-fx="grow"></div><div class="d" style="left:-30px"></div><div class="d e" style="left:730px" data-g="5.2" data-fx="stamp"></div>
    <div class="l" style="left:-90px">15/11<small>AUJOURD'HUI</small></div><div class="l" style="left:640px" data-g="5.2" data-fx="up">08/12<small>DATE LIMITE</small></div></div>
   <div class="jj" data-g="5.2" data-fx="stamp">J-23<small>AU 15/11</small></div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« HELLO »', '6.1', 'font-size:130px'), ('it gold', 'en privé,', '6.2', '')]) + '''
   <div class="pill" style="top:740px;border-color:rgba(255,154,60,.8)" data-g="6.3" data-fx="up"><div class="pin" style="background:#ff9a3c">✉</div><div><b>JE T'ENVOIE LE LIEN</b><span>demande en ligne avant le 8 décembre</span></div></div>
   <div class="cond" style="top:900px">Offre soumise aux conditions en vigueur · jusqu'à 330 €<br>80 € à l'ouverture (Hello One ou Hello Prime)<br>+ 50 € avec Hello Prime (5 paiements ou retraits / mois, 12 mois)<br>+ bon d'achat 200 € (Hello Start+) · nouveaux clients<br>demande en ligne au plus tard le 08/12/2026</div></div>
'''
