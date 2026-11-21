import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qg_ecran import *
from hacoo_items import icon
# Hacoo n°1 du 21/11/2026 - style E « Écran d'appli en gros plan » (brief veille du 21/11, vidéo 1), accent bleu cobalt.
# Format « 3 erreurs numérotées » (F1 erreur à éviter + F7 tuto écran) : « Ton code Hacoo ne marche pas ? 3 erreurs ».
# Doigt qui va appuyer sur Payer -> « ATTENDS ! » -> ERREUR N°1 case code promo jamais ouverte -> elle est dans la commande, avant Payer
# -> ERREUR N°2 hzklink tapé sans Appliquer -> total inchangé 47,00 € -> ERREUR N°3 ligne de réduction pas vérifiée -> -6,58 € -> 40,42 € (ralenti) -> fin.
# Téléphone DESSINÉ, générique, sans logo ni interface copiée.
# Prix d'exemple : survêt 34 € + bonnet 8 € + chaussettes 5 € = 47,00 € ; -14 % = 6,58 € (47 x 0,14) ; total 40,42 € (47 x 0,86).
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08, une synthèse pour les répliques 1 à 7 ; la dernière refaite à part
# (« Hacou » compris « Assou ») en écrivant « Akou ».
NAME = 'hacoo41'
TITLE = 'Hacoo 3 erreurs cobalt'
ROOT = ':root{--bg:#e4e9f7}'
LINES = [
 ("Attends ! Ton code promo Hacou ne marche pas ? C'est sûrement une de ces trois erreurs.", [("Attends !", None), ("Ton <em>code promo Hacoo</em>", None), ("ne marche pas ?", None), ("C'est sûrement", None), ("une de ces <em>3 erreurs</em>.", None)]),
 ("Erreur numéro un : tu paies sans ouvrir la case code promo.", [("<em>Erreur n°1</em> :", None), ("tu paies sans ouvrir", None), ("la case <em>code promo</em>.", None)]),
 ("Elle est dans ta commande, juste avant de payer.", [("Elle est dans ta commande,", None), ("juste avant de payer.", None)]),
 ("Erreur numéro deux : tu tapes H, Z, K, link, mais tu n'appuies pas sur Appliquer.", [("<em>Erreur n°2</em> :", None), ("tu tapes <i>hzklink</i>,", None), ("mais tu n'appuies pas", None), ("sur <em>Appliquer</em>.", None)]),
 ("Résultat : le total reste à quarante-sept euros.", [("Résultat :", None), ("le total reste", None), ("à <em>47 €</em>.", None)]),
 ("Erreur numéro trois : tu ne vérifies pas la ligne de réduction.", [("<em>Erreur n°3</em> :", None), ("tu ne vérifies pas", None), ("la ligne de réduction.", None)]),
 ("Là : moins six euros cinquante-huit. Tu paies quarante euros quarante-deux.", [("Là :", None), ("<i>-6,58 €</i>.", None), ("Tu paies", None), ("<em>40,42 €</em>.", None)]),
 ("Prix d'exemple. Enregistre la vidéo. Le code promo Akou, c'est H, Z, K, link.", [("Prix d'exemple.", None), ("Enregistre la vidéo.", None), ("Le <em>code promo Hacoo</em>,", None), ("c'est <i>hzklink</i>.", None)]),
]
SPLITS = [(0.0, 3.74), (4.34, 7.0), (7.42, 8.9), (9.51, 13.63), (14.16, 16.07), (16.53, 18.99), (19.35, 22.21), (22.6, 26.87)]
GSTART = [[0.0, 0.8, 1.5, 2.6, 3.0], [4.34, 5.4, 6.3], [7.42, 8.3], [9.51, 10.4, 12.6, 13.2], [14.16, 14.8, 15.4], [16.53, 17.6, 18.3],
          [19.35, 19.8, 21.21, 21.4], [22.6, 23.59, 24.72, 25.9]]
TAIL = 2.6
GAP = 0.3

CSS = '''
body,#stage{background:#e4e9f7}
#bgtex{background:radial-gradient(circle at 1px 1px,rgba(20,40,120,.10) 2px,transparent 2.5px) 0 0/44px 44px,linear-gradient(160deg,#f4f6fd 0%,#dfe5f6 60%,#d2daf1 100%)}
.search .cur{background:#2547d0}
.rip{border-color:#2547d0}
.ap .row{height:112px}
.ap .row .p{margin-left:auto;font:900 40px Inter;color:#0f172a}
.ap .row .ic{width:92px;height:92px;border-radius:20px;background:#f4f4f6;display:flex;align-items:center;justify-content:center;flex:none}
.ap .fr2{display:flex;gap:16px;align-items:center}
.ap .fr2 .fd{flex:1}
.ap .ap2{height:104px;padding:0 26px;border-radius:24px;background:#2547d0;color:#fff;font:900 34px Inter;display:flex;align-items:center;white-space:nowrap}
.ap .fd.on{border-color:#2547d0;background:#eef2ff}
.ap .fd.bl{border-color:#e11d48;background:#fff1f2}
.ap .fd .cd{font:900 46px 'DejaVu Sans Mono',monospace;color:#0f172a}
.ap .disc{height:92px;display:flex;align-items:center;font:900 28px Inter;color:#1d3aa8;border-bottom:3px solid #eef2f7;white-space:nowrap}
.ap .disc .p{margin-left:auto;font:900 40px Inter;color:#1d3aa8}
.ap .tot{display:flex;align-items:baseline;justify-content:space-between;margin-top:18px;font:900 44px Inter;white-space:nowrap}
.ap .tot b{font:900 76px Inter;letter-spacing:-2px}
.ap .tot s{font:800 38px Inter;color:#94a3b8;text-decoration-color:#2547d0;text-decoration-thickness:5px;margin-right:14px}
.ap .ex{font:700 26px Inter;color:#94a3b8;margin-top:4px}
.ap .pay{height:108px;border-radius:54px;background:#0f172a;color:#fff;font:900 42px Inter;display:flex;align-items:center;justify-content:center;margin-top:22px}
.gain{background:#2547d0;box-shadow:0 12px 0 #142a80}
.endc .c{background:#ffd43b;color:#0f172a}
.endc .b{color:#a5b4fc}
.hook{position:absolute;left:70px;top:330px;padding:14px 28px;border-radius:22px;background:#fff;border:5px solid #0f172a;box-shadow:8px 8px 0 #0f172a;font:900 54px/1.12 Inter;color:#0f172a;z-index:8;white-space:nowrap}
.hook b{color:#2547d0}
.err{position:absolute;left:70px;top:326px;height:72px;padding:0 30px;border-radius:36px;background:#2547d0;color:#fff;font:900 40px Inter;display:flex;align-items:center;gap:16px;letter-spacing:1px;z-index:8;white-space:nowrap;box-shadow:6px 6px 0 #0f172a}
.err i{font-style:normal;width:46px;height:46px;border-radius:50%;background:#fff;color:#2547d0;display:flex;align-items:center;justify-content:center;font:900 30px Inter}
.wait{position:absolute;left:330px;top:560px;padding:12px 34px;border-radius:24px;background:#e11d48;color:#fff;font:900 80px Inter;border:6px solid #0f172a;box-shadow:10px 10px 0 #0f172a;z-index:9;white-space:nowrap;transform:rotate(-5deg)}
.x{position:absolute;width:120px;height:120px;border-radius:50%;background:#e11d48;color:#fff;font:900 80px Inter;display:flex;align-items:center;justify-content:center;border:6px solid #0f172a;z-index:9}
.stk.cb{background:#fff;color:#2547d0}
'''
ITEMS = [('Survêt', 'Survêt', '34,00 €'), ('Bonnet', 'Bonnet', '8,00 €'), ('Chaussettes', 'Chaussettes', '5,00 €')]
ROWS = ''.join(f'<div class="row"><span class="ic">{icon(ic, 80)}</span>{lab}<span class="p">{pr}</span></div>' for ic, lab, pr in ITEMS)


def cart_top():
    """Panier : 3 articles, total, Payer. La case code promo n'est pas ouverte."""
    return phone(f'''<div class="hd">Ma commande Hacoo</div>{ROWS}
     <div class="tot"><span>Total</span><span><b>47,00 €</b></span></div><div class="ex">prix d'exemple</div><div class="pay">Payer</div>''')


def cart_code(field='', cls='', disc=False, total='47,00 €', old=None, gd=None):
    """Bas de la commande : case code promo Hacoo, Appliquer, ligne de réduction, total, Payer."""
    f = f'<div class="fd on {cls}"><span class="cd">{field}</span></div>' if field else f'<div class="fd {cls}" style="color:#94a3b8">Ajouter un code</div>'
    d = ''
    if disc:
        a = f' data-g="{gd}" data-fx="right"' if gd else ''
        d = f'<div class="disc"{a}>Code promo Hacoo (-14 %)<span class="p">-6,58 €</span></div>'
    o = f'<s>{old}</s>' if old else ''
    return phone(f'''<div class="hd">Ma commande Hacoo</div>
     <div class="lb">Sous-total</div><div class="row" style="height:80px">3 articles<span class="p">47,00 €</span></div>
     <div class="lb">Code promo Hacoo</div>
     <div class="fr2">{f}<div class="ap2">Appliquer</div></div>{d}
     <div class="tot"><span>Total</span><span>{o}<b>{total}</b></span></div><div class="ex">prix d'exemple</div><div class="pay">Payer</div>''')


def err(n, g=None):
    a = f' data-g="{g}" data-fx="left"' if g else ''
    return f'<div class="err"{a}><i>{n}</i>ERREUR N°{n}</div>'


BODY = search('code promo hacoo') + '''
  <div class="scene" data-s="0">''' + cart_top() + hand(470, 1180, '0.1', (300, 420)) + '''
   <div class="hook">Ton <b>code Hacoo</b> ne marche pas ?<br>3 erreurs</div>
   <div class="wait" data-g="0.0" data-fx="stamp">ATTENDS !</div></div>
  <div class="scene" data-s="1" data-in="right">''' + err(1, '1.0') + '''<div class="zm" data-zg="1.2" data-zs="1.15" style="transform-origin:380px 820px">''' + cart_code(cls='bl') + '''</div>
   <div class="x" style="left:700px;top:1150px" data-g="1.1" data-fx="stamp">✗</div>
   <div class="stk" style="left:120px;top:1000px;transform:rotate(-3deg)" data-g="1.2" data-fx="pop">CASE VIDE</div></div>
  <div class="scene" data-s="2" data-in="up">''' + err(1) + cart_code() + hand(380, 820, '2.0', (260, 420)) + '''
   <div class="stk cb" style="left:120px;top:1000px;font-size:46px" data-g="2.1" data-fx="pop">AVANT DE PAYER</div></div>
  <div class="scene" data-s="3" data-in="right">''' + err(2, '3.0') + '''<div class="zm" data-zg="3.1" data-zs="1.12" style="transform-origin:380px 820px">''' + cart_code('<span data-g="3.1" data-fx="type">hzklink</span>') + '''</div>
   ''' + hand(820, 980, '3.2', (0, 360)) + '''
   <div class="stk" style="left:470px;top:980px;transform:rotate(4deg);font-size:46px" data-g="3.3" data-fx="pop">APPLIQUER ?</div></div>
  <div class="scene" data-s="4" data-in="pop">''' + err(2) + cart_code('hzklink') + '''
   <div class="x" style="left:700px;top:980px" data-g="4.1" data-fx="stamp">✗</div>
   <div class="stk" style="left:150px;top:1180px;font-size:56px" data-g="4.2" data-fx="stamp">TOUJOURS 47,00 €</div></div>
  <div class="scene" data-s="5" data-in="right">''' + err(3, '5.0') + cart_code('hzklink') + hand(700, 814, '5.0', (260, 420)) + '''
   <div class="stk cb" style="left:130px;top:1010px;font-size:46px" data-g="5.2" data-fx="pop">LA LIGNE DE RÉDUCTION ?</div></div>
  <div class="scene" data-s="6" data-in="pop"><div class="zm" data-zg="6.1" data-zs="1.08" style="transform-origin:470px 900px">''' + cart_code('hzklink', disc=True, total='40,42 €', old='47,00 €', gd='6.1') + '''</div>
   <div class="gain" style="left:560px;top:600px" data-g="6.1" data-fx="stamp">-6,58 €</div>
   <div class="gain" style="left:280px;top:1225px;font-size:100px" data-g="6.3" data-fx="stamp" data-slow="6.3">40,42 €</div></div>
  <div class="scene" data-s="7" data-in="pop">''' + cart_code('hzklink', disc=True, total='40,42 €', old='47,00 €') + '''
   <div class="endc" data-g="7.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div><div class="b">📌 enregistre · liens des articles tendance en bio</div></div>
   <div class="cond" style="top:1150px;background:#fff" data-g="7.1" data-fx="fade">Prix d'exemple · -14 % avec le code promo Hacoo hzklink sur l'appli Hacoo · Offre soumise aux conditions en vigueur</div></div>
'''
