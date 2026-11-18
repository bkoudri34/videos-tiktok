import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from tuto import *
from hacoo_items import icon
# Hacoo n°2 du 18/11/2026 - style T « Tuto illustré » (1re vidéo de ce style, brief veille du 18/11) :
# papier blanc cassé, bonhomme au trait, main qui stoppe, panier dessiné, annotations au feutre rouge qui se tracent, surligneur jaune.
# Chaussettes de sport 8 € + gants de running 9 € + gourde 10 € = 27,00 € -> 23,22 € avec le code promo Hacoo hzklink
# (-14 % = -3,78 €), prix d'exemple. Interruption « Attends ! » -> case vide entourée -> 4 étapes numérotées -> nouvelle ligne -3,78 €
# soulignée deux fois -> total barré 27,00 € -> 23,22 € (ralenti) -> écran de fin blanc.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'hacoo32'
TITLE = 'Hacoo tuto illustre'
LINES = [
 ("Attends ! Avant de payer sur Hacou, regarde ta case code promo.", [("Attends !", None), ("Avant de payer sur <em>Hacoo</em>,", None), ("regarde ta case <em>code promo</em>.", None)]),
 ("Vide ? Alors tu paies trop.", [("<i>Vide ?</i>", None), ("Alors tu paies <em>trop</em>.", None)]),
 ("Un : ouvre ton panier. Deux : touche la case code promo Hacou.", [("<i>1 :</i> ouvre ton panier.", None), ("<i>2 :</i> touche la case <em>code promo Hacoo</em>.", None)]),
 ("Trois : tape H Z K link. Quatre : appuie sur appliquer.", [("<i>3 :</i> tape <em>hzklink</em>.", None), ("<i>4 :</i> appuie sur « Appliquer ».", None)]),
 ("Regarde cette nouvelle ligne : moins trois euros soixante-dix-huit.", [("Regarde cette nouvelle ligne :", None), ("<i>-3,78 €</i>", None)]),
 ("Vingt-trois euros vingt-deux au lieu de vingt-sept. Prix d'exemple.", [("<em>23,22 €</em>", None), ("au lieu de 27.", None), ("Prix d'exemple.", None)]),
 ("Code promo Hacou, H Z K link. Enregistre la vidéo pour ta prochaine commande.", [("<em>Code promo Hacoo</em>", None), ("<em>hzklink</em>.", None), ("Enregistre la vidéo", None), ("pour ta prochaine commande.", None)]),
]
SPLITS = [(0.0, 3.17), (3.72, 5.02), (5.63, 8.96), (9.45, 12.84), (13.47, 16.10), (16.51, 19.11), (19.58, 23.32)]
GSTART = [[0.0, 0.8, 2.0], [3.72, 4.3], [5.63, 7.24], [9.45, 11.55], [13.47, 14.76], [16.51, 17.5, 18.65], [19.58, 20.6, 21.7, 22.4]]

CSS = '''
.cart{left:140px;top:520px;width:800px;padding:30px 40px 34px}
.cart .h{font:900 46px Inter;margin-bottom:10px}
.cart .row{height:100px}
.cart .lab{margin-top:30px;font:800 30px Inter;letter-spacing:2px;color:#444}
.cart .fr{display:flex;gap:20px;margin-top:8px}
.cart .fr .field{flex:1}
.cart .disc{height:110px;align-items:flex-start;padding-top:22px;color:#e63946;font:900 42px Inter}
.cart .tot{display:flex;justify-content:space-between;margin-top:14px;padding-top:14px;border-top:4px dashed #111;font:900 50px Inter;white-space:nowrap}
.cart .tot s{color:#777;text-decoration-color:#e63946;text-decoration-thickness:5px;margin-right:16px;font-size:40px}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:700 30px 'Comic Relief',cursive;color:#555}
.payb{position:absolute;left:560px;top:820px;width:400px;height:150px;border-radius:75px;background:#111;color:#fff;font:900 56px Inter;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1.05;box-shadow:8px 10px 0 #e63946}
.payb small{font:800 30px Inter;color:#ffe14d}
.big2{position:absolute;left:0;top:660px;width:1080px;text-align:center}
.big2 .o{display:inline-block;position:relative;font:900 100px Inter;color:#777}
.big2 .n{font:900 210px Inter;line-height:1.1;margin-top:20px}
.big2 .n span{background:#ffe14d;padding:0 24px}
'''
ITEMS = [('Chaussettes', 'Chaussettes de sport', '8,00 €'), ('Gants', 'Gants de running', '9,00 €'), ('Gourde', 'Gourde', '10,00 €')]


def cart(field='empty', gtype=None, disc=False, gdisc=None, total='27,00 €'):
    rows = ''.join(f'<div class="row"><span class="ico">{icon(ic, 84)}</span>{lab}<span class="p">{pr}</span></div>' for ic, lab, pr in ITEMS)
    if field == 'empty':
        f = '<div class="field"><span class="ph">vide</span></div>'
    else:
        a = f' data-g="{gtype}" data-fx="type"' if gtype else ''
        f = f'<div class="field"><span class="hl"{a}>hzklink</span></div>'
    d = ''
    if disc:
        a = f' data-g="{gdisc}" data-fx="right"' if gdisc else ''
        d = f'<div class="row disc"{a}>Code promo Hacoo (-14 %)<span class="p">-3,78 €</span></div>'
    return f'''<div class="paper cart"><div class="h">Mon panier Hacoo</div>{rows}
     <div class="lab">CODE PROMO HACOO</div><div class="fr">{f}<div class="btn">Appliquer</div></div>{d}
     <div class="tot"><span>Total</span><span>{total}</span></div></div>'''


BODY = '''
  <div class="scene" data-s="0">''' + title('Attends !<br>Ta case <mark>code promo Hacoo</mark><br>est vide') + svg(110, 640, 260, 470, GUY) + '''
   <div class="payb">PAYER<small>27,00 €</small></div>''' + svg(700, 880, 260, 300, HANDSTOP).replace('class="abs ink"', 'class="abs ink" data-g="0.0" data-fx="up"') + '''
   <div class="note" style="left:380px;top:640px;transform:rotate(-6deg)" data-g="0.1" data-fx="pop">STOP !</div>
   <div class="ex" style="top:1220px">prix d'exemple</div></div>
  <div class="scene" data-s="1" data-in="up">''' + title('<em>Vide ?</em>', 220, size=110) + cart() + circle(150, 962, 440, 140, '1.0') + '''
   <div class="note" style="left:640px;top:400px;transform:rotate(4deg)" data-g="1.1" data-fx="pop">tu paies trop !</div></div>
  <div class="scene" data-s="2" data-in="right">''' + title('4 étapes', 220, size=90) + cart() + '''
   <div class="num" style="left:40px;top:500px" data-g="2.0" data-fx="stamp">1</div>
   <div class="num" style="left:30px;top:1005px" data-g="2.1" data-fx="stamp">2</div>''' + circle(150, 962, 440, 140, '2.1') + '''
   <div class="ex" style="top:400px">prix d'exemple</div></div>
  <div class="scene" data-s="3" data-in="right">''' + title('4 étapes', 220, size=90) + cart('code', '3.0') + '''
   <div class="num" style="left:30px;top:1005px" data-g="3.0" data-fx="stamp">3</div>
   <div class="num" style="left:770px;top:912px;width:90px;height:90px;font-size:54px" data-g="3.1" data-fx="stamp">4</div>''' + circle(575, 985, 350, 150, '3.1', 3) + '''</div>
  <div class="scene" data-s="4" data-in="up">''' + title('Nouvelle ligne :', 220, size=90) + cart('code', None, True, '4.0', '23,22 €') + underline2(180, 1182, 720, '4.1') + '''
   <div class="note" style="left:620px;top:380px;transform:rotate(-3deg)" data-g="4.1" data-fx="pop">-14 % !</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + title('Au lieu de 27,00 €', 220, size=80) + '''
   <div class="big2"><div class="o">27,00 €''' + svg(-20, 40, 500, 40, '<path class="dr" pathLength="1" d="M0 30 L480 6" data-g="5.1" data-fx="draw"/>', 'red') + '''</div>
    <div class="n" data-g="5.0" data-fx="stamp" data-slow="5.0"><span>23,22 €</span></div></div>
   <div class="ex" style="top:1150px" data-g="5.2" data-fx="fade">prix d'exemple · code promo Hacoo hzklink</div></div>
  <div class="scene" data-s="6" data-in="pop">
   <div class="endw" data-g="6.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div>
    <div class="b">liens des articles tendance en bio</div><div class="x">Prix d'exemple · -14 % avec le code promo Hacoo hzklink · Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
   <div class="note" style="left:300px;top:900px;transform:rotate(-3deg)" data-g="6.2" data-fx="pop">enregistre la vidéo ★</div></div>
'''
