import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°1 du 11/11/2026 - style v3 nuit & or, accent bleu glacier, « la jauge budget » : bougie 7,90 + mug 9,50 + chaussettes 12,60 = 30,00 € -> 25,80 € avec le code promo Hacoo hzklink (-14 %, prix d'exemple).
NAME = 'hacoo16'
TITLE = 'Hacoo jauge glacier'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Trente euros sur Hacou ? Regarde ça.", [("30 € sur Hacoo ?", None), ("Regarde ça.", None)]),
 ("Une bougie, un mug et des chaussettes : trente euros pile.", [("Une bougie, un mug", None), ("et des chaussettes :", None), ("30 € pile.", None)]),
 ("Au paiement, tu tapes le code promo Hacou H Z K link.", [("Au paiement,", None), ("tu tapes le code promo Hacoo", None), ("hzklink.", None)]),
 ("La jauge redescend : vingt-cinq euros quatre-vingts.", [("La jauge redescend :", None), ("25,80 €.", None)]),
 ("Quatre euros vingt de gagnés, juste avec le code.", [("4,20 € de gagnés,", None), ("juste avec le code.", None)]),
 ("Moins quatorze pour cent, et les liens sont dans ma bio.", [("-14 %,", None), ("et les liens", None), ("sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 1.98), (2.482, 5.410), (5.839, 9.396), (9.923, 12.218), (12.712, 14.772), (15.203, 17.533)]
GSTART = [[0.1, 1.48], [2.49, 3.9, 4.75], [5.84, 6.3, 7.75], [9.93, 11.11], [12.72, 13.82], [15.21, 16.31, 16.9]]
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
.gl{color:#7fd8ff;text-shadow:0 0 18px rgba(127,216,255,.45)}
.gauge{position:absolute;left:400px;top:700px;width:150px;height:620px;border-radius:75px;border:6px solid #d9a24c;background:#0d0c0b;overflow:hidden;box-shadow:0 0 50px rgba(240,180,80,.25)}
.gauge .f{position:absolute;left:0;bottom:0;width:100%;transform-origin:50% 100%;background:linear-gradient(180deg,#d6f4ff,#7fd8ff 40%,#2b7fae)}
.gauge .gh{position:absolute;left:0;bottom:0;width:100%;height:100%;background:repeating-linear-gradient(180deg,rgba(127,216,255,.18) 0 10px,transparent 10px 20px)}
.gm{position:absolute;left:580px;font:800 34px 'DejaVu Sans Mono',monospace;color:#e9e4da;white-space:nowrap}
.gm:before{content:'';display:inline-block;width:40px;height:4px;background:#d9a24c;vertical-align:middle;margin-right:14px}
.tile{position:absolute;width:230px;height:310px;border-radius:30px;background:#10161a;border:3px solid #7fd8ff;text-align:center;box-shadow:0 30px 70px rgba(0,0,0,.6)}
.tile .n{font:800 28px Inter;color:#f1ead9;margin-top:6px}
.tile .p{font:900 44px 'DejaVu Serif',serif;color:#7fd8ff}
.field{position:absolute;left:150px;width:780px;border-radius:26px;background:#f4efe4;color:#1c1712;padding:26px 36px;box-shadow:0 30px 80px rgba(0,0,0,.6)}
.field .l{font:800 26px Inter;letter-spacing:4px;color:#7a6f60}
.field .v{font:900 72px 'DejaVu Sans Mono',monospace;margin-top:8px;white-space:nowrap}
.field .ok{position:absolute;right:30px;top:58px;padding:14px 26px;border-radius:20px;background:#2b7fae;color:#fff;font:900 34px Inter}
.tk{position:absolute;left:190px;top:660px;width:700px;background:#f4efe4;color:#1c1712;border-radius:18px;padding:36px 44px 40px;box-shadow:0 40px 90px rgba(0,0,0,.7);transform:rotate(-2deg)}
.tk .row{display:flex;justify-content:space-between;font:600 32px 'DejaVu Sans Mono',monospace;line-height:1.8;white-space:nowrap}
.tk hr{border:0;border-top:3px dashed #b9ae9c;margin:14px 0}
.tk .x{font:600 22px Inter;letter-spacing:3px;color:#7a6f60;text-align:center;margin-top:8px}
'''
MARKS = '<div class="gm" style="left:350px;top:695px">30 €</div><div class="gm" style="left:350px;top:1000px">15 €</div><div class="gm" style="left:350px;top:1300px">0 €</div>'
BODY = hud('FRANCE · PANIER', 'BUDGET') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('big gold', '30 €', None, 'font-size:170px'), ('h1', 'SUR HACOO ?', None, ''), ('it gold', 'regarde ça.', '0.1', 'font-size:70px')]) + '''
   <div class="gauge" style="top:780px;height:560px"><div class="f" style="height:100%"></div></div>
   <div class="gm" style="top:770px">PLEIN · 30 €</div></div>
  <div class="scene" data-s="1" data-in="pop"><div class="rays" style="top:560px"></div>''' + hd(230, [('h1 s', 'UNE BOUGIE, UN MUG', '1.0', ''), ('it gold', 'et des chaussettes :', '1.1', 'font-size:66px')]) + '''
   <div class="tile" style="left:110px;top:620px" data-g="1.0" data-fx="up">''' + icon('Bougie', 180) + '''<div class="n">Bougie</div><div class="p">7,90 €</div></div>
   <div class="tile" style="left:425px;top:600px" data-g="1.0" data-fx="up">''' + icon('Mug', 180) + '''<div class="n">Mug</div><div class="p">9,50 €</div></div>
   <div class="tile" style="left:700px;top:620px" data-g="1.1" data-fx="up">''' + icon('Chaussettes', 180) + '''<div class="n">Chaussettes</div><div class="p">12,60 €</div></div>
   <div class="abs gold" style="left:0;top:1060px;width:1080px;text-align:center;font:900 110px 'DejaVu Serif',serif" data-g="1.2" data-fx="stamp">= 30,00 €</div>
   <div class="abs" style="left:240px;top:1230px;width:600px;text-align:center;font:700 24px Inter;letter-spacing:4px;color:#bba98a">PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1', 'AU PAIEMENT,', '2.0', ''), ('it gold', 'tu tapes le code promo Hacoo', '2.1', 'font-size:58px')]) + '''
   <div class="field" style="top:640px" data-g="2.0" data-fx="up"><div class="l">CODE PROMO HACOO</div><div class="v"><span data-g="2.2" data-fx="type">hzklink</span></div><div class="ok" data-g="2.2" data-fx="pop">OK</div></div>
   <div class="pill" style="top:900px;border-color:rgba(127,216,255,.85)" data-g="2.2" data-fx="up"><div class="pin" style="background:#7fd8ff">%</div><div><b class="gl">CODE HACOO : hzklink</b><span>-14 % sur ton panier</span></div></div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('h1', 'LA JAUGE REDESCEND :', '3.0', 'font-size:66px')]) + '''
   <div class="gauge" style="left:170px"><div class="f" style="height:100%"></div><div class="abs" style="left:0;top:0;width:100%;height:14%;background:#0d0c0b;transform-origin:50% 0" data-g="3.0" data-fx="growY"><div class="gh"></div></div></div>''' + MARKS + '''
   <div class="abs gold" style="left:520px;top:780px;font:900 96px 'DejaVu Serif',serif;white-space:nowrap" data-g="3.1" data-fx="stamp" data-slow="3.1">25,80 €</div>
   <div class="abs" style="left:540px;top:910px;font:700 32px Inter;color:#8f877a;text-decoration:line-through;white-space:nowrap" data-g="3.1" data-fx="fade">avant : 30,00 €</div></div>
  <div class="scene" data-s="4" data-in="up">''' + hd(230, [('h1', '4,20 € DE GAGNÉS,', '4.0', ''), ('it gold', 'juste avec le code.', '4.1', 'font-size:70px')]) + '''
   <div class="tk" data-g="4.0" data-fx="up"><div class="row"><span>Panier</span><span>30,00 €</span></div><div class="row" style="color:#2b7fae"><span>Code hzklink</span><span>-4,20 €</span></div><hr>
    <div class="row" style="font-weight:700;font-size:40px" data-g="4.1" data-fx="stamp"><span>À PAYER</span><span>25,80 €</span></div><div class="x">PRIX D'EXEMPLE · CODE PROMO HACOO</div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'CODE PROMO HACOO', '5.0', ''), ('big gold', 'hzklink', '5.0', 'font-size:150px'), ('it gold', "-14 % sur l'appli Hacoo", '5.1', 'font-size:60px')]) + '''
   <div class="pill" style="top:730px" data-g="5.2" data-fx="up"><div class="pin">★</div><div><b>ARTICLES TENDANCE</b><span>tous les liens sont dans ma bio</span></div></div>
   <div class="cond" style="top:880px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
