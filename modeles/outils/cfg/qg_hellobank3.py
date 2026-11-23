import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qg_ecran import *
# Vidéos QG du 23/11/2026, vidéo 2 : « Urgence Hello bank » (priorité du board). Format F13 réaction express (10-14 s).
# Style E « écran d'appli en gros plan » : calendrier de novembre avec le 30 entouré, écran d'ouverture via le lien, horloge 14:59.
# Source vérifiée le 23/11/2026 : https://www.hellobank.fr/fr/votre-offre-parrainage/ et /fr/parrainage/reglement-parrainage/
# (conditions en vigueur au 09/11/2026) : demande d'ouverture en ligne via le lien d'invitation avant le 30/11/2026 à 15 h
# (« sous réserve d'évolution »), ouverture définitive au plus tard le 30/12/2026 ; filleul 80 € (Hello One ou Hello Prime),
# + 50 € avec Hello Prime (5 paiements ou retraits carte / mois pendant 12 mois) ; parrain 150 €.
# Voix : Etienne (Cartesia sonic-3.5), speed 1.2, une synthèse par réplique, atempo 1.05.
NAME = 'qg_hellobank3'
TITLE = 'QG urgence Hello bank'
GAP = 0.12
MINLEN = 1.2
TAIL = 1.7
LINES = [
 ("Parrainage Hello bank : ça s'arrête le trente novembre, à quinze heures.", [("<em>Parrainage Hello bank</em> :", None), ("ça s'arrête", None), ("le <em>30 novembre</em>,", None), ("à <i>15 h</i>.", None)]),
 ("Avec mon lien, 80 € pour toi à l'ouverture.", [("Avec mon lien,", None), ("<em>80 €</em> pour toi", None), ("à l'ouverture.", None)]),
 ("Ta demande d'ouverture doit partir avant cette heure-là.", [("Ta demande", None), ("doit partir", None), ("<i>avant 15 h</i>.", None)]),
 ("Envoie-moi le mot Hello en privé. Vite.", [("Envoie-moi", None), ("<em>HELLO</em> en privé.", None), ("<i>Vite.</i>", None)]),
]
SPLITS = [(0.2, 3.346), (3.596, 6.324), (6.574, 8.974), (9.224, 11.792)]

CSS = '''
.alarm{position:absolute;left:70px;top:330px;padding:10px 26px;border-radius:18px;background:#e03131;color:#fff;font:900 46px Inter;letter-spacing:1px;box-shadow:0 10px 0 #8f1d1d;z-index:8;white-space:nowrap;transform:rotate(-2deg)}
.mo{font:900 46px Inter;margin:4px 0 18px;display:flex;justify-content:space-between}
.mo span{color:#e03131}
.gr{display:grid;grid-template-columns:repeat(7,1fr);gap:10px}
.gr b{height:100px;border-radius:16px;background:#f1f5f9;display:flex;align-items:center;justify-content:center;font:800 36px Inter;color:#94a3b8}
.gr b.p{background:#e2e8f0;color:#cbd5e1;text-decoration:line-through}
.gr b.t{background:#fff;color:#0f172a;outline:5px solid #2563eb}
.gr b.x{background:#e03131;color:#fff;font-weight:900;transform:scale(1.15);box-shadow:0 0 0 8px rgba(224,49,49,.25)}
.dl{position:absolute;left:150px;top:1200px;padding:14px 30px;border-radius:26px;background:#0f172a;color:#fff;font:900 62px Inter;white-space:nowrap;z-index:8;box-shadow:0 12px 0 rgba(15,23,42,.3)}
.dl span{color:#ffd43b}
.sm{position:absolute;left:540px;top:1265px;font:800 26px Inter;color:#334155;background:rgba(255,255,255,.95);border-radius:14px;padding:6px 14px;white-space:nowrap;z-index:8}
.clk{text-align:center;margin-top:30px}
.clk .v{font:900 200px/1 Inter;letter-spacing:-6px;color:#e03131}
.clk .k{font:800 34px Inter;color:#64748b;margin-top:10px}
.sent{margin-top:44px;border-radius:30px;background:#ecfdf5;border:4px solid #16a34a;padding:24px;font:900 40px Inter;color:#166534;text-align:center}
.cond{font-size:22px}
'''

CAL = '<div class="mo">Novembre <span>2026</span></div><div class="gr">' + ''.join(
    f'<b class="{"x" if d == 30 else ("t" if d == 23 else ("p" if d < 23 else ""))}">{d}</b>' for d in range(1, 31)) + '</div>'

BODY = search('parrainage hello bank') + '''
  <div class="alarm">⏳ FIN DE L'OFFRE</div>
  <div class="scene" data-s="0">
   <div class="zm" data-zg="0.2" data-zs="1.14" style="transform-origin:303px 1133px">''' + phone(CAL) + hand(303, 1133, '0.2') + '''</div>
   <div class="dl">FIN : <span>30/11 · 15 H</span></div></div>
  <div class="scene" data-s="1" data-in="right">
   <div class="zm" data-zg="1.1" data-zs="1.1" style="transform-origin:470px 760px">''' + phone('''<div class="hd"><span class="bk">‹</span>Ouvrir un compte</div>
     <div class="lb">Parrainage</div><div class="fd on">Lien d'invitation<span class="ok">✓</span></div>
     <div class="lb">Offre</div><div class="fd">Hello One / Hello Prime</div>
     <div class="btn">Faire ma demande</div><div class="gl"></div><div class="gl" style="width:60%"></div>''') + hand(470, 1010, '1.0') + '''</div>
   <div class="gain" style="left:410px;top:1170px;font-size:92px" data-g="1.1" data-fx="stamp" data-slow="1.1">+80 €</div>
   <div class="sm" style="left:330px;top:1325px" data-g="1.1" data-fx="fade">prime filleul si conditions remplies</div></div>
  <div class="scene" data-s="2" data-in="right">
   <div class="zm" data-zg="2.0" data-zs="1.08" style="transform-origin:470px 800px">''' + phone('''<div class="hd">Ta demande</div>
     <div class="clk"><div class="v">14:59</div><div class="k">lundi 30 novembre</div></div>
     <div class="sent" data-g="2.1" data-fx="pop">Demande envoyée ✓</div>''') + hand(470, 1030, '2.1') + '''</div>
   <div class="stk" style="left:470px;top:440px;transform:rotate(4deg)" data-g="2.2" data-fx="stamp">AVANT 15 H</div></div>
  <div class="scene" data-s="3" data-in="pop">''' + phone('''<div class="hd">Parrainage</div><div class="big" style="font-size:120px">80 €</div>''') + '''
   <div class="endc" data-g="3.0" data-fx="up"><div class="k">PARRAINAGE HELLO BANK</div><div class="d" style="margin-top:8px">envoie-moi en privé</div><div class="c">« HELLO »</div><div class="b">⏳ demande avant le 30/11 à 15 h</div></div>
   <div class="cond" style="top:905px" data-g="3.1" data-fx="fade">Offre soumise aux conditions en vigueur.<br>Hello bank (règlement au 09/11/2026) : 80 € pour le filleul (Hello One ou Hello Prime), prime filleul si conditions remplies ; + 50 € avec Hello Prime si 5 paiements ou retraits carte par mois pendant 12 mois. Demande en ligne via le lien d'invitation avant le 30/11/2026 à 15 h, sous réserve d'évolution ; ouverture définitive au plus tard le 30/12/2026. Écran : illustration.<br>Lien de parrainage : je touche une prime.</div></div>
'''
