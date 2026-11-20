import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Hello bank, 20/11/2026 18:00 - style v3 nuit & or, accent turquoise. Format F6 « le chemin de ta prime » :
# carte du chemin avec 4 jalons dès la 1re image -> étape 1 lien de parrainage -> 80 € Hello One / Hello Prime
# -> 12 mois cochés, +50 € Hello Prime -> bon d'achat 200 € mobilité -> fin du chemin 330 € (ralenti) + avant le 30/11 -> appel à l'action.
# Offre parrainage filleul (hellobank.fr/fr/votre-offre-parrainage, consultée le 20/11/2026) : 80 € Hello One ou Hello Prime,
# + 50 € Hello Prime sous réserve de 5 paiements ou retraits par mois sur les 12 premiers mois, bon d'achat 200 € (mobilité avec Hello Start+),
# « jusqu'à 330 € d'avantages pour votre filleul », avant le 30/11/2026 à 15h.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'hellobank13'
TITLE = 'Hello bank chemin turquoise'
ROOT = ':root{--bg:#05090a}'
LINES = [
 ("Parrainage Hello bank : voilà le chemin de ta prime.", [("Parrainage Hello bank :", None), ("voilà le chemin", None), ("de ta prime.", None)]),
 ("Étape un : tu ouvres ton compte avec un lien de parrainage.", [("Étape 1 :", None), ("tu ouvres ton compte", None), ("avec un lien de parrainage.", None)]),
 ("Quatre-vingts euros de prime, avec Hello One ou Hello Prime.", [("80 € de prime,", None), ("avec Hello One", None), ("ou Hello Prime.", None)]),
 ("Avec Hello Prime, cinq paiements par mois pendant un an : cinquante euros de plus.", [("Avec Hello Prime,", None), ("5 paiements par mois", None), ("pendant un an :", None), ("50 € de plus.", None)]),
 ("Et avec la mobilité bancaire, un bon d'achat de deux cents euros.", [("Et avec la mobilité", None), ("bancaire, un bon d'achat", None), ("de 200 €.", None)]),
 ("Jusqu'à trois cent trente euros, avant le trente novembre.", [("Jusqu'à 330 €,", None), ("avant le 30 novembre.", None)]),
 ("Envoie-moi HELLO BANK en privé, je t'envoie le lien.", [("Envoie-moi", None), ("HELLO BANK", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 2.37), (3.0, 5.81), (6.24, 8.73), (9.27, 12.77), (13.16, 15.72), (16.2, 18.11), (18.6, 20.7)]
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
.tq{color:#5ee6da;text-shadow:0 0 18px rgba(70,220,210,.5)}
.map{position:absolute;left:120px;top:600px;width:820px;height:860px}
.map svg{position:absolute;left:0;top:0}
.jl{position:absolute;display:flex;align-items:center;gap:22px;white-space:nowrap}
.jl .n{flex:none;width:96px;height:96px;border-radius:50%;background:#0d1d1f;border:6px solid #5ee6da;color:#eaffff;font:900 44px Inter;display:flex;align-items:center;justify-content:center;box-shadow:0 0 30px rgba(70,220,210,.4)}
.jl b{display:block;font:900 52px 'DejaVu Serif',serif;color:#5ee6da}
.jl span{font:700 30px Inter;color:#cfe9e7}
.flag{position:absolute;padding:18px 34px;border-radius:30px;background:linear-gradient(135deg,#fff1c4,#e9b456 50%,#a8701f);color:#2a1a05;font:900 64px 'DejaVu Serif',serif;white-space:nowrap;box-shadow:0 20px 60px rgba(0,0,0,.6)}
.lk{position:absolute;left:190px;top:720px;width:700px;border-radius:40px;background:#f2fbfa;color:#0d2a2a;padding:40px;box-shadow:0 30px 90px rgba(0,0,0,.7),0 0 0 5px rgba(70,220,210,.55);text-align:center}
.lk .u{display:flex;align-items:center;gap:18px;justify-content:center;font:700 34px 'DejaVu Sans Mono',monospace;color:#0e6b66;background:#dff3f1;border-radius:22px;padding:22px;white-space:nowrap}
.lk .bt{margin:34px auto 0;width:460px;height:110px;border-radius:55px;background:#12a89b;color:#fff;font:900 40px Inter;display:flex;align-items:center;justify-content:center;white-space:nowrap}
.lk .s{margin-top:22px;font:600 28px Inter;color:#4b6a68}
.off{position:absolute;top:740px;width:360px;height:380px;border-radius:36px;background:linear-gradient(160deg,#123033,#081416);border:5px solid #2b5052;text-align:center;padding-top:40px}
.off .k{font:800 30px Inter;color:#9fd6d1;letter-spacing:3px}
.off .nm{font:900 44px Inter;color:#eaffff;margin-top:10px;white-space:nowrap}
.off .cd{width:200px;height:126px;margin:30px auto 0;border-radius:16px;background:linear-gradient(135deg,#5ee6da,#0f7c74)}
.off.on{border-color:#5ee6da;box-shadow:0 0 40px rgba(70,220,210,.35)}
.tile{position:absolute;left:220px;width:640px;height:160px;border-radius:40px;background:#f2fbfa;color:#083735;display:flex;align-items:center;justify-content:center;gap:24px;font:900 92px 'DejaVu Serif',serif;box-shadow:0 20px 60px rgba(0,0,0,.6),0 0 0 5px rgba(70,220,210,.6);white-space:nowrap}
.tile small{font:800 32px Inter;color:#3d5f5c;letter-spacing:2px}
.cal{position:absolute;left:180px;top:720px;width:720px;display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.cal .m{height:110px;border-radius:22px;background:#0d1d1f;border:4px solid #2b5052;display:flex;flex-direction:column;align-items:center;justify-content:center;font:800 26px Inter;color:#9fd6d1;letter-spacing:2px}
.cal .m b{font:900 40px Inter;color:#5ee6da}
.bon{position:absolute;left:170px;top:760px;width:740px;height:330px;border-radius:30px;background:linear-gradient(135deg,#fff1c4,#e9b456 45%,#a8701f);color:#2a1a05;box-shadow:0 30px 80px rgba(0,0,0,.7);transform:rotate(-3deg)}
.bon:before,.bon:after{content:'';position:absolute;top:135px;width:60px;height:60px;border-radius:50%;background:#05090a}
.bon:before{left:-30px}.bon:after{right:-30px}
.bon .k{position:absolute;left:60px;top:44px;font:900 40px Inter;letter-spacing:4px}
.bon .v{position:absolute;left:60px;top:100px;font:900 150px 'DejaVu Serif',serif;line-height:1}
.bon .s{position:absolute;left:60px;top:262px;font:700 28px Inter;color:#4a3410}
.tot{position:absolute;left:0;width:1080px;text-align:center}
.tot .v{font:900 200px 'DejaVu Serif',serif;line-height:1}
.dl{position:absolute;left:290px;width:500px;height:120px;border-radius:24px;background:#f2fbfa;color:#083735;display:flex;align-items:center;justify-content:center;font:900 46px Inter;white-space:nowrap;box-shadow:0 0 0 5px #12a89b}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
LINK = '<svg width="46" height="46" viewBox="0 0 46 46"><path d="M19 27 L27 19" stroke="#0e6b66" stroke-width="5" stroke-linecap="round"/><path d="M21 13 l4-4 a8 8 0 0 1 12 12 l-4 4" fill="none" stroke="#0e6b66" stroke-width="5" stroke-linecap="round"/><path d="M25 33 l-4 4 a8 8 0 0 1 -12 -12 l4 -4" fill="none" stroke="#0e6b66" stroke-width="5" stroke-linecap="round"/></svg>'
PATH = '<svg width="820" height="860" viewBox="0 0 820 860"><path d="M70 60 L70 660" fill="none" stroke="#5ee6da" stroke-width="8" stroke-dasharray="6 22" stroke-linecap="round" opacity=".8"/></svg>'


def jalon(top, n, big, small, g=None, fx='left'):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    return f'<div class="jl" style="left:22px;top:{top}px"{a}><div class="n">{n}</div><div><b>{big}</b><span>{small}</span></div></div>'


MONTHS = ''.join(f'<div class="m" data-g="3.{1 if k < 6 else 2}" data-fx="tick">MOIS {k + 1}<b>✓</b></div>' for k in range(12))

BODY = hud('FRANCE · ITINÉRAIRE', 'HELLO BANK') + '''
  <div class="scene" data-s="0">''' + hd(215, [('h1 tq', 'PARRAINAGE HELLO BANK :', None, 'font-size:58px'), ('it gold', 'voilà le chemin', None, 'font-size:84px'), ('it gold', 'de ta prime.', None, 'font-size:84px')]) + '''
   <div class="map" style="top:580px">''' + PATH + jalon(12, 1, 'Ouverture', 'avec un lien de parrainage') + jalon(212, 2, '+80 €', 'Hello One ou Hello Prime') + jalon(412, 3, '+50 €', 'Hello Prime · 12 mois') + jalon(612, 4, '+200 €', "bon d'achat · mobilité") + '''
   <div class="flag" style="left:470px;top:760px">= 330 €</div></div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('big gold', 'Étape 1 :', '1.0', 'font-size:130px'), ('it gold', 'tu ouvres ton compte', '1.1', 'font-size:66px'), ('h1 tq', 'AVEC UN LIEN DE PARRAINAGE.', '1.2', 'font-size:50px')]) + '''
   <div class="lk" style="top:740px" data-g="1.1" data-fx="pop"><div class="u">''' + LINK + '''lien de parrainage</div><div class="bt" data-g="1.2" data-fx="stamp">Ouvrir mon compte</div><div class="s">le lien d'abord, l'inscription ensuite</div></div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('big gold', '80 € de prime,', '2.0', 'font-size:96px'), ('it gold', 'avec Hello One', '2.1', 'font-size:70px'), ('it tq', 'ou Hello Prime.', '2.2', 'font-size:70px')]) + '''
   <div class="off" style="left:150px" data-g="2.1" data-fx="left"><div class="k">OFFRE</div><div class="nm">HELLO ONE</div><div class="cd"></div></div>
   <div class="off on" style="left:570px" data-g="2.2" data-fx="right"><div class="k">OFFRE</div><div class="nm">HELLO PRIME</div><div class="cd"></div></div>
   <div class="tile" style="top:1190px" data-g="2.0" data-fx="stamp">+80 €<small>ÉTAPE 2</small></div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(215, [('h1 tq', 'AVEC HELLO PRIME,', '3.0', 'font-size:62px'), ('it gold', '5 paiements par mois', '3.1', 'font-size:70px'), ('it gold', 'pendant un an :', '3.2', 'font-size:70px')]) + '''
   <div class="cal" style="top:700px">''' + MONTHS + '''</div>
   <div class="tile" style="top:1150px" data-g="3.3" data-fx="stamp">+50 €<small>DE PLUS</small></div></div>
  <div class="scene" data-s="4" data-in="right">''' + hd(230, [('h1 tq', 'ET AVEC LA MOBILITÉ', '4.0', 'font-size:62px'), ('it gold', "bancaire, un bon d'achat", '4.1', 'font-size:66px'), ('big gold', 'de 200 €.', '4.2', 'font-size:120px')]) + '''
   <div class="bon" style="top:800px" data-g="4.1" data-fx="up"><div class="k">BON D'ACHAT</div><div class="v">200 €</div><div class="s">mobilité bancaire · validité limitée</div></div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="rays" style="top:640px"></div>''' + hd(215, [('h1 tq', "JUSQU'À", '5.0', ''), ('it gold', 'avant le 30 novembre.', '5.1', 'font-size:70px')]) + '''
   <div class="tot" style="top:720px" data-g="5.0" data-fx="stamp" data-slow="5.0" data-count="330"><div class="v gold">0 €</div></div>
   <div class="map" style="top:980px;height:300px"><div class="jl" style="left:0px;top:0" data-g="5.0" data-fx="left"><div class="n">2</div><div><b>80 €</b></div></div><div class="jl" style="left:275px;top:0" data-g="5.0" data-fx="up"><div class="n">3</div><div><b>50 €</b></div></div><div class="jl" style="left:550px;top:0" data-g="5.0" data-fx="right"><div class="n">4</div><div><b>200 €</b></div></div></div>
   <div class="dl" style="top:1170px" data-g="5.1" data-fx="pop">AVANT LE 30/11</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« HELLO BANK »', '6.1', 'font-size:100px'), ('it gold', 'en privé,', '6.2', '')]) + '''
   <div class="pill" style="top:760px;border-color:rgba(70,220,210,.85)" data-g="6.3" data-fx="up"><div class="pin" style="background:#12a89b;color:#fff">✉</div><div><b>JE T'ENVOIE LE LIEN</b><span>directement en message privé</span></div></div>
   <div class="search" style="top:900px" data-g="6.3" data-fx="fade">''' + SEARCH + '''<span data-g="6.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1040px;font-size:23px">Offre soumise aux conditions en vigueur · parrainage jusqu'au 30/11/2026 (15h)<br>80 € Hello One ou Hello Prime · + 50 € Hello Prime : 5 paiements ou retraits par mois<br>pendant 12 mois (revenus ≥ 1 500 €/mois) · bon d'achat 200 € : mobilité avec Hello Start+</div></div>
'''
