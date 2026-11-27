import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qg_ecran import *
from hacoo_items import icon
# Hacoo n°1 du 27/11/2026 (tâche du jour, vidéo 1) - style E « Écran d'appli en gros plan », accent bleu océan (brief veille du 27/11).
# Format dépannage : « Code promo refusé ? Vérifie ces 3 trucs » : champ rempli avec message rouge « code non appliqué » dès la 1re image
# + « ATTENDS » -> 1 pas d'espace (espace final barré) -> 2 tout attaché (« HZK LINK » barré -> hzklink) -> 3 appuie sur Appliquer
# -> la ligne -14 % surgit dans le récapitulatif -> 59,00 € barré -> 50,74 € (le seul ralenti) -> fin « enregistre ».
# Téléphone DESSINÉ, générique (en-tête neutre « Ma commande »), aucun nom ni logo d'appli.
# RÈGLE DU 26/11 : le nom de l'appli n'est JAMAIS écrit (écran, sous-titres) : seulement dit à l'oral (« l'appli Hacou », « code promo Hacou »).
# Prix d'exemple : survêt 38 € + casquette 15 € + chaussettes 6 € = 59,00 € ; -14 % = 8,26 € (59 x 0,14) ; total 50,74 € (59 x 0,86).
# Voix : Speko Manon (cartesia), speed 1.08, une synthèse par réplique, silences internes plafonnés à 0,16 s, atempo 1.2, -19 dB moyen ;
# répliques 2, 6 et 7 raccourcies (durée 33,7 s -> 28,3 s de voix).
NAME = 'hacoo63'
TITLE = 'Code promo refuse ocean'
ROOT = ':root{--bg:#eaf3f8}'
LINES = [
 ("Attends ! Sur l'appli Hacou, ton code promo ne passe pas ? Vérifie ces trois trucs.", [("<em>Attends&nbsp;!</em>", None), ("Sur l'appli,", "Sur l'appli Hacou,"), ("ton code promo", None), ("ne passe pas&nbsp;?", None), ("Vérifie ces", None), ("<em>3&nbsp;trucs.</em>", "trois trucs.")]),
 ("Un : pas d'espace avant ou après le code.", [("<em>Un :</em>", None), ("pas d'espace", None), ("avant ou après", None), ("le code.", None)]),
 ("Deux : tape-le tout attaché. Code promo Hacou : H, Z, K, link.", [("<em>Deux :</em>", None), ("tape-le", None), ("tout attaché.", None), ("<em>Code promo</em>", "Code promo Hacou :"), ("<i>hzklink</i>.", "H, Z, K, link.")]),
 ("Trois : appuie bien sur Appliquer, avant de payer.", [("<em>Trois :</em>", None), ("appuie bien", None), ("sur <em>Appliquer</em>,", None), ("avant de payer.", None)]),
 ("Dans le récapitulatif, une nouvelle ligne moins quatorze pour cent doit apparaître.", [("Dans le", None), ("récapitulatif,", None), ("une nouvelle ligne", None), ("<em>-14&nbsp;%</em>", "moins quatorze pour cent"), ("doit apparaître.", None)]),
 ("Sur cinquante-neuf euros d'exemple, tu paies cinquante euros et soixante-quatorze centimes.", [("Sur <em>59&nbsp;€</em>", "Sur cinquante-neuf euros"), ("d'exemple,", None), ("tu paies", None), ("<em>50,74&nbsp;€.</em>", "cinquante euros et soixante-quatorze centimes.")]),
 ("Enregistre la vidéo. Code promo Hacou, H, Z, K, link.", [("<em>Enregistre</em>", None), ("la vidéo.", None), ("<em>Code promo</em>", "Code promo Hacou,"), ("<i>hzklink</i>.", "H, Z, K, link.")]),
]
SPLITS = [(0.2, 4.069), (4.519, 6.807), (7.257, 11.68), (12.13, 14.232), (14.682, 18.478), (18.928, 22.915), (23.365, 28.089)]
TAIL = 1.6
GAP = 0.2
MINLEN = 1.8

P = '#0b6fa4'   # bleu océan
PL = '#dff0fa'
CSS = '''
body,#stage{background:#eaf3f8}
#cam{transform-origin:470px 250px}
#bgtex{background:radial-gradient(circle at 1px 1px,rgba(11,111,164,.10) 2px,transparent 2.5px) 0 0/44px 44px,linear-gradient(160deg,#f6fbfe 0%,#e2eff7 60%,#d3e6f2 100%)}
.search .cur{background:''' + P + '''}
.rip{border-color:''' + P + '''}
#sub em{color:#ffd43b}
.ap .row{height:104px}
.ap .row .p{margin-left:auto;font:900 40px Inter;color:#0f172a}
.ap .row .ic{width:86px;height:86px;border-radius:20px;background:#f1f5f9;display:flex;align-items:center;justify-content:center;flex:none}
.ap .fr2{display:flex;gap:16px;align-items:center}
.ap .fr2 .fd{flex:1}
.ap .ap2{height:104px;padding:0 26px;border-radius:24px;background:''' + P + ''';color:#fff;font:900 34px Inter;display:flex;align-items:center;white-space:nowrap}
.ap .fd.on{border-color:''' + P + ''';background:''' + PL + '''}
.ap .fd.err{border-color:#e11d48;background:#fff1f4}
.ap .fd .cd{font:900 46px 'DejaVu Sans Mono',monospace;color:#0f172a;white-space:pre}
.ap .fd .sp{display:inline-block;width:30px;height:46px;background:#fecdd3;border-radius:6px;vertical-align:-6px;margin-left:2px}
.ap .er{font:800 28px Inter;color:#e11d48;margin-top:8px}
.ap .disc{height:88px;display:flex;align-items:center;font:900 30px Inter;color:''' + P + ''';border-bottom:3px solid #eef2f7;white-space:nowrap}
.ap .disc .p{margin-left:auto;font:900 40px Inter;color:''' + P + '''}
.ap .tot{display:flex;align-items:baseline;justify-content:space-between;margin-top:16px;font:900 44px Inter;white-space:nowrap}
.ap .tot b{font:900 72px Inter;letter-spacing:-2px}
.ap .tot s{font:800 36px Inter;color:#94a3b8;text-decoration-color:''' + P + ''';text-decoration-thickness:5px;margin-right:14px}
.ap .ex{font:700 26px Inter;color:#94a3b8;margin-top:4px}
.gain{background:''' + P + ''';box-shadow:0 12px 0 #053a57}
.endc{background:#062a3f}
.endc .c{background:#ffd43b;color:#0f172a}
.endc .b{color:#9fd4f2}
.step{background:''' + P + '''}
.hook{position:absolute;left:70px;top:326px;padding:12px 26px;border-radius:22px;background:#fff;border:5px solid #0f172a;box-shadow:8px 8px 0 #0f172a;font:900 50px/1.12 Inter;color:#0f172a;z-index:8;white-space:nowrap}
.hook b{color:#e11d48}
.wait{position:absolute;padding:12px 30px;border-radius:24px;background:#e11d48;color:#fff;font:900 70px Inter;border:6px solid #0f172a;box-shadow:10px 10px 0 #0f172a;z-index:9;white-space:nowrap;transform:rotate(-5deg)}
.stk.cb{background:#fff;color:''' + P + '''}
.stk.pl{background:''' + P + ''';color:#fff}
.stk.ye{background:#ffd43b;color:#0f172a;font-family:'DejaVu Sans Mono',monospace}
.stk.no{background:#fff;color:#94a3b8;text-decoration:line-through;text-decoration-color:#e11d48;text-decoration-thickness:8px}
.ring{position:absolute;border:8px solid #e11d48;border-radius:50%;z-index:9;transform:rotate(-3deg)}
.xbar{position:absolute;height:10px;border-radius:5px;background:#e11d48;z-index:9;transform:rotate(-20deg)}
.ap .fd.hl{border-color:#e11d48;border-width:6px;background:#fff1f4}
.num3{position:absolute;left:40px;top:470px;display:flex;flex-direction:column;gap:14px;z-index:8}
.num3 span{width:64px;height:64px;border-radius:50%;background:#fff;border:4px solid #0f172a;font:900 34px Inter;color:#0f172a;display:flex;align-items:center;justify-content:center}
.num3 span.on{background:''' + P + ''';color:#fff}
'''

ITEMS = [('Survêt', 'Survêt', '38,00 €'), ('Casquette', 'Casquette', '15,00 €'), ('Chaussettes', 'Chaussettes', '6,00 €')]
ROWS = ''.join(f'<div class="row"><span class="ic">{icon(ic, 74)}</span>{lab}<span class="p">{pr}</span></div>' for ic, lab, pr in ITEMS)


def cart(field='', cls='fd on', err=False, disc=False, total='59,00 €', old=None, gd=None):
    f = f'<div class="{cls}"><span class="cd">{field}</span></div>' if field else f'<div class="fd hl" style="color:#94a3b8">Ajouter un code</div>'
    e = '<div class="er">⚠ code non appliqué</div>' if err else ''
    d = ''
    if disc:
        a = f' data-g="{gd}" data-fx="right"' if gd else ''
        d = f'<div class="disc"{a}>Code promo (-14 %)<span class="p">-8,26 €</span></div>'
    o = f'<s>{old}</s>' if old else ''
    return phone(f'''<div class="hd">Ma commande</div>{ROWS}
     <div class="lb">Code promo</div>
     <div class="fr2">{f}<div class="ap2">Appliquer</div></div>{e}{d}
     <div class="tot"><span>Total</span><span>{o}<b>{total}</b></span></div><div class="ex">prix d'exemple</div>''')


def nums(k):
    return '<div class="num3">' + ''.join(f'<span class="{"on" if i == k else ""}">{i}</span>' for i in (1, 2, 3)) + '</div>'


FIELDY = 1080
ERR = cart('hzklink<span class="sp"></span>', cls='fd err', err=True)
DONE = cart('hzklink', disc=True, total='50,74 €', old='59,00 €')
BODY = search('code promo refusé ?') + '''
  <div class="scene" data-s="0">''' + ERR + '''
   <div class="hook">Code promo <b>refusé</b> ?<br>Vérifie ces 3 trucs</div>
   <div class="ring" style="left:130px;top:1040px;width:720px;height:200px"></div>
   <div class="wait" style="left:480px;top:600px" data-g="0.0" data-fx="stamp">ATTENDS</div></div>
  <div class="scene" data-s="1" data-in="right">''' + step(1, 3, "PAS D'ESPACE", '1.0') + nums(1) + '''<div class="zm" data-zg="1.1" data-zs="1.22" style="transform-origin:470px ''' + str(FIELDY) + '''px">''' + ERR + '''
   <div class="xbar" style="left:455px;top:1086px;width:70px" data-g="1.2" data-fx="strike"></div></div>
   <div class="stk pl" style="left:170px;top:470px;transform:rotate(-3deg);font-size:52px" data-g="1.1" data-fx="stamp">① PAS D'ESPACE</div>
   <div class="stk cb" style="left:250px;top:600px;transform:rotate(2deg);font-size:40px" data-g="1.3" data-fx="pop">ni avant, ni après</div></div>
  <div class="scene" data-s="2" data-in="left">''' + step(2, 3, 'TOUT ATTACHÉ', '2.0') + nums(2) + '''<div class="zm" data-zg="2.0" data-zs="1.06" style="transform-origin:470px 1000px">''' + cart('<span data-g="2.4" data-fx="type">hzklink</span>') + '''</div>
   <div class="stk no" style="left:200px;top:470px;transform:rotate(-3deg);font-size:64px" data-g="2.1" data-fx="stamp">HZK LINK</div>
   <div class="stk ye" style="left:330px;top:640px;transform:rotate(2deg);font-size:72px" data-g="2.4" data-fx="stamp">hzklink</div>
   <div class="stk cb" style="left:150px;top:800px;transform:rotate(-1deg);font-size:40px" data-g="2.3" data-fx="pop">CODE PROMO : hzklink</div></div>
  <div class="scene" data-s="3" data-in="right">''' + step(3, 3, 'APPLIQUER', '3.0') + nums(3) + '''<div class="zm" data-zg="3.1" data-zs="1.08" style="transform-origin:700px ''' + str(FIELDY) + '''px">''' + cart('hzklink') + hand(735, FIELDY, '3.2', (200, 380)) + '''</div>
   <div class="stk pl" style="left:140px;top:470px;transform:rotate(-3deg);font-size:50px" data-g="3.3" data-fx="stamp">AVANT DE PAYER</div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="zm" data-zg="4.2" data-zs="1.14" style="transform-origin:470px 1180px">''' + cart('hzklink', disc=True, total='59,00 €', gd='4.2') + '''
   <div class="ring" style="left:130px;top:1150px;width:720px;height:110px" data-g="4.3" data-fx="pop"></div></div>
   <div class="stk pl" style="left:190px;top:470px;transform:rotate(-3deg);font-size:54px" data-g="4.3" data-fx="stamp">NOUVELLE LIGNE -14 %</div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="zm" data-zg="5.0" data-zs="1.04" style="transform-origin:470px 1000px">''' + DONE + '''</div>
   <div class="stk cb" style="left:150px;top:450px;transform:rotate(-2deg);font-size:44px" data-g="5.0" data-fx="pop">59,00 € → -8,26 €</div>
   <div class="gain" style="left:250px;top:580px;font-size:120px" data-g="5.3" data-fx="stamp" data-slow="5.3">50,74 €</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + ERR + '''
   <div class="abs" style="inset:0;background:rgba(234,243,248,.9);z-index:7"></div>
   <div class="endc" style="top:470px" data-g="6.0" data-fx="up"><div class="k">CODE PROMO</div><div class="c">hzklink</div><div class="d">-14 % avec le code hzklink</div><div class="b">enregistre · liens des articles tendance en bio</div></div>
   <div class="cond" style="top:1000px;height:200px;display:flex;align-items:center;justify-content:center;font-size:30px;background:#fff;border:3px solid #0b6fa4" data-g="6.0" data-fx="fade">Prix d'exemple · -14 % avec le code promo hzklink · Offre soumise aux conditions en vigueur</div></div>
'''
