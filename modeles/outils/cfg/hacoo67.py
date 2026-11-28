import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from tuto import *
from hacoo_items import icon
# 1re vidéo Hacoo du 28/11/2026 - style T tuto illustré, accent bleu encre. Sujet R (retours) « Avant de valider ta taille, regarde ça »
# (brief veille du 28/11) : téléphone « Ma commande » S/M/L dès la 1re image -> « la lettre ne suffit pas » (M barré)
# -> ① mesure à plat (pull au trait, flèches épaules / poitrine / longueur) -> ② guide des tailles en cm (valeurs d'exemple, ligne entourée)
# -> ③ avis avec photos + encart « trop petit ? revends-le en seconde main » -> panier doudoune 46 € + pyjama 22 € = 68,00 €,
# code promo -9,52 € -> 58,48 € (ralenti) -> fin « ENREGISTRE AVANT TA PROCHAINE COMMANDE ».
# Prix d'exemple : 68,00 x 0,14 = 9,52 ; 68,00 x 0,86 = 58,48.
# RÈGLE DU 26/11 : le nom de l'appli n'est JAMAIS écrit (ni à l'image ni dans les sous-titres), seulement dit à l'oral.
# Voix : Speko Leo (xai), speed 1.08, une synthèse par réplique, silences internes plafonnés à 0,12 s, atempo 1.25, -19 dB moyen ;
# réplique 3 refaite (« pose à plat » compris « pause à plein » -> « mesure à plat »), répliques 3, 6, 7 raccourcies (durée).
NAME = 'hacoo67'
TITLE = 'Tailles tuto bleu encre'
LINES = [
 ("Tu commandes des vêtements sur l'appli Hacou ? Avant de choisir ta taille, regarde ça.", [("Tu commandes des vêtements", None), ("sur l'appli ?", None), ("Avant de choisir ta taille,", None), ("<em>regarde&nbsp;ça.</em>", None)]),
 ("La lettre ne suffit pas : un M peut changer d'une boutique à l'autre.", [("La lettre", None), ("<em>ne suffit pas :</em>", None), ("un M peut changer", None), ("d'une boutique à l'autre.", None)]),
 ("Un : mesure à plat un vêtement qui te va bien : les épaules, la poitrine, la longueur.", [("1 : mesure à plat", None), ("un vêtement qui te va bien :", None), ("les épaules, la poitrine,", None), ("<em>la longueur.</em>", None)]),
 ("Deux : compare avec le guide des tailles en centimètres. Tu hésites ? Prends la plus grande.", [("2 : compare avec", None), ("le guide des tailles", None), ("en <em>centimètres.</em>", None), ("Tu hésites ?", None), ("Prends <em>la plus grande.</em>", None)]),
 ("Trois : regarde les avis avec photos. Trop petit quand même ? Ne demande pas de remboursement, revends-le en seconde main.", [("3 : regarde les avis", None), ("<em>avec photos.</em>", None), ("Trop petit quand même ?", None), ("Ne demande pas", None), ("de remboursement,", None), ("<i>revends-le</i> en seconde main.", None)]),
 ("Code promo Hacou : H, Z, K, link. Cinquante-huit euros et quarante-huit centimes au lieu de soixante-huit.", [("<em>Code promo :</em>", None), ("<i>hzklink.</i>", None), ("<em>58,48&nbsp;€</em>", None), ("au lieu de 68&nbsp;€.", None)]),
 ("Enregistre avant ta prochaine commande. Code promo Hacou, H, Z, K, link.", [("Enregistre avant", None), ("ta prochaine commande.", None), ("Code promo", None), ("<i>hzklink.</i>", None)]),
]
SPLITS = [(0.2, 3.315), (3.515, 6.191), (6.391, 10.334), (10.534, 14.032), (14.232, 19.222), (19.422, 23.925), (24.125, 28.002)]
MINLEN = 1.8
GAP = 0.14
TAIL = 1.0

B = '#1d3f8f'
CSS = '''
#bgtex{background:linear-gradient(rgba(29,63,143,.09) 2px,transparent 2px) 0 0/100% 64px,#f8f8f4 !important}
.ttl em{color:#1d3f8f}
.ttl mark{background:#ffe14d}
.note.b{color:#1d3f8f}
.ph{position:absolute;width:470px;height:720px;border:7px solid #111;border-radius:56px;background:#fff;box-shadow:12px 14px 0 #1d3f8f}
.ph .hd2{margin:46px 0 0;text-align:center;font:900 36px Inter;color:#1d3f8f;letter-spacing:1px}
.ph .it{margin:30px auto 0;width:260px;height:260px;border:5px solid #111;border-radius:26px;display:flex;align-items:center;justify-content:center;background:#f2f4fb}
.ph .lb{margin-top:26px;text-align:center;font:800 28px Inter;color:#555}
.ph .sz{display:flex;justify-content:center;gap:18px;margin-top:16px}
.ph .sz b{width:82px;height:82px;border:5px solid #111;border-radius:18px;display:flex;align-items:center;justify-content:center;font:900 40px Inter;background:#fff}
.bub{position:absolute;background:#fff;border:6px solid #111;border-radius:40px;padding:18px 34px;font:900 52px Inter;white-space:nowrap;box-shadow:8px 8px 0 #1d3f8f}
.bigm{position:absolute;font:700 330px/1 'Comic Relief',cursive;color:#1d3f8f}
.shop{position:absolute;width:350px;padding:24px 20px;border:6px solid #111;border-radius:26px;background:#fff;text-align:center;box-shadow:8px 10px 0 #1d3f8f}
.shop .n{font:800 32px Inter;color:#555}
.shop .m{font:900 70px Inter;margin-top:4px}
.shop .c{font:900 46px Inter;color:#1d3f8f;margin-top:4px;white-space:nowrap}
.lbl{position:absolute;font:700 44px 'Comic Relief',cursive;color:#e63946;white-space:nowrap}
.tab{position:absolute;left:150px;width:780px;border:6px solid #111;border-radius:26px;background:#fff;box-shadow:10px 12px 0 #1d3f8f;overflow:hidden}
.tab .r{display:flex;font:800 54px Inter;border-top:4px solid #111;height:130px;align-items:center}
.tab .r:first-child{border-top:0;background:#1d3f8f;color:#fff;font:900 34px Inter;height:90px}
.tab .r span{flex:1;text-align:center;white-space:nowrap}
.tab .r span+span{border-left:4px solid #111;height:100%;display:flex;align-items:center;justify-content:center}
.tab .r:first-child span+span{border-left-color:#fff}
.rev{position:absolute;left:150px;width:780px;padding:26px 30px;border:6px solid #111;border-radius:26px;background:#fff;box-shadow:10px 12px 0 #1d3f8f}
.rev .st{font:900 52px Inter;color:#f2b705;letter-spacing:6px}
.rev .ph3{display:flex;gap:18px;margin-top:16px}
.rev .ph3 i{width:220px;height:200px;border:5px solid #111;border-radius:18px;background:#e8ecf7;display:flex;align-items:center;justify-content:center}
.rev .tx{margin-top:16px;font:700 34px 'Comic Relief',cursive;color:#333;white-space:nowrap}
.warn{position:absolute;left:150px;width:780px;padding:26px 32px;border:6px solid #111;border-radius:26px;background:#ffe14d;font:800 42px Inter;line-height:1.25;box-shadow:10px 12px 0 #111}
.warn small{display:block;margin-top:12px;font:600 28px Inter;color:#333}
.pap{position:absolute;left:150px;width:780px;padding:28px 40px;background:#fff;border:6px solid #111;border-radius:28px;box-shadow:10px 12px 0 #1d3f8f}
.pap .t{font:900 38px Inter;margin-bottom:6px}
.pap .r{display:flex;align-items:center;gap:18px;font:800 34px Inter;white-space:nowrap;margin-top:4px}
.pap .r b{margin-left:auto;font:900 36px Inter}
.pap .tot{display:flex;justify-content:space-between;font:900 40px Inter;margin-top:12px;border-top:4px dashed #bbb;padding-top:12px;white-space:nowrap}
.pap .k{margin-top:16px;font:900 30px Inter;letter-spacing:2px;color:#1d3f8f}
.pap .fr{display:flex;gap:16px;margin-top:8px}.pap .fr .field{flex:1;height:90px}
.pap .ap{height:90px;padding:0 24px;border-radius:18px;background:#1d3f8f;color:#fff;font:900 32px Inter;display:flex;align-items:center;border:5px solid #111}
.pap .ds{display:flex;justify-content:space-between;font:900 38px Inter;color:#e63946;margin-top:14px;white-space:nowrap}
.newt{position:absolute;left:0;width:1080px;text-align:center}
.newt span{display:inline-block;padding:6px 36px;border:7px solid #111;border-radius:24px;background:#ffe14d;font:900 120px Inter;box-shadow:8px 10px 0 #111;white-space:nowrap}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:700 32px 'Comic Relief',cursive;color:#555}
.endw .k2{font:900 46px/1.15 Inter;margin-bottom:12px;color:#1d3f8f}
.bm{position:absolute;left:470px;width:140px;height:170px}
'''

PULL = '''<g class="ink"><path d="M150 40 Q200 70 250 40 L330 70 L390 200 L340 225 L320 180 L320 400 L80 400 L80 180 L60 225 L10 200 L70 70 Z" style="fill:#e8ecf7"/>
 <path d="M150 40 Q200 95 250 40"/><path d="M80 370 H320"/></g>'''

BODY = '''
  <div class="scene" data-s="0">''' + title('Avant de valider ta taille,<br><mark>regarde ça</mark>', 220, size=70) + '''
   <div class="ph" style="left:90px;top:480px;transform:rotate(-3deg)"><div class="hd2">Ma commande</div><div class="it">''' + icon('Doudoune', 230) + '''</div>
    <div class="lb">Choisis ta taille</div><div class="sz"><b>S</b><b>M</b><b>L</b></div></div>
   ''' + svg(610, 700, 288, 564, GUY, 'ink', '0 0 240 470') + '''
   <div class="bub" style="left:590px;top:520px;transform:rotate(4deg)" data-g="0.2" data-fx="pop">S, M ou L ?</div></div>
  <div class="scene" data-s="1" data-in="right">''' + title('La lettre <em>ne suffit pas</em>', 230, size=64) + '''
   <div class="bigm" style="left:420px;top:380px">M</div>''' + svg(380, 430, 320, 300, '<path class="dr" pathLength="1" d="M10 20 L300 280" data-g="1.1" data-fx="draw"/><path class="dr" pathLength="1" d="M300 20 L10 280" data-g="1.1" data-fx="draw"/>', 'red') + '''
   <div class="shop" style="left:120px;top:820px;transform:rotate(-3deg)" data-g="1.2" data-fx="pop"><div class="n">boutique 1</div><div class="m">M</div><div class="c">53 cm</div></div>
   <div class="shop" style="left:570px;top:800px;transform:rotate(3deg)" data-g="1.3" data-fx="pop"><div class="n">boutique 2</div><div class="m">M</div><div class="c">49 cm</div></div>
   <div class="ex" style="top:1200px" data-g="1.3" data-fx="fade">demi-tour de poitrine · valeurs d'exemple</div></div>
  <div class="scene" data-s="2" data-in="up"><div class="num" style="left:70px;top:205px">1</div>''' + title('Mesure <em>à plat</em>', 225, size=76).replace('style="', 'style="left:200px;width:820px;text-align:left;', 1) + '<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;transform:scale(1.28);transform-origin:560px 420px">' + \
    svg(340, 470, 400, 400, PULL, 'ink', '0 0 400 400') + \
    arrow(380, 455, 320, 40, 'M0 20 L320 20 M0 20 l22 -16 M0 20 l22 16 M320 20 l-22 -16 M320 20 l-22 16', '2.2') + '<div class="lbl" style="left:440px;top:380px" data-g="2.2" data-fx="pop">épaules</div>' + \
    arrow(420, 700, 240, 40, 'M0 20 L240 20 M0 20 l22 -16 M0 20 l22 16 M240 20 l-22 -16 M240 20 l-22 16', '2.2') + '<div class="lbl" style="left:440px;top:735px" data-g="2.2" data-fx="pop">poitrine</div>' + \
    arrow(780, 520, 40, 350, 'M20 0 L20 350 M20 0 l-16 22 M20 0 l16 22 M20 350 l-16 -22 M20 350 l16 -22', '2.3') + '<div class="lbl" style="left:640px;top:900px;transform:rotate(-4deg)" data-g="2.3" data-fx="pop">longueur</div></div>' + '''
   <div class="note b" style="left:160px;top:1170px;transform:rotate(-3deg)" data-g="2.1" data-fx="pop">un vêtement qui te va bien</div></div>
  <div class="scene" data-s="3" data-in="left"><div class="num" style="left:70px;top:205px">2</div>''' + title('Le guide <em>en cm</em>', 225, size=76).replace('style="', 'style="left:200px;width:820px;text-align:left;', 1) + '''
   <div class="tab" style="top:420px" data-g="3.0" data-fx="up"><div class="r"><span>Taille</span><span>Poitrine (à plat)</span></div>
    <div class="r"><span>S</span><span>50 cm</span></div><div class="r"><span>M</span><span>53 cm</span></div><div class="r"><span>L</span><span>56 cm</span></div></div>''' + \
    circle(120, 640, 840, 150, '3.2') + '''
   <div class="ex" style="top:960px" data-g="3.1" data-fx="fade">guide des tailles · valeurs d'exemple</div>
   <div class="note" style="left:170px;top:1040px;transform:rotate(-3deg)" data-g="3.3" data-fx="pop">tu hésites ?</div>
   <div class="note b" style="left:200px;top:1120px;transform:rotate(-3deg);font-size:58px" data-g="3.4" data-fx="stamp">→ prends la plus grande</div></div>
  <div class="scene" data-s="4" data-in="up"><div class="num" style="left:70px;top:205px">3</div>''' + title('Les avis <em>avec photos</em>', 225, size=64).replace('style="', 'style="left:200px;width:820px;text-align:left;', 1) + '''
   <div class="rev" style="top:400px" data-g="4.0" data-fx="up"><div class="st">★★★★☆</div><div class="ph3"><i>''' + icon('Pyjama', 170) + '</i><i>' + icon('Doudoune', 170) + '''</i><i>''' + icon('Pyjama', 170) + '''</i></div>
    <div class="tx">« taille un peu petit, prenez au-dessus »</div></div>
   <div class="warn" style="top:960px" data-g="4.2" data-fx="pop">Trop petit quand même ?<br>→ revends-le en seconde main
    <small>Des utilisateurs racontent des comptes bloqués après des demandes de remboursement.</small></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + title('<em>Code promo</em>', 210, size=74) + '''
   <div class="pap" style="top:320px"><div class="t">Commande</div>
    <div class="r">''' + icon('Doudoune', 60) + '<span>Doudoune</span><b>46,00 €</b></div><div class="r">' + icon('Pyjama', 60) + '''<span>Pyjama</span><b>22,00 €</b></div>
    <div class="tot"><span>Sous-total</span><span>68,00 €</span></div>
    <div class="k">CODE PROMO</div><div class="fr"><div class="field"><span data-g="5.1" data-fx="type">hzklink</span></div><div class="ap">Appliquer</div></div>
    <div class="ds" data-g="5.2" data-fx="stamp"><span>Code promo -14 %</span><span>-9,52 €</span></div></div>
   <div class="newt" style="top:1000px" data-g="5.2" data-fx="stamp" data-slow="5.2"><span>58,48 €</span></div>
   <div class="ex" style="top:1200px" data-g="5.3" data-fx="fade">au lieu de 68,00 € · prix d'exemple</div></div>
  <div class="scene" data-s="6" data-in="pop">
   <div class="endw" data-g="6.0" data-fx="up"><div class="k2">ENREGISTRE AVANT TA<br>PROCHAINE COMMANDE</div><div class="k">CODE PROMO :</div><div class="c">hzklink</div><div class="d">-14 % avec le code hzklink</div>
    <div class="b">liens des articles tendance en bio</div><div class="x">Prix d'exemple · Offre soumise aux conditions en vigueur</div></div>
   ''' + svg(470, 1010, 140, 170, '<path d="M10 0 H130 V170 L70 120 L10 170 Z" style="fill:#1d3f8f;stroke:#111;stroke-width:6"/>', '', '0 0 140 170').replace('class="abs "', 'class="abs" data-g="6.1" data-fx="stamp"') + '''
  </div>
'''
