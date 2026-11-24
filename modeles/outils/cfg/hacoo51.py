import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qg_ecran import *
from hacoo_items import icon
# Hacoo n°1 du 24/11/2026 (brief veille du 24/11, vidéo 1) - style E « Écran d'appli en gros plan », accent violet prune.
# Format F1 « STOP / erreur à éviter » + 4 étapes, sujet R (tailles) : « Avant de valider ta taille sur Hacoo, regarde ça ».
# Fiche article + doigt vers « Ajouter au panier » + ATTENDS -> taille ratée / remboursement / compte bloqué ? (« des utilisateurs racontent »)
# -> 1 guide des tailles en cm -> 2 mesurer un vêtement à soi (mètre ruban) -> 3 avis avec photos -> 4 case code promo Hacoo hzklink
# -> -12,88 € / 79,12 € (ralenti) -> seconde main + enregistre + carte de fin, retour à la fiche article (boucle).
# Téléphone DESSINÉ, générique, sans logo ni interface copiée ; jamais d'affirmation de bannissement.
# Prix d'exemple : survêt 39 € + baskets 47 € + chaussettes 6 € = 92,00 € ; -14 % = 12,88 € (92 x 0,14) ; total 79,12 € (92 x 0,86).
# Voix : Speko Manon (cartesia sonic-3.5), speed 1.08, une synthèse par réplique, silences coupés (internes plafonnés à 0,16 s), atempo 1.15.
NAME = 'hacoo51'
TITLE = 'Hacoo tailles prune'
ROOT = ':root{--bg:#f6eef4}'
LINES = [
 ("Attends ! Avant de valider ta taille sur l'appli Hacou, regarde ça.", [("Attends !", None), ("Avant de valider", None), ("ta taille sur", None), ("l'appli <em>Hacoo</em>,", None), ("regarde ça.", None)]),
 ("Taille ratée, remboursement… et des utilisateurs racontent que leur compte a été bloqué.", [("Taille ratée,", None), ("remboursement…", None), ("et des utilisateurs", None), ("racontent que leur", None), ("compte a été <em>bloqué</em>.", None)]),
 ("Un : ouvre le guide des tailles. Elles changent d'une boutique à l'autre.", [("<em>Un :</em>", None), ("ouvre le guide", None), ("des tailles.", None), ("Elles changent d'une", None), ("boutique à l'autre.", None)]),
 ("Deux : mesure un vêtement à toi qui te va bien, et compare en centimètres.", [("<em>Deux :</em>", None), ("mesure un vêtement", None), ("à toi qui te va bien,", None), ("et compare", None), ("en <em>centimètres</em>.", None)]),
 ("Trois : lis les avis avec photos. Taille petit, taille grand : tout est écrit.", [("<em>Trois :</em>", None), ("lis les avis", None), ("avec photos.", None), ("Taille petit,", None), ("taille grand :", None), ("tout est écrit.", None)]),
 ("Quatre : code promo Hacou, H, Z, K, link, dans la case code promo, et tu appuies sur Appliquer.", [("<em>Quatre :</em>", None), ("<em>code promo Hacoo</em>,", None), ("<i>hzklink</i>,", None), ("dans la case", None), ("code promo,", None), ("et tu appuies", None), ("sur <em>Appliquer</em>.", None)]),
 ("Toujours pas la bonne taille ? Revends-le en seconde main. Enregistre cette vidéo, les liens sont dans ma bio.", [("Toujours pas", None), ("la bonne taille ?", None), ("Revends-le en", None), ("<em>seconde main</em>.", None), ("Enregistre cette vidéo,", None), ("liens dans ma bio.", None)]),
]
SPLITS = [(0.2, 3.397), (3.747, 7.916), (8.266, 11.135), (11.485, 14.995), (15.345, 18.727), (19.077, 25.707), (26.057, 30.726)]
TAIL = 1.5
GAP = 0.2
MINLEN = 1.8

P = '#7b2d6b'   # violet prune
PL = '#f6e6f1'
CSS = '''
body,#stage{background:#f6eef4}
#cam{transform-origin:470px 250px}
#bgtex{background:radial-gradient(circle at 1px 1px,rgba(123,45,107,.11) 2px,transparent 2.5px) 0 0/44px 44px,linear-gradient(160deg,#fbf6fa 0%,#f1e2ec 60%,#ead3e3 100%)}
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
.gain{background:''' + P + ''';box-shadow:0 12px 0 #4a1640}
.endc{background:#2a0f25}
.endc .c{background:#ffd43b;color:#0f172a}
.endc .b{color:#f0abdc}
.step{background:''' + P + '''}
.hook{position:absolute;left:70px;top:326px;padding:12px 26px;border-radius:22px;background:#fff;border:5px solid #0f172a;box-shadow:8px 8px 0 #0f172a;font:900 48px/1.12 Inter;color:#0f172a;z-index:8;white-space:nowrap}
.hook b{color:''' + P + '''}
.wait{position:absolute;padding:12px 30px;border-radius:24px;background:#e11d48;color:#fff;font:900 70px Inter;border:6px solid #0f172a;box-shadow:10px 10px 0 #0f172a;z-index:9;white-space:nowrap;transform:rotate(-5deg)}
.chain{position:absolute;left:150px;width:640px;height:110px;border-radius:28px;border:5px solid #0f172a;box-shadow:8px 8px 0 #0f172a;display:flex;align-items:center;justify-content:center;font:900 50px Inter;white-space:nowrap;z-index:7}
.chain.a{background:#fff;color:#0f172a}.chain.b{background:#ffd43b;color:#0f172a}.chain.c{background:#e11d48;color:#fff}
.arr{position:absolute;left:440px;font:900 64px Inter;color:#0f172a;z-index:7}
.note{position:absolute;left:150px;width:640px;text-align:center;font:italic 800 34px Inter;color:#4a1640;background:rgba(255,255,255,.9);border-radius:20px;padding:12px 18px;z-index:7}
.stk.cb{background:#fff;color:''' + P + '''}
.stk.pl{background:''' + P + ''';color:#fff}
.mat{position:absolute;left:120px;top:440px;width:720px;height:880px;border-radius:40px;background:#fff;border:5px solid #0f172a;box-shadow:12px 12px 0 rgba(15,23,42,.25)}
.ms{position:absolute;padding:8px 18px;border-radius:16px;background:#ffd43b;border:4px solid #0f172a;font:900 40px Inter;color:#0f172a;white-space:nowrap;z-index:8}
'''

ITEMS = [('Survêt', 'Survêt', '39,00 €'), ('Baskets', 'Baskets', '47,00 €'), ('Chaussettes', 'Chaussettes', '6,00 €')]
ROWS = ''.join(f'<div class="row"><span class="ic">{icon(ic, 76)}</span>{lab}<span class="p">{pr}</span></div>' for ic, lab, pr in ITEMS)


def fiche(sel='M'):
    sz = ''.join(f'<span class="{"on" if s == sel else ""}">{s}</span>' for s in ['S', 'M', 'L', 'XL'])
    return phone(f'''<div class="pic">{icon('Survêt', 330)}</div><div class="nm">Survêt confort</div><div class="pr">39,00 € <span style="font:700 26px Inter;color:#94a3b8">prix d'exemple</span></div>
     <div class="sz">{sz}</div><div class="add">Ajouter au panier</div>''')


def guide():
    rows = [('S', '96', '66'), ('M', '102', '69'), ('L', '108', '72'), ('XL', '114', '74')]
    tr = ''.join(f'<tr class="{"hl" if s == "L" else ""}"><td>{s}</td><td>{a}</td><td>{b}</td></tr>' for s, a, b in rows)
    return phone(f'''<div class="hd">Guide des tailles</div><div class="gtab"><span class="on">en cm</span><span>en pouces</span></div>
     <table><tr><th>Taille</th><th>Poitrine</th><th>Longueur</th></tr>{tr}</table>
     <div class="ex" style="margin-top:18px">mesures d'exemple · varient selon la boutique</div>''')


CAM_SVG = '<svg width="80" height="80" viewBox="0 0 80 80"><rect x="8" y="22" width="64" height="44" rx="10" fill="none" stroke="#7b2d6b" stroke-width="6"/><circle cx="40" cy="44" r="12" fill="none" stroke="#7b2d6b" stroke-width="6"/><rect x="26" y="12" width="28" height="12" rx="4" fill="#7b2d6b"/></svg>'


def avis():
    return phone(f'''<div class="hd">Avis (128)</div><div class="gtab"><span>Tous</span><span class="on">✓ Avis avec photos</span></div>
     <div class="rv" data-g="4.3" data-fx="right"><div class="ph2">{CAM_SVG}</div><div><div class="st">★★★★★</div><div class="tx">« Taille <b>petit</b> »</div><div class="ex">prends au-dessus</div></div></div>
     <div class="rv" data-g="4.4" data-fx="right"><div class="ph2">{CAM_SVG}</div><div><div class="st">★★★★☆</div><div class="tx">« Taille <b>grand</b> »</div><div class="ex">prends en dessous</div></div></div>
     <div class="rv" data-g="4.5" data-fx="right"><div class="ph2">{CAM_SVG}</div><div><div class="st">★★★★★</div><div class="tx">« Taille <b>normal</b> »</div><div class="ex">ta taille habituelle</div></div></div>''')


def cart(field='', disc=False, total='92,00 €', old=None, gd=None):
    f = f'<div class="fd on"><span class="cd">{field}</span></div>' if field else '<div class="fd" style="color:#94a3b8">Ajouter un code</div>'
    d = ''
    if disc:
        a = f' data-g="{gd}" data-fx="right"' if gd else ''
        d = f'<div class="disc"{a}>Code promo Hacoo (-14 %)<span class="p">-12,88 €</span></div>'
    o = f'<s>{old}</s>' if old else ''
    return phone(f'''<div class="hd">Ma commande Hacoo</div>{ROWS}
     <div class="lb">Code promo Hacoo</div>
     <div class="fr2">{f}<div class="ap2">Appliquer</div></div>{d}
     <div class="tot"><span>Total</span><span>{o}<b>{total}</b></span></div><div class="ex">prix d'exemple</div>''')


# Mètre ruban sur un sweat posé à plat (dessin simple)
SWEAT = '''<svg class="abs" style="left:170px;top:520px" width="620" height="640" viewBox="0 0 620 640">
 <path d="M190 40 L250 20 Q310 60 370 20 L430 40 L590 170 L530 260 L470 210 L470 600 L150 600 L150 210 L90 260 L30 170 Z" fill="#c9a3bf" stroke="#0f172a" stroke-width="8" stroke-linejoin="round"/>
 <path d="M250 20 Q310 70 370 20" fill="none" stroke="#0f172a" stroke-width="7"/>
 <path d="M150 560 H470" stroke="#0f172a" stroke-width="6" opacity=".4"/>
</svg>
<svg class="abs" style="left:170px;top:520px" width="620" height="660" viewBox="0 0 620 660">
 <g data-g="3.1" data-fx="grow" style="transform-origin:150px 300px"><rect x="150" y="286" width="320" height="30" rx="6" fill="#ffd43b" stroke="#0f172a" stroke-width="5"/>
 <path d="M175 286 V300 M205 286 V296 M235 286 V300 M265 286 V296 M295 286 V300 M325 286 V296 M355 286 V300 M385 286 V296 M415 286 V300 M445 286 V296" stroke="#0f172a" stroke-width="4"/></g>
 <g data-g="3.2" data-fx="fade"><rect x="500" y="40" width="30" height="560" rx="6" fill="#ffd43b" stroke="#0f172a" stroke-width="5"/>
 <path d="M500 80 H514 M500 130 H510 M500 180 H514 M500 230 H510 M500 280 H514 M500 330 H510 M500 380 H514 M500 430 H510 M500 480 H514 M500 530 H510" stroke="#0f172a" stroke-width="4"/></g>
</svg>'''

BODY = search('code promo hacoo') + '''
  <div class="scene" data-s="0">''' + fiche('M') + hand(470, 1250, '0.0', (240, 380)) + '''
   <div class="hook">Avant de valider ta taille<br>sur <b>Hacoo</b>, regarde ça</div>
   <div class="wait" style="left:430px;top:560px" data-g="0.0" data-fx="stamp">ATTENDS !</div>
   <div class="stk pl" style="left:520px;top:840px;transform:rotate(4deg);font-size:50px" data-g="0.2" data-fx="pop">TA TAILLE ?</div></div>
  <div class="scene" data-s="1" data-in="up"><div class="zm" data-zg="1.0" data-zs="1.06" style="transform-origin:470px 900px;opacity:.15">''' + fiche('M') + '''</div>
   <div class="chain a" style="top:470px" data-g="1.0" data-fx="left">TAILLE RATÉE</div>
   <div class="arr" style="top:590px" data-g="1.1" data-fx="fade">▼</div>
   <div class="chain b" style="top:680px" data-g="1.1" data-fx="right">REMBOURSEMENT</div>
   <div class="arr" style="top:800px" data-g="1.3" data-fx="fade">▼</div>
   <div class="chain c" style="top:890px" data-g="1.4" data-fx="stamp">COMPTE BLOQUÉ ?</div>
   <div class="note" style="top:1040px" data-g="1.2" data-fx="fade">« des utilisateurs racontent »</div></div>
  <div class="scene" data-s="2" data-in="right">''' + step(1, 4, 'GUIDE DES TAILLES', '2.0') + '''<div class="zm" data-zg="2.1" data-zs="1.1" style="transform-origin:470px 760px">''' + guide() + '''</div>
   ''' + hand(330, 680, '2.1', (300, 420)) + '''
   <div class="stk cb" style="left:250px;top:1275px;transform:rotate(-2deg);font-size:44px" data-g="2.3" data-fx="stamp">SELON LA BOUTIQUE</div></div>
  <div class="scene" data-s="3" data-in="left">''' + step(2, 4, 'MESURE EN CM', '3.0') + '''<div class="mat"></div>''' + SWEAT + '''
   <div class="ms" style="left:330px;top:770px" data-g="3.1" data-fx="pop">largeur 54 cm</div>
   <div class="ms" style="left:520px;top:1030px" data-g="3.2" data-fx="pop">longueur 70 cm</div>
   <div class="stk pl" style="left:150px;top:1180px;transform:rotate(-3deg);font-size:46px" data-g="3.4" data-fx="stamp">COMPARE AU GUIDE</div></div>
  <div class="scene" data-s="4" data-in="right">''' + step(3, 4, 'AVIS AVEC PHOTOS', '4.0') + '''<div class="zm" data-zg="4.1" data-zs="1.06" style="transform-origin:470px 700px">''' + avis() + '''</div>
   ''' + hand(560, 610, '4.1', (260, 420)) + '''</div>
  <div class="scene" data-s="5" data-in="pop">''' + step(4, 4, 'CODE PROMO HACOO', '5.0') + '''
   <div class="zm" data-zg="5.1" data-zs="1.05" style="transform-origin:470px 1000px">''' + cart('<span data-g="5.2" data-fx="type">hzklink</span>') + hand(700, 1093, '5.5', (200, 380)) + '''
   <div class="abs" style="inset:0;z-index:11" data-g="5.6" data-fx="fade">''' + cart('hzklink', disc=True, total='79,12 €', old='92,00 €') + '''</div></div>
   <div class="gain" style="left:480px;top:440px" data-g="5.6" data-fx="stamp">-12,88 €</div>
   <div class="gain" style="left:220px;top:700px;font-size:110px" data-g="5.6" data-fx="stamp" data-slow="5.6">79,12 €</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + fiche('L') + '''
   <div class="stk pl" style="left:120px;top:440px;transform:rotate(-3deg);font-size:46px" data-g="6.2" data-fx="stamp">♻ SECONDE MAIN</div>
   <div class="endc" style="top:600px" data-g="6.4" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div><div class="b">enregistre · liens des articles tendance en bio</div></div>
   <div class="cond" style="top:1000px;height:268px;display:flex;align-items:center;justify-content:center;font-size:28px;background:#fff;border:3px solid #7b2d6b" data-g="6.4" data-fx="fade">Prix d'exemple · -14 % avec le code promo Hacoo hzklink sur l'appli Hacoo · Offre soumise aux conditions en vigueur</div></div>
'''
