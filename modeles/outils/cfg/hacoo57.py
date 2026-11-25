
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qg_ecran import *
from hacoo_items import icon
# Hacoo n°3 du 25/11/2026 (tâche « 2 vidéos Hacoo en plus », vidéo 3) - style E « Écran d'appli en gros plan », accent rouge cerise.
# Format F8 « résultat d'abord » : « Ta commande Hacoo a cette ligne ? » : la ligne « Code promo Hacoo (-14 %) -6,58 € » entourée
# dès la 1re image, zoom dessus, puis 3 étapes (panier -> Commander / case code promo avant de payer / hzklink + Appliquer)
# -> la ligne apparaît, 40,42 € (ralenti) -> « pas de ligne, pas de réduction » + enregistre + carte de fin (boucle sur la ligne).
# Téléphone DESSINÉ, générique, sans logo ni interface copiée.
# Prix d'exemple : lampe 26 € + coque 13 € + carnet 8 € = 47,00 € ; -14 % = 6,58 € (47 x 0,14) ; total 40,42 € (47 x 0,86).
# Voix : Speko Manon (cartesia), speed 1.08, une synthèse par réplique, silences coupés (internes plafonnés à 0,16 s), atempo 1.17,
# 0,2 s au début et 0,45 s entre répliques.
NAME = 'hacoo57'
TITLE = 'Hacoo ligne cerise'
ROOT = ':root{--bg:#f7eef0}'
LINES = [
 ("Ta commande sur l'appli Hacou a cette ligne ? Sinon, tu paies trop.", [("Ta commande sur", None), ("l'appli <em>Hacoo</em>", None), ("a cette ligne ?", None), ("Sinon,", None), ("tu paies <em>trop</em>.", None)]),
 ("Regarde : six euros cinquante-huit de moins, juste avec un code.", [("Regarde :", None), ("<em>6,58&nbsp;€</em>", "six euros cinquante-huit"), ("de moins,", None), ("juste avec", None), ("un code.", None)]),
 ("Un, ton panier : lampe, coque et carnet, quarante-sept euros. Tu passes commande.", [("<em>Un,</em> ton panier :", None), ("lampe, coque", None), ("et carnet,", None), ("<em>47&nbsp;€</em>.", "quarante-sept euros."), ("Tu passes", None), ("commande.", None)]),
 ("Deux : avant de payer, trouve la case code promo.", [("<em>Deux :</em>", None), ("avant de payer,", None), ("trouve la case", None), ("<em>code promo</em>.", None)]),
 ("Trois : code promo Hacou, H, Z, K, link, et tu appuies sur Appliquer.", [("<em>Trois :</em>", None), ("<em>code promo Hacoo</em>,", None), ("<i>hzklink</i>,", "H, Z, K, link,"), ("et tu appuies", None), ("sur <em>Appliquer</em>.", None)]),
 ("La ligne apparaît. Tu paies quarante euros et quarante-deux centimes.", [("La ligne", None), ("apparaît.", None), ("Tu paies", None), ("<em>40,42&nbsp;€</em>", "quarante euros et quarante-deux centimes")]),
 ("Pas de ligne, pas de réduction. Enregistre cette vidéo, les liens sont dans ma bio.", [("Pas de ligne,", None), ("pas de <em>réduction</em>.", None), ("Enregistre cette vidéo,", None), ("liens dans ma bio.", "les liens sont dans ma bio.")]),
]
SPLITS = [(0.2, 3.38), (3.83, 6.821), (7.271, 11.148), (11.598, 14.006), (14.456, 19.398), (19.848, 23.282), (23.732, 27.891)]
TAIL = 1.6
GAP = 0.2
MINLEN = 1.8

P = '#c8103e'   # rouge cerise
PL = '#fde4ea'
CSS = '''
body,#stage{background:#f7eef0}
#cam{transform-origin:470px 250px}
#bgtex{background:radial-gradient(circle at 1px 1px,rgba(200,16,62,.10) 2px,transparent 2.5px) 0 0/44px 44px,linear-gradient(160deg,#fcf6f7 0%,#f3e3e6 60%,#ecd2d8 100%)}
.search .cur{background:''' + P + '''}
.rip{border-color:''' + P + '''}
#sub em{color:#ffd43b}
.ap .row{height:108px}
.ap .row .p{margin-left:auto;font:900 40px Inter;color:#0f172a}
.ap .row .ic{width:88px;height:88px;border-radius:20px;background:#f4f4f6;display:flex;align-items:center;justify-content:center;flex:none}
.ap .fr2{display:flex;gap:16px;align-items:center}
.ap .fr2 .fd{flex:1}
.ap .ap2{height:104px;padding:0 26px;border-radius:24px;background:''' + P + ''';color:#fff;font:900 34px Inter;display:flex;align-items:center;white-space:nowrap}
.ap .fd.on{border-color:''' + P + ''';background:''' + PL + '''}
.ap .fd .cd{font:900 46px 'DejaVu Sans Mono',monospace;color:#0f172a}
.ap .disc{height:88px;display:flex;align-items:center;font:900 28px Inter;color:''' + P + ''';border-bottom:3px solid #eef2f7;white-space:nowrap}
.ap .disc .p{margin-left:auto;font:900 40px Inter;color:''' + P + '''}
.ap .tot{display:flex;align-items:baseline;justify-content:space-between;margin-top:16px;font:900 44px Inter;white-space:nowrap}
.ap .tot b{font:900 72px Inter;letter-spacing:-2px}
.ap .tot s{font:800 36px Inter;color:#94a3b8;text-decoration-color:''' + P + ''';text-decoration-thickness:5px;margin-right:14px}
.ap .ex{font:700 26px Inter;color:#94a3b8;margin-top:4px}
.ap .pay{height:104px;border-radius:52px;background:#0f172a;color:#fff;font:900 40px Inter;display:flex;align-items:center;justify-content:center;margin-top:20px}
/* fiche article */
.ap .pic{height:420px;border-radius:34px;background:#f1edf2;display:flex;align-items:center;justify-content:center}
.ap .nm{font:900 42px Inter;margin-top:24px}
.ap .pr{font:900 52px Inter;color:''' + P + ''';margin-top:6px}
.ap .sz{display:flex;gap:16px;margin-top:22px}
.ap .sz span{flex:1;height:84px;border-radius:20px;border:4px solid #cbd5e1;display:flex;align-items:center;justify-content:center;font:900 36px Inter;color:#334155}
.ap .sz span.on{border-color:''' + P + ''';background:''' + PL + ''';color:''' + P + '''}
.ap .add{height:108px;border-radius:54px;background:''' + P + ''';color:#fff;font:900 40px Inter;display:flex;align-items:center;justify-content:center;margin-top:30px;white-space:nowrap}
.ap .gtab{display:flex;gap:14px;margin:6px 0 18px}
.ap .gtab span{height:64px;padding:0 22px;border-radius:32px;background:#f1f5f9;font:800 28px Inter;color:#64748b;display:flex;align-items:center;white-space:nowrap}
.ap .gtab span.on{background:''' + P + ''';color:#fff}
.ap table{width:100%;border-collapse:collapse;font:800 34px Inter}
.ap th{font:800 26px Inter;color:#64748b;text-align:left;padding:10px 6px;border-bottom:3px solid #e2e8f0}
.ap td{padding:18px 6px;border-bottom:3px solid #eef2f7}
.ap tr.hl td{background:''' + PL + ''';color:''' + P + '''}
.ap .rv{border-radius:26px;background:#f8fafc;border:3px solid #e2e8f0;padding:20px;margin-top:20px;display:flex;gap:20px;align-items:center}
.ap .rv .ph2{width:150px;height:150px;border-radius:20px;background:#ead9e6;flex:none;display:flex;align-items:center;justify-content:center}
.ap .rv .st{font:900 30px Inter;color:#f59e0b;letter-spacing:2px}
.ap .rv .tx{font:800 34px Inter;color:#0f172a;margin-top:8px;white-space:nowrap}
.ap .rv .tx b{color:''' + P + '''}
.gain{background:''' + P + ''';box-shadow:0 12px 0 #6d0a24}
.endc{background:#2a0a12}
.endc .c{background:#ffd43b;color:#0f172a}
.endc .b{color:#ffb3c4}
.step{background:''' + P + '''}
.hook{position:absolute;left:70px;top:326px;padding:12px 26px;border-radius:22px;background:#fff;border:5px solid #0f172a;box-shadow:8px 8px 0 #0f172a;font:900 48px/1.12 Inter;color:#0f172a;z-index:8;white-space:nowrap}
.hook b{color:''' + P + '''}
.wait{position:absolute;padding:12px 30px;border-radius:24px;background:#e11d48;color:#fff;font:900 70px Inter;border:6px solid #0f172a;box-shadow:10px 10px 0 #0f172a;z-index:9;white-space:nowrap;transform:rotate(-5deg)}
.chain{position:absolute;left:150px;width:640px;height:110px;border-radius:28px;border:5px solid #0f172a;box-shadow:8px 8px 0 #0f172a;display:flex;align-items:center;justify-content:center;font:900 50px Inter;white-space:nowrap;z-index:7}
.chain.a{background:#fff;color:#0f172a}.chain.b{background:#ffd43b;color:#0f172a}.chain.c{background:#e11d48;color:#fff}
.arr{position:absolute;left:440px;font:900 64px Inter;color:#0f172a;z-index:7}
.note{position:absolute;left:150px;width:640px;text-align:center;font:italic 800 34px Inter;color:#6d0a24;background:rgba(255,255,255,.9);border-radius:20px;padding:12px 18px;z-index:7}
.stk.cb{background:#fff;color:''' + P + '''}
.stk.pl{background:''' + P + ''';color:#fff}
.mat{position:absolute;left:120px;top:440px;width:720px;height:880px;border-radius:40px;background:#fff;border:5px solid #0f172a;box-shadow:12px 12px 0 rgba(15,23,42,.25)}
.ms{position:absolute;padding:8px 18px;border-radius:16px;background:#ffd43b;border:4px solid #0f172a;font:900 40px Inter;color:#0f172a;white-space:nowrap;z-index:8}
'''

CSS += '''
.ring{position:absolute;border:8px solid #e11d48;border-radius:50%;z-index:9;transform:rotate(-3deg)}
.ap .cmd{height:108px;border-radius:54px;background:''' + P + ''';color:#fff;font:900 40px Inter;display:flex;align-items:center;justify-content:center;margin-top:26px}
.ap .fd.hl{border-color:#e11d48;border-width:6px;background:#fff1f4}
'''

ITEMS = [('Lampe', 'Lampe', '26,00 €'), ('Coque', 'Coque', '13,00 €'), ('Carnet', 'Carnet', '8,00 €')]
ROWS = ''.join(f'<div class="row"><span class="ic">{icon(ic, 76)}</span>{lab}<span class="p">{pr}</span></div>' for ic, lab, pr in ITEMS)


def panier():
    return phone(f'''<div class="hd">Mon panier</div>{ROWS}
     <div class="tot"><span>Total</span><span><b>47,00 €</b></span></div><div class="ex">prix d'exemple</div>
     <div class="cmd">Commander</div>''')


def cart(field='', disc=False, total='47,00 €', old=None, gd=None, hl=False):
    cls = 'fd on' if field else ('fd hl' if hl else 'fd')
    f = f'<div class="{cls}"><span class="cd">{field}</span></div>' if field else f'<div class="{cls}" style="color:#94a3b8">Ajouter un code</div>'
    d = ''
    if disc:
        a = f' data-g="{gd}" data-fx="right"' if gd else ''
        d = f'<div class="disc"{a}>Code promo Hacoo (-14 %)<span class="p">-6,58 €</span></div>'
    o = f'<s>{old}</s>' if old else ''
    return phone(f'''<div class="hd">Ma commande Hacoo</div>{ROWS}
     <div class="lb">Code promo Hacoo</div>
     <div class="fr2">{f}<div class="ap2">Appliquer</div></div>{d}
     <div class="tot"><span>Total</span><span>{o}<b>{total}</b></span></div><div class="ex">prix d'exemple</div>''')


CMDY, FIELDY = 1212, 1090
DONE = cart('hzklink', disc=True, total='40,42 €', old='47,00 €')
BODY = search('code promo hacoo') + '''
  <div class="scene" data-s="0">''' + DONE + '''
   <div class="hook">Ta commande <b>Hacoo</b><br>a cette ligne ?</div>
   <div class="ring" style="left:150px;top:RINGTOPpx;width:690px;height:120px"></div>
   <div class="wait" style="left:400px;top:560px;font-size:58px" data-g="0.2" data-fx="stamp">CETTE LIGNE ?</div></div>
  <div class="scene" data-s="1" data-in="pop"><div class="zm" data-zg="1.0" data-zs="1.18" style="transform-origin:470px RINGTOPpx">''' + DONE + '''
   <div class="ring" style="left:150px;top:RINGTOPpx;width:690px;height:120px"></div></div>
   <div class="gain" style="left:300px;top:520px;font-size:110px" data-g="1.1" data-fx="stamp">-6,58 €</div>
   <div class="stk pl" style="left:200px;top:760px;transform:rotate(-3deg)" data-g="1.3" data-fx="stamp">JUSTE UN CODE</div></div>
  <div class="scene" data-s="2" data-in="right">''' + step(1, 3, 'TON PANIER', '2.0') + '''<div class="zm" data-zg="2.1" data-zs="1.05" style="transform-origin:470px 900px">''' + panier() + '''</div>
   ''' + hand(470, CMDY, '2.4', (260, 420)) + '''
</div>
  <div class="scene" data-s="3" data-in="left">''' + step(2, 3, 'CASE CODE PROMO', '3.0') + '''<div class="zm" data-zg="3.2" data-zs="1.1" style="transform-origin:400px FIELDYpx">''' + cart(hl=True) + '''</div>
   ''' + hand(330, FIELDY, '3.2', (300, 420)) + '''
   <div class="stk pl" style="left:140px;top:450px;transform:rotate(-3deg);font-size:50px" data-g="3.1" data-fx="stamp">AVANT DE PAYER</div></div>
  <div class="scene" data-s="4" data-in="right">''' + step(3, 3, 'CODE PROMO HACOO', '4.0') + '''
   <div class="zm" data-zg="4.1" data-zs="1.05" style="transform-origin:470px 1000px">''' + cart('<span data-g="4.2" data-fx="type">hzklink</span>') + hand(640, FIELDY, '4.4', (200, 380)) + '''</div>
   <div class="stk cb" style="left:110px;top:470px;transform:rotate(-2deg);font-size:42px" data-g="4.2" data-fx="pop">CODE PROMO HACOO : hzklink</div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="zm" data-zg="5.0" data-zs="1.04" style="transform-origin:470px 1000px">''' + cart('hzklink', disc=True, total='40,42 €', old='47,00 €', gd='5.0') + '''
   <div class="ring" style="left:150px;top:RINGTOPpx;width:690px;height:120px" data-g="5.1" data-fx="pop"></div></div>
   <div class="gain" style="left:250px;top:460px;font-size:120px" data-g="5.3" data-fx="stamp" data-slow="5.3">40,42 €</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + DONE + '''
   <div class="stk pl" style="left:120px;top:440px;transform:rotate(-3deg);font-size:46px" data-g="6.0" data-fx="stamp">PAS DE LIGNE = PLEIN PRIX</div>
   <div class="abs" style="inset:0;background:rgba(247,238,240,.88);z-index:7" data-g="6.2" data-fx="fade"></div>
   <div class="endc" style="top:600px" data-g="6.2" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div><div class="b">enregistre · liens des articles tendance en bio</div></div>
   <div class="cond" style="top:1000px;height:268px;display:flex;align-items:center;justify-content:center;font-size:28px;background:#fff;border:3px solid #c8103e" data-g="6.2" data-fx="fade">Prix d'exemple · -14 % avec le code promo Hacoo hzklink sur l'appli Hacoo · Offre soumise aux conditions en vigueur</div></div>
'''
BODY = BODY.replace('RINGTOP', '1124').replace('CMDY', '1150').replace('FIELDY', '1080')
