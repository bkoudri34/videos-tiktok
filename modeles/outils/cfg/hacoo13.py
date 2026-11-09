import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# Hacoo n°2 du 09/11/2026 - style v3 nuit & or, accent rouge, « 3 trucs tendance à moins de 25 € » : gants 6,90 + bonnet 5,50 + plaid 11,90 = 24,30 € -> 20,90 € avec hzklink (prix d'exemple)
NAME = 'hacoo13'
TITLE = 'Hacoo 3 trucs tendance nuit et or'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Trois trucs tendance, moins de vingt-cinq euros.", [("Trois trucs tendance,", None), ("moins de 25 €.", None)]),
 ("Des gants tactiles, six euros quatre-vingt-dix.", [("Des gants tactiles,", None), ("6,90 €.", None)]),
 ("Un bonnet à pompon, cinq euros cinquante.", [("Un bonnet à pompon,", None), ("5,50 €.", None)]),
 ("Et un plaid tout doux, onze euros quatre-vingt-dix.", [("Et un plaid tout doux,", None), ("11,90 €.", None)]),
 ("Avec H Z K link, ça fait vingt euros quatre-vingt-dix.", [("Avec hzklink,", None), ("ça fait", None), ("20,90 €.", None)]),
 ("Liens en bio, et moins quatorze pour cent avec le code.", [("Liens en bio,", None), ("et -14 %", None), ("avec le code.", None)]),
]
SPLITS = [(0.0, 1.80), (2.19, 4.218), (4.612, 6.603), (7.032, 9.144), (9.570, 12.156), (12.584, 15.034)]
GSTART = [[0.1, 1.0], [2.2, 3.2], [4.62, 5.7], [7.04, 8.1], [9.58, 10.9, 11.1], [12.6, 13.6, 14.4]]
MINLEN = 2.4
GAP = 0.4
TAIL = 2.0
CSS = '''
.disc{position:absolute;width:250px;height:250px;border-radius:50%;border:4px solid #d9a24c;background:radial-gradient(circle,#2a1414,#120909 70%);box-shadow:0 0 30px rgba(224,72,72,.35);display:flex;align-items:center;justify-content:center}
.disc span{position:absolute;bottom:-50px;left:-40px;right:-40px;text-align:center;font:800 26px Inter;letter-spacing:2px;color:#e9e4da}
.prodbig{position:absolute;left:290px;top:640px;width:500px;height:500px;border-radius:50%;border:6px solid #d9a24c;background:radial-gradient(circle,#3a1717,#120909 70%);box-shadow:0 0 60px rgba(224,72,72,.4);display:flex;align-items:center;justify-content:center}
.ptag{position:absolute;left:560px;top:1060px;padding:20px 40px;border-radius:20px;background:#f4efe4;color:#b0302a;font:900 80px 'DejaVu Serif',serif;transform:rotate(-6deg);box-shadow:0 20px 50px rgba(0,0,0,.6);white-space:nowrap}
.ptag:before{content:'';position:absolute;left:-18px;top:50%;margin-top:-14px;width:28px;height:28px;border-radius:50%;background:#0b0907;border:4px solid #d9a24c}
.note{position:absolute;left:150px;top:1250px;width:780px;text-align:center;font:700 26px Inter;letter-spacing:4px;color:#bba98a}
'''
def disc(name, x, y, g):
    return f'<div class="disc" style="left:{x}px;top:{y}px" data-g="{g}" data-fx="pop">{icon(name, 190)}<span>{name.upper()}</span></div>'

def prodscene(sid, inn, title, name, price, floor=False):
    fl = '<div class="floor"></div>' if floor else ''
    return f'''  <div class="scene" data-s="{sid}" data-in="{inn}">{fl}''' + head(230, [('h1 s', title, f'{sid}.0'), ('it gold', 'prix d\'exemple', f'{sid}.1')]).replace('class="it gold"', 'class="it gold" style="font-size:56px"') + f'''
   <div class="prodbig" data-g="{sid}.0" data-fx="pop">{icon(name, 380)}</div>
   <div class="ptag" data-g="{sid}.1" data-fx="stamp">{price}</div></div>'''

BODY = hud('FRANCE · TENDANCES', 'PETITS PRIX') + '''
  <div class="scene" data-s="0"><div class="rays" style="top:700px"></div>''' + head(230, [('h1 s', '3 TRUCS TENDANCE', None), ('big gold', '- de 25 €', None), ('it gold', "prix d'exemple", '0.1')]).replace('class="big gold"', 'class="big gold" style="font-size:150px"').replace('class="it gold"', 'class="it gold" style="font-size:52px"') + '''
   ''' + disc('Gants', 110, 820, '0.0').replace('data-g="0.0" data-fx="pop"', '') + disc('Bonnet', 415, 1000, '0.0').replace('data-g="0.0" data-fx="pop"', '') + disc('Plaid', 720, 820, '0.0').replace('data-g="0.0" data-fx="pop"', '') + '''</div>
''' + prodscene(1, 'pop', 'GANTS TACTILES', 'Gants', '6,90 €') + '''
''' + prodscene(2, 'right', 'BONNET À POMPON', 'Bonnet', '5,50 €', True) + '''
''' + prodscene(3, 'left', 'PLAID TOUT DOUX', 'Plaid', '11,90 €') + '''
  <div class="scene" data-s="4" data-in="pop"><div class="floor"></div>''' + head(230, [('h1', 'AVEC HZKLINK,', '4.0'), ('it gold', 'ça fait', '4.1')]) + '''
   <div class="rcpt" style="top:560px;left:200px;width:680px"><div class="t">MON PANIER</div><div class="s">prix d'exemple</div><hr>
    <div class="row"><span>Gants tactiles</span><span>6,90</span></div><div class="row"><span>Bonnet à pompon</span><span>5,50</span></div><div class="row"><span>Plaid tout doux</span><span>11,90</span></div><hr>
    <div class="row"><span>Sous-total</span><span>24,30</span></div><div class="row" style="color:#b0302a"><span>Code hzklink -14 %</span><span>-3,40</span></div><hr>
    <div class="row tot" data-g="4.2" data-fx="stamp" data-slow="4.2"><span>TOTAL</span><span style="color:#b0302a;font-size:52px">20,90 €</span></div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', 'LIENS EN BIO,', '5.0'), ('big gold', '-14 %', '5.1'), ('it gold', 'avec le code.', '5.2')]).replace('class="big gold"', 'class="big gold" style="font-size:150px"') + '''
   <div class="search" style="top:760px" data-g="5.2" data-fx="fade"><svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg><span data-g="5.2" data-fx="type">hzklink</span></div>
   <div class="pill" style="top:900px" data-g="5.0" data-fx="up"><div class="pin">★</div><div><b>LIENS EN BIO</b><span>gants · bonnet · plaid</span></div></div>
   <div class="cond" style="top:1060px">Prix d'exemple · -14 % avec le code hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
