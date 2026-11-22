import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from tuto import *
from qg_figs import *
# Vidéos QG du 22/11/2026, vidéo 2 : BoursoBank. Style T « tuto illustré » (personnages blancs animés).
# Format F8 « résultat d'abord » : la notification « Virement reçu +80,00 € » dès la 1re image, puis d'où viennent les 260 €.
# Source : https://www.boursobank.com/bon-plan/parrainage-boursobank (consultée le 22/11/2026), « Détails des conditions » :
# 1re ouverture d'un compte bancaire individuel ; 20 € à l'ouverture effective (au plus tard 2 mois après) ; 80 € pour un 1er
# versement d'au moins 300 € pendant l'ouverture ou dans les 30 jours (10 € de 1 à 49 €, 40 € de 50 à 299 €), crédités dans les
# 7 jours ; 80 € pour au moins 1 opération carte par mois pendant 3 mois (20 € + 30 € + 30 €) ; 80 € pour la 1re mobilité
# EasyMove (formulaire signé dans le mois suivant l'ouverture, versés au plus tard 60 jours après) ; soit 260 € maximum ;
# primes reprises en cas de clôture dans les 24 mois (et prime mobilité si la domiciliation n'est pas maintenue 24 mois).
# Voix : Mathieu (inworld-tts-2), une réplique par synthèse, atempo 1.06, pauses internes > 0,28 s raccourcies.
NAME = 'qg_boursorama2'
TITLE = 'QG BoursoBank résultat d abord'
JS = 'const CAM=0.6, PUSH=0.010;' + FIGJS
GAP = 0.28
TAIL = 1.6
MINLEN = 1.8
LINES = [
 ("Parrainage BoursoBank : ce virement de 80&nbsp;€, tu peux l'avoir rien qu'en versant 300&nbsp;€ sur ton nouveau compte.",
  [("<em>Parrainage BoursoBank</em>&nbsp;:", None), ("ce virement de <em>80&nbsp;€</em>,", None), ("tu peux l'avoir", None), ("rien qu'en versant <i>300&nbsp;€</i>", None), ("sur ton nouveau compte.", None)]),
 ("Avec un lien de parrainage : 20&nbsp;€ à l'ouverture,",
  [("Avec un <em>lien de parrainage</em>&nbsp;:", None), ("<em>20&nbsp;€</em> à l'ouverture,", None)]),
 ("80&nbsp;€ si tu verses 300&nbsp;€, 80&nbsp;€ pour un paiement carte par mois pendant trois mois,",
  [("<em>80&nbsp;€</em> si tu verses 300&nbsp;€,", None), ("<em>80&nbsp;€</em> pour un paiement carte", None), ("par mois", None), ("pendant <i>3 mois</i>,", None)]),
 ("et encore 80&nbsp;€ avec le transfert EasyMove.",
  [("et encore <em>80&nbsp;€</em>", None), ("avec le transfert EasyMove.", None)]),
 ("Total : jusqu'à 260&nbsp;€, si tu gardes ton compte deux ans.",
  [("Total :", None), ("jusqu'à <em>260&nbsp;€</em>,", None), ("si tu gardes ton compte", None), ("<i>2 ans</i>.", None)]),
 ("Envoie-moi le mot Bourso en privé, je t'envoie mon lien.",
  [("Envoie-moi le mot <em>BOURSO</em>", None), ("en privé,", None), ("je t'envoie mon lien.", None)]),
]
SPLITS = [(0.05, 5.831), (6.331, 9.143), (9.643, 14.9), (15.4, 18.196), (18.695, 22.278), (22.778, 25.41)]

CSS = FIGCSS + '''
#sub{left:60px;width:850px}
.endc .c{font-size:96px;white-space:nowrap}
.lock{position:absolute;width:470px;height:840px;border:9px solid #111;border-radius:66px;background:#eef3fb;box-shadow:12px 14px 0 #111;overflow:hidden}
.lock:before{content:'';position:absolute;left:165px;top:18px;width:120px;height:26px;border-radius:13px;background:#111}
.lock .hr{position:absolute;left:0;right:0;top:90px;text-align:center;font:800 120px/1 Inter;color:#111}
.lock .dt{position:absolute;left:0;right:0;top:220px;text-align:center;font:700 30px Inter;color:#555}
.nt{position:absolute;left:22px;right:22px;top:300px;background:#fff;border:5px solid #111;border-radius:30px;padding:18px 20px;box-shadow:6px 7px 0 #111}
.nt .a{font:700 22px Inter;color:#666}
.nt .b{font:900 32px Inter;margin-top:4px}
.nt .m{font:900 70px/1.05 Inter;color:#1b8a3c;margin-top:6px;white-space:nowrap}
.bigG{position:absolute;font:900 150px/1 Inter;color:#1b8a3c;white-space:nowrap;letter-spacing:-4px}
.mo{position:absolute;width:230px;height:250px;background:#fff;border:6px solid #111;border-radius:24px;box-shadow:8px 9px 0 #111;text-align:center;overflow:hidden}
.mo .top{height:64px;background:#e63946;border-bottom:6px solid #111;color:#fff;font:900 34px/58px Inter}
.mo .v{font:900 72px/1.4 Inter;color:#1b8a3c}
.mo .s{font:800 26px Inter}
.bk{position:absolute;width:260px;height:230px;text-align:center;font:900 34px Inter}
.lst{position:absolute;left:70px;width:800px;padding:20px 34px}
.lst .r{display:flex;align-items:center;gap:22px;font:800 42px Inter;white-space:nowrap;height:96px}
.lst .r .p{margin-left:auto;font:900 56px Inter;color:#1b8a3c}
.lst .tt{border-top:6px solid #111;margin-top:10px;padding-top:10px;display:flex;font:900 64px Inter;white-space:nowrap}
.lst .tt .p{margin-left:auto}
'''

BANK = ('<path d="M20 70 L120 14 L220 70 Z"/><path d="M30 78 L210 78"/><path d="M50 92 L50 170 M95 92 L95 170 M145 92 L145 170 M190 92 L190 170"/>'
        '<path d="M22 182 L218 182"/>')

BODY = '''
  <div class="scene" data-s="0">''' + title('Parrainage<br><mark>BoursoBank</mark>', 210, size=86) + '''
   <div class="lock" style="left:430px;top:450px"><div class="hr">09:41</div><div class="dt">dimanche 22 novembre</div>
    <div class="nt"><div class="a">BANQUE · maintenant</div><div class="b">Virement reçu</div><div class="m">+80,00 €</div></div></div>''' + \
    circle(405, 715, 520, 300, '0.1', -3) + guy(110, 640, 'spiky', 'open', 'up', 0.95) + '''
   <div class="note" style="left:60px;top:1150px;font-size:48px;transform:rotate(-4deg)" data-g="0.3" data-fx="stamp">si 300 € versés !</div>
   <div class="note" style="left:470px;top:1310px;font-size:30px;color:#111;transform:rotate(-2deg)" data-g="0.1" data-fx="pop">prime filleul si conditions remplies</div></div>
  <div class="scene" data-s="1" data-in="right">''' + title('Étape <mark>1</mark> : le lien', 220, size=80) + '''
   <div class="phone" style="left:470px;top:400px"><div class="scr"><div class="tt">Ouverture</div><div class="ln"></div><div class="ln" style="width:70%"></div>
    <div class="fl">Lien parrain ✓</div><div class="bt">Ouvrir mon compte</div><div class="ln" style="margin-top:40px"></div><div class="ln" style="width:55%"></div></div></div>''' + \
    guy(110, 560, 'cap', 'smile', 'point', 0.95) + '''
   <div class="bigG" style="left:90px;top:1200px" data-g="1.1" data-fx="stamp">+20 €</div>
   <div class="note" style="left:560px;top:1250px;font-size:44px;transform:rotate(-3deg)" data-g="1.1" data-fx="pop">à l'ouverture</div></div>
  <div class="scene" data-s="2" data-in="right">''' + title('Étapes <mark>2</mark> et <mark>3</mark>', 220, size=80) + '''
   <div class="paper" style="left:70px;top:380px;width:800px;height:220px;padding:26px 34px" data-g="2.0" data-fx="left">
    <div style="font:800 40px Inter">1<sup>er</sup> versement ≥ 300 €</div><div style="font:700 28px Inter;color:#555;margin-top:6px">dans les 30 jours</div>
    <div style="position:absolute;right:30px;top:56px;font:900 90px Inter;color:#1b8a3c">+80 €</div></div>
   <div class="mo" style="left:70px;top:700px" data-g="2.1" data-fx="up"><div class="top">MOIS 1</div><div class="v">20 €</div><div class="s">1 paiement carte</div></div>
   <div class="mo" style="left:355px;top:700px" data-g="2.2" data-fx="up"><div class="top">MOIS 2</div><div class="v">30 €</div><div class="s">1 paiement carte</div></div>
   <div class="mo" style="left:640px;top:700px" data-g="2.3" data-fx="up"><div class="top">MOIS 3</div><div class="v">30 €</div><div class="s">1 paiement carte</div></div>''' + \
    underline2(120, 980, 700, '2.3') + '''
   <div class="note" style="left:250px;top:1040px;font-size:52px;transform:rotate(-3deg)" data-g="2.3" data-fx="stamp">= +80 € carte</div></div>
  <div class="scene" data-s="3" data-in="up">''' + title('Étape <mark>4</mark> : EasyMove', 220, size=80) + \
    svg(80, 450, 240, 200, BANK, 'ink') + svg(600, 450, 240, 200, BANK, 'ink') + '''
   <div class="tag" style="left:90px;top:670px">ancienne banque</div><div class="tag" style="left:600px;top:670px;background:#ffe14d">nouveau compte</div>''' + \
    arrow(330, 520, 260, 80, 'M0 40 Q130 -10 250 40 M215 15 L252 41 L212 62', '3.0') + '''
   <div class="note" style="left:300px;top:430px;font-size:36px;color:#111" data-g="3.0" data-fx="pop">prélèvements, salaire…</div>
   <div class="bigG" style="left:280px;top:800px" data-g="3.0" data-fx="stamp">+80 €</div>
   <div class="note" style="left:80px;top:1000px;font-size:42px;transform:rotate(-2deg)" data-g="3.1" data-fx="pop">formulaire signé dans le mois</div>''' + \
    guy(720, 870, 'bun', 'smile', 'up', 0.72) + '''</div>
  <div class="scene" data-s="4" data-in="right">''' + title('Le <mark>total</mark>', 220, size=86) + '''
   <div class="paper lst" style="top:380px"><div class="r" data-g="4.0" data-fx="left">ouverture<span class="p">20 €</span></div>
    <div class="r" data-g="4.0" data-fx="left">1er versement ≥ 300 €<span class="p">80 €</span></div>
    <div class="r" data-g="4.0" data-fx="left">carte 3 mois<span class="p">80 €</span></div>
    <div class="r" data-g="4.0" data-fx="left">EasyMove<span class="p">80 €</span></div>
    <div class="tt" data-g="4.1" data-fx="stamp">jusqu'à<span class="p" style="background:#ffe14d;padding:0 14px">260 €</span></div></div>''' + \
    '''
   <div class="note" style="left:90px;top:1010px;font-size:40px;width:780px;text-align:center;white-space:normal;transform:rotate(-2deg)" data-g="4.2" data-fx="pop">compte gardé 24 mois, sinon primes reprises</div>''' + \
    guy(40, 1080, 'cap', 'smile', 'up', 0.5) + '''</div>
  <div class="scene" data-s="5" data-in="pop">
   <div class="endc" data-g="5.0" data-fx="up"><div class="k">ENVOIE-MOI EN PRIVÉ</div><div class="c">« BOURSO »</div><div class="d">je t'envoie mon lien</div><div class="b">@htm.invest</div></div>
   <div class="note" style="left:300px;top:770px;transform:rotate(-3deg)" data-g="5.1" data-fx="pop">parrainage BoursoBank</div>''' + \
    guy(90, 850, 'spiky', 'smile', 'up', 0.55) + '''
   <div class="cond" style="top:860px;left:270px;width:640px">Offre soumise aux conditions en vigueur.<br>Parrainage BoursoBank, conditions consultées le 22/11/2026 sur boursobank.com : 1re ouverture d'un compte individuel ; 20 € à l'ouverture ; 80 € pour un 1er versement d'au moins 300 € (à l'ouverture ou dans les 30 jours) ; 80 € pour au moins 1 opération carte par mois pendant 3 mois (20 + 30 + 30 €) ; 80 € pour une 1re mobilité EasyMove signée dans le mois. Primes reprises si le compte est clôturé dans les 24 mois.<br>Lien de parrainage : je touche une prime.</div></div>
'''
