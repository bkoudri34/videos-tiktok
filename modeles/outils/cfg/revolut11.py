import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Revolut, 17/11/2026 18:00 - style v3 nuit & or, accent bleu glacier. Format « ouverture depuis le canapé », sans montant :
# pas de prime en argent pour le filleul, récompense du parrain selon l'offre en cours (variable selon les campagnes,
# affichée dans l'appli ; primebanque.fr, parrainage Revolut 2026, mise à jour du 08/10/2026, consultée le 17/11/2026).
# Voix : Speko (speechify, voix par défaut ; voix clonée refusée 402).
# Canapé + téléphone -> clavier / numéro -> pièce d'identité + selfie -> carte qui sort du téléphone (ralenti)
# -> colonne filleul (0 prime en argent) -> colonne parrain (cadeau selon l'offre) -> appel à l'action.
NAME = 'revolut11'
TITLE = 'Revolut canapé glacier'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Ton compte Revolut s'ouvre depuis ton canapé.", [("Ton compte Revolut", None), ("s'ouvre depuis", None), ("ton canapé.", None)]),
 ("Tu télécharges l'appli, et tu entres ton numéro.", [("Tu télécharges l'appli,", None), ("et tu entres ton numéro.", None)]),
 ("Photo de ta pièce d'identité, puis un selfie.", [("Photo de ta pièce d'identité,", None), ("puis un selfie.", None)]),
 ("Ensuite, tu commandes ta carte dans l'appli.", [("Ensuite,", None), ("tu commandes ta carte", None), ("dans l'appli.", None)]),
 ("Et le parrainage ? Pas de prime en argent pour le filleul.", [("Et le parrainage ?", None), ("Pas de prime en argent", None), ("pour le filleul.", None)]),
 ("Le parrain, lui, a une récompense, selon l'offre en cours.", [("Le parrain, lui,", None), ("a une récompense,", None), ("selon l'offre en cours.", None)]),
 ("Envoie-moi REVOLUT en privé, je t'envoie mon lien.", [("Envoie-moi", None), ("REVOLUT", None), ("en privé,", None), ("je t'envoie mon lien.", None)]),
]
SPLITS = [(0.0, 1.80), (2.41, 4.44), (4.87, 6.92), (7.64, 9.24), (9.82, 12.10), (12.76, 14.92), (15.29, 17.20)]
GSTART = [[0.1, 0.8, 1.3], [2.41, 3.61], [4.87, 6.36], [7.64, 8.0, 8.8], [9.82, 10.89, 11.6], [12.78, 13.3, 14.18], [15.29, 15.6, 16.0, 16.6]]
MINLEN = 1.9
GAP = 0.34
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.gl{color:#9fd8ff;text-shadow:0 0 18px rgba(120,200,255,.45)}
.sofa{position:absolute;left:150px;top:980px;width:780px;height:420px}
.pp{position:absolute;left:430px;top:720px;width:230px;height:420px;border-radius:36px;background:#0b0f14;border:7px solid #2e3640;box-shadow:0 0 70px rgba(120,200,255,.35),0 30px 80px rgba(0,0,0,.7);transform:rotate(-8deg);overflow:hidden}
.pp .sc{position:absolute;inset:14px;border-radius:24px;background:linear-gradient(170deg,#18324a,#0b1520);display:flex;align-items:center;justify-content:center;font:900 70px Inter;color:#9fd8ff}
.ph{position:absolute;left:300px;top:700px;width:480px;height:800px;border-radius:60px;background:#0b0f14;border:10px solid #2e3640;box-shadow:0 0 0 2px #4d5a66,0 30px 90px rgba(0,0,0,.7);padding:0 34px;overflow:hidden}
.ph .nt{width:130px;height:30px;background:#000;border-radius:0 0 18px 18px;margin:0 auto 30px}
.ph .t{font:800 26px Inter;letter-spacing:5px;color:#9fd8ff;text-align:center;margin-bottom:22px}
.fld{height:96px;border-radius:22px;border:4px solid #9fd8ff;background:rgba(159,216,255,.08);font:700 40px 'DejaVu Sans Mono',monospace;color:#fff;display:flex;align-items:center;padding:0 24px;white-space:nowrap;margin-bottom:30px}
.kp{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.kp i{height:96px;border-radius:50%;background:#1a222c;font:700 44px Inter;color:#e9eef4;font-style:normal;display:flex;align-items:center;justify-content:center}
.kp i.h{background:#9fd8ff;color:#0b1520}
.dl{position:absolute;left:600px;top:560px;width:270px;height:96px;border-radius:48px;background:#9fd8ff;color:#0b1520;font:900 34px Inter;display:flex;align-items:center;justify-content:center;gap:14px;box-shadow:0 20px 50px rgba(0,0,0,.6);transform:rotate(6deg)}
.scan{position:absolute;left:150px;top:720px;width:780px;height:470px}
.scan .c{position:absolute;width:70px;height:70px;border-color:#9fd8ff;border-style:solid;border-width:0}
.idc{position:absolute;left:90px;top:70px;width:600px;height:330px;border-radius:26px;background:linear-gradient(135deg,#f2f5f8,#c9d6e2);color:#14202c;box-shadow:0 30px 80px rgba(0,0,0,.6)}
.idc .k{position:absolute;left:40px;top:28px;font:800 26px 'DejaVu Sans Mono',monospace;letter-spacing:6px}
.idc .ph2{position:absolute;left:40px;top:90px;width:160px;height:200px;border-radius:16px;background:#9fb3c6}
.idc i{position:absolute;left:240px;height:22px;border-radius:11px;background:#9fb3c6}
.sline{position:absolute;left:60px;width:660px;height:6px;background:#9fd8ff;box-shadow:0 0 30px 6px rgba(159,216,255,.7)}
.self{position:absolute;left:330px;top:1220px;width:300px;height:300px;border-radius:50%;border:8px solid #9fd8ff;background:radial-gradient(circle at 50% 40%,#1c3348,#0b1520);overflow:hidden}
.okb{position:absolute;left:600px;top:1220px;width:110px;height:110px;border-radius:50%;background:#9fd8ff;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 30px rgba(0,0,0,.5)}
.php{position:absolute;left:180px;top:800px;width:360px;height:680px;border-radius:54px;background:#0b0f14;border:9px solid #2e3640;box-shadow:0 30px 90px rgba(0,0,0,.7);padding:40px 26px}
.php .bt{position:absolute;left:26px;right:26px;bottom:44px;height:90px;border-radius:45px;background:#9fd8ff;color:#0b1520;font:900 30px Inter;display:flex;align-items:center;justify-content:center}
.php .t{font:800 24px Inter;letter-spacing:4px;color:#9fd8ff;text-align:center;margin-top:30px}
.cd{position:absolute;left:440px;top:900px;width:440px;height:278px;border-radius:26px;background:linear-gradient(135deg,#e8f6ff,#9fd8ff 45%,#4a86b8);box-shadow:0 30px 80px rgba(0,0,0,.7),0 0 60px rgba(159,216,255,.3);color:#0b1520;transform:rotate(10deg)}
.cd .chip{position:absolute;left:38px;top:96px;width:74px;height:56px;border-radius:10px;background:linear-gradient(135deg,#fff1c4,#d9a24c)}
.cd .k{position:absolute;left:38px;top:32px;font:800 22px 'DejaVu Sans Mono',monospace;letter-spacing:5px}
.cd .n{position:absolute;left:38px;top:200px;font:700 28px 'DejaVu Sans Mono',monospace;letter-spacing:3px}
.col{position:absolute;top:700px;width:400px;height:640px;border-radius:34px;background:#0d1219;border:4px solid #33404d;text-align:center;padding-top:40px;box-shadow:0 30px 80px rgba(0,0,0,.6)}
.col .k{font:900 40px Inter;letter-spacing:6px;color:#e9eef4}
.col .z{margin-top:50px;font:900 150px 'DejaVu Serif',serif;color:#5d6873;line-height:1}
.col .s{margin-top:24px;font:700 30px Inter;color:#9aa6b2;line-height:1.35}
.col.on{border-color:#9fd8ff;box-shadow:0 0 50px rgba(159,216,255,.25),0 30px 80px rgba(0,0,0,.6)}
.xx{position:absolute;left:150px;top:910px;width:420px;height:12px;border-radius:6px;background:#ff5d5d;transform:rotate(-14deg);transform-origin:0 50%}
.gb{width:170px;height:170px;margin:40px auto 0;position:relative}
.gb .bx{position:absolute;left:10px;top:60px;width:150px;height:110px;border-radius:10px;background:#16263a;border:5px solid #f3c766}
.gb .ld{position:absolute;left:0;top:30px;width:170px;height:40px;border-radius:8px;background:#1d3350;border:5px solid #f3c766}
.gb .rv{position:absolute;left:70px;top:30px;width:30px;height:140px;background:#9fd8ff}
'''

SOFA = '''<svg class="sofa" viewBox="0 0 780 420" width="780" height="420">
 <rect x="60" y="40" width="660" height="200" rx="60" fill="#3a2c22"/>
 <rect x="0" y="150" width="140" height="220" rx="50" fill="#4a382b"/><rect x="640" y="150" width="140" height="220" rx="50" fill="#4a382b"/>
 <rect x="110" y="200" width="270" height="120" rx="34" fill="#5a4535"/><rect x="400" y="200" width="270" height="120" rx="34" fill="#5a4535"/>
 <rect x="60" y="300" width="660" height="70" rx="20" fill="#2d2219"/>
 <rect x="110" y="370" width="30" height="50" fill="#1c150f"/><rect x="640" y="370" width="30" height="50" fill="#1c150f"/>
 <rect x="150" y="110" width="150" height="110" rx="30" fill="#c9a36a" transform="rotate(-10)"/>
</svg>'''
FACE = '<svg width="300" height="300" viewBox="0 0 300 300"><circle cx="150" cy="125" r="62" fill="#f1c6a0"/><path d="M88 110 Q92 50 150 48 Q210 50 212 110 Q190 80 150 82 Q110 80 88 110 Z" fill="#2b1d14"/><path d="M50 300 Q60 200 150 196 Q240 200 250 300 Z" fill="#9fd8ff"/><circle cx="128" cy="128" r="6" fill="#222"/><circle cx="172" cy="128" r="6" fill="#222"/><path d="M130 158 Q150 172 170 158" stroke="#a5523f" stroke-width="6" fill="none" stroke-linecap="round"/></svg>'
OK = '<svg width="64" height="64" viewBox="0 0 100 100"><path d="M20 52 L42 74 L82 28" stroke="#0b1520" stroke-width="16" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
KP = ''.join(f'<i{" class=\"h\" data-g=\"1.1\" data-fx=\"tick\"" if k in (0, 6) else ""}>{k}</i>' for k in (1, 2, 3, 4, 5, 6, 7, 8, 9)) + '<i>+</i><i class="h" data-g="1.1" data-fx="tick">0</i><i>⌫</i>'
CRN = ''.join(f'<div class="c" style="{p}"></div>' for p in ('left:0;top:0;border-left-width:7px;border-top-width:7px', 'right:0;top:0;border-right-width:7px;border-top-width:7px', 'left:0;bottom:0;border-left-width:7px;border-bottom-width:7px', 'right:0;bottom:0;border-right-width:7px;border-bottom-width:7px'))

BODY = hud('FRANCE · DEPUIS LE CANAPÉ', 'APPLI') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(210, [('h1 gl', 'TON COMPTE REVOLUT', None, 'font-size:70px'), ('it gold', "s'ouvre depuis", None, 'font-size:84px'), ('it gold', 'ton canapé.', None, 'font-size:96px')]) + SOFA + '''
   <div class="pp"><div class="sc">€</div></div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1 s', "TU TÉLÉCHARGES L'APPLI,", '1.0', 'font-size:62px'), ('it gold', 'et tu entres ton numéro.', '1.1', 'font-size:68px')]) + '''
   <div class="ph"><div class="nt"></div><div class="t">INSCRIPTION</div><div class="fld"><span data-g="1.1" data-fx="type">06 •• •• •• ••</span></div><div class="kp">''' + KP + '''</div></div>
   <div class="dl" data-g="1.0" data-fx="pop">↓ INSTALLER</div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 s', "PHOTO DE TA PIÈCE", '2.0', ''), ('h1 s', "D'IDENTITÉ,", '2.0', ''), ('it gold', 'puis un selfie.', '2.1', 'font-size:80px')]) + '''
   <div class="scan">''' + CRN + '''<div class="idc" data-g="2.0" data-fx="pop"><div class="k">IDENTITÉ</div><div class="ph2"></div><i style="top:110px;width:280px"></i><i style="top:160px;width:220px"></i><i style="top:210px;width:250px"></i><i style="top:260px;width:180px"></i></div>
    <div class="sline" style="top:240px" data-g="2.0" data-fx="fade"></div></div>
   <div class="self" data-g="2.1" data-fx="pop">''' + FACE + '''</div><div class="okb" data-g="2.1" data-fx="stamp">''' + OK + '''</div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('h1 gl', 'ENSUITE,', '3.0', ''), ('it gold', 'tu commandes ta carte', '3.1', 'font-size:70px'), ('it gold', "dans l'appli.", '3.2', 'font-size:74px')]) + '''
   <div class="php"><div class="t">MA CARTE</div><div class="bt">COMMANDER</div></div>
   <div class="cd" data-g="3.1" data-fx="right" data-slow="3.1"><div class="k">MA CARTE</div><div class="chip"></div><div class="n">•••• 1711</div></div></div>
  <div class="scene" data-s="4" data-in="up">''' + hd(230, [('h1', 'ET LE PARRAINAGE ?', '4.0', 'font-size:72px'), ('it gold', 'Pas de prime en argent', '4.1', 'font-size:68px'), ('it gold', 'pour le filleul.', '4.2', 'font-size:72px')]) + '''
   <div class="col" style="left:120px" data-g="4.0" data-fx="left"><div class="k">FILLEUL</div><div class="z">0 €</div><div class="s">de prime<br>en argent</div></div>
   <div class="xx" data-g="4.1" data-fx="strike"></div>
   <div class="col" style="left:560px;opacity:.4"><div class="k">PARRAIN</div><div class="z">?</div></div></div>
  <div class="scene" data-s="5" data-in="right">''' + hd(230, [('h1 gl', 'LE PARRAIN, LUI,', '5.0', ''), ('it gold', 'a une récompense,', '5.1', 'font-size:74px')]) + '''
   <div class="col" style="left:120px;opacity:.4"><div class="k">FILLEUL</div><div class="z">0 €</div><div class="s">de prime<br>en argent</div></div>
   <div class="col on" style="left:560px" data-g="5.1" data-fx="pop"><div class="k">PARRAIN</div><div class="gb"><div class="bx"></div><div class="ld"></div><div class="rv"></div></div><div class="s" data-g="5.2" data-fx="up" style="color:#f3c766;font:700 italic 44px 'Liberation Serif',serif">selon l'offre<br>en cours</div></div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« REVOLUT »', '6.1', 'font-size:118px'), ('it gold', 'en privé,', '6.2', '')]) + '''
   <div class="pill" style="top:740px;border-color:rgba(159,216,255,.8)" data-g="6.3" data-fx="up"><div class="pin" style="background:#9fd8ff">✉</div><div><b>JE T'ENVOIE MON LIEN</b><span>directement en message privé</span></div></div>
   <div class="cond" style="top:900px">Offre soumise aux conditions en vigueur<br>récompense du parrain selon l'offre en cours (affichée dans l'appli)<br>pas de prime en argent pour le filleul</div></div>
'''
