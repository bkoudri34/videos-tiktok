import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# BoursoBank, 15/11/2026 16:00 - style v3 nuit & or, accent violet améthyste. Offre filleul jusqu'à 180 €
# (boursobank.com/bon-plan/parrainage-boursobank, consultée le 15/11/2026, pas de date de fin) :
# 20 € ouverture + jusqu'à 40 € 1er versement (40 € dès 300 €) + jusqu'à 40 € paiements carte sur 3 mois + 80 € mobilité EasyMove.
# Voix : Speko (speechify, voix par défaut ; voix clonée refusée 402).
# Carte « nouveau compte » -> compteur 180 € -> notifications +20 / +40 -> +40 carte 3 mois -> barre de cumul 180 € -> appel à l'action.
NAME = 'bourso10'
TITLE = 'BoursoBank 180 euros violet'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Ouvrir un compte peut te rapporter cent quatre-vingts euros.", [("Ouvrir un compte", None), ("peut te rapporter", None), ("180 €.", None)]),
 ("Chez Bourso Bank, c'est jusqu'à cent quatre-vingts euros pour le filleul.", [("Chez BoursoBank,", None), ("c'est jusqu'à", None), ("180 €", None), ("pour le filleul.", None)]),
 ("Vingt euros à l'ouverture. Jusqu'à quarante au premier versement.", [("20 €", None), ("à l'ouverture.", None), ("Jusqu'à 40", None), ("au premier versement.", None)]),
 ("Jusqu'à quarante de plus avec ta carte, sur trois mois.", [("Jusqu'à 40 de plus", None), ("avec ta carte,", None), ("sur 3 mois.", None)]),
 ("Et quatre-vingts euros avec le transfert EasyMove.", [("Et 80 €", None), ("avec le transfert", None), ("EasyMove.", None)]),
 ("Envoie-moi BOURSO en privé, je t'envoie mon lien.", [("Envoie-moi", None), ("BOURSO", None), ("en privé,", None), ("je t'envoie mon lien.", None)]),
]
SPLITS = [(0.0, 2.22), (2.78, 5.38), (5.84, 8.42), (8.95, 11.19), (11.94, 13.89), (14.34, 16.18)]
GSTART = [[0.1, 0.7, 1.3], [2.8, 3.7, 4.0, 4.8], [5.84, 6.2, 7.1, 7.7], [9.0, 9.9, 10.7], [11.96, 12.7, 13.5], [14.34, 14.6, 14.9, 15.5]]
MINLEN = 2.1
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
.vi{color:#b98cff;text-shadow:0 0 18px rgba(185,140,255,.45)}
.nc{position:absolute;left:250px;top:860px;width:580px;height:360px;border-radius:30px;background:linear-gradient(135deg,#3a2560,#1a1030 60%,#120b20);border:4px solid #d9a24c;box-shadow:0 40px 90px rgba(0,0,0,.7);transform:rotate(-6deg)}
.nc .chip{position:absolute;left:50px;top:120px;width:92px;height:70px;border-radius:12px;background:linear-gradient(135deg,#fff1c4,#d9a24c)}
.nc .k{position:absolute;left:50px;top:44px;font:800 26px 'DejaVu Sans Mono',monospace;letter-spacing:6px;color:#e6dcff}
.nc .n{position:absolute;left:50px;top:240px;font:700 34px 'DejaVu Sans Mono',monospace;letter-spacing:4px;color:#e6dcff}
.qm{position:absolute;left:690px;top:800px;width:150px;height:150px;border-radius:50%;background:#b98cff;color:#1a0f2e;font:900 100px Inter;display:flex;align-items:center;justify-content:center;box-shadow:0 20px 50px rgba(0,0,0,.6)}
.nt{position:absolute;left:130px;width:780px;height:150px;border-radius:30px;background:rgba(246,242,255,.97);color:#1a1226;display:flex;align-items:center;gap:24px;padding:0 30px;box-sizing:border-box;box-shadow:0 26px 70px rgba(0,0,0,.6);white-space:nowrap}
.nt .ic{flex:none;width:84px;height:84px;border-radius:22px;background:#7b4fd6;color:#fff;font:900 46px Inter;display:flex;align-items:center;justify-content:center}
.nt .x{flex:1}
.nt .x b{display:block;font:800 32px Inter}
.nt .x span{font:600 24px Inter;color:#6b6380}
.nt .a{font:900 58px 'DejaVu Serif',serif;color:#6a3fc9}
.nt.dim{opacity:.55 !important}
.mo{display:flex;gap:16px;justify-content:center}
.mo div{width:170px;height:64px;border-radius:32px;border:3px solid #b98cff;font:800 26px Inter;color:#b98cff;display:flex;align-items:center;justify-content:center}
.bar{position:absolute;left:150px;top:1040px;width:760px;height:80px;border-radius:40px;background:rgba(255,255,255,.08);border:3px solid rgba(217,162,76,.6);overflow:hidden;display:flex}
.bar i{transform-origin:0 50%;display:block;height:100%;font:800 26px Inter;color:#1a0f2e;display:flex;align-items:center;justify-content:center;font-style:normal;border-right:3px solid #07060a}
.bl2{position:absolute;left:150px;top:1140px;width:760px;display:flex;font:700 22px Inter;color:#c9bfe6;letter-spacing:1px}
.bl2 span{text-align:center}
.tot{position:absolute;left:0;top:1230px;width:1080px;text-align:center;font:900 76px 'DejaVu Serif',serif}
'''

N1 = '<div class="nt" style="top:{top}px"{g}><div class="ic">€</div><div class="x"><b>{t}</b><span>{s}</span></div><div class="a">{a}</div></div>'


def nt(top, t, s, a, g=None, fx='right', extra=''):
    ga = f' data-g="{g}" data-fx="{fx}"' if g else ''
    return N1.format(top=top, g=ga, t=t, s=s, a=a).replace('class="nt"', 'class="nt' + extra + '"', 1)


BODY = hud('FRANCE · BANQUE EN LIGNE', 'BIENVENUE') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('h1', 'OUVRIR UN COMPTE', None, ''), ('it gold', 'peut te rapporter', None, 'font-size:80px'), ('big gold', '180 €', None, 'font-size:150px')]) + '''
   <div class="nc" style="top:900px"><div class="k">NOUVEAU COMPTE</div><div class="chip"></div><div class="n">•••• •••• 2026</div></div>
   <div class="qm" style="top:840px">?</div></div>
  <div class="scene" data-s="1" data-in="pop"><div class="rays" style="top:560px"></div>''' + hd(230, [('h1', 'CHEZ BOURSOBANK,', '1.0', ''), ('it gold', "c'est jusqu'à", '1.1', 'font-size:80px')]) + '''
   <div class="abs" style="left:0;top:700px;width:1080px;text-align:center" data-g="1.2" data-fx="stamp" data-slow="1.2" data-count="180" data-suf=" €"><div class="v gold" style="font:900 200px 'DejaVu Serif',serif;line-height:1.2">0 €</div></div>
   <div class="abs it vi" style="left:0;top:1000px;width:1080px;text-align:center;font-size:76px" data-g="1.3" data-fx="up">pour le filleul.</div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 vi', "20 € À L'OUVERTURE.", '2.0', 'font-size:68px'), ('it gold', "jusqu'à 40", '2.2', 'font-size:76px'), ('it gold', 'au premier versement.', '2.3', 'font-size:66px')]) + \
    nt(720, 'BoursoBank', 'Ouverture du compte', '+20 €', '2.0') + nt(900, 'BoursoBank', '1er versement · 40 € dès 300 €', '+40 €', '2.2') + '''</div>
  <div class="scene" data-s="3" data-in="up">''' + hd(230, [('h1 vi', 'JUSQU\'À 40 DE PLUS', '3.0', 'font-size:70px'), ('it gold', 'avec ta carte,', '3.1', 'font-size:76px'), ('it gold', 'sur 3 mois.', '3.2', 'font-size:76px')]) + \
    nt(620, 'BoursoBank', 'Ouverture du compte', '+20 €', extra=' dim') + nt(790, 'BoursoBank', '1er versement', '+40 €', extra=' dim') + nt(960, 'BoursoBank', 'Paiements carte · 3 mois', '+40 €', '3.1', 'up') + '''
   <div class="mo abs" style="left:0;top:1170px;width:1080px"><div data-g="3.2" data-fx="pop">MOIS 1</div><div data-g="3.2" data-fx="pop">MOIS 2</div><div data-g="3.2" data-fx="pop">MOIS 3</div></div></div>
  <div class="scene" data-s="4" data-in="left">''' + hd(230, [('h1 vi', 'ET 80 €', '4.0', 'font-size:96px'), ('it gold', 'avec le transfert', '4.1', 'font-size:76px'), ('it gold', 'EasyMove.', '4.2', 'font-size:84px')]) + '''
   <div class="bar"><i style="width:84px;background:#d8c4ff" data-g="4.0" data-fx="fade">20</i><i style="width:169px;background:#c4a6ff" data-g="4.0" data-fx="fade">40</i><i style="width:169px;background:#b08cff" data-g="4.0" data-fx="fade">40</i><i style="width:338px;background:linear-gradient(90deg,#f3c766,#d9a24c);border-right:0" data-g="4.1" data-fx="grow">80</i></div>
   <div class="bl2"><span style="width:84px">ouv.</span><span style="width:169px">versement</span><span style="width:169px">carte</span><span style="width:338px">EasyMove</span></div>
   <div class="tot gold" data-g="4.2" data-fx="stamp">= 180 €</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« BOURSO »', '5.1', 'font-size:130px'), ('it gold', 'en privé,', '5.2', '')]) + '''
   <div class="pill" style="top:740px;border-color:rgba(185,140,255,.8)" data-g="5.3" data-fx="up"><div class="pin" style="background:#b98cff">✉</div><div><b>JE T'ENVOIE MON LIEN</b><span>jusqu'à 180 € pour le filleul</span></div></div>
   <div class="cond" style="top:900px">Offre soumise aux conditions en vigueur · jusqu'à 180 €<br>pour le filleul = 20 € à l'ouverture + jusqu'à 40 € au 1er versement<br>(40 € dès 300 €) + jusqu'à 40 € de paiements carte sur 3 mois<br>+ 80 € avec la mobilité EasyMove · compte individuel · nouveaux clients</div></div>
'''
