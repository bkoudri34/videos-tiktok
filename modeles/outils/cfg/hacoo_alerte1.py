import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from alerte import *
from hacoo_items import icon
# Hacoo, 1er exemple du style A « Alerte stickers » (22/11/2026), format F1 STOP / erreur à éviter :
# « Attention avant de demander un remboursement sur Hacoo ».
# Ce qu'on affirme : des utilisateurs RACONTENT un compte bloqué après des remboursements (avis Trustpilot / Reddit consultés le 22/11) ;
# on ne reprend pas les détails invérifiables de la vidéo repérée (IP, carte, appareil, « à vie »).
# Bon réflexe : revendre en seconde main + guide des tailles ; code promo Hacoo hzklink -14 %. Prix d'exemple.
NAME = 'hacoo_alerte1'
TITLE = 'Hacoo alerte remboursement'
LINES = [
 ("Attention avant de demander un remboursement sur l'appli Hacou.", [(kara("<i>Attention</i> avant"), None), (kara("de demander"), None), (kara("un <em>remboursement</em>"), None), (kara("sur <em>Hacoo</em>."), None)]),
 ("Beaucoup d'utilisateurs racontent que leur compte a été bloqué juste après.", [(kara("Beaucoup d'utilisateurs"), None), (kara("racontent que leur"), None), (kara("<i>compte</i> a été <i>bloqué</i>"), None), (kara("juste après."), None)]),
 ("Pourquoi ? Certains demandaient un remboursement... et gardaient l'article.", [(kara("<em>Pourquoi ?</em>"), None), (kara("Certains demandaient"), None), (kara("un remboursement..."), None), (kara("et <i>gardaient</i> l'article."), None)]),
 ("Le bon réflexe : un article trop petit ? Revends-le en seconde main.", [(kara("Le <em>bon réflexe</em> :"), None), (kara("un article"), None), (kara("<i>trop petit</i> ?"), None), (kara("Revends-le"), None), (kara("en <em>seconde main</em>."), None)]),
 ("Et avant de commander, regarde toujours le guide des tailles.", [(kara("Et avant de commander,"), None), (kara("regarde <em>toujours</em>"), None), (kara("le <em>guide des tailles</em>."), None)]),
 ("Et pour payer moins : code promo Hacou, H Z K link, moins quatorze pour cent.", [(kara("Et pour <em>payer moins</em> :"), None), (kara("<em>code promo Hacoo</em>"), None), (kara("<em>hzklink</em>,"), None), (kara("<i>-14 %</i>."), None)]),
 ("Enregistre la vidéo, et envoie-la au pote qui fait des retours. Code promo Hacou, H Z K link.", [(kara("<em>Enregistre</em> la vidéo"), None), (kara("et envoie-la au pote"), None), (kara("qui fait des <i>retours</i>."), None), (kara("<em>Code promo Hacoo</em>"), None), (kara("<em>hzklink</em>."), None)]),
]
SPLITS = [(0.2, 2.94), (3.16, 6.02), (6.24, 11.27), (11.49, 17.06), (17.28, 20.02), (20.24, 24.84), (25.06, 31.5)]

CSS = '''
.stamp{position:absolute;padding:6px 26px;border:9px solid #ee3b3b;border-radius:16px;color:#ee3b3b;font:900 70px Inter,'Arial Black',sans-serif;letter-spacing:2px;background:rgba(255,255,255,.85);z-index:5}
.phone{position:absolute;width:330px;height:540px;border:8px solid #141414;border-radius:46px;background:#fff;box-shadow:10px 12px 0 #141414;padding:22px 20px;text-align:center}
.phone .h{font:900 26px Inter,'Arial Black',sans-serif;letter-spacing:2px;background:#ffd84a;border:4px solid #141414;border-radius:10px;padding:4px 0}
.phone .pr{font:900 60px Inter,'Arial Black',sans-serif;margin-top:6px}
.phone .x{font:700 20px Inter,sans-serif;color:#777}
.phone .ok{margin-top:12px;display:inline-block;padding:6px 20px;border-radius:30px;background:#2fa35a;color:#fff;border:4px solid #141414;font:900 34px Inter,'Arial Black',sans-serif}
.tbl{left:150px;top:440px;width:780px;padding:30px 40px 34px}
.tbl .t{font:900 46px Inter,'Arial Black',sans-serif;text-align:center;margin-bottom:14px}
.tbl .r{display:flex;justify-content:space-between;font:800 50px Inter,'Arial Black',sans-serif;padding:12px 26px;border-top:5px solid #141414}
.tbl .r.hd{font-size:30px;letter-spacing:2px;color:#555;border-top:0}
.tbl .r b{font-weight:900}
.cp{left:130px;top:430px;width:820px;padding:34px 44px 36px}
.cp .lab{font:900 34px Inter,'Arial Black',sans-serif;letter-spacing:2px}
.cp .f{margin-top:14px;height:110px;border:6px solid #141414;border-radius:20px;background:#fff;display:flex;align-items:center;padding:0 28px;font:900 66px 'DejaVu Sans Mono',Menlo,monospace}
.cp .ok{margin-top:16px;font:900 46px Inter,'Arial Black',sans-serif;color:#2fa35a}
.cond{position:absolute;left:90px;width:900px;text-align:center;font:700 26px Inter,sans-serif;color:#6b6257}
'''

GRID = ''.join(avatar(90 + 150 * (k % 3), 90 + 150 * (k // 3), s, h, m) for k, (s, h, m) in enumerate([
    ('#f2c59a', '#3b2a20', 'smile'), ('#c98b5e', '#141414', 'flat'), ('#f6d3b3', '#e0a84a', 'sad'),
    ('#8d5a3b', '#141414', 'smile'), ('#f2c59a', '#7a4a2a', 'sad'), ('#e0ac7e', '#2a2a2a', 'flat'),
    ('#f6d3b3', '#c0392b', 'flat'), ('#a8714b', '#141414', 'sad'), ('#f2c59a', '#5a3a22', 'smile')]))
GRID += banned(90, 90, '1.2') + banned(240, 240, '1.2') + banned(390, 90, '1.3') + banned(240, 390, '1.3') + banned(390, 390, '1.3')

BODY = chrome() + '''
  <div class="scene" data-s="0">''' + tag('Retours sur Hacoo') + ban('⚠ Attention', 300, 'red', rot=-3) + ban('Remboursement Hacoo', 430, size=64, rot=1) + stk(330, 600, 420, 420, PADLOCK, vb='0 0 400 400') + '''</div>
  <div class="scene" data-s="1" data-in="pop">''' + tag('Comptes bloqués') + ban('Beaucoup de comptes', 300, size=62, g='1.0', rot=-2) + ban('bloqués', 420, 'red', g='1.2', fx='stamp', rot=2) + stk(300, 560, 480, 480, GRID) + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + tag('Pourquoi ?') + ban('Pourquoi ?', 300, 'yel', rot=-3) + stk(340, 450, 400, 330, tee('#5fb3ff'), g='2.1', fx='up', vb='0 0 400 330') + stk(340, 700, 400, 400, BOX, g='2.0') + '''
   <div class="stamp" style="left:250px;top:760px;transform:rotate(-12deg)" data-g="2.2" data-fx="stamp">REMBOURSÉ</div>
   <div class="ban" style="top:1060px" data-g="2.3" data-fx="pop"><span class="pill" style="background:#ee3b3b;color:#fff;font-size:48px;transform:rotate(3deg);display:inline-block">+ ARTICLE GARDÉ ✗</span></div></div>
  <div class="scene" data-s="3" data-in="right">''' + tag('Mon conseil') + ban('Le bon réflexe', 300, 'grn', rot=-2) + stk(60, 470, 400, 520, GUY + ARROWS_IN, vb='0 0 400 520') + '''
   <div class="ban" style="top:1015px;left:-280px" data-g="3.2" data-fx="pop"><span class="pill" style="background:#ffd84a;font-size:44px">TROP PETIT ?</span></div>
   <div class="phone" style="left:610px;top:470px" data-g="3.3" data-fx="right"><div class="h">SECONDE MAIN</div>''' + icon('Survêt', 0).replace('width="0" height="0"', 'width="230" height="230"').replace('<svg ', '<svg style="display:block;margin:12px auto 0" ') + '''
    <div class="pr">15,00 €</div><div class="x">prix d'exemple</div><div class="ok" data-g="3.4" data-fx="stamp">VENDU ✓</div></div></div>
  <div class="scene" data-s="4" data-in="up">''' + tag('Avant de commander') + '''
   <div class="card tbl"><div class="t">GUIDE DES TAILLES</div><div class="r hd"><span>TAILLE</span><span>TOUR DE POITRINE</span></div>
    <div class="r"><b>S</b><span>88-94 cm</span></div><div class="r"><b>M</b><span>94-100 cm</span></div><div class="r"><b>L</b><span>100-106 cm</span></div><div class="r"><b>XL</b><span>106-112 cm</span></div></div>''' + red_circle(150, 712, 790, 120, '4.2') + stk(315, 1062, 450, 112, TAPE, g='4.1', fx='right', vb='0 40 400 110', wob=False) + '''</div>
  <div class="scene" data-s="5" data-in="pop">''' + tag('Code promo Hacoo') + '''
   <div class="card cp"><div class="lab">CODE PROMO HACOO</div><div class="f"><span data-g="5.2" data-fx="type">hzklink</span></div><div class="ok" data-g="5.3" data-fx="fade">✓ -14 % appliqué</div></div>''' + ban('-14 %', 870, 'yel', g='5.3', fx='stamp', rot=-4, size=150) + '''</div>
  <div class="scene" data-s="6" data-in="pop">''' + tag('Partage') + stk(430, 300, 220, 300, BOOKMARK, g='6.0', vb='0 0 260 320') + ban('Enregistre cette vidéo', 650, size=62, g='6.0', rot=-2) + ban('Envoie-la ↗', 775, 'grn', g='6.1', rot=2, size=60) + ban('au pote qui fait des retours', 900, 'red', g='6.2', size=44, rot=-1) + '''
   <div class="ban" style="top:1025px" data-g="6.3" data-fx="up"><span class="pill" style="background:#ffd84a;font-size:46px">CODE PROMO HACOO : <span class="mono">hzklink</span></span></div>
   <div class="cond" style="top:1470px">-14 % avec le code promo Hacoo hzklink, selon conditions sur l'appli Hacoo · prix d'exemple</div></div>
'''
