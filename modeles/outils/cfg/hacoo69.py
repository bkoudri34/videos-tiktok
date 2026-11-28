import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qg_ecran import *
from hacoo_items import icon
# Hacoo, 28/11/2026, vidéo 3 (compte affiliation, tâche « 2 vidéos Hacoo en plus ») - style E « Écran d'appli en gros plan », accent orange mandarine.
# Format « petit panier » : « Petit panier ? Le code promo marche aussi » : téléphone DESSINÉ générique (en-tête « Ma commande »), case code promo vide
# entourée dès la 1re image + « ATTENDS » -> 3 articles d'exemple (26,00 €) -> « pour si peu » : la case reste vide -> hzklink tapé + Appliquer
# -> la ligne -14 % (-3,64 €) surgit -> 26,00 € barré -> 22,36 € (le seul ralenti) -> fin « enregistre ».
# RÈGLE DU 26/11 : le nom de l'appli n'est JAMAIS écrit (écran, sous-titres) : seulement dit à l'oral (« l'appli Hacou », « code promo Hacou »).
# Prix d'exemple : bougie 9 € + chaussettes 6 € + coque 11 € = 26,00 € ; -14 % = 3,64 € (26 x 0,14) ; total 22,36 € (26 x 0,86 ; 26 - 3,64).
# Voix : Speko Manon (cartesia), speed 1.08, une synthèse par réplique, silences internes plafonnés à 0,16 s, atempo 1.15, -19 dB moyen.
NAME = 'hacoo69'
TITLE = 'Petit panier mandarine'
ROOT = ':root{--bg:#fbf1ea}'
LINES = [
 ("Attends ! Ton panier sur l'appli Hacou est petit ? Le code promo marche quand même.", [("<em>Attends&nbsp;!</em>", None), ("Ton panier", None), ("sur l'appli", "sur l'appli Hacou"), ("est petit&nbsp;?", None), ("Le code promo", None), ("marche <em>quand&nbsp;même.</em>", None)]),
 ("Bougie, chaussettes et une coque : vingt-six euros d'exemple.", [("Bougie,", None), ("chaussettes", None), ("et une coque :", None), ("<em>26&nbsp;€</em> d'exemple.", "vingt-six euros d'exemple.")]),
 ("Pour si peu, beaucoup laissent la case code promo vide.", [("Pour si peu,", None), ("beaucoup laissent", None), ("la case code promo", None), ("<em>vide.</em>", None)]),
 ("Avant de payer, code promo Hacou : H, Z, K, link. Puis Appliquer.", [("Avant de payer,", None), ("<em>code promo</em>", "code promo Hacou :"), ("<i>hzklink</i>.", "H, Z, K, link."), ("Puis <em>Appliquer.</em>", None)]),
 ("Moins quatorze pour cent : trois euros et soixante-quatre centimes de moins.", [("<em>-14&nbsp;%</em> :", "Moins quatorze pour cent :"), ("<em>3,64&nbsp;€</em>", "trois euros et soixante-quatre centimes"), ("de moins.", None)]),
 ("Tu paies vingt-deux euros et trente-six centimes, au lieu de vingt-six.", [("Tu paies", None), ("<em>22,36&nbsp;€,</em>", "vingt-deux euros et trente-six centimes,"), ("au lieu de 26.", "au lieu de vingt-six.")]),
 ("Petit ou gros panier : code promo Hacou, H, Z, K, link. Enregistre la vidéo.", [("Petit ou gros panier :", None), ("<em>code promo</em>", "code promo Hacou,"), ("<i>hzklink</i>.", "H, Z, K, link."), ("<em>Enregistre</em> la vidéo.", None)]),
]
SPLITS = [(0.2, 3.679), (4.129, 6.95), (7.4, 10.095), (10.545, 15.56), (16.01, 19.361), (19.811, 23.13), (23.579, 28.982)]
TAIL = 1.8
GAP = 0.2
MINLEN = 1.8

P = '#d9480f'   # orange mandarine
PL = '#fff0e6'
CSS = '''
body,#stage{background:#fbf1ea}
#cam{transform-origin:470px 250px}
#bgtex{background:radial-gradient(circle at 1px 1px,rgba(217,72,15,.10) 2px,transparent 2.5px) 0 0/44px 44px,linear-gradient(160deg,#fffaf6 0%,#f8e8dc 60%,#f1dccb 100%)}
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
.gain{background:''' + P + ''';box-shadow:0 12px 0 #7a2606}
.endc{background:#3a1606}
.endc .c{background:#ffd43b;color:#0f172a}
.endc .b{color:#ffc9a8}
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

ITEMS = [('Bougie', 'Bougie', '9,00 €'), ('Chaussettes', 'Chaussettes', '6,00 €'), ('Coque', 'Coque', '11,00 €')]
ROWS = ''.join(f'<div class="row"><span class="ic">{icon(ic, 74)}</span>{lab}<span class="p">{pr}</span></div>' for ic, lab, pr in ITEMS)


def cart(field='', cls='fd on', err=False, disc=False, total='26,00 €', old=None, gd=None):
    f = f'<div class="{cls}"><span class="cd">{field}</span></div>' if field else f'<div class="fd hl" style="color:#94a3b8">Ajouter un code</div>'
    e = '<div class="er">⚠ code non appliqué</div>' if err else ''
    d = ''
    if disc:
        a = f' data-g="{gd}" data-fx="right"' if gd else ''
        d = f'<div class="disc"{a}>Code promo (-14 %)<span class="p">-3,64 €</span></div>'
    o = f'<s>{old}</s>' if old else ''
    return phone(f'''<div class="hd">Ma commande</div>{ROWS}
     <div class="lb">Code promo</div>
     <div class="fr2">{f}<div class="ap2">Appliquer</div></div>{e}{d}
     <div class="tot"><span>Total</span><span>{o}<b>{total}</b></span></div><div class="ex">prix d'exemple</div>''')


def nums(k):
    return '<div class="num3">' + ''.join(f'<span class="{"on" if i == k else ""}">{i}</span>' for i in (1, 2, 3)) + '</div>'


FIELDY = 1080
EMPTY = cart()
DONE = cart('hzklink', disc=True, total='22,36 €', old='26,00 €')
CSS += """
.ap .row.hlr{background:#fff0e6;border-radius:18px}
"""
BODY = search('petit panier, code promo ?') + '''
  <div class="scene" data-s="0">''' + EMPTY + '''
   <div class="hook">Petit panier ?<br>Le <b>code promo</b> marche aussi</div>
   <div class="ring" style="left:110px;top:1035px;width:560px;height:150px"></div>
   <div class="wait" style="left:480px;top:600px" data-g="0.0" data-fx="stamp">ATTENDS</div></div>
  <div class="scene" data-s="1" data-in="right"><div class="zm" data-zg="1.0" data-zs="1.12" style="transform-origin:470px 800px">''' + EMPTY + '''</div>
   <div class="stk pl" style="left:170px;top:470px;transform:rotate(-3deg);font-size:52px" data-g="1.0" data-fx="stamp">3 PETITS ARTICLES</div></div>
  <div class="scene" data-s="2" data-in="left"><div class="zm" data-zg="2.0" data-zs="1.2" style="transform-origin:470px ''' + str(FIELDY) + '''px">''' + EMPTY + '''
   <div class="ring" style="left:110px;top:1035px;width:560px;height:150px" data-g="2.2" data-fx="pop"></div></div>
   <div class="stk no" style="left:160px;top:470px;transform:rotate(-3deg);font-size:58px" data-g="2.0" data-fx="stamp">« pour si peu… » ✖</div></div>
  <div class="scene" data-s="3" data-in="right">''' + '''<div class="zm" data-zg="3.1" data-zs="1.08" style="transform-origin:700px ''' + str(FIELDY) + '''px">''' + cart('<span data-g="3.2" data-fx="type">hzklink</span>') + hand(735, FIELDY, '3.3', (200, 380)) + '''</div>
   <div class="stk ye" style="left:130px;top:450px;transform:rotate(-2deg);font-size:54px" data-g="3.1" data-fx="stamp">CODE PROMO : hzklink</div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="zm" data-zg="4.0" data-zs="1.14" style="transform-origin:470px 1180px">''' + cart('hzklink', disc=True, total='26,00 €', gd='4.0') + '''
   <div class="ring" style="left:130px;top:1150px;width:720px;height:110px" data-g="4.1" data-fx="pop"></div></div>
   <div class="stk pl" style="left:190px;top:470px;transform:rotate(-3deg);font-size:54px" data-g="4.1" data-fx="stamp">-14 % = -3,64 €</div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="zm" data-zg="5.0" data-zs="1.04" style="transform-origin:470px 1000px">''' + DONE + '''</div>
   <div class="stk cb" style="left:150px;top:450px;transform:rotate(-2deg);font-size:44px" data-g="5.0" data-fx="pop">26,00 € → -3,64 €</div>
   <div class="gain" style="left:250px;top:580px;font-size:120px" data-g="5.1" data-fx="stamp" data-slow="5.1">22,36 €</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + EMPTY + '''
   <div class="abs" style="inset:0;background:rgba(251,241,234,.92);z-index:7"></div>
   <div class="endc" style="top:470px" data-g="6.0" data-fx="up"><div class="k">CODE PROMO</div><div class="c">hzklink</div><div class="d">-14 % avec le code hzklink</div><div class="b">petit ou gros panier · liens des articles tendance en bio</div></div>
   <div class="cond" style="top:1000px;height:200px;display:flex;align-items:center;justify-content:center;font-size:30px;background:#fff;border:3px solid #d9480f" data-g="6.0" data-fx="fade">Prix d'exemple · -14 % avec le code promo hzklink · Offre soumise aux conditions en vigueur</div></div>
'''
