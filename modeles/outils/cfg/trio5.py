NAME = 'trio5'
TITLE = 'Trio v5'
ROOT = ':root{--bg:#fbe7e4;--bgg:linear-gradient(180deg,#fcece9 0%,#f5d9d4 100%);--ink:#3a0d1a;--acc:#c2185b;--sec:#ffd54a;--hl:#ffd54a;--flash:#ffd54a;--mute:#7a5560}'
H = lambda s: f'<span class=hl>{s}</span>'
LINES = [
 ("Tu laisses peut-être 770 euros sur la table.", [("Tu laisses", None), ("peut-être", None), (H("770 €"), "sept cent soixante-dix euros"), ("sur la table.", None)]),
 ("Trois banques te paient pour ouvrir un compte.", [("Trois banques", None), ("te paient", None), ("pour ouvrir", None), ("un compte.", None)]),
 ("Hello bank : jusqu'à 330 euros, mais le parrainage finit demain.", [("Hello bank :", None), ("jusqu'à", None), (H("330 €,"), "trois cent trente euros"), ("mais le parrainage", None), ("finit demain.", None)]),
 ("Fortuneo : jusqu'à 260 euros, avec la carte Gold.", [("Fortuneo :", None), ("jusqu'à", None), (H("260 €,"), "deux cent soixante euros"), ("avec la carte Gold.", None)]),
 ("BoursoBank : jusqu'à 180 euros à l'ouverture.", [("BoursoBank :", None), ("jusqu'à", None), (H("180 €"), "cent quatre-vingts euros"), ("à l'ouverture.", None)]),
 ("Additionne tout : 770 euros en cumulé.", [("Additionne tout :", None), (H("770 €"), "sept cent soixante-dix euros"), ("en cumulé.", None)]),
 ("Envoie-moi PARRAINAGE en privé.", [("Envoie-moi", None), (H("« PARRAINAGE »"), "parrainage"), ("en privé.", None)]),
]
CSS = '''
#brand{color:#fff;background:var(--ink)}
#s0{top:470px}
#s0 .l1{font:800 100px Inter;line-height:1.04;letter-spacing:-2px}
#s0 .big{font:900 260px 'Inter Display',Inter;letter-spacing:-8px;line-height:1;color:var(--acc);margin-top:18px;white-space:nowrap;display:inline-block;background:linear-gradient(transparent 68%,var(--sec) 68%,var(--sec) 92%,transparent 92%)}
#s0 .l2{font:800 100px Inter;letter-spacing:-2px;margin-top:10px}
#s1{top:470px}
#s1 .t{font:800 74px Inter;letter-spacing:-2px;line-height:1.05;margin-bottom:34px}
.chip{display:flex;justify-content:space-between;align-items:center;background:#fff;border:4px solid var(--ink);border-radius:28px;padding:22px 34px;margin-bottom:22px;font:800 58px Inter;white-space:nowrap}
.chip i{font-style:normal;color:var(--acc);font-weight:900}
.card{top:450px;background:#fff;border-radius:40px;padding:40px 46px 44px;box-shadow:0 22px 0 var(--ink);border:4px solid var(--ink)}
.card .n{font:700 34px Inter;color:var(--mute);letter-spacing:2px}
.card .b{font:900 104px Inter;letter-spacing:-3px;margin-top:6px;white-space:nowrap}
.card .j{font:800 52px Inter;margin-top:26px}
.card .a{display:inline-block;font:900 190px 'Inter Display',Inter;color:var(--acc);letter-spacing:-7px;line-height:1;white-space:nowrap;transform-origin:20% 60%}
.card .tg{display:inline-block;margin-top:26px;font:700 38px Inter;padding:12px 22px;border-radius:16px;background:var(--sec);white-space:nowrap}
.card .tg.u{background:var(--ink);color:#fff}
#s5{top:470px}
#s5 .r{font:800 84px Inter;letter-spacing:-1px;text-align:right;width:560px;white-space:nowrap}
#s5 .ln{height:8px;background:var(--ink);width:560px;margin:20px 0 10px;border-radius:4px}
#s5 .tot{font:900 220px 'Inter Display',Inter;letter-spacing:-8px;color:var(--acc);white-space:nowrap;transform-origin:10% 70%}
#s6{top:440px}
#s6 .a{font:800 92px Inter;letter-spacing:-1.5px}
#s6 .k{display:inline-block;margin-top:22px;background:var(--acc);color:#fff;font:900 84px Inter;padding:12px 28px 18px;border-radius:24px;white-space:nowrap}
#s6 .p{font:800 92px Inter;margin-top:18px}
#s6 .d{font:700 42px Inter;color:var(--mute);margin-top:30px}
#s6 .cond{color:#5d3a44;top:940px}
'''
BODY = '''  <div id="brand" class="abs">3 offres en cours · novembre</div>
  <div id="s0" class="scene" data-s="0"><div class="l1">Tu laisses<br>peut-être</div><div class="big">770 €</div><div class="l2">sur la table.</div></div>
  <div id="s1" class="scene" data-s="1"><div class="t">3 banques te paient<br>pour ouvrir un compte</div>
   <div class="chip" data-g="1.0" data-fx="right">Hello bank <i>?</i></div>
   <div class="chip" data-g="1.1" data-fx="right">Fortuneo <i>?</i></div>
   <div class="chip" data-g="1.2" data-fx="right">BoursoBank <i>?</i></div></div>
  <div class="scene card" data-s="2" data-in="right"><div class="n">1 / 3 · PARRAINAGE</div><div class="b">Hello bank</div><div class="j">jusqu'à</div><div class="a" data-g="2.2" data-fx="stamp">330 €</div><br><div class="tg u" data-g="2.3" data-fx="up">⏳ parrainage avant le 09/11, 15h</div></div>
  <div class="scene card" data-s="3" data-in="right"><div class="n">2 / 3 · OFFRE DE BIENVENUE</div><div class="b">Fortuneo</div><div class="j">jusqu'à</div><div class="a" data-g="3.2" data-fx="stamp">260 €</div><br><div class="tg" data-g="3.3" data-fx="up">carte Gold · jusqu'au 20/12</div></div>
  <div class="scene card" data-s="4" data-in="right"><div class="n">3 / 3 · OFFRE DE BIENVENUE</div><div class="b">BoursoBank</div><div class="j">jusqu'à</div><div class="a" data-g="4.2" data-fx="stamp">180 €</div><br><div class="tg" data-g="4.3" data-fx="up">à l'ouverture du compte</div></div>
  <div id="s5" class="scene" data-s="5" data-in="pop"><div class="r">330 €</div><div class="r">+ 260 €</div><div class="r">+ 180 €</div><div class="ln"></div>
   <div class="tot" data-g="5.1" data-fx="stamp" data-slow="5.1" data-count="770"><span class="v">0 €</span></div></div>
  <div id="s6" class="scene" data-s="6"><div class="a">Envoie-moi</div><div class="k" data-g="6.1" data-fx="stamp">« PARRAINAGE »</div><div class="p">en privé</div><div class="d" data-g="6.2" data-fx="up">📌 Enregistre la vidéo pour plus tard</div>
   <div class="cond">Offres soumises aux conditions en vigueur<br>Montants maximum, chacun sous conditions<br>Fortuneo, BoursoBank : offres de bienvenue</div></div>
'''

SPLITS = [(0.0, 2.36), (2.77, 4.30), (4.65, 7.93), (8.38, 11.32), (11.94, 14.57), (14.85, 17.34), (17.69, 18.84)]
GAP = 0.22
TAIL = 1.35
