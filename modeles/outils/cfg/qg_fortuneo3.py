import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from tuto import *
from qg_figs import *
# Vidéos QG du 25/11/2026, vidéo 1 : Fortuneo. Style T « tuto illustré » (personnages blancs animés).
# Format F14 « Pourquoi la banque te paie » (2e F14, 1re hors style X) : question -> « arnaque ? non » -> la banque paie la pub
# très cher -> avec le parrainage elle donne cet argent au filleul et au parrain -> elle espère un client fidèle -> gagnant-gagnant
# -> l'offre du jour -> appel à l'action. Aucun chiffre de coût de pub (pas de source officielle).
# Source : https://www.fortuneo.fr/parrainage/cartes-bancaires (consultée le 25/11/2026) : offre du 01/11 au 30/11/2026 (dossier
# complet reçu au plus tard le 30/11) ; filleul 80 € (1re ouverture avec carte Fosfo Mastercard, sans condition de revenus) ou
# 150 € (Gold CB Mastercard, dès 2 200 € de revenus nets mensuels pour un compte individuel) ; code parrain renseigné pendant la
# souscription ; versement initial de 300 € dans les 6 jours suivant l'ouverture ; compte et carte conservés au moins 1 an ;
# prime versée au plus tard le 31/12/2026 ; parrain 80 € (Fosfo) ou 120 € (Gold) s'il détient au moins 300 € d'encours.
# Voix : Etienne (cartesia sonic-3.5, speed 1.2), une synthèse par réplique, atempo 1.07, pauses internes ramenées à 0,22 s.
NAME = 'qg_fortuneo3'
TITLE = 'QG Fortuneo pourquoi la banque te paie'
JS = 'const CAM=0.6, PUSH=0.012;' + FIGJS + '''
const QM=[...document.querySelectorAll('.qm')];
const _ex=extra; extra=function(t){_ex(t);QM.forEach((q,i)=>{q.style.translate=`0 ${Math.sin(t*6+i*2)*10}px`;q.style.rotate=`${Math.sin(t*3+i)*8}deg`});
 document.querySelectorAll('.bill').forEach((b,i)=>{const k=((t*0.55+i*0.27)%1);b.style.translate=`${k*250}px ${-Math.sin(k*Math.PI)*90}px`;b.style.opacity=k<0.08?k/0.08:(k>0.9?(1-k)/0.1:1)});};
'''
GAP = 0.28
TAIL = 1.2
MINLEN = 1.5
LINES = [
 ("Parrainage Fortuneo : pourquoi la banque te paie pour ouvrir un compte ?",
  [("<em>Parrainage Fortuneo</em> :", None), ("pourquoi la banque", None), ("<i>te paie</i>", None), ("pour ouvrir un compte ?", None)]),
 ("Une arnaque ? Non.", [("Une <i>arnaque</i> ?", None), ("<em>Non.</em>", None)]),
 ("Pour trouver des clients, elle paie la pub très cher : télé, affiches, influenceurs.",
  [("Pour trouver des clients,", None), ("elle paie la pub", None), ("<i>très cher</i> :", None), ("télé,", None), ("affiches,", None), ("influenceurs.", None)]),
 ("Avec le parrainage, elle te donne cet argent, à toi et à ton parrain.",
  [("Avec le <em>parrainage</em>,", None), ("elle te donne cet argent,", None), ("à <em>toi</em>", None), ("et à ton parrain.", None)]),
 ("Et elle espère que tu resteras client. Gagnant-gagnant.",
  [("Et elle espère", None), ("que tu resteras client.", None), ("<em>Gagnant-gagnant.</em>", None)]),
 ("Jusqu'au trente novembre : 80 € avec la carte Fosfo, 150 € avec la Gold.",
  [("Jusqu'au <em>30 novembre</em> :", None), ("<em>80 €</em> avec la carte Fosfo,", None), ("<em>150 €</em> avec la Gold.", None)]),
 ("Envoie-moi le mot Fortuneo en privé, je t'envoie mon code.",
  [("Envoie-moi le mot <em>FORTUNEO</em>", None), ("en privé,", None), ("je t'envoie mon code.", None)]),
]
SPLITS = [(0.0, 3.138), (3.638, 4.997), (5.497, 9.899), (10.399, 14.222), (14.722, 17.582), (18.082, 22.769), (23.269, 26.469)]

CSS = FIGCSS + '''
#sub{left:60px;width:850px}
.endc{left:90px;width:780px}
.endc .c{font-size:96px;white-space:nowrap}
.legal{position:absolute;left:60px;top:1312px;width:850px;text-align:center;font:700 26px Inter;color:#555;z-index:5}
.qm{position:absolute;font:700 150px/1 'Comic Relief',cursive;color:#e63946}
.bigN{position:absolute;font:900 170px/1 Inter;letter-spacing:-5px;white-space:nowrap;color:#e63946}
.bill{position:absolute;width:120px;height:66px;border:6px solid #111;border-radius:10px;background:#bfe8c4;font:900 34px/54px Inter;text-align:center}
.lst{position:absolute;left:70px;width:800px;padding:24px 34px}
.lst .r{display:flex;align-items:center;gap:22px;font:800 44px Inter;white-space:nowrap;height:116px}
.lst .r .p{margin-left:auto;font:900 58px Inter;color:#1b8a3c}
.cardd{display:inline-block;width:120px;height:78px;border:6px solid #111;border-radius:12px;background:#fff;position:relative;flex:none}
.cardd:after{content:'';position:absolute;left:12px;top:16px;width:30px;height:22px;border-radius:5px;background:#111}
.ck{display:flex;align-items:center;gap:20px;font:800 44px Inter;white-space:nowrap;height:110px}
.ck b{color:#1b8a3c;font:900 64px Inter;width:60px}
.lbl{position:absolute;font:900 34px Inter;white-space:nowrap;padding:6px 18px;border:5px solid #111;border-radius:14px;background:#fff}
'''

BANK = ('<path d="M20 70 L120 14 L220 70 Z" style="fill:#fff"/><path d="M30 78 L210 78"/><path d="M50 92 L50 170 M95 92 L95 170 M145 92 L145 170 M190 92 L190 170"/>'
        '<path d="M22 182 L218 182"/>')
TV = ('<rect x="10" y="40" width="220" height="150" rx="18" style="fill:#fff"/><rect x="34" y="62" width="172" height="106" rx="8"/>'
      '<path d="M90 6 L120 40 L150 6"/><path d="M70 190 L56 220 M170 190 L184 220"/><path d="M70 115 l30 -25 l30 25 l30 -25"/>')
POSTER = ('<rect x="20" y="10" width="200" height="200" rx="6" style="fill:#ffe14d"/><path d="M120 210 L120 250 M70 250 L170 250"/>'
          '<text x="120" y="135" text-anchor="middle" style="font:900 74px Inter;fill:#111;stroke:none">PUB</text>')
PHONEI = ('<rect x="60" y="6" width="130" height="230" rx="24" style="fill:#fff"/><circle cx="125" cy="80" r="28"/>'
          '<path d="M85 150 Q125 110 165 150"/><path d="M110 190 q15 -22 30 0 q-15 18 -15 22 q0 -4 -15 -22" style="stroke:#e63946"/>')


def svgg(x, y, w, h, inner, g, vb, fx='pop'):
    return svg(x, y, w, h, inner, 'ink', vb).replace('class="abs ink"', f'class="abs ink" data-g="{g}" data-fx="{fx}"', 1)


BODY = '''
  <div class="legal">Offre soumise à conditions · lien de parrainage</div>
  <div class="scene" data-s="0">''' + title('Parrainage<br><mark>Fortuneo</mark>', 210, size=92) + \
    svg(70, 560, 240, 200, BANK, 'ink') + '''
   <div class="tag" style="left:85px;top:775px">la banque</div>
   <div class="bill" style="left:300px;top:640px">€</div><div class="bill" style="left:300px;top:640px">€</div><div class="bill" style="left:300px;top:640px">€</div>''' + \
    guy(640, 520, 'cap', 'open', 'shrug', 0.95) + '''
   <div class="qm" style="left:520px;top:450px" data-g="0.1" data-fx="pop">?</div><div class="qm" style="left:860px;top:400px" data-g="0.2" data-fx="pop">?</div>
   <div class="bigN" style="left:90px;top:960px;font-size:120px" data-g="0.0" data-fx="stamp">jusqu'à 150 €</div>
   <div class="note" style="left:200px;top:1110px;font-size:46px;transform:rotate(-3deg)" data-g="0.3" data-fx="pop">pour ouvrir un compte ?!</div></div>
  <div class="scene" data-s="1" data-in="right">''' + title('Une <em>arnaque</em> ?', 300, size=104) + \
    guy(110, 540, 'curly', 'open', 'hip', 1.0) + '''
   <div class="bigN" style="left:470px;top:640px;font-size:230px;transform:rotate(-8deg);border:12px solid #e63946;padding:0 30px;border-radius:30px" data-g="1.1" data-fx="stamp">NON</div>
   <div class="note" style="left:470px;top:960px;font-size:50px;color:#111;transform:rotate(-3deg)" data-g="1.1" data-fx="pop">c'est du <span class="hl">marketing</span></div></div>
  <div class="scene" data-s="2" data-in="right">''' + title('Trouver des clients,<br>ça coûte <em>cher</em>', 220, size=78) + \
    svg(90, 470, 240, 200, BANK, 'ink') + '''
   <div class="bigN" style="left:380px;top:500px;font-size:130px" data-g="2.2" data-fx="stamp">€€€</div>''' + \
    arrow(560, 520, 300, 120, 'M0 60 Q150 0 290 60 M255 34 L292 61 L252 82', '2.2') + \
    svgg(60, 760, 240, 230, TV, '2.3', '0 0 240 230') + svgg(340, 750, 240, 260, POSTER, '2.4', '0 0 240 260') + svgg(620, 750, 250, 240, PHONEI, '2.5', '0 0 250 240') + '''
   <div class="note" style="left:110px;top:1020px;font-size:40px" data-g="2.3" data-fx="pop">télé</div>
   <div class="note" style="left:380px;top:1030px;font-size:40px" data-g="2.4" data-fx="pop">affiches</div>
   <div class="note" style="left:620px;top:1020px;font-size:40px" data-g="2.5" data-fx="pop">influenceurs</div></div>
  <div class="scene" data-s="3" data-in="up">''' + title('Avec le <mark>parrainage</mark>', 220, size=72) + \
    svg(380, 380, 240, 200, BANK, 'ink') + '''
   <div class="tag" style="left:395px;top:590px">la banque</div>''' + \
    arrow(220, 600, 200, 200, 'M180 10 Q60 40 30 180 M10 140 L30 182 L62 150', '3.1') + arrow(620, 600, 200, 200, 'M10 10 Q140 40 170 180 M138 150 L170 182 L192 140', '3.1') + \
    guy(110, 800, 'spiky', 'smile', 'up', 0.85, g='3.2', fx='up') + guy(630, 800, 'bun', 'smile', 'up', 0.85, g='3.3', fx='up') + '''
   <div class="lbl" style="left:110px;top:1210px;background:#ffe14d" data-g="3.2" data-fx="stamp">TOI : ta prime</div>
   <div class="lbl" style="left:600px;top:1210px" data-g="3.3" data-fx="stamp">PARRAIN : sa prime</div></div>
  <div class="scene" data-s="4" data-in="right">''' + title('Gagnant-<mark>gagnant</mark>', 230, size=80) + '''
   <div class="paper" style="left:70px;top:400px;width:800px;padding:20px 34px">
    <div class="ck" data-g="4.0" data-fx="left"><b>✓</b>la banque : un client</div>
    <div class="ck" data-g="4.1" data-fx="left"><b>✓</b>… qui reste client</div>
    <div class="ck" data-g="4.2" data-fx="left"><b>✓</b>toi : ta prime</div></div>''' + \
    guy(110, 800, 'cap', 'smile', 'up', 0.85) + guy(560, 800, 'none', 'smile', 'up', 0.85, mirror=True) + '''
   <div class="note" style="left:330px;top:900px;font-size:40px;transform:rotate(-3deg)" data-g="4.1" data-fx="pop">compte + carte<br>gardés 1 an min.</div></div>
  <div class="scene" data-s="5" data-in="right">''' + title("Fortuneo, jusqu'au <mark>30/11</mark>", 220, size=78) + '''
   <div class="paper lst" style="top:400px"><div class="r" data-g="5.1" data-fx="left"><span class="cardd"></span>carte Fosfo<span class="p">80 €</span></div>
    <div class="r" data-g="5.2" data-fx="left"><span class="cardd" style="background:#ffe14d"></span>carte Gold<span class="p">150 €</span></div></div>''' + \
    circle(610, 530, 280, 130, '5.2', -3) + '''
   <div class="note" style="left:90px;top:720px;font-size:38px;width:780px;text-align:center;white-space:normal;transform:rotate(-2deg)" data-g="5.2" data-fx="pop">Gold : dès 2 200 € nets / mois</div>
   <div class="paper" style="left:70px;top:830px;width:800px;padding:22px 30px;font:800 36px/1.35 Inter" data-g="5.0" data-fx="up">✓ code parrain pendant l'ouverture<br>✓ 300 € versés sous 6 jours</div>''' + \
    guy(380, 1010, 'cap', 'smile', 'point', 0.55) + '''</div>
  <div class="scene" data-s="6" data-in="pop">
   <div class="endc" data-g="6.0" data-fx="up"><div class="k">ENVOIE-MOI EN PRIVÉ</div><div class="c">« FORTUNEO »</div><div class="d">je t'envoie mon code</div><div class="b">@htm.invest</div></div>
   <div class="note" style="left:300px;top:770px;transform:rotate(-3deg)" data-g="6.1" data-fx="pop">parrainage Fortuneo</div>''' + \
    guy(90, 850, 'cap', 'smile', 'up', 0.55) + '''
   <div class="cond" style="top:860px;left:270px;width:600px">Offre soumise aux conditions en vigueur.<br>Parrainage Fortuneo, offre du 01/11 au 30/11/2026 (dossier complet reçu au plus tard le 30/11) : 80 € avec la carte Fosfo, 150 € avec la Gold CB Mastercard (dès 2 200 € de revenus nets mensuels). Code parrain à saisir pendant la souscription, versement initial de 300 € dans les 6 jours, compte et carte gardés au moins 1 an. Prime versée au plus tard le 31/12/2026.<br>Lien de parrainage : je touche une prime.</div></div>
'''
