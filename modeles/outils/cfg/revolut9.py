import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Revolut, 14/11/2026 16:00 - style v3 nuit & or, accent bleu glacier. Pas de montant (récompense parrain selon l'offre en cours,
# pas de prime en argent pour le filleul ; nextbanq.fr 30/10/2026). Voix : Speko (speechify, voix par défaut), voix clonée refusée (402).
# Rideau d'agence baissé -> appli sur le téléphone -> checklist pièce d'identité / selfie / c'est parti -> carte virtuelle
# -> médaille parrain -> pièce barrée filleul -> appel à l'action.
NAME = 'revolut9'
TITLE = 'Revolut glacier'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Pas besoin d'agence pour ouvrir un compte.", [("Pas besoin d'agence", None), ("pour ouvrir un compte.", None)]),
 ("Avec Revolut, tout se passe dans l'appli.", [("Avec Revolut,", None), ("tout se passe", None), ("dans l'appli.", None)]),
 ("Une pièce d'identité, un selfie, et c'est parti.", [("Une pièce d'identité,", None), ("un selfie,", None), ("et c'est parti.", None)]),
 ("Ta carte virtuelle, tu la retrouves dans l'appli.", [("Ta carte virtuelle,", None), ("tu la retrouves", None), ("dans l'appli.", None)]),
 ("Tu parraines ? Une récompense pour toi, selon l'offre en cours.", [("Tu parraines ?", None), ("une récompense pour toi,", None), ("selon l'offre en cours.", None)]),
 ("Ton filleul, lui, n'a pas de prime en argent.", [("Ton filleul, lui,", None), ("n'a pas de prime en argent.", None)]),
 ("Envoie-moi REVOLUT en privé, je t'envoie mon lien.", [("Envoie-moi", None), ("REVOLUT", None), ("en privé,", None), ("je t'envoie mon lien.", None)]),
]
SPLITS = [(0.0, 1.50), (1.97, 3.49), (3.91, 5.87), (6.32, 7.85), (8.37, 10.75), (11.28, 12.49), (13.06, 14.70)]
GSTART = [[0.1, 0.7], [2.0, 2.7, 3.1], [3.91, 4.8, 5.43], [6.32, 7.1, 7.5], [8.37, 9.16, 10.12], [11.28, 11.8], [13.06, 13.4, 13.7, 14.19]]
MINLEN = 2.0
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
.gl{color:#8fdcff;text-shadow:0 0 18px rgba(127,211,255,.5)}
.shop{position:absolute;left:190px;top:700px;width:700px;height:640px}
.shop .aw{position:absolute;left:0;top:0;width:700px;height:90px;background:repeating-linear-gradient(90deg,#5c5446 0 70px,#3a352c 70px 140px);border-radius:12px 12px 0 0}
.shop .sh{position:absolute;left:40px;top:90px;width:620px;height:520px;background:repeating-linear-gradient(180deg,#4b463c 0 26px,#2c2822 26px 32px);border:6px solid #5c5446;border-top:0}
.shop .tag{position:absolute;left:190px;top:270px;width:320px;padding:18px 0;background:#f4efe4;color:#1c1310;text-align:center;font:900 46px Inter;letter-spacing:6px;border-radius:12px;transform:rotate(-5deg);box-shadow:0 20px 40px rgba(0,0,0,.6)}
.shop .tag small{display:block;font:700 22px Inter;letter-spacing:4px;color:#6d5f55}
.glow{position:absolute;left:600px;top:1060px;width:210px;height:380px;border-radius:34px;background:#0d0c0b;border:7px solid #2c2925;box-shadow:0 0 0 2px #514a40,0 0 70px rgba(127,211,255,.55);transform:rotate(8deg)}
.glow:before{content:'';position:absolute;inset:18px 12px;border-radius:20px;background:linear-gradient(160deg,#2a6f96,#0c1f2e)}
.glow:after{content:'✓';position:absolute;left:0;top:130px;width:100%;text-align:center;font:900 90px Inter;color:#fff}
.ph .scr{position:absolute;inset:60px 24px 30px;border-radius:30px;background:linear-gradient(170deg,#173547,#0b141b);text-align:left;padding:34px 26px}
.ph .ap{font:900 40px Inter;color:#fff;margin-bottom:30px;text-align:center}
.ph .row{display:flex;align-items:center;gap:20px;height:120px;border-radius:24px;background:rgba(127,211,255,.12);border:2px solid rgba(127,211,255,.45);margin-bottom:22px;padding:0 22px;font:800 34px Inter;color:#e9f6ff}
.ph .row i{font-style:normal;width:64px;height:64px;border-radius:50%;background:#7fd3ff;color:#0b141b;display:flex;align-items:center;justify-content:center;font:900 32px 'DejaVu Sans'}
.stp{position:absolute;left:150px;width:780px;height:180px;border-radius:30px;background:rgba(20,40,54,.65);border:3px solid #d9a24c;display:flex;align-items:center;gap:34px;padding:0 34px}
.stp .ic{flex:none;width:130px;height:130px;border-radius:24px;background:#f4efe4;display:flex;align-items:center;justify-content:center}
.stp .tx{font:800 44px Inter;color:#fff;white-space:nowrap}
.stp .ok{margin-left:auto;width:80px;height:80px;border-radius:50%;background:#7fd3ff;color:#0b141b;font:900 46px Inter;display:flex;align-items:center;justify-content:center}
.vc{position:absolute;left:230px;top:760px;width:620px;height:390px;border-radius:34px;background:linear-gradient(135deg,#bfefff 0%,#5fb8e6 45%,#1f5f86 100%);box-shadow:0 30px 80px rgba(0,0,0,.7),0 0 70px rgba(127,211,255,.4);color:#08202e;padding:40px 44px;transform:rotate(-5deg)}
.vc .nm{font:900 34px Inter;letter-spacing:4px}.vc .chip{width:96px;height:72px;border-radius:12px;background:linear-gradient(135deg,#fff7d6,#c9a04a);margin-top:40px}
.vc .num{font:700 42px 'DejaVu Sans Mono',monospace;letter-spacing:4px;margin-top:40px}
.vc .vt{position:absolute;right:36px;top:36px;padding:8px 18px;border:3px solid #08202e;border-radius:12px;font:900 24px Inter;letter-spacing:3px}
.medal{position:absolute;left:390px;top:690px;width:300px;height:420px}
.medal .rb{position:absolute;top:0;width:90px;height:190px;background:linear-gradient(#7fd3ff,#2c7fae)}
.medal .ds{position:absolute;left:20px;top:150px;width:260px;height:260px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#fff0c0,#e9b456 45%,#a8701f 100%);border:6px solid #f6d27a;box-shadow:0 0 60px rgba(240,180,80,.5);display:flex;align-items:center;justify-content:center;font:900 120px 'DejaVu Sans';color:#7a5016}
.bcoin{position:absolute;left:340px;top:740px;width:400px;height:400px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#fff0c0,#e9b456 45%,#a8701f 100%);border:8px solid #f6d27a;display:flex;align-items:center;justify-content:center;font:900 190px 'DejaVu Serif',serif;color:#7a5016;box-shadow:0 0 60px rgba(240,180,80,.4)}
.bx{position:absolute;left:290px;top:930px;width:500px;height:22px;border-radius:11px;background:#7fd3ff;box-shadow:0 0 30px rgba(127,211,255,.8);transform-origin:0 50%;rotate:-35deg}
.nb{position:absolute;left:0;top:1230px;width:1080px;text-align:center;font:800 36px Inter;letter-spacing:5px}
'''
ID = '<svg width="110" height="80" viewBox="0 0 110 80"><rect x="2" y="2" width="106" height="76" rx="10" fill="#cfe9f7" stroke="#1f5f86" stroke-width="4"/><circle cx="32" cy="34" r="13" fill="#1f5f86"/><rect x="14" y="52" width="36" height="14" rx="7" fill="#1f5f86"/><rect x="60" y="24" width="38" height="8" rx="4" fill="#1f5f86"/><rect x="60" y="40" width="30" height="8" rx="4" fill="#5fb8e6"/><rect x="60" y="56" width="34" height="8" rx="4" fill="#5fb8e6"/></svg>'
SELF = '<svg width="80" height="110" viewBox="0 0 80 110"><rect x="4" y="2" width="72" height="106" rx="14" fill="#1f2a33"/><circle cx="40" cy="46" r="18" fill="#f3c9a2"/><path d="M16 90 Q40 62 64 90 Z" fill="#7fd3ff"/><circle cx="40" cy="12" r="4" fill="#7fd3ff"/></svg>'
GO = '<svg width="100" height="100" viewBox="0 0 100 100"><path d="M50 8 Q72 28 70 62 L30 62 Q28 28 50 8 Z" fill="#1f5f86"/><circle cx="50" cy="36" r="9" fill="#bfefff"/><path d="M30 50 L16 70 L32 66 Z M70 50 L84 70 L68 66 Z" fill="#5fb8e6"/><path d="M40 66 Q50 96 60 66 Z" fill="#f3a73a"/></svg>'
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
BODY = hud('FRANCE · SANS AGENCE', 'PARRAINAGE') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('h1', "PAS BESOIN D'AGENCE", None, ''), ('it gold', 'pour ouvrir un compte.', None, 'font-size:72px')]) + '''
   <div class="shop"><div class="aw"></div><div class="sh"></div><div class="tag">FERMÉ<small>AGENCE</small></div></div>
   <div class="glow"></div></div>
  <div class="scene" data-s="1" data-in="right">''' + hd(230, [('h1 gl', 'AVEC REVOLUT,', '1.0', ''), ('it gold', "tout se passe dans l'appli.", '1.1', 'font-size:66px')]) + '''
   <div class="phone ph" style="top:620px;height:860px"><div class="notch"></div><div class="scr"><div class="ap">Revolut</div>
    <div class="row" data-g="1.1" data-fx="left"><i>▭</i>Compte</div><div class="row" data-g="1.2" data-fx="left"><i>⇄</i>Virements</div><div class="row" data-g="1.2" data-fx="left"><i>◔</i>Épargne</div></div></div></div>
  <div class="scene" data-s="2" data-in="up">''' + hd(230, [('h1 s', "UNE PIÈCE D'IDENTITÉ,", '2.0', ''), ('it gold', "un selfie, et c'est parti.", '2.1', 'font-size:68px')]) + '''
   <div class="stp" style="top:700px" data-g="2.0" data-fx="left"><div class="ic">''' + ID + '''</div><div class="tx">Pièce d'identité</div><div class="ok">✓</div></div>
   <div class="stp" style="top:920px" data-g="2.1" data-fx="right"><div class="ic">''' + SELF + '''</div><div class="tx">Selfie</div><div class="ok">✓</div></div>
   <div class="stp" style="top:1140px;border-color:#7fd3ff" data-g="2.2" data-fx="stamp"><div class="ic">''' + GO + '''</div><div class="tx gl">C'est parti</div><div class="ok">✓</div></div></div>
  <div class="scene" data-s="3" data-in="left"><div class="rays" style="top:700px"></div>''' + hd(230, [('h1 s', 'TA CARTE VIRTUELLE,', '3.0', ''), ('it gold', "tu la retrouves dans l'appli.", '3.1', 'font-size:64px')]) + '''
   <div class="vc" data-g="3.0" data-fx="up"><div class="vt">VIRTUELLE</div><div class="nm">MA CARTE</div><div class="chip"></div><div class="num">•••• •••• 1411</div></div>
   <div class="pill" style="top:1250px;border-color:rgba(127,211,255,.8)" data-g="3.2" data-fx="up"><div class="pin" style="background:#7fd3ff">▭</div><div><b>DANS L'APPLI</b><span>ta carte s'affiche sur l'écran</span></div></div></div>
  <div class="scene" data-s="4" data-in="pop">''' + hd(230, [('h1', 'TU PARRAINES ?', '4.0', ''), ('it gold', 'une récompense pour toi,', '4.1', 'font-size:68px')]) + '''
   <div class="medal" data-g="4.1" data-fx="up"><div class="rb" style="left:50px;transform:skewX(12deg)"></div><div class="rb" style="left:160px;transform:skewX(-12deg)"></div><div class="ds">★</div></div>
   <div class="abs" style="left:90px;top:1160px;width:900px;text-align:center" data-g="4.2" data-fx="stamp" data-slow="4.2"><div class="gold" style="font:900 84px 'DejaVu Serif',serif;line-height:1.2">selon l'offre</div><div class="gold" style="font:900 84px 'DejaVu Serif',serif;line-height:1.1">en cours</div></div></div>
  <div class="scene" data-s="5" data-in="right">''' + hd(230, [('h1', 'TON FILLEUL, LUI,', '5.0', ''), ('it gold', "n'a pas de prime en argent.", '5.1', 'font-size:64px')]) + '''
   <div class="bcoin" data-g="5.0" data-fx="pop">€</div><div class="bx" style="left:280px;top:1060px;rotate:-40deg" data-g="5.1" data-fx="strike"></div>
   <div class="nb gl" data-g="5.1" data-fx="up">ON RESTE HONNÊTES</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« REVOLUT »', '6.1', 'font-size:118px'), ('it gold', 'en privé,', '6.2', '')]) + '''
   <div class="pill" style="top:740px;border-color:rgba(127,211,255,.8)" data-g="6.3" data-fx="up"><div class="pin" style="background:#7fd3ff">✉</div><div><b>JE T'ENVOIE MON LIEN</b><span>directement en message privé</span></div></div>
   <div class="search" style="top:880px" data-g="6.3" data-fx="fade">''' + SEARCH + '''<span data-g="6.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1030px">Offre soumise aux conditions en vigueur<br>récompense parrain selon l'offre en cours<br>pas de prime en argent pour le filleul</div></div>
'''
