import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Hello bank, 22/11/2026 16:00 - style v3 nuit & or, accent vert émeraude. Format F8 « résultat d'abord » :
# notification « Virement reçu +80,00 € » (illustration) dès la 1re image -> 80 € Hello One ou Hello Prime (2 cartes)
# -> calendrier 12 mois cochés, +50 € le 13e mois avec Hello Prime -> mobilité Hello Start+ = bon d'achat 200 €
# -> total jusqu'à 330 € (ralenti) + avant le 30/11 -> appel à l'action, petite notification qui reboucle sur la 1re image.
# Offre parrainage filleul (hellobank.fr/fr/votre-offre-parrainage, consultée le 22/11/2026) : 80 € Hello One ou Hello Prime,
# + 50 € Hello Prime versés le 13e mois sous réserve de 5 paiements ou retraits par mois sur les 12 premiers mois,
# bon d'achat 200 € (mobilité Hello Start+), « jusqu'à 330 € d'avantages pour votre filleul », avant le 30/11/2026 à 15h.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'hellobank14'
TITLE = 'Hello bank virement emeraude'
ROOT = ':root{--bg:#04090a}'
LINES = [
 ("Parrainage Hello bank : regarde ce virement de quatre-vingts euros.", [("Parrainage Hello bank :", None), ("regarde ce virement", None), ("de 80 €.", None)]),
 ("C'est la prime du filleul, avec Hello One ou Hello Prime.", [("C'est la prime", None), ("du filleul,", None), ("avec Hello One", None), ("ou Hello Prime.", None)]),
 ("Avec Hello Prime : cinq paiements par mois pendant un an, et cinquante euros de plus.", [("Avec Hello Prime :", None), ("5 paiements par mois", None), ("pendant un an,", None), ("et 50 € de plus.", None)]),
 ("Tu changes de banque avec Hello Start plus ? Bon d'achat de deux cents euros.", [("Tu changes de banque", None), ("avec Hello Start+ ?", None), ("Bon d'achat", None), ("de 200 €.", None)]),
 ("Au total : jusqu'à trois cent trente euros d'avantages, avant le trente novembre.", [("Au total :", None), ("jusqu'à 330 €", None), ("d'avantages,", None), ("avant le 30 novembre.", None)]),
 ("Envoie-moi HELLO BANK en privé, je t'envoie le lien.", [("Envoie-moi", None), ("HELLO BANK", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 2.87), (3.48, 6.08), (6.69, 10.37), (11.04, 14.08), (14.77, 17.70), (18.34, 20.2)]
GSTART = [[0.0, 1.3, 2.1], [3.5, 3.9, 4.6, 5.4], [6.6, 7.6, 8.4, 9.2], [11.0, 11.6, 13.0, 13.4], [14.8, 15.2, 16.2, 16.9], [18.4, 18.7, 19.1, 19.5]]
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
.em{color:#46e0a6;text-shadow:0 0 18px rgba(50,220,150,.5)}
.ntf{position:absolute;left:140px;width:770px;height:150px;border-radius:36px;background:#f3f7f4;color:#0c1f17;display:flex;align-items:center;gap:26px;padding:0 34px;box-shadow:0 30px 80px rgba(0,0,0,.7),0 0 0 4px rgba(70,224,166,.55);white-space:nowrap}
.ntf .ic{flex:none;width:84px;height:84px;border-radius:22px;background:#13a874;color:#fff;display:flex;align-items:center;justify-content:center;font:900 48px Inter}
.ntf .tx{flex:1}
.ntf .tx b{display:block;font:800 36px Inter}
.ntf .tx span{font:600 24px Inter;color:#4d6a5d}
.ntf .am{font:900 50px Inter;color:#0d8f5f}
.ntf.sm{height:120px;left:190px;width:700px;gap:18px;padding:0 26px}.ntf.sm .ic{width:64px;height:64px;font-size:36px}.ntf.sm .tx b{font-size:30px}.ntf.sm .am{font-size:34px}.ntf.sm .tx span{font-size:21px}
.ill{position:absolute;left:0;width:1080px;text-align:center;font:600 24px Inter;color:#7f9a8e;letter-spacing:3px}
.amt{position:absolute;left:0;width:1080px;text-align:center}
.amt .v{font:900 210px 'DejaVu Serif',serif;line-height:1}
.offc{position:absolute;top:800px;width:360px;height:420px;border-radius:36px;text-align:center;padding-top:40px}
.offc .t{font:900 44px Inter;letter-spacing:2px;color:#eafaf3;white-space:nowrap}
.offc .cdx{margin:30px auto 0;width:260px;height:164px;border-radius:20px;box-shadow:0 20px 50px rgba(0,0,0,.6)}
.offc .v{margin-top:30px;font:900 84px 'DejaVu Serif',serif;white-space:nowrap}
.o1{left:150px;background:#0b1712;border:4px solid #2f6f55}
.o1 .cdx{background:linear-gradient(135deg,#2bd39a,#0f6e4e)}
.o2{left:570px;background:#141008;border:4px solid #e0ac55}
.o2 .cdx{background:linear-gradient(135deg,#fff1c4,#e9b456 45%,#a8701f)}
.months{position:absolute;left:170px;top:840px;width:740px;display:grid;grid-template-columns:repeat(6,110px);gap:18px 16px}
.months .m{height:110px;border-radius:24px;background:#0b1712;border:4px solid #2f6f55;display:flex;flex-direction:column;align-items:center;justify-content:center;font:800 24px Inter;color:#9fcfb9}
.months .m i{font-style:normal;font:900 40px Inter;color:#46e0a6;line-height:1}
.tile{position:absolute;left:200px;width:680px;height:160px;border-radius:40px;background:#f3f7f4;color:#0c1f17;display:flex;align-items:center;justify-content:center;gap:24px;font:900 96px 'DejaVu Serif',serif;box-shadow:0 20px 60px rgba(0,0,0,.6),0 0 0 5px rgba(70,224,166,.6);white-space:nowrap}
.tile small{font:800 30px Inter;color:#4d6a5d;letter-spacing:2px}
.bk{position:absolute;top:780px;width:290px;height:250px;border-radius:24px 24px 10px 10px;text-align:center;padding-top:150px;font:800 28px Inter;letter-spacing:2px;white-space:nowrap}
.bk:before{content:'';position:absolute;left:30px;right:30px;top:30px;height:90px;background:repeating-linear-gradient(90deg,currentColor 0 18px,transparent 18px 46px);opacity:.5}
.bk1{left:130px;background:#16181b;border:4px solid #50555c;color:#9aa0a8}
.bk2{left:640px;background:#0b1712;border:4px solid #46e0a6;color:#bff3dc}
.arr{position:absolute;left:450px;top:860px;width:170px;height:80px}
.vch{position:absolute;left:220px;top:1110px;width:640px;height:200px;border-radius:26px;background:#141008;border:5px dashed #e0ac55;display:flex;align-items:center;justify-content:center;gap:30px;white-space:nowrap}
.vch b{font:900 100px 'DejaVu Serif',serif}
.vch span{font:800 30px Inter;color:#f1ead9;letter-spacing:2px;line-height:1.3}
.stk{position:absolute;left:200px;width:680px}
.stk .r{height:96px;border-radius:28px;background:#0b1712;border:4px solid #2f6f55;margin-bottom:16px;display:flex;align-items:center;justify-content:space-between;padding:0 40px;font:800 34px Inter;color:#eafaf3;white-space:nowrap}
.stk .r b{font:900 50px 'DejaVu Serif',serif;color:#46e0a6}
.tot{position:absolute;left:0;width:1080px;text-align:center}
.tot .v{font:900 200px 'DejaVu Serif',serif;line-height:1}
.cal{position:absolute;left:300px;width:480px;height:100px;border-radius:24px;background:#f3f7f4;color:#0c1f17;display:flex;align-items:center;justify-content:center;font:900 40px Inter;white-space:nowrap;box-shadow:0 0 0 5px #13a874}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
ARR = '<svg class="arr" viewBox="0 0 170 80" data-g="3.1" data-fx="draw"><path d="M8 40 H140 M110 12 L150 40 L110 68" fill="none" stroke="#46e0a6" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def ntf(top, g=None, sm=False, fx='up'):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    return (f'<div class="ntf{" sm" if sm else ""}" style="top:{top}px"{a}><div class="ic">€</div><div class="tx"><b>Virement reçu</b>'
            f'<span>Prime de bienvenue · filleul</span></div><div class="am">+80,00 €</div></div>')


MONTHS = '<div class="months">' + ''.join(f'<div class="m" data-g="2.{1 if k < 6 else 2}" data-fx="tick"><i>✓</i>M{k + 1}</div>' for k in range(12)) + '</div>'

BODY = hud('FRANCE · PRIME FILLEUL', 'HELLO BANK') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(205, [('h1', 'PARRAINAGE', None, 'font-size:72px'), ('h1 em', 'HELLO BANK :', None, 'font-size:84px'), ('it gold', 'regarde ce virement', None, 'font-size:70px')]) + '''
   ''' + ntf(640) + '''
   <div class="ill" style="top:812px">ILLUSTRATION · PRIME DU FILLEUL</div>
   <div class="rays" style="top:860px"></div>
   <div class="amt" style="top:930px" data-g="0.2" data-fx="stamp"><div class="v gold">80 €</div></div>
   <div class="hd" style="top:1160px"><div class="it em" style="font-size:66px" data-g="0.1" data-fx="tw">de 80 €.</div></div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('it gold', "C'est la prime", '1.0', 'font-size:76px'), ('h1', 'DU FILLEUL,', '1.1', 'font-size:66px'), ('it em', 'avec Hello One', '1.2', 'font-size:66px'), ('it em', 'ou Hello Prime.', '1.3', 'font-size:66px')]) + '''
   <div class="offc o1" data-g="1.2" data-fx="left"><div class="t">HELLO ONE</div><div class="cdx"></div><div class="v em">80 €</div></div>
   <div class="offc o2" data-g="1.3" data-fx="right"><div class="t">HELLO PRIME</div><div class="cdx"></div><div class="v gold">80 €</div></div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('it gold', 'Avec Hello Prime :', '2.0', 'font-size:76px'), ('h1', '5 PAIEMENTS PAR MOIS', '2.1', 'font-size:58px'), ('it em', 'pendant un an,', '2.2', 'font-size:70px')]) + MONTHS + '''
   <div class="tile" style="top:1150px" data-g="2.3" data-fx="stamp">+50 €<small>LE 13e MOIS</small></div>
   <div class="cond" style="top:1340px;font-size:26px;color:#8fb3a3" data-g="2.3" data-fx="fade">5 paiements ou retraits par mois · 12 premiers mois · Hello Prime</div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('it gold', 'Tu changes de banque', '3.0', 'font-size:72px'), ('it em', 'avec Hello Start+ ?', '3.1', 'font-size:72px'), ('h1', "BON D'ACHAT", '3.2', 'font-size:66px')]) + '''
   <div class="bk bk1" data-g="3.0" data-fx="left">ANCIENNE<br>BANQUE</div>''' + ARR + '''<div class="bk bk2" data-g="3.1" data-fx="right">HELLO<br>BANK</div>
   <div class="vch" data-g="3.3" data-fx="stamp"><b class="gold">200 €</b><span>BON<br>D'ACHAT</span></div>
   <div class="cond" style="top:1350px;font-size:26px;color:#8fb3a3" data-g="3.3" data-fx="fade">avec le service de mobilité bancaire Hello Start+</div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:780px"></div>''' + hd(215, [('h1 em', 'AU TOTAL :', '4.0', 'font-size:72px')]) + '''
   <div class="stk" style="top:350px"><div class="r" data-g="4.0" data-fx="left">Prime d'ouverture<b>80 €</b></div><div class="r" data-g="4.0" data-fx="right">13e mois · Hello Prime<b>50 €</b></div><div class="r" data-g="4.0" data-fx="left">Bon d'achat · mobilité<b>200 €</b></div></div>
   <div class="hd" style="top:715px"><div class="it gold" style="font-size:70px" data-g="4.1" data-fx="tw">jusqu'à</div></div>
   <div class="tot" style="top:805px" data-g="4.1" data-fx="stamp" data-slow="4.1" data-count="330"><div class="v gold">0 €</div></div>
   <div class="hd" style="top:1030px"><div class="it em" style="font-size:64px" data-g="4.2" data-fx="tw">d'avantages,</div></div>
   <div class="cal" style="top:1140px" data-g="4.3" data-fx="pop">AVANT LE 30/11</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« HELLO BANK »', '5.1', 'font-size:78px'), ('it em', 'en privé,', '5.2', '')]) + '''
   <div class="pill" style="top:650px;border-color:rgba(70,224,166,.85)" data-g="5.3" data-fx="up"><div class="pin" style="background:#13a874;color:#fff">✉</div><div><b>JE T'ENVOIE LE LIEN</b><span>directement en message privé</span></div></div>
   <div class="search" style="top:790px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:920px;font-size:22px">Offre soumise aux conditions en vigueur<br>Nouveaux clients, avant le 30/11/2026 à 15h · 80 € à l'ouverture<br>(Hello One ou Hello Prime) · + 50 € le 13e mois avec Hello Prime<br>(5 paiements ou retraits par mois sur 12 mois)<br>Bon d'achat 200 € avec Hello Start+ (mobilité bancaire)</div>
   ''' + ntf(1130, '5.3', True, 'up') + '''</div>
'''
