import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from alerte import *
from hacoo_items import ICONS
# Hacoo, 27/11/2026, vidéo 3 (compte affiliation, tâche « 2 vidéos Hacoo en plus ») - style A « Alerte stickers », gribouillis abricot.
# Format F1 mise en garde « budget cadeaux » : « Panier à 115 € ? Ne retire rien » -> le mauvais réflexe (enlever un article)
# -> avant de payer, la case code promo -> code promo hzklink -14 % -> panier d'exemple doudoune 58 € + bottines 39 € + bonnet 10 €
# + gants 8 € = 115,00 € -> -16,10 € -> total 98,90 € (ralenti) « ça rentre dans le budget de 100 € » -> fin « enregistre / envoie-la ».
# Calcul : 115,00 × 0,14 = 16,10 ; 115,00 × 0,86 = 98,90 ; 115,00 - 16,10 = 98,90. Prix d'exemple, articles génériques sans marque.
# Règle du 26/11 : « Hacoo » n'est JAMAIS écrit à l'image (ni sous-titres) : seulement dit à l'oral (« l'appli Hacou », « code promo Hacou »).
# Voix : Marc (azure, fr-FR-Marc:MAI-Voice-2.1), speed 1.08, une synthèse par réplique, silences coupés (internes plafonnés à 0,16 s),
# atempo 1.2, chaque réplique normalisée à -19 dB moyen, recollées avec 0,2 s au début et 0,45 s entre elles (SPLITS).
NAME = 'hacoo65'
TITLE = 'Alerte budget cadeaux abricot'
MINLEN = 1.6
GAP = 0.22
TAIL = 2.2
LINES = [
 ("Attention. Ton panier sur l'appli Hacou fait cent quinze euros, pour un budget de cent ? Ne retire rien.", [(kara("<i>Attention.</i>"), None), (kara("Ton panier sur l'appli"), None), (kara("fait <em>115 €,</em>"), None), (kara("pour un budget de 100 ?"), None), (kara("<i>Ne retire rien.</i>"), None)]),
 ("Le réflexe, c'est d'enlever un article. Attends : avant de payer, il y a la case code promo.", [(kara("Le réflexe,"), None), (kara("c'est d'<i>enlever</i> un article."), None), (kara("<em>Attends :</em>"), None), (kara("avant de payer,"), None), (kara("il y a la case <em>code promo.</em>"), None)]),
 ("Code promo Hacou : H, Z, K, link. Moins quatorze pour cent.", [(kara("<em>Code promo</em>"), None), ('<u>hzklink</u>', None), (kara("<i>-14 %</i>"), None)]),
 ("Doudoune, bottines, bonnet et gants : cent quinze euros d'exemple.", [(kara("Doudoune, bottines,"), None), (kara("bonnet et gants :"), None), (kara("<em>115 €</em> d'exemple."), None)]),
 ("Avec le code, ça fait seize euros et dix centimes de moins.", [(kara("Avec le code,"), None), (kara("ça fait <i>16,10 €</i>"), None), (kara("de moins."), None)]),
 ("Tu paies quatre-vingt-dix-huit euros et quatre-vingt-dix centimes. Ça rentre dans le budget.", [(kara("Tu paies"), None), (kara("<em>98,90 €.</em>"), None), (kara("Ça rentre"), None), (kara("dans le <em>budget.</em>"), None)]),
 ("Enregistre la vidéo avant tes cadeaux. Code promo Hacou, H, Z, K, link.", [(kara("<em>Enregistre</em> la vidéo"), None), (kara("avant tes cadeaux."), None), (kara("<em>Code promo</em>"), None), ('<u>hzklink</u>', None)]),
]
SPLITS = [(0.2, 4.59), (5.04, 8.91), (9.36, 16.12), (16.57, 19.95), (20.4, 22.96), (23.41, 27.0), (27.45, 32.46)]

PRICE = '''<path class="ol" d="M40 120 L150 40 H330 Q350 40 350 60 V180 Q350 200 330 200 H150 Z" fill="#ffd84a"/>
<circle cx="105" cy="120" r="16" fill="#fff" class="ol"/>
<text x="250" y="140" text-anchor="middle" font-family="Inter,Arial Black,sans-serif" font-weight="900" font-size="62" fill="#141414">115 €</text>'''
WALLET = '''<path class="ol" d="M40 110 Q40 80 70 80 H320 Q350 80 350 110 V300 Q350 330 320 330 H70 Q40 330 40 300 Z" fill="#7a5a3a"/>
<path class="ol" d="M250 160 H360 V250 H250 Q220 250 220 205 Q220 160 250 160 Z" fill="#a07850"/><circle cx="260" cy="205" r="14" fill="#ffd84a" class="ol"/>
<text x="140" y="230" text-anchor="middle" font-family="Inter,Arial Black,sans-serif" font-weight="900" font-size="58" fill="#fff">100 €</text>'''
CROSS = '<path d="M30 30 L170 170 M170 30 L30 170" stroke="#ee3b3b" stroke-width="22" stroke-linecap="round"/>'

CSS = '''
.dood span{color:#f5a35c;opacity:.55}
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


TICKET_TOP = '''<div class="r"><span>Doudoune</span><span>58,00 €</span></div><div class="r"><span>Bottines</span><span>39,00 €</span></div>
    <div class="r"><span>Bonnet</span><span>10,00 €</span></div><div class="r"><span>Gants</span><span>8,00 €</span></div>'''

BODY = chrome() + '''
  <div class="scene" data-s="0">''' + tag('BUDGET CADEAUX') + ban('⚠ ATTENTION', 300, 'red', rot=-3) + ban('Panier à 115 € ?', 425, size=64, rot=1) + ban('Ne retire rien', 545, 'yel', size=64, rot=-1) + stk(130, 700, 380, 240, PRICE, vb='0 0 400 240') + stk(560, 690, 360, 330, WALLET, vb='0 0 400 360') + red_circle(110, 680, 420, 290, '0.3') + '''</div>
  <div class="scene" data-s="1" data-in="pop">''' + tag('LE MAUVAIS RÉFLEXE') + ban('✖ Enlever un article', 300, 'red', size=58, rot=-2) + ic('Bonnet', 150, 430, 230, g='1.0') + stk(150, 430, 230, 230, CROSS, g='1.1', fx='stamp', vb='0 0 200 200') + ban('Attends !', 470, 'yel', g='1.2', size=64, rot=3).replace('class="ban yel"', 'class="ban yel" ', 1).replace('top:470px', 'top:500px;left:420px;width:auto') + '''
   <div class="card cp" style="top:720px" data-g="1.3" data-fx="pop"><div class="lab">CODE PROMO</div><div class="f e">________</div><div class="pay">Payer</div></div>
   <div class="cond" style="top:1080px;font-size:30px;color:#141414;font-weight:900" data-g="1.4" data-fx="fade">↑ la case est avant « Payer »</div></div>
  <div class="scene" data-s="2" data-in="right">''' + tag('CODE PROMO') + '''
   <div class="card cp" style="top:320px"><div class="lab">CODE PROMO</div><div class="f"><span class="lc" data-g="2.1" data-fx="type">hzklink</span></div><div class="ok" data-g="2.2" data-fx="fade">✓ -14 % appliqué</div></div>''' + ban('-14 %', 760, 'yel', g='2.2', fx='stamp', rot=-4, size=150) + '''</div>
  <div class="scene" data-s="3-4" data-in="pop">''' + tag("PANIER D'EXEMPLE") + ic('Doudoune', 90, 290, 200, g='3.0') + ic('Bottines', 320, 300, 190, g='3.0') + ic('Bonnet', 545, 305, 180, g='3.1') + ic('Gants', 760, 305, 180, g='3.1') + '''
   <div class="card tk" style="top:530px">''' + TICKET_TOP + '''
    <div class="r tot"><span>Sous-total</span><span data-g="3.2" data-fx="stamp">115,00 €</span></div>
    <div class="r red" data-g="4.1" data-fx="left"><span>Code promo -14 %</span><span>-16,10 €</span></div><div class="ex">prix d'exemple</div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + tag('TOTAL') + '''
   <div class="card tk" style="top:300px">''' + TICKET_TOP + '''
    <div class="r"><span>Sous-total</span><span class="st">115,00 €</span></div><div class="r red"><span>Code promo -14 %</span><span>-16,10 €</span></div>
    <div class="r tot"><span>Total</span><span data-g="5.1" data-fx="stamp" data-slow="5.1">98,90 €</span></div><div class="ex">prix d'exemple</div></div>''' + ban('✔ Budget 100 € respecté', 900, 'grn', g='5.2', size=54, rot=-2) + '''</div>
  <div class="scene" data-s="6" data-in="pop">''' + tag('PARTAGE') + stk(430, 280, 220, 300, BOOKMARK, g='6.0', vb='0 0 260 320') + ban('Enregistre cette vidéo', 620, size=52, g='6.0', rot=-2) + ban('Envoie-la ↗', 735, 'red', g='6.1', rot=2, size=56) + '''
   <div class="ban" style="top:860px" data-g="6.2" data-fx="up"><span class="pill" style="background:#ffd84a;font-size:44px">CODE PROMO : <span class="mono lc">hzklink</span></span></div>
   <div class="ban" style="top:955px" data-g="6.2" data-fx="up"><span class="pill" style="background:#fff;font-size:38px">-14 % avec le code <span class="mono lc">hzklink</span></span></div>
   <div class="ban" style="top:1040px" data-g="6.2" data-fx="up"><span class="pill" style="background:#fff;font-size:34px">liens des articles tendance en bio</span></div>
   <div class="cond" style="top:1440px">Offre soumise aux conditions en vigueur · prix d'exemple</div></div>
'''
GSTART = [[], [], [9.36, 10.7, 14.55], [], [], [], []]
