import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Hello bank, 17/11/2026 16:00 - style v3 nuit & or, accent turquoise. Offre de bienvenue jusqu'à 330 € = 80 € à l'ouverture
# (Hello One ou Hello Prime) + 50 € avec Hello Prime (5 paiements ou retraits par mois pendant 12 mois) + bon d'achat 200 €
# (Hello Start+, mobilité bancaire), jusqu'au 08/12/2026 inclus (source : moneyvox.fr, article du 13/11/2026).
# Voix : Speko (speechify, voix par défaut ; voix clonée refusée 402), réplique 4 refaite seule (« trois » mal prononcé).
# Format « checklist en 3 étapes » : barre d'étapes 1-2-3 qui avance, téléphone (choix de l'offre) -> calendrier 5 paiements
# -> deux banques + bon d'achat -> ticket total 330 € (ralenti) -> sablier J-21 -> appel à l'action.
NAME = 'hellobank11'
TITLE = 'Hello bank checklist turquoise'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Hello bank lâche jusqu'à trois cent trente euros.", [("Hello bank lâche", None), ("jusqu'à", None), ("330 €.", None)]),
 ("Étape un : tu ouvres Hello One ou Hello Prime. Quatre-vingts euros.", [("Étape 1 :", None), ("tu ouvres Hello One", None), ("ou Hello Prime.", None), ("80 €.", None)]),
 ("Étape deux : avec Hello Prime, cinq paiements par mois. Cinquante euros de plus.", [("Étape 2 :", None), ("avec Hello Prime,", None), ("5 paiements par mois.", None), ("50 € de plus.", None)]),
 ("Dernière étape : tu actives la mobilité bancaire. Un bon d'achat de deux cents euros.", [("Dernière étape :", None), ("tu actives", None), ("la mobilité bancaire.", None), ("Un bon d'achat", None), ("de 200 €.", None)]),
 ("Ça fait jusqu'à trois cent trente euros.", [("Ça fait jusqu'à", None), ("330 €.", None)]),
 ("Ta demande en ligne, c'est avant le huit décembre.", [("Ta demande en ligne,", None), ("c'est avant", None), ("le 8 décembre.", None)]),
 ("Envoie-moi HELLO en privé, je t'envoie le lien.", [("Envoie-moi", None), ("HELLO", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 1.93), (2.34, 5.80), (6.28, 10.03), (10.31, 14.28), (14.63, 15.92), (16.35, 17.93), (18.33, 19.86)]
GSTART = [[0.1, 0.8, 1.1], [2.36, 3.1, 4.2, 5.2], [6.3, 7.0, 7.9, 9.2], [10.35, 11.35, 11.75, 13.15, 13.75], [14.66, 15.18], [16.38, 16.98, 17.38], [18.33, 18.78, 18.88, 19.38]]
MINLEN = 1.9
GAP = 0.34
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.tq{color:#45dccd;text-shadow:0 0 18px rgba(69,220,205,.45)}
.steps{position:absolute;left:190px;top:640px;width:700px;height:90px}
.steps .bar{position:absolute;left:45px;top:41px;width:610px;height:8px;border-radius:4px;background:rgba(255,255,255,.12)}
.steps .fill{position:absolute;left:45px;top:41px;height:8px;border-radius:4px;background:linear-gradient(90deg,#45dccd,#f3c766);transform-origin:0 50%}
.steps .d{position:absolute;top:0;width:90px;height:90px;border-radius:50%;border:5px solid #3a4644;background:#0b0f0e;font:900 40px Inter;color:#7f8c89;display:flex;align-items:center;justify-content:center}
.steps .d.on{border-color:#45dccd;color:#06120f;background:#45dccd;box-shadow:0 0 30px rgba(69,220,205,.5)}
.steps .d.done{border-color:#f3c766;background:#f3c766;color:#1a1408}
.ck{position:absolute;left:170px;top:860px;width:740px;border-radius:30px;background:#0d1312;border:4px solid rgba(69,220,205,.7);box-shadow:0 30px 80px rgba(0,0,0,.7);padding:24px 40px}
.ck .r{display:flex;align-items:center;gap:26px;height:110px;border-bottom:2px dashed rgba(69,220,205,.25);font:800 38px Inter;color:#e9e4da;white-space:nowrap}
.ck .r:last-child{border:0}
.ck .b{flex:none;width:62px;height:62px;border-radius:16px;border:5px solid #45dccd}
.ck .r span{flex:1}.ck .r em{font:900 40px 'DejaVu Serif',serif;color:#f3c766;font-style:normal}
.ph{position:absolute;left:300px;top:780px;width:480px;height:520px;border-radius:60px;background:#0b0f0e;border:10px solid #2c3331;box-shadow:0 0 0 2px #4d5a57,0 30px 90px rgba(0,0,0,.7);padding:30px 34px;transform:rotate(-3deg)}
.ph .nt{width:130px;height:30px;background:#000;border-radius:0 0 18px 18px;margin:-30px auto 26px}
.ph .t{font:800 26px Inter;letter-spacing:5px;color:#45dccd;text-align:center;margin-bottom:26px}
.opt{height:150px;border-radius:26px;border:4px solid #3a4644;margin-bottom:22px;padding:24px 28px;font:900 40px Inter;color:#e9e4da;position:relative;white-space:nowrap}
.opt small{display:block;font:600 24px Inter;color:#8f9a97;margin-top:8px;letter-spacing:1px}
.opt.sel{border-color:#45dccd;background:rgba(69,220,205,.10)}
.opt i{position:absolute;right:26px;top:48px;width:50px;height:50px;border-radius:50%;border:5px solid #45dccd}
.opt.sel i{background:radial-gradient(circle,#45dccd 45%,transparent 50%)}
.stmp{position:absolute;padding:16px 36px;border-radius:22px;border:6px solid #f3c766;font:900 92px 'DejaVu Serif',serif;color:#f3c766;background:rgba(20,16,8,.85);transform:rotate(-8deg);white-space:nowrap;box-shadow:0 20px 60px rgba(0,0,0,.6)}
.mo{position:absolute;left:190px;top:800px;width:700px;border-radius:30px;background:#f2efe7;color:#16201e;padding:26px 30px 34px;box-shadow:0 40px 90px rgba(0,0,0,.7)}
.mo .h{font:900 34px Inter;letter-spacing:6px;text-align:center;color:#0f6f66;margin-bottom:18px}
.mo .g{display:grid;grid-template-columns:repeat(7,1fr);gap:12px}
.mo .g i{height:66px;border-radius:12px;background:#dcd7cb;font:700 24px 'DejaVu Sans Mono',monospace;color:#7a766b;font-style:normal;display:flex;align-items:center;justify-content:center}
.mo .g i.p{background:#45dccd;color:#06120f;font-weight:900}
.bk{position:absolute;top:900px;width:220px;height:240px;text-align:center}
.bk .roof{width:0;height:0;margin:0 auto;border-left:110px solid transparent;border-right:110px solid transparent;border-bottom:70px solid #6f7a77}
.bk .cols{height:150px;background:repeating-linear-gradient(90deg,#6f7a77 0 26px,transparent 26px 46px);margin:10px 12px 0}
.bk .base{height:20px;background:#6f7a77;margin-top:6px}
.bk.on .roof{border-bottom-color:#45dccd}.bk.on .cols{background:repeating-linear-gradient(90deg,#45dccd 0 26px,transparent 26px 46px)}.bk.on .base{background:#45dccd}
.bk small{display:block;font:800 26px Inter;letter-spacing:3px;color:#e9e4da;margin-top:16px}
.arw{position:absolute;left:420px;top:980px;width:240px;height:10px;background:#f3c766;transform-origin:0 50%;border-radius:5px}
.arw:after{content:'';position:absolute;right:-18px;top:-16px;border:21px solid transparent;border-left:26px solid #f3c766;border-right:0}
.vch{position:absolute;left:200px;top:1250px;width:680px;height:250px;border-radius:24px;background:linear-gradient(120deg,#f6dc8e,#d6a347 55%,#a87228);color:#2a1a05;box-shadow:0 30px 80px rgba(0,0,0,.7);transform:rotate(3deg);overflow:hidden}
.vch:before,.vch:after{content:'';position:absolute;top:100px;width:50px;height:50px;border-radius:50%;background:#07060a}
.vch:before{left:-25px}.vch:after{right:-25px}
.vch .k{position:absolute;left:50px;top:36px;font:800 28px 'DejaVu Sans Mono',monospace;letter-spacing:6px}
.vch .a{position:absolute;left:50px;top:80px;font:900 120px 'DejaVu Serif',serif;line-height:1.1}
.vch .s{position:absolute;right:50px;top:36px;font:800 24px Inter;letter-spacing:3px;text-align:right}
.tk{position:absolute;left:250px;top:880px;width:580px;background:#f8f6f1;color:#1f1d1a;padding:40px 44px 60px;font:600 34px 'DejaVu Sans Mono',monospace;line-height:1.7;transform:rotate(-3deg);box-shadow:0 30px 80px rgba(0,0,0,.6)}
.tk .row{display:flex;justify-content:space-between;white-space:nowrap}
.tk hr{border:0;border-top:3px dashed #999;margin:12px 0}
.tk .t{font:800 30px Inter;letter-spacing:6px;text-align:center;color:#0f6f66}
.sg{position:absolute;left:390px;top:780px;width:300px;height:480px}
.jtag{position:absolute;left:640px;top:1140px;padding:18px 34px;border-radius:20px;background:#45dccd;color:#06120f;font:900 64px 'DejaVu Sans Mono',monospace;transform:rotate(-8deg);box-shadow:0 20px 50px rgba(0,0,0,.6)}
.dt{position:absolute;left:0;top:1320px;width:1080px;text-align:center;font:800 34px Inter;letter-spacing:4px;color:#e9e4da}
'''


def steps(cur, gfill=None):
    w = {1: 0, 2: 305, 3: 610}[cur]
    fill = f'<div class="fill" style="width:{max(w, 1)}px"' + (f' data-g="{gfill}" data-fx="grow"' if gfill else '') + '></div>'
    ds = ''.join(f'<div class="d {"done" if k < cur else ("on" if k == cur else "")}" style="left:{(k - 1) * 305}px">{"✓" if k < cur else k}</div>' for k in (1, 2, 3))
    return f'<div class="steps"><div class="bar"></div>{fill}{ds}</div>'


SAND = '''<svg class="sg" data-g="5.0" data-fx="pop" viewBox="0 0 300 480" width="300" height="480">
 <rect x="20" y="0" width="260" height="30" rx="10" fill="#f3c766"/><rect x="20" y="450" width="260" height="30" rx="10" fill="#f3c766"/>
 <path d="M50 30 L250 30 Q250 160 160 240 Q250 320 250 450 L50 450 Q50 320 140 240 Q50 160 50 30 Z" fill="rgba(69,220,205,.08)" stroke="#45dccd" stroke-width="8"/>
 <path d="M85 110 L215 110 Q200 170 150 215 Q100 170 85 110 Z" fill="#f3c766"/>
 <path d="M70 445 Q150 330 230 445 Z" fill="#f3c766"/>
 <rect x="146" y="225" width="8" height="200" fill="#f3c766"/>
</svg>'''

BODY = hud('FRANCE · BANQUE EN LIGNE', 'CHECKLIST') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(210, [('h1 tq', 'HELLO BANK LÂCHE', None, 'font-size:80px'), ('it gold', "jusqu'à", None, 'font-size:80px'), ('big gold', '330 €', None, 'font-size:180px')]) + '''
   <div class="ck" style="top:820px"><div class="r"><div class="b"></div><span>Ouvrir le compte</span><em>?</em></div><div class="r"><div class="b"></div><span>Payer avec la carte</span><em>?</em></div><div class="r"><div class="b"></div><span>Mobilité bancaire</span><em>?</em></div></div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1 tq', 'ÉTAPE 1 :', '1.0', ''), ('it gold', 'tu ouvres Hello One', '1.1', 'font-size:70px'), ('it gold', 'ou Hello Prime.', '1.2', 'font-size:70px')]) + steps(1) + '''
   <div class="ph" data-g="1.1" data-fx="up"><div class="nt"></div><div class="t">CHOISIS TON OFFRE</div>
    <div class="opt sel">HELLO ONE<small>offre d'entrée</small><i></i></div><div class="opt" data-g="1.2" data-fx="pop" style="border-color:#45dccd">HELLO PRIME<small>sous conditions</small><i></i></div></div>
   <div class="stmp" style="left:560px;top:1330px" data-g="1.3" data-fx="stamp">+80 €</div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 tq', 'ÉTAPE 2 :', '2.0', ''), ('it gold', 'avec Hello Prime,', '2.1', 'font-size:72px'), ('it gold', '5 paiements par mois.', '2.2', 'font-size:68px')]) + steps(2, '2.0') + '''
   <div class="mo" data-g="2.1" data-fx="up"><div class="h">CE MOIS-CI</div><div class="g">''' + ''.join(
    f'<i class="p" data-g="2.2" data-fx="pop">{d}</i>' if d in (3, 9, 14, 21, 27) else f'<i>{d}</i>' for d in range(1, 29)) + '''</div></div>
   <div class="stmp" style="left:560px;top:1300px" data-g="2.3" data-fx="stamp">+50 €</div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('h1 tq', 'DERNIÈRE ÉTAPE :', '3.0', 'font-size:70px'), ('it gold', 'tu actives', '3.1', 'font-size:72px'), ('it gold', 'la mobilité bancaire.', '3.2', 'font-size:68px')]) + steps(3, '3.0') + '''
   <div class="bk" style="left:170px"><div class="roof"></div><div class="cols"></div><div class="base"></div><small>AVANT</small></div>
   <div class="arw" data-g="3.2" data-fx="grow"></div>
   <div class="bk on" style="left:690px" data-g="3.2" data-fx="pop"><div class="roof"></div><div class="cols"></div><div class="base"></div><small>HELLO BANK</small></div>
   <div class="vch" data-g="3.3" data-fx="up"><div class="k">BON D'ACHAT</div><div class="a" data-g="3.4" data-fx="tick">200 €</div><div class="s">HELLO START +<br>MOBILITÉ BANCAIRE</div></div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:430px"></div>''' + hd(230, [('h1', "ÇA FAIT JUSQU'À", '4.0', '')]) + '''
   <div class="abs" style="left:0;top:380px;width:1080px;text-align:center" data-g="4.1" data-fx="stamp" data-slow="4.1" data-count="330" data-suf=" €"><div class="v gold" style="font:900 220px 'DejaVu Serif',serif;line-height:1.2">0 €</div></div>
   <div class="tk" data-g="4.0" data-fx="up"><div class="t">HELLO BANK · TICKET</div><hr><div class="row"><span>Ouverture</span><span>80 €</span></div><div class="row"><span>Hello Prime</span><span>50 €</span></div><div class="row"><span>Bon d'achat</span><span>200 €</span></div><hr><div class="row" style="font-weight:900"><span>TOTAL</span><span>330 €</span></div></div></div>
  <div class="scene" data-s="5" data-in="up">''' + hd(230, [('h1 tq', 'TA DEMANDE EN LIGNE,', '5.0', 'font-size:68px'), ('it gold', "c'est avant", '5.1', 'font-size:76px'), ('it gold', 'le 8 décembre.', '5.2', 'font-size:76px')]) + '''
   ''' + SAND + '''
   <div class="jtag" data-g="5.2" data-fx="stamp">J-21</div>
   <div class="dt" data-g="5.2" data-fx="fade">AUJOURD'HUI 17/11 → LIMITE 08/12</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« HELLO »', '6.1', 'font-size:130px'), ('it gold', 'en privé,', '6.2', '')]) + '''
   <div class="pill" style="top:740px;border-color:rgba(69,220,205,.8)" data-g="6.3" data-fx="up"><div class="pin" style="background:#45dccd">✉</div><div><b>JE T'ENVOIE LE LIEN</b><span>demande en ligne avant le 8 décembre</span></div></div>
   <div class="cond" style="top:900px">Offre soumise aux conditions en vigueur · jusqu'à 330 €<br>80 € à l'ouverture (Hello One ou Hello Prime)<br>+ 50 € avec Hello Prime (5 paiements ou retraits / mois, 12 mois)<br>+ bon d'achat 200 € (Hello Start+, mobilité bancaire) · nouveaux clients<br>jusqu'au 08/12/2026 inclus</div></div>
'''
