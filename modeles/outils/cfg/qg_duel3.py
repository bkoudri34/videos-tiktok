import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qg_collage import *
# Vidéos QG, 24/11/2026, vidéo 2 : duel BoursoBank / Hello bank. Format F8 « résultat d'abord » (2 notifications « +80,00 € »
# dès la 1re image). Style C « Collage POV en papier découpé » (1re utilisation, construit le 24/11).
# Montants vérifiés le 24/11/2026 :
#  - boursobank.com/bon-plan/parrainage-boursobank (« Détails des conditions ») : 1re ouverture d'un compte individuel, 260 € max =
#    20 € (ouverture effective) + 80 € (1er versement ≥ 300 €, à l'ouverture ou dans les 30 jours) + 80 € (1 opération carte / mois
#    pendant 3 mois : 20 + 30 + 30) + 80 € (1re mobilité EasyMove, formulaire signé dans le mois) ; primes reprises si clôture < 24 mois.
#  - hellobank.fr/fr/votre-offre-parrainage/ : filleul 80 € à l'ouverture (Hello One ou Hello Prime) + 50 € avec Hello Prime
#    (au moins 5 paiements ou retraits carte par mois pendant les 12 premiers mois, versés le 13e mois) ; demande via le lien
#    d'invitation avant le 30/11/2026 à 15 h, ouverture définitive au plus tard le 30/12/2026.
# Voix : xAI « leo » (1re utilisation, voix « à tester » de la semaine), une synthèse par réplique, pauses internes ramenées à 0,2 s,
# atempo 1.05, 0,2 s au début et 0,35 s entre les répliques.
NAME = 'qg_duel3'
TITLE = 'QG duel BoursoBank Hello bank'
LINES = [
 ("Parrainage BoursoBank ou Hello bank ? 80 € des deux côtés !", [("Parrainage", None), ("<em>BoursoBank</em>", None), ("ou <em>Hello bank</em> ?", None), ("<i>80 €</i>", None), ("des deux côtés !", None)]),
 ("Hello bank : 80 € à l'ouverture, et 50 € au treizième mois avec Hello Prime.", [("Hello bank :", None), ("<i>80 €</i>", None), ("à l'ouverture,", None), ("et <em>+50 €</em>", None), ("au 13e mois", None), ("avec Hello Prime.", None)]),
 ("BoursoBank : 80 € si tu verses 300 €, et jusqu'à 260 € avec la carte et le changement de banque.", [("BoursoBank :", None), ("<i>80 €</i>", None), ("si tu verses 300 €,", None), ("et jusqu'à", None), ("<em>260 €</em>", None), ("avec la carte", None), ("et le changement", None), ("de banque.", None)]),
 ("Hello bank, c'est jusqu'au trente novembre, quinze heures.", [("Hello bank :", None), ("jusqu'au", None), ("<em>30 novembre</em>,", None), ("15 h.", None)]),
 ("Tu prends lequel ? Envoie-moi Bourso ou Hello en privé.", [("Tu prends", None), ("<em>lequel ?</em>", None), ("Envoie-moi", None), ("<em>BOURSO</em>", None), ("ou <em>HELLO</em>", None), ("en privé.", None)]),
]
SPLITS = [(0.2, 3.75), (4.1, 8.98), (9.33, 15.48), (15.83, 18.25), (18.6, 21.46)]
JS = STOP_JS

CSS = '''
.vc.sheet{width:560px}
.small{position:absolute;width:max-content;padding:12px 18px;font:800 26px/1.3 'Inter',sans-serif;color:#3b3226;background:#fbf7ee;border-radius:6px}
.pill{position:absolute;padding:12px 26px;border-radius:40px;background:#1b1a17;color:#ffd84a;font:800 34px 'Inter',sans-serif;white-space:nowrap}
'''

BODY = '''
  <div class="scene" data-s="0">
''' + phone(70, 430, -5, 'BoursoBank', '+80,00 €') + phone(530, 440, 4, 'Hello bank', '+80,00 €', ng='0.2') + tape(180, 410, -10) + tape(650, 418, 8) + '''
   <div class="kw">Parrainage <b>BoursoBank</b><br>ou <b>Hello bank</b> ?</div>
''' + perso(475, 990, 1.0, '#e2452f', 'o', 'shrug', look=-1) + lab(70, 1060, -6, 'MÊME PRIME ?', 'dark', g='0.3', size=60) + lab(660, 1170, 5, 'PAS PAREIL', 'red', g='0.4', size=56) + '''
  </div>
  <div class="scene" data-s="1" data-in="right">
''' + lab(110, 230, -3, 'HELLO BANK', 'blue', g='1.0', fx='pop', size=96) + '''
   <div class="abs" style="left:110px;top:400px" data-g="1.0" data-fx="up"><div class="pp vc sheet" style="transform:rotate(-2deg)"><div class="t" style="color:#2f6fe2">filleul</div><div class="v">80 €</div><div class="x">à l'ouverture du compte<br>Hello One ou Hello Prime</div></div></div>
''' + tape(320, 385, -4) + lab(300, 860, 5, '+50 € AU 13<sup>e</sup> MOIS', 'green', g='1.3', size=70) + '''
   <div class="abs" style="left:150px;top:990px" data-g="1.5" data-fx="pop"><div class="small" style="transform:rotate(-1deg)">avec Hello Prime : 5 paiements ou retraits carte<br>par mois pendant les 12 premiers mois</div></div>
''' + perso(720, 520, 1.0, '#2f6fe2', 'smile', 'pointl', look=-1) + '''
  </div>
  <div class="scene" data-s="2" data-in="left">
''' + lab(110, 230, 3, 'BOURSOBANK', 'red', g='2.0', fx='pop', size=96) + '''
   <div class="abs" style="left:110px;top:390px" data-g="2.0" data-fx="up"><div class="pp vc sheet" style="transform:rotate(2deg)"><div class="t" style="color:#e2452f">filleul</div><div class="v">80 €</div><div class="x">si ton 1<sup>er</sup> versement<br>fait au moins 300 €</div></div></div>
''' + tape(330, 372, 6) + lab(110, 820, -3, '+20 € ouverture', '', g='2.3', fx='pop', size=52) + lab(170, 905, 2, '+80 € carte (3 mois)', '', g='2.5', fx='pop', size=52) + lab(110, 990, -2, '+80 € changement de banque', '', g='2.6', fx='pop', size=52) + '''
   <div class="abs" style="left:150px;top:1105px" data-g="2.4" data-fx="stamp" data-slow="2.4"><div class="lab dark" style="transform:rotate(-3deg);font-size:96px">= JUSQU'À 260 €</div></div>
''' + perso(720, 470, 1.0, '#2e9e5b', 'open', 'point', look=-1) + '''
  </div>
  <div class="scene" data-s="3" data-in="up">
   <div class="abs" style="left:330px;top:300px" data-g="3.1" data-fx="stamp"><div class="pp cal" style="transform:rotate(-4deg)"><div class="h">NOVEMBRE</div><div class="d">30</div><div class="s">15 H</div></div></div>
''' + tape(460, 285, -6) + lab(120, 900, -2, "FIN DE L'OFFRE HELLO BANK", 'red', g='3.0', fx='pop', size=64) + '''
   <div class="abs" style="left:170px;top:1030px" data-g="3.2" data-fx="pop"><div class="small">demande via le lien avant le 30/11/2026 à 15 h<br>(ouverture définitive au plus tard le 30/12)</div></div>
''' + perso(70, 460, 1.0, '#ff8fb1', 'o', 'up', look=1, jump=True) + '''
  </div>
  <div class="scene" data-s="4" data-in="pop">
''' + lab(120, 230, -3, 'TU PRENDS LEQUEL ?', 'dark', g='4.0', fx='pop', size=90) + '''
   <div class="abs" style="left:520px;top:400px" data-g="4.3" data-fx="right"><div class="pp bub me">BOURSO</div></div>
   <div class="abs" style="left:600px;top:540px" data-g="4.4" data-fx="right"><div class="pp bub me">HELLO</div></div>
   <div class="abs" style="left:90px;top:680px" data-g="4.5" data-fx="left"><div class="pp bub you">je te parraine 🤝</div></div>
   <div class="abs" style="left:90px;top:860px" data-g="4.5" data-fx="pop"><div class="pill">⏳ Hello bank : jusqu'au 30/11, 15 h</div></div>
''' + perso(700, 700, 1.0, '#2f6fe2', 'smile', 'wave', look=-1, wave=True) + '''
   <div class="mention" style="top:1040px;width:840px;z-index:3">Offres soumises aux conditions en vigueur. Primes filleul si conditions remplies. Hello bank : 80 € à l'ouverture (Hello One ou Hello Prime) + 50 € avec Hello Prime si 5 paiements ou retraits carte par mois pendant 12 mois ; demande avant le 30/11/2026 à 15 h. BoursoBank : 1re ouverture d'un compte individuel, 20 € à l'ouverture + 80 € (1er versement ≥ 300 €) + 80 € (1 opération carte par mois pendant 3 mois) + 80 € (mobilité EasyMove). Lien de parrainage : je touche une prime.</div>
''' + confetti('4.0', 26, 5) + '''
  </div>
'''
