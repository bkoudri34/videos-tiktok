import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°3 du 19/11/2026 (tâche « 2 vidéos Hacoo en plus ») - style v3 nuit & or, accent lilas.
# Format F5 défi chrono : « Code promo Hacoo : 10 secondes pour payer moins cher » ; un chronomètre suit chaque étape
# (panier -> case code promo Hacoo -> hzklink tapé -> -4,76 € -> 29,24 € (ralenti) -> « même pas 10 secondes » + fin).
# Prix d'exemple : plaid 18 € + bougie 7 € + mug 9 € = 34,00 € ; -14 % = 4,76 € (34 x 0,14) ; total 29,24 € (34 x 0,86).
# Voix : Speko, Manon (cartesia sonic-3.5, « 2f8e82c4-cb94-4e6d-8b6a-29bf58ceb60a »), speed 1.08, une synthèse par réplique,
# silences coupés, recollées avec 0,2 s au début et 0,45 s entre les répliques (SPLITS).
NAME = 'hacoo35'
TITLE = 'Hacoo chrono lilas'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Code promo Hacou : dix secondes pour payer moins cher. Chrono !", [("Code promo Hacoo :", None), ("10 secondes", None), ("pour payer moins cher.", None), ("Chrono !", None)]),
 ("Plaid, bougie, mug : trente-quatre euros.", [("Plaid,", None), ("bougie,", None), ("mug :", None), ("34 €.", None)]),
 ("Tu ouvres la case code promo Hacou.", [("Tu ouvres la case", None), ("code promo Hacoo.", None)]),
 ("Tu tapes : H, Z, K, link.", [("Tu tapes :", None), ("hzklink.", None)]),
 ("Moins quatre euros soixante-seize, d'un coup.", [("-4,76 €,", None), ("d'un coup.", None)]),
 ("Vingt-neuf euros vingt-quatre. Prix d'exemple.", [("29,24 €.", None), ("Prix d'exemple.", None)]),
 ("Même pas dix secondes. Code promo Hacou, H Z K link. Les liens sont dans ma bio.", [("Même pas 10 secondes.", None), ("Code promo Hacoo,", None), ("hzklink.", None), ("Les liens sont dans ma bio.", None)]),
]
SPLITS = [(0.2, 4.007), (4.457, 7.591), (8.041, 10.898), (11.348, 14.669), (15.119, 17.54), (17.99, 20.39), (20.84, 26.62)]
MINLEN = 1.9
GAP = 0.32
TAIL = 2.2

CSS = '''
.li{color:#c9a8ff;text-shadow:0 0 18px rgba(177,140,255,.6)}
.sw{position:absolute;left:390px;width:300px;height:300px;border-radius:50%;border:8px solid #b18cff;background:radial-gradient(circle,#1d1530 0%,#0c0914 70%);box-shadow:0 0 60px rgba(177,140,255,.45);display:flex;align-items:center;justify-content:center;font:900 92px 'DejaVu Sans Mono',monospace;color:#fff}
.sw:before{content:'';position:absolute;left:125px;top:-44px;width:50px;height:34px;border-radius:8px;background:#b18cff}
.sw.sm{left:auto;right:110px;width:190px;height:190px;font-size:52px;border-width:6px}
.sw.sm:before{left:72px;top:-34px;width:36px;height:24px}
.it3{position:absolute;top:760px;width:290px;text-align:center}
.it3 .pt{display:inline-block;margin-top:10px;padding:6px 22px;border-radius:14px;background:#f4efe4;color:#1d1530;font:900 58px 'DejaVu Serif',serif;white-space:nowrap}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:800 28px Inter;letter-spacing:5px;color:#a59cb8}
.co{position:absolute;left:190px;top:700px;width:700px;border-radius:40px;background:#f4efe4;color:#16101f;padding:34px 44px;box-shadow:0 30px 90px rgba(0,0,0,.7)}
.co .t{font:900 40px Inter}
.co .row{display:flex;justify-content:space-between;font:600 32px Inter;margin-top:14px;white-space:nowrap}
.co .lab{margin-top:24px;font:800 24px Inter;letter-spacing:3px;color:#6b4fb0}
.co .in{margin-top:8px;height:96px;border-radius:18px;border:4px solid #c9c4ba;background:#fff;display:flex;align-items:center;padding:0 24px;font:900 56px 'DejaVu Sans Mono',monospace;color:#16101f;white-space:nowrap}
.co .in.on{border-color:#b18cff;box-shadow:0 0 0 6px rgba(177,140,255,.3)}
.co .ok{margin-top:14px;font:900 38px Inter;color:#1f9d55}
.co .tot{display:flex;justify-content:space-between;margin-top:22px;font:900 44px Inter;white-space:nowrap}
.ring{position:absolute;left:200px;top:1085px;width:680px;height:150px;border:8px solid #b18cff;border-radius:50%;transform:rotate(-3deg);box-shadow:0 0 30px rgba(177,140,255,.6)}
.calc{position:absolute;left:140px;top:1000px;width:800px;text-align:center;font:700 44px 'DejaVu Sans Mono',monospace;color:#e9e1f7;white-space:nowrap}
.minus{position:absolute;left:0;top:640px;width:1080px;text-align:center;font:900 230px 'DejaVu Serif',serif;color:#c9a8ff;text-shadow:0 0 40px rgba(177,140,255,.6);white-space:nowrap}
.totx{position:absolute;left:0;top:600px;width:1080px;text-align:center}
.totx .n{font:900 220px 'DejaVu Serif',serif;line-height:1.05;white-space:nowrap}
.totx .o{font:900 80px 'DejaVu Serif',serif;color:#8f877a;text-decoration:line-through;text-decoration-color:#ff4d6d;text-decoration-thickness:7px}
.chip{position:absolute;left:150px;width:780px;height:130px;border-radius:65px;background:#140e20;border:5px solid #b18cff;display:flex;align-items:center;justify-content:center;gap:24px;white-space:nowrap;box-shadow:0 0 50px rgba(177,140,255,.35)}
.chip .k{font:800 30px Inter;letter-spacing:3px;color:#d9c6ff}
.chip .c{font:900 64px 'DejaVu Sans Mono',monospace;color:#fff}
.stp{position:absolute;left:390px;top:560px;width:300px;height:76px;border-radius:38px;background:#b18cff;color:#140e20;font:900 34px Inter;letter-spacing:3px;display:flex;align-items:center;justify-content:center;white-space:nowrap}
'''


def checkout(code=False, g=None, top=700):
    if code:
        field = (f'<div class="in on"><span data-g="{g}" data-fx="type">hzklink</span></div>'
                 f'<div class="ok" data-g="{g}" data-fx="fade">✓ -14 % appliqué</div>')
    else:
        field = '<div class="in" style="color:#b5afa4">Ajouter un code</div>'
    return f'''<div class="co" style="top:{top}px"><div class="t">Mon panier Hacoo</div>
     <div class="row"><span>Plaid</span><b>18,00 €</b></div><div class="row"><span>Bougie</span><b>7,00 €</b></div><div class="row"><span>Mug</span><b>9,00 €</b></div>
     <div class="lab">CODE PROMO HACOO</div>{field}</div>'''


def sw(txt, top=1300, small=False):
    return f'<div class="sw{" sm" if small else ""}" style="top:{top}px">{txt}</div>'


BODY = hud('FRANCE · DÉFI CHRONO', 'HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + head(225, [('h1', 'CODE PROMO HACOO', None), ('big gold', '10 sec.', None), ('it li', 'pour payer moins cher', None)]) + sw('0:00', 860) + '''
   <div class="ex" style="top:1220px">DÉFI CHRONO · PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="1" data-in="right">''' + head(225, [('h1', 'TON PANIER', '1.0'), ('it gold', 'cocooning d\'hiver', '1.1')]) + f'''
   <div class="it3" style="left:70px" data-g="1.0" data-fx="pop">{icon('Plaid', 240)}<div class="pt">18 €</div></div>
   <div class="it3" style="left:395px" data-g="1.1" data-fx="pop">{icon('Bougie', 240)}<div class="pt">7 €</div></div>
   <div class="it3" style="left:720px" data-g="1.2" data-fx="pop">{icon('Mug', 240)}<div class="pt">9 €</div></div>
   <div class="ex" style="top:1150px" data-g="1.3" data-fx="stamp"><b style="font-size:60px;color:#fff;letter-spacing:2px">TOTAL 34,00 €</b><br>PRIX D'EXEMPLE</div>''' + sw('0:02', 1300, True) + '''</div>
  <div class="scene" data-s="2" data-in="right"><div class="stp" data-g="2.0" data-fx="pop">ÉTAPE 1</div>''' + head(225, [('h1', 'LA CASE', '2.0'), ('it li', 'code promo Hacoo', '2.1')]) + checkout() + '''
   <div class="ring" style="top:998px;height:126px" data-g="2.1" data-fx="pop"></div>''' + sw('0:04', 1300, True) + '''</div>
  <div class="scene" data-s="3" data-in="up"><div class="stp" data-g="3.0" data-fx="pop">ÉTAPE 2</div>''' + head(225, [('h1', 'TU TAPES', '3.0'), ('big gold', 'hzklink', '3.1')]) + checkout(True, '3.1') + sw('0:06', 1300, True) + '''</div>
  <div class="scene" data-s="4" data-in="pop">''' + head(225, [('h1 li', '-14 %', '4.0'), ('it gold', 'd\'un coup', '4.1')]) + '''
   <div class="minus" data-g="4.0" data-fx="stamp">-4,76 €</div>
   <div class="calc" data-g="4.1" data-fx="fade">34,00 € × 14 % = 4,76 €</div>''' + sw('0:07', 1300, True) + '''</div>
  <div class="scene" data-s="5" data-in="pop"><div class="rays" style="top:470px"></div>''' + head(225, [('h1', 'TOTAL', '5.0')]) + '''
   <div class="totx"><div class="n gold" data-g="5.0" data-fx="stamp" data-slow="5.0">29,24 €</div><div class="o" data-g="5.0" data-fx="fade">34,00 €</div></div>
   <div class="chip" style="top:1040px" data-g="5.1" data-fx="up"><span class="k">CODE PROMO HACOO</span><span class="c">hzklink</span></div>
   <div class="ex" style="top:1210px" data-g="5.1" data-fx="fade">PRIX D'EXEMPLE · 4,76 € D'ÉCONOMIE</div>''' + sw('0:08', 1300, True) + '''</div>
  <div class="scene" data-s="6" data-in="pop">''' + head(215, [('h1', 'CODE PROMO HACOO', '6.1'), ('big gold', 'hzklink', '6.2'), ('it li', "-14 % sur l'appli Hacoo", '6.2')]) + '''
   <div class="pill" style="top:780px;border-color:rgba(177,140,255,.85)" data-g="6.0" data-fx="up"><div class="pin" style="background:#b18cff;color:#140e20">⏱</div><div><b style="color:#d9c6ff">MÊME PAS 10 SECONDES</b><span data-g="6.3" data-fx="fade">liens des articles tendance en bio</span></div></div>
   <div class="cond" style="top:930px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
'''
