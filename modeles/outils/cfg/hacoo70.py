import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from alerte import *
from hacoo_items import ICONS
# Hacoo, 28/11/2026, vidéo 4 (compte affiliation, tâche « 2 vidéos Hacoo en plus ») - style A « Alerte stickers », gribouillis vert menthe.
# Format mise en garde en 3 points « Cadeaux de Noël ? Regarde la date de livraison » : ① la livraison estimée avant de payer (avant le réveillon)
# -> ② commander tôt, pas la dernière semaine -> ③ la case code promo, hzklink -14 % -> panier d'exemple plaid 29 € + gants 14 € + mug 9 €
# = 52,00 € -> -7,28 € -> 44,72 € (ralenti) -> fin « enregistre / envoie-la ». Aucune date ni délai de livraison affirmé : seulement des conseils.
# Calcul : 52,00 × 0,14 = 7,28 ; 52,00 × 0,86 = 44,72 ; 52,00 - 7,28 = 44,72. Prix d'exemple, articles génériques sans marque.
# Règle du 26/11 : « Hacoo » n'est JAMAIS écrit à l'image (ni sous-titres) : seulement dit à l'oral (« l'appli Hacou », « code promo Hacou »).
# Voix : Mathieu (inworld), speed 1.08, une synthèse par réplique (réplique 5 refaite une fois : « plaid, gants et mug » compris « Plade, Gantemogue »),
# silences internes plafonnés à 0,16 s, atempo 1.1, -19 dB moyen, recollées avec 0,2 s au début et 0,45 s entre elles (SPLITS).
NAME = 'hacoo70'
TITLE = 'Alerte livraison Noel menthe'
MINLEN = 1.6
GAP = 0.22
TAIL = 2.2
LINES = [
 ("Attention. Tu commandes tes cadeaux de Noël sur l'appli Hacou ? Regarde d'abord la date de livraison.", [(kara("<i>Attention.</i>"), None), (kara("Tu commandes tes cadeaux"), None), (kara("de Noël sur l'appli ?"), "de Noël sur l'appli Hacou ?"), (kara("Regarde d'abord"), None), (kara("la <em>date de livraison.</em>"), None)]),
 ("Un : avant de payer, regarde la livraison estimée. Elle doit tomber avant le réveillon.", [(kara("<em>Un :</em> avant de payer,"), None), (kara("regarde la livraison"), None), (kara("<em>estimée.</em>"), None), (kara("Elle doit tomber"), None), (kara("avant le <em>réveillon.</em>"), None)]),
 ("Deux : commande tôt. Pas la dernière semaine.", [(kara("<em>Deux :</em> commande tôt."), None), (kara("<i>Pas</i> la dernière semaine."), None)]),
 ("Trois : la case code promo. Code promo Hacou : H, Z, K, link. Moins quatorze pour cent.", [(kara("<em>Trois :</em> la case"), None), (kara("code promo."), None), (kara("<em>Code promo</em>"), "Code promo Hacou :"), ('<u>hzklink</u>', "H, Z, K, link."), (kara("<i>-14 %</i>"), "Moins quatorze pour cent.")]),
 ("Un plaid, des gants, un mug : cinquante-deux euros d'exemple. Ça fait sept euros et vingt-huit centimes de moins.", [(kara("Un plaid, des gants,"), None), (kara("un mug :"), None), (kara("<em>52 €</em> d'exemple."), "cinquante-deux euros d'exemple."), (kara("Ça fait <i>7,28 €</i>"), "Ça fait sept euros et vingt-huit centimes"), (kara("de moins."), None)]),
 ("Tu paies quarante-quatre euros et soixante-douze centimes.", [(kara("Tu paies"), None), (kara("<em>44,72 €.</em>"), "quarante-quatre euros et soixante-douze centimes.")]),
 ("Enregistre la vidéo pour tes cadeaux. Code promo Hacou, H, Z, K, link.", [(kara("<em>Enregistre</em> la vidéo"), None), (kara("pour tes cadeaux."), None), (kara("<em>Code promo</em>"), "Code promo Hacou,"), ('<u>hzklink</u>', "H, Z, K, link.")]),
]
SPLITS = [(0.2, 3.975), (4.425, 7.946), (8.396, 10.102), (10.552, 15.6), (16.05, 20.799), (21.248, 23.686), (24.136, 28.118)]

CAL = '''<rect x="112" y="36" width="24" height="64" rx="12" fill="#141414"/><rect x="264" y="36" width="24" height="64" rx="12" fill="#141414"/>
<rect class="ol" x="50" y="70" width="300" height="290" rx="26" fill="#fff"/><path class="ol" d="M50 150 V96 Q50 70 76 70 H324 Q350 70 350 96 V150 Z" fill="#ee3b3b"/>
<text x="200" y="130" text-anchor="middle" font-family="Inter,Arial Black,sans-serif" font-weight="900" font-size="52" fill="#fff">DÉC</text>
<text x="200" y="310" text-anchor="middle" font-family="Inter,Arial Black,sans-serif" font-weight="900" font-size="150" fill="#141414">24</text>'''
WEEK = '''<rect class="ol" x="20" y="40" width="360" height="150" rx="20" fill="#fff"/>''' + ''.join(f'<rect x="{34+k*50}" y="80" width="40" height="40" rx="8" fill="{"#ffb3b3" if k>3 else "#d7f5e8"}" stroke="#141414" stroke-width="5"/>' for k in range(7)) + '''
<text x="200" y="170" text-anchor="middle" font-family="Inter,Arial Black,sans-serif" font-weight="900" font-size="34" fill="#141414">DERNIÈRE SEMAINE</text>'''
CROSS = '<path d="M30 30 L170 170 M170 30 L30 170" stroke="#ee3b3b" stroke-width="22" stroke-linecap="round"/>'

CSS = '''
.dood span{color:#3fc28f;opacity:.55}
#sub u{display:inline-block;padding:2px 20px 6px;margin:0 4px;border-radius:12px;background:#ffd84a;color:#141414;border:5px solid #141414;text-decoration:none;text-transform:none;font-family:'DejaVu Sans Mono',Menlo,monospace}
.lc{text-transform:none!important}
.tk{left:170px;width:740px;padding:26px 40px 24px;font:800 34px Inter,'Arial Black',sans-serif}
.tk .r{display:flex;justify-content:space-between;padding:6px 0;white-space:nowrap}
.tk .r.red{color:#ee3b3b}
.tk .tot{border-top:5px dashed #141414;margin-top:10px;padding-top:12px;font-size:50px}
.tk .ex{text-align:center;font:700 24px Inter,sans-serif;color:#6b6257;margin-top:8px}
.st{position:relative;display:inline-block}
.st:after{content:'';position:absolute;left:-4px;right:-4px;top:52%;height:5px;background:#ee3b3b;transform:rotate(-4deg)}
.cp{left:130px;width:820px;padding:30px 44px 32px}
.cp .lab{font:900 34px Inter,'Arial Black',sans-serif;letter-spacing:2px}
.cp .f{margin-top:14px;height:110px;border:6px solid #141414;border-radius:20px;background:#fff;display:flex;align-items:center;padding:0 28px;font:900 66px 'DejaVu Sans Mono',Menlo,monospace}
.cp .f.e{color:#b9b0a4}
.cp .ok{margin-top:16px;font:900 46px Inter,'Arial Black',sans-serif;color:#2fa35a}
.cp .pay{margin-top:18px;height:96px;border-radius:20px;background:#141414;color:#fff;display:flex;align-items:center;justify-content:center;font:900 46px Inter,'Arial Black',sans-serif}
.cond{position:absolute;left:90px;width:900px;text-align:center;font:700 26px Inter,sans-serif;color:#6b6257}
'''


def ic(name, x, y, s=170, g=None):
    return stk(x, y, s, s, ICONS[name], g=g, vb='0 0 200 200')


TICKET_TOP = '''<div class="r"><span>Plaid</span><span>29,00 €</span></div><div class="r"><span>Gants</span><span>14,00 €</span></div>
    <div class="r"><span>Mug</span><span>9,00 €</span></div>'''

BODY = chrome() + '''
  <div class="scene" data-s="0">''' + tag('CADEAUX DE NOËL') + ban('⚠ ATTENTION', 300, 'red', rot=-3) + ban('Cadeaux de Noël ?', 425, size=64, rot=1) + ban('Regarde la livraison', 545, 'yel', size=64, rot=-1) + stk(120, 700, 380, 380, BOX, vb='0 0 400 400') + stk(560, 700, 360, 360, CAL, vb='0 0 400 400') + red_circle(540, 690, 400, 400, '0.3') + '''</div>
  <div class="scene" data-s="1" data-in="pop">''' + tag('① LIVRAISON ESTIMÉE') + ban('Avant de payer', 300, 'yel', size=60, rot=-2) + '''
   <div class="card cp" style="top:450px" data-g="1.1" data-fx="pop"><div class="lab">LIVRAISON ESTIMÉE</div><div class="f e" style="font-size:52px">regarde la date</div><div class="pay">Payer</div></div>''' + stk(425, 758, 230, 230, CAL, g='1.3', vb='0 0 400 400') + ban('✔ Avant le réveillon ?', 995, 'grn', g='1.4', size=54, rot=2) + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + tag('② COMMANDE TÔT') + ban('✔ Commande tôt', 300, 'grn', size=64, rot=-2) + stk(140, 470, 800, 380, WEEK, g='2.1', vb='0 0 400 200') + stk(660, 575, 175, 175, CROSS, g='2.1', fx='stamp', vb='0 0 200 200') + ban('✖ Pas la dernière semaine', 900, 'red', g='2.1', size=54, rot=2) + '''</div>
  <div class="scene" data-s="3" data-in="right">''' + tag('③ CODE PROMO') + '''
   <div class="card cp" style="top:320px"><div class="lab">CODE PROMO</div><div class="f"><span class="lc" data-g="3.3" data-fx="type">hzklink</span></div><div class="ok" data-g="3.4" data-fx="fade">✓ -14 % appliqué</div></div>''' + ban('-14 %', 760, 'yel', g='3.4', fx='stamp', rot=-4, size=150) + '''</div>
  <div class="scene" data-s="4" data-in="pop">''' + tag("PANIER D'EXEMPLE") + ic('Plaid', 130, 290, 210, g='4.0') + ic('Gants', 420, 300, 200, g='4.0') + ic('Mug', 700, 300, 200, g='4.1') + '''
   <div class="card tk" style="top:540px">''' + TICKET_TOP + '''
    <div class="r tot"><span>Sous-total</span><span data-g="4.2" data-fx="stamp">52,00 €</span></div>
    <div class="r red" data-g="4.3" data-fx="left"><span>Code promo -14 %</span><span>-7,28 €</span></div><div class="ex">prix d'exemple</div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + tag('TOTAL') + '''
   <div class="card tk" style="top:300px">''' + TICKET_TOP + '''
    <div class="r"><span>Sous-total</span><span class="st">52,00 €</span></div><div class="r red"><span>Code promo -14 %</span><span>-7,28 €</span></div>
    <div class="r tot"><span>Total</span><span data-g="5.1" data-fx="stamp" data-slow="5.1">44,72 €</span></div><div class="ex">prix d'exemple</div></div>''' + ban('✔ Cadeaux moins chers', 860, 'grn', g='5.1', size=54, rot=-2) + '''</div>
  <div class="scene" data-s="6" data-in="pop">''' + tag('PARTAGE') + stk(430, 280, 220, 300, BOOKMARK, g='6.0', vb='0 0 260 320') + ban('Enregistre cette vidéo', 620, size=52, g='6.0', rot=-2) + ban('Envoie-la ↗', 735, 'red', g='6.1', rot=2, size=56) + '''
   <div class="ban" style="top:860px" data-g="6.2" data-fx="up"><span class="pill" style="background:#ffd84a;font-size:44px">CODE PROMO : <span class="mono lc">hzklink</span></span></div>
   <div class="ban" style="top:955px" data-g="6.2" data-fx="up"><span class="pill" style="background:#fff;font-size:38px">-14 % avec le code <span class="mono lc">hzklink</span></span></div>
   <div class="ban" style="top:1040px" data-g="6.2" data-fx="up"><span class="pill" style="background:#fff;font-size:34px">liens des articles tendance en bio</span></div>
   <div class="cond" style="top:1440px">Offre soumise aux conditions en vigueur · prix d'exemple</div></div>
'''
