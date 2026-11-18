import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from tuto import *
from qg_figs import *
# Vidéos QG, 18/11/2026 (2e passage), vidéo 4 : duel Fortuneo / Monabanq. Format F10 « le connaisseur vs l'ignorant ».
# Style T « tuto illustré » avec 2 bonshommes au trait (le style D Duo 3D était prévu, mais Three.js est injoignable :
# cdn.jsdelivr.net, unpkg.com et cdnjs refusés par le proxy le 18/11/2026).
# Montants vérifiés le 18/11/2026 : monabanq.com/fr/parrainage.html (jusqu'à 280 € en 5 primes, dont 60 € au 13e mois) et
# fortuneo.fr/parrainage/cartes-bancaires (Fosfo 80 €, Gold 150 € dès 2 200 € nets/mois, 300 € versés sous 6 jours, du 01/11 au 30/11/2026).
# Voix (STYLE.md « Duo 3D ») : l'ignorant = Mathieu (inworld), le connaisseur = cosmo (xai), speed 1.1, silences coupés,
# 0,2 s au début et 0,45 s entre les répliques.
NAME = 'qg_duel1'
TITLE = 'QG duel Fortuneo Monabanq'
JS = 'const CAM=0.6, PUSH=0.012;' + FIGJS
MINLEN = 0.9
GAP = 0.12
TAIL = 2.6
LINES = [
 ("Parrainage Fortuneo ou Monabanq ? Moi je prends Monabanq : deux cent quatre-vingts euros !",
  [("<em>Parrainage Fortuneo</em>", None), ("ou <em>Monabanq</em> ?", None), ("Moi je prends Monabanq :", None), ("<i>280 € !</i>", None)]),
 ("Doucement ! C'est en cinq étapes, et les derniers soixante euros arrivent au treizième mois.",
  [("<i>Doucement !</i>", None), ("C'est en <em>5 étapes</em>,", None), ("et les derniers 60 €", None), ("arrivent au <em>13e mois</em>.", None)]),
 ("Et Fortuneo, ça donne quoi ?", [("Et Fortuneo,", None), ("ça donne quoi ?", None)]),
 ("Quatre-vingts euros avec la carte Fosfo, cent cinquante avec la Gold. Tu verses trois cents euros à l'ouverture.",
  [("<em>80 €</em> avec la carte Fosfo,", None), ("<em>150</em> avec la Gold.", None), ("Tu verses 300 €", None), ("à l'ouverture.", None)]),
 ("Et c'est jusqu'à quand ?", [("Et c'est jusqu'à quand ?", None)]),
 ("Fortuneo, jusqu'au trente novembre. Envoie-moi FORTUNEO ou MONABANQ en privé.",
  [("Fortuneo : jusqu'au <i>30 novembre</i>.", None), ("Envoie-moi", None), ("<em>FORTUNEO</em> ou <em>MONABANQ</em>", None), ("en privé.", None)]),
]
SPLITS = [(0.2, 4.63), (5.08, 9.72), (10.17, 11.62), (12.07, 17.95), (18.4, 19.12), (19.57, 24.59)]
GSTART = [[0.2, 1.1, 2.4, 3.55], [5.08, 6.05, 7.3, 8.6], [10.17, 10.85], [12.07, 14.35, 16.15, 17.2], [18.4], [19.57, 21.85, 22.45, 24.0]]

CSS = FIGCSS + '''
.ttl{font-size:62px}
.lst{position:absolute;left:455px;top:410px;width:445px;padding:22px 26px}
.lst .h{font:900 34px Inter;white-space:nowrap;margin-bottom:6px;text-align:center}
.lst .r{display:flex;justify-content:space-between;font:800 29px Inter;height:58px;align-items:center;border-bottom:3px dashed #cfc7b8;white-space:nowrap}
.lst .r b{font:900 36px Inter}
.lst .r:last-child{border-bottom:none}
.lst .s{font:600 24px Inter;color:#555;text-align:center;margin-top:6px}
.vs{position:absolute;left:470px;top:1010px;font:900 92px 'Comic Relief',cursive;color:#e63946;transform:rotate(-8deg)}
.cal{position:absolute;width:300px;height:300px;border:7px solid #111;border-radius:30px;background:#fff;box-shadow:10px 12px 0 #111;text-align:center;overflow:hidden}
.cal .m{height:84px;background:#e63946;color:#fff;font:900 50px Inter;line-height:84px;border-bottom:7px solid #111}
.cal .d{font:900 150px Inter;line-height:200px}
'''


def duo(p_mouth, p_arms, m_mouth, m_arms, speaker, y=820, sc=0.95):
    """Les 2 bonshommes : l'ignorant à gauche (cheveux en pétard), le connaisseur à droite (lunettes)."""
    glasses = '<circle cx="98" cy="76" r="15"/><circle cx="142" cy="76" r="15"/><path d="M113 76 L127 76"/>'
    big = 1.06
    ps, ms = (sc * big, sc) if speaker == 'P' else (sc, sc * big)
    return (guy(110, y - (int(470 * ps) - int(470 * sc)), 'spiky', p_mouth, p_arms, ps) +
            guy(690, y - (int(470 * ms) - int(470 * sc)), 'bun', m_mouth, m_arms, ms, mirror=True, extra_svg=glasses) +
            '<div class="tag" style="left:90px;top:1270px;font-size:30px">L\'IGNORANT</div>'
            '<div class="tag" style="left:640px;top:1270px;font-size:30px">LE CONNAISSEUR</div>')


HEAD = ''
BODY = '''
  <div class="scene" data-s="0-5">''' + title('Parrainage <mark>Fortuneo</mark><br>ou <mark>Monabanq</mark>&nbsp;?', 205, size=62) + '''</div>
  <div class="scene" data-s="0">''' + duo('open', 'up', 'flat', 'hip', 'P') + \
    bubble(90, 470, 430, 'Monabanq<br><em style="font-size:84px">280 €</em> !', '0.0', 'left', 50).replace(' data-g="0.0" data-fx="pop"', '') + '''
   <div class="vs">VS</div></div>
  <div class="scene" data-s="1" data-in="pop">''' + duo('sad', 'shrug', 'smile', 'point', 'M') + '''
   <div class="paper lst" data-g="1.1" data-fx="up"><div class="h">Monabanq · 5 primes</div>
    <div class="r">ouverture<b>20 €</b></div><div class="r">300 € versés<b>60 €</b></div><div class="r">30 paiements<b>60 €</b></div>
    <div class="r">mobilité bancaire<b>80 €</b></div><div class="r" style="color:#e63946">13e mois<b>60 €</b></div></div>''' + \
    circle(420, 692, 510, 110, '1.3') + '''
   <div class="note" style="left:90px;top:560px;transform:rotate(-5deg)" data-g="1.3" data-fx="pop">dans 1 an ?!</div></div>
  <div class="scene" data-s="2" data-in="pop">''' + duo('open', 'shrug', 'smile', 'hip', 'P') + \
    bubble(90, 520, 400, 'Et <em>Fortuneo</em>&nbsp;?', '2.0', 'left', 54) + '''</div>
  <div class="scene" data-s="3" data-in="pop">''' + duo('open', 'down', 'smile', 'point', 'M') + '''
   <div class="paper lst" data-g="3.0" data-fx="up"><div class="h">Fortuneo</div>
    <div class="r">carte Fosfo<b>80 €</b></div><div class="r" data-g="3.1" data-fx="left">carte Gold<b>150 €</b></div>
    <div class="s" data-g="3.1" data-fx="fade">Gold : dès 2 200 € nets/mois</div>
    <div class="s" data-g="3.2" data-fx="left" style="font:800 26px Inter;color:#111;margin-top:10px;white-space:nowrap">+ 300 € versés sous 6 jours</div></div>''' + '''
   <div class="note" style="left:50px;top:560px;font-size:38px;transform:rotate(-5deg)" data-g="3.2" data-fx="pop">pas de 13e mois !</div></div>
  <div class="scene" data-s="4" data-in="pop">''' + duo('open', 'shrug', 'flat', 'hip', 'P') + \
    bubble(90, 520, 430, 'Jusqu\'à quand&nbsp;?', '4.0', 'left', 50) + '''</div>
  <div class="scene" data-s="5" data-in="pop">''' + duo('smile', 'up', 'smile', 'point', 'M', 960, 0.7) + '''
   <div class="cal" style="left:110px;top:420px;width:260px;height:270px" data-g="5.0" data-fx="stamp"><div class="m">NOV.</div><div class="d" style="font-size:130px;line-height:180px">30</div></div>''' + \
    circle(90, 400, 300, 310, '5.0') + '''
   <div class="note" style="left:110px;top:720px;font-size:38px" data-g="5.0" data-fx="pop">fin Fortuneo</div>
   <div class="paper" style="left:420px;top:410px;width:520px;padding:22px 20px;text-align:center" data-g="5.1" data-fx="up">
    <div style="font:900 38px Inter">ENVOIE-MOI EN PRIVÉ</div>
    <div style="font:900 50px Inter;margin:6px 0;white-space:nowrap"><span class="hl">« FORTUNEO »</span></div><div style="font:800 32px Inter">ou</div>
    <div style="font:900 50px Inter;margin:6px 0;white-space:nowrap"><span class="hl">« MONABANQ »</span></div>
    <div style="font:600 21px/1.3 Inter;color:#333;margin-top:8px">Offres soumises aux conditions en vigueur.<br>Fortuneo : 80 € (Fosfo) ou 150 € (Gold, dès 2 200 € nets/mois),<br>code parrain + 300 € versés sous 6 jours, jusqu'au 30/11/2026.<br>Monabanq : jusqu'à 280 € en 5 primes, la dernière au 13e mois.<br>Lien de parrainage : je touche une prime.</div></div></div>
'''
