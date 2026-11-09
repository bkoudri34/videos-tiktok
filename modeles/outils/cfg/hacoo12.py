import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°1 du 09/11/2026 - style v3 nuit & or, accent bleu nuit, « avant / après le code » : 50,00 € -> 43,00 € (prix d'exemple, -14 % code hzklink)
NAME = 'hacoo12'
TITLE = 'Hacoo avant apres nuit et or'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Même panier, deux prix. Regarde bien.", [("Même panier,", None), ("deux prix.", None), ("Regarde bien.", None)]),
 ("Avant le code : cinquante euros pile.", [("Avant le code :", None), ("50 € pile.", None)]),
 ("Tu tapes le code H Z K link.", [("Tu tapes le code", None), ("hzklink.", None)]),
 ("Après : quarante-trois euros. Sept euros d'économie.", [("Après :", None), ("43 €.", None), ("7 € d'économie.", None)]),
 ("Moins quatorze pour cent sur tout ton panier Hacou.", [("-14 %", None), ("sur tout ton panier", None), ("Hacoo.", None)]),
 ("Les liens des articles tendance ? Dans ma bio.", [("Les liens", None), ("des articles tendance ?", None), ("Dans ma bio.", None)]),
]
SPLITS = [(0.0, 2.572), (3.001, 5.187), (5.617, 8.913), (9.394, 12.388), (12.889, 15.216), (15.601, 17.759)]
GSTART = [[0.1, 1.0, 1.9], [3.0, 4.1], [5.62, 6.7], [9.4, 10.2, 11.5], [12.9, 13.8, 14.8], [15.61, 16.1, 17.2]]
MINLEN = 2.5
GAP = 0.4
TAIL = 2.0
CSS = '''
.mini{position:absolute;top:760px;width:380px;height:520px;border-radius:26px;background:#f4efe4;color:#1c1712;text-align:center;box-shadow:0 30px 70px rgba(0,0,0,.65);padding-top:40px}
.mini .k{font:900 40px Inter;letter-spacing:6px}
.mini .q{font:900 200px 'DejaVu Serif',serif;color:#2b3f6b;line-height:1.5}
.mini .s{font:700 24px Inter;letter-spacing:3px;color:#7a6f60}
.it3{position:absolute;width:120px;height:120px;border-radius:24px;background:#18202f;border:3px solid #4a7bd0;display:flex;align-items:center;justify-content:center}
.badge{position:absolute;left:640px;top:1150px;padding:18px 34px;border-radius:40px;background:#2b3f6b;border:3px solid #8fb3ff;font:900 46px Inter;color:#fff;white-space:nowrap}
'''
BODY = hud('FRANCE · SHOPPING', 'AVANT / APRÈS') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + head(230, [('h1', 'MÊME PANIER,', None), ('it gold', 'deux prix.', None), ('h1 s', 'REGARDE BIEN.', '0.2')]) + '''
   <div class="mini" style="left:110px;transform:rotate(-4deg)"><div class="k">AVANT</div><div class="q">?</div><div class="s">SANS CODE</div></div>
   <div class="mini" style="left:590px;transform:rotate(3deg);background:#1b2233;color:#fff;border:3px solid #d9a24c"><div class="k gold">APRÈS</div><div class="q gold">?</div><div class="s" style="color:#bba98a">AVEC LE CODE</div></div></div>
  <div class="scene" data-s="1" data-in="pop">''' + head(230, [('h1', 'AVANT LE CODE :', '1.0'), ('it gold', '50 € pile.', '1.1')]) + '''
   <div class="rcpt" style="top:600px"><div class="t">MON PANIER</div><div class="s">prix d'exemple</div><hr>
    <div class="row"><span>Doudoune légère</span><span>24,90</span></div><div class="row"><span>Bottines</span><span>17,90</span></div><div class="row"><span>Écharpe</span><span>7,20</span></div><hr>
    <div class="row tot"><span>TOTAL</span><span>50,00 €</span></div><hr><div class="s">SANS CODE PROMO</div></div>
</div>
  <div class="scene" data-s="2" data-in="right">''' + head(230, [('h1 s', 'TU TAPES LE CODE', '2.0'), ('big gold', 'hzklink', '2.1')]).replace('class="big gold"', 'class="big gold" style="font-size:120px"') + '''
   <div class="orb" style="left:200px;top:620px;width:680px;height:960px"></div>
   <div class="phone" style="top:700px;height:780px" data-g="2.0" data-fx="up"><div class="notch"></div>
    <div style="font:900 48px Inter;margin-top:40px">Paiement</div><div style="font:600 24px Inter;color:#aaa;margin-top:6px">3 articles · prix d'exemple</div>
    <div style="margin:40px 26px 0;text-align:left;font:600 30px Inter;color:#ddd">Sous-total<span style="float:right">50,00 €</span></div>
    <div style="margin:30px 26px 0;border:3px solid #8fb3ff;border-radius:18px;height:90px;display:flex;align-items:center;padding:0 20px;gap:14px;font:600 24px Inter;color:#999;white-space:nowrap">Code promo <span data-g="2.1" data-fx="type" style="font:900 42px Inter;color:#f3c766">hzklink</span></div>
    <div style="display:inline-block;margin-top:34px;background:#e0ac55;color:#1a1408;font:800 32px Inter;padding:14px 40px;border-radius:30px" data-g="2.1" data-fx="pop">Appliquer</div></div></div>
  <div class="scene" data-s="3" data-in="pop"><div class="rays" style="top:520px"></div>''' + head(230, [('h1', 'APRÈS :', '3.0')]) + '''
   <div class="abs" style="left:90px;top:380px;width:900px;text-align:center;font:900 70px 'DejaVu Serif',serif;color:#8f877a" data-g="3.0" data-fx="fade">50,00 €</div>
   <div class="abs" style="left:385px;top:425px;width:310px;height:10px;background:#e5322d;border-radius:5px;transform-origin:0 50%" data-g="3.1" data-fx="strike"></div>
   <div class="abs" style="left:90px;top:560px;width:900px;text-align:center" data-g="3.1" data-fx="stamp" data-slow="3.1"><div class="gold" style="font:900 150px 'DejaVu Serif',serif;line-height:1.3">43,00 €</div><div style="font:700 28px Inter;letter-spacing:5px;color:#bba98a">AVEC HZKLINK · PRIX D'EXEMPLE</div></div>
   <div class="badge" style="left:330px;top:1000px" data-g="3.2" data-fx="pop">− 7 € d'économie</div></div>
  <div class="scene" data-s="4" data-in="left"><div class="floor"></div><div class="rays"></div><div class="emb" data-g="4.0" data-fx="pop"><span class="gold" style="font:900 82px 'DejaVu Serif',serif">-14%</span></div>
   ''' + head(720, [('big gold', '-14 %', '4.0'), ('h1 s', 'SUR TOUT TON PANIER', '4.1'), ('it gold', 'Hacoo.', '4.2')]).replace('class="big gold"', 'class="big gold" style="font-size:160px"') + '''</div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', 'LES LIENS', '5.0'), ('it gold', 'des articles tendance', '5.1'), ('h1', 'DANS MA BIO', '5.2')]).replace('class="it gold"', 'class="it gold" style="font-size:64px"') + '''
   <div class="pill" style="top:620px" data-g="5.1" data-fx="up"><div class="pin">%</div><div><b>-14 % AVEC HZKLINK</b><span>sur ton panier Hacoo</span></div></div>
   <div class="search" style="top:770px" data-g="5.1" data-fx="fade"><svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg><span data-g="5.1" data-fx="type">hzklink</span></div>
   <div class="pill" style="top:910px" data-g="5.2" data-fx="up"><div class="pin">★</div><div><b>ARTICLES TENDANCE</b><span>tous les liens sont en bio</span></div></div>
   <div class="cond" style="top:1070px">Prix d'exemple · -14 % avec le code hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
