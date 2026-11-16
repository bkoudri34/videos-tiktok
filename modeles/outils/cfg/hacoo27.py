import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°2 du 16/11/2026 - style v3 nuit & or, accent rouge cerise, « 3 trouvailles tendance à petit prix » :
# bonnet 7,00 € + trousse 6,00 € + tote bag 9,00 € = 22,00 € -> 18,92 € avec le code promo Hacoo hzklink (-14 %, prix d'exemple).
# Étiquettes suspendues -> un article par plan sur un présentoir -> pastille du code -> 3 étiquettes barrées + nouveau total (ralenti) -> fin.
# Voix : Speko (speechify, voix par défaut ; voix clonée refusée 402).
NAME = 'hacoo27'
TITLE = 'Hacoo trouvailles cerise'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Trois trouvailles Hacou à moins de dix euros.", [("3 trouvailles Hacoo", None), ("à moins de 10 €.", None)]),
 ("Un bonnet tout doux : sept euros, prix d'exemple.", [("Un bonnet tout doux :", None), ("7 €,", None), ("prix d'exemple.", None)]),
 ("Une trousse rose : six euros.", [("Une trousse rose :", None), ("6 €.", None)]),
 ("Un tote bag : neuf euros.", [("Un tote bag :", None), ("9 €.", None)]),
 ("Avec le code promo Hacou H Z K link,", [("Avec le code promo Hacoo", None), ("hzklink,", None)]),
 ("les trois passent à dix-huit euros quatre-vingt-douze.", [("les 3 passent à", None), ("18,92 €.", None)]),
 ("Les liens des articles tendance sont dans ma bio.", [("Les liens des articles tendance", None), ("sont dans ma bio.", None)]),
]
SPLITS = [(0.0, 1.61), (2.17, 4.34), (4.99, 6.44), (6.75, 8.08), (8.57, 10.66), (10.82, 12.63), (13.23, 14.92)]
GSTART = [[0.1, 1.0], [2.2, 3.2, 3.9], [5.0, 5.9], [6.75, 7.6], [8.6, 9.8], [10.82, 11.5], [13.23, 14.4]]
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
.ce{color:#ff6b86;text-shadow:0 0 18px rgba(255,77,109,.5)}
.hang{position:absolute;top:620px;width:4px;background:#d9a24c;transform-origin:50% 0}
.tg{position:absolute;width:230px;height:300px;border-radius:20px;background:#f4efe4;color:#1c1310;text-align:center;box-shadow:0 26px 60px rgba(0,0,0,.65);padding-top:56px}
.tg:before{content:'';position:absolute;left:97px;top:16px;width:30px;height:30px;border-radius:50%;background:#07060a;border:4px solid #d9a24c}
.tg .q{font:900 120px 'DejaVu Serif',serif;color:#ff4d6d;line-height:1.1}
.tg .p{font:900 60px 'DejaVu Serif',serif;color:#c41f3e;margin-top:6px;white-space:nowrap}
.tg .x{font:800 18px Inter;letter-spacing:3px;color:#6d5f55}
.ped{position:absolute;left:290px;top:1180px;width:500px;height:200px}
.ped .t{position:absolute;left:0;top:0;width:500px;height:60px;border-radius:50%;background:radial-gradient(ellipse,#3a1a20,#1a0b0e);border:4px solid #d9a24c}
.ped .b{position:absolute;left:40px;top:30px;width:420px;height:170px;background:linear-gradient(180deg,#2a1a1c,#120a0b);border-left:4px solid #d9a24c;border-right:4px solid #d9a24c}
.art{position:absolute;left:340px;top:760px;width:400px;height:400px;border-radius:50%;background:radial-gradient(circle,#f4efe4 0 62%,transparent 63%);display:flex;align-items:center;justify-content:center;box-shadow:0 0 70px rgba(255,77,109,.3)}
.prt{position:absolute;left:690px;top:800px;width:220px;padding:18px 0;border-radius:18px;background:#ff4d6d;color:#fff;text-align:center;transform:rotate(8deg);box-shadow:0 20px 50px rgba(0,0,0,.6)}
.prt b{display:block;font:900 70px 'DejaVu Serif',serif;line-height:1.05}
.prt span{font:800 17px Inter;letter-spacing:2px}
.nb{position:absolute;left:150px;top:780px;font:900 italic 150px 'Liberation Serif',serif;color:rgba(255,77,109,.35)}
.chip3{position:absolute;left:170px;top:760px;width:740px;height:150px;border-radius:75px;background:#1a0a0d;border:5px solid #ff4d6d;display:flex;align-items:center;justify-content:center;gap:26px;white-space:nowrap;box-shadow:0 0 50px rgba(255,77,109,.35)}
.chip3 .k{font:800 30px Inter;letter-spacing:3px;color:#ff8fa3}
.chip3 .c{font:900 70px 'DejaVu Sans Mono',monospace;color:#fff}
.scis{position:absolute;left:0;top:960px;width:1080px;text-align:center;font:800 34px Inter;letter-spacing:5px;color:#f3c766}
.mini{position:absolute;top:760px;width:250px;height:290px;border-radius:22px;background:#f4efe4;text-align:center;padding-top:10px}
.mini .s{font:900 40px 'DejaVu Serif',serif;color:#8f877a;text-decoration:line-through;text-decoration-color:#ff4d6d}
.nt2{position:absolute;left:0;top:1110px;width:1080px;text-align:center}
.nt2 .o{font:900 70px 'DejaVu Serif',serif;color:#8f877a;text-decoration:line-through;text-decoration-color:#ff4d6d}
.nt2 .n{font:900 170px 'DejaVu Serif',serif;line-height:1.05}
.nt2 .x{font:800 24px Inter;letter-spacing:4px;color:#e9e4da}
'''
ITEMS = [('Bonnet', '7 €'), ('Trousse', '6 €'), ('Tote', '9 €')]


def item_scene(sid, k, ins):
    ic, pr = ITEMS[k]
    labels = ['UN BONNET TOUT DOUX :', 'UNE TROUSSE ROSE :', 'UN TOTE BAG :']
    sub = [('it gold', '7 €,', f'{sid}.1', 'font-size:110px'), ('it gold', "prix d'exemple.", f'{sid}.2', 'font-size:66px')] if k == 0 else [('it gold', pr + '.', f'{sid}.1', 'font-size:110px')]
    return (f'''  <div class="scene" data-s="{sid}" data-in="{ins}">''' + hd(230, [('h1 ce', labels[k], f'{sid}.0', 'font-size:64px')] + sub) +
            f'''<div class="nb">0{k + 1}</div><div class="ped"><div class="b"></div><div class="t"></div></div>
   <div class="art" data-g="{sid}.0" data-fx="pop">{icon(ic, 300)}</div>
   <div class="prt" data-g="{sid}.1" data-fx="stamp"><b>{pr}</b><span>PRIX D'EXEMPLE</span></div></div>
''')


TAGS = ''.join(f'<div class="hang" style="left:{x + 113}px;height:{h}px"></div><div class="tg" style="left:{x}px;top:{620 + h}px;transform:rotate({r}deg)"><div class="q">?</div><div class="x">MOINS DE 10 €</div></div>'
               for x, h, r in [(130, 220, -6), (425, 300, 3), (720, 200, 6)])

BODY = hud('FRANCE · TROUVAILLES', 'HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('h1', '3 TROUVAILLES HACOO', None, 'font-size:68px'), ('it gold', 'à moins de', None, 'font-size:76px'), ('big gold', '10 €.', None, 'font-size:150px')]).replace('top:220px', 'top:200px') + TAGS.replace('top:840px', 'top:880px').replace('top:920px', 'top:960px').replace('top:820px', 'top:860px') + '''</div>
''' + item_scene(1, 0, 'right') + item_scene(2, 1, 'right') + item_scene(3, 2, 'right') + '''  <div class="scene" data-s="4" data-in="pop">''' + hd(230, [('h1', 'AVEC LE CODE', '4.0', ''), ('h1 ce', 'PROMO HACOO', '4.0', ''), ('big gold', 'hzklink,', '4.1', 'font-size:120px')]) + '''
   <div class="chip3" style="top:820px" data-g="4.0" data-fx="up"><span class="k">CODE HACOO :</span><span class="c" data-g="4.1" data-fx="type">hzklink</span></div>
   <div class="scis" style="top:1020px" data-g="4.1" data-fx="fade">-14 % SUR L'APPLI HACOO</div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="rays" style="top:900px"></div>''' + hd(230, [('it gold', 'les 3 passent à', '5.0', 'font-size:80px')]) + ''.join(
    f'<div class="mini" style="left:{x}px;top:420px;transform:rotate({r}deg)" data-g="5.0" data-fx="up">{icon(ic, 180)}<div class="s">{pr}</div></div>' for (ic, pr), x, r in zip(ITEMS, [130, 415, 700], [-4, 2, 5])) + '''
   <div class="nt2" style="top:790px"><div class="o" data-g="5.0" data-fx="fade">22,00 €</div><div class="n gold" data-g="5.1" data-fx="stamp" data-slow="5.1">18,92 €</div><div class="x" data-g="5.1" data-fx="fade">PRIX D'EXEMPLE · CODE PROMO HACOO hzklink</div></div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'CODE PROMO HACOO', '6.0', ''), ('big gold', 'hzklink', '6.0', 'font-size:150px'), ('it gold', "-14 % sur l'appli Hacoo", '6.0', 'font-size:60px')]) + '''
   <div class="pill" style="top:730px;border-color:rgba(255,77,109,.85)" data-g="6.0" data-fx="up"><div class="pin" style="background:#ff4d6d;color:#fff">★</div><div><b>LES LIENS DES ARTICLES TENDANCE</b><span data-g="6.1" data-fx="fade">sont dans ma bio</span></div></div>
   <div class="cond" style="top:880px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
