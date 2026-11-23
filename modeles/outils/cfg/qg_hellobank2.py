import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo2d import *
# Vidéos QG, 23/11/2026, vidéo 1 : « BNP ou Hello bank : même groupe, pas les mêmes primes » (priorité du board, format F9 duel / comparatif).
# Style D2 « Duo dessiné » (personnages blancs au trait, 1re utilisation en QG) : le connaisseur (M) et l'indécise (P, chignon).
# Montants vérifiés le 23/11/2026 :
#  - hellobank.fr/fr/parrainage/reglement-parrainage/ (conditions en vigueur au 09/11/2026) : filleul 80 € (Hello One ou Hello Prime)
#    + 50 € avec Hello Prime si au moins 5 paiements ou retraits carte par mois pendant les 12 premiers mois ; demande avant le 30/11/2026
#    à 15 h (sous réserve d'évolution), ouverture définitive au plus tard le 30/12/2026 ; filleul exclu s'il détient déjà un compte Hello bank.
#  - hellobank.fr/faq/quel-est-le-delai-d-un-transfert-de-compte-bnp-paribas-vers-hello-bank : « vous pouvez ouvrir un compte bancaire
#    Hello bank! en plus de votre compte BNP Paribas ».
#  - mabanque.bnpparibas/fr/devenir-client-bnp-paribas : prime de bienvenue 80 € (1er compte, Esprit Libre Référence, au moins 10 opérations
#    carte dans les 3 mois suivant la réception de la carte), demande en ligne au plus tard le 14/12/2026.
# Voix : connaisseur = xAI « cosmo » speed 1.1 ; indécise = Cartesia Manon (Bright Belle) speed 1.15 ; une synthèse par réplique,
# silences coupés (pauses internes ramenées à 0,18 s), niveaux égalisés à -19 dB, atempo 1.14, 0,2 s au début, 0,3 s entre répliques.
NAME = 'qg_hellobank2'
TITLE = 'QG BNP ou Hello bank'
LINES = [
 ("Parrainage BNP, Hello bank ! Même groupe, pas les mêmes primes.", [("<em>Parrainage</em>", None), ("BNP, Hello bank&nbsp;!", None), ("Même groupe,", None), ("pas les mêmes <i>primes</i>", None)]),
 ("Hello bank, c'est pas déjà BNP ?", [("Hello bank,", None), ("c'est pas déjà <em>BNP&nbsp;?</em>", None)]),
 ("Si. Mais chez BNP, sans lien de parrainage : 80 € de bienvenue.", [("Si. Mais chez <em>BNP</em>,", None), ("sans lien", None), ("de parrainage :", None), ("<i>80&nbsp;€</i>", None), ("de bienvenue.", None)]),
 ("Et chez Hello bank, avec ton lien ?", [("Et chez <em>Hello bank</em>,", None), ("avec ton lien&nbsp;?", None)]),
 ("80 € à l'ouverture. Plus 50 € au treizième mois, avec Hello Prime.", [("<i>80&nbsp;€</i>", None), ("à l'ouverture.", None), ("Plus <em>50&nbsp;€</em>", None), ("au 13e mois,", None), ("avec Hello Prime.", None)]),
 ("Mais je suis déjà client BNP. Ça compte ?", [("Mais je suis déjà", None), ("client <em>BNP</em>.", None), ("Ça <i>compte&nbsp;?</i>", None)]),
 ("Le règlement exclut ceux qui ont déjà un compte Hello bank. Vérifie tes conditions.", [("Le règlement exclut", None), ("ceux qui ont déjà", None), ("un compte <em>Hello bank</em>.", None), ("Vérifie tes", None), ("<i>conditions.</i>", None)]),
 ("Fin le trente novembre, quinze heures. Envoie-moi le mot Hello en privé.", [("Fin le <em>30/11</em>,", None), ("15&nbsp;h.", None), ("Envoie-moi", None), ("le mot <i>HELLO</i>", None), ("en privé.", None)]),
]
SPLITS = [(0.2, 3.396), (3.696, 5.392), (5.692, 9.256), (9.556, 11.1), (11.4, 15.199), (15.499, 17.914), (18.214, 22.078), (22.378, 25.706)]
TAIL = 2.2
DUO_LINES = [
 {'who': 'M', 'M': 'talk', 'P': 'idle', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'idle', 'P': 'think', 'shot': 'P'},
 {'who': 'M', 'M': 'point', 'P': 'idle', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'hip', 'P': 'shrug', 'shot': 'P'},
 {'who': 'M', 'M': 'cool', 'P': 'shock', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'idle', 'P': 'head', 'shot': 'P'},
 {'who': 'M', 'M': 'talk', 'P': 'think', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'point', 'P': 'idle', 'shot': 'wide', 'lbl': False},
]
JS = duo2d_js(DUO_LINES, p_bun=True, cap='#2bb673')

CSS = '''
#sub i{text-transform:none}
.disc{position:absolute;left:50px;top:205px;width:880px;padding:10px 18px;border:5px solid #111;border-radius:18px;background:#fff;box-shadow:6px 7px 0 #111;
 font:800 33px/1.25 'Inter',sans-serif;color:#111;text-align:center;z-index:8}
.disc b{color:#e63946}
.hook{top:370px;left:60px;width:860px;font-size:84px}
.hook mark{display:inline-block;margin:6px 0}
.hook small{display:block;font:700 46px 'Comic Relief','Comic Sans MS',cursive;color:#e63946;text-transform:none;margin-top:14px;transform:rotate(-2deg)}
.cmp{position:absolute;top:350px;padding:20px 0 18px;border:6px solid #111;border-radius:30px;background:#fff;color:#111;text-align:center;box-shadow:9px 11px 0 #111;white-space:nowrap}
.cmp .t{font:900 32px 'Inter',sans-serif;letter-spacing:2px}
.cmp .t span{color:#e63946}
.cmp .p{font:900 120px 'Inter','Arial Black',sans-serif;letter-spacing:-3px;line-height:1.05}
.cmp .x{font:800 27px 'Inter',sans-serif;color:#444}
.cmp .s{font:700 22px 'Inter',sans-serif;color:#666;margin-top:6px}
.chips{display:flex;gap:10px;justify-content:center;margin-top:10px}
.chips b{display:inline-block;padding:6px 14px;border:4px solid #111;border-radius:14px;background:#ffe14d;font:900 34px 'Inter',sans-serif}
.faq{position:absolute;left:70px;top:350px;width:840px;padding:22px 26px;border:6px solid #111;border-radius:28px;background:#fff;box-shadow:9px 11px 0 #111;text-align:left}
.faq .r{font:800 33px/1.25 'Inter',sans-serif;margin:6px 0;white-space:normal}
.faq .r b{color:#2bb673}
.faq .r i{font-style:normal;color:#e63946}
.faq .w{margin-top:10px;display:inline-block;padding:6px 18px;background:#ffe14d;border:4px solid #111;border-radius:14px;font:900 36px 'Inter',sans-serif}
.endc{left:70px;top:340px;width:840px;padding:28px 26px 24px}
.endc .k{font-size:44px}
.endc .c{font-size:110px}
.endc .b{font-size:31px}
.endc .x{font-size:20.5px;line-height:1.32}
'''

BODY = duo2d_body("LE CONNAISSEUR", "L'INDÉCISE") + '''
  <div class="disc">Je n'ai <b>pas de lien BNP</b> : mon lien est <b>Hello bank</b>, je touche une prime.</div>
  <div class="scene" data-s="0"><div class="hook">Parrainage<br><mark>BNP</mark> <mark>Hello bank</mark><small>même groupe, pas les mêmes primes</small></div></div>
  <div class="scene" data-s="1" data-in="pop"><div class="tag" style="left:250px;top:380px;font-size:60px" data-g="1.1" data-fx="stamp">MÊME GROUPE ✓</div></div>
  <div class="scene" data-s="2" data-in="pop">
   <div class="cmp" style="left:150px;width:680px" data-g="2.0" data-fx="up"><div class="t">BNP PARIBAS · <span>SANS PARRAIN</span></div><div class="p" data-g="2.3" data-fx="stamp">80 €</div><div class="x">prime de bienvenue</div>
    <div class="s">si 10 paiements ou retraits carte en 3 mois</div><div class="s">demande avant le 14/12/2026</div></div>
  </div>
  <div class="scene" data-s="3" data-in="pop"><div class="tag red" style="left:200px;top:400px;font-size:66px" data-g="3.0" data-fx="stamp">ET HELLO BANK ?</div></div>
  <div class="scene" data-s="4" data-in="pop">
   <div class="cmp" style="left:150px;width:680px" data-g="4.0" data-fx="up"><div class="t">HELLO BANK · <span>AVEC MON LIEN</span></div><div class="p" style="color:#2bb673" data-g="4.0" data-fx="stamp" data-slow="4.0">80 €</div><div class="x">à l'ouverture du compte</div>
    <div class="chips" data-g="4.2" data-fx="pop"><b>+50 € au 13e mois</b></div><div class="s">avec Hello Prime · 5 paiements ou retraits / mois</div></div>
  </div>
  <div class="scene" data-s="5" data-in="pop"><div class="tag" style="left:190px;top:400px;font-size:60px" data-g="5.0" data-fx="stamp">DÉJÀ CLIENT BNP ?</div></div>
  <div class="scene" data-s="6" data-in="pop">
   <div class="faq" data-g="6.0" data-fx="up">
    <div class="r"><b>✓</b> FAQ Hello bank : on peut ouvrir un compte Hello bank <b>en plus</b> de son compte BNP</div>
    <div class="r" data-g="6.1" data-fx="pop"><i>✗</i> Règlement : pas de prime si tu as <i>déjà un compte Hello bank</i></div>
    <div class="w" data-g="6.4" data-fx="stamp">→ vérifie tes conditions</div>
   </div>
  </div>
  <div class="scene" data-s="7" data-in="pop" style="z-index:7">
   <div class="endc" data-g="7.0" data-fx="up"><div class="k">PARRAINAGE BNP HELLO BANK</div><div class="d" style="margin-top:6px">envoie-moi en privé</div><div class="c" data-g="7.0" data-fx="pop">HELLO</div>
    <div class="b" data-g="7.1" data-fx="pop">⏳ Hello bank : demande avant le 30/11, 15 h</div>
    <div class="x">Offre soumise aux conditions en vigueur. Hello bank (règlement au 09/11/2026) : 80 € pour le filleul (Hello One ou Hello Prime) + 50 € avec Hello Prime si 5 paiements ou retraits carte par mois pendant 12 mois ; demande avant le 30/11/2026 à 15 h, sous réserve d'évolution. BNP Paribas, offre de bienvenue sans parrain : 80 € si 10 opérations carte en 3 mois, demande avant le 14/12/2026. Lien de parrainage : je touche une prime.</div></div>
  </div>
'''
