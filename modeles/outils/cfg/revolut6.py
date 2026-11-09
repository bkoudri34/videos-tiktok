import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Revolut, 09/11/2026 16:00 - style v3 nuit & or, accent vert émeraude. Pas de montant (récompense parrain selon l'offre en cours, pas de prime en argent pour le filleul).
NAME = 'revolut6'
TITLE = 'Revolut parrainage nuit et or'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Sur Revolut, c'est le parrain qui est payé.", [("Sur Revolut,", None), ("c'est le parrain", None), ("qui est payé.", None)]),
 ("Toi, t'ouvres ton compte avec mon lien.", [("Toi,", None), ("t'ouvres ton compte", None), ("avec mon lien.", None)]),
 ("Ensuite, t'invites tes potes depuis l'appli.", [("Ensuite,", None), ("t'invites tes potes", None), ("depuis l'appli.", None)]),
 ("Chaque ami inscrit, une récompense selon l'offre en cours.", [("Chaque ami inscrit,", None), ("une récompense", None), ("selon l'offre en cours.", None)]),
 ("Par contre, pas de prime en argent pour le filleul.", [("Par contre,", None), ("pas de prime en argent", None), ("pour le filleul.", None)]),
 ("Envoie-moi REVOLUT en privé, je t'envoie le lien.", [("Envoie-moi", None), ("REVOLUT", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
GSTART = [[0.1, 0.9, 1.5], [2.62, 2.8, 3.7], [4.84, 5.6, 6.3], [7.37, 8.5, 9.2], [10.52, 11.0, 11.8], [12.9, 13.3, 13.6, 14.2]]
CSS = '''
.em{color:#3fd6a0;text-shadow:0 0 18px rgba(63,214,160,.45)}
.av{position:absolute;width:150px;height:150px;border-radius:50%;border:4px solid #d9a24c;display:flex;align-items:center;justify-content:center;font:900 56px Inter;color:#fff;box-shadow:0 0 30px rgba(240,180,80,.3)}
.av small{position:absolute;bottom:-46px;left:-30px;right:-30px;text-align:center;font:700 24px Inter;color:#e9e4da;letter-spacing:1px}
.ntf{position:absolute;left:170px;width:740px;height:124px;border-radius:30px;background:rgba(245,240,230,.96);color:#141210;display:flex;align-items:center;gap:22px;padding:0 26px;box-shadow:0 20px 50px rgba(0,0,0,.55);white-space:nowrap}
.ntf .ic{flex:none;width:70px;height:70px;border-radius:18px;background:#0f3b2c;color:#3fd6a0;font:900 40px Inter;display:flex;align-items:center;justify-content:center}
.ntf b{display:block;font:800 30px Inter}.ntf span{font:500 25px Inter;color:#555}
.col{position:absolute;top:640px;width:400px;height:560px;border-radius:30px;border:3px solid rgba(217,162,76,.7);background:rgba(30,24,15,.55);text-align:center;padding-top:40px}
.col .k{font:800 34px Inter;letter-spacing:4px;color:#bba98a}
.col .v{font:900 64px 'DejaVu Serif',serif;margin-top:40px;line-height:1.15}
.col .d{font:600 28px Inter;color:#e9e4da;margin-top:30px;line-height:1.4;padding:0 20px}
'''
BODY = hud('FRANCE · APPLI BANCAIRE', 'PARRAINAGE') + '''
  <div class="scene" data-s="0"><div class="floor"></div><div class="rays" style="top:640px"></div>
   ''' + head(240, [('h1', 'SUR REVOLUT,', None), ('h1 s', "C'EST LE PARRAIN", None), ('big gold', 'qui est payé.', None)]).replace('class="big gold"', 'class="it gold" style="font-size:96px"') + '''
   <div class="emb" style="top:740px"><span class="gold" style="font:900 64px 'DejaVu Serif',serif;letter-spacing:2px">PARRAIN</span></div>
   <div class="ntf" style="top:1150px"><div class="ic">★</div><div><b>Ton ami s'est inscrit</b><span>récompense selon l'offre en cours</span></div></div></div>
  <div class="scene" data-s="1" data-in="pop">''' + head(230, [('h1', "TOI, T'OUVRES", '1.1'), ('it gold', 'ton compte avec mon lien.', '1.2')]).replace('class="it gold"', 'class="it gold" style="font-size:62px"') + '''
   <div class="orb" style="left:200px;top:560px;width:680px;height:1000px"></div>
   <div class="phone" data-g="1.0" data-fx="up"><div class="notch"></div>
    <div style="font:900 50px Inter;margin-top:40px">Revolut</div><div style="font:600 24px Inter;color:#aaa;margin-top:6px">Ouvrir un compte</div>
    <div style="margin:50px 26px 0;border:3px solid #3fd6a0;border-radius:18px;height:84px;display:flex;align-items:center;padding:0 20px;gap:12px;font:600 24px Inter;color:#999;white-space:nowrap">Lien <span data-g="1.2" data-fx="type" style="font:800 30px Inter;color:#3fd6a0">parrainage ✓</span></div>
    <div style="margin:26px 26px 0;text-align:left;font:600 28px Inter;line-height:2.2;color:#ddd">✓ Appli<br>✓ Carte<br>✓ Identité</div>
    <div style="display:inline-block;margin-top:30px;background:#3fd6a0;color:#06261a;font:800 32px Inter;padding:14px 40px;border-radius:30px" data-g="1.2" data-fx="pop">Créer mon compte</div></div></div>
  <div class="scene" data-s="2" data-in="right">''' + head(230, [('h1', 'INVITE TES POTES', '2.1'), ('it gold', "depuis l'appli.", '2.2')]) + '''
   <div class="emb" style="left:390px;top:780px;width:300px;height:300px" data-g="2.0" data-fx="pop"><span class="em" style="font:900 120px Inter">+</span></div>
   <div class="ldr" style="left:250px;top:930px;width:140px" data-g="2.1" data-fx="grow"></div><div class="ldr" style="left:690px;top:930px;width:140px" data-g="2.1" data-fx="grow"></div>
   <div class="av" style="left:100px;top:855px;background:#2a5a8a" data-g="2.1" data-fx="pop">L<small>Léa</small></div>
   <div class="av" style="left:830px;top:855px;background:#8a3a5a" data-g="2.1" data-fx="pop">M<small>Malik</small></div>
   <div class="av" style="left:465px;top:1170px;background:#5a6a2a" data-g="2.2" data-fx="pop">S<small>Sam</small></div>
   <div class="abs" style="left:538px;top:1080px;width:4px;height:90px;background:#d9a24c" data-g="2.2" data-fx="fade"></div></div>
  <div class="scene" data-s="3" data-in="pop"><div class="floor"></div>''' + head(230, [('h1 s', 'CHAQUE AMI INSCRIT', '3.0'), ('it gold', 'une récompense', '3.1')]) + '''
   <div class="ntf" style="top:620px" data-g="3.0" data-fx="up"><div class="ic">✓</div><div><b>Léa s'est inscrite</b><span>Revolut · maintenant</span></div></div>
   <div class="ntf" style="top:770px" data-g="3.1" data-fx="up"><div class="ic">✓</div><div><b>Malik s'est inscrit</b><span>Revolut · maintenant</span></div></div>
   <div class="abs" style="left:90px;top:960px;width:900px;text-align:center" data-g="3.2" data-fx="stamp" data-slow="3.2"><div style="font:800 40px Inter;letter-spacing:5px">RÉCOMPENSE</div><div class="gold" style="font:900 92px 'DejaVu Serif',serif;line-height:1.3">selon l'offre</div><div class="gold" style="font:900 92px 'DejaVu Serif',serif;line-height:1.1">en cours</div><div style="font:700 26px Inter;letter-spacing:4px;color:#bba98a;margin-top:18px">POUR LE PARRAIN</div></div></div>
  <div class="scene" data-s="4" data-in="left">''' + head(230, [('h1', 'PAR CONTRE…', '4.0'), ('it gold', 'pas de prime en argent', '4.1')]).replace('class="it gold"', 'class="it gold" style="font-size:62px"') + '''
   <div class="col" style="left:110px" data-g="4.1" data-fx="up"><div class="k">PARRAIN</div><div class="v gold">Récom-<br>pense</div><div class="d">selon l'offre<br>en cours</div></div>
   <div class="col" style="left:560px;border-color:rgba(229,50,45,.8)" data-g="4.2" data-fx="up"><div class="k">FILLEUL</div><div class="v" style="color:#ff6b5e">0 €</div><div class="d">pas de prime<br>en argent</div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', 'ENVOIE-MOI', '5.0'), ('big gold', '« REVOLUT »', '5.1'), ('it gold', 'en privé.', '5.2')]).replace('class="big gold"', 'class="big gold" style="font-size:118px"') + '''
   <div class="pill" style="top:700px" data-g="5.2" data-fx="up"><div class="pin">✉</div><div><b>LE LIEN</b><span>je te l'envoie en privé</span></div></div>
   <div class="search" style="top:840px" data-g="5.3" data-fx="fade"><svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg><span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1000px">Offre soumise aux conditions en vigueur<br>récompense parrain selon l'offre en cours<br>pas de prime en argent pour le filleul</div></div>
'''
SPLITS = [(0.0, 2.07), (2.61, 4.36), (4.83, 6.87), (7.36, 9.94), (10.51, 12.42), (12.88, 14.81)]
MINLEN = 2.6
GAP = 0.4
TAIL = 2.0
