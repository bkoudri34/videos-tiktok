import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from alerte import *
from hacoo_items import ICONS
# Hacoo, 26/11/2026, vidéo 1 (compte affiliation) - style A « Alerte stickers », gribouillis bleu ciel, sujet R (retours) :
# « Trop petit sur l'appli ? Ne le renvoie pas » -> témoignages d'utilisateurs (comptes bloqués après des remboursements, présenté
# comme ce que racontent des utilisateurs, jamais comme un fait) -> revends-le en seconde main / offre-le -> compare le guide des tailles
# avec un vêtement qui te va -> code promo hzklink -14 % -> panier d'exemple survêt 36 € + doudoune 58 € + bonnet 9 € = 103,00 €,
# -14,42 €, total 88,58 € (ralenti) -> fin « enregistre / envoie-la ».
# Code du jour HACOO847 (demande de Badr du 26/11, aujourd'hui seulement, -14 %, écrit à l'image par exception).
# Règle du 26/11 : « Hacoo » n'est JAMAIS écrit à l'image (ni sous-titres) : seulement dit à l'oral (« l'appli Hacou », « code promo Hacou »).
# Voix : Eve (xai), speed 1.08, une synthèse par réplique, silences coupés (internes plafonnés à 0,16 s), atempo 1.1, +3 dB.
NAME = 'hacoo59'
TITLE = 'Alerte trop petit bleu ciel'
MINLEN = 1.6
GAP = 0.22
TAIL = 2.2
LINES = [
 ("Attention. Ton article de l'appli Hacou est arrivé trop petit ? Ne le renvoie pas tout de suite.", [(kara("<i>Attention.</i>"), None), (kara("Ton article de l'appli"), None), (kara("est arrivé <em>trop petit ?</em>"), None), (kara("<i>Ne le renvoie pas</i>"), None), (kara("tout de suite."), None)]),
 ("Des utilisateurs racontent que leur compte a été bloqué après des demandes de remboursement.", [(kara("Des utilisateurs racontent"), None), (kara("que leur compte"), None), (kara("a été <i>bloqué</i>"), None), (kara("après des demandes"), None), (kara("de <em>remboursement.</em>"), None)]),
 ("Le bon réflexe : revends-le en seconde main. Ou offre-le, Noël arrive.", [(kara("<em>Le bon réflexe :</em>"), None), (kara("revends-le"), None), (kara("en seconde main."), None), (kara("Ou <em>offre-le,</em>"), None), (kara("Noël arrive."), None)]),
 ("La prochaine fois, compare le guide des tailles avec un vêtement qui te va déjà.", [(kara("La prochaine fois,"), None), (kara("compare le <em>guide des tailles</em>"), None), (kara("avec un vêtement"), None), (kara("qui te va <em>déjà.</em>"), None)]),
 ("Et pour payer moins aujourd'hui, code promo Hacou huit cent quarante-sept. Moins quatorze pour cent.", [(kara("Et pour <em>payer moins</em> aujourd'hui,"), None), (kara("<em>code promo</em>"), None), ('<u>HACOO847</u>', None), (kara("<i>-14 %</i>"), None)]),
 ("Sur cent trois euros d'exemple, tu paies quatre-vingt-huit euros et cinquante-huit centimes.", [(kara("Sur <em>103 €</em> d'exemple,"), None), (kara("tu paies"), None), (kara("<em>88,58 €.</em>"), None)]),
 ("Enregistre la vidéo, et envoie-la au pote qui renvoie tout.", [(kara("<em>Enregistre</em> la vidéo,"), None), (kara("et <i>envoie-la</i>"), None), (kara("au pote qui renvoie tout."), None)]),
]
SPLITS = [(0.2, 4.89), (5.34, 9.28), (9.73, 13.4), (13.85, 17.34), (17.79, 22.52), (22.97, 26.84), (27.29, 30.0)]

TAG_PRICE = '''<path class="ol" d="M40 120 L150 40 H330 Q350 40 350 60 V180 Q350 200 330 200 H150 Z" fill="#ffd84a"/>
<circle cx="105" cy="120" r="16" fill="#fff" class="ol"/>
<text x="262" y="136" text-anchor="middle" font-family="Inter,Arial Black,sans-serif" font-weight="900" font-size="42" fill="#141414">À VENDRE</text>'''
BOW = '''<path class="ol" d="M200 200 Q120 90 70 150 Q40 220 200 200 Q360 220 330 150 Q280 90 200 200 Z" fill="#ee3b3b"/>
<path class="ol" d="M200 200 L150 330 L190 310 L200 350 L210 310 L250 330 Z" fill="#ee3b3b"/><circle class="ol" cx="200" cy="200" r="30" fill="#ff6b6b"/>'''
SMALL = '''<text x="200" y="20" text-anchor="middle" font-family="Inter,Arial Black,sans-serif" font-weight="900" font-size="44" fill="#ee3b3b">TROP PETIT</text>'''

CSS = '''
.dood span{color:#8cc8f0;opacity:.5}
#sub u{display:inline-block;padding:2px 20px 6px;margin:0 4px;border-radius:12px;background:#ffd84a;color:#141414;border:5px solid #141414;text-decoration:none;text-transform:none;font-family:'DejaVu Sans Mono',Menlo,monospace}
.lc{text-transform:none!important}
.tk{left:170px;width:740px;padding:30px 40px 28px;font:800 34px Inter,'Arial Black',sans-serif}
.tk .r{display:flex;justify-content:space-between;padding:8px 0;white-space:nowrap}
.tk .r.red{color:#ee3b3b}
.tk .t{font:900 40px Inter,'Arial Black',sans-serif;text-align:center;margin-bottom:8px}
.tk .tot{border-top:5px dashed #141414;margin-top:10px;padding-top:14px;font-size:48px}
.tk .ex{text-align:center;font:700 24px Inter,sans-serif;color:#6b6257;margin-top:10px}
.st{position:relative;display:inline-block}
.st:after{content:'';position:absolute;left:-4px;right:-4px;top:52%;height:5px;background:#ee3b3b;transform:rotate(-4deg)}
.cp{left:130px;width:820px;padding:34px 44px 36px}
.cp .lab{font:900 34px Inter,'Arial Black',sans-serif;letter-spacing:2px}
.cp .f{margin-top:14px;height:110px;border:6px solid #141414;border-radius:20px;background:#fff;display:flex;align-items:center;padding:0 28px;font:900 66px 'DejaVu Sans Mono',Menlo,monospace}
.cp .ok{margin-top:16px;font:900 46px Inter,'Arial Black',sans-serif;color:#2fa35a}
.sz{left:150px;width:780px;padding:26px 36px;font:800 34px Inter,'Arial Black',sans-serif}
.sz .t{font:900 38px Inter,'Arial Black',sans-serif;text-align:center;margin-bottom:12px}
.sz .g{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.sz .g span{border:5px solid #141414;border-radius:16px;text-align:center;padding:14px 0;font:900 46px Inter,'Arial Black',sans-serif;background:#eaf4fc}
.sz .g span.on{background:#ffd84a}
.cond{position:absolute;left:90px;width:900px;text-align:center;font:700 26px Inter,sans-serif;color:#6b6257}
'''


def ic(name, x, y, s=170, g=None):
    return stk(x, y, s, s, ICONS[name], g=g, vb='0 0 200 200')


AV = (avatar(110, 110, '#f2c59a', '#3b2a20') + avatar(260, 110, '#c98b5e', '#141414', 'flat') + avatar(410, 110, '#f6d2b0', '#d8a24a', 'sad'))

BODY = chrome() + '''
  <div class="scene" data-s="0">''' + tag("RETOURS SUR L'APPLI") + ban('⚠ ATTENTION', 300, 'red', rot=-3) + ban("Trop petit sur l'appli ?", 425, size=60, rot=1) + ban('Ne le renvoie pas', 540, 'yel', size=60, rot=-1) + stk(150, 690, 380, 380, tee('#5fb3ff') + SMALL + ARROWS_IN, vb='0 0 400 400') + stk(600, 720, 300, 300, BOX, vb='0 0 400 400') + red_circle(580, 720, 340, 320, '0.3') + '''</div>
  <div class="scene" data-s="1" data-in="pop">''' + tag('TÉMOIGNAGES') + ban('des comptes bloqués', 310, size=60, rot=-2) + ban('après des remboursements', 425, 'red', size=50, rot=1, g='1.3') + stk(160, 600, 520, 230, AV + banned(410, 110, '1.2'), vb='0 0 520 230') + '''
   <div class="cond" style="top:900px;font-size:28px" data-g="1.0" data-fx="fade">témoignages d'utilisateurs, pas une règle officielle</div></div>
  <div class="scene" data-s="2" data-in="right">''' + tag('LE BON RÉFLEXE') + ban('✔ Revends-le', 300, 'grn', size=64, rot=-2, g='2.1') + ban('en seconde main', 410, size=54, rot=1, g='2.2') + ban('✔ Ou offre-le', 520, 'grn', size=64, rot=-1, g='2.3') + stk(130, 690, 360, 360, tee('#5fb3ff'), vb='0 0 400 400', g='2.0') + stk(420, 700, 330, 220, TAG_PRICE, vb='0 0 400 240', g='2.2') + stk(690, 860, 260, 260, BOW, vb='0 0 400 400', g='2.3') + '''</div>
  <div class="scene" data-s="3" data-in="pop">''' + tag('MON CONSEIL') + ban('La prochaine fois', 300, size=60, rot=-2) + '''
   <div class="card sz" style="top:430px" data-g="3.1" data-fx="pop"><div class="t">GUIDE DES TAILLES</div><div class="g"><span>S</span><span class="on">M</span><span>L</span><span>XL</span></div></div>''' + ban('compare avec un vêtement', 700, 'yel', size=48, rot=1, g='3.2') + ban('qui te va déjà', 800, 'yel', size=48, rot=-1, g='3.3') + stk(380, 920, 320, 320, tee('#2fa35a'), vb='0 0 400 400', g='3.2') + '''</div>
  <div class="scene" data-s="4" data-in="right">''' + tag('POUR PAYER MOINS') + '''
   <div class="card cp" style="top:320px"><div class="lab">CODE PROMO DU JOUR</div><div class="f"><span class="lc" data-g="4.2" data-fx="type">HACOO847</span></div><div class="ok" data-g="4.3" data-fx="fade">✓ -14 % appliqué</div></div>''' + ban('-14 %', 760, 'yel', g='4.3', fx='stamp', rot=-4, size=150) + ban("aujourd'hui seulement", 960, 'red', g='4.3', size=50, rot=2) + '''</div>
  <div class="scene" data-s="5" data-in="pop">''' + tag("PANIER D'EXEMPLE") + ic('Survêt', 110, 300, 210, g='5.0') + ic('Doudoune', 430, 290, 220, g='5.0') + ic('Bonnet', 760, 310, 190, g='5.0') + '''
   <div class="card tk" style="top:560px"><div class="r"><span>Survêt</span><span>36,00 €</span></div><div class="r"><span>Doudoune</span><span>58,00 €</span></div><div class="r"><span>Bonnet</span><span>9,00 €</span></div>
    <div class="r"><span>Sous-total</span><span class="st">103,00 €</span></div><div class="r red" data-g="5.1" data-fx="left"><span>Code <span class="lc">HACOO847</span> -14 %</span><span>-14,42 €</span></div>
    <div class="r tot"><span>Total</span><span data-g="5.2" data-fx="stamp" data-slow="5.2">88,58 €</span></div><div class="ex">prix d'exemple</div></div></div>
  <div class="scene" data-s="6" data-in="pop">''' + tag('PARTAGE') + stk(430, 280, 220, 300, BOOKMARK, g='6.0', vb='0 0 260 320') + ban('Enregistre cette vidéo', 620, size=52, g='6.0', rot=-2) + ban('Envoie-la ↗', 735, 'red', g='6.1', rot=2, size=56) + '''
   <div class="ban" style="top:860px" data-g="6.2" data-fx="up"><span class="pill" style="background:#ffd84a;font-size:44px">CODE PROMO : <span class="mono lc">HACOO847</span></span></div>
   <div class="ban" style="top:955px" data-g="6.2" data-fx="up"><span class="pill" style="background:#fff;font-size:38px">-14 % · aujourd'hui seulement</span></div>
   <div class="ban" style="top:1040px" data-g="6.2" data-fx="up"><span class="pill" style="background:#fff;font-size:34px">liens des articles tendance en bio</span></div>
   <div class="cond" style="top:1440px">Offre soumise aux conditions en vigueur · prix d'exemple</div></div>
'''
