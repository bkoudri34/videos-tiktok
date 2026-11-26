import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# 3e vidéo Hacoo du 26/11/2026 - style V3 nuit & or, accent violet améthyste. Format quiz « Avec le code promo, tu paies combien ? »
# 3 réponses A/B/C dès la 1re image -> panier bottines 37 € + pyjama 12 € + trousse 5 € = 54,00 € -> « réfléchis 2 s »
# -> -14 % = 7,56 € -> bonne réponse B : 46,44 € (ralenti) -> case code promo hzklink -> fin « écris ta réponse en commentaire ».
# Prix d'exemple : 54,00 x 0,14 = 7,56 ; 54,00 x 0,86 = 46,44. Pas de sujet R.
# RÈGLE DU 26/11 : le nom de l'appli n'est JAMAIS écrit (ni à l'image ni dans les sous-titres), seulement dit à l'oral.
# Voix : Speko Hélène (inworld-tts-2), speed 1.08, une synthèse par réplique, silences internes plafonnés à 0,16 s, atempo 1.1, -19 dB moyen.
NAME = 'hacoo61'
TITLE = 'Quiz code promo amethyste'
ROOT = ':root{--bg:#07040c}'
LINES = [
 ("Sur l'appli Hacou, un panier à cinquante-quatre euros. Avec le code promo, tu paies combien ?", [("Sur l'appli,", None), ("un panier à 54 €.", None), ("Avec le code promo,", None), ("tu paies combien ?", None)]),
 ("Des bottines, un pyjama et une trousse. Prix d'exemple.", [("Des bottines,", None), ("un pyjama et une trousse.", None), ("Prix d'exemple.", None)]),
 ("Réponse A, B ou C ? Réfléchis deux secondes.", [("Réponse A, B ou C ?", None), ("Réfléchis 2 secondes.", None)]),
 ("Le code promo Hacou, c'est moins quatorze pour cent. Donc sept euros et cinquante-six centimes de moins.", [("Le code promo,", None), ("c'est -14 %.", None), ("Donc 7,56 €", None), ("de moins.", None)]),
 ("Bonne réponse : B. Tu paies quarante-six euros et quarante-quatre centimes.", [("Bonne réponse :", None), ("B !", None), ("Tu paies", None), ("46,44 €.", None)]),
 ("Code promo Hacou : H, Z, K, link. Tu le tapes dans la case code promo, avant de payer.", [("Code promo :", None), ("hzklink.", None), ("Tape-le dans la case", None), ("code promo, avant de payer.", None)]),
 ("Écris ta réponse en commentaire, et enregistre la vidéo. Les liens sont dans ma bio.", [("Écris ta réponse", None), ("en commentaire,", None), ("et enregistre la vidéo.", None), ("Les liens sont dans ma bio.", None)]),
]
SPLITS = [(0.2, 4.463), (4.913, 7.82), (8.27, 11.189), (11.639, 16.624), (17.074, 20.76), (21.21, 26.871), (27.321, 31.089)]
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
.vi{color:#c9a2ff;text-shadow:0 0 18px rgba(170,110,255,.55)}
.opt{position:absolute;left:150px;width:780px;height:140px;border-radius:30px;background:#140c22;border:5px solid #5a3a8c;display:flex;align-items:center;padding:0 36px;white-space:nowrap;gap:34px}
.opt .k{width:92px;height:92px;border-radius:50%;background:#2a1a44;border:4px solid #b07cff;display:flex;align-items:center;justify-content:center;font:900 54px Inter;color:#e6d6ff}
.opt b{font:900 76px 'DejaVu Serif',serif;color:#f1ecf8}
.opt.ok{border-color:#f3c766;box-shadow:0 0 50px rgba(240,180,80,.45);background:#1d1430}
.opt.ok .k{background:#f3c766;color:#1a1020;border-color:#f3c766}
.opt .tick{margin-left:auto;font:900 70px Inter;color:#f3c766}
.opt.dim{opacity:.35}
.it3{position:absolute;width:280px;text-align:center}
.it3 .pt{display:inline-block;margin-top:10px;padding:6px 22px;border-radius:14px;background:#f1ecf8;color:#1a1020;font:900 56px 'DejaVu Serif',serif;white-space:nowrap}
.it3 .nm{font:800 34px Inter;color:#e9e4da;margin-top:6px;white-space:nowrap}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:800 26px Inter;letter-spacing:4px;color:#a596bf}
.tile{position:absolute;left:150px;width:780px;height:150px;border-radius:30px;background:#140c22;border:4px solid #5a3a8c;display:flex;align-items:center;justify-content:space-between;padding:0 40px;white-space:nowrap}
.tile span{font:800 44px Inter;color:#eadcff}.tile b{font:900 74px 'DejaVu Serif',serif}
.tile.h{border-color:#f3c766;box-shadow:0 0 40px rgba(240,180,80,.3)}
.ring{position:absolute;left:390px;width:300px;height:300px;border-radius:50%;border:10px solid #b07cff;display:flex;align-items:center;justify-content:center;font:900 150px 'DejaVu Serif',serif;color:#f1ecf8;box-shadow:0 0 70px rgba(170,110,255,.4)}
.old{position:absolute;left:0;width:1080px;text-align:center;font:900 90px 'DejaVu Serif',serif;color:#7d7590;text-decoration:line-through;text-decoration-color:#ff5a6a;text-decoration-thickness:8px}
.tot{position:absolute;left:0;width:1080px;text-align:center}
.tot .v{font:900 190px 'DejaVu Serif',serif;line-height:1;white-space:nowrap}
.co{position:absolute;left:170px;width:740px;border-radius:40px;background:#f1ecf8;color:#1a1020;padding:34px 44px;box-shadow:0 30px 90px rgba(0,0,0,.7)}
.co .lab{font:900 30px Inter;letter-spacing:3px;color:#7a3fd6}
.co .fr{display:flex;gap:14px;margin-top:12px}
.co .in{flex:1;height:100px;border-radius:18px;border:4px solid #7a3fd6;box-shadow:0 0 0 6px rgba(122,63,214,.2);background:#fff;display:flex;align-items:center;padding:0 24px;font:900 56px 'DejaVu Sans Mono',monospace;color:#1a1020;white-space:nowrap}
.co .ap{height:100px;padding:0 26px;border-radius:18px;background:#7a3fd6;color:#fff;font:900 32px Inter;display:flex;align-items:center}
.co .ok{margin-top:20px;font:900 40px Inter;color:#7a3fd6;display:flex;justify-content:space-between;white-space:nowrap}
.chip{position:absolute;left:150px;width:780px;height:100px;border-radius:50px;background:#140c22;border:5px solid #b07cff;display:flex;align-items:center;justify-content:center;white-space:nowrap;font:800 30px Inter;letter-spacing:3px;color:#eadcff}
'''

ITEMS = [('Bottines', 'Bottines', 37), ('Pyjama', 'Pyjama', 12), ('Trousse', 'Trousse', 5)]
OPTS = [('A', '48,60 €'), ('B', '46,44 €'), ('C', '40,00 €')]


def opts(top, step, g=None, ok=False):
    out = []
    for k, (l, v) in enumerate(OPTS):
        cls = 'opt' + ((' ok' if l == 'B' else ' dim') if ok else '')
        a = f' data-g="{g}.{min(k, 1)}" data-fx="left"' if g is not None else ''
        tick = '<span class="tick">✓</span>' if ok and l == 'B' else ''
        out.append(f'<div class="{cls}" style="top:{top + step * k}px"{a}><div class="k">{l}</div><b>{v}</b>{tick}</div>')
    return ''.join(out)


BODY = hud('FRANCE · LE QUIZ', 'CODE PROMO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(200, [('h1', 'PANIER DE 54 €', None, 'font-size:76px'), ('it vi', 'avec le code promo,<br>tu paies combien ?', None, 'font-size:64px')]) + opts(560, 175) + '''
   <div class="ex" style="top:1110px">QUIZ · PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(215, [('h1', 'LE PANIER :', '1.0', 'font-size:70px'), ('it vi', 'bottines, pyjama, trousse', '1.1', 'font-size:56px')]) + ''.join(
    f'<div class="it3" style="left:{80 + 320 * k}px;top:470px" data-g="1.{min(k, 1)}" data-fx="pop">{icon(n, 220)}<div class="nm">{lab}</div><div class="pt">{p} €</div></div>' for k, (n, lab, p) in enumerate(ITEMS)) + '''
   <div class="tile h" style="top:930px" data-g="1.2" data-fx="stamp"><span>Total panier</span><b class="gold">54,00 €</b></div>
   <div class="ex" style="top:1110px">PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(215, [('h1', 'A, B OU C ?', '2.0', 'font-size:90px')]) + opts(420, 170, 2) + '''
   <div class="ring" style="top:930px;width:200px;height:200px;left:440px;font-size:100px" data-g="2.1" data-fx="pop">2 s</div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(215, [('h1', 'LE CODE PROMO :', '3.0', 'font-size:70px'), ('big gold', '-14 %', '3.1', 'font-size:140px')]) + '''
   <div class="tile" style="top:560px" data-g="3.1" data-fx="left"><span>54,00 € × 14 %</span><b class="gold" data-g="3.2" data-fx="stamp">7,56 €</b></div>
   <div class="tile h" style="top:760px" data-g="3.3" data-fx="up"><span>Réduction</span><b class="gold">-7,56 €</b></div>
   <div class="ex" style="top:960px" data-g="3.3" data-fx="fade">54,00 € × 0,14 = 7,56 € · PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:640px"></div>''' + hd(200, [('h1 vi', 'BONNE RÉPONSE : B', '4.0', 'font-size:76px')]) + '''
   <div class="opt ok" style="top:360px" data-g="4.1" data-fx="stamp"><div class="k">B</div><b>46,44 €</b><span class="tick">✓</span></div>
   <div class="old" style="top:580px" data-g="4.2" data-fx="pop">54,00 €</div>
   <div class="tot" style="top:720px" data-g="4.3" data-fx="stamp" data-slow="4.3"><div class="v gold">46,44 €</div></div>
   <div class="ex" style="top:960px" data-g="4.3" data-fx="fade">AVEC LE CODE PROMO hzklink · PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="5" data-in="up">''' + hd(215, [('h1', 'CODE PROMO :', '5.0', 'font-size:70px'), ('it vi', 'dans la case, avant de payer', '5.2', 'font-size:56px')]) + '''
   <div class="co" style="top:520px"><div class="lab">CODE PROMO</div><div class="fr"><div class="in"><span data-g="5.1" data-fx="type">hzklink</span></div><div class="ap">Appliquer</div></div>
    <div class="ok" data-g="5.3" data-fx="stamp"><span>✓ Code appliqué</span><span>-14 %</span></div></div>
   <div class="chip" style="top:900px" data-g="5.3" data-fx="up">54,00 € → 46,44 € · PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(215, [('h1', 'CODE PROMO', '6.0', 'font-size:70px'), ('big gold', 'hzklink', '6.0', 'font-size:140px'), ('it vi', '-14 % avec le code hzklink', '6.1', 'font-size:58px')]) + '''
   <div class="pill" style="top:720px;border-color:rgba(176,124,255,.85)" data-g="6.0" data-fx="up"><div class="pin" style="background:#b07cff;color:#07040c">?</div><div><b style="color:#eadcff">ÉCRIS TA RÉPONSE EN COMMENTAIRE</b><span>et enregistre la vidéo</span></div></div>
   <div class="chip" style="top:870px" data-g="6.3" data-fx="up">LIENS DES ARTICLES TENDANCE EN BIO</div>
   <div class="cond" style="top:1010px">Prix d'exemple · -14 % avec le code promo hzklink<br>Offre soumise aux conditions en vigueur</div></div>
'''
