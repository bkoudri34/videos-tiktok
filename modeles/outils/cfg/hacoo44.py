import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from tuto import *
from hacoo_items import icon
# Hacoo n°2 du 22/11/2026 - style T « Tuto illustré », accent vert sapin (brief veille du 22/11, vidéo 2).
# Format « STOP + checklist à enregistrer » (F1 + F2) : accroche fixe « Ta checklist Hacoo avant de payer : enregistre-la » + STOP tamponné
# sur le bouton PAYER -> case 1 mesures en cm (bottine + écharpe + mètre ruban) -> case 2 avis avec photos (vignettes étoilées)
# -> case 3 code promo Hacoo hzklink -> ardoise 41 + 13 + 6 = 60,00 € -> 60 € x 14 % = 8,40 € -> 60,00 € barré, 51,60 € (ralenti)
# -> écran de fin + « enregistre cette vidéo », retour au bouton PAYER (boucle). Pas de sujet retours / remboursements.
# Prix d'exemple : bottines 41 € + écharpe 13 € + chaussettes 6 € = 60,00 € ; -14 % = 8,40 € ; total 51,60 €.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08 ; « Hacou » pour Hacoo, « H, Z, K, link » pour hzklink.
NAME = 'hacoo44'
TITLE = 'Hacoo checklist vert sapin'
LINES = [
 ("Stop ! Ta checklist Hacou avant de payer : coche ces trois cases.", [("<i>Stop !</i>", None), ("Ta checklist <em>Hacoo</em>", None), ("avant de payer :", None), ("coche ces 3 cases.", None)]),
 ("Case un : les mesures en centimètres, pas juste la lettre.", [("<i>Case 1 :</i>", None), ("les mesures <em>en cm</em>,", None), ("pas juste la lettre.", None)]),
 ("Case deux : les avis avec photos.", [("<i>Case 2 :</i>", None), ("les avis <em>avec photos</em>.", None)]),
 ("Case trois : le code promo Hacou, H, Z, K, link.", [("<i>Case 3 :</i>", None), ("le <em>code promo Hacoo</em>,", None), ("<em>hzklink</em>.", None)]),
 ("Bottines, écharpe, chaussettes : soixante euros.", [("Bottines, écharpe,", None), ("chaussettes :", None), ("<i>60 €</i>.", None)]),
 ("Avec le code, tu économises huit euros quarante.", [("Avec le code,", None), ("tu économises", None), ("<em>8,40 €</em>.", None)]),
 ("Cinquante et un euros soixante. Prix d'exemple.", [("<em>51,60 €</em>.", None), ("Prix d'exemple.", None)]),
 ("Enregistre cette vidéo pour ta prochaine commande. Code promo Hacou, H, Z, K, link.", [("Enregistre cette vidéo", None), ("pour ta prochaine commande.", None), ("<em>Code promo Hacoo</em>,", None), ("<em>hzklink</em>.", None)]),
]
SPLITS = [(0.0, 3.10), (3.68, 6.58), (7.21, 8.64), (9.35, 12.84), (13.33, 15.48), (15.85, 18.01), (18.44, 20.51), (21.15, 25.32)]
GSTART = [[0.0, 0.8, 1.5, 2.3], [3.7, 4.6, 5.9], [7.21, 7.8], [9.35, 10.2, 11.3], [13.33, 14.2, 14.9], [15.95, 16.6, 17.2], [18.44, 19.9], [21.15, 22.0, 23.5, 24.3]]
MINLEN = 1.8
GAP = 0.25
TAIL = 1.9

CSS = '''
.ck{position:absolute;left:150px;width:780px;padding:22px 34px;background:#fff;border:6px solid #111;border-radius:28px;box-shadow:10px 12px 0 #111}
.ck .r{display:flex;align-items:center;gap:22px;height:84px;font:800 38px Inter;white-space:nowrap;color:#111}
.ck .r.off{color:#9a958b}
.ck .r.on{background:#e3f1e8;border-radius:16px;margin:0 -14px;padding:0 14px}
.bx{position:relative;flex:none;width:60px;height:60px;border:6px solid #111;border-radius:12px;background:#fff}
.bx svg{position:absolute;left:-8px;top:-22px}
.vs path{fill:none;stroke:#1f6f4a;stroke-width:12;stroke-linecap:round;stroke-linejoin:round}
.stop{position:absolute;padding:6px 34px;border:12px solid #e63946;border-radius:22px;color:#e63946;font:900 130px Inter;letter-spacing:6px;transform:rotate(-12deg);background:rgba(255,255,255,.75)}
.pay{position:absolute;left:500px;top:700px;width:380px;height:150px;border-radius:75px;background:#111;color:#fff;font:900 64px Inter;display:flex;align-items:center;justify-content:center;letter-spacing:3px;box-shadow:8px 10px 0 #1f6f4a}
.tape{position:absolute;height:70px;background:#ffe14d;border:5px solid #111;border-radius:10px;background-image:repeating-linear-gradient(90deg,#111 0 4px,transparent 4px 30px);background-size:30px 26px;background-repeat:repeat-x;background-color:#ffe14d}
.lb{position:absolute;font:700 40px 'Comic Relief',cursive;color:#e63946;white-space:nowrap}
.ph{position:absolute;width:210px;height:250px;background:#fff;border:6px solid #111;border-radius:20px;box-shadow:6px 8px 0 #111;text-align:center;padding-top:16px}
.ph .im{margin:0 auto;width:160px;height:120px;border:5px solid #111;border-radius:10px;background:linear-gradient(160deg,#dcefe4 0 55%,#1f6f4a 55%)}
.ph .st{font:900 34px Inter;color:#e6a400;margin-top:16px;letter-spacing:2px}
.fld{position:absolute;left:150px;width:780px;padding:34px 40px;background:#fff;border:6px solid #111;border-radius:28px;box-shadow:10px 12px 0 #111}
.fld .k{font:900 36px Inter;letter-spacing:2px;color:#1f6f4a;margin-bottom:16px}
.fld .row2{display:flex;justify-content:space-between;font:900 44px Inter;margin-top:22px;white-space:nowrap}
.its{position:absolute;left:150px;width:780px;display:flex;justify-content:space-between}
.its .it{width:240px;text-align:center;font:800 32px Inter;white-space:nowrap}.its .it .ico{display:block}
.its .it b{display:block;font:900 44px Inter;margin-top:6px}
.calc{position:absolute;left:130px;width:820px;padding:40px;border-radius:26px;background:#1f3a2b;border:18px solid #8a6a43;box-shadow:10px 12px 0 #111;color:#f4f1e8;text-align:center}
.calc .l{font:700 66px 'Comic Relief',cursive;white-space:nowrap;line-height:1.5}
.calc .l span{background:#ffe14d;color:#111;padding:0 18px;border-radius:10px}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:700 30px 'Comic Relief',cursive;color:#555}
.big2{position:absolute;left:0;top:640px;width:1080px;text-align:center}
.big2 .o{display:inline-block;position:relative;font:900 110px Inter;color:#777}
.big2 .n{font:900 190px Inter;line-height:1.1;margin-top:20px}
.big2 .n span{background:#ffe14d;padding:0 24px}
.pin{position:absolute;left:150px;top:1010px;width:780px;height:120px;border-radius:60px;background:#1f6f4a;color:#fff;display:flex;align-items:center;justify-content:center;gap:18px;font:900 44px Inter;white-space:nowrap;box-shadow:8px 10px 0 #111}
'''
TICK = '<svg class="vs" width="90" height="90" viewBox="0 0 90 90"><path d="M14 48 L36 70 L80 14"/></svg>'


def ck(top, on=None, done=(), g=None, labels=('Mesures en cm', 'Avis avec photos', 'Case code promo'), scale=1):
    rows = ''
    for k, lab in enumerate(labels):
        cls = 'on' if k == on else ('' if k in done or on is None else 'off')
        t = ''
        if k in done:
            t = TICK
        elif k == on and g:
            t = TICK.replace('<svg ', f'<svg data-g="{g}" data-fx="tick" ')
        rows += f'<div class="r {cls}"><div class="bx">{t}</div>{lab}</div>'
    st = f'top:{top}px' + (f';transform:scale({scale});transform-origin:50% 0' if scale != 1 else '')
    return f'<div class="ck" style="{st}">{rows}</div>'


BODY = '''
  <div class="scene" data-s="0">''' + title('Ta checklist <mark>Hacoo</mark><br>avant de payer :<br><em>enregistre-la</em>', 220, size=64) + svg(150, 660, 240, 460, GUY) + '''
   <div class="pay">PAYER</div>
   <div class="stop" style="left:510px;top:850px;font-size:100px" data-g="0.0" data-fx="stamp">STOP</div>
   <div class="note" style="left:170px;top:600px;transform:rotate(-6deg)" data-g="0.1" data-fx="pop">attends !</div>
   ''' + ck(1110, None, (), None, ('', '', ''), 1).replace('<div class="ck" style="top:1110px">', '<div class="ck" style="top:1060px;left:470px;width:400px;padding:14px 26px" data-g="0.3" data-fx="up">') + '''</div>
  <div class="scene" data-s="1" data-in="up">''' + title('Case 1', 220, size=90) + ck(360, 0, (), '1.0') + '''
   <span class="abs ico" style="left:190px;top:780px">''' + icon('Bottines', 230) + '''</span><span class="abs ico" style="left:610px;top:780px">''' + icon('Écharpe', 230) + '''</span>
   <div class="tape" style="left:170px;top:1040px;width:740px" data-g="1.1" data-fx="left"></div>
   <div class="lb" style="left:420px;top:900px;transform:rotate(-6deg)" data-g="1.1" data-fx="pop">en cm !</div>
   <div class="lb" style="left:360px;top:1150px;color:#111" data-g="1.2" data-fx="pop">pas juste « M » ou « L »</div>''' + underline2(400, 1215, 300, '1.2') + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + title('Case 2', 220, size=90) + ck(360, 1, (0,), '2.0') + '''
   <div class="ph" style="left:150px;top:800px;transform:rotate(-5deg)" data-g="2.1" data-fx="pop"><div class="im"></div><div class="st">★★★★★</div></div>
   <div class="ph" style="left:435px;top:780px" data-g="2.1" data-fx="pop"><div class="im"></div><div class="st">★★★★☆</div></div>
   <div class="ph" style="left:720px;top:800px;transform:rotate(5deg)" data-g="2.1" data-fx="pop"><div class="im"></div><div class="st">★★★★★</div></div>''' + circle(120, 760, 840, 330, '2.1', -2) + '''
   <div class="lb" style="left:330px;top:1130px" data-g="2.1" data-fx="pop">des vraies photos</div></div>
  <div class="scene" data-s="3" data-in="left">''' + title('Case 3', 220, size=90) + ck(360, 2, (0, 1), '3.0') + '''
   <div class="fld" style="top:780px" data-g="3.1" data-fx="pop"><div class="k">CODE PROMO HACOO</div><div class="field"><span data-g="3.2" data-fx="type">hzklink</span></div>
    <div class="row2" data-g="3.2" data-fx="stamp"><span>Réduction</span><span style="color:#1f6f4a">-14 %</span></div></div>
   <div class="note" style="left:640px;top:1130px;transform:rotate(-5deg)" data-g="3.2" data-fx="pop">-14 % !</div></div>
  <div class="scene" data-s="4" data-in="up">''' + title('Exemple', 220, size=90) + '''
   <div class="its" style="top:380px"><div class="it" data-g="4.0" data-fx="pop"><span class="ico">''' + icon('Bottines', 170) + '''</span>Bottines<b>41 €</b></div><div class="it" data-g="4.0" data-fx="pop"><span class="ico">''' + icon('Écharpe', 170) + '''</span>Écharpe<b>13 €</b></div><div class="it" data-g="4.1" data-fx="pop"><span class="ico">''' + icon('Chaussettes', 170) + '''</span>Chaussettes<b>6 €</b></div></div>
   <div class="calc" style="top:780px"><div class="l">41 + 13 + 6</div><div class="l" data-g="4.2" data-fx="stamp">= <span>60,00 €</span></div></div>
   <div class="ex" style="top:1180px">prix d'exemple</div></div>
  <div class="scene" data-s="5" data-in="right">''' + title('Le calcul', 220, size=90) + '''
   <div class="calc" style="top:560px"><div class="l">60 € × 14 %</div><div class="l" data-g="5.2" data-fx="stamp">= <span>8,40 €</span> en moins</div></div>
   <div class="fld" style="top:960px;padding:24px 40px"><div class="k" style="margin:0">CODE PROMO HACOO : <span style="color:#111;font-family:'DejaVu Sans Mono'">hzklink</span></div></div></div>
  <div class="scene" data-s="6" data-in="pop">''' + title('Ton total', 220, size=90) + '''
   <div class="big2"><div class="o">60,00 €''' + svg(-20, 40, 500, 40, '<path class="dr" pathLength="1" d="M0 30 L480 6" data-g="6.0" data-fx="draw"/>', 'red') + '''</div>
    <div class="n" data-g="6.0" data-fx="stamp" data-slow="6.0"><span>51,60 €</span></div></div>''' + circle(150, 800, 780, 320, '6.1') + '''
   <div class="ex" style="top:1150px" data-g="6.1" data-fx="fade">prix d'exemple · code promo Hacoo hzklink</div></div>
  <div class="scene" data-s="7" data-in="pop">
   <div class="endw" data-g="7.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div>
    <div class="b">liens des articles tendance en bio</div><div class="x">Prix d'exemple · -14 % avec le code promo Hacoo hzklink · Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
   <div class="pin" style="top:1150px" data-g="7.0" data-fx="pop">📌 ENREGISTRE CETTE VIDÉO</div>
   <div class="ck" style="top:790px;left:300px;width:480px;padding:10px 24px;transform:scale(.8);transform-origin:50% 0" data-g="7.1" data-fx="up"><div class="r"><div class="bx">''' + TICK + '''</div>cm</div><div class="r"><div class="bx">''' + TICK + '''</div>photos</div><div class="r"><div class="bx">''' + TICK + '''</div>hzklink</div></div></div>
'''
