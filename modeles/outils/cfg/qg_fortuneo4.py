import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from tuto import *
from qg_figs import *
# Vidéos QG du 28/11/2026, vidéo 1 : Fortuneo. Format F18 « Parraine à ton tour » (2e F18 en QG, 1re Fortuneo).
# Style T « tuto illustré » (personnages blancs au trait). Règles anti-bannissement du 26/11 : AUCUN montant écrit ni dit
# (l'offre actuelle se termine le 30/11/2026 : pas de total maximum, règle 6), bandeau de mentions permanent,
# un seul niveau (toi -> tes amis), « je ne touche rien sur les amis de mes filleuls ».
# Source : https://www.fortuneo.fr/parrainage/cartes-bancaires (consultée le 28/11/2026) : « Le parrain peut parrainer jusqu'à
# 10 personnes par an. Au-delà, aucune prime ne sera versée au parrain » ; prime parrain 120 € (Gold) ou 80 € (Fosfo) par
# filleul, offre du 01/11 au 30/11/2026 (montant non dit : il peut changer au 01/12).
# Voix : Cosmo (xai tts, speed 1.1), une synthèse par réplique, atempo 0.8-1.05 (débit ramené à ≈ 185 mots/min par réplique).
NAME = 'qg_fortuneo4'
TITLE = 'QG Fortuneo parraine a ton tour'
JS = 'const CAM=0.6, PUSH=0.011;' + FIGJS + '''
const QM=[...document.querySelectorAll('.qm')];
const _ex=extra; extra=function(t){_ex(t);QM.forEach((q,i)=>{q.style.translate=`0 ${Math.sin(t*6+i*2)*10}px`;q.style.rotate=`${Math.sin(t*3+i)*8}deg`});
 const cu=document.querySelector('.cur'); if(cu) cu.style.opacity=(Math.floor(t*2.4)%2)?0:1;
 document.querySelectorAll('.env').forEach(e=>{e.style.translate=`0 ${Math.sin(t*4)*6}px`});};
'''
GAP = 0.28
TAIL = 1.2
MINLEN = 1.5
LINES = [
 ("Parrainage Fortuneo : à ton tour de parrainer ?",
  [("<em>Parrainage Fortuneo</em> :", None), ("à ton tour", None), ("de <i>parrainer</i> ?", None)]),
 ("Je te parraine, tu ouvres ton compte, tu remplis les conditions.",
  [("Je te parraine,", None), ("tu ouvres ton compte,", None), ("tu remplis", None), ("les <em>conditions</em>.", None)]),
 ("Une fois client, tu as ton propre code.",
  [("Une fois <em>client</em>,", None), ("tu as ton propre code.", None)]),
 ("Une prime par ami qui remplit les conditions, jusqu'à dix amis par an : plafond fixé par la banque.",
  [("Une prime <i>par ami</i>", None), ("qui remplit les conditions,", None), ("jusqu'à <em>10 amis</em> par an :", None), ("<em>plafond</em> fixé", None), ("par la banque.", None)]),
 ("Et moi, je ne touche rien sur les amis de mes filleuls.",
  [("Et moi,", None), ("je ne touche <i>rien</i>", None), ("sur les amis", None), ("de mes filleuls.", None)]),
 ("Tu inviterais qui en premier ? Dis-le en commentaire.",
  [("Tu inviterais qui", None), ("en <em>premier</em> ?", None), ("Dis-le en <i>commentaire</i>.", None)]),
 ("Si tu veux que je te parraine, écris-moi en privé.",
  [("Si tu veux", None), ("que je te parraine,", None), ("écris-moi", None), ("en <em>privé</em>.", None)]),
]
SPLITS = [(0.0, 2.274), (2.774, 6.339), (6.839, 9.1), (9.6, 15.434), (15.934, 18.728), (19.228, 22.14), (22.64, 25.523)]

CROWN = '<path d="M92 132 Q120 150 148 132 L154 146 Q120 168 86 146 Z" style="fill:#ffe14d"/><path d="M130 150 L138 204 L158 196 L146 146" style="fill:#ffe14d"/>'  # écharpe jaune (après le gardien : plus de couronne, déjà vue dans le F18 Monabanq)

CSS = FIGCSS + '''
#bgtex{background:linear-gradient(rgba(70,110,200,.14) 2px,transparent 2px) 0 0/48px 48px,linear-gradient(90deg,rgba(70,110,200,.14) 2px,transparent 2px) 0 0/48px 48px,#f6f4ee !important}
#sub{left:80px;width:840px;font-size:66px}
.ment{position:absolute;left:110px;top:196px;width:780px;padding:10px 16px 12px;border:5px solid #111;border-radius:18px;background:#fff;text-align:center;z-index:9;box-shadow:6px 7px 0 #111}
.ment b{display:block;font:900 27px Inter;color:#111;white-space:nowrap}
.ment span{display:block;font:700 23px Inter;color:#e63946;white-space:nowrap}
.ttl{top:330px;left:80px;width:840px}
.qm{position:absolute;font:700 140px/1 'Comic Relief',cursive;color:#e63946}
.ck{display:flex;align-items:center;gap:20px;font:800 44px Inter;white-space:nowrap;height:104px}
.ck b{color:#1b8a3c;font:900 60px Inter;width:56px}
.env{position:absolute;width:250px;height:160px;border:6px solid #111;border-radius:14px;background:#fff;overflow:hidden}
.env:before{content:'';position:absolute;left:-6px;top:-70px;width:250px;height:150px;border:6px solid #111;transform:scaleY(.55) rotate(45deg);transform-origin:50% 100%;background:#ffe14d}
.env .w{position:absolute;left:0;right:0;bottom:12px;text-align:center;font:900 26px Inter;letter-spacing:1px}
.head{position:absolute;width:104px;height:104px}
.stampr{position:absolute;padding:12px 26px;border:8px solid #e63946;border-radius:22px;color:#e63946;font:900 50px/1.15 Inter;text-align:center;background:rgba(250,249,246,.92);white-space:nowrap}
.cmt{position:absolute;left:90px;top:520px;width:820px;padding:30px 34px 34px}
.cmt .h{font:900 38px Inter;border-bottom:4px solid #111;padding-bottom:16px;margin-bottom:22px}
.cmt .q{font:900 54px/1.15 Inter}
.cmt .in{margin-top:28px;height:96px;border:5px solid #111;border-radius:48px;display:flex;align-items:center;padding:0 30px;font:700 34px Inter;color:#888;white-space:nowrap}
.cmt .cur{display:inline-block;width:5px;height:46px;background:#111;margin-left:6px}
.endw{top:330px;left:110px;width:780px}
.endw .c{font-size:112px}
.endw .k{font-size:42px}
.cond{left:110px;width:780px;font-size:25px}
'''


def head(x, y, g, i):
    mouths = ['M34 64 Q52 80 70 64', 'M36 66 Q52 76 68 66']
    return (f'<svg class="head ink" style="left:{x}px;top:{y}px" viewBox="0 0 104 104" data-g="{g}" data-fx="pop">'
            f'<circle cx="52" cy="52" r="44" style="fill:#fff"/><path d="M38 44 l0 6 M66 44 l0 6"/><path d="{mouths[i % 2]}"/></svg>')


HEADS = ''.join(head(110 + (i % 5) * 160, 780 + (i // 5) * 140, f'3.{min(2, i // 4)}', i) for i in range(10))

BODY = '''
  <div class="ment"><b>Lien de parrainage : je touche une prime</b><span>Offre soumise à conditions</span></div>
  <div class="scene" data-s="0">''' + title('Parrainage<br><mark>Fortuneo</mark>', 330, size=100) + '''
   <div class="note" style="left:200px;top:560px;font-size:58px;transform:rotate(-3deg)">à ton tour de parrainer ?</div>''' + \
    guy(400, 700, 'none', 'open', 'up', 1.0, extra_svg=CROWN) + \
    circle(330, 650, 400, 560, '0.1', -3) + '''
   <div class="tag" style="left:150px;top:900px;background:#ffe14d" data-g="0.1" data-fx="stamp">TOI</div>
   <div class="qm" style="left:700px;top:700px" data-g="0.2" data-fx="pop">?</div><div class="qm" style="left:180px;top:1060px" data-g="0.2" data-fx="pop">?</div></div>
  <div class="scene" data-s="1" data-in="right">''' + title('<mark>1</mark> je te parraine', 330, size=84) + \
    guy(70, 470, 'cap', 'smile', 'point', 0.8) + guy(640, 470, 'none', 'open', 'up', 0.8, g='1.1', fx='right', extra_svg=CROWN) + '''
   <div class="tag" style="left:90px;top:860px">MOI</div><div class="tag" style="left:690px;top:860px;background:#ffe14d" data-g="1.1" data-fx="stamp">TOI</div>
   <div class="env" style="left:380px;top:560px" data-g="1.0" data-fx="left"><div class="w">EN PRIVÉ</div></div>
   <div class="paper" style="left:120px;top:990px;width:760px;padding:14px 34px">
    <div class="ck" data-g="1.0" data-fx="left"><b>✓</b>tu ouvres ton compte</div>
    <div class="ck" data-g="1.2" data-fx="left"><b>✓</b>tu remplis les conditions</div></div></div>
  <div class="scene" data-s="2" data-in="up">''' + title('<mark>2</mark> une fois client', 330, size=84) + '''
   <div class="phone" style="left:420px;top:470px;height:760px">
    <div class="scr"><div class="tt">Parrainage</div><div class="ln" style="width:70%"></div><div class="ln" style="width:50%"></div>
     <div class="fl" data-g="2.1" data-fx="stamp" data-slow="2.1">ton code parrain ✓</div>
     <div class="bt" data-g="2.1" data-fx="up">Partager</div><div class="ln" style="width:80%;margin-top:30px"></div><div class="ln" style="width:60%"></div></div></div>''' + \
    guy(90, 640, 'none', 'smile', 'point', 0.85, extra_svg=CROWN) + '''
   <div class="note" style="left:40px;top:1150px;font-size:42px;transform:rotate(-4deg)" data-g="2.0" data-fx="pop">ton propre code</div></div>
  <div class="scene" data-s="3" data-in="right">''' + title('<mark>3</mark> tes amis', 330, size=84) + \
    guy(450, 440, 'none', 'smile', 'up', 0.6, extra_svg=CROWN) + \
    arrow(160, 620, 300, 150, 'M290 10 Q120 30 30 140 M20 100 L30 142 L70 128', '3.0') + arrow(590, 620, 300, 150, 'M10 10 Q180 30 270 140 M232 128 L272 142 L280 100', '3.0') + \
    HEADS + '''
   <div class="paper" style="left:110px;top:1060px;width:780px;padding:12px 26px;font:800 36px/1.25 Inter;text-align:center" data-g="3.1" data-fx="up">une prime par ami<br><span class="hl">si conditions remplies</span></div>
   <div class="stampr" style="left:170px;top:1215px;font-size:36px;transform:rotate(-3deg)" data-g="3.3" data-fx="stamp">jusqu'à 10 amis par an<br>plafond fixé par la banque</div></div>
  <div class="scene" data-s="4" data-in="up">''' + title('Et moi ?', 330, size=96) + \
    guy(90, 520, 'cap', 'flat', 'shrug', 0.95) + '''
   <div class="tag" style="left:120px;top:990px">MOI</div>
   <div class="stampr" style="left:400px;top:560px;transform:rotate(-6deg)" data-g="4.1" data-fx="stamp">RIEN</div>
   <div class="note" style="left:400px;top:720px;font-size:60px;color:#111;line-height:1.2;white-space:normal;width:500px" data-g="4.2" data-fx="pop">sur les amis<br>de mes filleuls</div>
   <div class="paper" style="left:380px;top:930px;width:520px;padding:18px 24px;font:900 40px/1.25 Inter;text-align:center" data-g="4.3" data-fx="up">UN SEUL NIVEAU<br><span class="hl">toi → tes amis</span></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + title('À toi de jouer', 330, size=84) + '''
   <div class="paper cmt" data-g="5.0" data-fx="up"><div class="h">Commentaires</div><div class="q">Tu inviterais qui<br>en <span class="hl">premier</span> ?</div>
    <div class="in" data-g="5.2" data-fx="pop">Dis-le en commentaire<span class="cur"></span></div></div>''' + \
    guy(560, 940, 'none', 'smile', 'hip', 0.62, extra_svg=CROWN) + '''
   <div class="qm" style="left:180px;top:1000px" data-g="5.1" data-fx="pop">?</div><div class="qm" style="left:370px;top:1060px;font-size:100px" data-g="5.1" data-fx="pop">?</div></div>
  <div class="scene" data-s="6" data-in="pop">
   <div class="endw" data-g="6.0" data-fx="up"><div class="k">SI TU VEUX QUE JE TE PARRAINE</div><div class="c">ÉCRIS-MOI</div><div class="d">en privé</div><div class="b">@htm.invest</div></div>''' + \
    guy(110, 830, 'cap', 'smile', 'up', 0.55) + '''
   <div class="cond" style="top:860px;left:300px;width:600px;text-align:left">Offre soumise aux conditions en vigueur.<br>Parrainage Fortuneo : une prime pour le parrain par filleul qui remplit les conditions, montant selon l'offre en cours, dans la limite de 10 filleuls par an (plafond fixé par la banque). Un seul niveau de parrainage.<br>Lien de parrainage : je touche une prime.</div></div>
'''
