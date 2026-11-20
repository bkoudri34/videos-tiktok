import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°1 du 20/11/2026 - style V3 nuit & or, accent rouge signal (brief veille du 20/11, vidéo 1).
# Format F1 « STOP » en 3 rubriques : panneau STOP -> ❓ L'ERREUR (panier 52 €, case code promo vide qui clignote)
# -> ✅ LE BON RÉFLEXE (1 la case code promo Hacoo, 2 hzklink, 3 la ligne -7,28 € avant de payer) -> 🎟 LE RÉSULTAT 44,72 € (ralenti) -> fin.
# Prix d'exemple : doudoune 39 € + gants 7 € + chaussettes 6 € = 52,00 € ; -14 % = 7,28 € (52 x 0,14) ; total 44,72 € (52 x 0,86).
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08 ; « Hacou » pour Hacoo, « H Z K link » pour hzklink.
NAME = 'hacoo37'
TITLE = 'Hacoo STOP rouge signal'
ROOT = ':root{--bg:#0a0606}'
LINES = [
 ("Stop. Avant de payer sur l'appli Hacou, vérifie ça.", [("STOP.", None), ("Avant de payer", None), ("sur l'appli Hacoo,", None), ("vérifie ça.", None)]),
 ("Ton panier : doudoune, gants, chaussettes. Cinquante-deux euros.", [("Ton panier :", None), ("doudoune, gants,", None), ("chaussettes.", None), ("52 €.", None)]),
 ("Et la case code promo ? Vide. Comme chez presque tout le monde.", [("Et la case code promo ?", None), ("Vide.", None), ("Comme chez presque", None), ("tout le monde.", None)]),
 ("Le bon réflexe : un, la case code promo Hacou.", [("Le bon réflexe :", None), ("1, la case", None), ("code promo Hacoo.", None)]),
 ("Deux, tu tapes H Z K link.", [("2, tu tapes", None), ("hzklink.", None)]),
 ("Trois, tu vérifies la réduction avant de payer.", [("3, tu vérifies", None), ("la réduction", None), ("avant de payer.", None)]),
 ("Moins sept euros vingt-huit. Tu paies quarante-quatre euros soixante-douze. Prix d'exemple.", [("-7,28 €.", None), ("Tu paies", None), ("44,72 €.", None), ("Prix d'exemple.", None)]),
 ("Envoie ça à quelqu'un qui paie toujours plein pot. Code promo Hacou, H Z K link.", [("Envoie ça à quelqu'un", None), ("qui paie toujours plein pot.", None), ("Code promo Hacoo,", None), ("hzklink.", None)]),
]
SPLITS = [(0.0, 2.88), (3.17, 6.22), (6.68, 9.36), (9.88, 12.10), (12.45, 14.02), (14.37, 16.22), (16.57, 20.51), (20.91, 24.5)]
MINLEN = 1.9
GAP = 0.3
TAIL = 2.2


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.rd{color:#ff4a4a;text-shadow:0 0 18px rgba(255,60,60,.55)}
.stop{position:absolute;left:340px;top:700px;width:400px;height:400px}
.stop .o{position:absolute;inset:0;background:#e3262b;clip-path:polygon(29% 0,71% 0,100% 29%,100% 71%,71% 100%,29% 100%,0 71%,0 29%);box-shadow:0 0 60px rgba(255,60,60,.6)}
.stop .i{position:absolute;inset:16px;background:#e3262b;clip-path:polygon(29% 0,71% 0,100% 29%,100% 71%,71% 100%,29% 100%,0 71%,0 29%);border:0;outline:8px solid #fff}
.stop .w{position:absolute;inset:14px;clip-path:polygon(29% 0,71% 0,100% 29%,100% 71%,71% 100%,29% 100%,0 71%,0 29%);background:#fff}
.stop .w2{position:absolute;inset:26px;clip-path:polygon(29% 0,71% 0,100% 29%,100% 71%,71% 100%,29% 100%,0 71%,0 29%);background:#e3262b;display:flex;align-items:center;justify-content:center;font:900 112px Inter;color:#fff;letter-spacing:4px}
.band{position:absolute;left:60px;top:560px;height:84px;padding:0 34px 0 18px;border-radius:42px;background:#1a0d0d;border:4px solid #ff4a4a;display:flex;align-items:center;gap:18px;font:900 38px Inter;color:#fff;letter-spacing:3px;white-space:nowrap}
.band .pic{flex:none;width:58px;height:58px;border-radius:50%;background:#ff4a4a;color:#1a0d0d;font:900 38px Inter;display:flex;align-items:center;justify-content:center}
.band.g{border-color:#e9b456}.band.g .pic{background:#e9b456}
.it3{position:absolute;top:720px;width:290px;text-align:center}
.it3 .pt{display:inline-block;margin-top:10px;padding:6px 22px;border-radius:14px;background:#f4efe4;color:#1f0e0e;font:900 58px 'DejaVu Serif',serif;white-space:nowrap}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:800 28px Inter;letter-spacing:5px;color:#a8958f}
.co{position:absolute;left:190px;top:700px;width:700px;border-radius:40px;background:#f4efe4;color:#1f0e0e;padding:34px 44px;box-shadow:0 30px 90px rgba(0,0,0,.7)}
.co .t{font:900 40px Inter}
.co .row{display:flex;justify-content:space-between;font:600 32px Inter;margin-top:14px;white-space:nowrap}
.co .lab{margin-top:24px;font:800 24px Inter;letter-spacing:3px;color:#b3261e}
.co .in{margin-top:8px;height:96px;border-radius:18px;border:4px solid #c9c4ba;background:#fff;display:flex;align-items:center;padding:0 24px;font:900 56px 'DejaVu Sans Mono',monospace;color:#1f0e0e;white-space:nowrap}
.co .in.bad{border-color:#ff3b3b;box-shadow:0 0 0 8px rgba(255,59,59,.35)}
.co .in.on{border-color:#1f9d55;box-shadow:0 0 0 6px rgba(31,157,85,.3)}
.co .ok{margin-top:14px;font:900 38px Inter;color:#1f9d55;display:flex;justify-content:space-between;white-space:nowrap}
.co .tot{display:flex;justify-content:space-between;margin-top:18px;font:900 44px Inter;white-space:nowrap}
.vide{position:absolute;left:600px;top:1080px;padding:8px 26px;border-radius:16px;background:#ff3b3b;color:#fff;font:900 46px Inter;transform:rotate(-6deg);letter-spacing:3px}
.num{position:absolute;left:90px;top:1300px;width:150px;height:150px;border-radius:50%;background:linear-gradient(135deg,#fff1c4,#e9b456 50%,#a8701f);color:#2a1a05;font:900 96px 'DejaVu Serif',serif;display:flex;align-items:center;justify-content:center;box-shadow:0 20px 60px rgba(0,0,0,.6)}
.totx{position:absolute;left:0;top:700px;width:1080px;text-align:center}
.totx .n{font:900 170px 'DejaVu Serif',serif;line-height:1.05;white-space:nowrap}
.totx .o{font:900 80px 'DejaVu Serif',serif;color:#8f877a;text-decoration:line-through;text-decoration-color:#ff3b3b;text-decoration-thickness:7px}
.chip{position:absolute;left:150px;width:780px;height:130px;border-radius:65px;background:#1a0d0d;border:5px solid #ff4a4a;display:flex;align-items:center;justify-content:center;gap:24px;white-space:nowrap;box-shadow:0 0 50px rgba(255,60,60,.3)}
.chip .k{font:800 30px Inter;letter-spacing:3px;color:#ffd0c8}
.chip .c{font:900 64px 'DejaVu Sans Mono',monospace;color:#fff}
.pct{position:absolute;left:720px;top:600px;padding:10px 26px;border-radius:20px;background:#ff3b3b;color:#fff;font:900 60px Inter;transform:rotate(8deg)}
'''


def stop(top=700, g=None):
    a = f' data-g="{g}" data-fx="stamp"' if g else ''
    return f'<div class="stop" style="top:{top}px"{a}><div class="o"></div><div class="w"></div><div class="w2">STOP</div></div>'


def band(pic, txt, cls='', g=None):
    a = f' data-g="{g}" data-fx="left"' if g else ''
    return f'<div class="band {cls}"{a}><div class="pic">{pic}</div>{txt}</div>'


def checkout(state, g=None, top=700):
    if state == 'empty':
        field = '<div class="in bad" style="color:#b5afa4">Ajouter un code</div>'
        extra = '<div class="tot"><span>Total</span><span>52,00 €</span></div>'
    elif state == 'focus':
        field = '<div class="in on" style="color:#b5afa4">|</div>'
        extra = '<div class="tot"><span>Total</span><span>52,00 €</span></div>'
    elif state == 'type':
        field = f'<div class="in on"><span data-g="{g}" data-fx="type">hzklink</span></div>'
        extra = '<div class="tot"><span>Total</span><span>52,00 €</span></div>'
    else:
        field = '<div class="in on">hzklink</div>'
        extra = (f'<div class="ok" data-g="{g}" data-fx="stamp"><span>Code promo -14 %</span><span>-7,28 €</span></div>'
                 f'<div class="tot" data-g="{g}" data-fx="fade"><span>Total</span><span>44,72 €</span></div>')
    return f'''<div class="co" style="top:{top}px"><div class="t">Mon panier Hacoo</div>
     <div class="row"><span>Doudoune</span><b>39,00 €</b></div><div class="row"><span>Gants</span><b>7,00 €</b></div><div class="row"><span>Chaussettes</span><b>6,00 €</b></div>
     <div class="lab">CODE PROMO HACOO</div>{field}{extra}</div>'''


BODY = hud('FRANCE · AVANT DE PAYER', 'HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(215, [('h1 rd', 'STOP :', None, 'font-size:84px'), ('it gold', 'vérifie ça avant de payer', None, 'font-size:68px'), ('h1', 'SUR HACOO', None, 'font-size:76px')]) + stop(640) + '''
   <div class="ex" style="top:1110px">CODE PROMO HACOO · PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="1" data-in="right">''' + band('?', "L'ERREUR", '', '1.0') + hd(215, [('h1', 'TON PANIER :', '1.0', ''), ('it gold', 'doudoune, gants, chaussettes', '1.1', 'font-size:60px')]) + f'''
   <div class="it3" style="left:70px" data-g="1.1" data-fx="pop">{icon('Doudoune', 230)}<div class="pt">39 €</div></div>
   <div class="it3" style="left:395px" data-g="1.1" data-fx="pop">{icon('Gants', 230)}<div class="pt">7 €</div></div>
   <div class="it3" style="left:720px" data-g="1.2" data-fx="pop">{icon('Chaussettes', 230)}<div class="pt">6 €</div></div>
   <div class="ex" style="top:1110px" data-g="1.3" data-fx="stamp"><b style="font-size:66px;color:#fff;letter-spacing:2px">TOTAL 52,00 €</b><br>PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="2" data-in="up">''' + band('?', "L'ERREUR") + hd(215, [('h1 s', 'ET LA CASE CODE PROMO ?', '2.0', 'font-size:58px'), ('big rd', 'Vide.', '2.1', 'font-size:120px')]) + checkout('empty', top=660) + '''
   <div class="vide" style="top:1140px" data-g="2.1" data-fx="stamp">VIDE</div>
   <div class="ex" style="top:1420px;color:#d8c6c0" data-g="2.2" data-fx="fade">comme chez presque tout le monde</div></div>
  <div class="scene" data-s="3" data-in="right">''' + band('✓', 'LE BON RÉFLEXE', 'g', '3.0') + hd(215, [('h1', 'LE BON RÉFLEXE :', '3.0', 'font-size:66px'), ('it gold', '1, la case code promo Hacoo', '3.1', 'font-size:58px')]) + checkout('focus', top=700) + '''
   <div class="num" data-g="3.1" data-fx="stamp">1</div></div>
  <div class="scene" data-s="4" data-in="left">''' + band('✓', 'LE BON RÉFLEXE', 'g') + hd(215, [('h1', '2, TU TAPES', '4.0', ''), ('big gold', 'hzklink', '4.1', 'font-size:130px')]) + checkout('type', '4.1', top=740) + '''
   <div class="num" data-g="4.0" data-fx="stamp">2</div></div>
  <div class="scene" data-s="5" data-in="right">''' + band('✓', 'LE BON RÉFLEXE', 'g') + hd(215, [('h1 s', '3, TU VÉRIFIES', '5.0', ''), ('it gold', 'la réduction avant de payer', '5.1', 'font-size:60px')]) + checkout('done', '5.1', top=700) + '''
   <div class="num" data-g="5.0" data-fx="stamp">3</div></div>
  <div class="scene" data-s="6" data-in="pop"><div class="rays" style="top:600px"></div>''' + band('€', 'LE RÉSULTAT', 'g', '6.0') + hd(215, [('h1 rd', '-7,28 €', '6.0', 'font-size:110px'), ('it gold', 'tu paies', '6.1', '')]) + '''
   <div class="totx"><div class="n gold" data-g="6.2" data-fx="stamp" data-slow="6.2">44,72 €</div><div class="o" data-g="6.2" data-fx="fade">52,00 €</div></div>
   <div class="pct" style="top:1230px;left:440px" data-g="6.0" data-fx="stamp">-14 %</div>
   <div class="ex" style="top:1380px" data-g="6.3" data-fx="fade">PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="7" data-in="pop">''' + hd(215, [('h1', 'CODE PROMO HACOO', '7.2', ''), ('big gold', 'hzklink', '7.3', 'font-size:150px'), ('it rd', "-14 % sur l'appli Hacoo", '7.3', 'font-size:66px')]) + '''
   <div class="pill" style="top:720px;border-color:rgba(255,74,74,.85)" data-g="7.0" data-fx="up"><div class="pin" style="background:#ff4a4a;color:#fff">➜</div><div><b style="color:#ffd0c8">ENVOIE-LA À QUELQU'UN</b><span>qui paie toujours plein pot</span></div></div>
   <div class="chip" style="top:870px;height:100px" data-g="7.1" data-fx="up"><span class="k" style="font-size:30px">LIENS DES ARTICLES TENDANCE EN BIO</span></div>
   <div class="cond" style="top:1010px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
'''
