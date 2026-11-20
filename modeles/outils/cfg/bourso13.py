import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# BoursoBank, 20/11/2026 16:00 - style v3 nuit & or, accent vert émeraude. Format F8 « résultat d'abord » :
# relevé de compte d'exemple avec 4 primes créditées (+260 €) dès la 1re image -> compte ouvert +20 € -> paliers du 1er versement
# (10 / 40 / 80 €) -> 3 mois de carte (+20 +30 +30) -> mobilité EasyMove +80 € -> pile 20+80+80+80 = 260 € (ralenti) -> appel à l'action.
# Offre parrainage filleul jusqu'à 260 € (boursobank.com/bon-plan/parrainage-boursobank, consultée le 20/11/2026) :
# 20 € ouverture + 80 € 1er versement >= 300 € + 80 € carte (20 + 30 + 30 sur 3 mois) + 80 € 1re mobilité EasyMove.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'bourso13'
TITLE = 'BoursoBank releve emeraude'
ROOT = ':root{--bg:#060a08}'
LINES = [
 ("Parrainage Bourso Bank : jusqu'à deux cent soixante euros pour le filleul.", [("Parrainage BoursoBank :", None), ("jusqu'à 260 €", None), ("pour le filleul.", None)]),
 ("Vingt euros dès l'ouverture de ton compte.", [("20 €", None), ("dès l'ouverture", None), ("de ton compte.", None)]),
 ("Quatre-vingts euros si ton premier versement fait au moins trois cents euros.", [("80 €", None), ("si ton 1er versement", None), ("fait au moins 300 €.", None)]),
 ("Quatre-vingts euros si tu utilises ta carte chaque mois, pendant trois mois.", [("80 €", None), ("si tu utilises ta carte", None), ("chaque mois, pendant 3 mois.", None)]),
 ("Et quatre-vingts euros avec la mobilité bancaire Easy Move.", [("Et 80 €", None), ("avec la mobilité", None), ("bancaire EasyMove.", None)]),
 ("Total : deux cent soixante euros, sous conditions.", [("Total :", None), ("260 €,", None), ("sous conditions.", None)]),
 ("Envoie-moi PARRAINAGE en privé, je t'envoie le lien.", [("Envoie-moi", None), ("PARRAINAGE", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 3.04), (3.47, 5.0), (5.53, 8.1), (8.76, 11.45), (12.13, 14.57), (15.12, 17.31), (17.9, 19.63)]
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
.em{color:#5fe8b0;text-shadow:0 0 18px rgba(60,220,150,.5)}
.st{position:absolute;left:160px;top:720px;width:740px;border-radius:44px;background:#f3f7f4;color:#10221a;padding:34px 40px 30px;box-shadow:0 30px 90px rgba(0,0,0,.75),0 0 0 5px rgba(60,220,150,.55)}
.st .t{display:flex;justify-content:space-between;font:800 30px Inter;color:#3b5a4c;letter-spacing:2px;white-space:nowrap}
.st .r{display:flex;justify-content:space-between;align-items:center;font:700 34px Inter;padding:16px 0;border-bottom:2px dashed #b9cfc4;white-space:nowrap}
.st .r b{font:900 42px 'DejaVu Serif',serif;color:#0f8a5a}
.st .s{display:flex;justify-content:space-between;align-items:center;margin-top:16px;font:900 40px Inter;white-space:nowrap}
.st .s b{font:900 92px 'DejaVu Serif',serif;color:#0b6b45}
.st .ex{display:inline-block;margin-top:8px;font:700 22px Inter;color:#5d6f66;border:2px solid #b9cfc4;border-radius:14px;padding:4px 12px;letter-spacing:2px}
.acc{position:absolute;left:240px;top:720px;width:600px;height:400px;border-radius:40px;background:linear-gradient(160deg,#123326,#08140f);border:6px solid #5fe8b0;text-align:center;padding-top:50px;box-shadow:0 30px 80px rgba(0,0,0,.7)}
.acc .ck{width:150px;height:150px;margin:0 auto;border-radius:50%;background:#1bb57a;display:flex;align-items:center;justify-content:center}
.acc b{display:block;margin-top:30px;font:900 52px Inter;color:#eafff4;letter-spacing:2px;white-space:nowrap}
.acc span{font:600 30px Inter;color:#9fcab6}
.tile{position:absolute;left:220px;width:640px;height:160px;border-radius:40px;background:#f3f7f4;color:#0b3d2a;display:flex;align-items:center;justify-content:center;gap:24px;font:900 92px 'DejaVu Serif',serif;box-shadow:0 20px 60px rgba(0,0,0,.6),0 0 0 5px rgba(60,220,150,.6);white-space:nowrap}
.tile small{font:800 32px Inter;color:#3b5a4c;letter-spacing:2px}
.tier{position:absolute;left:170px;width:740px;height:130px;border-radius:30px;background:#0f1a15;border:4px solid #2c4a3d;display:flex;align-items:center;justify-content:space-between;padding:0 44px;font:800 40px Inter;color:#d6efe3;white-space:nowrap}
.tier b{font:900 64px 'DejaVu Serif',serif;color:#7fbfa3}
.tier.on{background:#103c2b;border-color:#5fe8b0;box-shadow:0 0 40px rgba(60,220,150,.35)}
.tier.on b{color:#5fe8b0}
.mo{position:absolute;top:760px;width:230px;height:300px;border-radius:30px;background:#0f1a15;border:4px solid #2c4a3d;text-align:center;padding-top:26px}
.mo .m{font:800 32px Inter;color:#9fcab6;letter-spacing:2px}
.mo .cd{width:150px;height:96px;margin:24px auto 0;border-radius:14px;background:linear-gradient(135deg,#5fe8b0,#127a52)}
.mo b{display:block;margin-top:24px;font:900 64px 'DejaVu Serif',serif;color:#5fe8b0}
.bk{position:absolute;top:760px;width:300px;height:360px;text-align:center}
.bk .bd{width:300px;height:280px;border-radius:20px;background:#0f1a15;border:5px solid #2c4a3d;position:relative}
.bk .bd i{position:absolute;bottom:0;width:50px;height:150px;background:#1d2e26;border-radius:8px 8px 0 0}
.bk .rf{width:0;height:0;margin:0 auto;border-left:170px solid transparent;border-right:170px solid transparent;border-bottom:80px solid #2c4a3d}
.bk b{display:block;margin-top:18px;font:800 32px Inter;color:#eafff4;letter-spacing:2px;white-space:nowrap}
.bk.on .bd{border-color:#5fe8b0;box-shadow:0 0 40px rgba(60,220,150,.35)}
.bk.on .rf{border-bottom-color:#1bb57a}
.mv{position:absolute;left:420px;top:880px;width:240px;height:80px}
.stk{position:absolute;left:190px;width:700px}
.stk .r{height:96px;border-radius:28px;background:#0f1a15;border:4px solid #2c4a3d;margin-bottom:16px;display:flex;align-items:center;justify-content:space-between;padding:0 40px;font:800 36px Inter;color:#eafff4;white-space:nowrap}
.stk .r b{font:900 50px 'DejaVu Serif',serif;color:#5fe8b0}
.tot{position:absolute;left:0;width:1080px;text-align:center}
.tot .v{font:900 200px 'DejaVu Serif',serif;line-height:1}
'''
CHECK = '<svg width="90" height="90" viewBox="0 0 90 90"><path d="M18 46 L38 66 L74 24" fill="none" stroke="#fff" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
MVA = '<svg class="mv" viewBox="0 0 240 80" width="240" height="80"><path d="M10 40 H200" stroke="#5fe8b0" stroke-width="12" stroke-linecap="round" stroke-dasharray="4 26"/><path d="M180 12 L225 40 L180 68" fill="none" stroke="#5fe8b0" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg>'
COLS = '<i style="left:30px"></i><i style="left:125px"></i><i style="left:220px"></i>'


def bank(left, name, on, g):
    return f'<div class="bk{" on" if on else ""}" style="left:{left}px" data-g="{g}" data-fx="pop"><div class="rf"></div><div class="bd">{COLS}</div><b>{name}</b></div>'


def mo(left, m, v, g):
    return f'<div class="mo" style="left:{left}px" data-g="{g}" data-fx="up"><div class="m">{m}</div><div class="cd"></div><b>+{v} €</b></div>'


BODY = hud('FRANCE · RELEVÉ', 'BOURSOBANK') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(215, [('h1 em', 'PARRAINAGE BOURSOBANK :', None, 'font-size:56px'), ('big gold', "jusqu'à 260 €", None, 'font-size:120px'), ('it gold', 'pour le filleul.', None, 'font-size:70px')]) + '''
   <div class="st" style="top:640px"><div class="t"><span>MON RELEVÉ</span><span>NOUVEAU COMPTE</span></div>
    <div class="r">Prime ouverture<b>+20 €</b></div><div class="r">1er versement<b>+80 €</b></div><div class="r">Carte · 3 mois<b>+80 €</b></div><div class="r">Mobilité EasyMove<b>+80 €</b></div>
    <div class="s">Total primes<b>+260 €</b></div><span class="ex">EXEMPLE · MAXIMUM SOUS CONDITIONS</span></div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('big gold', '20 €', '1.0', 'font-size:150px'), ('it gold', "dès l'ouverture", '1.1', 'font-size:72px'), ('h1 em', 'DE TON COMPTE.', '1.2', 'font-size:64px')]) + '''
   <div class="acc" style="top:700px" data-g="1.1" data-fx="pop"><div class="ck">''' + CHECK + '''</div><b>COMPTE OUVERT</b><span>1re ouverture · compte individuel</span></div>
   <div class="tile" style="top:1170px" data-g="1.0" data-fx="stamp">+20 €<small>OUVERTURE</small></div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('big gold', '80 €', '2.0', 'font-size:150px'), ('it gold', 'si ton 1er versement', '2.1', 'font-size:66px'), ('h1 em', 'FAIT AU MOINS 300 €.', '2.2', 'font-size:60px')]) + '''
   <div class="tier" style="top:720px" data-g="2.1" data-fx="left">De 1 à 49 €<b>10 €</b></div>
   <div class="tier" style="top:880px" data-g="2.1" data-fx="right">De 50 à 299 €<b>40 €</b></div>
   <div class="tier on" style="top:1040px" data-g="2.2" data-fx="stamp">300 € et plus<b>80 €</b></div>
   <div class="cond" style="top:1210px;font-size:28px;color:#8fb3a3" data-g="2.2" data-fx="fade">1er versement à l'ouverture ou dans les 30 jours</div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('big gold', '80 €', '3.0', 'font-size:150px'), ('it gold', 'si tu utilises ta carte', '3.1', 'font-size:64px'), ('h1 em', 'CHAQUE MOIS, PENDANT 3 MOIS.', '3.2', 'font-size:50px')]) + '''
   ''' + mo(150, 'MOIS 1', 20, '3.1') + mo(425, 'MOIS 2', 30, '3.2') + mo(700, 'MOIS 3', 30, '3.2') + '''
   <div class="cond" style="top:1110px;font-size:28px;color:#8fb3a3" data-g="3.2" data-fx="fade">au moins 1 paiement ou retrait par mois</div></div>
  <div class="scene" data-s="4" data-in="right">''' + hd(230, [('big gold', 'Et 80 €', '4.0', 'font-size:140px'), ('it gold', 'avec la mobilité', '4.1', 'font-size:68px'), ('h1 em', 'BANCAIRE EASYMOVE.', '4.2', 'font-size:62px')]) + '''
   ''' + bank(110, 'ANCIENNE', False, '4.1') + '<span data-g="4.2" data-fx="fade">' + MVA + '</span>' + bank(670, 'NOUVELLE', True, '4.2') + '''
   <div class="tile" style="top:1200px" data-g="4.0" data-fx="stamp">+80 €<small>EASYMOVE</small></div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="rays" style="top:930px"></div>''' + hd(215, [('h1 em', 'TOTAL :', '5.0', ''), ('it gold', 'sous conditions.', '5.2', 'font-size:66px')]) + '''
   <div class="stk" style="top:470px"><div class="r" data-g="5.0" data-fx="left">Ouverture<b>20 €</b></div><div class="r" data-g="5.0" data-fx="right">1er versement<b>80 €</b></div><div class="r" data-g="5.0" data-fx="left">Carte 3 mois<b>80 €</b></div><div class="r" data-g="5.0" data-fx="right">EasyMove<b>80 €</b></div></div>
   <div class="tot" style="top:960px" data-g="5.1" data-fx="stamp" data-slow="5.1" data-count="260"><div class="v gold">0 €</div></div>
   <div class="cond" style="top:1210px;font-size:30px;color:#a9c9bb" data-g="5.2" data-fx="up">pour une 1re ouverture de compte individuel</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« PARRAINAGE »', '6.1', 'font-size:100px'), ('it gold', 'en privé,', '6.2', '')]) + '''
   <div class="pill" style="top:760px;border-color:rgba(60,220,150,.85)" data-g="6.3" data-fx="up"><div class="pin" style="background:#1bb57a;color:#fff">✉</div><div><b>JE T'ENVOIE LE LIEN</b><span>directement en message privé</span></div></div>
   <div class="search" style="top:900px" data-g="6.3" data-fx="fade">''' + SEARCH + '''<span data-g="6.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1040px;font-size:23px">Offre soumise aux conditions en vigueur · 1re ouverture de compte individuel<br>jusqu'à 260 € pour le filleul : 20 € ouverture + 80 € 1er versement (≥ 300 €)<br>+ 80 € carte sur 3 mois + 80 € mobilité EasyMove · relevé d'illustration</div></div>
'''
