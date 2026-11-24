import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Revolut, 24/11/2026 16:00 - style v3 nuit & or, accent turquoise. Format F1 « STOP / erreur à éviter » :
# panneau STOP + « PARRAINAGE REVOLUT : il commence AVANT l'inscription » dès la 1re image -> l'erreur : télécharger l'appli et s'inscrire
# sans lien -> sans lien : pas d'invitation, récompense perdue -> avec le lien : checklist de l'invitation (ralenti « LE BON ORDRE »)
# -> FILLEUL (pas de prime en argent) / PARRAIN (récompense indiquée dans l'invitation) -> appel à l'action, petit STOP qui reboucle.
# Aucun montant. Source : revolut.com/fr-FR/legal/referrals-terms (consultée le 24/11/2026) : récompense indiquée dans l'invitation
# (courriel ou appli) ; l'invité ne doit pas avoir de compte Revolut Personnel, doit être éligible, avoir reçu un lien de parrainage,
# ouvrir son compte avec ce lien et suivre les étapes de l'invitation dans les délais indiqués.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'revolut15'
TITLE = 'Revolut STOP turquoise'
ROOT = ':root{--bg:#040909}'
LINES = [
 ("Stop : ton parrainage Revolut commence avant l'inscription.", [("STOP :", None), ("ton parrainage Revolut", None), ("commence avant", None), ("l'inscription.", None)]),
 ("L'erreur : télécharger l'appli et t'inscrire sans lien.", [("L'erreur :", None), ("télécharger l'appli", None), ("et t'inscrire", None), ("sans lien.", None)]),
 ("Sans lien de parrainage, pas d'invitation… et la récompense est perdue.", [("Sans lien de parrainage,", None), ("pas d'invitation…", None), ("et la récompense", None), ("est perdue.", None)]),
 ("Avec le lien : tu ouvres ton compte, puis tu suis les étapes de l'invitation, dans les délais.", [("Avec le lien :", None), ("tu ouvres ton compte,", None), ("puis tu suis les étapes", None), ("de l'invitation,", None), ("dans les délais.", None)]),
 ("Attention : le filleul ne touche pas de prime en argent. La récompense, c'est celle indiquée dans l'invitation.", [("Attention :", None), ("le filleul ne touche pas", None), ("de prime en argent.", None), ("La récompense,", None), ("c'est celle indiquée", None), ("dans l'invitation.", None)]),
 ("Envoie-moi REVOLUT en privé, je t'envoie mon lien avant ton inscription.", [("Envoie-moi", None), ("REVOLUT", None), ("en privé,", None), ("je t'envoie mon lien", None), ("avant ton inscription.", None)]),
]
SPLITS = [(0.0, 2.86), (3.15, 5.58), (5.89, 8.93), (9.42, 13.24), (13.70, 18.51), (18.90, 21.30)]
GSTART = [[0.0, 0.83, 1.7, 2.3], [3.15, 3.9, 4.8, 5.2], [5.9, 6.7, 7.93, 8.5], [9.42, 10.23, 11.34, 12.1, 12.8],
          [13.7, 14.55, 15.5, 16.57, 17.4, 18.0], [18.9, 19.2, 19.6, 20.1, 20.6]]
MINLEN = 1.9
GAP = 0.3
TAIL = 2.0

TQ = '#35e0cc'


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


def stop(left, top, size, g=None, fx='stamp'):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    fs = int(size * 0.27)
    return f'''<svg class="abs" style="left:{left}px;top:{top}px" width="{size}" height="{size}" viewBox="0 0 100 100"{a}>
 <polygon points="30,2 70,2 98,30 98,70 70,98 30,98 2,70 2,30" fill="#d8322c" stroke="#fff" stroke-width="4"/>
 <text x="50" y="61" text-anchor="middle" font-family="Inter" font-weight="900" font-size="{fs * 100 // size}" fill="#fff" letter-spacing="1">STOP</text></svg>'''


CSS = '''
.cond.tag{left:150px;width:780px;color:#f1ece2;background:rgba(4,9,9,.82);border:2px solid rgba(53,224,204,.45);border-radius:20px;padding:12px 18px;font-weight:600}
.tq{color:#35e0cc;text-shadow:0 0 18px rgba(53,224,204,.55)}
.rd{color:#ff5a4e;text-shadow:0 0 18px rgba(255,80,70,.5)}
.flow{position:absolute;left:170px;width:740px;display:flex;align-items:center;justify-content:space-between}
.st{width:310px;height:110px;border-radius:26px;display:flex;align-items:center;justify-content:center;gap:12px;padding:0 18px;font:900 29px Inter;letter-spacing:1px;white-space:nowrap}
.st i{font-style:normal;flex:none;width:58px;height:58px;border-radius:50%;display:flex;align-items:center;justify-content:center;font:900 32px Inter}
.s1{background:#0b2421;border:4px solid #35e0cc;color:#c8fff6}.s1 i{background:#35e0cc;color:#04201c}
.s2{background:#15110a;border:4px solid #6b5630;color:#e9dcc4}.s2 i{background:#3a2f1c;color:#e9dcc4}
.arw{font:900 64px Inter;color:#f3c766}
.ph{position:absolute;left:330px;width:420px;height:640px;background:#0c0f0f;border:10px solid #263130;border-radius:60px;box-shadow:0 0 0 2px #3f5552,0 30px 90px rgba(0,0,0,.7);overflow:hidden;text-align:center}
.ph .nt{width:130px;height:30px;background:#000;border-radius:0 0 18px 18px;margin:0 auto 40px}
.ph .t{font:800 34px Inter;color:#f3efe6}
.ph .f{margin:30px 34px 0;height:82px;border-radius:18px;border:3px dashed #5d6f6c;font:600 24px Inter;color:#8fa3a0;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1.3}
.ph .bt{margin:34px 34px 0;height:88px;border-radius:44px;background:#f3efe6;color:#111;font:800 32px Inter;display:flex;align-items:center;justify-content:center}
.ph .ln{margin:22px 60px 0;height:18px;border-radius:9px;background:#1e2626}
.tap{position:absolute;width:90px;height:90px;border-radius:50%;border:6px solid rgba(255,255,255,.85);background:rgba(255,255,255,.18)}
.xx{position:absolute;width:150px;height:150px;border-radius:50%;background:#d8322c;color:#fff;display:flex;align-items:center;justify-content:center;font:900 100px Inter;box-shadow:0 0 50px rgba(255,60,50,.5)}
.chip{position:absolute;left:250px;width:580px;height:96px;border-radius:24px;display:flex;align-items:center;justify-content:center;gap:16px;font:900 36px Inter;letter-spacing:2px;white-space:nowrap}
.bad{background:#3a1210;border:4px solid #ff5a4e;color:#ffd2cc}
.okc{background:#0b2a26;border:4px solid #35e0cc;color:#c8fff6}
.lost{position:absolute;left:170px;width:740px;display:flex;gap:40px;justify-content:center}
.lost .b{position:relative;width:340px;height:300px;border-radius:34px;background:#140e0a;border:4px solid #5a3a30;text-align:center;padding-top:40px}
.lost .b .ic{font:400 120px 'DejaVu Sans';line-height:1;color:#e9dcc4}
.lost .b .d{font:800 32px Inter;color:#f1e4d0;margin-top:22px;letter-spacing:1px;white-space:nowrap}
.lost .b .k{position:absolute;left:30px;top:150px;width:280px;height:14px;border-radius:7px;background:#ff5a4e;transform-origin:0 50%;transform:rotate(-14deg)}
.chk{position:absolute;left:170px;width:740px}
.chk .r{height:116px;border-radius:30px;background:#071312;border:4px solid #1f5a53;margin-bottom:22px;display:flex;align-items:center;gap:26px;padding:0 30px;font:800 38px Inter;color:#eaf7f4;white-space:nowrap}
.chk .r .bx{flex:none;width:68px;height:68px;border-radius:16px;border:5px solid #35e0cc;display:flex;align-items:center;justify-content:center;font:900 46px Inter;color:#35e0cc}
.who{position:absolute;width:360px;height:360px;border-radius:36px;text-align:center;padding:36px 20px 0}
.who .t{font:900 40px Inter;letter-spacing:3px;white-space:nowrap}
.who .ic{margin:22px auto;width:120px;height:120px;border-radius:50%;display:flex;align-items:center;justify-content:center;font:900 60px Inter}
.who .d{font:700 28px Inter;line-height:1.35}
.w1{left:140px;background:#150c0a;border:4px solid #6b2f28;color:#e9cfc8}.w1 .ic{background:#3a1210;color:#ff7a6e}
.w2{left:540px;background:linear-gradient(180deg,#0e2b27,#061412);border:5px solid #35e0cc;color:#d4fff8;box-shadow:0 0 50px rgba(53,224,204,.25)}.w2 .ic{background:#35e0cc;color:#04201c}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'

BODY = hud('FRANCE · ERREUR À ÉVITER', 'REVOLUT') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(230, [('h1', 'PARRAINAGE', None, 'font-size:74px'), ('h1 tq', 'REVOLUT :', None, 'font-size:92px'), ('it gold', 'il commence AVANT', None, 'font-size:68px'), ('it gold', "l'inscription", None, 'font-size:68px')]) + '''
   <div class="rays" style="top:560px"></div>
   ''' + stop(395, 650, 290) + '''
   <div class="flow" style="top:1020px"><div class="st s1" data-g="0.1" data-fx="left"><i>1</i>LE LIEN</div><div class="arw" data-g="0.2" data-fx="pop">➜</div><div class="st s2" data-g="0.2" data-fx="right"><i>2</i>INSCRIPTION</div></div>
   <div class="chip okc" style="top:1180px" data-g="0.3" data-fx="stamp">✓ DANS CET ORDRE</div></div>
  <div class="scene" data-s="1" data-in="right"><div class="floor"></div>''' + hd(220, [('h1 rd', "L'ERREUR :", '1.0', 'font-size:80px'), ('it gold', "télécharger l'appli", '1.1', 'font-size:68px'), ('it gold', "et t'inscrire sans lien.", '1.2', 'font-size:64px')]) + '''
   <div class="ph" style="top:540px" data-g="1.0" data-fx="up"><div class="nt"></div><div class="t">Créer un compte</div>
    <div class="f">lien de parrainage<br><b style="color:#ff7a6e">aucun</b></div><div class="ln"></div><div class="ln" style="margin-right:120px"></div>
    <div class="bt">S'inscrire</div></div>
   <div class="tap" style="left:560px;top:930px" data-g="1.2" data-fx="pop"></div>
   <div class="xx" style="left:660px;top:600px" data-g="1.3" data-fx="stamp">✗</div>
   <div class="chip bad" style="top:1240px" data-g="1.3" data-fx="stamp">✗ SANS LIEN</div></div>
  <div class="scene" data-s="2" data-in="left"><div class="floor"></div>''' + hd(220, [('it gold', 'Sans lien de parrainage,', '2.0', 'font-size:64px'), ('h1 rd', "PAS D'INVITATION…", '2.1', 'font-size:60px'), ('it gold', 'et la récompense', '2.2', 'font-size:64px'), ('it rd', 'est perdue.', '2.3', 'font-size:70px')]) + '''
   <div class="lost" style="top:720px"><div class="b" data-g="2.0" data-fx="left"><div class="ic">✉</div><div class="d">INVITATION</div><div class="k" data-g="2.1" data-fx="strike"></div></div><div class="b" data-g="2.2" data-fx="right"><div class="ic">🎁</div><div class="d">RÉCOMPENSE</div><div class="k" data-g="2.3" data-fx="strike"></div></div></div>
   <div class="chip bad" style="top:1100px" data-g="2.3" data-fx="stamp">✗ PERDUE</div>
   <div class="cond tag" style="top:1230px;font-size:28px" data-g="2.3" data-fx="fade">le lien de parrainage se reçoit avant d'ouvrir le compte</div></div>
  <div class="scene" data-s="3" data-in="up"><div class="floor"></div>''' + hd(245, [('h1 tq', 'AVEC LE LIEN :', '3.0', 'font-size:80px')]) + '''
   <div class="chk" style="top:430px"><div class="r" data-g="3.0" data-fx="left"><div class="bx" data-g="3.0" data-fx="tick">✓</div>Lien de parrainage reçu</div><div class="r" data-g="3.1" data-fx="left"><div class="bx" data-g="3.1" data-fx="tick">✓</div>Compte ouvert avec le lien</div><div class="r" data-g="3.2" data-fx="left"><div class="bx" data-g="3.3" data-fx="tick">✓</div>Étapes de l'invitation</div><div class="r" data-g="3.4" data-fx="left"><div class="bx" data-g="3.4" data-fx="tick">✓</div>Dans les délais</div></div>
   <div class="chip okc" style="top:1060px" data-g="3.4" data-fx="stamp" data-slow="3.4">✓ LE BON ORDRE</div>
   <div class="cond tag" style="top:1190px;font-size:28px" data-g="3.4" data-fx="fade">étapes et délais : ceux écrits dans ton invitation</div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="floor"></div>''' + hd(215, [('h1 rd', 'ATTENTION :', '4.0', 'font-size:80px'), ('it gold', 'le filleul ne touche pas', '4.1', 'font-size:62px'), ('it gold', 'de prime en argent.', '4.2', 'font-size:62px')]) + '''
   <div class="who w1" style="top:610px" data-g="4.1" data-fx="left"><div class="t">FILLEUL</div><div class="ic">✗ €</div><div class="d">pas de prime<br>en argent</div></div>
   <div class="who w2" style="top:610px" data-g="4.3" data-fx="stamp"><div class="t">PARRAIN</div><div class="ic">🎁</div><div class="d">récompense indiquée<br>dans l'invitation</div></div>
   <div class="hd" style="top:1020px"><div class="it tq" style="font-size:62px" data-g="4.3" data-fx="tw">La récompense :</div><div class="it gold" style="font-size:58px" data-g="4.4" data-fx="tw">celle de l'invitation.</div></div>
   <div class="cond tag" style="top:1230px;font-size:26px" data-g="4.5" data-fx="fade">le filleul ouvre un compte et suit les étapes de l'invitation</div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="floor"></div>''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« REVOLUT »', '5.1', 'font-size:92px'), ('it tq', 'en privé,', '5.2', '')]) + '''
   <div class="pill" style="top:650px;border-color:rgba(53,224,204,.85)" data-g="5.3" data-fx="up"><div class="pin" style="background:#35e0cc;color:#04201c">✉</div><div><b>JE T'ENVOIE MON LIEN</b><span>avant ton inscription</span></div></div>
   <div class="search" style="top:790px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:915px;font-size:23px;color:#b4ab9b">Offre soumise aux conditions en vigueur<br>Pas de prime en argent pour le filleul · nouveaux clients<br>Récompense indiquée dans l'invitation de parrainage<br>(étapes et délais indiqués dans l'invitation)</div>
   ''' + stop(450, 1100, 180, '5.4', 'pop') + '''</div>
'''
