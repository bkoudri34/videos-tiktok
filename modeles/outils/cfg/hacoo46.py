import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°4 du 22/11/2026 (tâche « 2 vidéos Hacoo en plus ») - style V3 nuit & or, accent vert émeraude.
# Format F8 « résultat d'abord » : ticket « -9,66 € » visible dès la 1re image -> LE PANIER (casque, lampe, carnet = 69,00 €)
# -> 1 la case code promo Hacoo avant de payer -> 2 hzklink + Appliquer -> LE RÉSULTAT 59,34 € (ralenti) -> -14 % prix d'exemple -> fin.
# Prix d'exemple : casque audio 38 € + lampe 23 € + carnet 8 € = 69,00 € ; -14 % = 9,66 € (69 x 0,14) ; total 59,34 € (69 x 0,86).
# Voix : Speko Manon (cartesia sonic-3.5), speed 1.08, une synthèse par réplique, silences coupés (internes plafonnés à 0,16 s), atempo 1.1.
# Réplique 5 refaite (« cinquante-neuf euros trente-quatre » compris « 59,33 ») en « cinquante-neuf euros et trente-quatre centimes ».
NAME = 'hacoo46'
TITLE = 'Hacoo résultat d abord émeraude'
ROOT = ':root{--bg:#050a08}'
LINES = [
 ("Code promo Hacou : neuf euros soixante-six de moins sur ce ticket. Voilà comment.", [("<em>Code promo Hacoo</em> :", None), ("<i>9,66 €</i> de moins", None), ("sur ce ticket.", None), ("Voilà comment.", None)]),
 ("Le panier : un casque, une lampe, un carnet. Soixante-neuf euros.", [("Le panier :", None), ("un casque, une lampe,", None), ("un carnet.", None), ("<em>69 €</em>.", None)]),
 ("Avant de payer, ouvre la case code promo de l'appli Hacou.", [("Avant de payer,", None), ("ouvre la case code promo", None), ("de l'appli <em>Hacoo</em>.", None)]),
 ("Tape H, Z, K, link. Puis Appliquer.", [("Tape <i>hzklink</i>.", None), ("Puis <em>Appliquer</em>.", None)]),
 ("Le total passe à cinquante-neuf euros et trente-quatre centimes.", [("Le total passe", None), ("à <em>59,34 €</em>.", None)]),
 ("Quatorze pour cent de moins. Et ce sont des prix d'exemple.", [("<em>-14&nbsp;%</em>.", None), ("Et ce sont", None), ("des prix d'exemple.", None)]),
 ("Envoie cette vidéo à quelqu'un qui paie plein pot. Code promo Hacou : H, Z, K, link.", [("Envoie cette vidéo", None), ("à quelqu'un qui paie", None), ("plein pot.", None), ("<em>Code promo Hacoo</em> :", None), ("<i>hzklink</i>.", None)]),
]
SPLITS = [(0.2, 4.278), (4.728, 8.768), (9.218, 12.42), (12.87, 16.755), (17.205, 20.402), (20.852, 23.636), (24.086, 29.739)]
MINLEN = 1.9
GAP = 0.22
TAIL = 2.2


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.em2{color:#3ee0a0;text-shadow:0 0 18px rgba(40,220,150,.5)}
.band{position:absolute;left:60px;top:560px;height:84px;padding:0 34px 0 18px;border-radius:42px;background:#08160f;border:4px solid #3ee0a0;display:flex;align-items:center;gap:18px;font:900 38px Inter;color:#fff;letter-spacing:3px;white-space:nowrap}
.band .pic{flex:none;width:58px;height:58px;border-radius:50%;background:#3ee0a0;color:#06140d;font:900 36px Inter;display:flex;align-items:center;justify-content:center}
.it3{position:absolute;top:720px;width:290px;text-align:center}
.it3 .pt{display:inline-block;margin-top:10px;padding:6px 22px;border-radius:14px;background:#f4efe4;color:#0d1f17;font:900 58px 'DejaVu Serif',serif;white-space:nowrap}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:800 28px Inter;letter-spacing:5px;color:#93a89c}
.tk{position:absolute;left:220px;top:600px;width:640px;background:#f6f1e6;color:#13211a;padding:34px 40px 46px;font:600 35px 'DejaVu Sans Mono',monospace;box-shadow:0 30px 90px rgba(0,0,0,.7);transform:rotate(-2deg);
 -webkit-mask-image:linear-gradient(135deg,transparent 12px,#000 0),linear-gradient(225deg,transparent 12px,#000 0);-webkit-mask-size:24px 100%;-webkit-mask-position:0 100%}
.tk .t{text-align:center;font:900 34px Inter;letter-spacing:4px;margin-bottom:14px}
.tk .r{display:flex;justify-content:space-between;margin-top:8px;white-space:nowrap}
.tk .dash{border-top:3px dashed #b9b2a3;margin:16px 0}
.tk .g{color:#0f8a5a;font-weight:900}
.tk .tot{display:flex;justify-content:space-between;font:900 46px Inter;white-space:nowrap}
.tk s{color:#8f877a;text-decoration-color:#e3262b;text-decoration-thickness:5px;font-size:34px;margin-right:12px}
.co{position:absolute;left:190px;top:700px;width:700px;border-radius:40px;background:#f4efe4;color:#0d1f17;padding:34px 44px;box-shadow:0 30px 90px rgba(0,0,0,.7)}
.co .t{font:900 40px Inter}
.co .row{display:flex;justify-content:space-between;font:600 32px Inter;margin-top:14px;white-space:nowrap}
.co .lab{margin-top:24px;font:800 24px Inter;letter-spacing:3px;color:#0f8a5a}
.co .fr{display:flex;gap:14px;margin-top:8px}
.co .in{flex:1;height:96px;border-radius:18px;border:4px solid #c9c4ba;background:#fff;display:flex;align-items:center;padding:0 24px;font:900 54px 'DejaVu Sans Mono',monospace;color:#0d1f17;white-space:nowrap}
.co .in.on{border-color:#0f8a5a;box-shadow:0 0 0 6px rgba(15,138,90,.3)}
.co .ap{height:96px;padding:0 24px;border-radius:18px;background:#0f8a5a;color:#fff;font:900 32px Inter;display:flex;align-items:center}
.co .ok{margin-top:14px;font:900 36px Inter;color:#0f8a5a;display:flex;justify-content:space-between;white-space:nowrap}
.co .tot{display:flex;justify-content:space-between;margin-top:18px;font:900 44px Inter;white-space:nowrap}
.num{position:absolute;left:90px;top:1180px;width:150px;height:150px;border-radius:50%;background:linear-gradient(135deg,#d9fff0,#3ee0a0 50%,#0f8a5a);color:#04140c;font:900 96px 'DejaVu Serif',serif;display:flex;align-items:center;justify-content:center;box-shadow:0 20px 60px rgba(0,0,0,.6)}
.totx{position:absolute;left:0;top:700px;width:1080px;text-align:center}
.totx .n{font:900 170px 'DejaVu Serif',serif;line-height:1.05;white-space:nowrap}
.totx .o{font:900 80px 'DejaVu Serif',serif;color:#8f877a;text-decoration:line-through;text-decoration-color:#3ee0a0;text-decoration-thickness:7px}
.pct{position:absolute;left:340px;top:680px;width:400px;height:400px;border-radius:50%;border:8px solid #3ee0a0;display:flex;align-items:center;justify-content:center;white-space:nowrap;font:900 104px 'DejaVu Serif',serif;color:#fff;box-shadow:0 0 70px rgba(40,220,150,.35)}
.chip{position:absolute;left:150px;width:780px;border-radius:52px;background:#08160f;border:5px solid #3ee0a0;display:flex;align-items:center;justify-content:center;white-space:nowrap}
.chip .k{font:800 30px Inter;letter-spacing:3px;color:#c8ffe8}
'''


def band(pic, txt, g=None):
    a = f' data-g="{g}" data-fx="left"' if g else ''
    return f'<div class="band"{a}><div class="pic">{pic}</div>{txt}</div>'


def ticket(top=640, g=None):
    a = f' data-g="{g}" data-fx="pop"' if g else ''
    return f'''<div class="tk" style="top:{top}px"{a}><div class="t">TICKET · HACOO</div>
     <div class="r"><span>Casque audio</span><span>38,00</span></div><div class="r"><span>Lampe</span><span>23,00</span></div><div class="r"><span>Carnet</span><span>8,00</span></div>
     <div class="dash"></div><div class="r g"><span>CODE PROMO HACOO</span><span>-9,66</span></div><div class="r" style="font-size:26px"><span>hzklink (-14 %)</span><span></span></div>
     <div class="dash"></div><div class="tot"><span>TOTAL</span><span><s>69,00</s>59,34 €</span></div></div>'''


def checkout(state, g=None, top=700):
    if state == 'focus':
        field = '<div class="in on" style="color:#b5afa4">|</div>'
        extra = '<div class="tot"><span>Total</span><span>69,00 €</span></div>'
    elif state == 'type':
        field = f'<div class="in on"><span data-g="{g}" data-fx="type">hzklink</span></div>'
        extra = '<div class="tot"><span>Total</span><span>69,00 €</span></div>'
    return f'''<div class="co" style="top:{top}px"><div class="t">Mon panier Hacoo</div>
     <div class="row"><span>Casque audio</span><b>38,00 €</b></div><div class="row"><span>Lampe</span><b>23,00 €</b></div><div class="row"><span>Carnet</span><b>8,00 €</b></div>
     <div class="lab">CODE PROMO HACOO</div><div class="fr">{field}<div class="ap">Appliquer</div></div>{extra}</div>'''


BODY = hud('FRANCE · LE TICKET', 'HACOO') + '''
  <div class="scene" data-s="0"><div class="floor"></div><div class="rays" style="top:560px"></div>''' + hd(215, [('h1', 'CODE PROMO HACOO', None, 'font-size:72px'), ('big em2', '-9,66 €', None, 'font-size:150px'), ('it gold', 'sur ce ticket', None, 'font-size:64px')]) + ticket(640) + '''
   <div class="ex" style="top:1450px">PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="1" data-in="right">''' + band('1', 'LE PANIER', '1.0') + hd(215, [('h1', 'LE PANIER :', '1.0', ''), ('it gold', 'casque, lampe, carnet', '1.1', 'font-size:62px')]) + f'''
   <div class="it3" style="left:70px" data-g="1.1" data-fx="pop">{icon('Casque', 230)}<div class="pt">38 €</div></div>
   <div class="it3" style="left:395px" data-g="1.1" data-fx="pop">{icon('Lampe', 230)}<div class="pt">23 €</div></div>
   <div class="it3" style="left:720px" data-g="1.2" data-fx="pop">{icon('Carnet', 230)}<div class="pt">8 €</div></div>
   <div class="ex" style="top:1110px" data-g="1.3" data-fx="stamp"><b style="font-size:66px;color:#fff;letter-spacing:2px">TOTAL 69,00 €</b><br>PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="2" data-in="up">''' + band('2', 'LA CASE') + hd(215, [('h1 s', 'AVANT DE PAYER', '2.0', ''), ('it em2', 'la case code promo Hacoo', '2.1', 'font-size:60px')]) + checkout('focus', top=680) + '''
</div>
  <div class="scene" data-s="3" data-in="left">''' + band('3', 'LE CODE') + hd(215, [('h1', 'TAPE', '3.0', ''), ('big gold', 'hzklink', '3.0', 'font-size:130px')]) + checkout('type', '3.0', top=740) + '''
</div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:600px"></div>''' + band('€', 'LE RÉSULTAT', '4.0') + hd(215, [('h1', 'LE TOTAL PASSE À', '4.0', 'font-size:66px')]) + '''
   <div class="totx"><div class="n gold" data-g="4.1" data-fx="stamp" data-slow="4.1">59,34 €</div><div class="o" data-g="4.1" data-fx="fade">69,00 €</div></div>
   <div class="ex" style="top:1110px" data-g="4.1" data-fx="fade">CODE PROMO HACOO hzklink · -9,66 €</div></div>
  <div class="scene" data-s="5" data-in="right"><div class="floor"></div>''' + hd(215, [('h1', 'CODE PROMO HACOO', '5.0', 'font-size:68px'), ('it gold', 'sur ce panier', '5.0', 'font-size:60px')]) + '''
   <div class="pct" data-g="5.0" data-fx="stamp">-14 %</div>
   <div class="ex" style="top:1110px;font-size:40px;color:#fff" data-g="5.2" data-fx="stamp">PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(215, [('h1', 'CODE PROMO HACOO', '6.0', ''), ('big gold', 'hzklink', '6.0', 'font-size:150px'), ('it em2', "-14 % sur l'appli Hacoo", '6.1', 'font-size:66px')]) + '''
   <div class="pill" style="top:720px;border-color:rgba(62,224,160,.85)" data-g="6.1" data-fx="up"><div class="pin" style="background:#3ee0a0;color:#04140c">➜</div><div><b style="color:#c8ffe8">ENVOIE-LA À QUELQU'UN</b><span>qui paie toujours plein pot</span></div></div>
   <div class="chip" style="top:870px;height:100px" data-g="6.2" data-fx="up"><span class="k">LIENS DES ARTICLES TENDANCE EN BIO</span></div>
   <div class="cond" style="top:1010px">Prix d'exemple · -14 % avec le code promo Hacoo hzklink<br>Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
'''
