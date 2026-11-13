import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Hello bank, 13/11/2026 21:00 - style v3 nuit & or, accent rose. Offre de bienvenue jusqu'à 330 € = 80 € à l'ouverture (Hello One ou Hello Prime)
# + 200 € en bon d'achat (Hello Start+, mobilité bancaire) + 50 € Hello Prime (5 paiements ou retraits par mois pendant 12 mois),
# demande d'ouverture validée au plus tard le 08/12/2026 (source : moneyvox.fr, 05/11/2026). Voix : Speko (speechify, voix par défaut).
# Sablier + étiquette -> compteur 330 € -> bon d'achat 200 € -> ticket 80 € + 50 € -> calendrier 08/12 (J-25) -> appel à l'action.
NAME = 'hellobank9'
TITLE = 'Hello bank 330 euros rose'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Moins d'un mois pour récupérer ça. Regarde.", [("Moins d'un mois", None), ("pour récupérer ça.", None), ("Regarde.", None)]),
 ("Hello bank offre jusqu'à trois cent trente euros aux nouveaux clients.", [("Hello bank offre", None), ("jusqu'à 330 €", None), ("aux nouveaux clients.", None)]),
 ("Dont deux cents euros en bon d'achat, avec Hello Start plus.", [("Dont 200 €", None), ("en bon d'achat,", None), ("avec Hello Start +.", None)]),
 ("Plus quatre-vingts euros à l'ouverture, et cinquante avec Hello Prime.", [("Plus 80 €", None), ("à l'ouverture,", None), ("et 50", None), ("avec Hello Prime.", None)]),
 ("Ta demande doit être validée au plus tard le huit décembre.", [("Ta demande", None), ("doit être validée", None), ("au plus tard", None), ("le 8 décembre.", None)]),
 ("Envoie-moi HELLO en privé, je t'envoie le lien.", [("Envoie-moi", None), ("HELLO", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 1.98), (2.60, 5.14), (5.54, 8.42), (8.94, 11.61), (12.06, 14.07), (14.58, 16.14)]
GSTART = [[0.05, 0.6, 1.6], [2.6, 3.4, 4.6], [5.54, 6.4, 7.2], [8.94, 9.6, 10.4, 10.9], [12.06, 12.4, 13.1, 13.5], [14.58, 14.9, 15.05, 15.6]]
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
.ro{color:#ff8fb1;text-shadow:0 0 18px rgba(255,143,177,.45)}
.hg{position:absolute;left:200px;top:760px;width:300px;height:520px}
.hg .tp,.hg .bt{position:absolute;left:0;width:300px;height:30px;border-radius:10px;background:linear-gradient(90deg,#a8701f,#f3c766,#a8701f)}
.hg .tp{top:0}.hg .bt{bottom:0}
.hg .gl{position:absolute;left:30px;top:30px;width:240px;height:460px;border:5px solid rgba(255,230,200,.5);border-radius:40% 40% 40% 40%/50% 50% 50% 50%;clip-path:polygon(0 0,100% 0,55% 50%,100% 100%,0 100%,45% 50%)}
.hg .s1{position:absolute;left:62px;top:120px;width:176px;height:100px;background:#ff8fb1;clip-path:polygon(0 0,100% 0,50% 100%)}
.hg .s2{position:absolute;left:46px;top:380px;width:208px;height:110px;background:#ff8fb1;clip-path:polygon(50% 0,100% 100%,0 100%)}
.hg .st{position:absolute;left:148px;top:250px;width:4px;height:140px;background:#ff8fb1}
.ptag{position:absolute;left:540px;top:880px;width:410px;height:190px;border-radius:20px 60px 60px 20px;background:linear-gradient(135deg,#fff1c4,#e9b456 50%,#a8701f);color:#2a1a05;text-align:center;transform:rotate(-10deg);box-shadow:0 20px 50px rgba(0,0,0,.6);white-space:nowrap}
.ptag:before{content:'';position:absolute;right:30px;top:80px;width:28px;height:28px;border-radius:50%;background:#07060a}
.ptag .a{font:900 92px 'DejaVu Serif',serif;line-height:1;margin-top:30px;margin-right:46px}
.ptag .s{font:800 22px Inter;letter-spacing:3px;margin-right:46px}
.vch{position:absolute;left:150px;top:760px;width:780px;height:400px;border-radius:28px;background:linear-gradient(135deg,#ffd6e2,#ff8fb1);color:#2b0e18;box-shadow:0 40px 100px rgba(0,0,0,.75);transform:rotate(-4deg);overflow:hidden}
.vch:before,.vch:after{content:'';position:absolute;top:170px;width:60px;height:60px;border-radius:50%;background:#07060a}
.vch:before{left:-30px}.vch:after{right:-30px}
.vch .k{position:absolute;left:60px;top:46px;font:800 28px 'DejaVu Sans Mono',monospace;letter-spacing:6px}
.vch .a{position:absolute;left:60px;top:100px;font:900 170px 'DejaVu Serif',serif;line-height:1}
.vch .s{position:absolute;left:60px;top:300px;font:800 30px Inter;letter-spacing:2px}
.vch .cut{position:absolute;left:560px;top:30px;height:340px;border-left:5px dashed rgba(43,14,24,.4)}
.vch .bc{position:absolute;left:600px;top:80px;width:130px;height:240px;background:repeating-linear-gradient(90deg,#2b0e18 0 6px,transparent 6px 11px,#2b0e18 11px 14px,transparent 14px 22px)}
.rc{position:absolute;left:210px;top:720px;width:660px;background:#f6f1ea;color:#1e1418;padding:40px 46px 50px;font:600 32px 'DejaVu Sans Mono',monospace;transform:rotate(3deg);box-shadow:0 40px 90px rgba(0,0,0,.7)}
.rc .t{font:800 30px Inter;letter-spacing:6px;color:#c2557a;text-align:center;margin-bottom:16px}
.rc .r{display:flex;justify-content:space-between;align-items:baseline;padding:20px 0;border-bottom:3px dashed #bbb;white-space:nowrap}
.rc .r small{display:block;font:500 22px Inter;color:#6d6066}
.rc .r b{font:900 64px 'DejaVu Serif',serif;color:#c2557a}
.cal{position:absolute;left:290px;top:700px;width:500px;height:560px;border-radius:30px;background:#f6f1ea;color:#1e1418;text-align:center;box-shadow:0 40px 90px rgba(0,0,0,.7);overflow:hidden;transform:rotate(-3deg)}
.cal .h{height:130px;background:#ff8fb1;color:#2b0e18;font:900 44px Inter;letter-spacing:5px;line-height:130px}
.cal .d{font:900 230px 'DejaVu Serif',serif;line-height:1.2}
.cal .m{font:800 40px Inter;letter-spacing:8px;color:#6d6066}
.jx{position:absolute;left:700px;top:1180px;width:230px;height:230px;border-radius:50%;background:#ff8fb1;color:#2b0e18;display:flex;flex-direction:column;align-items:center;justify-content:center;font:900 72px Inter;box-shadow:0 20px 50px rgba(0,0,0,.6)}
.jx small{font:800 22px Inter;letter-spacing:3px}
'''

BODY = hud('FRANCE · BANQUE EN LIGNE', 'COMPTE À REBOURS') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('h1', "MOINS D'UN MOIS", None, 'font-size:92px'), ('it gold', 'pour récupérer ça.', None, 'font-size:84px'), ('h1 ro s', 'REGARDE.', None, 'margin-top:12px')]) + '''
   <div class="hg"><div class="tp"></div><div class="gl"></div><div class="s1"></div><div class="st"></div><div class="s2"></div><div class="bt"></div></div>
   <div class="ptag"><div class="a">330 €</div><div class="s">MAXIMUM</div></div></div>
  <div class="scene" data-s="1" data-in="pop"><div class="rays" style="top:600px"></div>''' + hd(230, [('h1', 'HELLO BANK OFFRE', '1.0', ''), ('it gold', 'aux nouveaux clients.', '1.2', 'font-size:64px;margin-top:820px')]) + '''
   <div class="abs" style="left:0;top:720px;width:1080px;text-align:center" data-g="1.1" data-fx="stamp" data-slow="1.1" data-count="330" data-suf=" €"><div style="font:800 34px Inter;letter-spacing:6px;color:#e9e4da">JUSQU'À</div><div class="v gold" style="font:900 200px 'DejaVu Serif',serif;line-height:1.2">0 €</div></div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1', 'DONT 200 €', '2.0', ''), ('it gold', "en bon d'achat,", '2.1', 'font-size:80px'), ('it gold', 'avec Hello Start +.', '2.2', 'font-size:66px')]) + '''
   <div class="vch" data-g="2.0" data-fx="up"><div class="k">BON D'ACHAT</div><div class="a">200 €</div><div class="s">HELLO START +</div><div class="cut"></div><div class="bc"></div></div>
   <div class="abs ro" style="left:0;top:1260px;width:1080px;text-align:center;font:800 30px Inter;letter-spacing:4px" data-g="2.2" data-fx="fade">AVEC LA MOBILITÉ BANCAIRE</div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('h1', 'PLUS 80 €', '3.0', ''), ('it gold', "à l'ouverture,", '3.1', 'font-size:76px'), ('it gold', 'et 50 avec Hello Prime.', '3.2', 'font-size:66px')]).replace('data-g="3.2"', 'data-g="3.2"', 1) + '''
   <div class="rc" style="top:760px" data-g="3.0" data-fx="up"><div class="t">TICKET DE BIENVENUE</div>
    <div class="r" data-g="3.0" data-fx="left"><span>Ouverture<small>Hello One ou Hello Prime</small></span><b>80 €</b></div>
    <div class="r" data-g="3.3" data-fx="left"><span>Hello Prime<small>5 paiements / mois · 12 mois</small></span><b>+ 50 €</b></div>
    <div class="r" data-g="3.3" data-fx="left" style="border-bottom:0"><span>Bon d'achat<small>Hello Start +</small></span><b>+ 200 €</b></div></div></div>
  <div class="scene" data-s="4" data-in="up">''' + hd(230, [('h1 ro', 'TA DEMANDE', '4.0', ''), ('it gold', 'doit être validée', '4.1', 'font-size:72px'), ('it gold', 'au plus tard le 8 décembre.', '4.2', 'font-size:60px')]) + '''
   <div class="cal" data-g="4.2" data-fx="up"><div class="h">DÉCEMBRE</div><div class="d">08</div><div class="m">2026</div></div>
   <div class="jx" data-g="4.3" data-fx="stamp">J-25<small>AU 13/11</small></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« HELLO »', '5.1', 'font-size:130px'), ('it gold', 'en privé,', '5.2', '')]) + '''
   <div class="pill" style="top:740px;border-color:rgba(255,143,177,.8)" data-g="5.3" data-fx="up"><div class="pin" style="background:#ff8fb1">✉</div><div><b>JE T'ENVOIE LE LIEN</b><span>avant le 8 décembre</span></div></div>
   <div class="cond" style="top:900px">Offre soumise aux conditions en vigueur · jusqu'à 330 €<br>= 80 € à l'ouverture (Hello One ou Hello Prime) + 200 € en bon<br>d'achat (Hello Start+) + 50 € avec Hello Prime (12 mois)<br>· nouveaux clients · demande validée au plus tard le 08/12/2026</div></div>
'''
