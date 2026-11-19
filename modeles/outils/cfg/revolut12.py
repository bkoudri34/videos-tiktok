import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Revolut, 19/11/2026 16:00 - style v3 nuit & or, accent orange cuivre. Format F2 « démystification » :
# question « comment ça marche vraiment ? » -> carte MYTHE / RÉALITÉ (0 € en argent pour le filleul) -> lien AVANT l'inscription
# -> checklist 3 cases (identité, carte, paiements) -> coffret du parrain « selon l'offre en cours » -> appel à l'action.
# Aucun montant : pas de prime en argent pour le filleul, récompense du parrain variable selon les campagnes, affichée dans l'appli
# (primebanque.fr, parrainage Revolut 2026, situation au 08/10/2026, consultée le 19/11/2026 ; help.revolut.com).
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'revolut12'
TITLE = 'Revolut demystification cuivre'
ROOT = ':root{--bg:#08070a}'
LINES = [
 ("Parrainage Revolut : comment ça marche, vraiment ?", [("Parrainage Revolut :", None), ("comment ça marche,", None), ("vraiment ?", None)]),
 ("Premier point : pas de prime en argent pour le filleul.", [("Premier point :", None), ("pas de prime en argent", None), ("pour le filleul.", None)]),
 ("Le lien de parrainage, c'est avant l'inscription, pas après.", [("Le lien de parrainage,", None), ("c'est avant l'inscription,", None), ("pas après.", None)]),
 ("Ensuite : identité vérifiée, carte commandée, quelques paiements.", [("Ensuite :", None), ("identité vérifiée,", None), ("carte commandée,", None), ("quelques paiements.", None)]),
 ("Le parrain, lui, est récompensé selon l'offre affichée dans l'appli.", [("Le parrain, lui,", None), ("est récompensé", None), ("selon l'offre affichée", None), ("dans l'appli.", None)]),
 ("Envoie-moi REVOLUT en privé, je t'envoie mon lien.", [("Envoie-moi", None), ("REVOLUT", None), ("en privé,", None), ("je t'envoie mon lien.", None)]),
]
MINLEN = 1.9
GAP = 0.32
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.cu{color:#ffab6b;text-shadow:0 0 18px rgba(255,140,60,.5)}
.qm{position:absolute;left:340px;top:700px;width:400px;height:560px;font:900 520px 'DejaVu Serif',serif;line-height:560px;text-align:center;color:#ff9a4d;text-shadow:0 0 60px rgba(255,140,60,.45)}
.qs{position:absolute;font:800 34px Inter;color:#f1ead9;background:rgba(40,26,16,.85);border:3px solid rgba(255,154,77,.7);border-radius:40px;padding:16px 30px;white-space:nowrap}
.myth{position:absolute;left:150px;top:720px;width:780px;height:560px;border-radius:40px;background:#f6f1ea;color:#1b1714;box-shadow:0 30px 90px rgba(0,0,0,.7);overflow:hidden}
.myth .k{height:110px;background:#2a1d14;color:#ffab6b;font:900 40px Inter;letter-spacing:8px;display:flex;align-items:center;justify-content:center}
.myth .q{font:800 46px Inter;text-align:center;margin-top:60px;white-space:nowrap}
.myth .z{font:900 170px 'DejaVu Serif',serif;text-align:center;color:#c2410c;line-height:1.1;margin-top:20px}
.myth .s{font:700 34px Inter;text-align:center;color:#5b4a3c}
.stampx{position:absolute;left:375px;top:1320px;width:330px;height:120px;border:10px solid #e2483d;border-radius:18px;color:#e2483d;font:900 64px Inter;letter-spacing:6px;display:flex;align-items:center;justify-content:center;transform:rotate(-12deg);background:rgba(20,10,8,.85)}
.flow{position:absolute;left:110px;top:760px;width:860px;height:520px}
.flow .b{position:absolute;width:360px;height:220px;border-radius:34px;background:#15100c;border:4px solid #5a4030;text-align:center;padding-top:36px}
.flow .b b{display:block;font:900 40px Inter;color:#f1ead9;letter-spacing:2px}
.flow .b span{display:block;font:700 30px Inter;color:#b9a48f;margin-top:14px}
.flow .b.on{border-color:#ff9a4d;box-shadow:0 0 50px rgba(255,154,77,.35)}
.flow .ar{position:absolute;left:375px;top:80px;width:110px;height:60px}
.flow .bad{position:absolute;left:0;top:300px;width:860px;height:150px;border-radius:30px;background:rgba(226,72,61,.12);border:4px dashed #e2483d;font:800 36px Inter;color:#ffb3ab;display:flex;align-items:center;justify-content:center;white-space:nowrap}
.chk{position:absolute;left:150px;top:740px;width:780px}
.chk .r{height:150px;border-radius:30px;background:#15100c;border:4px solid #5a4030;margin-bottom:30px;display:flex;align-items:center;gap:30px;padding:0 36px;font:800 44px Inter;color:#f1ead9;white-space:nowrap}
.chk .bx{flex:none;width:84px;height:84px;border-radius:20px;border:6px solid #ff9a4d;position:relative}
.chk .bx svg{position:absolute;left:4px;top:4px}
.chest{position:absolute;left:290px;top:800px;width:500px;height:400px}
.chest .bd{position:absolute;left:0;top:150px;width:500px;height:250px;border-radius:24px;background:linear-gradient(180deg,#5a3a22,#3a2414);border:8px solid #f3c766}
.chest .ld{position:absolute;left:-10px;top:60px;width:520px;height:110px;border-radius:60px 60px 14px 14px;background:linear-gradient(180deg,#6b4428,#4a2e1a);border:8px solid #f3c766;transform-origin:10px 100%}
.chest .lk{position:absolute;left:215px;top:140px;width:70px;height:90px;border-radius:12px;background:#f3c766}
.glow{position:absolute;left:240px;top:640px;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(255,170,90,.45),transparent 65%)}
.tag2{position:absolute;left:180px;top:1250px;width:720px;text-align:center;font:700 italic 54px 'Liberation Serif',serif;color:#ffab6b;white-space:nowrap}
'''
CHECK = '<svg width="64" height="64" viewBox="0 0 100 100"><path d="M18 52 L42 76 L84 26" stroke="#ff9a4d" stroke-width="16" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW = '<svg class="ar" viewBox="0 0 110 60" width="110" height="60"><path d="M5 30 H85" stroke="#ff9a4d" stroke-width="10" stroke-linecap="round"/><path d="M70 10 L100 30 L70 50" fill="none" stroke="#ff9a4d" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'


def row(txt, g):
    return f'<div class="r" data-g="{g}" data-fx="left"><div class="bx"><span data-g="{g}" data-fx="stamp">{CHECK}</span></div>{txt}</div>'


BODY = hud('FRANCE · LE VRAI DU FAUX', 'REVOLUT') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(215, [('h1 cu', 'PARRAINAGE REVOLUT :', None, 'font-size:74px'), ('it gold', 'comment ça marche,', None, 'font-size:84px'), ('big gold', 'vraiment ?', None, 'font-size:130px')]) + '''
   <div class="qm">?</div>
   <div class="qs" style="left:110px;top:820px;transform:rotate(-6deg)">prime pour moi ?</div>
   <div class="qs" style="left:640px;top:980px;transform:rotate(5deg)">le lien, quand ?</div>
   <div class="qs" style="left:150px;top:1200px;transform:rotate(3deg)">et le parrain ?</div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1 cu', 'PREMIER POINT :', '1.0', ''), ('it gold', 'pas de prime en argent', '1.1', 'font-size:70px'), ('it gold', 'pour le filleul.', '1.2', 'font-size:70px')]) + '''
   <div class="myth" data-g="1.0" data-fx="pop"><div class="k">LE FILLEUL REÇOIT…</div><div class="q">une prime en argent ?</div><div class="z">0 €</div><div class="s">pas de prime en argent</div></div>
   <div class="stampx" data-g="1.1" data-fx="stamp">NON</div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1', 'LE LIEN DE PARRAINAGE,', '2.0', 'font-size:66px'), ("it gold", "c'est avant l'inscription,", '2.1', 'font-size:70px'), ('h1 cu', 'PAS APRÈS.', '2.2', '')]) + '''
   <div class="flow"><div class="b on" style="left:0;top:0" data-g="2.0" data-fx="pop"><b>1. LE LIEN</b><span>tu cliques d'abord</span></div>
    <span data-g="2.1" data-fx="fade">''' + ARROW + '''</span>
    <div class="b on" style="left:500px;top:0" data-g="2.1" data-fx="pop"><b>2. INSCRIPTION</b><span>dans l'appli</span></div>
    <div class="bad" data-g="2.2" data-fx="up">✕ inscrit sans lien = parrainage perdu</div></div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('h1 cu', 'ENSUITE :', '3.0', ''), ('it gold', 'les étapes à valider', '3.0', 'font-size:66px')]) + '''
   <div class="chk">''' + row('identité vérifiée', '3.1') + row('carte commandée', '3.2') + row('quelques paiements', '3.3') + '''</div>
   <div class="cond" style="top:1310px;font-size:28px">nombre de paiements et délai : selon la campagne en cours</div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="glow" data-g="4.1" data-fx="fade"></div>''' + hd(230, [('h1 cu', 'LE PARRAIN, LUI,', '4.0', ''), ('it gold', 'est récompensé', '4.1', 'font-size:74px')]) + '''
   <div class="chest" data-g="4.1" data-fx="stamp" data-slow="4.1"><div class="bd"></div><div class="ld"></div><div class="lk"></div></div>
   <div class="tag2" data-g="4.2" data-fx="up">selon l'offre affichée dans l'appli</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« REVOLUT »', '5.1', 'font-size:118px'), ('it gold', 'en privé,', '5.2', '')]) + '''
   <div class="pill" style="top:760px;border-color:rgba(255,154,77,.8)" data-g="5.3" data-fx="up"><div class="pin" style="background:#ff9a4d">✉</div><div><b>JE T'ENVOIE MON LIEN</b><span>directement en message privé</span></div></div>
   <div class="search" style="top:900px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1040px">Offre soumise aux conditions en vigueur<br>pas de prime en argent pour le filleul<br>récompense du parrain selon l'offre en cours (affichée dans l'appli)</div></div>
'''
