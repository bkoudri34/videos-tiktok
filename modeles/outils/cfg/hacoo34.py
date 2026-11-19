import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qg_ecran import *
from hacoo_items import icon
# Hacoo n°2 du 19/11/2026 - style E « Écran d'appli en gros plan » (brief veille du 19/11, vidéo 2), accent orange.
# Réutilise les briques E des vidéos QG (cfg/qg_ecran.py, qg_base_ecran.css) : téléphone DESSINÉ, générique, sans logo ni interface copiée.
# Format F8 résultat d'abord : total 55,90 € déjà réduit dès la 1re image -> rembobinage -> panier à 65,00 € -> 1 : on touche la case
# -> 2 : hzklink tapé au clavier -> 3 : Appliquer, ligne -9,10 € -> 55,90 € (ralenti) -> écran de fin (boucle sur le résultat).
# Prix d'exemple : baskets de running 49 € + sacoche 16 € = 65,00 € ; -14 % = 9,10 € ; total 55,90 €.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08 ; « Hacou », « H Z K link ».
NAME = 'hacoo34'
TITLE = 'Hacoo ecran appli orange'
ROOT = ':root{--bg:#f3ece6}'
LINES = [
 ("Attends, regarde ce total sur l'appli Hacou.", [("<em>Attends</em>,", None), ("regarde ce total", None), ("sur l'appli <em>Hacoo</em>.", None)]),
 ("Avant le code promo Hacou, c'était soixante-cinq euros.", [("Avant le", None), ("<em>code promo Hacoo</em>,", None), ("c'était <i>65 €</i>.", None)]),
 ("Un : touche la case code promo.", [("<em>Un</em> :", None), ("touche la case", None), ("code promo.", None)]),
 ("Deux : tape H Z K link.", [("<em>Deux</em> :", None), ("tape", None), ("<em>hzklink</em>.", None)]),
 ("Trois : appliquer. Moins neuf euros dix, d'un coup.", [("<em>Trois</em> :", None), ("appliquer.", None), ("<i>-9,10 €</i>,", None), ("d'un coup.", None)]),
 ("Cinquante-cinq euros quatre-vingt-dix. Prix d'exemple.", [("<em>55,90 €</em>.", None), ("Prix d'exemple.", None)]),
 ("Code promo Hacou, H Z K link. Enregistre-la pour ta prochaine commande.", [("<em>Code promo Hacoo</em>", None), ("<em>hzklink</em>.", None), ("Enregistre-la", None), ("pour ta prochaine commande.", None)]),
]
SPLITS = [(0.0, 1.95), (2.57, 5.04), (5.50, 6.98), (7.40, 9.03), (9.44, 12.14), (12.57, 14.68), (15.16, 18.30)]
TAIL = 3.4
GSTART = [[0.0, 0.4, 1.1], [2.57, 2.8, 4.0], [5.50, 6.0, 6.5], [7.40, 8.0, 8.3], [9.44, 9.9, 10.8, 11.8], [12.57, 14.2], [15.16, 16.0, 17.0, 17.5]]

CSS = '''
body,#stage{background:#f3ece6}
#bgtex{background:radial-gradient(circle at 1px 1px,rgba(60,30,10,.10) 2px,transparent 2.5px) 0 0/44px 44px,linear-gradient(160deg,#fbf6f1 0%,#f1e6dc 60%,#e9dbcf 100%)}
.search .cur{background:#ff6b2c}
.rip{border-color:#ff6b2c}
.step b{color:#ffb38a}
.ap .row{height:110px}
.ap .row .p{margin-left:auto;font:900 40px Inter;color:#0f172a}
.ap .row .ic{width:92px;height:92px;border-radius:20px;background:#f4f4f6;display:flex;align-items:center;justify-content:center;flex:none}
.ap .fr2{display:flex;gap:16px;align-items:center}
.ap .fr2 .fd{flex:1}
.ap .ap2{height:104px;padding:0 26px;border-radius:24px;background:#ff6b2c;color:#fff;font:900 34px Inter;display:flex;align-items:center;white-space:nowrap}
.ap .fd.on{border-color:#ff6b2c;background:#fff4ee}
.ap .fd .cd{font:900 46px 'DejaVu Sans Mono',monospace;color:#0f172a}
.ap .disc{height:96px;display:flex;align-items:center;font:900 28px Inter;color:#e8590c;border-bottom:3px solid #eef2f7;white-space:nowrap}
.ap .disc .p{margin-left:auto;font:900 40px Inter;color:#e8590c}
.ap .tot{display:flex;align-items:baseline;justify-content:space-between;margin-top:22px;font:900 44px Inter;white-space:nowrap}
.ap .tot b{font:900 76px Inter;letter-spacing:-2px}
.ap .tot s{font:800 38px Inter;color:#94a3b8;text-decoration-color:#e8590c;text-decoration-thickness:5px;margin-right:14px}
.ap .ex{font:700 26px Inter;color:#94a3b8;margin-top:6px}
.kb{position:absolute;left:0;right:0;bottom:0;height:470px;background:#d6d9df;padding:24px 14px;display:grid;grid-template-columns:repeat(10,1fr);gap:12px;align-content:start}
.kb i{height:86px;border-radius:12px;background:#fff;font:600 38px Inter;font-style:normal;display:flex;align-items:center;justify-content:center;color:#0f172a;box-shadow:0 3px 0 #9aa0aa}
.kb i.h{background:#ff6b2c;color:#fff}
.rew{position:absolute;left:0;top:0;width:1080px;height:1920px;background:rgba(15,23,42,.18);z-index:7}
.rew b{position:absolute;left:290px;top:1235px;width:460px;height:140px;border-radius:30px;background:#0f172a;color:#fff;font:900 66px Inter;display:flex;flex-direction:row;align-items:center;justify-content:center;gap:20px;letter-spacing:4px;white-space:nowrap}
.gain{background:#e8590c;box-shadow:0 12px 0 #8a3305}
.endc .c{background:#ff6b2c;color:#fff}
.endc .b{color:#ffb38a}
'''
ROWS = ''.join(f'<div class="row"><span class="ic">{icon(ic, 80)}</span>{lab}<span class="p">{pr}</span></div>' for ic, lab, pr in [('Baskets', 'Baskets running', '49,00 €'), ('Sacoche', 'Sacoche', '16,00 €')])
KEYS = ''.join(f'<i{" class=\"h\"" if k in "hzkl" else ""}>{k}</i>' for k in 'azertyuiopqsdfghjklmwxcvbn')


def cart(field='', disc=False, total='65,00 €', old=None, extra='', gd=None):
    f = f'<div class="fd on"><span class="cd">{field}</span></div>' if field else '<div class="fd" style="color:#94a3b8">Ajouter un code</div>'
    d = ''
    if disc:
        a = f' data-g="{gd}" data-fx="right"' if gd else ''
        d = f'<div class="disc"{a}>Code promo Hacoo (-14 %)<span class="p">-9,10 €</span></div>'
    o = f'<s>{old}</s>' if old else ''
    return phone(f'''<div class="hd">Mon panier Hacoo</div>{ROWS}<div class="lb">Code promo Hacoo</div>
     <div class="fr2">{f}<div class="ap2">Appliquer</div></div>{d}
     <div class="tot"><span>Total</span><span>{o}<b>{total}</b></span></div><div class="ex">prix d'exemple</div>{extra}''')


def kbd(ph):
    return ph[:-12] + '<div class="kb" data-g="3.0" data-fx="up">' + KEYS + '</div></div></div>'


BODY = search('code promo hacoo') + '''
  <div class="scene" data-s="0">''' + cart('hzklink', True, '55,90 €', '65,00 €') + '''
   <div class="stk" style="left:470px;top:345px;transform:rotate(4deg)">ATTENDS !</div></div>
  <div class="scene" data-s="1" data-in="left"><div class="rew" data-g="1.0" data-fx="fade"><b><span>◀◀</span><span>AVANT</span></b></div>''' + cart() + '''
   </div>
  <div class="scene" data-s="2" data-in="right">''' + step(1, 3, 'LA CASE') + '''
   <div class="zm" data-zg="2.1" data-zs="1.22" style="transform-origin:360px 972px">''' + cart() + hand(360, 975, '2.1') + '''</div></div>
  <div class="scene" data-s="3" data-in="right">''' + step(2, 3, 'LE CODE') + '''
   <div class="zm" data-zg="3.0" data-zs="1.12" style="transform-origin:360px 972px">''' + kbd(cart('<span data-g="3.2" data-fx="type">hzklink</span>')) + '''</div>
   <div class="stk" style="left:200px;top:1245px" data-g="3.2" data-fx="pop">CODE PROMO HACOO</div></div>
  <div class="scene" data-s="4" data-in="up">''' + step(3, 3, 'APPLIQUER') + '''
   <div class="zm" data-zg="4.2" data-zs="1.12" style="transform-origin:470px 1076px">''' + cart('hzklink', True, '65,00 €', None, gd='4.2') + hand(700, 975, '4.1') + '''</div>
   <div class="gain" style="left:470px;top:1210px" data-g="4.2" data-fx="stamp">-9,10 €</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + cart('hzklink', True, '55,90 €', '65,00 €') + '''
   <div class="gain" style="left:300px;top:1180px;font-size:110px" data-g="5.0" data-fx="stamp" data-slow="5.0">55,90 €</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + cart('hzklink', True, '55,90 €', '65,00 €') + '''
   <div class="endc" data-g="6.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div><div class="b">liens des articles tendance en bio</div></div>
   <div class="cond" style="top:1285px;background:#fff" data-g="6.1" data-fx="fade">Prix d'exemple · -14 % avec le code promo Hacoo hzklink sur l'appli Hacoo · Offre soumise aux conditions en vigueur</div></div>
'''
