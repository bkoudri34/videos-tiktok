import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from tuto import *
from hacoo_items import icon
# Hacoo n°4 du 23/11/2026 (tâche « 2 vidéos Hacoo en plus ») - style T « Tuto illustré », accent bleu stylo.
# Format F5 défi chrono : « DÉFI : code promo Hacoo en 10 s » + chrono dessiné dès la 1re image -> 1 Commander -> 2 la case code promo
# -> 3 hzklink + Appliquer -> STOP 8 s -> ardoise 19 + 14 + 11 = 44,00 € x 14 % = 6,16 € -> 44,00 € barré, 37,84 € (ralenti)
# -> fin « enregistre et relève le défi ». Pas de sujet R.
# Prix d'exemple : sac 19 € + bouillotte 14 € + coque 11 € = 44,00 € ; -14 % = 6,16 € (44 x 0,14) ; total 37,84 € (44 x 0,86).
# Voix : Speko Hélène (inworld-tts-2), speed 1.08, une synthèse par réplique, silences coupés (internes plafonnés à 0,16 s), atempo 1.12, +3 dB.
# Réplique 6 refaite (« Tote bag » compris « taux de bague ») en « Un sac, une bouillotte, une coque ».
NAME = 'hacoo50'
TITLE = 'Hacoo défi chrono bleu'
LINES = [
 ("Défi : appliquer le code promo Hacou en dix secondes. Top chrono !", [("<i>Défi :</i>", None), ("le <em>code promo Hacoo</em>", None), ("en 10 secondes.", None), ("Top chrono !", None)]),
 ("Un : dans ton panier, touche Commander.", [("<i>1 :</i> dans ton panier,", None), ("touche <em>Commander</em>.", None)]),
 ("Deux : ouvre la case code promo.", [("<i>2 :</i> ouvre la case", None), ("<em>code promo</em>.", None)]),
 ("Trois : tape H, Z, K, link, puis Appliquer.", [("<i>3 :</i> tape <em>hzklink</em>,", None), ("puis <em>Appliquer</em>.", None)]),
 ("Stop ! Huit secondes.", [("<i>Stop !</i>", None), ("<em>8 secondes</em>.", None)]),
 ("Un sac, une bouillotte, une coque : quarante-quatre euros. Avec le code, tu économises six euros et seize centimes.", [("Un sac, une bouillotte,", None), ("une coque : <em>44 €</em>.", None), ("Avec le code,", None), ("tu économises <em>6,16 €</em>.", None)]),
 ("Tu paies trente-sept euros et quatre-vingt-quatre centimes. Prix d'exemple.", [("Tu paies <em>37,84 €</em>.", None), ("Prix d'exemple.", None)]),
 ("Enregistre cette vidéo et relève le défi. Code promo Hacou : H, Z, K, link. Les liens sont dans ma bio.", [("Enregistre cette vidéo", None), ("et relève le défi.", None), ("<em>Code promo Hacoo</em> :", None), ("<em>hzklink</em>.", None), ("Les liens sont dans ma bio.", None)]),
]
SPLITS = [(0.2, 3.585), (4.035, 5.983), (6.433, 8.034), (8.484, 12.484), (12.934, 14.215), (14.665, 20.518), (20.968, 24.271), (24.721, 31.281)]
MINLEN = 1.8
GAP = 0.22
TAIL = 2.0

CSS = '''
.chr{position:absolute;border:12px solid #111;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;font:900 Inter;color:#111;box-shadow:10px 12px 0 #2b6cf0;white-space:nowrap}
.chr:before{content:'';position:absolute;left:50%;top:-46px;width:56px;height:34px;margin-left:-28px;background:#111;border-radius:8px}
.chr b{font:900 inherit}
.chr small{position:absolute;bottom:18%;font:800 30px Inter;color:#2b6cf0;letter-spacing:2px}
.ph2{position:absolute;left:330px;width:420px;padding-bottom:40px !important;border:10px solid #111;border-radius:56px;background:#fff;box-shadow:10px 12px 0 #111;padding:60px 28px 0}
.ph2 .t{font:900 34px Inter;color:#111;margin-bottom:14px}
.ph2 .r{display:flex;justify-content:space-between;font:700 28px Inter;color:#333;margin-top:10px;white-space:nowrap}
.ph2 .tot{display:flex;justify-content:space-between;font:900 34px Inter;margin-top:20px;border-top:4px dashed #bbb;padding-top:14px;white-space:nowrap}
.ph2 .bt{margin-top:28px;height:84px;border-radius:42px;background:#2b6cf0;color:#fff;font:900 34px Inter;display:flex;align-items:center;justify-content:center;letter-spacing:2px}
.fld{position:absolute;left:150px;width:780px;padding:34px 40px;background:#fff;border:6px solid #111;border-radius:28px;box-shadow:10px 12px 0 #111}
.fld .k{font:900 36px Inter;letter-spacing:2px;color:#2b6cf0;margin-bottom:16px}
.fld .fr{display:flex;gap:16px}.fld .fr .field{flex:1}
.fld .ap{height:100px;padding:0 26px;border-radius:18px;background:#2b6cf0;color:#fff;font:900 34px Inter;display:flex;align-items:center;border:5px solid #111}
.fld .ok{margin-top:20px;font:900 40px Inter;color:#2b6cf0;display:flex;justify-content:space-between;white-space:nowrap}
.big1{position:absolute;left:60px;top:240px;width:180px;height:180px;border-radius:50%;background:#2b6cf0;color:#fff;font:900 120px Inter;display:flex;align-items:center;justify-content:center;border:8px solid #111}
.stop{position:absolute;padding:6px 34px;border:14px solid #e63946;border-radius:22px;color:#e63946;font:900 150px Inter;letter-spacing:6px;transform:rotate(-10deg);background:rgba(255,255,255,.8)}
.its{position:absolute;left:150px;width:780px;display:flex;justify-content:space-between}
.its .it{width:240px;text-align:center;font:800 34px Inter;white-space:nowrap}.its .it .ico{display:block}
.its .it b{display:block;font:900 46px Inter;margin-top:6px}
.calc{position:absolute;left:130px;width:820px;padding:36px;border-radius:26px;background:#1d2a44;border:18px solid #8a6a43;box-shadow:10px 12px 0 #111;color:#f4f1e8;text-align:center}
.calc .l{font:700 62px 'Comic Relief',cursive;white-space:nowrap;line-height:1.45}
.calc .l span{background:#ffe14d;color:#111;padding:0 18px;border-radius:10px}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:700 32px 'Comic Relief',cursive;color:#555}
.big2{position:absolute;left:0;top:560px;width:1080px;text-align:center}
.big2 .o{display:inline-block;position:relative;font:900 110px Inter;color:#777}
.big2 .n{font:900 190px Inter;line-height:1.1;margin-top:20px}
.big2 .n span{background:#ffe14d;padding:0 24px}
.pin{position:absolute;left:150px;width:780px;height:120px;border-radius:60px;background:#2b6cf0;color:#fff;display:flex;align-items:center;justify-content:center;gap:18px;font:900 42px Inter;white-space:nowrap;box-shadow:8px 10px 0 #111}
'''


def chrono(x, y, size, txt, sub='SECONDES', g=None, fx='pop'):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    return f'<div class="chr" style="left:{x}px;top:{y}px;width:{size}px;height:{size}px;font-size:{int(size * .42)}px"{a}><b>{txt}</b><small>{sub}</small></div>'


def phone(top, btn_g=None):
    return f'''<div class="ph2" style="top:{top}px"><div class="t">Mon panier Hacoo</div>
     <div class="r"><span>Sac</span><b>19,00 €</b></div><div class="r"><span>Bouillotte</span><b>14,00 €</b></div><div class="r"><span>Coque</span><b>11,00 €</b></div>
     <div class="tot"><span>Total</span><span>44,00 €</span></div><div class="bt">COMMANDER</div></div>'''


def fld(top, state, g=None):
    if state == 'empty':
        f = '<div class="field"><span class="ph">ton code ici</span></div>'
        ok = ''
    else:
        f = f'<div class="field"><span data-g="{g}" data-fx="type">hzklink</span></div>'
        ok = f'<div class="ok" data-g="3.1" data-fx="stamp"><span>✓ Appliqué</span><span>-14 %</span></div>'
    return f'<div class="fld" style="top:{top}px"><div class="k">CODE PROMO HACOO</div><div class="fr">{f}<div class="ap">Appliquer</div></div>{ok}</div>'


BODY = '''
  <div class="scene" data-s="0">''' + title('DÉFI : code promo <mark>Hacoo</mark><br>appliqué en <em>10 s</em>', 230, size=72) + chrono(400, 580, 400, '10') + '''
   <div class="note" style="left:610px;top:500px;transform:rotate(8deg)">top chrono !</div>''' + svg(150, 640, 240, 460, GUY) + '''
   <div class="ex" style="top:1080px">3 gestes · prix d'exemple</div></div>
  <div class="scene" data-s="1" data-in="up"><div class="big1">1</div>''' + title('Touche <em>Commander</em>', 450, size=70) + chrono(700, 240, 180, '2', 's', None) + phone(580) + circle(330, 895, 440, 150, '1.1') + '''
   <div class="note" style="left:110px;top:960px;transform:rotate(-8deg)" data-g="1.1" data-fx="pop">ici !</div></div>
  <div class="scene" data-s="2" data-in="right"><div class="big1">2</div>''' + title('La case <em>code promo</em>', 450, size=70) + chrono(700, 240, 180, '4', 's', None) + fld(720, 'empty') + arrow(380, 560, 200, 150, 'M10 10 Q150 20 170 120 M140 95 L170 125 L190 90', '2.1') + '''
   <div class="note" style="left:200px;top:1040px;transform:rotate(-5deg)" data-g="2.1" data-fx="pop">ouvre-la !</div></div>
  <div class="scene" data-s="3" data-in="left"><div class="big1">3</div>''' + title('Tape <mark style="text-transform:none">hzklink</mark> + Appliquer', 450, size=62) + chrono(700, 240, 180, '6', 's', None) + fld(640, 'type', '3.0') + '''
   <div class="note" style="left:560px;top:1060px;transform:rotate(-6deg)" data-g="3.1" data-fx="pop">-14 % !</div></div>
  <div class="scene" data-s="4" data-in="pop">''' + title('Code promo <mark>Hacoo</mark><br>appliqué en…', 230, size=72) + chrono(330, 560, 420, '8', 'SECONDES', '4.1', 'stamp') + '''
   <div class="stop" style="left:330px;top:1020px;font-size:120px" data-g="4.0" data-fx="stamp">STOP</div></div>
  <div class="scene" data-s="5" data-in="up">''' + title('Exemple', 220, size=90) + '''
   <div class="its" style="top:370px"><div class="it" data-g="5.0" data-fx="pop"><span class="ico">''' + icon('Tote', 170) + '''</span>Sac<b>19 €</b></div><div class="it" data-g="5.0" data-fx="pop"><span class="ico">''' + icon('Bouillotte', 170) + '''</span>Bouillotte<b>14 €</b></div><div class="it" data-g="5.1" data-fx="pop"><span class="ico">''' + icon('Coque', 170) + '''</span>Coque<b>11 €</b></div></div>
   <div class="calc" style="top:780px"><div class="l" data-g="5.1" data-fx="stamp">19 + 14 + 11 = <span>44,00 €</span></div><div class="l" data-g="5.3" data-fx="stamp">44 € × 14 % = <span>6,16 €</span></div></div>
   <div class="ex" style="top:1210px">prix d'exemple · code promo Hacoo hzklink</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + title('Tu paies', 220, size=90) + '''
   <div class="big2"><div class="o">44,00 €''' + svg(-20, 40, 500, 40, '<path class="dr" pathLength="1" d="M0 30 L480 6" data-g="6.0" data-fx="draw"/>', 'red') + '''</div>
    <div class="n" data-g="6.0" data-fx="stamp" data-slow="6.0"><span>37,84 €</span></div></div>''' + circle(150, 720, 780, 320, '6.1') + '''
   <div class="ex" style="top:1100px" data-g="6.1" data-fx="fade">prix d'exemple · code promo Hacoo hzklink (-14 %)</div></div>
  <div class="scene" data-s="7" data-in="pop">
   <div class="endw" data-g="7.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div>
    <div class="b">liens des articles tendance en bio</div><div class="x">Prix d'exemple · -14 % avec le code promo Hacoo hzklink · Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
   <div class="pin" style="top:1000px" data-g="7.1" data-fx="pop">⏱ ENREGISTRE & RELÈVE LE DÉFI</div>
   </div>
'''
