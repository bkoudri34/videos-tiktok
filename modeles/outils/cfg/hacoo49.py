import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°3 du 23/11/2026 (tâche « 2 vidéos Hacoo en plus ») - style V3 nuit & or, accent rose framboise.
# Format F9 duel / comparatif : « Même panier Hacoo, deux prix » -> colonnes SANS CODE 58,00 € / AVEC CODE ?? dès la 1re image
# -> le panier (survêt, casquette, trousse) -> à droite la case code promo Hacoo -> hzklink -14 % -> -8,12 €
# -> duel 58,00 € vs 49,88 € (ralenti) -> fin « enregistre ». Pas de sujet R.
# Prix d'exemple : survêt 36 € + casquette 13 € + trousse 9 € = 58,00 € ; -14 % = 8,12 € (58 x 0,14) ; total 49,88 € (58 x 0,86).
# Voix : Speko Etienne (cartesia sonic-3.5), speed 1.08, une synthèse par réplique, silences coupés (internes plafonnés à 0,16 s), atempo 1.12.
NAME = 'hacoo49'
TITLE = 'Hacoo duel framboise'
ROOT = ':root{--bg:#0a0508}'
LINES = [
 ("Même panier sur l'appli Hacou, deux prix différents. Pourquoi ?", [("Même panier <em>Hacoo</em>,", None), ("deux prix différents.", None), ("Pourquoi ?", None)]),
 ("À gauche : survêt, casquette, trousse. Cinquante-huit euros.", [("À gauche :", None), ("survêt, casquette,", None), ("trousse.", None), ("<em>58 €</em>.", None)]),
 ("À droite, les mêmes articles. Mais avec une case en plus : la case code promo.", [("À droite,", None), ("les mêmes articles.", None), ("Mais une case en plus :", None), ("la case code promo.", None)]),
 ("Code promo Hacou : H, Z, K, link. Moins quatorze pour cent.", [("<em>Code promo Hacoo</em> :", None), ("<i>hzklink</i>.", None), ("<em>-14&nbsp;%</em>.", None)]),
 ("Résultat : huit euros et douze centimes de moins.", [("Résultat :", None), ("<em>8,12 €</em> de moins.", None)]),
 ("Quarante-neuf euros et quatre-vingt-huit centimes, au lieu de cinquante-huit. Et ce sont des prix d'exemple.", [("<em>49,88 €</em>", None), ("au lieu de 58.", None), ("Et ce sont", None), ("des prix d'exemple.", None)]),
 ("Enregistre cette vidéo pour tes achats de fin d'année. Code promo Hacou : H, Z, K, link. Les liens sont dans ma bio.", [("Enregistre cette vidéo", None), ("pour tes achats", None), ("de fin d'année.", None), ("<em>Code promo Hacoo</em> :", None), ("<i>hzklink</i>.", None), ("Les liens sont dans ma bio.", None)]),
]
SPLITS = [(0.2, 2.986), (3.436, 6.61), (7.06, 10.951), (11.401, 15.887), (16.337, 18.693), (19.143, 24.165), (24.615, 31.955)]
MINLEN = 1.9
GAP = 0.22
TAIL = 2.2

A = '#ff4f8b'


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.em2{color:#ff6b9d;text-shadow:0 0 18px rgba(255,79,139,.5)}
.col{position:absolute;top:640px;width:430px;height:560px;border-radius:36px;background:#160a10;border:5px solid #5a3a46;text-align:center;padding-top:34px}
.col.r{border-color:#ff4f8b;box-shadow:0 0 60px rgba(255,79,139,.3)}
.col .k{font:900 36px Inter;letter-spacing:4px;color:#c9b6bd}
.col.r .k{color:#ffd0e0;font-size:25px;letter-spacing:2px;margin-top:6px}
.col .ic{display:flex;justify-content:center;gap:4px;margin-top:26px}
.col .p{margin-top:30px;font:900 84px 'DejaVu Serif',serif;white-space:nowrap}
.col .p.q{color:#ff6b9d}
.col .p.o{color:#8f877a;text-decoration:line-through;text-decoration-color:#ff4f8b;text-decoration-thickness:7px}
.col .f{margin:26px auto 0;width:340px;height:76px;border-radius:16px;border:4px dashed #ff4f8b;font:900 40px 'DejaVu Sans Mono',monospace;color:#fff;display:flex;align-items:center;justify-content:center}
.col .f.e{border-color:#5a3a46;color:#5a3a46}
.vs{position:absolute;left:485px;top:600px;width:110px;height:110px;border-radius:50%;background:linear-gradient(135deg,#ffe3ed,#ff4f8b 55%,#a3164a);color:#1a0610;font:900 44px Inter;display:flex;align-items:center;justify-content:center;box-shadow:0 20px 60px rgba(0,0,0,.6);z-index:3}
.it3{position:absolute;top:640px;width:290px;text-align:center}
.it3 .pt{display:inline-block;margin-top:10px;padding:6px 22px;border-radius:14px;background:#f4efe4;color:#1f0d15;font:900 58px 'DejaVu Serif',serif;white-space:nowrap}
.it3 .nm{font:800 34px Inter;color:#e9e4da;margin-top:6px}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:800 28px Inter;letter-spacing:5px;color:#a8939c}
.co{position:absolute;left:190px;width:700px;border-radius:40px;background:#f4efe4;color:#1f0d15;padding:34px 44px;box-shadow:0 30px 90px rgba(0,0,0,.7)}
.co .t{font:900 40px Inter}
.co .row{display:flex;justify-content:space-between;font:600 32px Inter;margin-top:14px;white-space:nowrap}
.co .lab{margin-top:24px;font:800 26px Inter;letter-spacing:3px;color:#c2185b}
.co .fr{display:flex;gap:14px;margin-top:8px}
.co .in{flex:1;height:96px;border-radius:18px;border:4px solid #c2185b;box-shadow:0 0 0 6px rgba(194,24,91,.25);background:#fff;display:flex;align-items:center;padding:0 24px;font:900 54px 'DejaVu Sans Mono',monospace;color:#1f0d15;white-space:nowrap}
.co .ap{height:96px;padding:0 24px;border-radius:18px;background:#c2185b;color:#fff;font:900 32px Inter;display:flex;align-items:center}
.co .ok{margin-top:18px;font:900 38px Inter;color:#c2185b;display:flex;justify-content:space-between;white-space:nowrap}
.pct{position:absolute;left:340px;top:700px;width:400px;height:400px;border-radius:50%;border:8px solid #ff4f8b;display:flex;align-items:center;justify-content:center;white-space:nowrap;font:900 150px 'DejaVu Serif',serif;color:#fff;box-shadow:0 0 70px rgba(255,79,139,.35)}
.chip{position:absolute;left:150px;width:780px;border-radius:52px;background:#160a10;border:5px solid #ff4f8b;display:flex;align-items:center;justify-content:center;white-space:nowrap}
.chip .k{font:800 30px Inter;letter-spacing:3px;color:#ffd0e0}
'''

ITEMS = [('Survêt', 'Survêt', 36), ('Casquette', 'Casquette', 13), ('Trousse', 'Trousse', 9)]


def col(side, k, price, pcls, field, g=None, ic=78):
    a = f' data-g="{g}" data-fx="pop"' if g else ''
    left = 60 if side == 'l' else 590
    icons = ''.join(icon(n, ic) for n, _, _ in ITEMS)
    f = f'<div class="f{" e" if field == "" else ""}">{field or "code promo ?"}</div>'
    return f'<div class="col {side}" style="left:{left}px"{a}><div class="k">{k}</div><div class="ic">{icons}</div><div class="p {pcls}">{price}</div>{f}</div>'


BODY = hud('FRANCE · LE DUEL', 'HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(215, [('h1', 'MÊME PANIER HACOO', None, 'font-size:74px'), ('it em2', 'deux prix différents ?', None, 'font-size:68px')]) + \
    col('l', 'SANS CODE', '58,00 €', '', '') + col('r', 'AVEC CODE PROMO HACOO', '?? €', 'q', 'hzklink') + '''<div class="vs">VS</div>
   <div class="ex" style="top:1240px">PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="1" data-in="right">''' + hd(215, [('h1', 'À GAUCHE :', '1.0', ''), ('it em2', 'survêt, casquette, trousse', '1.1', 'font-size:60px')]) + ''.join(
    f'<div class="it3" style="left:{70 + 325 * k}px" data-g="1.{1 + (k > 1)}" data-fx="pop">{icon(n, 230)}<div class="nm">{lab}</div><div class="pt">{p} €</div></div>' for k, (n, lab, p) in enumerate(ITEMS)) + '''
   <div class="ex" style="top:1110px" data-g="1.3" data-fx="stamp"><b style="font-size:70px;color:#fff;letter-spacing:2px">TOTAL 58,00 €</b><br>PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="2" data-in="left">''' + hd(215, [('h1', 'À DROITE :', '2.0', ''), ('it em2', 'les mêmes articles…', '2.1', 'font-size:60px')]) + '''
   <div class="co" style="top:600px"><div class="t">Mon panier Hacoo</div>
    <div class="row"><span>Survêt</span><b>36,00 €</b></div><div class="row"><span>Casquette</span><b>13,00 €</b></div><div class="row"><span>Trousse</span><b>9,00 €</b></div>
    <div data-g="2.2" data-fx="pop"><div class="lab">+ LA CASE CODE PROMO HACOO</div><div class="fr"><div class="in" style="color:#b5afa4">|</div><div class="ap">Appliquer</div></div></div></div></div>
  <div class="scene" data-s="3" data-in="up"><div class="rays" style="top:560px"></div>''' + hd(215, [('h1', 'CODE PROMO HACOO', '3.0', 'font-size:72px'), ('big gold', 'hzklink', '3.1', 'font-size:140px')]) + '''
   <div class="co" style="top:700px"><div class="lab" style="margin-top:0">CODE PROMO HACOO</div><div class="fr"><div class="in"><span data-g="3.1" data-fx="type">hzklink</span></div><div class="ap">Appliquer</div></div>
    <div class="ok" data-g="3.2" data-fx="stamp"><span>✓ Code appliqué</span><span>-14 %</span></div></div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="floor"></div>''' + hd(215, [('h1', 'RÉSULTAT :', '4.0', '')]) + '''
   <div class="pct" data-g="4.1" data-fx="stamp" style="font-size:118px">-8,12 €</div>
   <div class="ex" style="top:1150px" data-g="4.1" data-fx="fade">58,00 € × 14 % = 8,12 € · PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="5" data-in="right"><div class="rays" style="top:600px"></div>''' + hd(215, [('h1', 'MÊME PANIER HACOO', '5.0', 'font-size:70px'), ('it em2', 'deux prix', '5.0', 'font-size:64px')]) + \
    col('l', 'SANS CODE', '58,00 €', 'o', '') + col('r', 'AVEC CODE PROMO HACOO', '<span data-g="5.0" data-fx="stamp" data-slow="5.0">49,88 €</span>', 'gold', 'hzklink') + '''<div class="vs">VS</div>
   <div class="ex" style="top:1240px;font-size:38px;color:#fff" data-g="5.3" data-fx="stamp">PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(215, [('h1', 'CODE PROMO HACOO', '6.0', ''), ('big gold', 'hzklink', '6.0', 'font-size:150px'), ('it em2', "-14 % sur l'appli Hacoo", '6.1', 'font-size:66px')]) + '''
   <div class="pill" style="top:720px;border-color:rgba(255,79,139,.85)" data-g="6.1" data-fx="up"><div class="pin" style="background:#ff4f8b;color:#1a0610">★</div><div><b style="color:#ffd0e0">ENREGISTRE CETTE VIDÉO</b><span>pour tes achats de fin d'année</span></div></div>
   <div class="chip" style="top:870px;height:100px" data-g="6.2" data-fx="up"><span class="k">LIENS DES ARTICLES TENDANCE EN BIO</span></div>
   <div class="cond" style="top:1010px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
'''
