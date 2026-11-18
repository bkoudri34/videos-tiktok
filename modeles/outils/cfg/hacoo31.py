import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°1 du 18/11/2026 - style v3 nuit & or, accent ambre (repli : le brief veille demandait le style D « Duo 3D »,
# mais Three.js est injoignable depuis le bac à sable (jsDelivr, unpkg, cdnjs et registre npm refusés) ; scénario du brief conservé).
# « Les 3 signes que tu paies trop sur Hacoo » : doudoune 39 € + casquette 11 € = 50,00 € -> 43,00 € avec le code promo Hacoo hzklink
# (-14 %, 7,00 € d'économie), prix d'exemple. 3 pastilles « signe » qui s'allument -> articles -> case code promo vide entourée
# -> bulle « les codes c'est du flan » tamponnée FAUX -> champ qui se tape hzklink -> total 43,00 € (ralenti) -> fin.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'hacoo31'
TITLE = 'Hacoo 3 signes ambre'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Les trois signes que tu paies trop sur Hacou.", [("Les 3 signes", None), ("que tu paies trop", None), ("sur Hacoo.", None)]),
 ("Signe numéro un : une doudoune, une casquette, cinquante euros, sans réfléchir.", [("Signe n° 1 :", None), ("une doudoune,", None), ("une casquette,", None), ("50 €, sans réfléchir.", None)]),
 ("Signe numéro deux : tu ne regardes jamais la case code promo.", [("Signe n° 2 :", None), ("tu ne regardes jamais", None), ("la case code promo.", None)]),
 ("Signe numéro trois : tu crois que les codes, c'est du flan.", [("Signe n° 3 :", None), ("tu crois que les codes,", None), ("c'est du flan.", None)]),
 ("Code promo Hacou, H Z K link : moins quatorze pour cent.", [("Code promo Hacoo,", None), ("hzklink :", None), ("-14 %.", None)]),
 ("Quarante-trois euros au lieu de cinquante. Prix d'exemple.", [("43 €", None), ("au lieu de 50.", None), ("Prix d'exemple.", None)]),
 ("Envoie ça au pote qui paie plein pot. Les liens sont dans ma bio.", [("Envoie ça au pote", None), ("qui paie plein pot.", None), ("Les liens sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 1.54), (2.12, 6.12), (6.58, 9.21), (9.67, 12.24), (12.70, 15.31), (15.75, 18.09), (18.59, 21.44)]
GSTART = [[0.0, 0.6, 1.1], [2.12, 3.3, 4.0, 4.8], [6.6, 7.63, 8.4], [9.7, 10.84, 11.8], [12.7, 13.6, 14.5], [15.75, 16.5, 17.57], [18.8, 19.6, 20.45]]
MINLEN = 1.9
GAP = 0.32
TAIL = 2.2


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.am{color:#ffa45c;text-shadow:0 0 18px rgba(255,138,61,.55)}
.sg3{position:absolute;left:150px;width:780px;display:flex;justify-content:space-between}
.sg3 div{width:230px;height:230px;border-radius:50%;border:6px solid #5a4a3a;background:#14100c;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#6d6152}
.sg3 div b{font:900 110px 'DejaVu Serif',serif;line-height:1}
.sg3 div small{font:800 24px Inter;letter-spacing:4px}
.sg3 div.on{border-color:#ff8a3d;background:#2a1708;color:#ffd9b8;box-shadow:0 0 50px rgba(255,138,61,.55)}
.sg3 div.on b{color:#ffa45c}
.it3{position:absolute;top:900px;width:330px;text-align:center}
.it3 .pt{display:inline-block;margin-top:10px;padding:6px 24px;border-radius:14px;background:#f4efe4;color:#2a1708;font:900 60px 'DejaVu Serif',serif;white-space:nowrap}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:800 28px Inter;letter-spacing:5px;color:#9a917f}
.co{position:absolute;left:190px;top:760px;width:700px;border-radius:40px;background:#f4efe4;color:#1a1408;padding:36px 44px;box-shadow:0 30px 90px rgba(0,0,0,.7)}
.co .t{font:900 40px Inter}
.co .row{display:flex;justify-content:space-between;font:600 32px Inter;margin-top:16px;white-space:nowrap}
.co .lab{margin-top:26px;font:800 24px Inter;letter-spacing:3px;color:#8a5a2a}
.co .in{margin-top:8px;height:96px;border-radius:18px;border:4px solid #c9c4ba;background:#fff;display:flex;align-items:center;padding:0 24px;font:900 56px 'DejaVu Sans Mono',monospace;color:#1a1408;white-space:nowrap}
.co .tot{display:flex;justify-content:space-between;margin-top:24px;font:900 44px Inter;white-space:nowrap}
.ring{position:absolute;left:210px;top:1035px;width:660px;height:150px;border:8px solid #ff8a3d;border-radius:50%;transform:rotate(-3deg);box-shadow:0 0 30px rgba(255,138,61,.6)}
.bq{position:absolute;left:150px;top:820px;width:780px;padding:50px 40px;border-radius:50px;background:#fff;color:#1a1a1a;font:800 italic 66px 'Liberation Serif',serif;text-align:center;line-height:1.15}
.bq:after{content:'';position:absolute;left:140px;bottom:-40px;border:24px solid transparent;border-top:40px solid #fff;border-left:24px solid #fff}
.stmp{position:absolute;left:560px;top:1050px;padding:10px 40px;border:10px solid #e5322d;border-radius:20px;color:#e5322d;font:900 110px Inter;transform:rotate(-12deg);background:rgba(255,255,255,.06)}
.ok{margin-top:14px;font:900 40px Inter;color:#1f9d55}
.tot43{position:absolute;left:0;top:640px;width:1080px;text-align:center}
.tot43 .n{font:900 210px 'DejaVu Serif',serif;line-height:1.05}
.tot43 .o{font:900 80px 'DejaVu Serif',serif;color:#8f877a;text-decoration:line-through;text-decoration-color:#ff4d4d;text-decoration-thickness:7px}
.chip{position:absolute;left:170px;width:740px;height:130px;border-radius:65px;background:#1a1008;border:5px solid #ff8a3d;display:flex;align-items:center;justify-content:center;gap:24px;white-space:nowrap;box-shadow:0 0 50px rgba(255,138,61,.35)}
.chip .k{font:800 30px Inter;letter-spacing:3px;color:#ffc99c}
.chip .c{font:900 64px 'DejaVu Sans Mono',monospace;color:#fff}
'''


def signs(on, g=None, top=760):
    out = f'<div class="sg3" style="top:{top}px">'
    for k in range(3):
        cls = 'on' if k < on else ''
        a = f' data-g="{g}" data-fx="stamp"' if (g and k == on - 1) else ''
        out += f'<div class="{cls}"{a}><b>{k + 1}</b><small>SIGNE</small></div>'
    return out + '</div>'


def checkout(code=False, g=None):
    field = (f'<div class="in"><span data-g="{g}" data-fx="type">hzklink</span></div><div class="ok" data-g="{g}" data-fx="fade">✓ -14 % appliqué</div>'
             if code else '<div class="in" style="color:#b5afa4">vide</div>')
    return f'''<div class="co"><div class="t">Mon panier Hacoo</div>
     <div class="row"><span>Doudoune</span><b>39,00 €</b></div><div class="row"><span>Casquette</span><b>11,00 €</b></div>
     <div class="lab">CODE PROMO HACOO</div>{field}</div>'''


BODY = hud('FRANCE · 3 SIGNES', 'HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(215, [('h1', 'LES 3 SIGNES', None, 'font-size:96px'), ('it gold', 'que tu paies trop', None, 'font-size:80px'), ('h1 am', 'SUR HACOO', None, 'font-size:110px')]) + signs(0, top=780) + '''
   <div class="ex" style="top:1100px">CODE PROMO HACOO · PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="1" data-in="right">''' + hd(215, [('h1 am', 'SIGNE N° 1 :', '1.0', 'font-size:84px'), ('it gold', 'plein pot, sans réfléchir.', '1.3', 'font-size:64px')]) + f'''
   <div class="it3" style="left:150px" data-g="1.1" data-fx="pop">{icon('Doudoune', 260)}<div class="pt">39 €</div></div>
   <div class="it3" style="left:600px" data-g="1.2" data-fx="pop">{icon('Casquette', 260)}<div class="pt">11 €</div></div>
   <div class="ex" style="top:1300px" data-g="1.3" data-fx="fade">TOTAL 50,00 € · PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(215, [('h1 am', 'SIGNE N° 2 :', '2.0', 'font-size:84px'), ('it gold', 'tu ne regardes jamais', '2.1', 'font-size:64px'), ('it gold', 'la case code promo.', '2.2', 'font-size:64px')]) + checkout() + '''
   <div class="ring" data-g="2.2" data-fx="pop"></div></div>
  <div class="scene" data-s="3" data-in="right">''' + hd(215, [('h1 am', 'SIGNE N° 3 :', '3.0', 'font-size:84px'), ('it gold', 'tu crois que les codes,', '3.1', 'font-size:64px')]) + '''
   <div class="bq" data-g="3.1" data-fx="pop">« Les codes,<br>c'est du flan. »</div>
   <div class="stmp" data-g="3.2" data-fx="stamp">FAUX</div></div>
  <div class="scene" data-s="4" data-in="up">''' + hd(215, [('h1', 'CODE PROMO HACOO', '4.0', 'font-size:80px'), ('big gold', 'hzklink', '4.1', 'font-size:130px')]) + checkout(True, '4.1').replace('class="co"', 'class="co" style="top:640px"') + '''</div>
  <div class="scene" data-s="5" data-in="pop"><div class="rays" style="top:540px"></div>''' + hd(215, [('h1 am', '-14 %', '5.0', 'font-size:110px')]) + '''
   <div class="tot43"><div class="n gold" data-g="5.0" data-fx="stamp" data-slow="5.0">43,00 €</div><div class="o" data-g="5.1" data-fx="fade">50,00 €</div></div>
   <div class="chip" style="top:1080px" data-g="5.1" data-fx="up"><span class="k">CODE PROMO HACOO</span><span class="c">hzklink</span></div>
   <div class="ex" style="top:1260px" data-g="5.2" data-fx="fade">PRIX D'EXEMPLE · 7,00 € D'ÉCONOMIE</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(215, [('h1', 'CODE PROMO HACOO', '6.0', ''), ('big gold', 'hzklink', '6.0', 'font-size:150px'), ('it gold', "-14 % sur l'appli Hacoo", '6.0', 'font-size:60px')]) + '''
   <div class="pill" style="top:730px;border-color:rgba(255,138,61,.85)" data-g="6.0" data-fx="up"><div class="pin" style="background:#ff8a3d;color:#1a0d04">↗</div><div><b>ENVOIE AU POTE QUI PAIE PLEIN POT</b><span data-g="6.2" data-fx="fade">liens des articles tendance en bio</span></div></div>
   <div class="cond" style="top:880px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
'''
