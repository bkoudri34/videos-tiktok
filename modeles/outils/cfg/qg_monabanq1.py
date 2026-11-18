import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Vidéos QG, 18/11/2026, vidéo 1 : Monabanq. Style v3 nuit & or, accent bleu glacier. Format F3 « anti-arnaque / confiance » :
# « 280 € ? Voilà le vrai calcul » -> ticket « prime annoncée 280 € / à vérifier » dès la 1re image -> relevé qui se remplit étape par étape
# (20 + 60 + 60 + 80 + 60) -> total 280 € tamponné (ralenti) -> appel à l'action.
# Offre : monabanq.com/fr/parrainage.html consulté le 18/11/2026 (offre de bienvenue filleul « jusqu'à 280 € », valable depuis le 01/07/2026).
# Voix : Speko (speechify simba-3.5, voix par défaut, ElevenLabs/voix-htm-luxe refusé : 402 top-up), speed 1.08.
NAME = 'qg_monabanq1'
TITLE = 'QG Monabanq vrai calcul'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Parrainage Monabanq : deux cent quatre-vingts euros ? Voilà le vrai calcul.", [("Parrainage Monabanq :", None), ("280 € ?", None), ("Voilà le vrai calcul.", None)]),
 ("Vingt euros à l'ouverture, et soixante si tu verses trois cents euros le premier mois.", [("20 €", None), ("à l'ouverture,", None), ("et 60", None), ("si tu verses 300 €", None), ("le 1er mois.", None)]),
 ("Soixante de plus après trente paiements carte en deux mois.", [("60 de plus", None), ("après 30 paiements carte", None), ("en 2 mois.", None)]),
 ("Quatre-vingts avec le transfert de tes prélèvements.", [("80 €", None), ("avec le transfert", None), ("de tes prélèvements.", None)]),
 ("Et soixante au treizième mois, avec deux autres produits, dont une épargne.", [("Et 60", None), ("au 13e mois,", None), ("avec 2 autres produits,", None), ("dont une épargne.", None)]),
 ("Envoie-moi MONABANQ en privé, je t'envoie l'invitation.", [("Envoie-moi", None), ("MONABANQ", None), ("en privé,", None), ("je t'envoie l'invitation.", None)]),
]
SPLITS = [(0.0, 3.49), (3.87, 7.41), (7.83, 10.01), (10.38, 12.23), (12.65, 15.46), (16.0, 18.2)]
GSTART = [[0.0, 1.25, 2.64], [3.87, 4.4, 5.26, 5.8, 6.9], [7.83, 8.6, 9.6], [10.38, 10.9, 11.6], [12.65, 13.0, 13.8, 14.9], [16.0, 16.3, 16.8, 17.3]]
MINLEN = 2.0
GAP = 0.42
TAIL = 2.6


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.bl{color:#8fd3ff;text-shadow:0 0 18px rgba(120,200,255,.55)}
.tick{position:absolute;left:200px;top:860px;width:680px;height:470px;border-radius:28px;background:#f5f1e8;color:#1a1814;text-align:center;padding-top:50px;transform:rotate(-3deg);box-shadow:0 30px 90px rgba(0,0,0,.65)}
.tick .k{font:800 34px Inter;letter-spacing:6px;color:#6b665e}
.tick .v{font:900 190px 'DejaVu Serif',serif;color:#1a1814;line-height:1.15}
.tick .q{font:700 34px 'DejaVu Sans Mono';color:#8a847a;letter-spacing:3px}
.stampx{position:absolute;left:560px;top:1200px;padding:14px 30px;border:7px solid #e0453a;color:#e0453a;font:900 50px Inter;letter-spacing:3px;transform:rotate(-12deg);border-radius:14px;background:rgba(245,241,232,.85);white-space:nowrap}
.mag{position:absolute;left:110px;top:1130px;width:210px;height:210px;border-radius:50%;border:16px solid #d9a24c;background:rgba(143,211,255,.12);box-shadow:0 0 40px rgba(240,180,80,.35)}
.mag:after{content:'';position:absolute;left:150px;top:170px;width:34px;height:150px;border-radius:14px;background:#8a6428;transform:rotate(-45deg);transform-origin:50% 0}
.led{position:absolute;left:110px;top:560px;width:860px;height:760px;border-radius:30px;background:#f6f2ea;color:#1b1915;padding:34px 40px;box-shadow:0 30px 90px rgba(0,0,0,.6)}
.led .t{font:800 30px Inter;letter-spacing:5px;color:#7a7368;text-align:center;margin-bottom:18px}
.row{display:flex;justify-content:space-between;align-items:center;height:104px;border-bottom:3px dashed #cfc7b8;white-space:nowrap}
.row .n{display:inline-block;width:52px;height:52px;border-radius:50%;background:#1b2a36;color:#8fd3ff;font:900 30px Inter;text-align:center;line-height:52px;margin-right:18px}
.row span{font:700 38px Inter}
.row small{display:block;font:500 24px Inter;color:#7a7368;margin-left:70px;margin-top:-4px}
.row b{font:900 52px 'DejaVu Serif',serif;color:#1d5f8f}
.tot{position:absolute;left:40px;right:40px;bottom:26px;display:flex;justify-content:space-between;align-items:center;font:900 44px Inter;letter-spacing:3px}
.tot b{font:900 96px 'DejaVu Serif',serif;color:#9a5d10}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'


def row(n, lab, sub, amt, g):
    return f'<div class="row" data-g="{g}" data-fx="left"><div><span><i class="n" style="font-style:normal">{n}</i>{lab}</span><small>{sub}</small></div><b>{amt}</b></div>'


LEDGER = '''<div class="led"><div class="t">LE VRAI CALCUL</div>''' + \
    row(1, 'Ouverture du compte', 'versés le 16 du mois suivant', '20 €', '1.1') + \
    row(2, '300 € versés', 'dans le mois suivant l\'ouverture', '60 €', '1.3') + \
    row(3, '30 paiements carte', 'dans les 2 mois', '60 €', '2.1') + \
    row(4, 'Mobilité bancaire', 'transfert de tes prélèvements', '80 €', '3.1') + \
    row(5, 'Fidélité au 13e mois', '+ 2 autres produits dont 1 épargne', '60 €', '4.2') + \
    '''<div class="tot" data-g="4.3" data-fx="stamp" data-slow="4.3"><span>TOTAL</span><b>280 €</b></div></div>'''

BODY = hud('FRANCE · MONABANQ', 'VRAI CALCUL') + '''
  <div class="scene" data-s="0">''' + hd(215, [('h1', 'PARRAINAGE MONABANQ', None, 'font-size:66px'), ('big gold', '280 € ?', None, 'font-size:170px'), ('it bl', 'voilà le vrai calcul', None, 'font-size:66px')]) + '''
   <div class="tick" style="top:780px"><div class="k">PRIME ANNONCÉE</div><div class="v">280 €</div><div class="q">= ? + ? + ? + ?</div></div>
   <div class="mag"></div>
   <div class="stampx" style="top:1150px">À VÉRIFIER</div></div>
  <div class="scene" data-s="1-4" data-in="up">''' + LEDGER + '''</div>
  <div class="scene" data-s="1" data-in="right">''' + hd(260, [('h1', 'ÉTAPES 1 ET 2', '1.0', 'font-size:64px'), ('it bl', "l'ouverture, puis 300 € versés", '1.2', 'font-size:58px')]) + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + hd(260, [('h1', 'ÉTAPE 3', '2.0', 'font-size:64px'), ('it bl', '30 paiements carte en 2 mois', '2.1', 'font-size:58px')]) + '''</div>
  <div class="scene" data-s="3" data-in="right">''' + hd(260, [('h1', 'ÉTAPE 4', '3.0', 'font-size:64px'), ('it bl', 'le transfert de tes prélèvements', '3.1', 'font-size:56px')]) + '''</div>
  <div class="scene" data-s="4" data-in="right">''' + hd(260, [('h1', 'ÉTAPE 5', '4.0', 'font-size:64px'), ('it bl', 'le 13e mois, avec 2 autres produits', '4.1', 'font-size:54px')]) + '''</div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« MONABANQ »', '5.1', 'font-size:104px'), ('it gold', 'en privé', '5.2', '')]) + '''
   <div class="pill" style="top:760px;border-color:rgba(143,211,255,.85)" data-g="5.3" data-fx="up"><div class="pin" style="background:#8fd3ff;color:#0b1a26">✉</div><div><b>JE T'ENVOIE L'INVITATION</b><span>jusqu'à 280 € · en 5 étapes</span></div></div>
   <div class="search" style="top:900px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1040px;left:70px;width:940px;font-size:25px">Offre soumise aux conditions en vigueur · offre de bienvenue Monabanq<br>pour une 1re ouverture de compte courant (via le lien d'invitation) :<br>20 € à l'ouverture + 60 € si 300 € versés le mois suivant + 60 € après<br>30 paiements carte en 2 mois + 80 € mobilité bancaire + 60 € au 13e mois<br>(2 autres produits dont 1 épargne) · primes reprises si clôture sous 12 mois</div></div>
'''
