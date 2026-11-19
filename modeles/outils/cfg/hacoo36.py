import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qg_ecran import *
from hacoo_items import icon
# Hacoo n°4 du 19/11/2026 (tâche « 2 vidéos Hacoo en plus ») - style E « Écran d'appli en gros plan », accent vert sarcelle.
# Repli : le style D « Duo 3D » était prévu (le moins utilisé), mais Three.js reste injoignable depuis le bac à sable
# (raw.githubusercontent.com refusé 403 par le proxy, comme jsDelivr / npm les jours précédents).
# Format F2 démystification / tuto : « Où se cache la case code promo Hacoo ? » ; haut du panier -> on descend tout en bas
# (sous les recommandations) -> 1 : descendre -> 2 : toucher la case -> 3 : taper hzklink + Appliquer -> -8,12 € -> 49,88 € (ralenti) -> fin.
# Téléphone DESSINÉ, générique, sans logo ni interface copiée.
# Prix d'exemple : bottines 36 € + casque audio 22 € = 58,00 € ; -14 % = 8,12 € (58 x 0,14) ; total 49,88 € (58 x 0,86).
# Voix : Speko, Marc (azure, « fr-FR-Marc:MAI-Voice-2.1 »), speed 1.08, une synthèse par réplique, silences coupés,
# recollées avec 0,2 s au début et 0,45 s entre les répliques (SPLITS).
NAME = 'hacoo36'
TITLE = 'Hacoo ou est la case sarcelle'
ROOT = ':root{--bg:#e3f1ee}'
LINES = [
 ("Où se cache la case code promo sur l'appli Hacou ? Je te montre.", [("Où se cache", None), ("la case <em>code promo</em>", None), ("sur l'appli <em>Hacoo</em> ?", None), ("Je te montre.", None)]),
 ("Ton panier : bottines, casque, cinquante-huit euros.", [("Ton panier :", None), ("bottines, casque,", None), ("<i>58 €</i>.", None)]),
 ("Un : descends tout en bas, sous le panier.", [("<em>Un</em> :", None), ("descends tout en bas,", None), ("sous le panier.", None)]),
 ("Deux : touche la case code promo Hacou.", [("<em>Deux</em> :", None), ("touche la case", None), ("<em>code promo Hacoo</em>.", None)]),
 ("Trois : tape H Z K link, puis appliquer.", [("<em>Trois</em> :", None), ("tape <em>hzklink</em>,", None), ("puis appliquer.", None)]),
 ("Moins huit euros douze. Total : quarante-neuf euros quatre-vingt-huit.", [("<i>-8,12 €</i>.", None), ("Total :", None), ("<em>49,88 €</em>.", None)]),
 ("Prix d'exemple. Enregistre la vidéo, et note le code promo Hacou : H Z K link.", [("Prix d'exemple.", None), ("Enregistre la vidéo,", None), ("et note le", None), ("<em>code promo Hacoo</em>", None), ("<em>hzklink</em>.", None)]),
]
SPLITS = [(0.2, 5.908), (6.358, 10.541), (10.991, 14.412), (14.862, 19.052), (19.502, 23.943), (24.393, 28.074), (28.524, 34.439)]
TAIL = 2.6
GAP = 0.3

AC = '#0d9488'
CSS = '''
body,#stage{background:#e3f1ee}
#bgtex{background:radial-gradient(circle at 1px 1px,rgba(10,60,55,.10) 2px,transparent 2.5px) 0 0/44px 44px,linear-gradient(160deg,#f3faf8 0%,#dcefea 60%,#cfe6e0 100%)}
.search .cur{background:#0d9488}
.rip{border-color:#0d9488}
.step b{color:#5eead4}
.ap .row{height:116px}
.ap .row .p{margin-left:auto;font:900 40px Inter;color:#0f172a}
.ap .row .ic{width:96px;height:96px;border-radius:20px;background:#f4f4f6;display:flex;align-items:center;justify-content:center;flex:none}
.ap .rc{font:900 34px Inter;color:#0f172a;margin:30px 0 16px}
.ap .tiles{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.ap .tiles div{height:250px;border-radius:26px;background:#eef2f6;position:relative}
.ap .tiles div:after{content:'';position:absolute;left:22px;right:60px;bottom:24px;height:22px;border-radius:11px;background:#dbe2ea}
.ap .tiles.cut div{height:150px;border-radius:0 0 26px 26px}
.ap .fr2{display:flex;gap:16px;align-items:center}
.ap .fr2 .fd{flex:1}
.ap .ap2{height:104px;padding:0 26px;border-radius:24px;background:#0d9488;color:#fff;font:900 34px Inter;display:flex;align-items:center;white-space:nowrap}
.ap .fd.on{border-color:#0d9488;background:#effcf9}
.ap .fd .cd{font:900 46px 'DejaVu Sans Mono',monospace;color:#0f172a}
.ap .disc{height:96px;display:flex;align-items:center;font:900 28px Inter;color:#0f766e;border-bottom:3px solid #eef2f7;white-space:nowrap}
.ap .disc .p{margin-left:auto;font:900 40px Inter;color:#0f766e}
.ap .tot{display:flex;align-items:baseline;justify-content:space-between;margin-top:22px;font:900 44px Inter;white-space:nowrap}
.ap .tot b{font:900 76px Inter;letter-spacing:-2px}
.ap .tot s{font:800 38px Inter;color:#94a3b8;text-decoration-color:#0d9488;text-decoration-thickness:5px;margin-right:14px}
.ap .ex{font:700 26px Inter;color:#94a3b8;margin-top:6px}
.kb{position:absolute;left:0;right:0;bottom:0;height:470px;background:#d6d9df;padding:24px 14px;display:grid;grid-template-columns:repeat(10,1fr);gap:12px;align-content:start}
.kb i{height:86px;border-radius:12px;background:#fff;font:600 38px Inter;font-style:normal;display:flex;align-items:center;justify-content:center;color:#0f172a;box-shadow:0 3px 0 #9aa0aa}
.kb i.h{background:#0d9488;color:#fff}
.gain{background:#0d9488;box-shadow:0 12px 0 #075e56}
.endc .c{background:#5eead4;color:#0f172a}
.endc .b{color:#99f6e4}
.hook{position:absolute;left:70px;top:330px;padding:14px 28px;border-radius:22px;background:#fff;border:5px solid #0f172a;box-shadow:8px 8px 0 #0f172a;font:900 54px/1.12 Inter;color:#0f172a;z-index:8;white-space:nowrap}
.hook b{color:#0d9488}
.scr{position:absolute;left:840px;top:760px;width:110px;height:360px;z-index:8}
.down{position:absolute;padding:12px 26px;border-radius:18px;background:#0d9488;color:#fff;font:900 50px Inter;box-shadow:8px 8px 0 #0f172a;white-space:nowrap;z-index:8}
'''
ROWS = ''.join(f'<div class="row"><span class="ic">{icon(ic, 84)}</span>{lab}<span class="p">{pr}</span></div>' for ic, lab, pr in [('Bottines', 'Bottines', '36,00 €'), ('Casque', 'Casque audio', '22,00 €')])
KEYS = ''.join(f'<i{" class=\"h\"" if k in "hzkl" else ""}>{k}</i>' for k in 'azertyuiopqsdfghjklmwxcvbn')


def top_view():
    """Haut du panier : la case code promo est hors de l'écran, sous les recommandations."""
    return phone(f'''<div class="hd">Mon panier Hacoo</div>{ROWS}
     <div class="rc">Recommandé pour toi</div><div class="tiles"><div></div><div></div><div></div><div></div></div>''')


def bottom_view(field='', disc=False, total='58,00 €', old=None, gd=None, gin=None):
    """Bas du panier (après avoir descendu) : la case code promo Hacoo, Appliquer et le total."""
    f = f'<div class="fd on"><span class="cd">{field}</span></div>' if field else '<div class="fd" style="color:#94a3b8">Ajouter un code</div>'
    d = ''
    if disc:
        a = f' data-g="{gd}" data-fx="right"' if gd else ''
        d = f'<div class="disc"{a}>Code promo Hacoo (-14 %)<span class="p">-8,12 €</span></div>'
    o = f'<s>{old}</s>' if old else ''
    a = f' data-g="{gin}" data-fx="up"' if gin else ''
    return phone(f'''<div{a}><div class="tiles cut"><div></div><div></div></div>
     <div class="lb">Sous-total (2 articles)</div><div class="row" style="height:80px">Bottines + casque<span class="p">58,00 €</span></div>
     <div class="lb">Code promo Hacoo</div>
     <div class="fr2">{f}<div class="ap2">Appliquer</div></div>{d}
     <div class="tot"><span>Total</span><span>{o}<b>{total}</b></span></div><div class="ex">prix d'exemple</div></div>''')


def kbd(ph):
    return ph[:-12] + '<div class="kb" data-g="4.1" data-fx="up">' + KEYS + '</div></div></div>'


BODY = search('code promo hacoo') + '''
  <div class="scene" data-s="0">''' + top_view() + '''
   <div class="hook">Où est la case<br><b>code promo Hacoo</b> ?</div>
   <div class="stk" style="left:600px;top:1180px;transform:rotate(5deg);font-size:90px">?!</div></div>
  <div class="scene" data-s="1" data-in="right"><div class="zm" data-zg="1.1" data-zs="1.2" style="transform-origin:470px 700px">''' + top_view() + '''</div>
   <div class="stk" style="left:520px;top:880px;transform:rotate(-4deg)" data-g="1.2" data-fx="stamp">58,00 €</div></div>
  <div class="scene" data-s="2" data-in="up">''' + step(1, 3, 'TOUT EN BAS') + bottom_view(gin='2.0') + hand(470, 1050, '2.1', (0, 380)) + '''
   <div class="down" style="left:330px;top:1265px" data-g="2.1" data-fx="pop">↓ SOUS LE PANIER</div></div>
  <div class="scene" data-s="3" data-in="right">''' + step(2, 3, 'LA CASE') + '''
   <div class="zm" data-zg="3.1" data-zs="1.18" style="transform-origin:360px 1000px">''' + bottom_view() + hand(330, 1000, '3.1') + '''</div>
   <div class="stk" style="left:150px;top:1268px" data-g="3.2" data-fx="pop">CODE PROMO HACOO</div></div>
  <div class="scene" data-s="4" data-in="right">''' + step(3, 3, 'HZKLINK + APPLIQUER') + '''
   <div class="zm" data-zg="4.1" data-zs="1.1" style="transform-origin:360px 1000px">''' + kbd(bottom_view('<span data-g="4.1" data-fx="type">hzklink</span>')) + hand(660, 1000, '4.2') + '''</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + bottom_view('hzklink', True, '49,88 €', '58,00 €', gd='5.0') + '''
   <div class="gain" style="left:590px;top:585px" data-g="5.0" data-fx="stamp">-8,12 €</div>
   <div class="gain" style="left:300px;top:1180px;font-size:110px" data-g="5.2" data-fx="stamp" data-slow="5.2">49,88 €</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + bottom_view('hzklink', True, '49,88 €', '58,00 €') + '''
   <div class="endc" data-g="6.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div><div class="b">liens des articles tendance en bio</div></div>
   <div class="cond" style="top:1290px;background:#fff" data-g="6.1" data-fx="fade">Prix d'exemple · -14 % avec le code promo Hacoo hzklink sur l'appli Hacoo · Offre soumise aux conditions en vigueur</div></div>
'''
