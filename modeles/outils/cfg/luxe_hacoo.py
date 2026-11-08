import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
NAME = 'luxe_hacoo'
TITLE = 'Hacoo nuit et or'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Marre de payer le prix fort sur Hacoo ?!", [("Marre de payer", None), ("le prix fort", None), ("sur Hacoo ?!", None)]),
 ("Le seul truc qui gonfle... c'est ton panier.", [("Le seul truc qui gonfle…", None), ("c'est ton panier.", None)]),
 ("Et si on te disait qu'il y a un code ?", [("Et si on te disait", None), ("qu'il y a un code ?", None)]),
 ("H Z K link. Moins 14 % sur ton panier.", [("hzklink.", "H Z K link"), ("-14 %", "moins quatorze pour cent"), ("sur ton panier.", None)]),
 ("Sweat, sac, bonnet... les articles tendance sont en bio.", [("Sweat,", None), ("sac,", None), ("bonnet…", None), ("les articles tendance", None), ("sont en bio.", None)]),
 ("Pas 44 euros... 37 euros 84.", [("Pas 44 €…", "pas quarante-quatre euros"), ("37,84 €.", "trente-sept euros quatre-vingt-quatre")]),
 ("Code H Z K link, liens en bio. Fais-toi plaisir, sans te ruiner !", [("Code hzklink,", "code H Z K link"), ("liens en bio.", None), ("Fais-toi plaisir,", None), ("sans te ruiner !", None)]),
]
SPLITS = [(0.0, 1.72), (1.98, 4.40), (4.67, 6.05), (6.21, 10.05), (10.32, 14.18), (14.64, 17.20), (17.55, 22.98)]
CSS = '''
.prod{position:absolute;width:250px;height:250px;border-radius:50%;border:4px solid #d9a24c;box-shadow:0 0 30px rgba(240,180,80,.35);overflow:hidden;display:flex;align-items:center;justify-content:center}
.prod span{position:absolute;bottom:22px;left:0;right:0;text-align:center;font:800 24px Inter;color:#fff;text-shadow:0 2px 6px #000}
'''
STRIP = 'TOTAL    44,00\n-----------\n SWEAT  17,90\n SAC    12,50\n BONNET  6,40\n CHAUSS. 7,20\n***********\nMERCI !\n\nTOTAL    44,00\n-----------\n SWEAT  17,90\n SAC    12,50'
ticks = ''.join(f'<div class="tk" style="transform:rotate({i*6}deg);{"height:40px" if i%5==0 else "opacity:.6"}"></div>' for i in range(60))
ICONS = {
 'Sweat': ('linear-gradient(135deg,#6f86c9,#2e3f78)', '<path d="M40 50 L70 30 Q100 45 130 30 L160 50 L175 110 L150 115 L148 170 L52 170 L50 115 L25 110 Z" fill="#dfe6ff"/><path d="M85 34 Q100 60 115 34" fill="none" stroke="#9aa8d6" stroke-width="6"/>'),
 'Sac': ('linear-gradient(135deg,#d99a6c,#7a3f22)', '<path d="M60 75 Q100 20 140 75" fill="none" stroke="#fbe3cc" stroke-width="9"/><rect x="45" y="75" width="110" height="85" rx="18" fill="#fbe3cc"/><rect x="88" y="100" width="24" height="14" rx="4" fill="#d99a6c"/>'),
 'Bonnet': ('linear-gradient(135deg,#a7c97a,#3e6a2a)', '<circle cx="100" cy="42" r="16" fill="#f3f7e8"/><path d="M45 130 Q45 55 100 55 Q155 55 155 130 Z" fill="#f3f7e8"/><rect x="40" y="125" width="120" height="32" rx="10" fill="#dfe8c8"/>'),
 'Chaussettes': ('linear-gradient(135deg,#e9c95a,#8a6a12)', '<path d="M70 35 h40 v80 q0 40 -40 40 h-25 q-15 0 -15 -15 q0 -15 15 -15 h25 z" fill="#fff8e0"/><rect x="70" y="35" width="40" height="18" fill="#e9c95a"/>'),
 'Casquette': ('linear-gradient(135deg,#c97aa8,#5a2346)', '<path d="M45 115 Q50 55 105 55 Q155 58 158 115 Z" fill="#fde6f2"/><path d="M150 112 Q185 112 190 125 L120 125 Z" fill="#f2c3dc"/>'),
 'Lunettes': ('linear-gradient(135deg,#7ac9c4,#1f5a57)', '<circle cx="68" cy="100" r="28" fill="#123" stroke="#e6fffd" stroke-width="7"/><circle cx="132" cy="100" r="28" fill="#123" stroke="#e6fffd" stroke-width="7"/><path d="M96 98 Q100 90 104 98" stroke="#e6fffd" stroke-width="6" fill="none"/>'),
}
def prod(name, x, y, g):
    bg, svg = ICONS[name]
    return f'<div class="prod" style="left:{x}px;top:{y}px;background:{bg}" data-g="{g}" data-fx="pop"><svg width="200" height="200" viewBox="0 0 200 200" style="margin-top:-30px">{svg}</svg><span>{name}</span></div>'
BODY = hud('FRANCE · SHOPPING', 'CODE PROMO') + '''
''' + counter_scene(0, 'Boutique Plein Pot', 'PRIX FORT GARANTI', '44,00', 'Ça fera 44 €,<br>s\'il vous plaît.', '0.1', '0.1', STRIP).replace('class="sign gold"', 'class="sign gold" style="top:720px"').replace('style="left:420px;top:880px"', 'style="left:440px;top:900px"') + '''
  ''' + head(230, [('h1', 'MARRE DE PAYER', None), ('big gold', '44 €', None), ('it gold', 'plein pot sur Hacoo ?!', '0.2')]).replace('class="hd"', 'class="hd scene" data-s="0"') + '''
  <div class="scene" data-s="1" data-in="pop">''' + head(230, [('h1', 'LE SEUL TRUC', '1.0'), ('h1', 'QUI GONFLE…', '1.0'), ('it gold', "c'est ton panier.", '1.1')]) + '''
   <div class="rcpt" style="top:700px"><div class="t">COMMANDE HACOO</div><div class="s">prix d'exemple</div><hr>
    <div class="row"><span>Sweat oversize</span><span>17,90</span></div><div class="row"><span>Sac bandoulière</span><span>12,50</span></div><div class="row"><span>Bonnet côtelé</span><span>6,40</span></div><div class="row"><span>Chaussettes x5</span><span>7,20</span></div><hr>
    <div class="row tot"><span>TOTAL</span><span>44,00 €</span><svg class="abs" style="left:-30px;top:-26px" width="560" height="110" viewBox="0 0 560 110"><path d="M30 55 C30 10 530 5 535 50 C540 100 40 105 20 60" fill="none" stroke="#e5322d" stroke-width="6" pathLength="1" stroke-dasharray="1" data-g="1.1" data-fx="draw"/></svg></div><hr>
    <div class="s">MERCI POUR<br>VOTRE GÉNÉROSITÉ :)</div></div></div>
  <div class="scene" data-s="2" data-in="pop">''' + head(230, [('h1 s', 'ET SI ON TE DISAIT…', '2.0'), ('it gold', "qu'il y a un code ?", '2.1')]) + '''
   <div class="orb" style="left:200px;top:560px;width:680px;height:1020px"></div><div class="orb" style="left:260px;top:620px;width:560px;height:900px;opacity:.6"></div>
   <div class="phone" data-g="2.0" data-fx="up"><div class="notch"></div>
    <div style="font:900 52px Inter;margin-top:34px">Mon panier</div><div style="font:600 24px Inter;color:#aaa;margin-top:6px">4 articles · prix d'exemple</div>
    <div style="margin:26px 26px 0;text-align:left;font:600 28px Inter;line-height:2.1;color:#ddd">Sweat oversize<span style="float:right">17,90 €</span><br>Sac bandoulière<span style="float:right">12,50 €</span><br>Bonnet côtelé<span style="float:right">6,40 €</span><br>Chaussettes x5<span style="float:right">7,20 €</span></div>
    <div style="margin:24px 26px 0;border:3px solid #e0ac55;border-radius:18px;height:84px;display:flex;align-items:center;padding:0 20px;gap:14px;font:600 24px Inter;color:#999;white-space:nowrap">Code promo <span data-g="2.1" data-fx="type" style="font:900 40px Inter;color:#f3c766">hzklink</span></div>
    <div style="display:inline-block;margin-top:26px;background:#e0ac55;color:#1a1408;font:800 32px Inter;padding:14px 40px;border-radius:30px" data-g="2.1" data-fx="pop">Appliquer</div></div>
   <div class="spark" style="left:170px;top:900px" data-g="2.1" data-fx="pop">✦</div><div class="spark" style="left:860px;top:760px" data-g="2.1" data-fx="pop">✦</div><div class="spark" style="left:830px;top:1320px" data-g="2.1" data-fx="pop">✦</div></div>
  <div class="scene" data-s="3" data-in="pop"><div class="floor"></div><div class="rays"></div><div class="emb" data-g="3.0" data-fx="pop"><span class="gold" style="font:900 78px 'DejaVu Serif',serif">-14%</span></div>
   ''' + head(720, [('h1', 'CODE HZKLINK', '3.0'), ('big gold', "-14 %", '3.1'), ('h1 s', "SUR TON PANIER", '3.2')]).replace('class="big gold"', 'class="big gold" style="font-size:180px"') + '''</div>
  <div class="scene" data-s="4" data-in="pop">''' + head(230, [('h1 s', 'LES ARTICLES TENDANCE…', '4.3'), ('it gold', 'sont en bio.', '4.4')]) + '''
   ''' + prod('Sweat', 110, 620, '4.0') + prod('Sac', 415, 620, '4.1') + prod('Bonnet', 720, 620, '4.2') + prod('Chaussettes', 110, 920, '4.3') + prod('Casquette', 415, 920, '4.3') + prod('Lunettes', 720, 920, '4.3') + '''
   <div class="spark" style="left:380px;top:880px" data-g="4.3" data-fx="pop">✦</div><div class="spark" style="left:690px;top:600px" data-g="4.2" data-fx="pop">✦</div><div class="spark" style="left:660px;top:1180px" data-g="4.4" data-fx="pop">✦</div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="floor"></div>''' + head(230, [('h1', 'PAS 44 €', '5.0')]).replace('class="h1"', 'class="h1" style="font-size:110px;position:relative"') + '''
   <div class="abs" style="left:300px;top:300px;width:480px;height:12px;background:#e5322d;border-radius:6px;transform-origin:0 50%" data-g="5.1" data-fx="strike"></div>
   <div class="dial">''' + ticks + '''<div class="nd" data-g="5.0" data-fx="sweep"></div>
    <div class="abs" style="left:0;width:600px;top:160px;text-align:center" data-g="5.1" data-fx="stamp" data-slow="5.1"><div style="font:800 36px Inter;letter-spacing:4px">AVEC LE CODE</div><div class="gold" style="font:900 96px 'DejaVu Serif',serif;line-height:1.4">37,84 €</div><div style="font:700 28px Inter;letter-spacing:5px;color:#bba98a">PRIX D'EXEMPLE</div></div></div></div>
  <div class="scene" data-s="6" data-in="pop">''' + head(230, [('h1', 'LE CODE', '6.0'), ('big gold', 'hzklink', '6.0'), ('it gold', 'liens en bio.', '6.1')]).replace('class="big gold"', 'class="big gold" style="font-size:150px"') + '''
   <div class="pill" style="top:720px" data-g="6.0" data-fx="up"><div class="pin">%</div><div><b>-14 % AVEC HZKLINK</b><span>sur ton panier Hacoo</span></div></div>
   <div class="pill" style="top:845px" data-g="6.1" data-fx="up"><div class="pin">★</div><div><b>ARTICLES TENDANCE</b><span>tous les liens sont en bio</span></div></div>
   <div class="search" style="top:980px" data-g="6.1" data-fx="fade"><svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg><span data-g="6.1" data-fx="type">hzklink</span></div>
   ''' + head(1120, [('h1', 'FAIS-TOI PLAISIR !', '6.2'), ('it gold', 'sans te ruiner.', '6.3')]) + '''
   <div class="cond" style="top:1420px">Prix d'exemple · -14 % avec le code hzklink<br>selon conditions sur l'appli Hacoo</div></div>
'''
GSTART = [[0.1, 0.7, 1.2], [2.0, 3.7], [4.7, 5.2], [6.2, 8.4, 9.3], [10.4, 11.1, 11.6, 12.3, 13.5], [14.6, 15.8], [17.5, 20.4, 21.3, 22.3]]
