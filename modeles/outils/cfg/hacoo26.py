import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°1 du 16/11/2026 - style v3 nuit & or, accent émeraude, « écran de paiement : le total baisse quand on tape le code » :
# pyjama 16,00 € + lampe 14,00 € = 30,00 € -> 25,80 € avec le code promo Hacoo hzklink (-14 %, prix d'exemple).
# Voix : Speko (speechify, voix par défaut ; voix clonée refusée 402).
NAME = 'hacoo26'
TITLE = 'Hacoo paiement emeraude'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Regarde ce que fait ce code sur Hacou.", [("Regarde ce que fait", None), ("ce code sur Hacoo.", None)]),
 ("Dans le panier : un pyjama et une lampe.", [("Dans le panier :", None), ("un pyjama", None), ("et une lampe.", None)]),
 ("Trente euros, en prix d'exemple.", [("30 €,", None), ("en prix d'exemple.", None)]),
 ("On ajoute le code promo Hacou H Z K link.", [("On ajoute", None), ("le code promo Hacoo", None), ("hzklink.", None)]),
 ("Le total descend à vingt-cinq euros quatre-vingts.", [("Le total descend à", None), ("25,80 €.", None)]),
 ("Moins quatorze pour cent. Les liens des articles tendance sont dans ma bio.", [("-14 %.", None), ("Les liens des articles tendance", None), ("sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 1.44), (1.90, 3.69), (3.98, 5.13), (5.90, 8.19), (8.67, 10.40), (10.86, 13.75)]
GSTART = [[0.1, 0.8], [1.9, 2.8, 3.3], [3.98, 4.67], [5.9, 6.3, 7.0], [8.67, 9.5], [10.86, 12.1, 13.2]]
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
.em{color:#4fe3a4;text-shadow:0 0 18px rgba(61,220,151,.5)}
.ph{position:absolute;left:230px;width:620px;border-radius:56px;background:#0c0f0d;border:10px solid #2c2925;box-shadow:0 0 0 2px #514a40,0 30px 90px rgba(0,0,0,.7);padding:40px 34px 34px;box-sizing:border-box}
.ph .top{display:flex;justify-content:space-between;font:800 24px 'DejaVu Sans Mono',monospace;letter-spacing:4px;color:#4fe3a4;margin-bottom:14px}
.ph .it{display:flex;align-items:center;gap:20px;padding:14px 0;border-bottom:2px solid rgba(255,255,255,.07);white-space:nowrap}
.ph .ic{flex:none;width:110px;height:110px;border-radius:22px;background:#f4efe4;display:flex;align-items:center;justify-content:center}
.ph .nm{flex:1;font:800 34px Inter;color:#f3f1ec}
.ph .pr{font:900 40px 'DejaVu Serif',serif;color:#f3f1ec}
.ph .cd{margin-top:22px;height:90px;border-radius:18px;border:3px dashed rgba(79,227,164,.6);display:flex;align-items:center;gap:16px;padding:0 22px;white-space:nowrap}
.ph .cd small{font:800 20px Inter;letter-spacing:2px;color:#4fe3a4}
.ph .cd b{font:900 44px 'DejaVu Sans Mono',monospace;color:#fff}
.ph .tt{display:flex;justify-content:space-between;align-items:baseline;margin-top:22px;font:900 34px Inter;color:#e9e4da;white-space:nowrap}
.ph .tt b{font:900 60px 'DejaVu Serif',serif;color:#fff}
.ph .ex{font:700 20px Inter;letter-spacing:3px;color:#7f8a84;text-align:right;margin-top:4px}
.ph .btn{margin-top:20px;height:84px;border-radius:42px;background:#3ddc97;color:#06150e;font:900 32px Inter;letter-spacing:3px;display:flex;align-items:center;justify-content:center}
.eye{position:absolute;width:120px;height:120px;border-radius:50%;background:#3ddc97;color:#06150e;font:900 70px Inter;display:flex;align-items:center;justify-content:center;box-shadow:0 20px 50px rgba(0,0,0,.6)}
.kb{position:absolute;left:190px;top:1180px;width:700px;display:grid;grid-template-columns:repeat(7,1fr);gap:10px}
.kb i{height:74px;border-radius:12px;background:#1c1f1d;border:2px solid #333a36;font:800 30px 'DejaVu Sans Mono',monospace;font-style:normal;color:#cfd8d2;display:flex;align-items:center;justify-content:center}
.kb i.on{background:#3ddc97;color:#06150e;border-color:#f3c766}
.old{position:absolute;left:0;width:1080px;text-align:center;font:900 96px 'DejaVu Serif',serif;color:#8f877a;text-decoration:line-through;text-decoration-color:#ff5a5a}
.dn{position:absolute;left:700px;top:700px;font:900 110px Inter;color:#3ddc97}
.bdg{position:absolute;left:390px;top:1060px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle,#0f3324,#06140e);border:6px solid #3ddc97;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 0 50px rgba(61,220,151,.45)}
.bdg b{font:900 90px 'DejaVu Serif',serif;color:#fff}.bdg span{font:800 20px Inter;letter-spacing:3px;color:#bff5dd}
'''
ITEMS = [('Pyjama', 'Pyjama', '16,00 €'), ('Lampe', 'Lampe', '14,00 €')]


def phone(top, gs=None, code=None, total='30,00 €', g_tot=None, g_code=None):
    rows = ''
    for k, (ic, nm, pr) in enumerate(ITEMS):
        a = f' data-g="{gs[k]}" data-fx="right"' if gs else ''
        rows += f'<div class="it"{a}><div class="ic">{icon(ic, 96)}</div><div class="nm">{nm}</div><div class="pr">{pr}</div></div>'
    if code:
        gc = f' data-g="{g_code}" data-fx="type"' if g_code else ''
        cd = f'<div class="cd"><small>CODE PROMO HACOO</small><b{gc}>{code}</b></div>'
    else:
        cd = '<div class="cd"><small>CODE PROMO HACOO</small><b style="color:#4a524d">……</b></div>'
    ta = f' data-g="{g_tot}" data-fx="tick"' if g_tot else ''
    return (f'<div class="ph" style="top:{top}px"><div class="top"><span>PAIEMENT · HACOO</span><span>2 ART.</span></div>{rows}{cd}'
            f'<div class="tt"{ta}><span>TOTAL</span><b>{total}</b></div><div class="ex">PRIX D\'EXEMPLE</div><div class="btn">PAYER</div></div>')


KEYS = ''.join(f'<i class="{"on" if c in "hzklin" else ""}">{c}</i>' for c in 'azertyuqsdfghjklmwxcvbn'[:21])

BODY = hud('FRANCE · PAIEMENT', 'HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('h1', 'REGARDE CE QUE FAIT', None, 'font-size:64px'), ('it em', 'ce code sur Hacoo.', None, 'font-size:84px')]) + phone(520, None, None).replace('class="ph"', 'class="ph" style="transform:scale(.9);transform-origin:50% 0"', 1).replace('style="transform:scale(.9);transform-origin:50% 0" style="top:520px"', 'style="top:520px;transform:scale(.9);transform-origin:50% 0"') + '''
   <div class="eye" style="left:780px;top:1180px">?</div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1 em', 'DANS LE PANIER :', '1.0', ''), ('it gold', 'un pyjama', '1.1', 'font-size:80px'), ('it gold', 'et une lampe.', '1.2', 'font-size:80px')]) + phone(620, ['1.1', '1.2'], None, '…') + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('big gold', '30 €,', '2.0', 'font-size:150px'), ('it gold', "en prix d'exemple.", '2.1', 'font-size:76px')]) + phone(620, None, None, '30,00 €', '2.0') + '''</div>
  <div class="scene" data-s="3" data-in="pop">''' + hd(230, [('h1', 'ON AJOUTE', '3.0', ''), ('it gold', 'le code promo Hacoo', '3.1', 'font-size:78px'), ('big gold', 'hzklink.', '3.2', 'font-size:110px')]) + phone(640, None, 'hzklink', '30,00 €', None, '3.2').replace('<div class="tt"', '<div class="tt" style="display:none"').replace('<div class="ex">', '<div class="ex" style="display:none">').replace('<div class="btn">', '<div class="btn" style="display:none">') + '''
   <div class="kb" data-g="3.1" data-fx="up">''' + KEYS + '''</div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:640px"></div>''' + hd(230, [('h1 em', 'LE TOTAL DESCEND À', '4.0', 'font-size:66px')]) + '''
   <div class="old" style="top:380px" data-g="4.0" data-fx="fade">30,00 €</div>
   <div class="abs" style="left:0;top:540px;width:1080px;text-align:center" data-g="4.1" data-fx="stamp" data-slow="4.1"><div class="gold" style="font:900 200px 'DejaVu Serif',serif;line-height:1.1">25,80 €</div></div>
   <div class="abs" style="left:0;top:860px;width:1080px;text-align:center;font:800 30px Inter;letter-spacing:4px;color:#bff5dd" data-g="4.1" data-fx="fade">✓ CODE PROMO HACOO hzklink APPLIQUÉ</div>
   <div class="abs" style="left:0;top:920px;width:1080px;text-align:center;font:700 24px Inter;letter-spacing:4px;color:#8f877a" data-g="4.1" data-fx="fade">PRIX D'EXEMPLE</div>
   <div class="bdg" data-g="4.1" data-fx="pop"><b>-14 %</b><span>4,20 € EN MOINS</span></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'CODE PROMO HACOO', '5.0', ''), ('big gold', 'hzklink', '5.0', 'font-size:150px'), ('it gold', "-14 % sur l'appli Hacoo", '5.0', 'font-size:60px')]) + '''
   <div class="pill" style="top:730px;border-color:rgba(61,220,151,.85)" data-g="5.1" data-fx="up"><div class="pin" style="background:#3ddc97">★</div><div><b>LES LIENS DES ARTICLES TENDANCE</b><span data-g="5.2" data-fx="fade">sont dans ma bio</span></div></div>
   <div class="cond" style="top:880px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
