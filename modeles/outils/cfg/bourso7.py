import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# BoursoBank, 10/11/2026 16:00 - style v3 nuit & or, accent améthyste. Offre de bienvenue jusqu'à 180 € (nouveaux clients, sans date de fin annoncée ;
# sources : comparabanques.fr maj 20/10/2026, selectra.info). Relevé -> cadran -> téléphone -> checklist -> 3 mois -> appel à l'action.
NAME = 'bourso7'
TITLE = 'BoursoBank 180 euros amethyste'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Ta banque t'a déjà offert cent quatre-vingts euros ?", [("Ta banque t'a déjà", None), ("offert 180 € ?", None)]),
 ("Chez BoursoBank, c'est jusqu'à cent quatre-vingts euros de bienvenue.", [("Chez BoursoBank,", None), ("jusqu'à 180 €", None), ("de bienvenue.", None)]),
 ("Tu ouvres ton compte en ligne, depuis ton canapé.", [("Tu ouvres ton compte", None), ("en ligne,", None), ("depuis ton canapé.", None)]),
 ("Un premier versement, puis tu utilises ta carte.", [("Un premier versement,", None), ("puis tu utilises", None), ("ta carte.", None)]),
 ("La prime tombe par étapes, sur trois mois.", [("La prime tombe", None), ("par étapes,", None), ("sur 3 mois.", None)]),
 ("Envoie-moi BOURSO en privé, je t'envoie le lien.", [("Envoie-moi", None), ("BOURSO", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 1.94), (2.22, 4.874), (5.314, 7.457), (7.839, 10.169), (10.614, 12.606), (13.155, 15.208)]
GSTART = [[0.1, 0.9], [2.23, 3.3, 4.3], [5.32, 6.0, 6.6], [7.85, 9.1, 9.7], [10.62, 11.2, 12.0], [13.16, 13.6, 14.0, 14.5]]
MINLEN = 2.5
GAP = 0.4
TAIL = 2.0
TICKS = ''.join(f'<div class="tk" style="transform:rotate({k*12}deg)"></div>' for k in range(30))
CSS = '''
.am{color:#b48cff;text-shadow:0 0 18px rgba(180,140,255,.45)}
.rl{position:absolute;left:170px;top:700px;width:740px;background:#f4efe4;color:#1c1712;border-radius:26px;padding:40px 44px 46px;box-shadow:0 40px 90px rgba(0,0,0,.7);transform:rotate(-3deg)}
.rl .t{font:900 40px Inter;letter-spacing:5px;text-align:center}
.rl .s{font:600 22px Inter;letter-spacing:3px;color:#7a6f60;text-align:center;margin-top:6px}
.rl hr{border:0;border-top:3px dashed #b9ae9c;margin:22px 0}
.rl .row{display:flex;justify-content:space-between;font:600 32px Inter;line-height:1.9;white-space:nowrap}
.rl .row b{font-weight:900}
.rl .q{color:#7a3fd6;font:900 52px 'DejaVu Serif',serif}
.dial .ct{position:absolute;left:0;top:190px;width:592px;text-align:center}
.mo{position:absolute;bottom:0;width:200px;border-radius:18px 18px 0 0;background:linear-gradient(180deg,#c9a6ff,#4b2a8a);box-shadow:0 0 40px rgba(180,140,255,.35);transform-origin:50% 100%}
.mos{position:absolute;left:150px;top:760px;width:780px;height:440px;border-bottom:4px solid #d9a24c}
.ml{position:absolute;top:1230px;width:260px;text-align:center;font:800 28px Inter;letter-spacing:3px;color:#e9e4da}
.ck{position:absolute;left:0;top:0}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
BODY = hud('FRANCE · BANQUE EN LIGNE', 'BIENVENUE') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + head(240, [('h1', "TA BANQUE T'A DÉJÀ", None), ('it gold', 'offert 180 € ?', None)]).replace('class="it gold"', 'class="it gold" style="font-size:104px"') + '''
   <div class="rl"><div class="t">MON RELEVÉ</div><div class="s">CE MOIS-CI</div><hr>
    <div class="row"><span>Virement salaire</span><b>✓</b></div><div class="row"><span>Prélèvements</span><b>✓</b></div><div class="row"><span>Paiements carte</span><b>✓</b></div><hr>
    <div class="row" style="align-items:center"><span><b>Prime de bienvenue</b></span><span class="q">?</span></div></div></div>
  <div class="scene" data-s="1" data-in="pop"><div class="rays" style="top:690px"></div>''' + head(230, [('h1', 'CHEZ BOURSOBANK,', '1.0'), ('it gold', 'de bienvenue.', '1.2')]) + '''
   <div class="dial" style="top:600px">''' + TICKS + '''
    <div class="ct"><div style="font:800 40px Inter;letter-spacing:6px;color:#e9e4da">JUSQU'À</div>
     <div data-g="1.1" data-fx="stamp" data-slow="1.1" data-count="180" data-suf=" €"><div class="v gold" style="font:900 150px 'DejaVu Serif',serif;line-height:1.3">0 €</div></div>
     <div class="am" style="font:800 30px Inter;letter-spacing:5px">OFFRE DE BIENVENUE</div></div></div></div>
  <div class="scene" data-s="2" data-in="right">''' + head(230, [('h1', 'TON COMPTE,', '2.0'), ('it gold', 'en ligne, depuis ton canapé.', '2.1')]).replace('class="it gold"', 'class="it gold" style="font-size:60px"') + '''
   <div class="orb" style="left:200px;top:560px;width:680px;height:1000px"></div>
   <div class="phone" style="top:600px" data-g="2.0" data-fx="up"><div class="notch"></div>
    <div style="font:900 46px Inter;margin-top:40px">BoursoBank</div><div style="font:600 24px Inter;color:#aaa;margin-top:6px">Ouvrir un compte</div>
    <div style="margin:44px 26px 0;text-align:left;font:600 30px Inter;line-height:2.3;color:#ddd">
     <div data-g="2.1" data-fx="left"><span class="am">✓</span> Identité</div><div data-g="2.1" data-fx="left"><span class="am">✓</span> Justificatifs</div><div data-g="2.2" data-fx="left"><span class="am">✓</span> Signature</div></div>
    <div style="display:inline-block;margin-top:40px;background:#b48cff;color:#1b0f33;font:800 32px Inter;padding:14px 40px;border-radius:30px" data-g="2.2" data-fx="pop">Valider</div></div></div>
  <div class="scene" data-s="3" data-in="left"><div class="floor"></div>''' + head(230, [('h1', 'UN 1ER VERSEMENT,', '3.0'), ('it gold', 'puis ta carte.', '3.2')]) + '''
   <div class="pill" style="top:620px" data-g="3.0" data-fx="up"><div class="pin">1</div><div><b>COMPTE OUVERT</b><span>en ligne, en quelques étapes</span></div></div>
   <div class="pill" style="top:760px" data-g="3.0" data-fx="up"><div class="pin">2</div><div><b>PREMIER VERSEMENT</b><span>pour activer ton compte</span></div></div>
   <div class="pill" style="top:900px;border-color:rgba(180,140,255,.85)" data-g="3.1" data-fx="up"><div class="pin" style="background:#b48cff">3</div><div><b class="am">PAIEMENTS CARTE</b><span>tu utilises ta carte</span></div></div>
   <div class="abs" style="left:440px;top:1060px;width:200px;height:126px;border-radius:16px;background:linear-gradient(135deg,#3a2466,#120c20);border:3px solid #b48cff;box-shadow:0 20px 50px rgba(0,0,0,.6)" data-g="3.2" data-fx="pop"><div style="position:absolute;left:22px;top:34px;width:40px;height:30px;border-radius:6px;background:#e0ac55"></div></div></div>
  <div class="scene" data-s="4" data-in="pop">''' + head(230, [('h1', 'LA PRIME TOMBE', '4.0'), ('it gold', 'par étapes, sur 3 mois.', '4.1')]).replace('class="it gold"', 'class="it gold" style="font-size:66px"') + '''
   <div class="mos"><div class="mo" style="left:20px;height:150px" data-g="4.0" data-fx="up"></div><div class="mo" style="left:290px;height:260px" data-g="4.1" data-fx="up"></div><div class="mo" style="left:560px;height:400px" data-g="4.2" data-fx="up"></div></div>
   <div class="ml" style="left:120px">MOIS 1</div><div class="ml" style="left:390px">MOIS 2</div><div class="ml" style="left:660px">MOIS 3</div>
   <div class="abs gold" style="left:600px;top:640px;font:900 52px 'DejaVu Serif',serif;white-space:nowrap" data-g="4.2" data-fx="pop">180 € max</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', 'ENVOIE-MOI', '5.0'), ('big gold', '« BOURSO »', '5.1'), ('it gold', 'en privé.', '5.2')]).replace('class="big gold"', 'class="big gold" style="font-size:130px"') + '''
   <div class="pill" style="top:720px" data-g="5.2" data-fx="up"><div class="pin">✉</div><div><b>LE LIEN</b><span>je te l'envoie en privé</span></div></div>
   <div class="search" style="top:860px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1010px">Offre soumise aux conditions en vigueur<br>BoursoBank : jusqu'à 180 € (offre de bienvenue,<br>nouveaux clients, montant maximum versé par étapes)</div></div>
'''
