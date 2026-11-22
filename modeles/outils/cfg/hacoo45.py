import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qg_ecran import *
from hacoo_items import icon
# Hacoo n°3 du 22/11/2026 (tâche « 2 vidéos Hacoo en plus ») - style E « Écran d'appli en gros plan », accent orange mandarine.
# Format F4 « argent laissé sur la table » + tuto 3 étapes : « 10 € oubliés sur ce panier Hacoo ».
# Panier plein (74,00 €) + « ATTENDS ! » -> zoom sur les articles -> case code promo vide -> ÉTAPE 1 ouvrir la case code promo Hacoo
# -> ÉTAPE 2 hzklink + Appliquer -> ÉTAPE 3 la ligne -14 % -> -10,36 € / 63,64 € (ralenti) -> fin « enregistre ».
# Téléphone DESSINÉ, générique, sans logo ni interface copiée.
# Prix d'exemple : pyjama 31 € + chaussons 16 € + plaid 27 € = 74,00 € ; -14 % = 10,36 € (74 x 0,14) ; total 63,64 € (74 x 0,86).
# Voix : Speko Leo (xai), speed 1.08, une synthèse par réplique, silences coupés (internes plafonnés à 0,16 s), atempo 1.12.
NAME = 'hacoo45'
TITLE = 'Hacoo 10 euros sur la table mandarine'
ROOT = ':root{--bg:#f8ece2}'
LINES = [
 ("Attends ! Sur ce panier de l'appli Hacou, tu laisses dix euros sur la table.", [("Attends !", None), ("Sur ce panier", None), ("de l'appli <em>Hacoo</em>,", None), ("tu laisses <em>10 €</em>", None), ("sur la table.", None)]),
 ("Pyjama, chaussons, plaid : soixante-quatorze euros.", [("Pyjama, chaussons,", None), ("plaid :", None), ("<em>74 €</em>.", None)]),
 ("Le problème ? La case code promo est restée vide.", [("Le problème ?", None), ("La case code promo", None), ("est restée <em>vide</em>.", None)]),
 ("Étape un : tu ouvres la case code promo Hacou.", [("<em>Étape 1</em> :", None), ("tu ouvres la case", None), ("<em>code promo Hacoo</em>.", None)]),
 ("Étape deux : tu tapes H, Z, K, link, et tu appuies sur Appliquer.", [("<em>Étape 2</em> :", None), ("tu tapes <i>hzklink</i>,", None), ("et tu appuies", None), ("sur <em>Appliquer</em>.", None)]),
 ("Étape trois : la ligne moins quatorze pour cent apparaît.", [("<em>Étape 3</em> :", None), ("la ligne <em>-14&nbsp;%</em>", None), ("apparaît.", None)]),
 ("Tu économises dix euros trente-six. Tu paies soixante-trois euros soixante-quatre.", [("Tu économises", None), ("<i>10,36 €</i>.", None), ("Tu paies", None), ("<em>63,64 €</em>.", None)]),
 ("Prix d'exemple. Enregistre la vidéo. Code promo Hacou : H, Z, K, link.", [("Prix d'exemple.", None), ("Enregistre la vidéo.", None), ("<em>Code promo Hacoo</em> :", None), ("<i>hzklink</i>.", None)]),
]
SPLITS = [(0.2, 3.411), (3.861, 6.782), (7.232, 9.909), (10.359, 13.047), (13.497, 17.92), (18.37, 21.207), (21.657, 25.461), (25.911, 30.805)]
TAIL = 2.3
GAP = 0.2
MINLEN = 1.8

CSS = '''
body,#stage{background:#f8ece2}
#bgtex{background:radial-gradient(circle at 1px 1px,rgba(150,60,10,.10) 2px,transparent 2.5px) 0 0/44px 44px,linear-gradient(160deg,#fdf6f0 0%,#f6e6d8 60%,#f1dccb 100%)}
.search .cur{background:#ea580c}
.rip{border-color:#ea580c}
.ap .row{height:112px}
.ap .row .p{margin-left:auto;font:900 40px Inter;color:#0f172a}
.ap .row .ic{width:92px;height:92px;border-radius:20px;background:#f4f4f6;display:flex;align-items:center;justify-content:center;flex:none}
.ap .fr2{display:flex;gap:16px;align-items:center}
.ap .fr2 .fd{flex:1}
.ap .ap2{height:104px;padding:0 26px;border-radius:24px;background:#ea580c;color:#fff;font:900 34px Inter;display:flex;align-items:center;white-space:nowrap}
.ap .fd.on{border-color:#ea580c;background:#fff1e6}
.ap .fd.bl{border-color:#e11d48;background:#fff1f2}
.ap .fd .cd{font:900 46px 'DejaVu Sans Mono',monospace;color:#0f172a}
.ap .disc{height:92px;display:flex;align-items:center;font:900 28px Inter;color:#c2410c;border-bottom:3px solid #eef2f7;white-space:nowrap}
.ap .disc .p{margin-left:auto;font:900 40px Inter;color:#c2410c}
.ap .tot{display:flex;align-items:baseline;justify-content:space-between;margin-top:18px;font:900 44px Inter;white-space:nowrap}
.ap .tot b{font:900 76px Inter;letter-spacing:-2px}
.ap .tot s{font:800 38px Inter;color:#94a3b8;text-decoration-color:#ea580c;text-decoration-thickness:5px;margin-right:14px}
.ap .ex{font:700 26px Inter;color:#94a3b8;margin-top:4px}
.ap .pay{height:108px;border-radius:54px;background:#0f172a;color:#fff;font:900 42px Inter;display:flex;align-items:center;justify-content:center;margin-top:22px}
.gain{background:#ea580c;box-shadow:0 12px 0 #9a3412}
.endc .c{background:#ffd43b;color:#0f172a}
.endc .b{color:#fdba74}
.hook{position:absolute;left:70px;top:330px;padding:14px 28px;border-radius:22px;background:#fff;border:5px solid #0f172a;box-shadow:8px 8px 0 #0f172a;font:900 54px/1.12 Inter;color:#0f172a;z-index:8;white-space:nowrap}
.hook b{color:#ea580c}
.err{position:absolute;left:70px;top:326px;height:72px;padding:0 30px;border-radius:36px;background:#ea580c;color:#fff;font:900 40px Inter;display:flex;align-items:center;gap:16px;letter-spacing:1px;z-index:8;white-space:nowrap;box-shadow:6px 6px 0 #0f172a}
.err i{font-style:normal;width:46px;height:46px;border-radius:50%;background:#fff;color:#ea580c;display:flex;align-items:center;justify-content:center;font:900 30px Inter}
.wait{position:absolute;left:330px;top:560px;padding:12px 34px;border-radius:24px;background:#e11d48;color:#fff;font:900 80px Inter;border:6px solid #0f172a;box-shadow:10px 10px 0 #0f172a;z-index:9;white-space:nowrap;transform:rotate(-5deg)}
.x{position:absolute;width:120px;height:120px;border-radius:50%;background:#e11d48;color:#fff;font:900 80px Inter;display:flex;align-items:center;justify-content:center;border:6px solid #0f172a;z-index:9}
.stk.cb{background:#fff;color:#ea580c}
'''

ITEMS = [('Pyjama', 'Pyjama', '31,00 €'), ('Chaussons', 'Chaussons', '16,00 €'), ('Plaid', 'Plaid', '27,00 €')]
ROWS = ''.join(f'<div class="row"><span class="ic">{icon(ic, 80)}</span>{lab}<span class="p">{pr}</span></div>' for ic, lab, pr in ITEMS)


def cart_top():
    """Panier : 3 articles, total, Payer."""
    return phone(f'''<div class="hd">Ma commande Hacoo</div>{ROWS}
     <div class="tot"><span>Total</span><span><b>74,00 €</b></span></div><div class="ex">prix d'exemple</div><div class="pay">Payer</div>''')


def cart_code(field='', cls='', disc=False, total='74,00 €', old=None, gd=None):
    """Bas de la commande : case code promo Hacoo, Appliquer, ligne de réduction, total, Payer."""
    f = f'<div class="fd on {cls}"><span class="cd">{field}</span></div>' if field else f'<div class="fd {cls}" style="color:#94a3b8">Ajouter un code</div>'
    d = ''
    if disc:
        a = f' data-g="{gd}" data-fx="right"' if gd else ''
        d = f'<div class="disc"{a}>Code promo Hacoo (-14 %)<span class="p">-10,36 €</span></div>'
    o = f'<s>{old}</s>' if old else ''
    return phone(f'''<div class="hd">Ma commande Hacoo</div>
     <div class="lb">Sous-total</div><div class="row" style="height:80px">3 articles<span class="p">74,00 €</span></div>
     <div class="lb">Code promo Hacoo</div>
     <div class="fr2">{f}<div class="ap2">Appliquer</div></div>{d}
     <div class="tot"><span>Total</span><span>{o}<b>{total}</b></span></div><div class="ex">prix d'exemple</div><div class="pay">Payer</div>''')


BODY = search('code promo hacoo') + '''
  <div class="scene" data-s="0">''' + cart_top() + '''
   <div class="hook">10 € oubliés sur ce<br>panier <b>Hacoo</b></div>
   <div class="wait" style="left:540px;top:450px;font-size:56px" data-g="0.0" data-fx="stamp">ATTENDS !</div>
   <div class="stk" style="left:150px;top:1170px;transform:rotate(-4deg)" data-g="0.3" data-fx="pop">10 € SUR LA TABLE</div></div>
  <div class="scene" data-s="1" data-in="right"><div class="zm" data-zg="1.0" data-zs="1.14" style="transform-origin:470px 700px">''' + cart_top() + '''</div>
   <div class="stk cb" style="left:470px;top:1180px;transform:rotate(3deg)" data-g="1.2" data-fx="stamp">74,00 €</div></div>
  <div class="scene" data-s="2" data-in="up"><div class="zm" data-zg="2.1" data-zs="1.12" style="transform-origin:380px 820px">''' + cart_code(cls='bl') + '''</div>
   <div class="x" style="left:700px;top:1150px" data-g="2.2" data-fx="stamp">✗</div>
   <div class="stk" style="left:120px;top:1000px;transform:rotate(-3deg)" data-g="2.2" data-fx="pop">CASE VIDE</div></div>
  <div class="scene" data-s="3" data-in="right">''' + step(1, 3, 'LA CASE', '3.0') + cart_code() + hand(380, 820, '3.1', (260, 420)) + '''
   <div class="stk cb" style="left:120px;top:1000px;font-size:44px" data-g="3.2" data-fx="pop">CODE PROMO HACOO</div></div>
  <div class="scene" data-s="4" data-in="right">''' + step(2, 3, 'LE CODE', '4.0') + '''<div class="zm" data-zg="4.1" data-zs="1.12" style="transform-origin:380px 820px">''' + cart_code('<span data-g="4.1" data-fx="type">hzklink</span>') + '''</div>
   ''' + hand(640, 895, '4.3', (60, 360)) + '''
   <div class="stk" style="left:150px;top:1180px;transform:rotate(-3deg);font-size:46px" data-g="4.3" data-fx="pop">+ APPLIQUER</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + step(3, 3, 'LA RÉDUCTION', '5.0') + cart_code('hzklink', disc=True, gd='5.1') + hand(700, 1010, '5.1', (260, 420)) + '''
   <div class="stk cb" style="left:560px;top:700px;transform:rotate(4deg)" data-g="5.1" data-fx="stamp">-14 %</div></div>
  <div class="scene" data-s="6" data-in="pop"><div class="zm" data-zg="6.0" data-zs="1.08" style="transform-origin:470px 900px">''' + cart_code('hzklink', disc=True, total='63,64 €', old='74,00 €') + '''</div>
   <div class="gain" style="left:520px;top:600px" data-g="6.1" data-fx="stamp">-10,36 €</div>
   <div class="gain" style="left:280px;top:1225px;font-size:100px" data-g="6.3" data-fx="stamp" data-slow="6.3">63,64 €</div></div>
  <div class="scene" data-s="7" data-in="pop">''' + cart_code('hzklink', disc=True, total='63,64 €', old='74,00 €') + '''
   <div class="endc" data-g="7.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div><div class="b">📌 enregistre · liens des articles tendance en bio</div></div>
   <div class="cond" style="top:1150px;background:#fff" data-g="7.1" data-fx="fade">Prix d'exemple · -14 % avec le code promo Hacoo hzklink sur l'appli Hacoo · Offre soumise aux conditions en vigueur</div></div>
'''
