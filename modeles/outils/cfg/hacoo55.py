import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°1 du 25/11/2026 - style V3 nuit & or, accent bleu saphir (brief veille du 25/11). Format F2 démystification
# « Le code promo Hacoo, ça te fait combien ? » : -14 % plein écran dès la 1re image -> règle « 1,40 € tous les 10 € » (pièce coupée)
# -> panier d'exemple casque audio 42 € + sac 13 € + pinces 7 € = 62,00 € -> calcul 6 x 1,40 = 8,40 + 0,28 -> -8,68 € -> 53,32 € (ralenti)
# -> case code promo Hacoo hzklink + Appliquer -> fin « enregistre ». Pas de sujet R.
# Prix d'exemple : 62,00 x 0,14 = 8,68 ; 62,00 x 0,86 = 53,32.
# Voix : Speko Leo (xai), speed 1.08, une synthèse, silences internes plafonnés à 0,16 s, atempo 1.15.
NAME = 'hacoo55'
TITLE = 'Hacoo combien saphir'
ROOT = ':root{--bg:#04060c}'
LINES = [
 ("Code promo Hacou, moins quatorze pour cent. Mais en vrai, ça te fait combien ?", [("Code promo Hacoo,", None), ("-14 %.", None), ("Mais en vrai,", None), ("ça te fait combien ?", None)]),
 ("Retiens juste ça : un euro quarante de moins tous les dix euros.", [("Retiens juste ça :", None), ("1,40 € de moins", None), ("tous les 10 €.", None)]),
 ("Exemple : un casque audio, un sac et des pinces. Soixante-deux euros.", [("Exemple :", None), ("un casque audio,", None), ("un sac et des pinces.", None), ("62 €.", None)]),
 ("Six fois dix euros : huit euros quarante. Plus vingt-huit centimes pour les deux euros qui restent.", [("6 × 10 € :", None), ("8,40 €.", None), ("Plus 0,28 €", None), ("pour les 2 € qui restent.", None)]),
 ("Total : huit euros soixante-huit de moins. Tu paies cinquante-trois euros et trente-deux centimes.", [("Total :", None), ("8,68 € de moins.", None), ("Tu paies", None), ("53,32 €.", None)]),
 ("Sur l'appli Hacou, tape le code promo Hacou, H, Z, K, link, puis appuie sur Appliquer.", [("Sur l'appli Hacoo,", None), ("tape le code promo Hacoo,", None), ("hzklink,", None), ("puis Appliquer.", None)]),
 ("Enregistre cette vidéo pour ton prochain panier. Les liens sont dans ma bio.", [("Enregistre cette vidéo", None), ("pour ton prochain panier.", None), ("Les liens sont dans ma bio.", None)]),
]
SPLITS = [(0.174, 3.557), (4.007, 6.877), (7.327, 10.668), (11.118, 15.134), (15.584, 19.445), (19.895, 24.786), (25.236, 28.116)]
MINLEN = 1.9
GAP = 0.2
TAIL = 2.2


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px;left:90px;width:840px">' + ''.join(out) + '</div>'


CSS = '''
.sp{color:#7fb0ff;text-shadow:0 0 18px rgba(80,140,255,.55)}
.pct{position:absolute;left:250px;width:580px;height:580px;border-radius:50%;border:8px solid #4f8cff;display:flex;flex-direction:column;align-items:center;justify-content:center;white-space:nowrap;box-shadow:0 0 80px rgba(79,140,255,.35),inset 0 0 60px rgba(79,140,255,.15);background:radial-gradient(circle,#0d1630,#05070e 70%)}
.pct b{font:900 165px 'DejaVu Serif',serif;line-height:1}
.pct span{margin-top:10px;font:900 64px Inter;color:#7fb0ff}
.coin2{position:absolute;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#fff0c0,#e9b456 45%,#a8701f 100%);display:flex;align-items:center;justify-content:center;font:900 96px 'DejaVu Serif',serif;color:#3a2408;box-shadow:0 0 50px rgba(240,180,80,.45);white-space:nowrap}
.shard{position:absolute;padding:18px 34px;border-radius:24px;background:#0d1630;border:5px solid #4f8cff;font:900 80px 'DejaVu Serif',serif;color:#fff;white-space:nowrap;transform:rotate(8deg)}
.it3{position:absolute;width:280px;text-align:center}
.it3 .pt{display:inline-block;margin-top:10px;padding:6px 22px;border-radius:14px;background:#eef2fb;color:#0b1430;font:900 56px 'DejaVu Serif',serif;white-space:nowrap}
.it3 .nm{font:800 34px Inter;color:#e9e4da;margin-top:6px;white-space:nowrap}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:800 26px Inter;letter-spacing:4px;color:#93a3c4}
.tile{position:absolute;left:150px;width:780px;height:150px;border-radius:30px;background:#0b1226;border:4px solid #33528f;display:flex;align-items:center;justify-content:space-between;padding:0 40px;white-space:nowrap}
.tile span{font:800 44px Inter;color:#dfe8ff}.tile b{font:900 74px 'DejaVu Serif',serif}
.tile.h{border-color:#f3c766;box-shadow:0 0 40px rgba(240,180,80,.3)}
.old{position:absolute;left:0;width:1080px;text-align:center;font:900 90px 'DejaVu Serif',serif;color:#7d869a;text-decoration:line-through;text-decoration-color:#ff5a6a;text-decoration-thickness:8px}
.tot{position:absolute;left:0;width:1080px;text-align:center}
.tot .v{font:900 190px 'DejaVu Serif',serif;line-height:1;white-space:nowrap}
.co{position:absolute;left:170px;width:740px;border-radius:40px;background:#eef2fb;color:#0b1430;padding:34px 44px;box-shadow:0 30px 90px rgba(0,0,0,.7)}
.co .lab{font:900 30px Inter;letter-spacing:3px;color:#2a5fd6}
.co .fr{display:flex;gap:14px;margin-top:12px}
.co .in{flex:1;height:100px;border-radius:18px;border:4px solid #2a5fd6;box-shadow:0 0 0 6px rgba(42,95,214,.2);background:#fff;display:flex;align-items:center;padding:0 24px;font:900 56px 'DejaVu Sans Mono',monospace;color:#0b1430;white-space:nowrap}
.co .ap{height:100px;padding:0 26px;border-radius:18px;background:#2a5fd6;color:#fff;font:900 32px Inter;display:flex;align-items:center}
.co .ok{margin-top:20px;font:900 40px Inter;color:#2a5fd6;display:flex;justify-content:space-between;white-space:nowrap}
.chip{position:absolute;left:150px;width:780px;height:100px;border-radius:50px;background:#0b1226;border:5px solid #4f8cff;display:flex;align-items:center;justify-content:center;white-space:nowrap;font:800 30px Inter;letter-spacing:3px;color:#dfe8ff}
'''

ITEMS = [('Casque', 'Casque audio', 42), ('Tote', 'Sac', 13), ('Pinces', 'Pinces', 7)]

BODY = hud('FRANCE · LE CALCUL', 'HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(215, [('h1', 'LE CODE PROMO HACOO,', None, 'font-size:62px'), ('it sp', 'ça te fait combien ?', None, 'font-size:76px')]) + '''
   <div class="pct" style="top:520px"><b class="gold">-14 %</b><span data-g="0.3" data-fx="pop">= ? €</span></div>
   <div class="ex" style="top:1150px">CODE PROMO HACOO · hzklink</div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(215, [('h1', 'RETIENS JUSTE ÇA :', '1.0', 'font-size:64px'), ('big gold', '-1,40 €', '1.1', 'font-size:130px'), ('it sp', 'tous les 10 €.', '1.2', 'font-size:72px')]) + '''
   <div class="coin2" style="left:240px;top:760px" data-g="1.1" data-fx="pop">10 €</div>
   <div class="shard" style="left:580px;top:840px" data-g="1.2" data-fx="right">1,40 €</div>
   <div class="ex" style="top:1120px" data-g="1.2" data-fx="fade">14 % DE 10 € = 1,40 €</div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(215, [('h1', 'EXEMPLE :', '2.0', 'font-size:70px'), ('it sp', 'un casque, un sac, des pinces', '2.1', 'font-size:56px')]) + ''.join(
    f'<div class="it3" style="left:{80 + 320 * k}px;top:470px" data-g="2.{1 + k}" data-fx="pop">{icon(n, 220)}<div class="nm">{lab}</div><div class="pt">{p} €</div></div>' for k, (n, lab, p) in enumerate(ITEMS)) + '''
   <div class="tile h" style="top:930px" data-g="2.3" data-fx="stamp"><span>Total panier</span><b class="gold">62,00 €</b></div>
   <div class="ex" style="top:1110px">PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(215, [('h1', '6 × 10 € :', '3.0', 'font-size:80px')]) + '''
   <div class="tile" style="top:400px" data-g="3.0" data-fx="left"><span>6 × 1,40 €</span><b class="gold" data-g="3.1" data-fx="stamp">8,40 €</b></div>
   <div class="tile" style="top:580px" data-g="3.2" data-fx="left"><span>2 € × 14 %</span><b class="gold">0,28 €</b></div>
   <div class="tile h" style="top:800px" data-g="3.3" data-fx="up"><span>Réduction</span><b class="gold">8,68 €</b></div>
   <div class="ex" style="top:990px" data-g="3.3" data-fx="fade">62,00 € × 14 % = 8,68 € · PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:560px"></div>''' + hd(215, [('h1 sp', 'TOTAL : -8,68 €', '4.0', 'font-size:76px'), ('it gold', 'tu paies', '4.2', 'font-size:66px')]) + '''
   <div class="old" style="top:470px" data-g="4.1" data-fx="pop">62,00 €</div>
   <div class="tot" style="top:620px" data-g="4.3" data-fx="stamp" data-slow="4.3"><div class="v gold">53,32 €</div></div>
   <div class="ex" style="top:880px" data-g="4.3" data-fx="fade">AVEC LE CODE PROMO HACOO · PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="5" data-in="up">''' + hd(215, [('h1', "SUR L'APPLI HACOO,", '5.0', 'font-size:64px'), ('it sp', 'tape le code promo Hacoo', '5.1', 'font-size:60px')]) + '''
   <div class="co" style="top:520px"><div class="lab">CODE PROMO HACOO</div><div class="fr"><div class="in"><span data-g="5.2" data-fx="type">hzklink</span></div><div class="ap">Appliquer</div></div>
    <div class="ok" data-g="5.3" data-fx="stamp"><span>✓ Code appliqué</span><span>-14 %</span></div></div>
   <div class="chip" style="top:900px" data-g="5.3" data-fx="up">62,00 € → 53,32 € · PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(215, [('h1', 'CODE PROMO HACOO', '6.0', 'font-size:70px'), ('big gold', 'hzklink', '6.0', 'font-size:140px'), ('it sp', "-14 % sur l'appli Hacoo", '6.1', 'font-size:62px')]) + '''
   <div class="pill" style="top:720px;border-color:rgba(79,140,255,.85)" data-g="6.0" data-fx="up"><div class="pin" style="background:#4f8cff;color:#04060c">★</div><div><b style="color:#dfe8ff">ENREGISTRE CETTE VIDÉO</b><span>1,40 € de moins tous les 10 €</span></div></div>
   <div class="chip" style="top:870px" data-g="6.2" data-fx="up">LIENS DES ARTICLES TENDANCE EN BIO</div>
   <div class="cond" style="top:1010px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
'''
