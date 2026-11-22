import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Fortuneo, 22/11/2026 21:00 - style v3 nuit & or, accent bleu roi. Format F9 « duel / comparatif » :
# duel Fosfo VS Gold dès la 1re image -> Fosfo : 80 € pour le filleul -> Gold : 150 € (ralenti) -> condition : le filleul dépose 300 €
# dans les 6 jours -> calendrier « jusqu'au 30/11 » -> appel à l'action + tableau des scores Fosfo 80 € / Gold 150 € (reboucle sur le duel).
# Offre de parrainage Fortuneo (fortuneo.fr/parrainage, consultée le 22/11/2026) : du 01/11 au 30/11/2026, filleul 80 € avec Fosfo,
# 150 € avec Gold CB Mastercard, code parrain, versement initial de 300 € dans les 6 jours suivant l'ouverture, compte et carte gardés 1 an,
# non cumulable avec une autre offre ; prime versée au plus tard le 31/12/2026.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'fortuneo13'
TITLE = 'Fortuneo duel bleu roi'
ROOT = ':root{--bg:#05060d}'
LINES = [
 ("Parrainage Fortunéo : Fosfo ou Gold, laquelle choisir ?", [("Parrainage Fortuneo :", None), ("Fosfo ou Gold,", None), ("laquelle choisir ?", None)]),
 ("Avec la carte Fosfo, le filleul touche quatre-vingts euros.", [("Avec la carte Fosfo,", None), ("le filleul touche", None), ("80 €.", None)]),
 ("Avec la Gold, c'est cent cinquante euros.", [("Avec la Gold,", None), ("c'est 150 €.", None)]),
 ("Condition : tu déposes trois cents euros sur ton compte, dans les six jours.", [("Condition :", None), ("tu déposes 300 €", None), ("sur ton compte,", None), ("dans les 6 jours.", None)]),
 ("Et c'est valable jusqu'au trente novembre.", [("Et c'est valable", None), ("jusqu'au 30 novembre.", None)]),
 ("Envoie-moi FORTUNÉO en privé, je t'envoie mon code parrain.", [("Envoie-moi", None), ("FORTUNEO", None), ("en privé,", None), ("je t'envoie mon code parrain.", None)]),
]
SPLITS = [(0.0, 3.17), (3.92, 6.53), (7.22, 8.74), (9.48, 12.05), (12.71, 13.98), (14.52, 16.6)]
GSTART = [[0.0, 1.4, 2.5], [3.92, 5.1, 5.9], [7.22, 7.9], [9.48, 9.9, 10.9, 11.5], [12.71, 13.2], [14.52, 14.8, 15.3, 15.7]]
MINLEN = 2.0
GAP = 0.3
TAIL = 2.4


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.rb{color:#7ea2ff;text-shadow:0 0 18px rgba(90,130,255,.55)}
.cd{position:absolute;width:340px;height:214px;border-radius:22px;box-shadow:0 30px 80px rgba(0,0,0,.7)}
.cd .chip{position:absolute;left:30px;top:78px;width:60px;height:46px;border-radius:9px;background:linear-gradient(135deg,#f6f1e7,#bfa98a)}
.cd .k{position:absolute;left:30px;top:24px;font:800 24px 'DejaVu Sans Mono',monospace;letter-spacing:4px}
.cd .n{position:absolute;left:30px;top:156px;font:700 22px 'DejaVu Sans Mono',monospace;letter-spacing:3px}
.fos{background:linear-gradient(135deg,#3a3f4f,#1b1e27 60%,#0e1016);border:3px solid #5b6275;color:#d8dbe6}
.gld{background:linear-gradient(135deg,#fff1c4,#e9b456 45%,#a8701f);color:#3a2810}
.vs{position:absolute;left:470px;width:140px;height:140px;border-radius:50%;background:#2747c9;border:6px solid #a9bfff;display:flex;align-items:center;justify-content:center;font:900 58px Inter;color:#fff;box-shadow:0 0 50px rgba(80,120,255,.6)}
.qm{position:absolute;left:0;width:1080px;text-align:center;font:900 150px 'DejaVu Serif',serif;color:#7ea2ff;text-shadow:0 0 30px rgba(90,130,255,.6)}
.tag{position:absolute;left:290px;width:500px;height:210px;border-radius:30px;background:#f2f4fb;color:#0e1638;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 20px 60px rgba(0,0,0,.6),0 0 0 5px rgba(90,130,255,.6)}
.tag b{font:900 124px 'DejaVu Serif',serif;line-height:1}
.tag small{font:800 26px Inter;color:#4b5680;letter-spacing:3px;white-space:nowrap}
.tag.g{background:linear-gradient(180deg,#2a1d0c,#120c05);border:5px solid #e9b456;color:#ffe9c0;box-shadow:0 0 60px rgba(240,180,80,.4)}
.tag.g small{color:#e8c98f}
.tline{position:absolute;left:215px;width:630px;height:6px;background:#2b3a6a}
.dot{position:absolute;width:170px;text-align:center;font:800 28px Inter;color:#c9d4f5;white-space:nowrap}
.dot i{display:block;margin:0 auto 18px;width:56px;height:56px;border-radius:50%;background:#0e1430;border:6px solid #7ea2ff}
.dot.on i{background:#7ea2ff}
.dep{position:absolute;left:260px;width:560px;height:150px;border-radius:34px;background:#0c1230;border:4px solid #7ea2ff;display:flex;align-items:center;justify-content:center;gap:24px;white-space:nowrap}
.dep b{font:900 84px 'DejaVu Serif',serif;color:#fff}
.dep span{font:800 28px Inter;color:#a9bfff;letter-spacing:2px;line-height:1.3}
.calp{position:absolute;left:370px;width:340px;height:360px;border-radius:30px;background:#f2f4fb;overflow:hidden;text-align:center;box-shadow:0 30px 80px rgba(0,0,0,.7)}
.calp .h{height:90px;background:#2747c9;color:#fff;font:900 46px Inter;letter-spacing:6px;display:flex;align-items:center;justify-content:center}
.calp b{display:block;font:900 200px 'DejaVu Serif',serif;color:#0e1638;line-height:1.25}
.sc{position:absolute;left:170px;width:740px;display:flex;gap:20px}
.sc .c{flex:1;height:120px;border-radius:28px;display:flex;align-items:center;justify-content:space-between;padding:0 30px;font:800 34px Inter;white-space:nowrap}
.sc .c b{font:900 52px 'DejaVu Serif',serif}
.sc .f{background:#15161c;border:4px solid #3d4150;color:#b8bccb}
.sc .gg{background:#1d150a;border:4px solid #e9b456;color:#ffe9c0}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'


def card(cls, left, top, rot, label, g=None, fx='pop'):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    return f'<div class="cd {cls}" style="left:{left}px;top:{top}px;transform:rotate({rot}deg)"{a}><div class="k">{label}</div><div class="chip"></div><div class="n">•••• 2026</div></div>'


BODY = hud('FRANCE · LE DUEL', 'FORTUNEO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(205, [('h1', 'PARRAINAGE', None, 'font-size:72px'), ('h1 rb', 'FORTUNEO :', None, 'font-size:86px'), ('it gold', 'Fosfo ou Gold ?', None, 'font-size:80px')]) + '''
   ''' + card('fos', 140, 760, -7, 'FOSFO') + card('gld', 600, 760, 7, 'GOLD') + '''
   <div class="vs" style="top:800px" data-g="0.1" data-fx="stamp">VS</div>
   <div class="qm" style="top:1030px" data-g="0.2" data-fx="pop">?</div></div>
  <div class="scene" data-s="1" data-in="left">''' + hd(230, [('it gold', 'Avec la carte Fosfo,', '1.0', 'font-size:76px'), ('h1', 'LE FILLEUL TOUCHE', '1.1', 'font-size:60px')]) + '''
   ''' + card('fos', 370, 600, -4, 'FOSFO', '1.0', 'left') + '''
   <div class="tag" style="top:900px" data-g="1.2" data-fx="stamp"><b>80 €</b><small>PRIME FILLEUL · FOSFO</small></div></div>
  <div class="scene" data-s="2" data-in="right"><div class="rays" style="top:780px"></div>''' + hd(230, [('it gold', 'Avec la Gold,', '2.0', 'font-size:80px'), ('big gold', "c'est 150 €.", '2.1', 'font-size:110px')]) + '''
   ''' + card('gld', 370, 620, 4, 'GOLD', '2.0', 'right') + '''
   <div class="tag g" style="top:910px" data-g="2.1" data-fx="stamp" data-slow="2.1" data-count="150"><b class="v gold">0 €</b><small>PRIME FILLEUL · GOLD</small></div></div>
  <div class="scene" data-s="3" data-in="up">''' + hd(230, [('h1 rb', 'CONDITION :', '3.0', 'font-size:70px'), ('it gold', 'tu déposes 300 €', '3.1', 'font-size:76px'), ('it gold', 'sur ton compte,', '3.2', 'font-size:72px')]) + '''
   <div class="dep" style="top:640px" data-g="3.1" data-fx="pop"><b>300 €</b><span>À DÉPOSER<br>PAR TOI</span></div>
   <div class="tline" style="top:952px" data-g="3.2" data-fx="grow"></div>
   <div class="dot on" style="left:130px;top:925px" data-g="3.2" data-fx="pop"><i></i>OUVERTURE</div>
   <div class="dot on" style="left:760px;top:925px" data-g="3.3" data-fx="pop"><i></i>JOUR 6</div>
   <div class="hd" style="top:1090px"><div class="it rb" style="font-size:64px" data-g="3.3" data-fx="tw">dans les 6 jours.</div></div></div>
  <div class="scene" data-s="4" data-in="pop">''' + hd(230, [('it gold', "Et c'est valable", '4.0', 'font-size:76px'), ('h1 rb', "JUSQU'AU 30 NOVEMBRE.", '4.1', 'font-size:56px')]) + '''
   <div class="calp" style="top:560px" data-g="4.1" data-fx="stamp"><div class="h">NOV.</div><b>30</b></div>
   <div class="cond" style="top:960px;font-size:28px;color:#9fb0dd" data-g="4.1" data-fx="fade">offre de parrainage du 01/11 au 30/11/2026</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« FORTUNEO »', '5.1', 'font-size:86px'), ('it rb', 'en privé,', '5.2', '')]) + '''
   <div class="pill" style="top:650px;border-color:rgba(126,162,255,.85)" data-g="5.3" data-fx="up"><div class="pin" style="background:#2747c9;color:#fff">✉</div><div><b>JE T'ENVOIE MON CODE</b><span>code parrain en message privé</span></div></div>
   <div class="search" style="top:790px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:920px;font-size:22px">Offre soumise aux conditions en vigueur · du 01/11 au 30/11/2026<br>1re ouverture d'un compte Fortuneo avec code parrain · 80 € (Fosfo)<br>ou 150 € (Gold, sous conditions d'éligibilité) · dépôt de 300 € sous 6 jours<br>Compte et carte à garder 1 an · non cumulable avec une autre offre</div>
   <div class="sc" style="top:1130px" data-g="5.3" data-fx="up"><div class="c f">FOSFO<b>80 €</b></div><div class="c gg">GOLD<b class="gold">150 €</b></div></div></div>
'''
