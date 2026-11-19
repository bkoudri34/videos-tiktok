import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from tuto import *
from hacoo_items import icon
# Hacoo n°1 du 19/11/2026 - style T « Tuto illustré » (brief veille du 19/11, vidéo 1). Format F2 démystification + calcul montré :
# bonhomme perplexe « -14 % ?? » -> panier dessiné 45,00 € entouré -> ardoise 10 % = 4,50 / + 4 % = 1,80 -> 6,30 € surligné
# -> total barré 45,00 € -> 38,70 € (ralenti) -> checklist « avant de payer » 3 cases -> écran de fin.
# Prix d'exemple : survêt 29 € + bonnet 8 € + écharpe 8 € = 45,00 € ; -14 % = 6,30 € ; total 38,70 €.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08 ; « Hacou » pour Hacoo, « H Z K link » pour hzklink.
NAME = 'hacoo33'
TITLE = 'Hacoo tuto ardoise calcul'
LINES = [
 ("Code promo Hacou : moins quatorze pour cent, ça fait combien, vraiment ?", [("<em>Code promo Hacoo</em> :", None), ("<i>-14 %</i>,", None), ("ça fait combien,", None), ("vraiment ?", None)]),
 ("Prends ce panier sur l'appli Hacou : quarante-cinq euros.", [("Prends ce panier", None), ("sur l'appli <em>Hacoo</em> :", None), ("<i>45 €</i>.", None)]),
 ("Dix pour cent, quatre euros cinquante. Plus quatre pour cent, un euro quatre-vingts.", [("10 %,", None), ("<em>4,50 €</em>.", None), ("Plus 4 %,", None), ("<em>1,80 €</em>.", None)]),
 ("Ça fait six euros trente en moins.", [("Ça fait", None), ("<em>6,30 €</em> en moins.", None)]),
 ("Tu paies trente-huit euros soixante-dix au lieu de quarante-cinq. Prix d'exemple.", [("Tu paies", None), ("<em>38,70 €</em>", None), ("au lieu de 45.", None), ("Prix d'exemple.", None)]),
 ("Avant de payer : la case code promo, H Z K link, et tu vérifies le total.", [("Avant de payer :", None), ("la case <em>code promo</em>,", None), ("<em>hzklink</em>,", None), ("et tu vérifies <i>le total</i>.", None)]),
 ("Envoie ça à ton pote qui ne compte jamais. Code promo Hacou, H Z K link.", [("Envoie ça à ton pote", None), ("qui ne compte jamais.", None), ("<em>Code promo Hacoo</em>", None), ("<em>hzklink</em>.", None)]),
]
SPLITS = [(0.0, 2.75), (3.10, 5.16), (5.50, 8.76), (9.11, 10.19), (10.51, 13.54), (14.0, 17.62), (18.04, 21.65)]
GSTART = [[0.0, 1.0, 2.1, 2.6], [3.10, 3.7, 4.5], [5.50, 6.2, 7.3, 8.1], [9.11, 9.4], [10.51, 10.7, 12.0, 13.1], [14.0, 14.9, 15.8, 16.7], [18.04, 18.8, 20.0, 21.0]]

CSS = '''
.cart{left:140px;top:560px;width:800px;padding:30px 40px 34px}
.cart .h{font:900 46px Inter;margin-bottom:10px}
.cart .row{height:104px}
.cart .tot{display:flex;justify-content:space-between;margin-top:14px;padding-top:16px;border-top:4px dashed #111;font:900 56px Inter;white-space:nowrap}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:700 30px 'Comic Relief',cursive;color:#555}
.slate{position:absolute;left:110px;top:560px;width:860px;height:600px;border-radius:26px;background:#25352b;border:18px solid #8a6a43;box-shadow:10px 12px 0 #111;padding:50px 50px;color:#f4f1e8}
.slate .l{font:700 74px 'Comic Relief',cursive;white-space:nowrap;line-height:1.5}
.slate .l b{color:#ffe14d}
.slate .r{position:absolute;left:50px;bottom:40px;font:700 70px 'Comic Relief',cursive;white-space:nowrap}
.slate .r span{background:#ffe14d;color:#111;padding:0 18px;border-radius:10px}
.big2{position:absolute;left:0;top:640px;width:1080px;text-align:center}
.big2 .o{display:inline-block;position:relative;font:900 100px Inter;color:#777}
.big2 .n{font:900 200px Inter;line-height:1.1;margin-top:20px}
.big2 .n span{background:#ffe14d;padding:0 24px}
.chk{position:absolute;left:120px;top:560px;width:840px}
.chk .r{height:180px;display:flex;align-items:center;gap:34px;font:900 50px Inter;white-space:nowrap;border-bottom:5px dashed #111}
.chk .bx{flex:none;width:100px;height:100px;border:7px solid #111;border-radius:16px;background:#fff;position:relative}
.chk .bx svg{position:absolute;left:-6px;top:-22px}
.chk .r .hl{font-family:'DejaVu Sans Mono',monospace}
'''
ITEMS = [('Survêt', 'Survêt', '29,00 €'), ('Bonnet', 'Bonnet', '8,00 €'), ('Écharpe', 'Écharpe', '8,00 €')]
TICK = '<path class="dr" pathLength="1" d="M10 70 L50 110 L130 10"/>'


def cart():
    rows = ''.join(f'<div class="row"><span class="ico">{icon(ic, 88)}</span>{lab}<span class="p">{pr}</span></div>' for ic, lab, pr in ITEMS)
    return f'<div class="paper cart"><div class="h">Mon panier Hacoo</div>{rows}<div class="tot"><span>Total</span><span>45,00 €</span></div></div>'


def chk(txt, g):
    return f'<div class="r"><div class="bx">' + svg(-6, -22, 140, 120, TICK.replace('class="dr"', f'class="dr" data-g="{g}" data-fx="draw"'), 'red') + f'</div>{txt}</div>'


BODY = '''
  <div class="scene" data-s="0">''' + title('<mark>Code promo Hacoo</mark> :<br>-14 %, ça fait<br><em>combien vraiment ?</em>') + svg(150, 660, 260, 470, GUY) + '''
   <div class="note" style="left:470px;top:700px;font-size:110px;transform:rotate(-8deg)">-14 % ??</div>
   <div class="note" style="left:520px;top:900px;transform:rotate(4deg)" data-g="0.2" data-fx="pop">sur 45 € ?</div>
   <div class="ex" style="top:1200px">prix d'exemple</div></div>
  <div class="scene" data-s="1" data-in="up">''' + title('Le panier', 220, size=90) + cart() + circle(560, 1000, 400, 150, '1.2') + '''
   <div class="ex" style="top:400px">prix d'exemple</div></div>
  <div class="scene" data-s="2" data-in="right">''' + title('Le calcul', 220, size=90) + '''
   <div class="slate"><div class="l" data-g="2.0" data-fx="fade">10 % de 45 = <b>4,50</b></div><div class="l" data-g="2.2" data-fx="fade">+ 4 % = <b>1,80</b></div>
    <div class="r" data-g="2.3" data-fx="fade">= ?</div></div>''' + underline2(650, 728, 210, '2.1') + '''</div>
  <div class="scene" data-s="3" data-in="pop">''' + title('Le calcul', 220, size=90) + '''
   <div class="slate"><div class="l">10 % de 45 = <b>4,50</b></div><div class="l">+ 4 % = <b>1,80</b></div>
    <div class="r" data-g="3.1" data-fx="stamp">= <span>6,30 €</span> en moins</div></div></div>
  <div class="scene" data-s="4" data-in="pop">''' + title('Ce que tu paies', 220, size=86) + '''
   <div class="big2"><div class="o">45,00 €''' + svg(-20, 40, 500, 40, '<path class="dr" pathLength="1" d="M0 30 L480 6" data-g="4.0" data-fx="draw"/>', 'red') + '''</div>
    <div class="n" data-g="4.1" data-fx="stamp" data-slow="4.1"><span>38,70 €</span></div></div>
   <div class="note" style="left:620px;top:1080px;transform:rotate(-4deg)" data-g="4.2" data-fx="pop">← ça, tu paies</div>
   <div class="ex" style="top:1220px" data-g="4.3" data-fx="fade">prix d'exemple · code promo Hacoo hzklink</div></div>
  <div class="scene" data-s="5" data-in="right">''' + title('Avant de payer', 220, size=86) + '''
   <div class="chk">''' + chk('case code promo Hacoo', '5.1') + chk('tape <span class="hl">hzklink</span>', '5.2') + chk('vérifie le <em style="font-style:normal;color:#e63946">TOTAL</em>', '5.3') + '''</div></div>
  <div class="scene" data-s="6" data-in="pop">
   <div class="endw" data-g="6.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div>
    <div class="b">liens des articles tendance en bio</div><div class="x">Prix d'exemple · -14 % avec le code promo Hacoo hzklink · Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
   <div class="note" style="left:200px;top:960px;transform:rotate(-3deg)" data-g="6.0" data-fx="pop">envoie-la à ton pote<br>qui ne compte jamais</div></div>
'''
