import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Fortuneo, 16/11/2026 16:00 - style v3 nuit & or, accent bleu roi. Offre de bienvenue jusqu'à 260 € avec la carte Gold CB Mastercard
# (sous conditions de revenus) : 160 € après 5 paiements en 90 jours + 80 € mobilité bancaire + 20 € Livret +, jusqu'au 20/12/2026
# (sources : selectra.info, moneyvox.fr, francetransactions.com, consultées le 16/11/2026). Voix : Speko (speechify, voix par défaut ; voix clonée refusée 402).
# Carte Gold en gros plan -> fiche offre -> appli : 5 paiements cochés + barre 90 jours -> virement mobilité -> jauge du total 260 € (ralenti)
# -> calendrier 20 déc. J-34 -> appel à l'action.
NAME = 'fortuneo9'
TITLE = 'Fortuneo carte bleu roi'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Ta carte bancaire peut te rapporter deux cent soixante euros.", [("Ta carte bancaire", None), ("peut te rapporter", None), ("260 €.", None)]),
 ("C'est l'offre Fortunéo, avec la carte Gold.", [("C'est l'offre Fortuneo,", None), ("avec la carte Gold.", None)]),
 ("Cinq paiements en quatre-vingt-dix jours : cent soixante euros.", [("5 paiements", None), ("en 90 jours :", None), ("160 €.", None)]),
 ("Tu changes de banque : quatre-vingts euros de plus.", [("Tu changes de banque :", None), ("80 € de plus.", None)]),
 ("Un Livret plus, et encore vingt euros.", [("Un Livret +,", None), ("et encore 20 €.", None)]),
 ("Attention, l'offre s'arrête le vingt décembre.", [("Attention,", None), ("l'offre s'arrête", None), ("le 20 décembre.", None)]),
 ("Envoie-moi FORTUNÉO en privé, je t'envoie le lien.", [("Envoie-moi", None), ("FORTUNEO", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 2.41), (2.85, 4.80), (5.27, 7.85), (8.34, 10.14), (10.42, 12.06), (12.48, 14.46), (14.86, 16.76)]
GSTART = [[0.1, 0.8, 1.4], [2.9, 4.0], [5.3, 5.9, 7.1], [8.4, 9.3], [10.42, 11.3], [12.5, 13.3, 13.9], [14.86, 15.2, 15.6, 16.2]]
MINLEN = 2.0
GAP = 0.32
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.bl{color:#7db8ff;text-shadow:0 0 18px rgba(90,169,255,.5)}
.gc{position:absolute;width:560px;height:350px;border-radius:30px;background:linear-gradient(135deg,#f6dc8e 0%,#d6a347 40%,#8a5a18 100%);box-shadow:0 30px 80px rgba(0,0,0,.75),0 0 60px rgba(240,180,80,.25);color:#2a1a05;padding:36px 40px;font:900 34px Inter;letter-spacing:4px}
.gc i{display:block;width:96px;height:72px;border-radius:12px;background:linear-gradient(135deg,#fff1c4,#b98a3a);margin-top:40px}
.gc em{position:absolute;left:40px;bottom:36px;font:700 30px 'DejaVu Sans Mono',monospace;letter-spacing:5px;font-style:normal}
.gc u{position:absolute;right:40px;top:34px;width:110px;height:70px;text-decoration:none}
.gc u:before,.gc u:after{content:'';position:absolute;top:0;width:70px;height:70px;border-radius:50%;background:rgba(90,60,10,.35)}
.gc u:before{left:0}.gc u:after{right:0}
.qm{position:absolute;width:130px;height:130px;border-radius:50%;background:#5aa9ff;color:#06101e;font:900 90px Inter;display:flex;align-items:center;justify-content:center;box-shadow:0 20px 50px rgba(0,0,0,.6)}
.fiche{position:absolute;left:170px;top:880px;width:740px;border-radius:28px;background:#0d1320;border:4px solid #5aa9ff;box-shadow:0 30px 80px rgba(0,0,0,.7);padding:30px 40px}
.fiche .r{display:flex;justify-content:space-between;align-items:center;font:700 34px Inter;color:#e9e4da;padding:14px 0;border-bottom:2px dashed rgba(125,184,255,.3);white-space:nowrap}
.fiche .r:last-child{border:0}
.fiche .r b{font:900 40px 'DejaVu Serif',serif;color:#f3c766}
.app{position:absolute;left:190px;top:640px;width:700px;height:780px;border-radius:44px;background:#0b0f18;border:8px solid #2c2f37;box-shadow:0 0 0 2px #514a40,0 30px 90px rgba(0,0,0,.7);padding:34px 40px}
.app .t{font:800 28px Inter;letter-spacing:5px;color:#7db8ff;margin-bottom:14px}
.ln{display:flex;align-items:center;gap:22px;height:84px;border-bottom:2px solid rgba(255,255,255,.07);font:700 34px Inter;color:#e9e4da;white-space:nowrap}
.ln .bx{flex:none;width:52px;height:52px;border-radius:14px;background:#5aa9ff;color:#06101e;font:900 36px Inter;display:flex;align-items:center;justify-content:center}
.ln span{flex:1}.ln small{font:600 26px 'DejaVu Sans Mono',monospace;color:#8f877a}
.pg{margin-top:30px;height:34px;border-radius:17px;background:rgba(255,255,255,.08);overflow:hidden}
.pg i{display:block;height:100%;width:100%;background:linear-gradient(90deg,#5aa9ff,#f3c766);transform-origin:0 50%}
.pgl{display:flex;justify-content:space-between;font:700 24px 'DejaVu Sans Mono',monospace;color:#8f877a;margin-top:10px}
.big160{position:absolute;left:0;top:1440px;width:1080px;text-align:center}
.nt{position:absolute;left:150px;width:780px;height:150px;border-radius:30px;background:rgba(242,246,255,.97);color:#0e1626;display:flex;align-items:center;gap:24px;padding:0 30px;box-shadow:0 26px 70px rgba(0,0,0,.6);white-space:nowrap}
.nt .ic{flex:none;width:84px;height:84px;border-radius:22px;background:#2d6fd6;color:#fff;font:900 46px Inter;display:flex;align-items:center;justify-content:center}
.nt .x{flex:1}.nt .x b{display:block;font:800 32px Inter}.nt .x span{font:600 24px Inter;color:#5d6780}
.nt .a{font:900 58px 'DejaVu Serif',serif;color:#1f5fc4}
.bk{position:absolute;top:1020px;width:220px;height:240px;text-align:center}
.bk .roof{width:0;height:0;margin:0 auto;border-left:110px solid transparent;border-right:110px solid transparent;border-bottom:70px solid #8a7f69}
.bk .cols{height:150px;background:repeating-linear-gradient(90deg,#8a7f69 0 26px,transparent 26px 46px);margin:10px 12px 0}
.bk .base{height:20px;background:#8a7f69;margin-top:6px}
.bk.on .roof{border-bottom-color:#5aa9ff}.bk.on .cols{background:repeating-linear-gradient(90deg,#5aa9ff 0 26px,transparent 26px 46px)}.bk.on .base{background:#5aa9ff}
.bk small{display:block;font:800 26px Inter;letter-spacing:3px;color:#e9e4da;margin-top:16px}
.arw{position:absolute;left:420px;top:1080px;width:240px;height:10px;background:#f3c766;transform-origin:0 50%;border-radius:5px}
.arw:after{content:'';position:absolute;right:-18px;top:-16px;border:21px solid transparent;border-left:26px solid #f3c766;border-right:0}
.gauge{position:absolute;left:240px;top:700px;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,#0d1320 58%,transparent 59%),conic-gradient(from -135deg,#5aa9ff 0 166deg,#7db8ff 166deg 249deg,#f3c766 249deg 270deg,rgba(255,255,255,.06) 270deg)}
.gauge .c{position:absolute;left:0;top:190px;width:100%;text-align:center}
.gauge .c .k{font:800 30px Inter;letter-spacing:6px;color:#e9e4da}
.gauge .c .v{font:900 150px 'DejaVu Serif',serif;line-height:1.1}
.leg{position:absolute;left:150px;top:1340px;width:780px;display:flex;justify-content:space-around;font:800 30px Inter;color:#e9e4da;white-space:nowrap}
.leg i{display:inline-block;width:26px;height:26px;border-radius:7px;margin-right:12px;vertical-align:-3px}
.cal{position:absolute;left:290px;top:760px;width:500px;height:540px;border-radius:30px;background:#f4efe4;color:#14161c;text-align:center;box-shadow:0 40px 90px rgba(0,0,0,.7);overflow:hidden}
.cal .top{height:120px;background:#2d6fd6;color:#fff;font:900 52px Inter;letter-spacing:8px;line-height:120px}
.cal .d{font:900 260px 'DejaVu Serif',serif;line-height:1.2}
.cal .y{font:800 34px Inter;letter-spacing:8px;color:#5d6780}
.ring{position:absolute;top:-24px;width:30px;height:70px;border-radius:15px;background:#2c2f37;border:4px solid #8a7f69}
.jtag{position:absolute;left:640px;top:1180px;padding:18px 34px;border-radius:20px;background:#e5322d;color:#fff;font:900 64px 'DejaVu Sans Mono',monospace;transform:rotate(-8deg);box-shadow:0 20px 50px rgba(0,0,0,.6)}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'

CARD = '<div class="gc" style="{st}"{a}>CARTE GOLD<u></u><i></i><em>•••• •••• •••• 2026</em></div>'
LN = ''.join(f'<div class="ln" data-g="2.{0 if k < 3 else 1}" data-fx="tick"><div class="bx">✓</div><span>Paiement {k + 1}</span><small>J+{(4, 11, 23, 37, 58)[k]}</small></div>' for k in range(5))

BODY = hud('FRANCE · CARTE GOLD', 'BIENVENUE') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(210, [('h1', 'TA CARTE BANCAIRE', None, 'font-size:70px'), ('it gold', 'peut te rapporter', None, 'font-size:76px'), ('big gold', '260 €', None, 'font-size:170px')]) + '''
   ''' + CARD.format(st='left:250px;top:920px;transform:rotate(-7deg)', a='') + '''<div class="qm" style="left:740px;top:860px">?</div></div>
  <div class="scene" data-s="1" data-in="pop"><div class="rays" style="top:640px"></div>''' + hd(230, [('h1', "C'EST L'OFFRE", '1.0', ''), ('h1 bl', 'FORTUNEO,', '1.0', 'font-size:88px'), ('it gold', 'avec la carte Gold.', '1.1', 'font-size:72px')]) + '''
   ''' + CARD.format(st='left:260px;top:700px;transform:rotate(4deg)', a=' data-g="1.1" data-fx="pop"') + '''
   <div class="fiche" style="top:1110px;padding:20px 40px" data-g="1.1" data-fx="up"><div class="r"><span>Carte</span><b>Gold CB Mastercard</b></div><div class="r"><span>Condition</span><span style="color:#7db8ff">revenus requis</span></div></div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 bl', '5 PAIEMENTS', '2.0', 'font-size:84px'), ('it gold', 'en 90 jours :', '2.1', 'font-size:72px')]) + '''
   <div class="app" style="top:520px;height:640px;transform:scale(.86);transform-origin:50% 0"><div class="t">MES PAIEMENTS CARTE</div>''' + LN + '''
    <div class="pg"><i data-g="2.1" data-fx="grow"></i></div><div class="pgl"><span>J0</span><span>J90</span></div></div>
   <div class="big160 big gold" style="top:1110px;font-size:130px" data-g="2.2" data-fx="stamp">160 €</div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('h1', 'TU CHANGES', '3.0', ''), ('h1', 'DE BANQUE :', '3.0', ''), ('it gold', '80 € de plus.', '3.1', 'font-size:84px')]) + '''
   <div class="bk" style="left:170px"><div class="roof"></div><div class="cols"></div><div class="base"></div><small>AVANT</small></div>
   <div class="arw" data-g="3.0" data-fx="grow"></div>
   <div class="bk on" style="left:690px" data-g="3.0" data-fx="pop"><div class="roof"></div><div class="cols"></div><div class="base"></div><small>FORTUNEO</small></div>
   <div class="nt" style="top:720px" data-g="3.1" data-fx="right"><div class="ic">€</div><div class="x"><b>Mobilité bancaire</b><span>prime de bienvenue</span></div><div class="a">+80 €</div></div></div>
  <div class="scene" data-s="4" data-in="pop">''' + hd(230, [('h1 bl', 'UN LIVRET +,', '4.0', ''), ('it gold', 'et encore 20 €.', '4.1', 'font-size:80px')]) + '''
   <div class="gauge" data-g="4.0" data-fx="pop"><div class="c" data-g="4.1" data-fx="tick" data-slow="4.1" data-count="260"><div class="k">TOTAL JUSQU'À</div><div class="v gold">0 €</div></div></div>
   <div class="leg" data-g="4.1" data-fx="fade"><span><i style="background:#5aa9ff"></i>160 carte</span><span><i style="background:#7db8ff"></i>80 mobilité</span><span><i style="background:#f3c766"></i>20 livret</span></div></div>
  <div class="scene" data-s="5" data-in="up">''' + hd(230, [('h1', 'ATTENTION,', '5.0', ''), ('it gold', "l'offre s'arrête", '5.1', 'font-size:74px'), ('it gold', 'le 20 décembre.', '5.2', 'font-size:74px')]) + '''
   <div class="cal" data-g="5.0" data-fx="up"><div class="ring" style="left:120px"></div><div class="ring" style="left:350px"></div><div class="top">DÉCEMBRE</div><div class="d">20</div><div class="y">2026</div></div>
   <div class="jtag" data-g="5.2" data-fx="stamp">J-34</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« FORTUNEO »', '6.1', 'font-size:96px'), ('it gold', 'en privé,', '6.2', '')]) + '''
   <div class="pill" style="top:740px;border-color:rgba(90,169,255,.8)" data-g="6.3" data-fx="up"><div class="pin" style="background:#5aa9ff;color:#06101e">✉</div><div><b>JE T'ENVOIE LE LIEN</b><span>offre valable jusqu'au 20/12</span></div></div>
   <div class="search" style="top:880px" data-g="6.3" data-fx="fade">''' + SEARCH + '''<span data-g="6.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1020px">Offre soumise aux conditions en vigueur · 1re ouverture de compte<br>jusqu'à 260 € avec la carte Gold (sous conditions de revenus) :<br>160 € après 5 paiements en 90 jours + 80 € mobilité + 20 € Livret +<br>· jusqu'au 20/12/2026</div></div>
'''
