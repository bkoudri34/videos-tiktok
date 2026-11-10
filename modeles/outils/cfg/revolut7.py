import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Revolut, 10/11/2026 21:00 - style v3 nuit & or, accent rouge corail. Pas de montant (récompense parrain selon l'offre en cours, pas de prime en argent pour le filleul).
# Ticket d'attente barré -> téléphone -> emblème parrain -> amis inscrits -> carte « filleul » tamponnée -> appel à l'action.
NAME = 'revolut7'
TITLE = 'Revolut parrain corail'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Pas d'agence, pas de rendez-vous : juste ton téléphone.", [("Pas d'agence,", None), ("pas de rendez-vous :", None), ("juste ton téléphone.", None)]),
 ("Revolut, tu l'ouvres directement depuis l'appli.", [("Revolut,", None), ("tu l'ouvres directement", None), ("depuis l'appli.", None)]),
 ("Et ensuite, c'est toi qui deviens parrain.", [("Et ensuite,", None), ("c'est toi qui deviens parrain.", None)]),
 ("Tes amis s'inscrivent avec ton lien : une récompense selon l'offre en cours.", [("Tes amis s'inscrivent", None), ("une récompense", None), ("selon l'offre en cours.", None)]),
 ("Pour eux, pas de prime en argent. Soyons clairs.", [("Pour eux,", None), ("pas de prime en argent.", None), ("Soyons clairs.", None)]),
 ("Envoie-moi REVOLUT en privé, je t'envoie le lien.", [("Envoie-moi", None), ("REVOLUT", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 2.442), (3.015, 5.215), (5.721, 7.284), (7.785, 10.971), (11.465, 13.573), (14.082, 16.327)]
GSTART = [[0.1, 0.8, 1.7], [3.02, 3.7, 4.6], [5.73, 6.4], [7.79, 9.4, 10.1], [11.47, 11.9, 13.0], [14.09, 14.5, 15.0, 15.6]]
MINLEN = 2.4
GAP = 0.4
TAIL = 2.0
CSS = '''
.co{color:#ff6b78;text-shadow:0 0 18px rgba(255,95,109,.45)}
.tkt{position:absolute;left:300px;top:760px;width:480px;height:460px;background:#f4efe4;color:#1c1712;text-align:center;border-radius:14px;box-shadow:0 40px 90px rgba(0,0,0,.7);transform:rotate(-5deg);padding-top:44px}
.tkt .k{font:800 30px Inter;letter-spacing:5px;color:#6b5f4f}
.tkt .n{font:900 170px 'DejaVu Sans Mono',monospace;line-height:1.2}
.tkt .w{font:700 28px Inter;letter-spacing:2px;color:#6b5f4f}
.xl{position:absolute;left:250px;top:970px;width:580px;height:16px;border-radius:8px;background:#ff5f6d;box-shadow:0 0 30px rgba(255,95,109,.6);transform-origin:0 50%}
.av{position:absolute;width:140px;height:140px;border-radius:50%;border:4px solid #d9a24c;display:flex;align-items:center;justify-content:center;font:900 52px Inter;color:#fff;box-shadow:0 0 30px rgba(240,180,80,.3)}
.av small{position:absolute;bottom:-44px;left:-30px;right:-30px;text-align:center;font:700 24px Inter;color:#e9e4da}
.card{position:absolute;left:190px;top:700px;width:700px;height:470px;border-radius:30px;background:#f4efe4;color:#1c1712;padding:44px 50px;box-shadow:0 40px 90px rgba(0,0,0,.7);transform:rotate(2deg)}
.card .k{font:900 40px Inter;letter-spacing:6px}
.card .l{height:16px;border-radius:8px;background:#ddd3c2;margin-top:30px}
.stp{position:absolute;left:230px;top:880px;width:620px;padding:24px 10px;border:8px solid #e0404f;border-radius:20px;color:#e0404f;text-align:center;font:900 50px Inter;letter-spacing:2px;line-height:1.15;transform:rotate(-8deg);background:rgba(244,239,228,.85)}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
BODY = hud('FRANCE · SANS AGENCE', 'PARRAINAGE') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + head(230, [('h1', "PAS D'AGENCE,", None), ('h1 s', 'PAS DE RENDEZ-VOUS :', None), ('it gold', 'juste ton téléphone.', None)]).replace('class="it gold"', 'class="it gold" style="font-size:72px"') + '''
   <div class="tkt"><div class="k">TICKET D'ATTENTE</div><div class="n">047</div><div class="w">GUICHET · PATIENTEZ…</div></div>
   <div class="xl" data-g="0.1" data-fx="strike"></div></div>
  <div class="scene" data-s="1" data-in="pop">''' + head(230, [('h1', 'REVOLUT,', '1.0'), ('it gold', "depuis l'appli.", '1.2')]) + '''
   <div class="orb" style="left:200px;top:560px;width:680px;height:1000px"></div>
   <div class="phone" style="top:600px" data-g="1.0" data-fx="up"><div class="notch"></div>
    <div style="font:900 50px Inter;margin-top:40px">Revolut</div><div style="font:600 24px Inter;color:#aaa;margin-top:6px">Créer un compte</div>
    <div style="margin:44px 26px 0;text-align:left;font:600 30px Inter;line-height:2.3;color:#ddd">
     <div data-g="1.1" data-fx="left"><span class="co">✓</span> Téléphone</div><div data-g="1.1" data-fx="left"><span class="co">✓</span> Identité</div><div data-g="1.2" data-fx="left"><span class="co">✓</span> Selfie</div></div>
    <div style="display:inline-block;margin-top:40px;background:#ff5f6d;color:#2a0a0e;font:800 32px Inter;padding:14px 40px;border-radius:30px" data-g="1.2" data-fx="pop">C'est parti</div></div></div>
  <div class="scene" data-s="2" data-in="right"><div class="floor"></div><div class="rays" style="top:640px"></div>''' + head(230, [('h1', 'ET ENSUITE,', '2.0'), ('it gold', "c'est toi le parrain.", '2.1')]) + '''
   <div class="emb" style="top:760px" data-g="2.0" data-fx="pop"><div style="text-align:center"><div class="co" style="font:400 90px 'DejaVu Sans';line-height:1">♛</div><div class="gold" style="font:900 40px 'DejaVu Serif',serif;letter-spacing:1px">PARRAIN</div></div></div>
   <div class="abs" style="left:240px;top:1110px;width:600px;text-align:center;font:800 30px Inter;letter-spacing:5px;color:#e9e4da" data-g="2.1" data-fx="fade">C'EST TOI.</div></div>
  <div class="scene" data-s="3" data-in="left">''' + head(230, [('h1', 'TES AMIS', '3.0'), ('it gold', "s'inscrivent avec ton lien.", '3.0')]).replace('class="it gold"', 'class="it gold" style="font-size:64px"') + '''
   <div class="av" style="left:150px;top:560px;background:#7a2a33" data-g="3.0" data-fx="pop">I<small>Inès</small></div>
   <div class="av" style="left:470px;top:560px;background:#2a4a7a" data-g="3.0" data-fx="pop">Y<small>Yanis</small></div>
   <div class="av" style="left:790px;top:560px;background:#4a6a2a" data-g="3.1" data-fx="pop">C<small>Chloé</small></div>
   <div class="abs" style="left:90px;top:880px;width:900px;text-align:center" data-g="3.2" data-fx="stamp" data-slow="3.2"><div style="font:800 40px Inter;letter-spacing:5px">UNE RÉCOMPENSE</div><div class="gold" style="font:900 92px 'DejaVu Serif',serif;line-height:1.3">selon l'offre</div><div class="gold" style="font:900 92px 'DejaVu Serif',serif;line-height:1.1">en cours</div><div class="co" style="font:700 28px Inter;letter-spacing:4px;margin-top:18px">POUR TOI, LE PARRAIN</div></div></div>
  <div class="scene" data-s="4" data-in="pop">''' + head(230, [('h1', 'POUR EUX :', '4.0'), ('it gold', 'pas de prime en argent.', '4.1')]).replace('class="it gold"', 'class="it gold" style="font-size:66px"') + '''
   <div class="card" data-g="4.0" data-fx="up"><div class="k">FILLEUL</div><div class="l" style="width:90%"></div><div class="l" style="width:70%"></div><div class="l" style="width:82%"></div><div class="l" style="width:55%"></div><div class="l" style="width:76%"></div></div>
   <div class="stp" data-g="4.1" data-fx="stamp">PAS DE PRIME<br>EN ARGENT</div>
   <div class="abs" style="left:240px;top:1240px;width:600px;text-align:center;font:800 32px Inter;letter-spacing:5px;color:#e9e4da" data-g="4.2" data-fx="fade">SOYONS CLAIRS.</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', 'ENVOIE-MOI', '5.0'), ('big gold', '« REVOLUT »', '5.1'), ('it gold', 'en privé.', '5.2')]).replace('class="big gold"', 'class="big gold" style="font-size:118px"') + '''
   <div class="pill" style="top:720px" data-g="5.3" data-fx="up"><div class="pin">✉</div><div><b>LE LIEN</b><span>je te l'envoie en privé</span></div></div>
   <div class="search" style="top:860px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1010px">Offre soumise aux conditions en vigueur<br>récompense parrain selon l'offre en cours<br>pas de prime en argent pour le filleul</div></div>
'''
