import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parraine import *
# Hello bank, 27/11/2026 (vidéo A) - style v3 nuit & or, accent corail. Format F18 « Parraine à ton tour » (règles de Badr du 26/11) :
# mascotte ronde à lunettes dorées sous une guirlande d'ampoules -> 1 invitation en privé (enveloppe) -> 2 tu ouvres ton compte (checklist)
# -> 3 une fois client, ton propre lien / QR code dans l'appli (téléphone dessiné, sans logo) -> 4 tu le partages à tes amis
# (un seul niveau, tampon « plafond fixé par la banque », ralenti) -> « je ne touche rien sur les amis de mes filleuls » -> appel discret.
# AUCUN montant écrit : montants à l'oral seulement.
# Source (hellobank.fr/fr/votre-offre-parrainage, consultée le 27/11/2026) : parrain 150 € par parrainage validé, 20 parrainages validés
# par année civile ; filleul jusqu'à 330 € d'avantages (80 € + 50 € le 13e mois avec Hello Prime et 5 paiements/retraits par mois,
# bon d'achat 200 € avec Hello Start+) ; invitation avant le 30/11/2026 à 15 h. Pas de total : l'offre finit avant 12 mois.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08, une synthèse par réplique, atempo 1.15, -19 dB moyen ;
# réplique 1 refaite (« et si, après, c'était toi » mal compris), répliques 2, 4, 5 raccourcies (durée).
NAME = 'hellobank17'
TITLE = 'Hello bank parraine a ton tour corail'
ROOT = ':root{--bg:#0b0605;--ac:#ff8f6b}'
LINES = [
 ("Parrainage Hello bank : et si le prochain parrain, c'était toi ?", [("Parrainage Hello bank :", None), ("et si le prochain parrain,", None), ("c'était toi ?", None)]),
 ("Un : je te parraine, je t'envoie l'invitation en privé.", [("1 : je te parraine,", None), ("je t'envoie l'invitation", None), ("en privé.", None)]),
 ("Deux : tu ouvres ton compte. Jusqu'à trois cent trente euros d'avantages, si tu remplis les conditions.", [("2 : tu ouvres ton compte.", None), ("Jusqu'à … d'avantages,", None), ("si tu remplis les conditions.", None)]),
 ("Trois : une fois client, ton propre lien d'invitation est dans ton appli.", [("3 : une fois client,", None), ("ton propre lien d'invitation", None), ("est dans ton appli.", None)]),
 ("Quatre : tu partages ton lien à tes amis. Jusqu'à cent cinquante euros par ami validé, vingt par an au maximum, fixé par la banque.", [("4 : tu partages ton lien", None), ("à tes amis.", None), ("Une prime par ami validé,", None), ("20 par an au maximum,", None), ("fixé par la banque.", None)]),
 ("Un seul niveau : je ne touche rien sur les amis de mes filleuls.", [("Un seul niveau :", None), ("je ne touche rien", None), ("sur les amis de mes filleuls.", None)]),
 ("Si tu veux que je te parraine, écris-moi en privé.", [("Si tu veux", None), ("que je te parraine,", None), ("écris-moi en privé.", None)]),
]
SPLITS = [(0.2, 2.392), (2.842, 5.21), (5.66, 9.61), (10.06, 12.995), (13.445, 18.952), (19.402, 21.69), (22.14, 23.878)]
MINLEN = 1.6
GAP = 0.3
TAIL = 1.9

CSS = PCSS + '''
.co{color:#ff8f6b;text-shadow:0 0 18px rgba(255,120,90,.5)}
.bulbs{position:absolute;left:40px;width:1000px;height:120px}
.bulb{position:absolute;width:22px;height:30px;border-radius:50% 50% 45% 45%;background:#ffd79a;box-shadow:0 0 22px 8px rgba(255,190,110,.45)}
.env{position:absolute;width:300px;height:200px;border-radius:18px;background:#f4ede0;box-shadow:0 26px 60px rgba(0,0,0,.6);overflow:hidden}
.env:before{content:'';position:absolute;left:0;top:0;border-left:150px solid transparent;border-right:150px solid transparent;border-top:110px solid #e3d6bf}
.env b{position:absolute;left:0;right:0;bottom:22px;text-align:center;font:900 26px Inter;color:#b4532f;letter-spacing:2px}
.phone{position:absolute;width:360px;height:640px;border-radius:52px;background:#141012;border:6px solid #3a2a24;box-shadow:0 30px 80px rgba(0,0,0,.7)}
.phone .scr{position:absolute;left:22px;top:60px;right:22px;bottom:40px;border-radius:30px;background:linear-gradient(180deg,#1f1715,#120c0b);text-align:center;color:#f3efe6}
.phone .scr .t{font:900 30px Inter;color:#ff8f6b;margin-top:34px;letter-spacing:1px}
.qr{width:200px;height:200px;margin:36px auto 0;border-radius:16px;background:#f4ede0;padding:16px;box-sizing:border-box;display:grid;grid-template-columns:repeat(7,1fr);gap:4px}
.qr i{background:#151010;border-radius:3px}.qr i.o{background:transparent}
.phone .btn{margin:40px auto 0;width:240px;padding:18px 0;border-radius:40px;background:#ff8f6b;color:#141010;font:900 28px Inter}
.share{position:absolute;font:900 64px Inter;color:#ff8f6b;text-shadow:0 0 20px rgba(255,120,90,.6)}
'''
def bulbs(top):
    return f'<div class="bulbs" style="top:{top}px"><svg class="abs" width="1000" height="120"><path d="M0 20 Q250 110 500 40 Q750 -20 1000 60" stroke="#6b5a48" stroke-width="3" fill="none"/></svg>' + \
    ''.join(f'<div class="bulb" style="left:{x}px;top:{y}px"></div>' for x, y in [(60, 40), (190, 74), (330, 86), (470, 50), (610, 26), (750, 22), (890, 44)]) + '</div>'

QR = '<div class="qr">' + ''.join('<i class="o"></i>' if c == '0' else '<i></i>' for c in '1110111101010110111011000101101011100111011010111') + '</div>'
ME = '#ff8f6b'

BODY = hud('FRANCE · PARRAINE À TON TOUR', 'HELLO BANK') + BANNER + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + bulbs(560) + hdx(220, [('h1 co', 'PARRAINAGE HELLO BANK', None, 'font-size:66px'), ('it gold', 'et si le prochain parrain,', None, 'font-size:64px'), ('it gold', "c'était toi ?", None, 'font-size:74px')]) + mascot(330, 700, 400, ME, 'glasses') + '''
   <div class="bubble2" style="left:150px;top:690px;transform:rotate(-6deg)">moi ?</div></div>
  <div class="scene" data-s="1" data-in="right"><div class="floor"></div>''' + '<div class="num" style="left:110px;top:230px" data-g="1.0" data-fx="stamp">1</div>' + hdx(250, [('h1', 'JE TE PARRAINE', '1.0', 'font-size:66px'), ('it co', 'en privé.', '1.2', 'font-size:72px')], left=290, width=640) + mascot(90, 820, 300, ME, 'glasses') + friend(700, 870, 210, '#f3c766', g='1.2') + '''
   <div class="env" style="left:390px;top:620px" data-g="1.1" data-fx="right"><b>INVITATION</b></div></div>
  <div class="scene" data-s="2" data-in="up">''' + '<div class="num" style="left:465px;top:230px" data-g="2.0" data-fx="stamp">2</div>' + hdx(410, [('h1', 'TU OUVRES TON COMPTE', '2.0', 'font-size:62px')]) + '''
   <div class="card2" style="left:130px;top:600px;width:780px" data-g="2.1" data-fx="up"><div class="t">Avantages de bienvenue</div>
    <div class="chk"><i>✓</i>ouverture avec l'invitation</div><div class="chk"><i>✓</i>offre groupée souscrite</div><div class="chk" data-g="2.2" data-fx="fade"><i>✓</i>conditions de l'offre remplies</div></div>
   <div class="tagp" style="left:250px;top:1080px" data-g="2.2" data-fx="pop">si tu remplis les conditions</div>
   ''' + friend(430, 1180, 180, '#f3c766', g='2.2') + '''</div>
  <div class="scene" data-s="3" data-in="pop"><div class="floor"></div>''' + '<div class="num" style="left:110px;top:230px" data-g="3.0" data-fx="stamp">3</div>' + hdx(250, [('h1', 'UNE FOIS CLIENT,', '3.0', 'font-size:62px'), ('it co', 'ton propre lien.', '3.1', 'font-size:68px')], left=290, width=640) + '''
   <div class="phone" style="left:340px;top:560px" data-g="3.1" data-fx="up"><div class="scr"><div class="t">MON PARRAINAGE</div>''' + QR + '''<div class="btn" data-g="3.2" data-fx="stamp">Partager le lien</div></div></div>
   ''' + friend(110, 900, 200, '#f3c766') + '''</div>
  <div class="scene" data-s="4" data-in="right">''' + '<div class="num" style="left:465px;top:230px" data-g="4.0" data-fx="stamp">4</div>' + hdx(410, [('h1', 'TU LE PARTAGES', '4.0', 'font-size:62px'), ('it co', 'à tes amis.', '4.1', 'font-size:66px')]) + \
    link(540, 780, 240, 1000, '4.1') + link(540, 780, 440, 1060, '4.1') + link(540, 780, 640, 1060, '4.1') + link(540, 780, 840, 1000, '4.1') + \
    friend(430, 610, 220, '#f3c766') + friend(160, 960, 160, ME, g='4.1') + friend(360, 1010, 160, ME, g='4.2') + friend(560, 1010, 160, ME, g='4.2') + friend(760, 960, 160, ME, g='4.3') + '''
   <div class="tagp" style="left:200px;top:1220px" data-g="4.4" data-fx="stamp" data-slow="4.4">plafond fixé par la banque</div>
   <div class="cond" style="top:1310px;color:#e6cfc6" data-g="4.2" data-fx="fade">une prime pour chaque ami validé</div></div>
  <div class="scene" data-s="5" data-in="up">''' + hdx(230, [('h1 co', 'UN SEUL NIVEAU', '5.0', 'font-size:72px'), ('it gold', 'je ne touche rien sur', '5.1', 'font-size:60px'), ('it gold', 'les amis de mes filleuls.', '5.2', 'font-size:60px')]) + \
    mascot(150, 640, 230, ME, 'glasses') + link(380, 760, 520, 760) + friend(520, 680, 170, '#f3c766') + link(690, 765, 800, 900, '5.2') + friend(760, 900, 130, '#9a8fae', g='5.2', cls='grey') + friend(560, 960, 130, '#9a8fae', g='5.2', cls='grey') + link(640, 850, 620, 960, '5.2') + '''
   <div class="x" style="left:790px;top:880px" data-g="5.2" data-fx="stamp">✕</div><div class="x" style="left:590px;top:940px" data-g="5.2" data-fx="stamp">✕</div>
   <div class="cond" style="top:1180px;color:#e6cfc6" data-g="5.1" data-fx="fade">toi → tes amis, c'est tout</div></div>
  <div class="scene" data-s="6" data-in="pop"><div class="floor"></div>''' + bulbs(300) + hdx(440, [('h1', 'SI TU VEUX QUE', '6.0', 'font-size:64px'), ('h1', 'JE TE PARRAINE,', '6.1', 'font-size:64px'), ('it gold', 'écris-moi en privé.', '6.2', 'font-size:70px')]) + mascot(400, 760, 260, ME, 'glasses', g='6.2') + '''
   <div class="tagp" style="left:230px;top:1060px" data-g="6.2" data-fx="pop">Invitation avant le 30/11, 15 h</div>
   <div class="cond" style="top:1160px;font-size:24px">Offres soumises aux conditions en vigueur · nouveaux clients,<br>offre groupée souscrite, compte et carte gardés 1 an</div></div>
'''
