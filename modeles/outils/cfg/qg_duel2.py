import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo import *
# Vidéos QG, 21/11/2026, vidéo 1 : duel Hello bank / Monabanq. Format F9 « duel / comparatif » joué par les 2 mannequins.
# Style D « Duo 3D » (1re utilisation en QG : Three.js r149 embarqué dans outils/vendor depuis le 20/11).
# Montants vérifiés le 21/11/2026 :
#  - hellobank.fr/fr/votre-offre-parrainage/ + /fr/parrainage/reglement-parrainage/ : filleul 80 € à l'ouverture (Hello One ou Hello Prime),
#    + 50 € avec Hello Prime / Prime Duo (5 paiements ou retraits carte par mois sur les 12 premiers mois, versés le 13e mois),
#    demande d'ouverture avant le 30/11/2026 15 h, ouverture définitive au plus tard le 30/12/2026.
#  - monabanq.com/fr/parrainage.html : jusqu'à 280 € = 20 + 60 (300 € versés le mois suivant) + 60 (30 paiements carte en 2 mois)
#    + 80 (mobilité bancaire) + 60 (13e mois, 2 autres produits dont 1 épargne) ; offre valable depuis le 01/07/2026.
# Voix : l'indécis (P) = xAI « cosmo » speed 1.1 ; le connaisseur (M) = Cartesia Etienne speed 1.2 ; une synthèse par réplique,
# silences coupés, cosmo +6,5 dB, tout à atempo 1.07, 0,2 s au début et 0,45 s entre les répliques.
NAME = 'qg_duel2'
TITLE = 'QG duel Hello bank Monabanq'
HEAD = THREE
LINES = [
 ("Parrainage Hello bank ou Monabanque ? Je prends lequel ?", [("<em>Parrainage</em>", None), ("Hello bank", None), ("ou Monabanq ?", None), ("Je prends <i>lequel ?</i>", None)]),
 ("Ça dépend. Tu veux ta prime vite, ou le plus gros total ?", [("Ça dépend.", None), ("Ta prime", None), ("<em>vite</em>,", None), ("ou le plus", None), ("<i>gros total ?</i>", None)]),
 ("Vite, évidemment !", [("<em>Vite</em>,", None), ("évidemment !", None)]),
 ("Alors Hello bank : 80 € à l'ouverture. Et 50 € de plus au treizième mois, avec Hello Prime.", [("Alors Hello bank :", None), ("<i>80 €</i>", None), ("à l'ouverture.", None), ("Et <em>50 €</em> de plus", None), ("au 13e mois,", None), ("avec Hello Prime.", None)]),
 ("Et chez Monabanque, alors ?", [("Et chez", None), ("<em>Monabanq</em> ?", None)]),
 ("Jusqu'à 280 €, mais en cinq étapes, sur treize mois.", [("Jusqu'à", None), ("<i>280 €</i>,", None), ("mais en", None), ("<em>5 étapes</em>,", None), ("sur 13 mois.", None)]),
 ("Donc plus d'argent, mais plus long ?", [("Plus d'argent,", None), ("mais", None), ("<em>plus long ?</em>", None)]),
 ("Exact. Et Hello bank, c'est jusqu'au trente novembre. Envoie-moi Hello ou Monabanque en privé.", [("Exact.", None), ("Hello bank :", None), ("jusqu'au <em>30/11</em>.", None), ("Envoie-moi", None), ("<i>HELLO</i> ou <i>MONABANQ</i>", None), ("en privé.", None)]),
]
SPLITS = [(0.2, 3.014), (3.464, 6.608), (7.058, 8.075), (8.525, 14.252), (14.702, 15.716), (16.166, 19.801), (20.251, 21.699), (22.149, 27.253)]
MINLEN = 0.9
GAP = 0.12
TAIL = 2.0
DUO_LINES = [
 {'who': 'P', 'M': 'idle', 'P': 'think', 'shot': 'wide'},
 {'who': 'M', 'M': 'talk', 'P': 'idle', 'shot': 'M', 'lbl': False},
 {'who': 'P', 'M': 'hip', 'P': 'point', 'shot': 'P'},
 {'who': 'M', 'M': 'point', 'P': 'idle', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'cool', 'P': 'shrug', 'shot': 'P'},
 {'who': 'M', 'M': 'talk', 'P': 'shock', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'idle', 'P': 'head', 'shot': 'P'},
 {'who': 'M', 'M': 'cool', 'P': 'idle', 'shot': 'wide', 'lbl': False},
]
JS = duo_js(DUO_LINES)

CSS = '''
#sub i{text-transform:none}
.hook{top:230px;font-size:78px}
.hook em{white-space:nowrap}
.endc{left:80px;width:830px}
.hook small{display:block;font:900 46px 'Inter',sans-serif;-webkit-text-stroke:8px #000;margin-top:10px;color:#ffd23f}
.cmp{position:absolute;top:230px;width:400px;padding:22px 0 20px;border-radius:30px;background:#fff;color:#111;text-align:center;box-shadow:0 16px 0 rgba(0,0,0,.35),0 30px 80px rgba(0,0,0,.55)}
.cmp .t{font:900 34px 'Inter',sans-serif;letter-spacing:2px}
.cmp .p{font:900 104px 'Inter','Arial Black',sans-serif;letter-spacing:-3px;line-height:1.05}
.cmp .x{font:800 28px 'Inter',sans-serif;color:#4b5563}
.chips{display:flex;gap:10px;justify-content:center;margin-top:12px}
.chips b{display:inline-block;padding:6px 12px;border-radius:14px;background:#ffd23f;font:900 30px 'Inter',sans-serif}
.endc .c{font-size:64px;letter-spacing:0;line-height:1.25}
.endc .x{font-size:21px;line-height:1.35;white-space:normal}
'''

BODY = duo_body("LE CONNAISSEUR", "L'INDÉCIS") + '''
  <div class="scene" data-s="0"><div class="hook">Parrainage<br><em>Hello bank</em> ou <em>Monabanq</em> ?<small>lequel choisir</small></div></div>
  <div class="scene" data-s="1" data-in="pop">
   <div class="tag" style="left:150px;top:260px;font-size:60px" data-g="1.2" data-fx="pop">⚡ VITE</div>
   <div class="tag red" style="left:500px;top:260px;font-size:60px" data-g="1.4" data-fx="pop">GROS TOTAL</div>
  </div>
''' + anc('P', '<div class="bub" style="left:-95px;top:-240px" data-g="2.0" data-fx="stamp">!</div>', '2') + '''
  <div class="scene" data-s="3" data-in="pop">
   <div class="cmp" style="left:240px;width:600px" data-g="3.0" data-fx="up"><div class="t">HELLO BANK</div><div class="p" data-g="3.1" data-fx="stamp">80 €</div><div class="x">à l'ouverture du compte</div>
    <div class="chips" data-g="3.3" data-fx="pop"><b>+50 € au 13e mois</b></div><div class="x" style="font-size:22px;margin-top:8px">avec Hello Prime · 5 paiements carte / mois</div></div>
  </div>
  <div class="scene" data-s="4" data-in="pop"><div class="tag red" style="left:250px;top:280px;font-size:72px" data-g="4.0" data-fx="stamp">ET MONABANQ ?</div></div>
  <div class="scene" data-s="5" data-in="pop">
   <div class="cmp" style="left:190px;width:700px" data-g="5.0" data-fx="up"><div class="t">MONABANQ</div><div class="x">jusqu'à</div><div class="p" style="color:#e5322d" data-g="5.1" data-fx="stamp" data-slow="5.1">280 €</div>
    <div class="chips" data-g="5.3" data-fx="pop"><b>20</b><b>60</b><b>60</b><b>80</b><b>60</b></div><div class="x" style="margin-top:8px">5 étapes · sur 13 mois</div></div>
  </div>
  <div class="scene" data-s="6" data-in="pop">
   <div class="cmp" style="left:110px" data-g="6.0" data-fx="left"><div class="t">HELLO BANK</div><div class="p">80 €</div><div class="x">dès l'ouverture</div></div>
   <div class="cmp" style="left:570px" data-g="6.1" data-fx="right"><div class="t">MONABANQ</div><div class="p" style="color:#e5322d">280 €</div><div class="x">sur 13 mois</div></div>
  </div>
  <div class="scene" data-s="7" data-in="pop" style="z-index:7">
   <div class="endc" data-g="7.0" data-fx="up"><div class="k">PARRAINAGE HELLO BANK OU MONABANQ</div><div class="d" style="margin-top:8px">envoie-moi en privé</div><div class="c" data-g="7.3" data-fx="pop">« HELLO »<br>ou « MONABANQ »</div>
    <div class="b" data-g="7.2" data-fx="pop">Hello bank : jusqu'au 30/11, 15 h</div>
    <div class="x">Offres soumises aux conditions en vigueur. Hello bank : 80 € à l'ouverture (Hello One ou Hello Prime) + 50 € avec Hello Prime si 5 paiements ou retraits carte par mois pendant 12 mois ; demande avant le 30/11/2026 à 15 h. Monabanq : 20 € à l'ouverture + 60 € (300 € versés le mois suivant) + 60 € (30 paiements carte en 2 mois) + 80 € (mobilité bancaire) + 60 € au 13e mois (2 autres produits dont 1 épargne). Lien de parrainage : je touche une prime.</div></div>
  </div>
'''
