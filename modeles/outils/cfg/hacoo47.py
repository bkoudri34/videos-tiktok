import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from alerte import *
from hacoo_items import ICONS
# Hacoo, 23/11/2026, vidéo 1 (compte affiliation) - style A « Alerte stickers », format F3 anti-arnaque / confiance :
# « ATTENTION aux faux codes promo Hacoo » + 3 réflexes numérotés, fin « enregistre ». Sujet nouveau « faux codes » (pas R).
# Aucun créateur ni code visé : le « -70 % » est un exemple dessiné, barré. Aucune affirmation invérifiable (« méfie-toi, vérifie la ligne »).
# Panier d'exemple : plaid 24 € + bougie 9 € + mug 12 € = 45,00 € ; -14 % = 6,30 € ; total 38,70 €. Prix d'exemple.
# Voix : Eve (xai), speed 1.08, une synthèse par réplique, silences coupés + atempo 1.1, 0,2 s au début et 0,4 s entre les répliques.
NAME = 'hacoo47'
TITLE = 'Hacoo alerte faux codes'
MINLEN = 1.6
GAP = 0.22
TAIL = 2.2
LINES = [
 ("Attention aux faux codes promo Hacou qui promettent la lune.", [(kara("<i>Attention</i> aux"), None), (kara("faux <em>codes promo</em>"), None), (kara("<em>Hacoo</em> qui promettent"), None), (kara("la lune."), None)]),
 ("Un code qui promet un chiffre énorme, dans un commentaire ou un message ? Méfie-toi.", [(kara("Un code qui promet"), None), (kara("un <em>chiffre énorme</em>,"), None), (kara("dans un commentaire"), None), (kara("ou un message ?"), None), (kara("<i>Méfie-toi.</i>"), None)]),
 ("Le seul juge, c'est la ligne de réduction, juste avant de payer.", [(kara("Le seul juge,"), None), (kara("c'est la <em>ligne de réduction</em>,"), None), (kara("juste avant de payer."), None)]),
 ("Personne n'a besoin de ton mot de passe ou de ta carte pour te donner un code.", [(kara("Personne n'a besoin"), None), (kara("de ton <i>mot de passe</i>"), None), (kara("ou de ta <i>carte</i>"), None), (kara("pour te donner un code."), None)]),
 ("Code promo Hacou, H, Z, K, link : moins quatorze pour cent, et tu le vois tout de suite.", [(kara("<em>Code promo Hacoo</em>"), None), ('<u>hzklink</u>', None), (kara("<i>-14 %</i>,"), None), (kara("et tu le vois"), None), (kara("tout de suite."), None)]),
 ("Quarante-cinq euros, ça fait trente-huit euros et soixante-dix centimes.", [(kara("45 €,"), None), (kara("ça fait"), None), (kara("<em>38,70 €</em>."), None)]),
 ("Enregistre cette vidéo, et envoie-la à quelqu'un qui commande sur l'appli Hacou. Les liens sont dans ma bio.", [(kara("<em>Enregistre</em> cette vidéo,"), None), (kara("et envoie-la à quelqu'un"), None), (kara("qui commande sur <em>Hacoo</em>."), None), (kara("Les liens"), None), (kara("sont dans ma bio."), None)]),
]
SPLITS = [(0.2, 2.84), (3.24, 7.71), (8.11, 11.18), (11.58, 14.78), (15.18, 20.56), (20.96, 23.85), (24.25, 29.06)]

CSS = '''
#sub u{display:inline-block;padding:2px 20px 6px;margin:0 4px;border-radius:12px;background:#ffd84a;color:#141414;border:5px solid #141414;text-decoration:none;text-transform:none;font-family:'DejaVu Sans Mono',Menlo,monospace}
.lc{text-transform:none!important}
.ph{position:absolute;width:360px;height:560px;border:8px solid #141414;border-radius:48px;background:#fff;box-shadow:10px 12px 0 #141414;padding:60px 24px 20px}
.msg{border:5px solid #141414;border-radius:24px 24px 24px 6px;background:#f2f2f2;padding:14px 18px;font:800 30px Inter,'Arial Black',sans-serif;margin-bottom:18px;text-align:left}
.msg.big{background:#ffd84a;font-size:58px;text-align:center;border-radius:24px 24px 6px 24px}
.x{position:absolute;left:-30px;top:200px;width:420px;height:12px;background:#ee3b3b;border:4px solid #141414;border-radius:8px;transform:rotate(-24deg)}
.tk{left:190px;width:700px;padding:30px 40px 28px;font:800 33px Inter,'Arial Black',sans-serif}
.tk .r{display:flex;justify-content:space-between;padding:8px 0;white-space:nowrap}
.tk .r.red{color:#ee3b3b}
.tk .t{font:900 40px Inter,'Arial Black',sans-serif;text-align:center;margin-bottom:8px}
.tk .tot{border-top:5px dashed #141414;margin-top:10px;padding-top:14px;font-size:48px}
.tk .ex{text-align:center;font:700 24px Inter,sans-serif;color:#6b6257;margin-top:10px}
.cp{left:130px;top:430px;width:820px;padding:34px 44px 36px}
.cp .lab{font:900 34px Inter,'Arial Black',sans-serif;letter-spacing:2px}
.cp .f{margin-top:14px;height:110px;border:6px solid #141414;border-radius:20px;background:#fff;display:flex;align-items:center;padding:0 28px;font:900 66px 'DejaVu Sans Mono',Menlo,monospace}
.cp .ok{margin-top:16px;font:900 46px Inter,'Arial Black',sans-serif;color:#2fa35a}
.strk{position:absolute;height:10px;background:#ee3b3b;transform-origin:0 50%}
.big2{position:absolute;left:0;width:1080px;text-align:center;font:900 150px Inter,'Arial Black',sans-serif;z-index:4}
.cond{position:absolute;left:90px;width:900px;text-align:center;font:700 26px Inter,sans-serif;color:#6b6257}
'''


def ic(name, x, y, s=170, g=None):
    return stk(x, y, s, s, ICONS[name], g=g, vb='0 0 200 200')


BODY = chrome() + '''
  <div class="scene" data-s="0">''' + tag('CODE PROMO HACOO') + ban('⚠ ATTENTION', 300, 'red', rot=-3) + ban('aux faux codes promo Hacoo', 430, size=44, rot=1) + '''
   <div class="ph" style="left:360px;top:560px;transform:rotate(-5deg)"><div class="msg">code secret ?</div><div class="msg big">-70 % !!!</div><div class="msg">dépêche-toi 🔥</div><div class="x"></div></div></div>
  <div class="scene" data-s="1" data-in="pop">''' + tag('RÉFLEXE 1') + ban('Un chiffre énorme ?', 300, 'yel', g='1.0', rot=-2, size=54) + ban('Méfiance.', 420, 'red', g='1.4', fx='stamp', rot=2) + '''
   <div class="ph" style="left:120px;top:570px;transform:rotate(-4deg)" data-g="1.2" data-fx="left"><div class="msg">💬 commentaire</div><div class="msg big">-80 %</div><div class="msg">« clique vite »</div></div>
   <div class="ph" style="left:555px;top:600px;transform:rotate(5deg)" data-g="1.3" data-fx="right"><div class="msg">✉ message</div><div class="msg big">-90 %</div><div class="msg">« code caché »</div></div>
   <div class="big2" style="top:850px;color:#ee3b3b" data-g="1.4" data-fx="stamp">?!</div></div>
  <div class="scene" data-s="2" data-in="right">''' + tag('RÉFLEXE 2') + ban('La ligne de réduction', 300, 'grn', rot=-2, size=50) + ban('ne ment pas', 410, size=56, g='2.1', rot=1) + '''
   <div class="card tk" style="top:560px"><div class="t">TON PANIER</div><div class="r"><span>Sous-total</span><span>45,00 €</span></div><div class="r red"><span>Réduction code</span><span>-6,30 €</span></div><div class="r tot"><span>Total</span><span>38,70 €</span></div><div class="ex">prix d'exemple</div></div>''' + red_circle(160, 682, 760, 118, '2.1') + '''
   <div class="ban" style="top:1000px" data-g="2.2" data-fx="pop"><span class="pill" style="background:#ffd84a;font-size:44px">JUSTE AVANT DE PAYER</span></div></div>
  <div class="scene" data-s="3" data-in="up">''' + tag('RÉFLEXE 3') + ban('Jamais ton mot de passe', 300, 'red', rot=-2, size=46) + ban('ni ta carte', 420, size=56, g='3.2', rot=2) + stk(340, 540, 400, 400, PADLOCK, g='3.0', vb='0 0 400 400') + '''</div>
  <div class="scene" data-s="4" data-in="pop">''' + tag('MON CODE') + '''
   <div class="card cp"><div class="lab">CODE PROMO HACOO</div><div class="f"><span class="lc" data-g="4.1" data-fx="type">hzklink</span></div><div class="ok" data-g="4.2" data-fx="fade">✓ -14 % appliqué</div></div>''' + ban('-14 %', 840, 'yel', g='4.2', fx='stamp', rot=-4, size=150) + '''</div>
  <div class="scene" data-s="5" data-in="right">''' + tag('PREUVE') + ic('Plaid', 140, 300) + ic('Bougie', 455, 280) + ic('Mug', 770, 300, 150) + '''
   <div class="card tk" style="top:520px"><div class="r"><span>Plaid</span><span>24,00 €</span></div><div class="r"><span>Bougie</span><span>9,00 €</span></div><div class="r"><span>Mug</span><span>12,00 €</span></div>
    <div class="r" style="position:relative"><span>Sous-total</span><span>45,00 €</span></div><div class="r red" data-g="5.1" data-fx="left"><span>Code <span class="lc">hzklink</span> -14 %</span><span>-6,30 €</span></div>
    <div class="r tot"><span>Total</span><span data-g="5.2" data-fx="stamp" data-slow="5.2">38,70 €</span></div><div class="ex">prix d'exemple</div></div></div>
  <div class="scene" data-s="6" data-in="pop">''' + tag('PARTAGE') + stk(430, 290, 220, 300, BOOKMARK, g='6.0', vb='0 0 260 320') + ban('Enregistre cette vidéo', 630, size=50, g='6.0', rot=-2) + ban('Envoie-la ↗', 750, 'grn', g='6.1', rot=2, size=58) + '''
   <div class="ban" style="top:880px" data-g="6.2" data-fx="up"><span class="pill" style="background:#ffd84a;font-size:44px">CODE PROMO HACOO : <span class="mono lc">hzklink</span></span></div>
   <div class="ban" style="top:975px" data-g="6.3" data-fx="up"><span class="pill" style="background:#fff;font-size:34px">-14 % · liens des articles tendance en bio</span></div>
   <div class="cond" style="top:1470px">Offre soumise aux conditions en vigueur sur l'appli Hacoo · prix d'exemple</div></div>
'''
