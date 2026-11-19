import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Fortuneo, 19/11/2026 18:00 - style v3 nuit & or, accent améthyste. Format F8 « résultat d'abord » :
# écran verrouillé avec la notification « prime carte Gold +160 € » (illustration) dès la 1re image -> frise 5 paiements en 90 jours
# -> transfert ancienne banque -> nouvelle (+80 € mobilité) -> livret (+20 €) -> pile 160 + 80 + 20 = 260 € (ralenti) + calendrier 20 déc. -> appel à l'action.
# Offre de bienvenue Fortuneo jusqu'au 20/12/2026 : carte Gold (revenus >= 2 200 €/mois) 160 € après 5 paiements en 90 jours + 80 € mobilité
# + 20 € Livret + = 260 € ; Fosfo jusqu'à 150 € (selectra.info, offre-bienvenue Fortuneo, màj 13/10/2026, consultée le 19/11/2026 ;
# moneyvox.fr « jusqu'à 260 euros offerts »).
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'fortuneo11'
TITLE = 'Fortuneo notification amethyste'
ROOT = ':root{--bg:#08060c}'
LINES = [
 ("Parrainage Fortunéo : regarde cette notif à cent soixante euros.", [("Parrainage Fortuneo :", None), ("regarde cette notif", None), ("à 160 €.", None)]),
 ("C'est la prime carte Gold, après cinq paiements en quatre-vingt-dix jours.", [("C'est la prime carte Gold,", None), ("après 5 paiements", None), ("en 90 jours.", None)]),
 ("Plus quatre-vingts euros si tu fais la mobilité bancaire.", [("Plus 80 €", None), ("si tu fais", None), ("la mobilité bancaire.", None)]),
 ("Et vingt euros pour l'ouverture d'un Livret plus.", [("Et 20 €", None), ("pour l'ouverture", None), ("d'un Livret +.", None)]),
 ("Jusqu'à deux cent soixante euros, jusqu'au vingt décembre, sous conditions.", [("Jusqu'à 260 €,", None), ("jusqu'au 20 décembre,", None), ("sous conditions.", None)]),
 ("Envoie-moi FORTUNÉO en privé, je t'envoie le lien.", [("Envoie-moi", None), ("FORTUNEO", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
MINLEN = 1.9
GAP = 0.32
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.am{color:#c9a8ff;text-shadow:0 0 18px rgba(160,110,255,.55)}
.lock{position:absolute;left:150px;top:640px;width:780px;height:860px;border-radius:70px;background:linear-gradient(180deg,#1a1030,#09060f 70%);border:10px solid #2a2433;box-shadow:0 0 0 2px #4d4559,0 30px 90px rgba(0,0,0,.75);overflow:hidden}
.lock .clk{position:absolute;left:0;top:50px;width:100%;text-align:center;font:200 116px Inter;color:#efe8ff}
.lock .dt{position:absolute;left:0;top:186px;width:100%;text-align:center;font:600 30px Inter;color:#b7a6d8}
.nf{position:absolute;left:30px;top:290px;width:700px;border-radius:40px;background:rgba(246,242,255,.95);color:#17121f;padding:30px 34px;box-shadow:0 14px 40px rgba(0,0,0,.4)}
.nf .h{display:flex;align-items:center;gap:18px;font:800 32px Inter;white-space:nowrap}
.nf .h .ic{width:70px;height:70px;border-radius:18px;background:#8b5cf6;display:flex;align-items:center;justify-content:center}
.nf .h small{margin-left:auto;font:600 24px Inter;color:#6f6680}
.nf .l{font:700 32px Inter;color:#3b3150;margin-top:22px}
.nf .v{font:900 130px 'DejaVu Serif',serif;color:#5b2bc4;line-height:1.05;white-space:nowrap}
.nf .ex{display:inline-block;margin-top:6px;font:700 22px Inter;color:#6f6680;border:2px solid #b9aed0;border-radius:14px;padding:4px 12px;letter-spacing:2px}
.goldc{position:absolute;left:290px;top:640px;width:500px;height:315px;border-radius:30px;background:linear-gradient(135deg,#fff1c4,#e9b456 45%,#a8701f);box-shadow:0 30px 80px rgba(0,0,0,.7),0 0 60px rgba(240,180,80,.3);transform:rotate(-6deg)}
.goldc .chip{position:absolute;left:44px;top:110px;width:84px;height:64px;border-radius:12px;background:linear-gradient(135deg,#f6f1e7,#bfa98a)}
.goldc .k{position:absolute;left:44px;top:36px;font:800 26px 'DejaVu Sans Mono',monospace;letter-spacing:6px;color:#3a2810}
.goldc .n{position:absolute;left:44px;top:230px;font:700 30px 'DejaVu Sans Mono',monospace;letter-spacing:3px;color:#3a2810}
.track{position:absolute;left:120px;top:1080px;width:840px;height:200px}
.track .ln{position:absolute;left:30px;top:60px;width:780px;height:8px;border-radius:4px;background:#3a3047}
.track .dot{position:absolute;top:24px;width:80px;height:80px;border-radius:50%;background:#8b5cf6;border:5px solid #c9a8ff;color:#fff;font:900 36px Inter;display:flex;align-items:center;justify-content:center;box-shadow:0 0 24px rgba(160,110,255,.6)}
.track .d{position:absolute;top:130px;font:700 30px Inter;color:#b7a6d8;white-space:nowrap}
.bk{position:absolute;top:760px;width:300px;height:360px;text-align:center}
.bk .bd{width:300px;height:280px;border-radius:20px;background:#17121f;border:5px solid #4d4559;position:relative}
.bk .bd i{position:absolute;bottom:0;width:50px;height:150px;background:#2a2236;border-radius:8px 8px 0 0}
.bk .rf{width:0;height:0;margin:0 auto;border-left:170px solid transparent;border-right:170px solid transparent;border-bottom:80px solid #4d4559}
.bk b{display:block;margin-top:18px;font:800 32px Inter;color:#efe8ff;letter-spacing:2px;white-space:nowrap}
.bk.on .bd{border-color:#c9a8ff;box-shadow:0 0 40px rgba(160,110,255,.35)}
.bk.on .rf{border-bottom-color:#8b5cf6}
.mv{position:absolute;left:420px;top:880px;width:240px;height:80px}
.tile{position:absolute;left:220px;width:640px;height:170px;border-radius:40px;background:#f6f2ff;color:#2a1a52;display:flex;align-items:center;justify-content:center;gap:24px;font:900 96px 'DejaVu Serif',serif;box-shadow:0 20px 60px rgba(0,0,0,.6),0 0 0 5px rgba(160,110,255,.6);white-space:nowrap}
.tile small{font:800 34px Inter;color:#5b4a80;letter-spacing:2px}
.liv{position:absolute;left:340px;top:700px;width:400px;height:460px;border-radius:30px;background:linear-gradient(160deg,#2a1d48,#140e24);border:6px solid #c9a8ff;text-align:center;padding-top:50px;box-shadow:0 30px 80px rgba(0,0,0,.7)}
.liv .t{font:900 54px Inter;color:#efe8ff;letter-spacing:3px}
.liv .p{font:900 150px 'DejaVu Serif',serif;color:#c9a8ff;line-height:1.2}
.liv .s{font:700 30px Inter;color:#b7a6d8}
.stk{position:absolute;left:190px;top:640px;width:700px}
.stk .r{height:110px;border-radius:30px;background:#17121f;border:4px solid #4d4559;margin-bottom:20px;display:flex;align-items:center;justify-content:space-between;padding:0 40px;font:800 38px Inter;color:#efe8ff;white-space:nowrap}
.stk .r b{font:900 54px 'DejaVu Serif',serif;color:#c9a8ff}
.tot{position:absolute;left:0;top:1060px;width:1080px;text-align:center}
.tot .v{font:900 200px 'DejaVu Serif',serif;line-height:1}
.cal{position:absolute;left:290px;top:1290px;width:500px;height:120px;border-radius:24px;background:#f6f2ff;color:#2a1a52;display:flex;align-items:center;justify-content:center;gap:16px;font:900 46px Inter;white-space:nowrap;box-shadow:0 0 0 5px #8b5cf6}
'''
BELL = '<svg width="44" height="44" viewBox="0 0 50 50"><path d="M25 6c-8 0-13 6-13 14v9l-5 7h36l-5-7v-9c0-8-5-14-13-14z" fill="#fff"/><circle cx="25" cy="42" r="5" fill="#fff"/></svg>'
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
MVA = '<svg class="mv" viewBox="0 0 240 80" width="240" height="80"><path d="M10 40 H200" stroke="#c9a8ff" stroke-width="12" stroke-linecap="round" stroke-dasharray="4 26"/><path d="M180 12 L225 40 L180 68" fill="none" stroke="#c9a8ff" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg>'
COLS = '<i style="left:30px"></i><i style="left:125px"></i><i style="left:220px"></i>'
DAYS = ['J+5', 'J+20', 'J+40', 'J+60', 'J+85']


def bank(left, name, on, g):
    return f'<div class="bk{" on" if on else ""}" style="left:{left}px" data-g="{g}" data-fx="pop"><div class="rf"></div><div class="bd">{COLS}</div><b>{name}</b></div>'


TRACK = '<div class="track"><div class="ln"></div>' + ''.join(
    f'<div class="dot" style="left:{20 + k * 175}px" data-g="1.{1 if k < 3 else 2}" data-fx="pop">{k + 1}</div><div class="d" style="left:{24 + k * 175}px">{DAYS[k]}</div>' for k in range(5)) + '</div>'

BODY = hud('FRANCE · NOTIFICATION', 'FORTUNEO') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(205, [('h1 am', 'PARRAINAGE FORTUNEO :', None, 'font-size:70px'), ('it gold', 'regarde cette notif', None, 'font-size:82px'), ('it gold', 'à 160 €.', None, 'font-size:82px')]) + '''
   <div class="lock" style="top:650px"><div class="clk">18:00</div><div class="dt">jeudi 19 novembre</div>
    <div class="nf"><div class="h"><div class="ic">''' + BELL + '''</div>Fortuneo<small>maintenant</small></div>
     <div class="l">Prime carte Gold versée</div><div class="v">+160 €</div><span class="ex">EXEMPLE · SOUS CONDITIONS</span></div></div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1 s', "C'EST LA PRIME CARTE GOLD,", '1.0', 'font-size:60px'), ('it gold', 'après 5 paiements', '1.1', 'font-size:74px'), ('it am', 'en 90 jours.', '1.2', 'font-size:74px')]) + '''
   <div class="goldc" data-g="1.0" data-fx="right"><div class="k">CARTE GOLD</div><div class="chip"></div><div class="n">•••• 2026</div></div>
   ''' + TRACK + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('big gold', 'Plus 80 €', '2.0', 'font-size:130px'), ('it gold', 'si tu fais', '2.1', 'font-size:66px'), ('h1 am', 'LA MOBILITÉ BANCAIRE.', '2.2', 'font-size:64px')]) + '''
   ''' + bank(110, 'ANCIENNE', False, '2.1') + '<span data-g="2.2" data-fx="fade">' + MVA + '</span>' + bank(670, 'NOUVELLE', True, '2.2') + '''
   <div class="tile" style="top:1210px" data-g="2.0" data-fx="stamp">+80 €<small>MOBILITÉ</small></div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('big gold', 'Et 20 €', '3.0', 'font-size:130px'), ('it gold', "pour l'ouverture", '3.1', 'font-size:66px'), ('it am', "d'un Livret +.", '3.2', 'font-size:74px')]) + '''
   <div class="liv" data-g="3.1" data-fx="up"><div class="t">LIVRET</div><div class="p">+</div><div class="s">1re ouverture</div></div>
   <div class="tile" style="top:1210px" data-g="3.0" data-fx="stamp">+20 €<small>LIVRET +</small></div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:880px"></div>''' + hd(215, [('h1 am', "JUSQU'À", '4.0', ''), ('it gold', "jusqu'au 20 décembre,", '4.1', 'font-size:66px')]) + '''
   <div class="stk" style="top:470px"><div class="r" data-g="4.0" data-fx="left">Carte Gold<b>160 €</b></div><div class="r" data-g="4.0" data-fx="right">Mobilité<b>80 €</b></div><div class="r" data-g="4.0" data-fx="left">Livret +<b>20 €</b></div></div>
   <div class="tot" style="top:900px" data-g="4.0" data-fx="stamp" data-slow="4.0" data-count="260"><div class="v gold">0 €</div></div>
   <div class="cal" style="top:1150px" data-g="4.1" data-fx="pop">AVANT LE 20/12</div>
   <div class="cond" style="top:1310px;font-size:30px;color:#c9bfdc" data-g="4.2" data-fx="up">sous conditions · offre de bienvenue</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« FORTUNEO »', '5.1', 'font-size:110px'), ('it gold', 'en privé,', '5.2', '')]) + '''
   <div class="pill" style="top:760px;border-color:rgba(160,110,255,.85)" data-g="5.3" data-fx="up"><div class="pin" style="background:#8b5cf6;color:#fff">✉</div><div><b>JE T'ENVOIE LE LIEN</b><span>directement en message privé</span></div></div>
   <div class="search" style="top:900px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1040px">Offre soumise aux conditions en vigueur · nouveaux clients, jusqu'au 20/12<br>jusqu'à 260 € avec la carte Gold (revenus ≥ 2 200 €/mois), Fosfo : jusqu'à 150 €<br>prime carte après 5 paiements en 90 jours · notification d'illustration</div></div>
'''
