import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo import *
# Vidéos QG, 27/11/2026, vidéo 2 : BoursoBank. Format F15 « La 1re prime » (1re vidéo F15) joué par les 2 mannequins blancs :
# l'indécise saute de joie devant une carte dessinée « Prime validée ✓ » (sans montant, « prime si conditions remplies »),
# puis « et après ? » : les conditions à remplir, garder le compte, question à commenter, fausse conversation et mentions.
# Style D « Duo 3D » (Three.js r149 embarqué). Règles anti-bannissement du 26/11 : AUCUN montant écrit (écran et sous-titres),
# pas de virement ni de solde, bandeau de mentions permanent, appel à l'action unique à la fin.
# Offre vérifiée le 27/11/2026 sur boursobank.com/bon-plan/parrainage-boursobank (conditions de l'offre filleul) : du 24/11/2026 14 h
# au 01/12/2026 14 h, 1re ouverture d'un compte individuel : prime maximale de 300 € = 60 € (ouverture effective, au plus tard 2 mois)
# + 80 € (1er versement ≥ 300 €, à l'ouverture ou dans les 30 jours) + 80 € (1 opération carte par mois pendant 3 mois : 20 + 30 + 30)
# + 80 € (1re mobilité EasyMove, formulaire signé dans le mois) ; primes reprises si clôture dans les 24 mois.
# Après le gardien anti-ban (originalité) : fond aubergine 0x2b1420 au lieu du noir, bulle « Oui, avec plaisir 🤝 » (l'appel « écris-moi en privé » reste à l'oral).
# Voix : l'indécise (P) = Cartesia « Manon » (sonic-3.5, speed 1.15) ; le connaisseur (M) = Cartesia « Etienne » (sonic-3.5, speed 1.2) ;
# une synthèse par réplique, pauses internes ramenées à 0,2 s, niveaux égalisés (≈ -19 dB).
NAME = 'qg_boursorama3'
TITLE = 'QG BoursoBank premiere prime'
HEAD = THREE
LINES = [
 ("Parrainage BoursoBank : ma première prime est validée !", [("<em>Parrainage</em>", None), ("BoursoBank :", None), ("ma 1re prime", None), ("est <i>validée !</i>", None)]),
 ("Bien joué ! La prime de bienvenue va jusqu'à 300 €, si tu remplis toutes les conditions.", [("<i>Bien joué !</i>", None), ("La prime", None), ("de bienvenue", None), ("va jusqu'à…", "va jusqu'à trois cents euros,"), ("si tu remplis", None), ("<em>toutes</em>", None), ("les conditions.", None)]),
 ("Et après ? Il faut faire quoi ?", [("Et <i>après ?</i>", None), ("Il faut", None), ("faire <i>quoi ?</i>", None)]),
 ("Un premier versement de 300 €, une opération carte par mois pendant trois mois, et le changement de banque.",
  [("Un 1er <em>versement</em>", "Un premier versement de trois cents euros,"), ("une opération", None), ("<em>carte</em>", None), ("par mois", None), ("pendant 3 mois,", None), ("et le changement", None), ("de <em>banque</em>.", None)]),
 ("Et garde ton compte au moins deux ans.", [("Et <i>garde</i>", None), ("ton compte", None), ("au moins <em>2 ans</em>.", None)]),
 ("Ta première prime, tu l'as eue ? Dis-le en commentaire !", [("Ta 1re prime,", None), ("tu l'as <i>eue ?</i>", None), ("Dis-le en", None), ("<em>commentaire !</em>", None)]),
 ("Si tu veux que je te parraine, écris-moi en privé.", [("Si tu veux", None), ("que je te parraine,", None), ("écris-moi", None), ("en <i>privé</i>.", None)]),
]
SPLITS = [(0.2, 3.011), (3.331, 8.422), (8.742, 10.242), (10.562, 16.556), (16.876, 18.946), (19.266, 22.021), (22.341, 24.695)]
MINLEN = 0.9
GAP = 0.2
TAIL = 1.4
DUO_LINES = [
 {'who': 'P', 'M': 'idle', 'P': 'cool', 'shot': 'wide'},
 {'who': 'M', 'M': 'talk', 'P': 'cool', 'shot': 'M', 'lbl': False},
 {'who': 'P', 'M': 'idle', 'P': 'think', 'shot': 'P', 'lbl': False},
 {'who': 'M', 'M': 'point', 'P': 'idle', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'hip', 'P': 'idle', 'shot': 'M', 'lbl': False},
 {'who': 'P', 'M': 'idle', 'P': 'point', 'shot': 'P', 'lbl': False},
 {'who': 'M', 'M': 'talk', 'P': 'idle', 'shot': 'wide', 'lbl': False},
]
JS = duo_js(DUO_LINES, bg=0x2b1420)
ROOT = ':root{--bg:#2b1420}'

CSS = '''
#sub{left:60px;width:860px;font-size:86px}
.ment{position:absolute;left:150px;top:208px;width:760px;padding:10px 18px 12px;border-radius:18px;background:rgba(8,8,10,.85);border:2px solid rgba(255,255,255,.35);text-align:center;z-index:8;line-height:1.28}
.ment b{display:block;font:800 27px 'Inter',sans-serif;color:#fff;white-space:nowrap}
.ment span{display:block;font:700 23px 'Inter',sans-serif;color:#ffd23f;white-space:nowrap}
.hook{top:300px;font-size:74px;left:70px;width:860px}
.ok{position:absolute;left:480px;top:560px;width:430px;padding:26px 0 24px;border-radius:34px;background:#fff;color:#111;text-align:center;box-shadow:0 16px 0 rgba(0,0,0,.35),0 30px 80px rgba(0,0,0,.55)}
.ok .t{font:900 30px 'Inter',sans-serif;letter-spacing:3px;color:#6b7280}
.ok .p{font:900 58px/1.1 'Inter','Arial Black',sans-serif;letter-spacing:-2px;color:#0f766e}
.ok .c{display:inline-block;width:110px;height:110px;border-radius:50%;background:#16a34a;color:#fff;font:900 76px/110px 'Inter',sans-serif;margin-top:6px}
.ok .x{margin-top:12px;font:800 25px 'Inter',sans-serif;color:#111;background:#ffd23f;display:inline-block;padding:6px 18px;border-radius:12px}
.cmp{position:absolute;top:300px;padding:22px 0 20px;border-radius:30px;background:#fff;color:#111;text-align:center;box-shadow:0 16px 0 rgba(0,0,0,.35),0 30px 80px rgba(0,0,0,.55)}
.cmp .t{font:900 34px 'Inter',sans-serif;letter-spacing:2px}
.cmp .p{font:900 120px 'Inter','Arial Black',sans-serif;letter-spacing:-3px;line-height:1.05}
.cmp .x{font:800 30px 'Inter',sans-serif;color:#4b5563}
.tl{position:absolute;left:90px;top:300px;width:820px;padding:20px 26px;border-radius:30px;background:#fff;color:#111;box-shadow:0 16px 0 rgba(0,0,0,.35),0 30px 80px rgba(0,0,0,.55)}
.tl .r{display:flex;align-items:center;gap:22px;padding:12px 0;border-bottom:3px dashed #e5e7eb}
.tl .r:last-child{border-bottom:0}
.tl .a{flex:0 0 90px;width:90px;height:90px;border-radius:50%;background:#e5322d;color:#fff;text-align:center;font:900 56px/90px 'Inter','Arial Black',sans-serif}
.tl .w{font:900 40px/1.2 'Inter',sans-serif;color:#111}
.tl .w b{display:block;font:800 28px 'Inter',sans-serif;color:#0f766e}
.tl .h{font:900 30px 'Inter',sans-serif;letter-spacing:2px;color:#6b7280;text-align:center;padding-bottom:6px}
.qbox{position:absolute;left:90px;top:300px;width:820px;padding:30px 30px 34px;border-radius:40px;background:#ffd23f;color:#111;text-align:center;box-shadow:0 16px 0 rgba(0,0,0,.35)}
.qbox .q{font:900 72px/1.08 'Inter','Arial Black',sans-serif;letter-spacing:-1px}
.qbox .c{margin-top:16px;display:inline-block;padding:10px 26px;border-radius:30px;background:#111;color:#fff;font:800 38px 'Inter',sans-serif}
.chat{position:absolute;left:90px;top:300px;width:820px;padding:26px 26px 22px;border-radius:40px;background:#fff;color:#111;box-shadow:0 22px 0 rgba(0,0,0,.35),0 40px 100px rgba(0,0,0,.6)}
.chat .hd{font:800 26px 'Inter',sans-serif;color:#6b7280;letter-spacing:2px;text-align:center;padding-bottom:12px;border-bottom:2px solid #eee}
.chat .m{margin:14px 0 0 auto;width:max-content;padding:14px 26px;border-radius:30px 30px 8px 30px;background:#2563eb;color:#fff;font:800 44px 'Inter',sans-serif}
.chat .y{margin:14px auto 0 0;width:max-content;padding:14px 26px;border-radius:30px 30px 30px 8px;background:#f1f1f1;color:#111;font:800 44px 'Inter',sans-serif}
.chat .pill{margin:16px auto 0;width:max-content;padding:8px 22px;border-radius:30px;background:#111;color:#ffd23f;font:800 30px 'Inter',sans-serif}
.chat .x{margin-top:14px;font:600 22px/1.35 'Inter',sans-serif;color:#6b7280}
'''

BODY = duo_body("LE CONNAISSEUR", "L'INDÉCISE") + '''
  <div class="ment"><b>Lien de parrainage : je touche une prime</b><span>Offre soumise à conditions</span></div>
  <div class="scene" data-s="0">
   <div class="hook">Parrainage <em>BoursoBank</em> :<br>1re prime validée !</div>
   <div class="ok" data-g="0.0" data-fx="stamp"><div class="t">CHEZ L'INDÉCISE</div><div class="p">Prime validée</div><div class="c">✓</div><br><div class="x">prime si conditions remplies</div></div>
  </div>
  <div class="scene" data-s="1" data-in="pop">
   <div class="tag" style="left:300px;top:310px;font-size:72px" data-g="1.0" data-fx="stamp">BIEN JOUÉ !</div>
   <div class="cmp" style="left:150px;top:450px;width:760px" data-g="1.1" data-fx="up"><div class="t">PRIME DE BIENVENUE</div><div class="p" style="font-size:64px;line-height:1.15">si tu remplis<br>TOUTES les conditions</div><div class="x">offre BoursoBank en cours, 1re ouverture d'un compte</div></div>
  </div>
  <div class="scene" data-s="2" data-in="pop"><div class="tag red" style="left:150px;top:340px;font-size:80px" data-g="2.0" data-fx="stamp">IL FAUT FAIRE QUOI ?</div></div>
  <div class="scene" data-s="3" data-in="up">
   <div class="tl" data-g="3.0" data-fx="up"><div class="h">LES CONDITIONS À REMPLIR</div>
    <div class="r" data-g="3.0" data-fx="left"><div class="a">1</div><div class="w">1er versement<b>à l'ouverture ou dans les 30 jours</b></div></div>
    <div class="r" data-g="3.1" data-fx="left"><div class="a">2</div><div class="w">1 opération carte / mois<b>pendant les 3 premiers mois</b></div></div>
    <div class="r" data-g="3.5" data-fx="left"><div class="a">3</div><div class="w">changement de banque<b>EasyMove, signé dans le mois</b></div></div>
   </div>
  </div>
  <div class="scene" data-s="4" data-in="pop">
   <div class="cmp" style="left:140px;top:330px;width:800px" data-g="4.0" data-fx="pop"><div class="t">GARDE TON COMPTE</div><div class="p" data-g="4.1" data-fx="stamp">2 ANS</div><div class="x">clôture avant 24 mois :<br>la banque peut reprendre les primes</div></div>
  </div>
  <div class="scene" data-s="5" data-in="pop">
   <div class="qbox" data-g="5.0" data-fx="up"><div class="q">Ta 1re prime,<br>tu l'as eue ?</div><div class="c" data-g="5.2" data-fx="pop">💬 dis-le en commentaire</div></div>
  </div>
  <div class="scene" data-s="6" data-in="pop" style="z-index:7">
   <div class="chat" data-g="6.0" data-fx="up"><div class="hd">MESSAGE PRIVÉ</div>
    <div class="y" data-g="6.0" data-fx="left">Tu peux me parrainer ?</div>
    <div class="m" data-g="6.2" data-fx="right">Oui, avec plaisir 🤝</div>
    <div class="pill" data-g="6.3" data-fx="pop">⏳ offre BoursoBank jusqu'au 01/12, 14 h</div>
    <div class="x">Offre soumise aux conditions en vigueur (offre filleul du 24/11/2026 14 h au 01/12/2026 14 h, 1re ouverture d'un compte individuel ; primes versées si conditions remplies, reprises si clôture dans les 24 mois). Lien de parrainage : je touche une prime.</div></div>
  </div>
'''
