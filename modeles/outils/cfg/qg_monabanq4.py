import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo import *
# Vidéos QG, 24/11/2026, vidéo 1 : Monabanq. Format F16 « Quand est-ce que je suis payé ? » (1re vidéo F16) joué par les
# 2 mannequins blancs : l'indécise pose la question, le connaisseur déroule la frise des 5 primes avec les délais officiels.
# Style D « Duo 3D » (Three.js r149 embarqué). Fin : question à commenter, puis fausse conversation de messagerie et mentions.
# Montants et délais vérifiés le 24/11/2026 sur monabanq.com/fr/parrainage.html (mentions légales, renvoi 2, offre de bienvenue
# valable depuis le 01/07/2026, 1re ouverture d'un compte courant Pratiq, Pratiq+, Uniq ou Uniq+ suivie d'une 1re alimentation) :
#  - 20 € à l'ouverture, versés le 16 du mois suivant l'ouverture ;
#  - 60 € si au moins 300 € versés dans le mois suivant l'ouverture, versés au plus tard 2 mois après le constat de l'alimentation ;
#  - 60 € avec une carte Visa et au moins 30 paiements carte dans les 2 mois, versés le 16 du mois suivant la 30e opération ;
#  - 80 € pour le service d'aide à la mobilité bancaire (mandat signé en ligne dans le mois), versés au plus tard 60 jours après
#    la signature du formulaire ;
#  - 60 € de fidélité le 13e mois (compte conservé + 2 autres produits dont 1 épargne), versés au plus tard le 16 du 13e mois ;
#  - primes reprises en cas de clôture à l'initiative du client dans les 12 mois.
# Voix : l'indécise (P) = Smallest « manon » (lightning_v3.1_pro, -11 dB) ; le connaisseur (M) = Inworld « Mathieu » (inworld-tts-2) ;
# dernière réplique coupée après « Pour mon lien, » (entendu « Pour nos liens ») ; une synthèse par réplique, pauses internes ramenées à 0,2 s, 0,2 s au début et 0,32 s entre les répliques.
NAME = 'qg_monabanq4'
TITLE = 'QG Monabanq ta prime arrive quand'
HEAD = THREE
LINES = [
 ("Parrainage Monabanque : ma prime, elle arrive quand ?", [("<em>Parrainage</em>", None), ("Monabanq :", None), ("ma prime,", None), ("elle arrive", None), ("<i>QUAND ?</i>", None)]),
 ("En cinq morceaux. D'abord 20 €, le seize du mois après l'ouverture.", [("En <em>5 morceaux</em>.", None), ("D'abord <i>20 €</i>,", None), ("le 16 du mois", None), ("après l'ouverture.", None)]),
 ("Puis versement, carte, changement de banque : chacune au plus tard deux mois après la condition.", [("Puis versement,", None), ("carte,", None), ("changement de banque :", None), ("chacune", None), ("<em>au plus tard</em>", None), ("2 mois après", None), ("la condition.", None)]),
 ("Et le reste ?", [("Et le <i>reste ?</i>", None)]),
 ("Soixante euros au treizième mois, avec deux autres produits dont une épargne.", [("<i>60 €</i>", None), ("au <em>13e mois</em>,", None), ("avec 2 autres produits", None), ("dont 1 épargne.", None)]),
 ("Et toi, ta prime, tu l'attends depuis quand ? Dis-le en commentaire !", [("Et toi,", None), ("ta prime,", None), ("tu l'attends", None), ("<i>depuis quand ?</i>", None), ("Dis-le en", None), ("<em>commentaire !</em>", None)]),
 ("Envoie-moi le mot Monabanque, en message privé.", [("Envoie-moi", None), ("le mot <i>MONABANQ</i>", None), ("en message", None), ("privé.", None)]),
]
SPLITS = [(0.2, 2.41), (2.73, 6.42), (6.74, 11.69), (12.01, 12.58), (12.9, 16.63), (16.95, 20.02), (20.34, 23.03)]
MINLEN = 0.9
GAP = 0.12
TAIL = 2.0
DUO_LINES = [
 {'who': 'P', 'M': 'idle', 'P': 'think', 'shot': 'wide'},
 {'who': 'M', 'M': 'talk', 'P': 'idle', 'shot': 'M', 'lbl': False},
 {'who': 'M', 'M': 'point', 'P': 'idle', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'idle', 'P': 'shrug', 'shot': 'P'},
 {'who': 'M', 'M': 'cool', 'P': 'shock', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'idle', 'P': 'point', 'shot': 'P', 'lbl': False},
 {'who': 'M', 'M': 'hip', 'P': 'idle', 'shot': 'wide', 'lbl': False},
]
JS = duo_js(DUO_LINES)

CSS = '''
#sub{left:60px;width:860px;font-size:86px}
.hook{top:225px;font-size:80px}
.hook small{display:block;font:900 44px 'Inter',sans-serif;-webkit-text-stroke:8px #000;margin-top:12px;color:#ffd23f}
.cmp{position:absolute;top:230px;padding:22px 0 20px;border-radius:30px;background:#fff;color:#111;text-align:center;box-shadow:0 16px 0 rgba(0,0,0,.35),0 30px 80px rgba(0,0,0,.55)}
.cmp .t{font:900 34px 'Inter',sans-serif;letter-spacing:2px}
.cmp .p{font:900 120px 'Inter','Arial Black',sans-serif;letter-spacing:-3px;line-height:1.05}
.cmp .x{font:800 30px 'Inter',sans-serif;color:#4b5563}
.tl{position:absolute;left:90px;top:215px;width:820px;padding:20px 26px;border-radius:30px;background:#fff;color:#111;box-shadow:0 16px 0 rgba(0,0,0,.35),0 30px 80px rgba(0,0,0,.55)}
.tl .r{display:flex;align-items:center;gap:20px;padding:12px 0;border-bottom:3px dashed #e5e7eb}
.tl .r:last-child{border-bottom:0}
.tl .a{flex:0 0 170px;text-align:center;font:900 72px 'Inter','Arial Black',sans-serif;color:#e5322d;letter-spacing:-2px}
.tl .w{font:800 32px/1.25 'Inter',sans-serif;color:#111}
.tl .w b{display:block;font:900 34px 'Inter',sans-serif;color:#0f766e}
.tl .h{font:900 30px 'Inter',sans-serif;letter-spacing:2px;color:#6b7280;text-align:center;padding-bottom:6px}
.qbox{position:absolute;left:90px;top:230px;width:820px;padding:30px 30px 34px;border-radius:40px;background:#ffd23f;color:#111;text-align:center;box-shadow:0 16px 0 rgba(0,0,0,.35)}
.qbox .q{font:900 72px/1.08 'Inter','Arial Black',sans-serif;letter-spacing:-1px}
.qbox .c{margin-top:16px;display:inline-block;padding:10px 26px;border-radius:30px;background:#111;color:#fff;font:800 38px 'Inter',sans-serif}
.chat{position:absolute;left:90px;top:200px;width:820px;padding:26px 26px 22px;border-radius:40px;background:#fff;color:#111;box-shadow:0 22px 0 rgba(0,0,0,.35),0 40px 100px rgba(0,0,0,.6)}
.chat .hd{font:800 26px 'Inter',sans-serif;color:#6b7280;letter-spacing:2px;text-align:center;padding-bottom:12px;border-bottom:2px solid #eee}
.chat .m{margin:14px 0 0 auto;width:max-content;padding:14px 26px;border-radius:30px 30px 8px 30px;background:#2563eb;color:#fff;font:900 52px 'Inter',sans-serif}
.chat .y{margin:14px auto 0 0;width:max-content;padding:14px 26px;border-radius:30px 30px 30px 8px;background:#f1f1f1;color:#111;font:800 44px 'Inter',sans-serif}
.chat .pill{margin:16px auto 0;width:max-content;padding:8px 22px;border-radius:30px;background:#111;color:#ffd23f;font:800 28px 'Inter',sans-serif}
.chat .x{margin-top:14px;font:600 21px/1.35 'Inter',sans-serif;color:#6b7280}
'''

BODY = duo_body("LE CONNAISSEUR", "L'INDÉCISE") + '''
  <div class="scene" data-s="0"><div class="hook">Parrainage <em>Monabanq</em> :<br>ta prime arrive <em>quand</em> ?</div></div>
  <div class="scene" data-s="1" data-in="pop">
   <div class="tag" style="left:250px;top:230px;font-size:64px" data-g="1.0" data-fx="stamp">5 MORCEAUX</div>
   <div class="cmp" style="left:190px;top:360px;width:700px" data-g="1.1" data-fx="up"><div class="t">PRIME N°1 · OUVERTURE</div><div class="p" data-g="1.1" data-fx="stamp">20 €</div><div class="x">versés le 16 du mois<br>suivant l'ouverture</div></div>
  </div>
  <div class="scene" data-s="2" data-in="up">
   <div class="tl" data-g="2.0" data-fx="up"><div class="h">TES PRIMES SUIVANTES</div>
    <div class="r" data-g="2.0" data-fx="left"><div class="a">60 €</div><div class="w">300 € versés dans le mois<b>→ au plus tard 2 mois après</b></div></div>
    <div class="r" data-g="2.1" data-fx="left"><div class="a">60 €</div><div class="w">30 paiements carte en 2 mois<b>→ le 16 du mois suivant</b></div></div>
    <div class="r" data-g="2.2" data-fx="left"><div class="a">80 €</div><div class="w">mobilité bancaire (mandat)<b>→ au plus tard 60 jours après</b></div></div>
   </div>
  </div>
  <div class="scene" data-s="3" data-in="pop"><div class="tag red" style="left:250px;top:280px;font-size:76px" data-g="3.0" data-fx="stamp">ET LE RESTE ?</div></div>
  <div class="scene" data-s="4" data-in="pop">
   <div class="cmp" style="left:140px;width:800px" data-g="4.0" data-fx="up"><div class="t">PRIME DE FIDÉLITÉ</div><div class="p" data-g="4.0" data-fx="stamp">60 €</div><div class="x">le 13e mois · compte conservé<br>+ 2 autres produits dont 1 épargne</div></div>
   <div class="tag" style="left:200px;top:700px;font-size:62px" data-g="4.2" data-fx="stamp" data-slow="4.2">TOTAL : JUSQU'À 280 €</div>
   <div class="tag" style="left:230px;top:800px;font-size:30px;background:#fff" data-g="4.2" data-fx="pop">primes filleul si conditions remplies</div>
  </div>
  <div class="scene" data-s="5" data-in="pop">
   <div class="qbox" data-g="5.0" data-fx="up"><div class="q">Tu attends ta prime<br>depuis quand ?</div><div class="c" data-g="5.4" data-fx="pop">💬 dis-le en commentaire</div></div>
  </div>
  <div class="scene" data-s="6" data-in="pop" style="z-index:7">
   <div class="chat" data-g="6.0" data-fx="up"><div class="hd">PARRAINAGE MONABANQ · message privé</div>
    <div class="m" data-g="6.2" data-fx="right">MONABANQ</div>
    <div class="y" data-g="6.3" data-fx="left">je te parraine 🤝</div>
    <div class="pill" data-g="6.3" data-fx="pop">⏳ offre de bienvenue en cours (vérifiée le 24/11)</div>
    <div class="x">Offre soumise aux conditions en vigueur. Monabanq, 1re ouverture d'un compte courant : 20 € (versés le 16 du mois suivant l'ouverture) + 60 € si 300 € versés dans le mois (au plus tard 2 mois après) + 60 € pour 30 paiements carte en 2 mois (le 16 du mois suivant) + 80 € avec la mobilité bancaire (au plus tard 60 jours après le mandat) + 60 € le 13e mois (2 autres produits dont 1 épargne). Primes reprises si clôture dans les 12 mois. Lien de parrainage : je touche une prime.</div></div>
  </div>
'''
