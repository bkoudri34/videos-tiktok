import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from tuto import *
from qg_figs import *
# Vidéos QG, 18/11/2026 (2e passage), vidéo 3 : Revolut. Style T « tuto illustré » (personnages blancs animés, choix de Badr du 18/11).
# Format F2 « démystification » : « Parrainage Revolut : qui touche vraiment la prime ? » -> pas toi (seul le parrain) ->
# 3 étapes (lien d'invitation, identité, achats carte) -> montant et conditions dans l'invitation de l'appli -> appel à l'action.
# Source : help.revolut.com/fr-FR (conditions de la campagne de parrainage) + revolut.com/fr-FR/legal/referrals-terms, consultés le 18/11/2026 :
# campagne unilatérale, seul le parrain reçoit une récompense, montant indiqué dans l'invitation de l'appli -> aucun montant à l'écran.
# Voix : Speko par défaut (speechify simba-3.5 ; voix-htm-luxe refusée : 402, recharge ElevenLabs requise), speed 1.08.
NAME = 'qg_revolut1'
TITLE = 'QG Revolut qui touche la prime'
JS = 'const CAM=0.6, PUSH=0.010;' + FIGJS
GAP = 0.36
TAIL = 2.5
MINLEN = 1.8
LINES = [
 ("Parrainage Revolut : qui touche vraiment la prime ?", [("<em>Parrainage Revolut</em> :", None), ("qui touche <i>vraiment</i>", None), ("la prime ?", None)]),
 ("Pas toi. Chez Revolut, seul le parrain est récompensé.", [("<i>Pas toi.</i>", None), ("Chez Revolut,", None), ("seul le <em>parrain</em>", None), ("est récompensé.", None)]),
 ("Toi, tu ouvres ton compte avec son lien d'invitation.", [("Toi, tu ouvres ton compte", None), ("avec son <em>lien d'invitation</em>.", None)]),
 ("Tu vérifies ton identité, puis tu fais quelques achats avec ta carte.", [("Tu vérifies ton <em>identité</em>,", None), ("puis tu fais quelques <em>achats</em>", None), ("avec ta carte.", None)]),
 ("Le montant et les conditions sont écrits dans l'invitation, dans l'appli.", [("Le <em>montant</em> et les conditions", None), ("sont écrits dans l'invitation,", None), ("dans l'appli.", None)]),
 ("Tu veux l'ouvrir quand même ? Envoie-moi REVOLUT en privé, je t'envoie mon lien.", [("Tu veux l'ouvrir quand même ?", None), ("Envoie-moi <em>REVOLUT</em>", None), ("en privé,", None), ("je t'envoie mon lien.", None)]),
]
SPLITS = [(0.0, 2.42), (2.5, 5.52), (5.7, 7.72), (8.0, 10.82), (11.0, 13.62), (13.8, 17.3)]
GSTART = [[0.0, 1.27, 1.8], [2.55, 3.55, 4.05, 4.65], [5.75, 6.55], [8.05, 9.15, 10.05], [11.05, 12.05, 13.05], [13.85, 15.25, 15.85, 16.45]]

CSS = FIGCSS + '''
.coin{position:absolute;width:190px;height:190px;border-radius:50%;border:8px solid #111;background:#ffe14d;font:900 96px Inter;display:flex;align-items:center;justify-content:center;box-shadow:8px 9px 0 #111}
.idc{position:absolute;width:520px;height:300px;padding:28px}
.idc .ph{position:absolute;left:30px;top:40px;width:150px;height:190px;border:5px solid #111;border-radius:14px}
.idc .l{position:absolute;left:210px;height:24px;border-radius:12px;background:#e9e5dc}
.bk{position:absolute;width:520px;height:320px;border-radius:30px;border:7px solid #111;background:#fff;box-shadow:10px 12px 0 #111}
.bk .chip{position:absolute;left:46px;top:96px;width:90px;height:68px;border:5px solid #111;border-radius:12px;background:#ffe14d}
.bk .nb{position:absolute;left:46px;top:200px;font:800 36px 'DejaVu Sans Mono',monospace;letter-spacing:4px}
.pay{position:absolute;font:900 40px Inter;white-space:nowrap}
'''

GUY_IN = '<g class="ink"><circle cx="120" cy="80" r="56"/></g>'

BODY = '''
  <div class="scene" data-s="0">''' + title('Parrainage <mark>Revolut</mark><br><em>qui touche la prime&nbsp;?</em>', 220, size=76) + \
    guy(110, 600, 'cap', 'smile', 'hip') + guy(730, 600, 'curly', 'open', 'shrug', mirror=True) + '''
   <div class="coin" style="left:445px;top:700px">€</div>
   <div class="note" style="left:470px;top:930px;font-size:120px" data-g="0.1" data-fx="pop">?</div>
   <div class="tag" style="left:100px;top:1110px">LE PARRAIN</div><div class="tag" style="left:690px;top:1110px">TOI</div></div>
  <div class="scene" data-s="1" data-in="up">''' + title('Prime : <mark>le parrain</mark><br>seulement', 220, size=84) + \
    guy(110, 600, 'cap', 'smile', 'up') + guy(730, 600, 'curly', 'sad', 'down', mirror=True) + '''
   <div class="coin" style="left:170px;top:460px;width:140px;height:140px;font-size:70px" data-g="1.2" data-fx="stamp">€</div>''' + \
    svg(700, 640, 300, 300, '<path class="dr" pathLength="1" d="M20 20 L280 280" data-g="1.0" data-fx="draw"/><path class="dr" pathLength="1" d="M280 20 L20 280" data-g="1.0" data-fx="draw"/>', 'red') + '''
   <div class="note" style="left:560px;top:1000px;transform:rotate(-4deg)" data-g="1.1" data-fx="pop">0 € de prime</div>
   <div class="tag" style="left:100px;top:1110px">LE PARRAIN</div><div class="tag" style="left:690px;top:1170px">TOI</div></div>
  <div class="scene" data-s="2" data-in="right">''' + title('Étape 1', 220, size=84) + '''
   <div class="phone" style="left:300px;top:440px"><div class="scr"><div class="tt">Invitation reçue</div><div class="ln"></div><div class="ln" style="width:70%"></div>
    <div class="fl" data-g="2.1" data-fx="left">lien d'invitation ✓</div><div class="bt">Ouvrir mon compte</div><div class="ln" style="margin-top:40px"></div><div class="ln" style="width:55%"></div></div></div>
   <div class="num" style="left:150px;top:470px" data-g="2.0" data-fx="stamp">1</div>''' + circle(310, 650, 420, 150, '2.1') + \
    guy(780, 840, 'curly', 'smile', 'point', 0.62, mirror=True) + '''</div>
  <div class="scene" data-s="3" data-in="right">''' + title('Étapes 2 et 3', 220, size=84) + '''
   <div class="paper idc" style="left:120px;top:450px"><div class="ph"></div>''' + svg(55, 60, 100, 150, '<circle cx="50" cy="45" r="30"/><path d="M8 145 Q50 80 92 145"/>') + '''
    <div class="l" style="top:60px;width:260px"></div><div class="l" style="top:110px;width:220px"></div><div class="l" style="top:160px;width:250px"></div><div class="l" style="top:210px;width:160px"></div></div>
   <div class="num" style="left:30px;top:410px" data-g="3.0" data-fx="stamp">2</div>
   <div class="note" style="left:675px;top:520px;transform:rotate(5deg)" data-g="3.0" data-fx="pop">identité ✓</div>
   <div class="bk" style="left:380px;top:860px" data-g="3.1" data-fx="up"><div class="chip"></div><div class="nb">•••• 4821</div></div>
   <div class="num" style="left:250px;top:850px" data-g="3.1" data-fx="stamp">3</div>
   <div class="pay" style="left:400px;top:1215px;transform:rotate(-3deg)" data-g="3.2" data-fx="pop">achats carte</div>''' + circle(360, 840, 570, 360, '3.2', 3) + '''</div>
  <div class="scene" data-s="4" data-in="up">''' + title('Le montant ?', 220, size=84) + '''
   <div class="phone" style="left:470px;top:430px"><div class="scr"><div class="tt">Inviter des amis</div><div class="ln"></div>
    <div class="fl" style="font-size:28px">Récompense : <span class="hl" style="margin-left:8px">ici</span></div><div class="fl" style="font-size:28px">Conditions : <span class="hl" style="margin-left:8px">ici</span></div>
    <div class="bt">Partager mon lien</div><div class="ln" style="margin-top:40px"></div><div class="ln" style="width:55%"></div></div></div>''' + \
    circle(480, 610, 420, 230, '4.0') + guy(90, 640, 'cap', 'smile', 'point', 0.95) + '''
   <div class="note" style="left:40px;top:1160px;font-size:40px;transform:rotate(-3deg)" data-g="4.1" data-fx="pop">c'est dans l'appli !</div></div>
  <div class="scene" data-s="5" data-in="pop">
   <div class="endc" data-g="5.0" data-fx="up"><div class="k">ENVOIE-MOI EN PRIVÉ</div><div class="c">« REVOLUT »</div><div class="d">je t'envoie mon lien</div><div class="b">@htm.invest</div></div>
   <div class="note" style="left:330px;top:790px;transform:rotate(-3deg)" data-g="5.1" data-fx="pop">parrainage Revolut</div>''' + \
    guy(110, 830, 'curly', 'smile', 'up', 0.58) + '''
   <div class="cond" style="top:880px;left:290px;width:640px">Offre soumise aux conditions en vigueur.<br>Parrainage Revolut : seul le parrain reçoit une récompense ; montant et étapes indiqués dans l'invitation de l'appli. Le filleul ne reçoit pas de prime en argent.<br>Lien de parrainage : je touche une prime.</div></div>
'''
