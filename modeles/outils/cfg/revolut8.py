import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Revolut, 12/11/2026 18:00 - style v3 nuit & or, accent lavande. Pas de montant (récompense parrain selon l'offre en cours, pas de prime en argent pour le filleul).
# Poche + téléphone -> agence barrée -> 3 tuiles -> coffret cadeau -> colonnes parrain / filleul -> appel à l'action.
NAME = 'revolut8'
TITLE = 'Revolut poche lavande'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Une banque entière, dans ta poche.", [("Une banque entière,", None), ("dans ta poche.", None)]),
 ("Revolut, tu l'ouvres depuis l'appli, sans passer en agence.", [("Revolut,", None), ("tu l'ouvres", None), ("depuis l'appli,", None), ("sans passer en agence.", None)]),
 ("Carte, virements, épargne : tu gères tout au même endroit.", [("Carte,", None), ("virements,", None), ("épargne :", None), ("tu gères tout", None), ("au même endroit.", None)]),
 ("Et si tu parraines, une récompense pour toi, selon l'offre en cours.", [("Et si tu parraines,", None), ("une récompense", None), ("pour toi,", None), ("selon l'offre en cours.", None)]),
 ("Pour ton filleul, pas de prime en argent. On reste honnêtes.", [("Pour ton filleul,", None), ("pas de prime en argent.", None), ("On reste honnêtes.", None)]),
 ("Envoie-moi REVOLUT en privé, je t'envoie mon lien.", [("Envoie-moi", None), ("REVOLUT", None), ("en privé,", None), ("je t'envoie mon lien.", None)]),
]
SPLITS = [(0.0, 2.119), (2.594, 5.533), (5.894, 8.702), (9.099, 12.152), (12.555, 15.062), (15.581, 17.761)]
GSTART = [[0.1, 1.3], [2.6, 3.2, 3.6, 4.4], [5.9, 6.2, 6.8, 7.5, 8.2], [9.1, 10.0, 10.7, 11.2], [12.56, 13.4, 14.4], [15.59, 16.0, 16.5, 17.0]]
MINLEN = 2.3
GAP = 0.36
TAIL = 2.0
CSS = '''
.lv{color:#c4a2ff;text-shadow:0 0 18px rgba(180,140,255,.5)}
.pocket{position:absolute;left:250px;top:880px;width:580px;height:560px;background:linear-gradient(170deg,#2c3c63,#151d33);border-radius:20px 20px 260px 260px;border:4px dashed rgba(217,162,76,.7);box-shadow:0 40px 90px rgba(0,0,0,.7);overflow:hidden}
.pocket:before{content:'';position:absolute;left:-10px;top:-4px;width:600px;height:70px;background:#1d2844;border-bottom:4px dashed rgba(217,162,76,.7)}
.mph{position:absolute;left:400px;top:640px;width:280px;height:520px;border-radius:44px;background:#0d0c0b;border:8px solid #2c2925;box-shadow:0 0 0 2px #514a40,0 0 60px rgba(180,140,255,.35);text-align:center;transform:rotate(-6deg)}
.mph .scr{position:absolute;inset:30px 18px;border-radius:26px;background:linear-gradient(160deg,#3b2a66,#120c22);padding-top:70px}
.mph .scr b{display:block;font:900 34px Inter;color:#fff}.mph .scr span{display:block;margin-top:14px;font:900 60px 'DejaVu Serif',serif}
.bank{position:absolute;left:330px;top:720px;width:420px;height:420px}
.bank .roof{position:absolute;left:0;top:0;width:0;height:0;border-left:210px solid transparent;border-right:210px solid transparent;border-bottom:110px solid #6f6553}
.bank .col{position:absolute;top:130px;width:46px;height:200px;background:#8a7f69;border-radius:6px}
.bank .bs{position:absolute;left:-20px;top:340px;width:460px;height:40px;background:#6f6553;border-radius:6px}
.bank .nm{position:absolute;left:0;top:400px;width:420px;text-align:center;font:800 34px Inter;letter-spacing:8px;color:#9a917f}
.xx{position:absolute;left:280px;top:920px;width:520px;height:18px;border-radius:9px;background:#b48cff;box-shadow:0 0 30px rgba(180,140,255,.7);transform-origin:0 50%}
.app{position:absolute;left:0;top:1230px;width:1080px;text-align:center;font:800 36px Inter;letter-spacing:5px}
.tiles{position:absolute;left:150px;top:700px;width:780px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:24px}
.tl2{height:250px;border-radius:30px;border:3px solid #d9a24c;background:rgba(40,28,70,.6);text-align:center;padding-top:44px}
.tl2 .i{font:400 84px 'DejaVu Sans';line-height:1;color:#c4a2ff}
.tl2 .n{font:800 26px Inter;letter-spacing:2px;margin-top:26px;color:#e9e4da}
.one{position:absolute;left:170px;top:1030px;width:740px;height:110px;border-radius:55px;background:#b48cff;color:#170c2a;text-align:center;font:900 44px Inter;line-height:110px;letter-spacing:3px}
.gift{position:absolute;left:340px;top:760px;width:400px;height:340px;border-radius:16px;background:linear-gradient(160deg,#4a3380,#1d1236);border:4px solid #d9a24c;box-shadow:0 40px 90px rgba(0,0,0,.7),0 0 50px rgba(180,140,255,.3)}
.gift:before{content:'';position:absolute;left:175px;top:0;width:50px;height:100%;background:linear-gradient(#f3c766,#c8892c)}
.lid{position:absolute;left:320px;top:690px;width:440px;height:90px;border-radius:14px;background:linear-gradient(160deg,#5a3f99,#2a1a4d);border:4px solid #d9a24c}
.lid:before{content:'';position:absolute;left:191px;top:0;width:50px;height:100%;background:linear-gradient(#f3c766,#c8892c)}
.bow{position:absolute;left:470px;top:620px;font:400 110px 'DejaVu Sans';color:#f3c766;line-height:1}
.vs{position:absolute;top:700px;width:400px;height:520px;border-radius:30px;text-align:center;padding:40px 24px}
.vs .k{font:900 40px Inter;letter-spacing:5px}
.vs .r{margin-top:40px;font:700 italic 50px 'Liberation Serif',serif;line-height:1.25}
.nob{display:inline-block;margin-top:40px;padding:14px 26px;border:6px solid #ff6b78;border-radius:18px;color:#ff6b78;font:900 34px Inter;transform:rotate(-6deg);line-height:1.2}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
COLS = ''.join(f'<div class="col" style="left:{x}px"></div>' for x in (50, 140, 234, 324))
BODY = hud('FRANCE · DEPUIS LE CANAPÉ', 'PARRAINAGE') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + head(220, [('h1', 'UNE BANQUE ENTIÈRE,', None), ('it gold', 'dans ta poche.', None)]) + '''
   <div class="orb" style="left:240px;top:520px;width:600px;height:900px"></div>
   <div class="mph"><div class="scr"><b>Revolut</b><span class="gold">appli</span></div></div>
   <div class="pocket"></div></div>
  <div class="scene" data-s="1" data-in="right">''' + head(230, [('h1', 'REVOLUT,', '1.0'), ('it gold', "tu l'ouvres depuis l'appli,", '1.1')]).replace('class="it gold"', 'class="it gold" style="font-size:66px"') + '''
   <div class="bank"><div class="roof"></div>''' + COLS + '''<div class="bs"></div><div class="nm">AGENCE</div></div>
   <div class="xx" data-g="1.3" data-fx="strike"></div>
   <div class="app lv" data-g="1.3" data-fx="up">SANS PASSER EN AGENCE</div></div>
  <div class="scene" data-s="2" data-in="pop">''' + head(230, [('h1', 'CARTE, VIREMENTS, ÉPARGNE :', '2.0'), ('it gold', 'tu gères tout.', '2.3')]).replace('class="h1"', 'class="h1 s" style="font-size:58px"') + '''
   <div class="tiles"><div class="tl2" data-g="2.0" data-fx="pop"><div class="i">▭</div><div class="n">CARTE</div></div><div class="tl2" data-g="2.1" data-fx="pop"><div class="i">⇄</div><div class="n">VIREMENTS</div></div><div class="tl2" data-g="2.2" data-fx="pop"><div class="i">◔</div><div class="n">ÉPARGNE</div></div></div>
   <div class="one" data-g="2.4" data-fx="stamp">AU MÊME ENDROIT</div></div>
  <div class="scene" data-s="3" data-in="left"><div class="rays" style="top:600px"></div>''' + head(230, [('h1', 'SI TU PARRAINES :', '3.0'), ('it gold', 'une récompense pour toi,', '3.1')]).replace('class="it gold"', 'class="it gold" style="font-size:68px"') + '''
   <div class="gift" data-g="3.0" data-fx="up"></div><div class="lid" data-g="3.1" data-fx="up"></div><div class="bow" data-g="3.1" data-fx="pop">✿</div>
   <div class="abs" style="left:90px;top:1150px;width:900px;text-align:center" data-g="3.3" data-fx="stamp" data-slow="3.3"><div class="gold" style="font:900 84px 'DejaVu Serif',serif;line-height:1.2">selon l'offre</div><div class="gold" style="font:900 84px 'DejaVu Serif',serif;line-height:1.1">en cours</div></div></div>
  <div class="scene" data-s="4" data-in="pop">''' + head(230, [('h1', 'POUR TON FILLEUL :', '4.0'), ('it gold', 'on reste honnêtes.', '4.2')]) + '''
   <div class="vs" style="left:110px;border:3px solid #d9a24c;background:rgba(40,28,70,.5)" data-g="4.0" data-fx="left"><div class="k gold">PARRAIN</div><div class="r">récompense<br>selon l'offre<br>en cours</div></div>
   <div class="vs" style="left:570px;border:3px solid #ff6b78;background:rgba(60,14,20,.45)" data-g="4.0" data-fx="right"><div class="k" style="color:#ff8a95">FILLEUL</div><div class="nob" data-g="4.1" data-fx="stamp">PAS DE PRIME<br>EN ARGENT</div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + head(230, [('h1', 'ENVOIE-MOI', '5.0'), ('big gold', '« REVOLUT »', '5.1'), ('it gold', 'en privé.', '5.2')]).replace('class="big gold"', 'class="big gold" style="font-size:118px"') + '''
   <div class="pill" style="top:720px" data-g="5.3" data-fx="up"><div class="pin" style="background:#b48cff">✉</div><div><b>MON LIEN</b><span>je te l'envoie en privé</span></div></div>
   <div class="search" style="top:860px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1010px">Offre soumise aux conditions en vigueur<br>récompense parrain selon l'offre en cours<br>pas de prime en argent pour le filleul</div></div>
'''
