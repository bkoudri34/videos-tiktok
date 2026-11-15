import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Revolut, 15/11/2026 21:00 - style v3 nuit & or, accent vert lime. Format « question / réponse », sans montant :
# pas de prime en argent pour le filleul, récompense du parrain selon l'offre en cours (variable selon les campagnes,
# affichée dans l'appli ; primebanque.fr, parrainage Revolut 2026, consultée le 15/11/2026).
# Voix : Speko (speechify, voix par défaut ; voix clonée refusée 402).
# Document « petites lignes » + loupe -> bulle question -> tampon NON -> boîte cadeau parrain -> appli + carte -> 3 étapes -> appel à l'action.
NAME = 'revolut10'
TITLE = 'Revolut question lime'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Parrainage Revolut : ce que personne ne te précise.", [("Parrainage Revolut :", None), ("ce que personne", None), ("ne te précise.", None)]),
 ("Le filleul touche de l'argent ?", [("Le filleul", None), ("touche de l'argent ?", None)]),
 ("Non. Pas de prime en argent pour lui.", [("Non.", None), ("Pas de prime en argent", None), ("pour lui.", None)]),
 ("Le parrain, lui, a une récompense, selon l'offre en cours.", [("Le parrain, lui,", None), ("a une récompense,", None), ("selon l'offre en cours.", None)]),
 ("Toi, tu gagnes une appli et une carte, sans passer en agence.", [("Toi, tu gagnes", None), ("une appli et une carte,", None), ("sans passer en agence.", None)]),
 ("Une pièce d'identité, un selfie, et c'est parti.", [("Une pièce d'identité,", None), ("un selfie,", None), ("et c'est parti.", None)]),
 ("Envoie-moi REVOLUT en privé, je t'envoie mon lien.", [("Envoie-moi", None), ("REVOLUT", None), ("en privé,", None), ("je t'envoie mon lien.", None)]),
]
SPLITS = [(0.0, 2.74), (3.16, 4.16), (4.66, 6.20), (6.60, 8.82), (9.33, 11.63), (12.07, 14.14), (14.61, 16.67)]
GSTART = [[0.1, 1.3, 2.1], [3.16, 3.6], [4.7, 5.2, 5.9], [6.7, 7.3, 8.1], [9.33, 9.8, 10.8], [12.07, 13.0, 13.7], [14.8, 15.2, 15.6, 16.1]]
MINLEN = 1.9
GAP = 0.34
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.li{color:#b8f25a;text-shadow:0 0 18px rgba(184,242,90,.4)}
.doc{position:absolute;left:230px;top:820px;width:520px;height:620px;border-radius:18px;background:#f1efe8;box-shadow:0 40px 100px rgba(0,0,0,.7);transform:rotate(-5deg);padding:50px 46px;box-sizing:border-box}
.doc .t{font:800 30px 'DejaVu Sans Mono',monospace;letter-spacing:5px;color:#1d2410;margin-bottom:28px}
.doc i{display:block;height:14px;border-radius:7px;background:#c9c6bb;margin:20px 0}
.doc i.s{width:60%;height:10px;background:#d8d5cb}
.lp{position:absolute;left:560px;top:1060px;width:260px;height:260px;border-radius:50%;border:16px solid #b8f25a;background:rgba(184,242,90,.10);box-shadow:0 20px 60px rgba(0,0,0,.6)}
.lp:after{content:'';position:absolute;left:210px;top:220px;width:36px;height:140px;border-radius:18px;background:#b8f25a;transform:rotate(-45deg);transform-origin:18px 0}
.bb{position:absolute;max-width:760px;padding:34px 44px;border-radius:44px;font:800 52px Inter;white-space:nowrap;box-shadow:0 26px 70px rgba(0,0,0,.6)}
.bb.q{left:130px;background:#2a2f24;color:#f3f6ee;border-bottom-left-radius:10px}
.bb.a{right:170px;background:#b8f25a;color:#18200b;border-bottom-right-radius:10px}
.bb small{display:block;font:700 24px Inter;letter-spacing:3px;opacity:.65;margin-bottom:8px}
.stp{position:absolute;left:0;width:1080px;text-align:center;font:900 230px Inter;color:#b8f25a;letter-spacing:6px;text-shadow:0 0 30px rgba(184,242,90,.45)}
.gift{position:absolute;left:340px;top:820px;width:400px;height:420px}
.gift .bx{position:absolute;left:20px;top:140px;width:360px;height:280px;border-radius:14px;background:linear-gradient(160deg,#2b3320,#12160c);border:5px solid #d9a24c}
.gift .ld{position:absolute;left:0;top:80px;width:400px;height:80px;border-radius:12px;background:linear-gradient(160deg,#36402a,#1a2010);border:5px solid #d9a24c}
.gift .rv{position:absolute;left:175px;top:80px;width:50px;height:340px;background:#b8f25a}
.gift .bw{position:absolute;left:120px;top:10px;width:160px;height:80px}
.gift .bw:before,.gift .bw:after{content:'';position:absolute;top:0;width:70px;height:70px;border:14px solid #b8f25a;border-radius:50% 50% 10% 50%}
.gift .bw:before{left:0;transform:rotate(-20deg)}.gift .bw:after{right:0;transform:rotate(20deg) scaleX(-1)}
.gift .q{position:absolute;left:0;top:200px;width:400px;text-align:center;font:900 120px 'DejaVu Serif',serif;color:#f3c766}
.tg{position:absolute;left:150px;top:1300px;width:780px;text-align:center}
.ph2{position:absolute;left:180px;top:720px;width:330px;height:640px;border-radius:52px;background:#0d0f0a;border:9px solid #2f3528;box-shadow:0 30px 90px rgba(0,0,0,.7);overflow:hidden;transform:rotate(-4deg)}
.ph2 .nt{width:120px;height:28px;background:#000;border-radius:0 0 16px 16px;margin:0 auto}
.ph2 .bal{margin:60px 0 0;text-align:center;font:800 26px Inter;letter-spacing:4px;color:#9fb08a}
.ph2 .row{margin:22px 26px 0;height:70px;border-radius:18px;background:#1c2116;display:flex;align-items:center;gap:16px;padding:0 18px;font:700 26px Inter;color:#e9f0dc}
.ph2 .row i{width:40px;height:40px;border-radius:12px;background:#b8f25a;font-style:normal}
.cd{position:absolute;left:520px;top:900px;width:420px;height:265px;border-radius:24px;background:linear-gradient(135deg,#d6ff94,#b8f25a 45%,#7fb22c);box-shadow:0 30px 80px rgba(0,0,0,.65);transform:rotate(8deg);color:#18200b}
.cd .chip{position:absolute;left:36px;top:90px;width:70px;height:54px;border-radius:10px;background:linear-gradient(135deg,#fff1c4,#d9a24c)}
.cd .k{position:absolute;left:36px;top:30px;font:800 22px 'DejaVu Sans Mono',monospace;letter-spacing:5px}
.cd .n{position:absolute;left:36px;top:190px;font:700 26px 'DejaVu Sans Mono',monospace;letter-spacing:3px}
.ag{position:absolute;left:0;top:1420px;width:1080px;text-align:center;font:800 34px Inter;letter-spacing:4px;color:#e9e4da}
.ag s{color:#ff6a6a;text-decoration-thickness:5px}
.st3{position:absolute;left:90px;top:820px;width:840px;display:flex;justify-content:space-between}
.st3 .c{width:250px;text-align:center}
.st3 .o{width:200px;height:200px;margin:0 auto;border-radius:50%;border:6px solid #b8f25a;background:#141a0c;display:flex;align-items:center;justify-content:center}
.st3 .c b{display:block;margin-top:22px;font:800 34px Inter;color:#f1ead9;white-space:nowrap}
.ln3{position:absolute;left:215px;top:916px;width:590px;height:8px;background:linear-gradient(90deg,#b8f25a,#f3c766);transform-origin:0 50%}
'''
ID = '<svg width="120" height="88" viewBox="0 0 110 80"><rect x="2" y="2" width="106" height="76" rx="10" fill="#eaf7d2" stroke="#4d6a1c" stroke-width="4"/><circle cx="32" cy="34" r="13" fill="#4d6a1c"/><rect x="14" y="52" width="36" height="14" rx="7" fill="#4d6a1c"/><rect x="60" y="24" width="38" height="8" rx="4" fill="#4d6a1c"/><rect x="60" y="40" width="30" height="8" rx="4" fill="#9ccf4a"/><rect x="60" y="56" width="34" height="8" rx="4" fill="#9ccf4a"/></svg>'
SELF = '<svg width="86" height="118" viewBox="0 0 80 110"><rect x="4" y="2" width="72" height="106" rx="14" fill="#2a3120"/><circle cx="40" cy="46" r="18" fill="#f3c9a2"/><path d="M16 90 Q40 62 64 90 Z" fill="#b8f25a"/><circle cx="40" cy="12" r="4" fill="#b8f25a"/></svg>'
OK = '<svg width="110" height="110" viewBox="0 0 100 100"><path d="M20 52 L42 74 L82 28" stroke="#b8f25a" stroke-width="14" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'

BODY = hud('FRANCE · SANS AGENCE', 'QUESTION / RÉPONSE') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('h1 li', 'PARRAINAGE REVOLUT :', None, 'font-size:68px'), ('it gold', 'ce que personne', None, 'font-size:80px'), ('it gold', 'ne te précise.', None, 'font-size:80px')]) + '''
   <div class="doc"><div class="t">CONDITIONS</div><i></i><i class="s"></i><i></i><i></i><i class="s"></i><i></i><i class="s"></i><i></i></div>
   <div class="lp"></div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1', 'LE FILLEUL', '1.0', 'font-size:90px'), ('it gold', "touche de l'argent ?", '1.1', 'font-size:76px')]) + '''
   <div class="bb q" style="top:800px" data-g="1.0" data-fx="left"><small>TA QUESTION</small>Le filleul touche<br>de l'argent ?</div>
   <div class="abs" style="left:700px;top:1080px;font:900 220px 'DejaVu Serif',serif;color:#f3c766" data-g="1.1" data-fx="pop">?</div></div>
  <div class="scene" data-s="2" data-in="pop">''' + hd(230, [('it gold', 'Pas de prime en argent', '2.1', 'font-size:72px;margin-top:300px'), ('it gold', 'pour lui.', '2.2', 'font-size:76px')]) + '''
   <div class="stp" style="top:250px" data-g="2.0" data-fx="stamp" data-slow="2.0">NON.</div>
   <div class="bb a" style="top:820px" data-g="2.1" data-fx="right"><small>RÉPONSE</small>Pas de prime en argent<br>pour le filleul.</div></div>
  <div class="scene" data-s="3" data-in="right">''' + hd(230, [('h1 li', 'LE PARRAIN, LUI,', '3.0', ''), ('it gold', 'a une récompense,', '3.1', 'font-size:76px')]) + '''
   <div class="gift" data-g="3.0" data-fx="up"><div class="ld"></div><div class="bx"></div><div class="rv"></div><div class="bw"></div></div>
   <div class="tg" data-g="3.2" data-fx="stamp"><div class="gold" style="font:900 italic 70px 'Liberation Serif',serif;line-height:1.15">selon l'offre en cours</div><div style="font:700 26px Inter;letter-spacing:4px;color:#9a917f;margin-top:8px">MONTANT AFFICHÉ DANS L'APPLI</div></div></div>
  <div class="scene" data-s="4" data-in="left">''' + hd(230, [('h1', 'TOI, TU GAGNES', '4.0', ''), ('it gold', 'une appli et une carte,', '4.1', 'font-size:68px'), ('it gold', 'sans passer en agence.', '4.2', 'font-size:66px')]) + '''
   <div class="ph2" data-g="4.1" data-fx="up"><div class="nt"></div><div class="bal">MON COMPTE</div><div class="row"><i></i>Carte</div><div class="row"><i></i>Virements</div><div class="row"><i></i>Épargne</div><div class="row"><i></i>Paramètres</div></div>
   <div class="cd" data-g="4.1" data-fx="right"><div class="k">MA CARTE</div><div class="chip"></div><div class="n">•••• 1511</div></div>
   <div class="ag" data-g="4.2" data-fx="fade"><s>AGENCE</s> &nbsp;→&nbsp; TOUT DANS L'APPLI</div></div>
  <div class="scene" data-s="5" data-in="up">''' + hd(230, [('h1 s', "UNE PIÈCE D'IDENTITÉ,", '5.0', ''), ('it gold', 'un selfie,', '5.1', 'font-size:80px'), ('it gold', "et c'est parti.", '5.2', 'font-size:80px')]) + '''
   <div class="ln3" data-g="5.1" data-fx="grow"></div>
   <div class="st3"><div class="c" data-g="5.0" data-fx="pop"><div class="o">''' + ID + '''</div><b>Pièce d'identité</b></div><div class="c" data-g="5.1" data-fx="pop"><div class="o">''' + SELF + '''</div><b>Selfie</b></div><div class="c" data-g="5.2" data-fx="stamp"><div class="o" style="background:#1e2a0e">''' + OK + '''</div><b>C'est parti</b></div></div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« REVOLUT »', '6.1', 'font-size:118px'), ('it gold', 'en privé,', '6.2', '')]) + '''
   <div class="pill" style="top:740px;border-color:rgba(184,242,90,.8)" data-g="6.3" data-fx="up"><div class="pin" style="background:#b8f25a">✉</div><div><b>JE T'ENVOIE MON LIEN</b><span>directement en message privé</span></div></div>
   <div class="cond" style="top:900px">Offre soumise aux conditions en vigueur<br>récompense du parrain selon l'offre en cours (affichée dans l'appli)<br>pas de prime en argent pour le filleul</div></div>
'''
