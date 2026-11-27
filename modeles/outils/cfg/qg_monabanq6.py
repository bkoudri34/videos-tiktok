import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qg_collage import *
# Vidéos QG, 27/11/2026, vidéo 1 : Monabanq. Format F18 « Parraine à ton tour » (1re F18 en QG), règles anti-bannissement du 26/11 :
# AUCUN montant écrit (ni à l'écran, ni dans les sous-titres), bandeau de mentions permanent, un seul niveau (toi -> tes amis).
# Style C « Collage POV en papier découpé », variante bleu ciel, personnage « toi » à couronne de papier.
# Offre vérifiée le 27/11/2026 sur monabanq.com/fr/parrainage.html (mentions légales, renvoi 1, offre valable depuis le 16/11/2026) :
# parrain jusqu'à 50 € par filleul (50 € Uniq+, 30 € Pratiq+ ou Uniq), versés 60 jours après l'ouverture si le compte du filleul
# est toujours ouvert, dans la limite de 5 parrainages par année glissante. Total oral (règle 6) : 50 € x 5 = 250 € par an au maximum.
# Pas de date de fin annoncée. Filleul : jusqu'à 280 € (renvoi 2), non dit dans cette vidéo.
# Relance changée après le gardien (« Tu parraines qui ? » trop proche du F18 BoursoBank du 26/11).
# Voix : Inworld « Mathieu » (inworld-tts-2), une synthèse par réplique, pauses internes ramenées à 0,2 s, atempo 0.94-1.0.
NAME = 'qg_monabanq6'
TITLE = 'QG Monabanq parraine a ton tour'
ROOT = root(BG_SKY)
LINES = [
 ("Parrainage Monabanque : et si c'était toi, le parrain ?", [("<em>Parrainage</em>", None), ("<em>Monabanq</em> :", None), ("et si c'était <i>toi</i>,", None), ("le parrain ?", None)]),
 ("Je te parraine, tu ouvres ton compte et tu remplis les conditions.", [("Je te parraine,", None), ("tu ouvres", None), ("ton compte", None), ("et tu remplis", None), ("les <em>conditions</em>.", None)]),
 ("Une fois client, tu invites tes amis : une prime par ami.", [("Une fois <em>client</em>,", None), ("tu invites", None), ("tes amis :", None), ("une prime", None), ("<i>par ami</i>.", None)]),
 ("Au maximum, jusqu'à 250 € par an, plafond fixé par la banque, seulement si chacun de tes amis remplit les conditions : ce n'est pas garanti.",
  [("Au <em>maximum</em>,", None), ("<em>par an</em>,", "jusqu'à deux cent cinquante euros par an,"), ("<em>plafond</em> fixé", None), ("par la banque,", None),
   ("seulement si", None), ("<i>chacun</i> de tes amis", None), ("remplit", None), ("les conditions :", None), ("ce n'est <em>pas</em>", None), ("<em>garanti</em>.", None)]),
 ("Et moi, je ne touche rien sur les amis de mes filleuls.", [("Et moi,", None), ("je ne touche", None), ("<em>rien</em>", None), ("sur les amis", None), ("de mes filleuls.", None)]),
 ("Qui serait ton premier filleul ? Dis-le en commentaire.", [("Qui serait", None), ("ton 1er <em>filleul ?</em>", None), ("Dis-le en", None), ("<i>commentaire</i>.", None)]),
 ("Si tu veux que je te parraine, écris-moi en privé.", [("Si tu veux", None), ("que je te parraine,", None), ("écris-moi", None), ("en <em>privé</em>.", None)]),
]
SPLITS = [(0.2, 2.688), (3.008, 6.416), (6.736, 9.644), (9.964, 17.523), (17.843, 20.665), (20.985, 23.626), (23.946, 26.478)]
GAP = 0.2
TAIL = 1.1
MINLEN = 1.0
JS = STOP_JS


def crown(x, y, s=1.0, g=None):
    a = f' data-g="{g}" data-fx="pop"' if g else ''
    return (f'<svg class="pp" style="left:{x}px;top:{y}px" width="{int(120*s)}" height="{int(80*s)}" viewBox="0 0 120 80"{a}>'
            '<path d="M6 74 L12 18 L38 46 L60 6 L82 46 L108 18 L114 74 Z" fill="#ffd84a" stroke="#1b1a17" stroke-width="5" stroke-linejoin="round"/>'
            '<circle cx="60" cy="58" r="8" fill="#e2452f"/></svg>')


def strip(x, y, w, rot):
    return f'<div class="pp strip" style="left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg)"></div>'


CSS = '''
.ment{position:absolute;left:150px;top:206px;width:760px;padding:10px 18px 12px;border-radius:14px;background:#1b1a17;text-align:center;z-index:8;line-height:1.28;
 filter:drop-shadow(6px 8px 0 rgba(40,25,0,.25))}
.ment b{display:block;font:800 27px 'Inter',sans-serif;color:#fff;white-space:nowrap}
.ment span{display:block;font:700 23px 'Inter',sans-serif;color:#ffd84a;white-space:nowrap}
.kw{top:305px;font-size:76px}
.note{position:absolute;padding:16px 24px;font:800 34px/1.3 'Inter',sans-serif;color:#1b1a17;background:#fbf7ee;border-radius:8px;white-space:nowrap}
.note .ck{display:inline-block;width:44px;height:44px;margin-right:14px;border-radius:50%;background:#2e9e5b;color:#fff;text-align:center;font:900 30px/44px 'Inter',sans-serif;vertical-align:-4px}
.env{position:absolute;width:300px;height:200px;background:#fbf7ee;border-radius:8px}
.env:before{content:'';position:absolute;left:0;top:0;border-left:150px solid transparent;border-right:150px solid transparent;border-top:110px solid #e9dcc2}
.env .w{position:absolute;left:0;right:0;bottom:22px;text-align:center;font:400 38px 'Anton',sans-serif;color:#e2452f;letter-spacing:2px}
.strip{position:absolute;height:16px;background:#1b1a17;border-radius:4px;transform-origin:0 50%}
.pill{position:absolute;padding:14px 30px;border-radius:40px;background:#1b1a17;color:#ffd84a;font:800 38px 'Inter',sans-serif;white-space:nowrap}
.bub{font-size:52px}
'''

BANNER = '<div class="ment"><b>Lien de parrainage : je touche une prime</b><span>Offre soumise à conditions</span></div>'

BODY = BANNER + '''
  <div class="scene" data-s="0">
   <div class="kw">Parrainage <b>Monabanq</b></div>
''' + lab(150, 455, -3, "ET SI C'ÉTAIT TOI", 'dark', size=92) + lab(270, 590, 4, 'LE PARRAIN ?', 'red', size=100) + \
    perso(395, 800, 1.35, '#2f6fe2', 'open', 'up', look=0, jump=True) + crown(458, 742, 1.2) + lab(90, 1150, -6, 'TOI', 'blue', g='0.2', fx='pop', size=70) + '''
  </div>
  <div class="scene" data-s="1" data-in="right">
''' + lab(110, 320, -2, '1 · JE TE PARRAINE', 'dark', g='1.0', fx='pop', size=80) + \
    perso(90, 560, 1.0, '#2e9e5b', 'smile', 'point', look=1) + perso(700, 560, 1.0, '#2f6fe2', 'o', 'down', look=-1) + '''
   <div class="abs" style="left:380px;top:640px" data-g="1.0" data-fx="right"><div class="pp env" style="transform:rotate(-6deg)"><div class="w">INVITATION</div></div></div>
''' + lab(110, 940, 2, '2 · TU REMPLIS LES CONDITIONS', 'red', g='1.3', fx='pop', size=62) + '''
   <div class="abs" style="left:150px;top:1060px" data-g="1.2" data-fx="up"><div class="pp note" style="transform:rotate(-1deg)"><span class="ck">✓</span>compte ouvert</div></div>
   <div class="abs" style="left:520px;top:1080px" data-g="1.4" data-fx="up"><div class="pp note" style="transform:rotate(2deg)"><span class="ck">✓</span>conditions</div></div>
  </div>
  <div class="scene" data-s="2" data-in="left">
''' + lab(90, 320, 2, '3 · UNE FOIS CLIENT', 'dark', g='2.0', fx='pop', size=80) + \
    strip(520, 780, 270, -30) + strip(520, 820, 270, 0) + strip(520, 860, 270, 30) + \
    perso(230, 600, 1.3, '#2f6fe2', 'smile', 'pointl', look=1) + crown(300, 535, 1.2) + \
    perso(800, 520, 0.6, '#e2452f', 'smile', 'down', look=-1, g='2.1') + perso(840, 700, 0.6, '#2e9e5b', 'smile', 'down', look=-1, g='2.2') + perso(800, 880, 0.6, '#ff8fb1', 'smile', 'down', look=-1, g='2.3') + \
    lab(110, 1060, -3, '4 · TES AMIS', 'blue', g='2.2', fx='pop', size=72) + lab(430, 1170, 3, 'UNE PRIME PAR AMI ✓', 'green', g='2.3', fx='stamp', size=56) + '''
  </div>
  <div class="scene" data-s="3" data-in="up">
''' + lab(90, 320, -2, 'AU MAXIMUM', 'dark', g='3.0', fx='pop', size=96) + \
    lab(110, 470, 2, 'PLAFOND FIXÉ', 'red', g='3.2', fx='stamp', size=104) + lab(300, 610, -2, 'PAR LA BANQUE', 'red', g='3.3', fx='pop', size=84) + '''
   <div class="abs" style="left:100px;top:790px" data-g="3.5" data-fx="up"><div class="pp note" style="transform:rotate(-1deg);font-size:31px">seulement si <b>chacun</b> de tes amis<br>remplit les conditions</div></div>
''' + lab(110, 1060, -4, "CE N'EST PAS GARANTI", 'dark', g='3.8', fx='stamp', size=76) + \
    perso(745, 790, 0.92, '#2f6fe2', 'flat', 'hip', look=-1) + crown(797, 740, 0.85) + '''
  </div>
  <div class="scene" data-s="4" data-in="pop">
''' + lab(140, 320, 3, 'UN SEUL NIVEAU', 'dark', g='4.0', fx='pop', size=110) + \
    lab(120, 560, -3, 'TOI', 'blue', g='4.0', fx='pop', size=96) + strip(330, 615, 200, 0) + lab(560, 560, 2, 'TES AMIS', 'green', g='4.1', fx='pop', size=96) + '''
   <div class="abs" style="left:110px;top:760px" data-g="4.2" data-fx="up"><div class="pp note" style="transform:rotate(1deg)">moi, je ne touche <b>rien</b><br>sur les amis de mes filleuls</div></div>
''' + perso(640, 930, 1.1, '#2e9e5b', 'flat', 'shrug', look=-1) + '''
  </div>
  <div class="scene" data-s="5" data-in="pop">
''' + lab(120, 360, -3, 'TON 1ER FILLEUL ?', 'dark', g='5.0', fx='stamp', size=100) + '''
   <div class="abs" style="left:190px;top:560px" data-g="5.2" data-fx="pop"><div class="pp pill">💬 dis-le en commentaire</div></div>
''' + perso(130, 760, 1.25, '#2f6fe2', 'open', 'point', look=1) + crown(200, 690, 1.2) + perso(540, 860, 0.95, '#e2452f', 'o', 'down', look=-1) + perso(740, 880, 0.9, '#ff8fb1', 'smile', 'down', look=-1) + '''
  </div>
  <div class="scene" data-s="6" data-in="pop">
   <div class="abs" style="left:90px;top:340px" data-g="6.0" data-fx="left"><div class="pp bub you">Tu peux me parrainer ?</div></div>
   <div class="abs" style="left:290px;top:490px" data-g="6.2" data-fx="right"><div class="pp bub me">Oui, écris-moi en privé 🤝</div></div>
   <div class="abs" style="left:150px;top:650px" data-g="6.3" data-fx="pop"><div class="pp pill" style="font-size:32px">⏳ offre Monabanq en cours (vérifiée le 27/11)</div></div>
''' + perso(700, 780, 0.9, '#2f6fe2', 'smile', 'wave', look=-1, wave=True) + crown(752, 730, 0.9) + '''
   <div class="mention" style="top:1110px;width:600px;z-index:3">Offre soumise aux conditions en vigueur. Parrainage Monabanq : une prime par filleul dont le compte est toujours ouvert 60 jours après l'ouverture, dans la limite de 5 filleuls par année glissante (plafond fixé par la banque). Lien de parrainage : je touche une prime.</div>
  </div>
'''
