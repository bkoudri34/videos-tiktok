import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parraine import *
# Hello bank, 28/11/2026 (vidéo C, 21:00) - style v3 nuit & or, accent bleu saphir. Format F7 « tuto écran 1-2-3 » (pas de mascotte) :
# bureau de nuit (lampe dorée, plateau), grand téléphone dessiné sans logo au centre -> 1 tu reçois mon invitation (lien ou QR code)
# -> 2 tu ouvres ton compte avec l'invitation avant le 30/11 à 15 h -> offre groupée (Hello Prime) -> 3 tu remplis les conditions
# (5 paiements ou retraits par mois avec la carte) -> avantages de bienvenue « si tu remplis les conditions » (ralenti) -> appel discret.
# Règles de Badr du 26/11 : AUCUN montant écrit (montant à l'oral seulement, « jusqu'à », « si tu remplis les conditions »),
# bandeau de mentions pendant toute la vidéo, pas de fausse preuve de gain.
# Source (hellobank.fr/fr/votre-offre-parrainage, consultée le 28/11/2026) : filleul jusqu'à 330 € d'avantages avec souscription
# simultanée à une offre groupée (Hello Prime : 80 € à l'ouverture + 50 € le 13e mois avec au moins 5 paiements ou retraits par mois
# avec la carte sur les 12 premiers mois ; bon d'achat 200 € pour une mobilité bancaire avec Hello Start+) ; invitation envoyée depuis
# l'appli du parrain (lien ou QR code) avant le 30/11/2026 à 15 h. Parrain 150 € par parrainage validé, 20 par an : pas de total
# (offre qui finit avant 12 mois).
# Voix : Speko (voix par défaut, speechify simba-3.5), speed 1.08, une synthèse par réplique, atempo 1.15, -19 dB moyen,
# silences internes plafonnés à 0,2 s.
NAME = 'hellobank18'
TITLE = 'Hello bank tuto 1-2-3 saphir'
ROOT = ':root{--bg:#04060c;--ac:#6fa8ff}'
LINES = [
 ("Parrainage Hello bank : voici la marche à suivre, en trois étapes.", [("Parrainage Hello bank :", None), ("voici la marche à suivre,", None), ("en trois étapes.", None)]),
 ("Un : tu reçois mon invitation, par lien ou par QR code.", [("1 : tu reçois mon invitation,", None), ("par lien", None), ("ou par QR code.", None)]),
 ("Deux : tu ouvres ton compte avec cette invitation, avant le trente novembre à quinze heures.", [("2 : tu ouvres ton compte", None), ("avec cette invitation,", None), ("avant le 30 novembre à 15 h.", None)]),
 ("Tu choisis une offre groupée, comme Hello Prime.", [("Tu choisis une offre groupée,", None), ("comme Hello Prime.", None)]),
 ("Trois : tu remplis les conditions. Par exemple, cinq paiements ou retraits par mois avec ta carte.", [("3 : tu remplis les conditions.", None), ("Par exemple, 5 paiements ou retraits", None), ("par mois avec ta carte.", None)]),
 ("Jusqu'à trois cent trente euros d'avantages, si tu remplis les conditions.", [("Jusqu'à … d'avantages,", None), ("si tu remplis les conditions.", None)]),
 ("Si tu veux que je te parraine, écris-moi en privé.", [("Si tu veux", None), ("que je te parraine,", None), ("écris-moi en privé.", None)]),
]
SPLITS = [(0.2, 3.147), (3.547, 6.019), (6.419, 9.976), (10.376, 12.245), (12.645, 16.778), (17.178, 19.77), (20.17, 21.945)]
MINLEN = 1.6
GAP = 0.3
TAIL = 1.9

CSS = PCSS + '''
.sa{color:#6fa8ff;text-shadow:0 0 18px rgba(110,160,255,.5)}
.desk{position:absolute;left:0;top:1190px;width:1080px;height:760px;background:linear-gradient(180deg,#1a1410 0%,#0d0a08 60%);border-top:4px solid #c9963f;box-shadow:0 -10px 60px rgba(240,180,80,.18)}
.desk:after{content:'';position:absolute;left:0;right:0;top:0;height:120px;background:repeating-linear-gradient(90deg,rgba(255,220,160,.04) 0 60px,rgba(0,0,0,0) 60px 140px)}
.cone{position:absolute;left:-60px;top:-40px;width:760px;height:1120px;background:linear-gradient(160deg,rgba(255,214,140,.20),rgba(255,214,140,0) 70%);clip-path:polygon(18% 0,32% 0,100% 100%,0 100%)}
.lampb{position:absolute;left:96px;top:110px;width:120px;height:60px;border-radius:60px 60px 10px 10px;background:linear-gradient(#e7b65e,#9a6a22);box-shadow:0 30px 60px rgba(255,200,120,.45)}
.shadow{position:absolute;width:420px;height:46px;border-radius:50%;background:rgba(0,0,0,.55);filter:blur(10px)}
.ph{position:absolute;width:400px;height:700px;border-radius:58px;background:#0e1016;border:8px solid #2a2f3a;box-shadow:0 0 0 2px #4a5262,0 34px 90px rgba(0,0,0,.75);overflow:hidden;color:#eef2fb}
.ph .nt{width:120px;height:28px;background:#000;border-radius:0 0 16px 16px;margin:0 auto}
.ph .hdr{font:800 26px Inter;color:#9fb0cc;letter-spacing:3px;text-align:center;margin-top:24px;text-transform:uppercase}
.ph .row{margin:18px 26px 0;padding:20px 22px;border-radius:24px;background:#171b25;border:2px solid #2b3345;font:700 28px Inter;white-space:nowrap;text-align:left}
.ph .row.on{border-color:var(--ac);background:#132036}
.ph .row i{font-style:normal;display:inline-block;width:40px;height:40px;border-radius:50%;background:var(--ac);color:#0b0f18;text-align:center;line-height:40px;font:900 24px Inter;margin-right:14px;vertical-align:1px}
.ph .row.off i{background:#3a4255;color:#9fb0cc}
.ph .msg{margin:26px 24px 0;padding:22px;border-radius:26px 26px 26px 6px;background:#1c2232;text-align:left;font:600 26px Inter;line-height:1.35}
.ph .msg b{display:block;font:800 28px Inter;color:var(--ac);margin-bottom:6px}
.ph .btn{margin:22px auto 0;width:300px;padding:18px 0;border-radius:40px;background:var(--ac);color:#0b0f18;font:900 28px Inter;text-align:center}
.qr{width:180px;height:180px;margin:24px auto 0;border-radius:16px;background:#f4ede0;padding:14px;display:grid;grid-template-columns:repeat(7,1fr);gap:4px}
.qr i{background:#151010;border-radius:3px}.qr i.o{background:transparent}
.cal{position:absolute;width:230px;border-radius:26px;overflow:hidden;background:#f4ede0;box-shadow:0 24px 60px rgba(0,0,0,.6);text-align:center;color:#141414}
.cal .m{background:#c9963f;color:#141010;font:900 30px Inter;padding:10px 0;letter-spacing:4px}
.cal .d{font:900 104px 'DejaVu Serif',serif;line-height:1.1}
.cal .h{font:800 30px Inter;color:#2a4f8f;padding-bottom:14px}
.dots{display:flex;gap:14px;justify-content:center;margin-top:24px}
.dots i{width:52px;height:52px;border-radius:50%;border:3px solid var(--ac);font:900 24px Inter;font-style:normal;color:var(--ac);display:flex;align-items:center;justify-content:center}
.dots i.f{background:var(--ac);color:#0b0f18}
.cardb{position:absolute;width:300px;height:190px;border-radius:22px;background:linear-gradient(135deg,#1f3a6e,#0f1d3a);border:2px solid #6fa8ff;box-shadow:0 24px 60px rgba(0,0,0,.6)}
.cardb:before{content:'';position:absolute;left:30px;top:62px;width:56px;height:42px;border-radius:8px;background:linear-gradient(135deg,#f3d08a,#b98a35)}
.cardb:after{content:'•••• ••••';position:absolute;left:30px;bottom:26px;font:700 26px 'DejaVu Sans Mono',monospace;color:#cfdaf0;letter-spacing:2px}
.gift{position:absolute}
'''

QR = '<div class="qr">' + ''.join('<i class="o"></i>' if c == '0' else '<i></i>' for c in '1110111100110110101011100101110011010110111011001') + '</div>'


def desk():
    return '<div class="cone"></div><div class="desk"></div>'


def phone(x, y, inner, g=None, fx='up'):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    return f'<div class="shadow" style="left:{x - 10}px;top:{y + 690}px"></div><div class="ph" style="left:{x}px;top:{y}px"{a}><div class="nt"></div>{inner}</div>'


def numc(x, y, n, g):
    return f'<div class="num" style="left:{x}px;top:{y}px" data-g="{g}" data-fx="stamp">{n}</div>'


GIFT = '''<svg class="gift" style="left:{x}px;top:{y}px" width="{s}" height="{s}" viewBox="0 0 200 200"{a}>
 <rect x="30" y="80" width="140" height="110" rx="10" fill="#1f3a6e" stroke="#6fa8ff" stroke-width="4"/>
 <rect x="20" y="58" width="160" height="34" rx="8" fill="#2a4f8f" stroke="#6fa8ff" stroke-width="4"/>
 <rect x="90" y="58" width="20" height="132" fill="#f3c766"/>
 <path d="M100 58 Q70 10 52 34 Q44 52 100 58 Z M100 58 Q130 10 148 34 Q156 52 100 58 Z" fill="none" stroke="#f3c766" stroke-width="7"/>
</svg>'''

BODY = hud('BUREAU · TUTO 1-2-3', 'HELLO BANK') + BANNER + '''
  <div class="scene" data-s="0">''' + desk() + hdx(230, [('h1 sa', 'PARRAINAGE HELLO BANK', None, 'font-size:66px'), ('it gold', 'la marche à suivre', None, 'font-size:70px'), ('it gold', 'en 3 étapes', None, 'font-size:70px')]) + \
    phone(340, 560, '<div class="hdr">Mon parrainage</div><div class="row on"><i>1</i>Invitation</div><div class="row off"><i>2</i>Ouverture</div><div class="row off"><i>3</i>Conditions</div><div class="btn">C\'est parti</div>') + '''</div>
  <div class="scene" data-s="1" data-in="right">''' + desk() + numc(90, 240, '1', '1.0') + hdx(250, [('h1', 'TU REÇOIS', '1.0', 'font-size:62px'), ('it sa', 'mon invitation', '1.0', 'font-size:66px')], left=270, width=640) + \
    phone(340, 560, '<div class="hdr">Messages</div><div class="msg"><b>Invitation de parrainage</b>Ouvre ton compte avec mon lien</div><div class="btn" data-g="1.1" data-fx="stamp">Ouvrir le lien</div>' + QR.replace('class="qr"', 'class="qr" data-g="1.2" data-fx="pop"')) + '''
   <div class="tagp" style="left:110px;top:1240px;transform:rotate(-4deg)" data-g="1.2" data-fx="pop">lien ou QR code</div></div>
  <div class="scene" data-s="2" data-in="up">''' + desk() + numc(90, 240, '2', '2.0') + hdx(250, [('h1', 'TU OUVRES', '2.0', 'font-size:62px'), ('it sa', 'ton compte', '2.0', 'font-size:66px')], left=270, width=640) + \
    phone(150, 560, '<div class="hdr">Ouverture</div><div class="row on"><i>✓</i>Invitation reçue</div><div class="row on" data-g="2.1" data-fx="fade"><i>✓</i>Identité</div><div class="row off"><i>…</i>Signature</div>', g='2.0') + '''
   <div class="cal" style="left:640px;top:700px;transform:rotate(5deg)" data-g="2.2" data-fx="stamp"><div class="m">NOV.</div><div class="d">30</div><div class="h">avant 15 h</div></div></div>
  <div class="scene" data-s="3" data-in="pop">''' + desk() + hdx(240, [('h1', 'UNE OFFRE GROUPÉE', '3.0', 'font-size:62px'), ('it sa', 'comme Hello Prime', '3.1', 'font-size:66px')]) + \
    phone(340, 560, '<div class="hdr">Choisis ton offre</div><div class="row on" data-g="3.1" data-fx="stamp"><i>✓</i>Hello Prime</div><div class="row off"><i>○</i>Hello One</div><div class="row off"><i>○</i>Hello Start+</div><div class="btn">Continuer</div>') + '''</div>
  <div class="scene" data-s="4" data-in="right">''' + desk() + numc(90, 240, '3', '4.0') + hdx(250, [('h1', 'TU REMPLIS', '4.0', 'font-size:62px'), ('it sa', 'les conditions', '4.0', 'font-size:66px')], left=270, width=640) + '''
   <div class="card2" style="left:130px;top:580px;width:780px" data-g="4.1" data-fx="up"><div class="t">Par exemple, chaque mois</div>
    <div class="chk"><i>✓</i>5 paiements ou retraits</div><div class="chk"><i>✓</i>avec ta carte</div>
    <div class="dots"><i class="f" data-g="4.1" data-fx="pop">1</i><i class="f" data-g="4.1" data-fx="pop">2</i><i class="f" data-g="4.2" data-fx="pop">3</i><i class="f" data-g="4.2" data-fx="pop">4</i><i class="f" data-g="4.2" data-fx="stamp">5</i></div></div>
   <div class="cardb" style="left:390px;top:1040px;transform:rotate(-6deg)" data-g="4.2" data-fx="right"></div></div>
  <div class="scene" data-s="5" data-in="up">''' + desk() + '<div class="rays" style="left:290px;top:560px"></div>' + hdx(240, [('h1', 'TES AVANTAGES', '5.0', 'font-size:66px'), ('it gold', 'de bienvenue', '5.0', 'font-size:70px')]) + \
    GIFT.format(x=390, y=610, s=300, a=' data-g="5.0" data-fx="pop"') + '''
   <div class="tagp" style="left:200px;top:1000px" data-g="5.1" data-fx="stamp" data-slow="5.1">si tu remplis les conditions</div>
   <div class="cond" style="top:1100px;color:#c9d3e6">nouveaux clients · offre groupée souscrite</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + desk() + hdx(240, [('h1', 'SI TU VEUX QUE', '6.0', 'font-size:62px'), ('h1', 'JE TE PARRAINE,', '6.1', 'font-size:62px'), ('it gold', 'écris-moi en privé.', '6.2', 'font-size:68px')]) + \
    phone(340, 620, '<div class="hdr">Messages</div><div class="msg"><b>Moi</b>Je veux bien que tu me parraines</div>', g='6.1', fx='up') + '''
   <div class="cond" style="top:1340px;font-size:22px;color:#b8b0a0">Offres soumises aux conditions en vigueur · invitation avant le 30/11, 15 h</div></div>
'''
