import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo2d import *
# Vidéos QG, 26/11/2026, vidéo 2 : Revolut, format F17 « Problème / solution (FAQ) » : « je ferme le compte, ça compte ? ».
# Style D2 « Duo dessiné » (personnages blancs au trait) : le connaisseur (M) et l'indécise (P, chignon), casquette bleue.
# Source : https://www.revolut.com/fr-FR/legal/referrals-terms/ (consultée le 26/11/2026) : la récompense n'est pas versée, ou peut
# être révoquée, si l'invité annule une étape requise (exemples : fermeture du compte Revolut Personnel dans les 14 jours suivant
# l'ouverture, carte résiliée ou renvoyée avant livraison, achat éligible annulé ou remboursé) ; l'invité doit ouvrir le compte avec
# le lien et suivre les étapes de l'invitation dans les délais indiqués ; récompense versée sous 10 jours ouvrables ; les récompenses
# (et, le cas échéant, celles de l'invité) sont indiquées dans l'invitation. Règle de Badr : pas de prime en argent pour le filleul.
# Aucun montant.
# Voix : indécise = Manon (smallest, lightning_v3.1_pro), atempo 0.88 / 0.8 (débit naturel très rapide) ; connaisseur = Cosmo (xai)
# speed 1.1 ; « quatorze jours » compris « 18 jours » 2 fois (écrit en lettres puis en chiffres) -> « dans les deux semaines » ;
# silences internes ramenés à 0,16 s, niveaux à -19 dB.
NAME = 'qg_revolut3'
TITLE = 'QG Revolut je ferme le compte'
LINES = [
 ("Parrainage Revolut : j'ouvre le compte, puis je le ferme. Ça compte quand même ?",
  [("<em>Parrainage Revolut</em>", None), ("j'ouvre le compte,", None), ("puis je le <i>ferme</i>.", None), ("Ça compte quand même&nbsp;?", None)]),
 ("Non. Fermé dans les deux semaines, la récompense est annulée.",
  [("<i>Non.</i>", None), ("Fermé dans les", None), ("<em>2 semaines</em>,", None), ("la récompense", None), ("est <i>annulée</i>.", None)]),
 ("Et si je renvoie la carte avant de la recevoir ?",
  [("Et si je renvoie", None), ("la <em>carte</em>", None), ("avant de la recevoir&nbsp;?", None)]),
 ("Pareil, c'est annulé. Fais les étapes de l'invitation, dans les délais.",
  [("Pareil,", None), ("c'est <i>annulé</i>.", None), ("Fais les <em>étapes</em>", None), ("de l'invitation,", None), ("dans les <em>délais</em>.", None)]),
 ("Et moi, filleule, j'ai une prime en argent ?",
  [("Et moi, <em>filleule</em>,", None), ("j'ai une prime", None), ("en argent&nbsp;?", None)]),
 ("Non, pas chez Revolut. Une autre question ? Dis-la en commentaire. Et pour mon lien, envoie-moi Revolut en privé.",
  [("<i>Non</i>, pas chez Revolut.", None), ("Une autre question&nbsp;?", None), ("Dis-la en <em>commentaire</em>.", None),
   ("Et pour mon lien,", None), ("envoie-moi <em>REVOLUT</em>", None), ("en privé.", None)]),
]
SPLITS = [(0.15, 4.364), (4.614, 7.923), (8.173, 10.699), (10.949, 14.929), (15.179, 17.778), (18.028, 24.4)]
GAP = 0.2
TAIL = 2.4
DUO_LINES = [
 {'who': 'P', 'M': 'idle', 'P': 'talk', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'point', 'P': 'shock', 'shot': 'M'},
 {'who': 'P', 'M': 'idle', 'P': 'think', 'shot': 'P'},
 {'who': 'M', 'M': 'talk', 'P': 'idle', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'idle', 'P': 'shrug', 'shot': 'P'},
 {'who': 'M', 'M': 'point', 'P': 'head', 'shot': 'wide', 'lbl': False},
]
JS = duo2d_js(DUO_LINES, p_bun=True, cap='#3a6df0')

CSS = '''
#sub i{text-transform:none}
.hook{top:300px;left:60px;width:860px;font-size:92px}
.hook mark{display:inline-block;margin:6px 0}
.hook small{display:block;font:700 50px 'Comic Relief','Comic Sans MS',cursive;color:#e63946;text-transform:none;margin-top:14px;transform:rotate(-2deg)}
.faq{position:absolute;left:70px;top:330px;width:840px;padding:22px 26px;border:6px solid #111;border-radius:28px;background:#fff;box-shadow:9px 11px 0 #111;text-align:left}
.faq .h{font:900 34px 'Inter',sans-serif;letter-spacing:1px;margin-bottom:8px}
.faq .r{font:800 34px/1.25 'Inter',sans-serif;margin:7px 0;white-space:normal}
.faq .r b{color:#2bb673}
.faq .r i{font-style:normal;color:#e63946}
.faq .w{margin-top:10px;display:inline-block;padding:6px 18px;background:#ffe14d;border:4px solid #111;border-radius:14px;font:900 34px 'Inter',sans-serif}
.cmt{position:absolute;left:90px;top:330px;width:800px;padding:20px 26px;border:6px solid #111;border-radius:30px;background:#ffe14d;box-shadow:9px 11px 0 #111;font:900 44px/1.2 'Inter',sans-serif;color:#111;text-align:center}
.endc{left:70px;top:330px;width:840px;padding:26px 26px 22px}
.endc .k{font-size:46px}
.endc .c{font-size:104px}
.endc .b{font-size:31px}
.endc .x{font-size:21px;line-height:1.32}
'''

BODY = duo2d_body("LE CONNAISSEUR", "L'INDÉCISE") + '''
  <div class="scene" data-s="0"><div class="hook">Parrainage<br><mark>Revolut</mark><small>j'ouvre, je ferme… ça compte ?</small></div></div>
  <div class="scene" data-s="1" data-in="pop">
   <div class="tag" style="left:180px;top:290px;font-size:54px" data-g="1.1" data-fx="stamp">FERMÉ AVANT 14 JOURS</div>
   <div class="tag red" style="left:150px;top:410px;font-size:54px" data-g="1.4" data-fx="stamp" data-slow="1.4">RÉCOMPENSE ANNULÉE</div></div>
  <div class="scene" data-s="2" data-in="pop"><div class="tag" style="left:230px;top:330px;font-size:56px" data-g="2.1" data-fx="stamp">CARTE RENVOYÉE</div><div class="tag red" style="left:190px;top:450px;font-size:56px" data-g="2.2" data-fx="stamp">AVANT LIVRAISON ?</div></div>
  <div class="scene" data-s="3" data-in="pop">
   <div class="faq" data-g="3.0" data-fx="up"><div class="h">CONDITIONS REVOLUT : PAS DE RÉCOMPENSE SI…</div>
    <div class="r"><i>✗</i> compte fermé dans les <i>14 jours</i></div>
    <div class="r"><i>✗</i> carte renvoyée avant d'être livrée</div>
    <div class="r" data-g="3.1" data-fx="pop"><i>✗</i> achat éligible annulé ou remboursé</div>
    <div class="w" data-g="3.2" data-fx="stamp">✓ les étapes de l'invitation, dans les délais</div>
   </div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="tag" style="left:200px;top:380px;font-size:62px" data-g="4.0" data-fx="stamp">ET MOI, FILLEULE ?</div></div>
  <div class="scene" data-s="5" data-in="pop" style="z-index:7">
   <div class="tag red" style="left:120px;top:360px;font-size:46px" data-g="5.0" data-fx="stamp">filleul : pas de prime en argent</div>
   <div class="cmt" style="top:500px" data-g="5.1" data-fx="up">💬 Ta question sur le parrainage Revolut ? <u>Écris-la en commentaire</u></div>
  </div>
  <div class="scene" data-s="5" data-in="pop" style="z-index:8">
   <div class="endc" style="top:330px" data-g="5.3" data-fx="up"><div class="k">PARRAINAGE REVOLUT</div><div class="d" style="margin-top:6px">envoie-moi en privé</div><div class="c" data-g="5.4" data-fx="pop">REVOLUT</div>
    <div class="b" data-g="5.4" data-fx="pop">ouvre le compte avec le lien · suis les étapes de l'invitation</div>
    <div class="x">Offre soumise aux conditions en vigueur. Conditions de parrainage Revolut (revolut.com, consultées le 26/11/2026) : la récompense n'est pas versée ou peut être reprise si une étape est annulée (compte fermé dans les 14 jours, carte renvoyée avant livraison, achat éligible remboursé) ; étapes et délais indiqués dans l'invitation. Pas de prime en argent pour le filleul. Lien de parrainage : je touche une prime.</div></div>
  </div>
'''
