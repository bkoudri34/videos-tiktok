import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Revolut, 22/11/2026 18:00 - style v3 nuit & or, accent orange ambre. Format F5 « défi chrono » :
# chronomètre « 15 s » + accroche dès la 1re image -> 1 lien de parrainage avant l'inscription -> 2 compte ouvert + étapes de l'invitation
# -> « 0 € en argent pour le filleul » (ralenti) -> le parrain est récompensé selon l'offre de l'appli -> appel à l'action, chrono qui reboucle.
# Aucun montant : pas de prime en argent pour le filleul ; récompense du parrain selon la campagne affichée dans l'appli
# (revolut.com/fr-FR/legal/referrals-terms et help.revolut.com conditions de la campagne, consultés le 22/11/2026 ;
#  comparabanques.fr/revolut/parrainage : « le filleul ne touche aucune prime en argent »).
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'revolut14'
TITLE = 'Revolut chrono ambre'
ROOT = ':root{--bg:#0a0704}'
LINES = [
 ("Parrainage Revolut : tout comprendre en quinze secondes, chrono.", [("Parrainage Revolut :", None), ("tout comprendre", None), ("en 15 secondes,", None), ("chrono.", None)]),
 ("Un : tu passes par un lien de parrainage, avant de t'inscrire.", [("1 :", None), ("tu passes par un lien", None), ("de parrainage,", None), ("avant de t'inscrire.", None)]),
 ("Deux : tu ouvres ton compte, et tu fais les étapes de l'invitation.", [("2 :", None), ("tu ouvres ton compte,", None), ("et tu fais les étapes", None), ("de l'invitation.", None)]),
 ("Attention : le filleul ne touche pas de prime en argent.", [("Attention :", None), ("le filleul ne touche pas", None), ("de prime en argent.", None)]),
 ("C'est le parrain qui est récompensé, selon l'offre affichée dans l'appli.", [("C'est le parrain", None), ("qui est récompensé,", None), ("selon l'offre affichée", None), ("dans l'appli.", None)]),
 ("Envoie-moi REVOLUT en privé, je t'envoie mon lien.", [("Envoie-moi", None), ("REVOLUT", None), ("en privé,", None), ("je t'envoie mon lien.", None)]),
]
SPLITS = [(0.0, 3.36), (3.87, 6.62), (7.15, 10.35), (10.94, 13.30), (13.78, 15.96), (16.71, 18.85)]
GSTART = [[0.0, 1.6, 2.2, 3.1], [3.9, 4.6, 5.3, 6.0], [7.2, 8.0, 9.1, 9.8], [11.0, 11.9, 12.7], [13.8, 14.2, 14.9, 15.6], [16.7, 17.0, 17.4, 18.1]]
MINLEN = 1.9
GAP = 0.3
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.am{color:#ffad42;text-shadow:0 0 18px rgba(255,160,50,.55)}
.sw{position:absolute;left:350px;width:380px;height:380px;border-radius:50%;background:radial-gradient(circle,#2a1a08,#0d0904 70%);border:8px solid #ffad42;box-shadow:0 0 60px rgba(255,160,50,.35);display:flex;align-items:center;justify-content:center;flex-direction:column}
.sw:before{content:'';position:absolute;left:160px;top:-56px;width:44px;height:40px;border-radius:8px;background:#ffad42}
.sw b{font:900 170px 'DejaVu Serif',serif;line-height:1}
.sw span{font:800 30px Inter;letter-spacing:6px;color:#f1d9b8}
.go{position:absolute;left:390px;width:300px;height:96px;border-radius:48px;background:#ffad42;color:#1a0f02;display:flex;align-items:center;justify-content:center;font:900 44px Inter;letter-spacing:4px}
.cp{position:absolute;left:400px;top:1350px;width:280px;height:84px;border-radius:42px;background:#1a1006;border:4px solid #ffad42;display:flex;align-items:center;justify-content:center;font:900 40px 'DejaVu Sans Mono',monospace;color:#ffd9a0;white-space:nowrap}
.num{position:absolute;left:440px;width:200px;height:200px;border-radius:50%;background:#ffad42;color:#1a0f02;display:flex;align-items:center;justify-content:center;font:900 130px 'DejaVu Serif',serif;box-shadow:0 0 50px rgba(255,160,50,.45)}
.lnk{position:absolute;left:170px;width:740px;height:110px;border-radius:55px;background:#f7f2ea;color:#1a0f02;display:flex;align-items:center;gap:22px;padding:0 36px;font:700 38px Inter;white-space:nowrap}
.lnk i{font-style:normal;flex:none;width:66px;height:66px;border-radius:50%;background:#ffad42;display:flex;align-items:center;justify-content:center;font:900 34px Inter}
.chip{position:absolute;left:250px;width:580px;height:96px;border-radius:24px;display:flex;align-items:center;justify-content:center;gap:16px;font:900 36px Inter;letter-spacing:2px;white-space:nowrap}
.ok{background:#173a1f;border:4px solid #5bd47a;color:#c9f5d4}
.chk{position:absolute;left:170px;width:740px}
.chk .r{height:120px;border-radius:30px;background:#140d05;border:4px solid #6b4a1f;margin-bottom:24px;display:flex;align-items:center;gap:26px;padding:0 34px;font:800 40px Inter;color:#f7ead6;white-space:nowrap}
.chk .r .bx{flex:none;width:70px;height:70px;border-radius:16px;border:5px solid #ffad42;display:flex;align-items:center;justify-content:center;font:900 46px Inter;color:#ffad42}
.zero{position:absolute;left:0;width:1080px;text-align:center}
.zero .v{font:900 260px 'DejaVu Serif',serif;line-height:1;color:#ff6a4a;text-shadow:0 0 40px rgba(255,90,60,.5)}
.zero .s{font:800 36px Inter;letter-spacing:3px;color:#f7ead6;margin-top:10px}
.x{position:absolute;left:330px;width:420px;height:16px;border-radius:8px;background:#ff6a4a;transform:rotate(-12deg)}
.who{position:absolute;top:820px;width:360px;height:380px;border-radius:36px;text-align:center;padding:40px 20px 0}
.who .t{font:900 40px Inter;letter-spacing:3px;white-space:nowrap}
.who .ic{margin:26px auto;width:120px;height:120px;border-radius:50%;display:flex;align-items:center;justify-content:center;font:900 64px Inter}
.who .d{font:700 28px Inter;line-height:1.35}
.w1{left:130px;background:#120c06;border:4px solid #6b4a1f;color:#d8c4a6}.w1 .ic{background:#2a1d0e;color:#d8c4a6}
.w2{left:550px;background:linear-gradient(180deg,#2a1a08,#120b03);border:5px solid #ffad42;color:#ffe3bd;box-shadow:0 0 50px rgba(255,160,50,.3)}.w2 .ic{background:#ffad42;color:#1a0f02}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'


def cp(v, g):
    return f'<div class="cp" data-g="{g}" data-fx="pop">⏱ {v}</div>'


BODY = hud('FRANCE · DÉFI CHRONO', 'REVOLUT') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(205, [('h1', 'PARRAINAGE', None, 'font-size:72px'), ('h1 am', 'REVOLUT :', None, 'font-size:88px'), ('it gold', 'tout comprendre', None, 'font-size:70px'), ('it gold', 'en 15 s, chrono', None, 'font-size:70px')]) + '''
   <div class="rays" style="top:700px"></div>
   <div class="sw" style="top:760px"><b class="gold">15</b><span>SECONDES</span></div>
   <div class="go" style="top:1210px" data-g="0.3" data-fx="stamp">GO ▶</div></div>
  <div class="scene" data-s="1" data-in="right">''' + hd(220, [('h1 am', '1 :', '1.0', 'font-size:80px'), ('it gold', 'tu passes par un lien', '1.1', 'font-size:68px'), ('it gold', 'de parrainage,', '1.2', 'font-size:68px')]) + '''
   <div class="lnk" style="top:760px" data-g="1.1" data-fx="left"><i>🔗</i>lien de parrainage</div>
   <div class="chip ok" style="top:930px" data-g="1.3" data-fx="stamp">✓ AVANT L'INSCRIPTION</div>
   <div class="hd" style="top:1070px"><div class="it am" style="font-size:60px" data-g="1.3" data-fx="tw">avant de t'inscrire.</div></div>
   ''' + cp('15 s', '1.0') + '''</div>
  <div class="scene" data-s="2" data-in="left">''' + hd(220, [('h1 am', '2 :', '2.0', 'font-size:80px'), ('it gold', 'tu ouvres ton compte,', '2.1', 'font-size:68px'), ('it gold', 'et tu fais les étapes', '2.2', 'font-size:68px'), ('it am', "de l'invitation.", '2.3', 'font-size:68px')]) + '''
   <div class="chk" style="top:760px"><div class="r" data-g="2.1" data-fx="left"><div class="bx" data-g="2.1" data-fx="tick">✓</div>Compte ouvert</div><div class="r" data-g="2.2" data-fx="left"><div class="bx" data-g="2.3" data-fx="tick">✓</div>Étapes de l'invitation</div></div>
   <div class="cond" style="top:1080px;font-size:26px;color:#b89c78" data-g="2.3" data-fx="fade">dans les délais indiqués dans l'invitation</div>
   ''' + cp('10 s', '2.0') + '''</div>
  <div class="scene" data-s="3" data-in="pop">''' + hd(215, [('h1 am', 'ATTENTION :', '3.0', 'font-size:80px'), ('it gold', 'le filleul ne touche pas', '3.1', 'font-size:66px')]) + '''
   <div class="zero" style="top:560px" data-g="3.2" data-fx="stamp" data-slow="3.2"><div class="v">0 €</div><div class="s">DE PRIME EN ARGENT</div></div>
   <div class="hd" style="top:930px"><div class="it gold" style="font-size:66px" data-g="3.2" data-fx="tw">de prime en argent.</div></div>
   <div class="cond" style="top:1060px;font-size:26px;color:#b89c78" data-g="3.2" data-fx="fade">côté filleul : le compte et l'appli, pas de prime en argent</div>
   ''' + cp('6 s', '3.0') + '''</div>
  <div class="scene" data-s="4" data-in="right">''' + hd(220, [('it gold', "C'est le parrain", '4.0', 'font-size:72px'), ('h1 am', 'QUI EST RÉCOMPENSÉ,', '4.1', 'font-size:58px'), ('it gold', "selon l'offre affichée", '4.2', 'font-size:64px'), ('it gold', "dans l'appli.", '4.3', 'font-size:64px')]) + '''
   <div class="who w1" style="top:840px" data-g="4.0" data-fx="left"><div class="t">FILLEUL</div><div class="ic">0 €</div><div class="d">compte + appli</div></div>
   <div class="who w2" style="top:840px" data-g="4.1" data-fx="stamp"><div class="t">PARRAIN</div><div class="ic">🎁</div><div class="d">récompense selon<br>la campagne</div></div>
   ''' + cp('0 s ✓', '4.3') + '''</div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« REVOLUT »', '5.1', 'font-size:92px'), ('it am', 'en privé,', '5.2', '')]) + '''
   <div class="pill" style="top:650px;border-color:rgba(255,173,66,.85)" data-g="5.3" data-fx="up"><div class="pin" style="background:#ffad42;color:#1a0f02">✉</div><div><b>JE T'ENVOIE MON LIEN</b><span>directement en message privé</span></div></div>
   <div class="search" style="top:790px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:920px;font-size:22px">Offre soumise aux conditions en vigueur<br>Pas de prime en argent pour le filleul · nouveaux clients<br>Récompense du parrain selon la campagne affichée dans l'appli<br>(étapes et délais indiqués dans l'invitation)</div>
   <div class="sw" style="top:1110px;left:440px;width:200px;height:200px;border-width:6px" data-g="5.3" data-fx="pop"><b class="gold" style="font-size:90px">15</b></div></div>
'''
