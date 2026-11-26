import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from tuto import *
from hacoo_items import icon
# 4e vidéo Hacoo du 26/11/2026 - style T tuto illustré, accent vert sapin. Format liste de Noël « 4 cadeaux de Noël à moins de 15 € » :
# liste dessinée (maman / papa / frangin / pote) dès la 1re image -> bougie 11 € + gants 9 € -> casquette 13 € + mug 8 €
# -> total 41,00 € et case code promo avant Payer -> hzklink -14 % = -5,74 € -> 35,26 € (ralenti) -> fin « envoie-la ». Pas de sujet R.
# Prix d'exemple : 41,00 x 0,14 = 5,74 ; 41,00 x 0,86 = 35,26.
# RÈGLE DU 26/11 : le nom de l'appli n'est JAMAIS écrit (ni à l'image ni dans les sous-titres), seulement dit à l'oral.
# Voix : Speko Leo (xai), speed 1.08, une synthèse par réplique, silences internes plafonnés à 0,16 s, atempo 1.1, -19 dB moyen.
NAME = 'hacoo62'
TITLE = 'Liste de Noel sapin'
LINES = [
 ("Sur l'appli Hacou, quatre cadeaux de Noël à moins de quinze euros.", [("Sur l'appli,", None), ("<em>4 cadeaux</em> de Noël", None), ("à moins de <em>15&nbsp;€.</em>", None)]),
 ("Pour maman, une bougie : onze euros. Pour papa, des gants : neuf euros.", [("Pour maman,", None), ("une bougie : <em>11&nbsp;€.</em>", None), ("Pour papa,", None), ("des gants : <em>9&nbsp;€.</em>", None)]),
 ("Pour le frangin, une casquette : treize euros. Et pour ton pote, un mug : huit euros.", [("Pour le frangin,", None), ("une casquette : <em>13&nbsp;€.</em>", None), ("Et pour ton pote,", None), ("un mug : <em>8&nbsp;€.</em>", None)]),
 ("Total : quarante et un euros. Mais avant de payer, il y a la case code promo.", [("Total : <em>41&nbsp;€.</em>", None), ("Mais avant de payer,", None), ("la case <i>code promo</i>.", None)]),
 ("Code promo Hacou : H, Z, K, link. Moins quatorze pour cent, soit cinq euros soixante-quatorze de moins.", [("<em>Code promo :</em>", None), ("<em>hzklink.</em>", None), ("<i>-14&nbsp;%</i>, soit", None), ("<em>5,74&nbsp;€</em> de moins.", None)]),
 ("Tu paies trente-cinq euros et vingt-six centimes pour quatre cadeaux.", [("Tu paies", None), ("<em>35,26&nbsp;€</em>", None), ("pour 4 cadeaux.", None)]),
 ("Envoie cette vidéo à celui qui n'a pas encore fait ses cadeaux. Les liens sont dans ma bio.", [("Envoie cette vidéo", None), ("à celui qui n'a pas", None), ("fait ses cadeaux.", None), ("Les liens sont dans ma bio.", None)]),
]
SPLITS = [(0.2, 3.316), (3.766, 7.584), (8.034, 12.439), (12.889, 17.191), (17.641, 23.357), (23.807, 26.619), (27.069, 30.85)]
MINLEN = 1.8
GAP = 0.2
TAIL = 2.2

G = '#1f7a4a'
CSS = '''
#bgtex{background:linear-gradient(rgba(31,122,74,.08) 2px,transparent 2px) 0 0/100% 64px,#f8f7f1 !important}
.ttl em{color:#1f7a4a}
.lst{position:absolute;left:150px;width:780px;padding:30px 44px;background:#fff;border:6px solid #111;border-radius:28px;box-shadow:10px 12px 0 #1f7a4a;transform:rotate(-1.5deg)}
.lst .t{font:700 54px 'Comic Relief',cursive;color:#1f7a4a;margin-bottom:6px}
.lst .r{display:flex;align-items:center;gap:22px;font:800 46px Inter;padding:14px 0;border-bottom:3px dashed #ccc;white-space:nowrap}
.lst .r:last-child{border-bottom:0}
.lst .bx{width:54px;height:54px;border:5px solid #111;border-radius:10px;display:flex;align-items:center;justify-content:center;font:900 44px Inter;color:#1f7a4a}
.lst .r b{margin-left:auto;font:900 46px Inter;color:#999}
.gift{position:absolute;width:400px;text-align:center}
.gift .who{display:inline-block;font:700 52px 'Comic Relief',cursive;color:#1f7a4a;transform:rotate(-3deg)}
.gift .card{margin-top:14px;padding:24px 10px 20px;background:#fff;border:6px solid #111;border-radius:28px;box-shadow:8px 10px 0 #1f7a4a}
.gift .nm{font:800 40px Inter;white-space:nowrap;margin-top:6px}
.gift .pt{display:inline-block;margin-top:10px;padding:4px 26px;border:5px solid #111;border-radius:18px;background:#ffe14d;font:900 62px Inter;white-space:nowrap}
.pap{position:absolute;left:170px;width:740px;padding:30px 40px;background:#fff;border:6px solid #111;border-radius:28px;box-shadow:10px 12px 0 #1f7a4a}
.pap .t{font:900 38px Inter;margin-bottom:6px}
.pap .r{display:flex;align-items:center;gap:18px;font:800 32px Inter;white-space:nowrap;margin-top:4px}
.pap .r b{margin-left:auto;font:900 36px Inter}
.pap .tot{display:flex;justify-content:space-between;font:900 40px Inter;margin-top:12px;border-top:4px dashed #bbb;padding-top:12px;white-space:nowrap}
.pap .cp{display:flex;justify-content:space-between;font:900 34px Inter;padding:16px 16px;margin-top:14px;border:5px dashed #1f7a4a;border-radius:18px;color:#1f7a4a;white-space:nowrap}
.pap .pay{margin-top:18px;height:84px;border-radius:42px;background:#111;color:#fff;font:900 36px Inter;display:flex;align-items:center;justify-content:center;letter-spacing:2px}
.fld{position:absolute;left:150px;width:780px;padding:34px 40px;background:#fff;border:6px solid #111;border-radius:28px;box-shadow:10px 12px 0 #1f7a4a}
.fld .k{font:900 36px Inter;letter-spacing:2px;color:#1f7a4a;margin-bottom:16px}
.fld .fr{display:flex;gap:16px}.fld .fr .field{flex:1}
.fld .ap{height:100px;padding:0 26px;border-radius:18px;background:#1f7a4a;color:#fff;font:900 34px Inter;display:flex;align-items:center;border:5px solid #111}
.fld .ok{margin-top:20px;font:900 40px Inter;color:#1f7a4a;display:flex;justify-content:space-between;white-space:nowrap}
.loot{position:absolute;left:0;width:1080px;text-align:center}
.loot span{display:inline-block;padding:10px 40px;border:7px solid #111;border-radius:24px;background:#ffe14d;font:900 110px Inter;box-shadow:8px 10px 0 #111;white-space:nowrap}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:700 32px 'Comic Relief',cursive;color:#555}
.big2{position:absolute;left:0;top:480px;width:1080px;text-align:center}
.big2 .o{display:inline-block;position:relative;font:900 110px Inter;color:#777}
.big2 .n{font:900 190px Inter;line-height:1.1;margin-top:20px}
.big2 .n span{background:#ffe14d;padding:0 24px}
.pin{position:absolute;left:120px;width:840px;height:120px;border-radius:60px;background:#1f7a4a;color:#fff;display:flex;align-items:center;justify-content:center;gap:18px;font:900 31px Inter;white-space:nowrap;box-shadow:8px 10px 0 #111}
'''

GIFTS = [('Maman', 'Bougie', 'Une bougie', 11), ('Papa', 'Gants', 'Des gants', 9), ('Frangin', 'Casquette', 'Une casquette', 13), ('Pote', 'Mug', 'Un mug', 8)]


def gift(x, top, who, n, lab, p, g):
    return (f'<div class="gift" style="left:{x}px;top:{top}px" data-g="{g}" data-fx="pop"><div class="who">pour {who.lower()}</div>'
            f'<div class="card">{icon(n, 200)}<div class="nm">{lab}</div><div class="pt">{p} €</div></div></div>')


BODY = '''
  <div class="scene" data-s="0">''' + title('4 cadeaux de Noël<br><mark>à moins de 15 €</mark>', 220, size=72) + '''
   <div class="lst" style="top:470px"><div class="t">Ma liste de Noël</div>''' + ''.join(
    f'<div class="r"><div class="bx"></div><span>{w}</span><b>? €</b></div>' for w, _, _, _ in GIFTS) + '''</div>
   <div class="ex" style="top:1180px">liste de Noël · prix d'exemple</div></div>
  <div class="scene" data-s="1" data-in="up">''' + title('Maman <em>&amp;</em> papa', 230, size=80) + gift(100, 400, *GIFTS[0], '1.1') + gift(580, 400, *GIFTS[1], '1.3') + '''
   <div class="note" style="left:180px;top:1040px;transform:rotate(-4deg)" data-g="1.1" data-fx="pop">✓ maman</div><div class="note" style="left:660px;top:1040px;transform:rotate(-4deg)" data-g="1.3" data-fx="pop">✓ papa</div></div>
  <div class="scene" data-s="2" data-in="right">''' + title('Frangin <em>&amp;</em> pote', 230, size=80) + gift(100, 400, *GIFTS[2], '2.1') + gift(580, 400, *GIFTS[3], '2.3') + '''
   <div class="note" style="left:160px;top:1040px;transform:rotate(-4deg)" data-g="2.1" data-fx="pop">✓ frangin</div><div class="note" style="left:680px;top:1040px;transform:rotate(-4deg)" data-g="2.3" data-fx="pop">✓ pote</div></div>
  <div class="scene" data-s="3" data-in="left">''' + title('Total : <em>41 €</em>', 230, size=84) + '''
   <div class="pap" style="top:380px"><div class="t">Commande</div>''' + ''.join(
    f'<div class="r">{icon(n, 56)}<span>{lab}</span><b>{p},00 €</b></div>' for _, n, lab, p in GIFTS) + '''
    <div class="tot"><span>Total</span><span>41,00 €</span></div><div class="cp" data-g="3.2" data-fx="pop"><span>Code promo</span><span>›</span></div><div class="pay">PAYER</div></div>''' + '''
   <div class="note" style="left:600px;top:1180px;transform:rotate(-5deg)" data-g="3.1" data-fx="pop">avant Payer !</div></div>
  <div class="scene" data-s="4" data-in="up">''' + title('La case <em>code promo</em>', 230, size=70) + '''
   <div class="fld" style="top:400px"><div class="k">CODE PROMO</div><div class="fr"><div class="field"><span data-g="4.1" data-fx="type">hzklink</span></div><div class="ap">Appliquer</div></div>
    <div class="ok" data-g="4.2" data-fx="stamp"><span>✓ Appliqué</span><span>-14 %</span></div></div>
   <div class="loot" style="top:830px" data-g="4.3" data-fx="stamp"><span>-5,74 €</span></div>
   <div class="ex" style="top:1060px" data-g="4.3" data-fx="fade">41,00 € × 14 % = 5,74 € · prix d'exemple</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + title('Tu paies', 220, size=90) + '''
   <div class="big2"><div class="o">41,00 €''' + svg(-20, 40, 500, 40, '<path class="dr" pathLength="1" d="M0 30 L480 6" data-g="5.0" data-fx="draw"/>', 'red') + '''</div>
    <div class="n" data-g="5.1" data-fx="stamp" data-slow="5.1"><span>35,26 €</span></div></div>''' + '''
   <div class="ex" style="top:1030px" data-g="5.2" data-fx="fade">4 cadeaux · prix d'exemple · code promo hzklink (-14 %)</div></div>
  <div class="scene" data-s="6" data-in="pop">
   <div class="endw" data-g="6.0" data-fx="up"><div class="k">CODE PROMO</div><div class="c">hzklink</div><div class="d">-14 % avec le code hzklink</div>
    <div class="b">liens des articles tendance en bio</div><div class="x">Prix d'exemple · -14 % avec le code promo hzklink · Offre soumise aux conditions en vigueur</div></div>
   <div class="pin" style="top:1000px" data-g="6.1" data-fx="pop">↗ ENVOIE-LA À CELUI QUI N'A PAS FINI SES CADEAUX</div>
   </div>
'''
