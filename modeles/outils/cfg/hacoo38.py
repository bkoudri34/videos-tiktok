import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from tuto import *
from hacoo_items import icon
# Hacoo n°2 du 20/11/2026 - style T « Tuto illustré » (repli prévu par le brief veille du 20/11 : le style D2 « Duo dessiné » n'a pas été construit
# aujourd'hui). On garde l'histoire du duo, racontée par une seule voix : « Il a payé plein pot sur Hacoo… ».
# Format F10 raconté : le pigeon et son ticket 70 € -> panier dessiné -> « t'as mis le code promo ? » -> « quel code ?! » case vide
# -> code promo Hacoo hzklink -14 % -> 9,80 € en moins -> 70,00 € barré, 60,20 € (ralenti) -> écran de fin + « envoie-la à ton pote ».
# Prix d'exemple : baskets de running 49 € + casquette 12 € + gourde 9 € = 70,00 € ; -14 % = 9,80 € ; total 60,20 €.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08 ; « Hacou » pour Hacoo, « H Z K link » pour hzklink.
NAME = 'hacoo38'
TITLE = 'Hacoo plein pot duo tuto'
LINES = [
 ("Il a payé plein pot sur l'appli Hacou. Regarde.", [("<em>Il a payé plein pot</em>", None), ("sur l'appli <em>Hacoo</em>.", None), ("Regarde.", None)]),
 ("Baskets de running, casquette, gourde : soixante-dix euros.", [("Baskets de running,", None), ("casquette, gourde :", None), ("<i>70 €</i>.", None)]),
 ("Son pote lui demande : t'as mis le code promo ?", [("Son pote lui demande :", None), ("t'as mis", None), ("le <em>code promo</em> ?", None)]),
 ("Quel code ? La case était juste là, vide.", [("Quel code ?", None), ("La case était juste là,", None), ("<i>vide</i>.", None)]),
 ("Code promo Hacou : H Z K link. Moins quatorze pour cent.", [("<em>Code promo Hacoo</em> :", None), ("<em>hzklink</em>.", None), ("<i>-14 %</i>.", None)]),
 ("Ça fait neuf euros quatre-vingts en moins.", [("Ça fait", None), ("<em>9,80 €</em> en moins.", None)]),
 ("Soixante euros vingt au lieu de soixante-dix. Prix d'exemple.", [("<em>60,20 €</em>", None), ("au lieu de 70.", None), ("Prix d'exemple.", None)]),
 ("Envoie-la à ton pote, avant qu'il paie. Code promo Hacou, H Z K link.", [("Envoie-la à ton pote,", None), ("avant qu'il paie.", None), ("<em>Code promo Hacoo</em>,", None), ("<em>hzklink</em>.", None)]),
]
SPLITS = [(0.0, 2.53), (2.98, 5.63), (6.17, 8.10), (8.51, 10.47), (10.94, 13.77), (14.24, 15.44), (16.02, 18.33), (18.82, 22.25)]
MINLEN = 1.9

CSS = '''
.cart{left:140px;top:560px;width:800px;padding:30px 40px 34px}
.cart .h{font:900 46px Inter;margin-bottom:10px}
.cart .row{height:104px}
.cart .tot{display:flex;justify-content:space-between;margin-top:14px;padding-top:16px;border-top:4px dashed #111;font:900 56px Inter;white-space:nowrap}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:700 30px 'Comic Relief',cursive;color:#555}
.tk{position:absolute;padding:20px 30px;background:#fff;border:6px solid #111;border-radius:12px;box-shadow:8px 10px 0 #111;font:900 64px Inter;white-space:nowrap;transform:rotate(-6deg)}
.tk small{display:block;font:700 26px Inter;color:#555}
.lb{position:absolute;font:700 34px 'Comic Relief',cursive;color:#111;white-space:nowrap}
.bub{position:absolute;padding:26px 34px;background:#fff;border:6px solid #111;border-radius:40px;font:900 46px Inter;white-space:nowrap;box-shadow:8px 10px 0 #111}
.fld{position:absolute;left:150px;top:640px;width:780px;padding:34px 40px;background:#fff;border:6px solid #111;border-radius:28px;box-shadow:10px 12px 0 #111}
.fld .k{font:900 36px Inter;letter-spacing:2px;color:#e63946;margin-bottom:16px}
.fld .row2{display:flex;justify-content:space-between;font:900 44px Inter;margin-top:22px;white-space:nowrap}
.big2{position:absolute;left:0;top:640px;width:1080px;text-align:center}
.big2 .o{display:inline-block;position:relative;font:900 110px Inter;color:#777}
.big2 .n{font:900 190px Inter;line-height:1.1;margin-top:20px}
.big2 .n span{background:#ffe14d;padding:0 24px}
.calc{position:absolute;left:110px;top:620px;width:860px;padding:44px;border-radius:26px;background:#25352b;border:18px solid #8a6a43;box-shadow:10px 12px 0 #111;color:#f4f1e8;text-align:center}
.calc .l{font:700 70px 'Comic Relief',cursive;white-space:nowrap;line-height:1.5}
.calc .l span{background:#ffe14d;color:#111;padding:0 18px;border-radius:10px}
'''
ITEMS = [('Baskets', 'Baskets de running', '49,00 €'), ('Casquette', 'Casquette', '12,00 €'), ('Gourde', 'Gourde', '9,00 €')]

# Le pigeon (rond, t-shirt hachuré) et le malin (fin, casquette), dessinés au trait.
PIGEON = '''<g class="ink"><circle cx="130" cy="90" r="62"/><path d="M108 82 l0 8 M152 82 l0 8"/><path d="M108 122 Q130 136 152 122"/>
 <ellipse cx="130" cy="290" rx="100" ry="130"/><path d="M70 230 L190 350 M60 280 L170 390 M95 200 L200 305"/>
 <path d="M90 410 L70 520 M170 410 L190 520"/><path d="M40 250 L-10 170"/><path d="M220 250 L280 190"/></g>'''
PIGEON_HEAD = '''<g class="ink"><circle cx="130" cy="90" r="62"/><path d="M104 80 l10 8 M156 80 l-10 8"/><ellipse cx="130" cy="128" rx="14" ry="18"/>
 <ellipse cx="130" cy="290" rx="100" ry="130"/><path d="M70 230 L190 350 M60 280 L170 390 M95 200 L200 305"/>
 <path d="M90 410 L70 520 M170 410 L190 520"/><path d="M40 250 Q20 120 80 60"/><path d="M220 250 Q240 120 180 60"/></g>'''
MALIN = '''<g class="ink"><circle cx="110" cy="90" r="52"/><path d="M58 76 Q110 20 162 76 Z" style="fill:#e63946"/><path d="M150 72 L210 78"/>
 <path d="M92 96 l0 6 M128 96 l0 6"/><path d="M94 120 Q112 128 132 116"/>
 <path d="M110 142 L110 360"/><path d="M110 360 L70 500 M110 360 L150 500"/><path d="M110 200 L30 280"/><path d="M110 200 L200 150"/></g>'''


def cart():
    rows = ''.join(f'<div class="row"><span class="ico">{icon(ic, 88)}</span>{lab}<span class="p">{pr}</span></div>' for ic, lab, pr in ITEMS)
    return f'<div class="paper cart"><div class="h">Son panier Hacoo</div>{rows}<div class="tot"><span>Total</span><span>70,00 €</span></div></div>'


BODY = '''
  <div class="scene" data-s="0">''' + title('Il a payé plein pot<br>sur <mark>Hacoo</mark>…', 220, size=84) + svg(130, 700, 280, 540, PIGEON) + svg(700, 760, 240, 520, MALIN) + '''
   <div class="tk" style="left:330px;top:640px">70,00 €<small>ticket · prix d'exemple</small></div>
   <div class="lb" style="left:150px;top:1270px">le pigeon</div><div class="lb" style="left:720px;top:1290px">le malin</div>
   <div class="note" style="left:470px;top:880px;transform:rotate(-8deg)" data-g="0.2" data-fx="pop">plein pot !</div></div>
  <div class="scene" data-s="1" data-in="up">''' + title('Son panier', 220, size=90) + cart() + circle(520, 1000, 440, 150, '1.2') + '''
   <div class="ex" style="top:400px">prix d'exemple</div></div>
  <div class="scene" data-s="2" data-in="right">''' + title('Le malin :', 220, size=90) + svg(130, 760, 280, 540, PIGEON) + svg(700, 800, 240, 520, MALIN) + '''
   <div class="bub" style="left:150px;top:560px;font-size:40px" data-g="2.1" data-fx="pop">« T'as mis le <span class="hl">code promo</span> ? »</div></div>
  <div class="scene" data-s="3" data-in="left">''' + title('Le pigeon :', 220, size=90) + svg(80, 800, 280, 540, PIGEON_HEAD) + '''
   <div class="note" style="left:120px;top:650px;font-size:120px;transform:rotate(-6deg)" data-g="3.0" data-fx="stamp">?!</div>
   <div class="fld" style="left:400px;top:700px;width:520px;padding:28px 30px" data-g="3.1" data-fx="pop"><div class="k" style="font-size:28px">CODE PROMO HACOO</div><div class="field"><span class="ph">Ajouter un code</span></div></div>''' + circle(380, 790, 560, 210, '3.2') + '''
   <div class="note" style="left:600px;top:1010px;transform:rotate(4deg)" data-g="3.2" data-fx="pop">vide !</div></div>
  <div class="scene" data-s="4" data-in="pop">''' + title('Code promo Hacoo', 220, size=86) + '''
   <div class="fld"><div class="k">CODE PROMO HACOO</div><div class="field"><span data-g="4.1" data-fx="type">hzklink</span></div>
    <div class="row2" data-g="4.2" data-fx="stamp"><span>Réduction</span><span style="color:#e63946">-14 %</span></div></div>
   <div class="note" style="left:640px;top:1060px;transform:rotate(-5deg);font-size:60px" data-g="4.2" data-fx="pop">-14 % !</div></div>
  <div class="scene" data-s="5" data-in="right">''' + title('Le calcul', 220, size=90) + '''
   <div class="calc"><div class="l">70 € × 14 %</div><div class="l" data-g="5.1" data-fx="stamp">= <span>9,80 €</span> en moins</div></div></div>
  <div class="scene" data-s="6" data-in="pop">''' + title('Ce qu\'il aurait payé', 220, size=80) + '''
   <div class="big2"><div class="o">70,00 €''' + svg(-20, 40, 500, 40, '<path class="dr" pathLength="1" d="M0 30 L480 6" data-g="6.0" data-fx="draw"/>', 'red') + '''</div>
    <div class="n" data-g="6.0" data-fx="stamp" data-slow="6.0"><span>60,20 €</span></div></div>
   <div class="ex" style="top:1150px" data-g="6.2" data-fx="fade">prix d'exemple · code promo Hacoo hzklink</div></div>
  <div class="scene" data-s="7" data-in="pop">
   <div class="endw" data-g="7.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div>
    <div class="b">liens des articles tendance en bio</div><div class="x">Prix d'exemple · -14 % avec le code promo Hacoo hzklink · Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
   <div class="note" style="left:190px;top:1000px;transform:rotate(-3deg)" data-g="7.0" data-fx="pop">envoie-la à ton pote<br>avant qu'il paie</div></div>
'''
