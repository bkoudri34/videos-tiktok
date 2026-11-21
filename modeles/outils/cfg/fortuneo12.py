import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Fortuneo, 21/11/2026 16:00 - style v3 nuit & or, accent rouge carmin. Format F1 « STOP / erreur à éviter » :
# panneau STOP + 2 cartes retournées « ? » dès la 1re image -> carte Fosfo 50 € -> carte Gold 160 € (5 paiements cochés en 90 jours)
# -> condition revenus 2 200 €/mois OU épargne 10 000 € -> +80 € mobilité / +20 € Livret + -> colonnes Fosfo 150 € vs Gold 260 € (ralenti)
# + avant le 20/12 -> appel à l'action.
# Offre de bienvenue Fortuneo du 02/11 au 20/12/2026 (code FTN1126) : Gold 160 € (revenus >= 2 200 €/mois ou 10 000 € d'épargne),
# Fosfo 50 €, après 5 paiements en 90 jours ; + 80 € mobilité bancaire ; + 20 € ouverture Livret + ; jusqu'à 260 €
# (moneyvox.fr, article du 12/11/2026, consulté le 21/11/2026).
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'fortuneo12'
TITLE = 'Fortuneo STOP carmin'
ROOT = ':root{--bg:#0b0607}'
LINES = [
 ("Stop ! Parrainage Fortunéo : ne choisis pas ta carte au hasard.", [("STOP !", None), ("Parrainage Fortuneo :", None), ("ne choisis pas ta carte", None), ("au hasard.", None)]),
 ("Avec la carte Fosfo, la prime est de cinquante euros.", [("Avec la carte Fosfo,", None), ("la prime est", None), ("de 50 €.", None)]),
 ("Avec la Gold, c'est cent soixante euros, après cinq paiements en quatre-vingt-dix jours.", [("Avec la Gold,", None), ("c'est 160 €,", None), ("après 5 paiements", None), ("en 90 jours.", None)]),
 ("Condition : deux mille deux cents euros de revenus par mois, ou dix mille euros d'épargne.", [("Condition :", None), ("2 200 € de revenus par mois,", None), ("ou 10 000 € d'épargne.", None)]),
 ("Ajoute quatre-vingts euros de mobilité, et vingt euros avec le Livret plus.", [("Ajoute 80 €", None), ("de mobilité,", None), ("et 20 €", None), ("avec le Livret +.", None)]),
 ("Résultat : jusqu'à deux cent soixante euros avec la Gold, avant le vingt décembre.", [("Résultat :", None), ("jusqu'à 260 €", None), ("avec la Gold,", None), ("avant le 20 décembre.", None)]),
 ("Envoie-moi FORTUNÉO en privé, je t'envoie le lien.", [("Envoie-moi", None), ("FORTUNEO", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 3.08), (3.52, 5.77), (6.22, 9.45), (9.99, 13.62), (14.03, 17.22), (17.69, 21.23), (21.73, 23.81)]
GSTART = [[0.0, 0.8, 1.9, 2.8], [3.52, 4.7, 5.2], [6.22, 7.0, 8.1, 8.8], [9.99, 10.84, 12.7], [14.03, 14.9, 15.6, 16.3], [17.69, 18.57, 19.6, 20.5], [21.73, 22.1, 22.5, 23.14]]
MINLEN = 1.9
GAP = 0.3
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.rd{color:#ff5a68;text-shadow:0 0 18px rgba(255,60,80,.55)}
.oct{position:absolute;left:390px;top:600px;width:300px;height:300px;background:#d8202f;clip-path:polygon(30% 0,70% 0,100% 30%,100% 70%,70% 100%,30% 100%,0 70%,0 30%);display:flex;align-items:center;justify-content:center;font:900 92px Inter;color:#fff;letter-spacing:2px;box-shadow:0 0 60px rgba(255,40,60,.5)}
.cd{position:absolute;width:400px;height:252px;border-radius:26px;box-shadow:0 30px 80px rgba(0,0,0,.7)}
.cd .chip{position:absolute;left:36px;top:92px;width:70px;height:54px;border-radius:10px;background:linear-gradient(135deg,#f6f1e7,#bfa98a)}
.cd .k{position:absolute;left:36px;top:28px;font:800 24px 'DejaVu Sans Mono',monospace;letter-spacing:5px}
.cd .n{position:absolute;left:36px;top:184px;font:700 26px 'DejaVu Sans Mono',monospace;letter-spacing:3px}
.cd .q{position:absolute;right:34px;top:60px;font:900 130px 'DejaVu Serif',serif;color:rgba(255,255,255,.85)}
.fos{background:linear-gradient(135deg,#3a3f4f,#1b1e27 60%,#0e1016);border:3px solid #5b6275;color:#d8dbe6}
.gld{background:linear-gradient(135deg,#fff1c4,#e9b456 45%,#a8701f);color:#3a2810}
.tag{position:absolute;left:300px;width:480px;height:200px;border-radius:30px;background:#f7f1ef;color:#3a0c12;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 20px 60px rgba(0,0,0,.6),0 0 0 5px rgba(255,80,95,.6)}
.tag b{font:900 120px 'DejaVu Serif',serif;line-height:1}
.tag small{font:800 28px Inter;color:#7a4a50;letter-spacing:3px}
.pays{position:absolute;left:130px;top:1150px;width:820px;display:flex;justify-content:space-between}
.pays .p{width:136px;height:136px;border-radius:30px;background:#1a0e10;border:4px solid #ff5a68;display:flex;align-items:center;justify-content:center;font:900 52px Inter;color:#ffe9ea}
.pays .p.ok{background:#d8202f;border-color:#ffb0b6}
.chrono{position:absolute;left:340px;top:1330px;width:400px;height:90px;border-radius:45px;background:#f7f1ef;color:#3a0c12;display:flex;align-items:center;justify-content:center;font:900 44px Inter;letter-spacing:2px;white-space:nowrap}
.cnd{position:absolute;left:150px;width:780px;height:170px;border-radius:36px;background:#160b0d;border:4px solid #5a3036;display:flex;align-items:center;gap:30px;padding:0 40px;white-space:nowrap}
.cnd .ic{flex:none;width:96px;height:96px;border-radius:24px;background:#d8202f;display:flex;align-items:center;justify-content:center;font:900 50px Inter;color:#fff}
.cnd b{display:block;font:900 54px 'DejaVu Serif',serif;color:#ffd7a0}
.cnd span{font:700 30px Inter;color:#e7c9cc;letter-spacing:1px}
.ou{position:absolute;left:0;width:1080px;text-align:center;font:900 64px Inter;color:#ff5a68;letter-spacing:4px}
.tile{position:absolute;left:220px;width:640px;height:160px;border-radius:40px;background:#f7f1ef;color:#3a0c12;display:flex;align-items:center;justify-content:center;gap:24px;font:900 92px 'DejaVu Serif',serif;box-shadow:0 20px 60px rgba(0,0,0,.6),0 0 0 5px rgba(255,80,95,.6);white-space:nowrap}
.tile small{font:800 32px Inter;color:#7a4a50;letter-spacing:2px}
.col{position:absolute;top:560px;width:420px;border-radius:36px;text-align:center;padding:34px 0 30px}
.col .t{font:900 44px Inter;letter-spacing:3px}
.col .r{font:700 30px Inter;margin-top:14px;white-space:nowrap}
.col .v{font:900 96px 'DejaVu Serif',serif;line-height:1.1;margin-top:20px;white-space:nowrap}
.col.f{left:90px;background:#15161c;border:4px solid #3d4150;color:#b8bccb}
.col.g{left:570px;background:linear-gradient(180deg,#2a1d0c,#120c05);border:5px solid #e9b456;color:#ffe9c0;box-shadow:0 0 50px rgba(240,180,80,.35)}
.cal{position:absolute;left:290px;width:500px;height:110px;border-radius:24px;background:#f7f1ef;color:#3a0c12;display:flex;align-items:center;justify-content:center;font:900 44px Inter;white-space:nowrap;box-shadow:0 0 0 5px #d8202f}
'''
CHK = '<svg width="70" height="70" viewBox="0 0 90 90"><path d="M18 46 L38 66 L74 24" fill="none" stroke="#fff" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'


def card(cls, left, top, rot, label, q=False, g=None, fx='pop'):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    qq = '<div class="q">?</div>' if q else ''
    return f'<div class="cd {cls}" style="left:{left}px;top:{top}px;transform:rotate({rot}deg)"{a}><div class="k">{label}</div><div class="chip"></div><div class="n">•••• 2026</div>{qq}</div>'


PAYS = '<div class="pays">' + ''.join(f'<div class="p ok" data-g="2.{2 if k < 3 else 3}" data-fx="tick">{CHK}</div>' for k in range(5)) + '</div>'

BODY = hud('FRANCE · CHOIX DE CARTE', 'FORTUNEO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(205, [('h1 rd', 'STOP !', None, 'font-size:96px'), ('h1', 'PARRAINAGE FORTUNEO :', None, 'font-size:64px'), ('it gold', 'ne choisis pas ta carte', None, 'font-size:74px'), ('it gold', 'au hasard.', None, 'font-size:74px')]) + '''
   ''' + card('fos', 110, 900, -8, 'CARTE ?', True) + card('gld', 570, 900, 7, 'CARTE ?', True) + '''
   <div class="oct" style="left:440px;top:1120px;width:200px;height:200px;font-size:58px">STOP</div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('it gold', 'Avec la carte Fosfo,', '1.0', 'font-size:80px'), ('h1', 'LA PRIME EST', '1.1', 'font-size:64px'), ('big rd', 'de 50 €.', '1.2', 'font-size:130px')]) + '''
   ''' + card('fos', 340, 760, -5, 'FOSFO', False, '1.0', 'right') + '''
   <div class="tag" style="top:1100px" data-g="1.2" data-fx="stamp"><b>50 €</b><small>PRIME CARTE FOSFO</small></div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('it gold', 'Avec la Gold,', '2.0', 'font-size:80px'), ('big gold', "c'est 160 €,", '2.1', 'font-size:130px'), ('h1', 'APRÈS 5 PAIEMENTS', '2.2', 'font-size:60px'), ('it rd', 'en 90 jours.', '2.3', 'font-size:72px')]) + '''
   ''' + card('gld', 340, 800, 4, 'GOLD', False, '2.0', 'left') + PAYS + '''
   <div class="chrono" data-g="2.3" data-fx="pop">⏱ 90 JOURS</div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('h1 rd', 'CONDITION :', '3.0', 'font-size:72px'), ('it gold', '2 200 € de revenus par mois,', '3.1', 'font-size:62px'), ('it gold', "ou 10 000 € d'épargne.", '3.2', 'font-size:62px')]) + '''
   <div class="cnd" style="top:720px" data-g="3.1" data-fx="left"><div class="ic">€</div><div><b>≥ 2 200 € / mois</b><span>REVENUS</span></div></div>
   <div class="ou" style="top:925px" data-g="3.2" data-fx="pop">OU</div>
   <div class="cnd" style="top:1040px" data-g="3.2" data-fx="right"><div class="ic">▣</div><div><b>≥ 10 000 €</b><span>ÉPARGNE</span></div></div>
   <div class="cond" style="top:1250px;font-size:28px;color:#c9a9ad" data-g="3.2" data-fx="fade">condition de la carte Gold · Fosfo : sans condition de revenus</div></div>
  <div class="scene" data-s="4" data-in="right">''' + hd(230, [('big gold', 'Ajoute 80 €', '4.0', 'font-size:130px'), ('h1', 'DE MOBILITÉ,', '4.1', 'font-size:62px'), ('it gold', 'et 20 €', '4.2', 'font-size:74px'), ('it rd', 'avec le Livret +.', '4.3', 'font-size:74px')]) + '''
   <div class="tile" style="top:880px" data-g="4.1" data-fx="stamp">+80 €<small>MOBILITÉ</small></div>
   <div class="tile" style="top:1100px" data-g="4.3" data-fx="stamp">+20 €<small>LIVRET +</small></div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="rays" style="top:640px;left:570px;width:420px;height:420px"></div>''' + hd(215, [('h1 rd', 'RÉSULTAT :', '5.0', 'font-size:72px')]) + '''
   <div class="col f" style="top:420px" data-g="5.1" data-fx="left"><div class="t">FOSFO</div><div class="r">50 + 80 + 20</div><div class="v">150 €</div></div>
   <div class="col g" style="top:420px" data-g="5.1" data-fx="stamp" data-slow="5.1" data-count="260"><div class="t">GOLD</div><div class="r">160 + 80 + 20</div><div class="v gold">0 €</div></div>
   <div class="hd" style="top:850px"><div class="it gold" style="font-size:74px" data-g="5.1" data-fx="tw">jusqu'à 260 €</div><div class="it gold" style="font-size:64px" data-g="5.2" data-fx="tw">avec la Gold,</div></div>
   <div class="cal" style="top:1080px" data-g="5.3" data-fx="pop">AVANT LE 20/12</div>
   <div class="cond" style="top:1230px;font-size:28px;color:#c9a9ad" data-g="5.3" data-fx="fade">montants maximum · 1re ouverture de compte · sous conditions</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« FORTUNEO »', '6.1', 'font-size:110px'), ('it gold', 'en privé,', '6.2', '')]) + '''
   <div class="pill" style="top:760px;border-color:rgba(255,80,95,.85)" data-g="6.3" data-fx="up"><div class="pin" style="background:#d8202f;color:#fff">✉</div><div><b>JE T'ENVOIE LE LIEN</b><span>directement en message privé</span></div></div>
   <div class="search" style="top:900px" data-g="6.3" data-fx="fade">''' + SEARCH + '''<span data-g="6.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1040px;font-size:23px">Offre soumise aux conditions en vigueur · nouveaux clients, jusqu'au 20/12/2026<br>Gold : 160 € (revenus ≥ 2 200 €/mois ou 10 000 € d'épargne), Fosfo : 50 €,<br>après 5 paiements en 90 jours · + 80 € mobilité · + 20 € Livret +</div></div>
'''
