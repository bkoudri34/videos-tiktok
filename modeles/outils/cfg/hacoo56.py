import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from tuto import *
from hacoo_items import icon
# Hacoo n°2 du 25/11/2026 - style T tuto illustré, accent orange brique (brief veille du 25/11). Format F6/F7 carte au trésor
# « Où se cache la case code promo Hacoo ? » : carte au trésor dessinée + X rouge + bonhomme à la loupe dès la 1re image
# -> île 1 le panier (Commander) -> île 2 la page de commande (« avant Payer ! ») -> le X = la case code promo Hacoo, hzklink + Appliquer
# -> coffre « -11,06 € » -> 67,94 € (ralenti) -> fin « envoie à ton pote ». Pas de sujet R.
# Prix d'exemple : baskets 54 € + sacoche 19 € + chaussettes 6 € = 79,00 € ; -14 % = 11,06 € ; total 67,94 €.
# Voix : Speko Etienne (cartesia sonic-3.5), speed 1.08, une synthèse, silences internes plafonnés à 0,16 s, atempo 1.16.
NAME = 'hacoo56'
TITLE = 'Hacoo carte au tresor brique'
LINES = [
 ("Où est la case code promo sur l'appli Hacou ? Elle n'est pas là où tu crois.", [("Où est la case <em>code promo</em>", None), ("sur l'appli <em>Hacoo</em> ?", None), ("Pas là où tu crois.", None)]),
 ("Étape un : ton panier. Tu appuies sur Commander.", [("<i>Étape 1 :</i> ton panier.", None), ("Appuie sur <em>Commander</em>.", None)]),
 ("Étape deux : la page de commande. Surtout, n'appuie pas encore sur Payer.", [("<i>Étape 2 :</i> la page", None), ("de commande.", None), ("Surtout, n'appuie pas", None), ("encore sur <i>Payer</i>.", None)]),
 ("Étape trois : la case code promo. Code promo Hacou, H, Z, K, link, et Appliquer.", [("<i>Étape 3 :</i> la case", None), ("<em>code promo</em>.", None), ("<em>Code promo Hacoo</em>,", None), ("<em>hzklink</em>,", None), ("et <em>Appliquer</em>.", None)]),
 ("Soixante-dix-neuf euros de baskets, sacoche et chaussettes : onze euros et six centimes de moins.", [("<em>79 €</em> de baskets,", None), ("sacoche et chaussettes :", None), ("<em>11,06 €</em> de moins.", None)]),
 ("Tu paies soixante-sept euros et quatre-vingt-quatorze centimes.", [("Tu paies", None), ("<em>67,94 €</em>.", None)]),
 ("Envoie cette vidéo à ton pote qui commande. Les liens sont dans ma bio.", [("Envoie cette vidéo", None), ("à ton pote qui commande.", None), ("Les liens sont dans ma bio.", None)]),
]
SPLITS = [(0.172, 3.596), (4.046, 6.77), (7.22, 11.118), (11.568, 18.354), (18.804, 23.14), (23.59, 25.997), (26.447, 29.436)]
MINLEN = 1.8
GAP = 0.2
TAIL = 2.0

CSS = '''
#bgtex{background:linear-gradient(rgba(150,90,40,.08) 2px,transparent 2px) 0 0/100% 64px,#fbf6ec !important}
.ttl em{color:#c4501f}
.map{position:absolute;left:110px;width:860px;height:640px;border:7px solid #111;border-radius:30px;background:#f3e3c3;box-shadow:10px 12px 0 #111;overflow:hidden}
.isl{position:absolute;border:6px solid #111;border-radius:48% 52% 45% 55%;background:#d9c08a;display:flex;align-items:center;justify-content:center;font:900 34px Inter;color:#111;white-space:nowrap;text-align:center;line-height:1.1}
.xx{position:absolute;font:900 150px Inter;color:#e63946;line-height:1}
.pap{position:absolute;left:190px;width:700px;padding:34px 40px;background:#fff;border:6px solid #111;border-radius:28px;box-shadow:10px 12px 0 #c4501f}
.pap .t{font:900 38px Inter;margin-bottom:10px}
.pap .r{display:flex;align-items:center;gap:20px;font:800 34px Inter;white-space:nowrap;margin-top:8px}
.pap .r b{margin-left:auto;font:900 38px Inter}
.pap .tot{display:flex;justify-content:space-between;font:900 40px Inter;margin-top:16px;border-top:4px dashed #bbb;padding-top:14px;white-space:nowrap}
.pap .bt{margin-top:24px;height:90px;border-radius:45px;background:#c4501f;color:#fff;font:900 38px Inter;display:flex;align-items:center;justify-content:center;letter-spacing:2px;border:5px solid #111}
.pap .ln{display:flex;justify-content:space-between;font:800 34px Inter;padding:18px 0;border-bottom:3px solid #eee;white-space:nowrap}
.pap .cp{display:flex;justify-content:space-between;font:900 34px Inter;padding:18px 16px;margin-top:8px;border:5px dashed #c4501f;border-radius:18px;color:#c4501f;white-space:nowrap}
.pap .pay{margin-top:24px;height:90px;border-radius:45px;background:#111;color:#fff;font:900 38px Inter;display:flex;align-items:center;justify-content:center;letter-spacing:2px}
.fld{position:absolute;left:150px;width:780px;padding:34px 40px;background:#fff;border:6px solid #111;border-radius:28px;box-shadow:10px 12px 0 #c4501f}
.fld .k{font:900 36px Inter;letter-spacing:2px;color:#c4501f;margin-bottom:16px}
.fld .fr{display:flex;gap:16px}.fld .fr .field{flex:1}
.fld .ap{height:100px;padding:0 26px;border-radius:18px;background:#c4501f;color:#fff;font:900 34px Inter;display:flex;align-items:center;border:5px solid #111}
.fld .ok{margin-top:20px;font:900 40px Inter;color:#c4501f;display:flex;justify-content:space-between;white-space:nowrap}
.chest{position:absolute;left:340px;width:400px;height:250px}
.loot{position:absolute;left:0;width:1080px;text-align:center}
.loot span{display:inline-block;padding:10px 40px;border:7px solid #111;border-radius:24px;background:#ffe14d;font:900 110px Inter;box-shadow:8px 10px 0 #111;white-space:nowrap}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:700 32px 'Comic Relief',cursive;color:#555}
.big2{position:absolute;left:0;top:520px;width:1080px;text-align:center}
.big2 .o{display:inline-block;position:relative;font:900 110px Inter;color:#777}
.big2 .n{font:900 190px Inter;line-height:1.1;margin-top:20px}
.big2 .n span{background:#ffe14d;padding:0 24px}
.pin{position:absolute;left:150px;width:780px;height:120px;border-radius:60px;background:#c4501f;color:#fff;display:flex;align-items:center;justify-content:center;gap:18px;font:900 31px Inter;white-space:nowrap;box-shadow:8px 10px 0 #111}
'''

LOUPE = '''<g class="ink"><circle cx="120" cy="80" r="56"/><path d="M98 72 l0 6 M142 72 l0 6"/><path d="M104 110 Q120 104 136 110"/>
 <path d="M120 136 L120 320"/><path d="M120 320 L75 440 M120 320 L165 440"/><path d="M120 190 L50 260"/><path d="M120 190 L210 150"/>
 <circle cx="250" cy="120" r="46" style="fill:rgba(255,255,255,.6)"/><path d="M216 152 L200 172"/></g>'''


def tmap(top, x_g=None):
    a = f' data-g="{x_g}" data-fx="stamp"' if x_g else ''
    path = svg(0, 0, 860, 640, '<path d="M150 470 C260 420 300 300 400 330 C500 360 520 200 640 180" style="stroke-dasharray:4 26;stroke-width:12"/>', 'red')
    return (f'<div class="map" style="top:{top}px">{path}'
            '<div class="isl" style="left:60px;top:420px;width:220px;height:150px">1<br>PANIER</div>'
            '<div class="isl" style="left:300px;top:250px;width:230px;height:150px">2<br>COMMANDE</div>'
            f'<div class="xx" style="left:600px;top:90px"{a}>✕</div>'
            '<div class="note" style="left:560px;top:250px;transform:rotate(-6deg)">la case !</div></div>')


ITEMS = [('Baskets', 'Baskets', 54), ('Sacoche', 'Sacoche', 19), ('Chaussettes', 'Chaussettes', 6)]

BODY = '''
  <div class="scene" data-s="0">''' + title('Où se cache la case<br><mark>code promo Hacoo</mark> ?', 220, size=68) + tmap(470) + svg(700, 820, 300, 440, LOUPE) + '''
   <div class="ex" style="top:1150px">carte au trésor · prix d'exemple</div></div>
  <div class="scene" data-s="1" data-in="up">''' + title('1 · Ton <em>panier</em>', 240, size=80) + '''
   <div class="pap" style="top:420px"><div class="t">Mon panier Hacoo</div>''' + ''.join(
    f'<div class="r">{icon(n, 70)}<span>{lab}</span><b>{p},00 €</b></div>' for n, lab, p in ITEMS) + '''
    <div class="tot"><span>Total</span><span>79,00 €</span></div><div class="bt" data-g="1.1" data-fx="pop">COMMANDER</div></div>''' + circle(170, 940, 740, 170, '1.1') + '''
   <div class="note" style="left:640px;top:1130px;transform:rotate(-6deg)" data-g="1.1" data-fx="pop">appuie !</div></div>
  <div class="scene" data-s="2" data-in="right">''' + title('2 · La page de <em>commande</em>', 240, size=62) + '''
   <div class="pap" style="top:420px"><div class="t">Commande</div><div class="ln"><span>Adresse</span><span>✓</span></div><div class="ln"><span>Livraison</span><span>✓</span></div>
    <div class="cp"><span>Code promo</span><span>›</span></div><div class="pay">PAYER</div></div>''' + svg(220, 900, 660, 120, '<path class="dr" pathLength="1" d="M10 10 L640 110 M640 10 L10 110" data-g="2.2" data-fx="draw"/>', 'red') + '''
   <div class="note" style="left:560px;top:1060px;transform:rotate(-5deg)" data-g="2.2" data-fx="pop">avant Payer !</div></div>
  <div class="scene" data-s="3" data-in="left">''' + title('3 · ✕ = la case <em>code promo</em>', 240, size=58) + '''
   <div class="fld" style="top:440px"><div class="k">CODE PROMO HACOO</div><div class="fr"><div class="field"><span data-g="3.3" data-fx="type">hzklink</span></div><div class="ap">Appliquer</div></div>
    <div class="ok" data-g="3.4" data-fx="stamp"><span>✓ Appliqué</span><span>-14 %</span></div></div>
   <div class="xx" style="left:820px;top:330px;font-size:110px" data-g="3.0" data-fx="stamp">✕</div>''' + circle(95, 390, 890, 430, '3.4') + '''
   <div class="note" style="left:160px;top:830px;transform:rotate(-4deg)" data-g="3.2" data-fx="pop">code promo Hacoo</div></div>
  <div class="scene" data-s="4" data-in="up">''' + title('Le trésor', 220, size=84) + '''
   <div class="its" style="position:absolute;left:150px;top:360px;width:780px;display:flex;justify-content:space-between">''' + ''.join(
    f'<div style="width:240px;text-align:center;font:800 32px Inter;white-space:nowrap" data-g="4.{min(k, 1)}" data-fx="pop">{icon(n, 150)}<br>{lab}<b style="display:block;font:900 44px Inter">{p} €</b></div>' for k, (n, lab, p) in enumerate(ITEMS)) + '''</div>
   ''' + svg(340, 680, 400, 250, '<rect x="20" y="90" width="360" height="150" rx="14" style="fill:#c98a4b"/><path d="M20 90 Q200 0 380 90" style="fill:#a86a33"/><path d="M20 150 L380 150 M200 90 L200 240"/>') + '''
   <div class="loot" style="top:960px" data-g="4.2" data-fx="stamp"><span>-11,06 €</span></div>
   <div class="ex" style="top:1150px">79,00 € × 14 % = 11,06 € · prix d'exemple</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + title('Tu paies', 220, size=90) + '''
   <div class="big2"><div class="o">79,00 €''' + svg(-20, 40, 500, 40, '<path class="dr" pathLength="1" d="M0 30 L480 6" data-g="5.0" data-fx="draw"/>', 'red') + '''</div>
    <div class="n" data-g="5.1" data-fx="stamp" data-slow="5.1"><span>67,94 €</span></div></div>''' + circle(150, 680, 780, 320, '5.1') + '''
   <div class="ex" style="top:1060px" data-g="5.1" data-fx="fade">prix d'exemple · code promo Hacoo hzklink (-14 %)</div></div>
  <div class="scene" data-s="6" data-in="pop">
   <div class="endw" data-g="6.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div>
    <div class="b">liens des articles tendance en bio</div><div class="x">Prix d'exemple · -14 % avec le code promo Hacoo hzklink · Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
   <div class="pin" style="top:1000px" data-g="6.1" data-fx="pop">↗ ENVOIE-LA À TON POTE QUI COMMANDE</div>
   </div>
'''
