import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from alerte import *
from hacoo_items import ICONS
# Hacoo, 24/11/2026, vidéo 3 (compte affiliation, tâche « 2 vidéos Hacoo en plus ») - style A « Alerte stickers », accent rouge Noël / vert sapin,
# format F1 mise en garde saisonnière : « Cadeaux de Noël sur Hacoo ? Lis ça avant » + 3 réflexes numérotés (date de livraison estimée /
# total final livraison comprise / case code promo), fin « enregistre ». Sans sujet R (déjà traité par la vidéo 1 du jour).
# Aucune affirmation sur les délais réels ni sur une opération promo : on dit seulement de REGARDER la date estimée et le total avant de payer.
# Panier d'exemple : pyjama 29 € + guirlande 13 € + porte-clés 7 € = 49,00 € ; -14 % = 6,86 € ; total 42,14 €. Prix d'exemple.
# Voix : Marc (azure, fr-FR-Marc:MAI-Voice-2.1), speed 1.08, une synthèse par réplique, silences coupés (internes plafonnés à 0,16 s),
# atempo 1.12, +4 dB, 0,2 s au début et 0,45 s entre les répliques.
NAME = 'hacoo53'
TITLE = 'Hacoo alerte cadeaux de Noël'
MINLEN = 1.6
GAP = 0.22
TAIL = 2.2
LINES = [
 ("Tu fais tes cadeaux de Noël sur l'appli Hacou ? Attends, lis ça.", [(kara("Tes <em>cadeaux de Noël</em>"), None), (kara("sur l'appli <em>Hacoo</em> ?"), None), (kara("<i>Attends,</i> lis ça."), None)]),
 ("Réflexe un : regarde la date de livraison estimée, avant de payer.", [(kara("<em>Réflexe 1 :</em>"), None), (kara("regarde la date"), None), (kara("de <em>livraison</em> estimée,"), None), (kara("<i>avant</i> de payer."), None)]),
 ("Réflexe deux : vérifie le total final, livraison comprise, pas juste le prix des articles.", [(kara("<em>Réflexe 2 :</em>"), None), (kara("vérifie le <em>total final</em>,"), None), (kara("livraison comprise,"), None), (kara("pas juste le prix"), None), (kara("des articles."), None)]),
 ("Réflexe trois : code promo Hacou, H, Z, K, link, dans la case code promo. Moins quatorze pour cent.", [(kara("<em>Réflexe 3 :</em>"), None), (kara("<em>code promo Hacoo</em>"), None), ('<u>hzklink</u>', None), (kara("dans la case code promo."), None), (kara("<i>-14 %</i>"), None)]),
 ("Pyjama, guirlande, porte-clés : quarante-neuf euros.", [(kara("Pyjama, guirlande,"), None), (kara("porte-clés :"), None), (kara("<em>49 €</em>."), None)]),
 ("Avec le code, ça fait quarante-deux euros et quatorze centimes.", [(kara("Avec le code,"), None), (kara("ça fait"), None), (kara("<em>42,14 €</em>."), None)]),
 ("Enregistre cette vidéo pour tes cadeaux. Les liens des articles sont dans ma bio.", [(kara("<em>Enregistre</em> cette vidéo"), None), (kara("pour tes cadeaux."), None), (kara("Les liens des articles"), None), (kara("sont dans ma bio."), None)]),
]
SPLITS = [(0.2, 2.75), (3.2, 6.89), (7.34, 11.63), (12.08, 16.99), (17.44, 20.28), (20.73, 23.52), (23.97, 27.26)]

GIFT = '''<rect class="ol" x="60" y="170" width="280" height="200" rx="14" fill="#ee3b3b"/>
<rect class="ol" x="40" y="120" width="320" height="70" rx="14" fill="#f25a5a"/>
<rect class="ol" x="176" y="120" width="48" height="250" fill="#2fa35a"/>
<path class="ol" d="M200 120 Q140 40 110 80 Q90 120 200 120 Q310 120 290 80 Q260 40 200 120 Z" fill="#2fa35a"/>
<path d="M80 200 V300" stroke="#ff9a9a" stroke-width="12" stroke-linecap="round"/>'''

CAL = '''<rect class="ol" x="50" y="70" width="300" height="290" rx="30" fill="#fff"/>
<path class="ol" d="M50 100 Q50 70 80 70 H320 Q350 70 350 100 V150 H50 Z" fill="#ee3b3b"/>
<rect class="ol" x="110" y="40" width="26" height="70" rx="13" fill="#c9d0d8"/><rect class="ol" x="264" y="40" width="26" height="70" rx="13" fill="#c9d0d8"/>
<text x="200" y="135" text-anchor="middle" font-family="Inter,Arial Black,sans-serif" font-weight="900" font-size="44" fill="#fff">DÉCEMBRE</text>
<text x="200" y="305" text-anchor="middle" font-family="Inter,Arial Black,sans-serif" font-weight="900" font-size="150" fill="#141414">24</text>'''

CSS = '''
#sub u{display:inline-block;padding:2px 20px 6px;margin:0 4px;border-radius:12px;background:#ffd84a;color:#141414;border:5px solid #141414;text-decoration:none;text-transform:none;font-family:'DejaVu Sans Mono',Menlo,monospace}
.lc{text-transform:none!important}
.tk{left:170px;width:740px;padding:30px 40px 28px;font:800 34px Inter,'Arial Black',sans-serif}
.tk .r{display:flex;justify-content:space-between;padding:8px 0;white-space:nowrap}
.tk .r.red{color:#ee3b3b}
.tk .r.grey{color:#8a8178}
.tk .t{font:900 40px Inter,'Arial Black',sans-serif;text-align:center;margin-bottom:8px}
.tk .tot{border-top:5px dashed #141414;margin-top:10px;padding-top:14px;font-size:48px}
.tk .ex{text-align:center;font:700 24px Inter,sans-serif;color:#6b6257;margin-top:10px}
.dl{left:170px;width:740px;padding:26px 36px;font:800 34px Inter,'Arial Black',sans-serif}
.dl .t{font:900 36px Inter,'Arial Black',sans-serif;margin-bottom:10px}
.dl .d{display:flex;justify-content:space-between;align-items:center;border:5px solid #141414;border-radius:18px;padding:14px 20px;background:#eaf7ef}
.cp{left:130px;top:430px;width:820px;padding:34px 44px 36px}
.cp .lab{font:900 34px Inter,'Arial Black',sans-serif;letter-spacing:2px}
.cp .f{margin-top:14px;height:110px;border:6px solid #141414;border-radius:20px;background:#fff;display:flex;align-items:center;padding:0 28px;font:900 66px 'DejaVu Sans Mono',Menlo,monospace}
.cp .ok{margin-top:16px;font:900 46px Inter,'Arial Black',sans-serif;color:#2fa35a}
.cond{position:absolute;left:90px;width:900px;text-align:center;font:700 26px Inter,sans-serif;color:#6b6257}
'''


def ic(name, x, y, s=170, g=None):
    return stk(x, y, s, s, ICONS[name], g=g, vb='0 0 200 200')


BODY = chrome() + '''
  <div class="scene" data-s="0">''' + tag('CADEAUX DE NOËL') + ban('⚠ ATTENTION', 300, 'red', rot=-3) + ban('Cadeaux sur Hacoo ?', 425, size=58, rot=1) + ban('Lis ça avant', 535, 'yel', size=54, rot=-1) + stk(190, 680, 360, 360, GIFT, vb='0 0 400 400') + stk(560, 700, 300, 300, BOX, vb='0 0 400 400') + '''</div>
  <div class="scene" data-s="1" data-in="pop">''' + tag('RÉFLEXE 1') + ban('La date de livraison', 300, 'yel', rot=-2, size=56) + ban('AVANT de payer', 415, 'grn', g='1.3', fx='stamp', rot=2, size=58) + stk(80, 560, 320, 320, CAL, g='1.1', vb='0 0 400 400') + '''
   <div class="card dl" style="left:440px;width:520px;top:640px" data-g="1.2" data-fx="right"><div class="t">Livraison estimée</div><div class="d"><span>📦 regarde-la</span><span>✓</span></div></div>''' + red_circle(445, 715, 520, 120, '1.3') + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + tag('RÉFLEXE 2') + ban('Le total final', 300, 'grn', rot=-2, size=62) + ban('livraison comprise', 415, size=54, g='2.2', rot=1) + '''
   <div class="card tk" style="top:560px"><div class="t">RÉCAP COMMANDE</div><div class="r"><span>Articles</span><span>49,00 €</span></div><div class="r grey"><span>Livraison</span><span>à vérifier</span></div><div class="r tot"><span>Total final</span><span>?</span></div><div class="ex">prix d'exemple</div></div>''' + red_circle(110, 738, 860, 160, '2.1') + '''</div>
  <div class="scene" data-s="3" data-in="pop">''' + tag('RÉFLEXE 3') + '''
   <div class="card cp" style="top:330px"><div class="lab">CODE PROMO HACOO</div><div class="f"><span class="lc" data-g="3.2" data-fx="type">hzklink</span></div><div class="ok" data-g="3.4" data-fx="fade">✓ -14 % appliqué</div></div>''' + ban('-14 %', 820, 'yel', g='3.4', fx='stamp', rot=-4, size=150) + '''</div>
  <div class="scene" data-s="4" data-in="right">''' + tag('MES CADEAUX') + ic('Pyjama', 110, 330, 220, g='4.0') + ic('Guirlande', 430, 300, 220, g='4.1') + ic('Porte-clés', 750, 330, 200, g='4.1') + '''
   <div class="card tk" style="top:640px"><div class="r"><span>Pyjama</span><span>29,00 €</span></div><div class="r"><span>Guirlande</span><span>13,00 €</span></div><div class="r"><span>Porte-clés</span><span>7,00 €</span></div>
    <div class="r tot" data-g="4.2" data-fx="stamp"><span>Sous-total</span><span>49,00 €</span></div><div class="ex">prix d'exemple</div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + tag('CODE PROMO HACOO') + '''
   <div class="card tk" style="top:330px"><div class="r"><span>Sous-total</span><span>49,00 €</span></div><div class="r red" data-g="5.0" data-fx="left"><span>Code <span class="lc">hzklink</span> -14 %</span><span>-6,86 €</span></div>
    <div class="r tot"><span>Total</span><span data-g="5.2" data-fx="stamp" data-slow="5.2">42,14 €</span></div><div class="ex">prix d'exemple</div></div>''' + ban('42,14 €', 800, 'grn', g='5.2', fx='stamp', rot=-3, size=130) + '''</div>
  <div class="scene" data-s="6" data-in="pop">''' + tag('PARTAGE') + stk(430, 290, 220, 300, BOOKMARK, g='6.0', vb='0 0 260 320') + ban('Enregistre cette vidéo', 630, size=50, g='6.0', rot=-2) + ban('pour tes cadeaux 🎁', 750, 'red', g='6.1', rot=2, size=52) + '''
   <div class="ban" style="top:880px" data-g="6.2" data-fx="up"><span class="pill" style="background:#ffd84a;font-size:44px">CODE PROMO HACOO : <span class="mono lc">hzklink</span></span></div>
   <div class="ban" style="top:975px" data-g="6.3" data-fx="up"><span class="pill" style="background:#fff;font-size:38px">-14 % sur l'appli Hacoo</span></div>
   <div class="ban" style="top:1060px" data-g="6.3" data-fx="up"><span class="pill" style="background:#fff;font-size:34px">liens des articles tendance en bio</span></div>
   <div class="cond" style="top:1470px">Offre soumise aux conditions en vigueur sur l'appli Hacoo · prix d'exemple</div></div>
'''
