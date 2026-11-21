import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Vidéos QG, 21/11/2026, vidéo 2 : Revolut. Style V3 « nuit & or », accent vert émeraude. Format F3 « anti-arnaque / confiance » :
# « une prime pour toi ? pas vraiment » -> seul le parrain est récompensé -> les 5 étapes du filleul cochées sur un téléphone
# -> le montant minimum est dans l'appli du parrain -> appel à l'action. Aucun montant (Revolut ne le publie pas), jamais « illimité ».
# Sources consultées le 21/11/2026 : help.revolut.com/fr-FR/help/referrals/more-help-with-referrals/referrals-new/what-are-the-conditions-of-the-referral-campaign/
# Voix : Manon (Bright Belle), Cartesia sonic-3.5, speed 1.2, un seul appel, +7 dB.
NAME = 'qg_revolut2'
TITLE = 'QG Revolut prime pour toi'
ROOT = ':root{--bg:#06080a}'
LINES = [
 ("Parrainage Revolut : une prime pour toi ? Pas vraiment.", [("Parrainage Revolut :", None), ("une prime pour toi ?", None), ("Pas vraiment.", None)]),
 ("Chez Revolut, seul le parrain est récompensé. Pas toi.", [("Chez Revolut,", None), ("seul le parrain", None), ("est récompensé.", None), ("Pas toi.", None)]),
 ("Toi, tu ouvres ton compte avec son lien, et tu vérifies ton identité.", [("Toi, tu ouvres ton compte", None), ("avec son lien,", None), ("et tu vérifies ton identité.", None)]),
 ("Tu ajoutes de l'argent, et tu commandes une carte physique.", [("Tu ajoutes de l'argent,", None), ("et tu commandes", None), ("une carte physique.", None)]),
 ("Puis tu paies par carte avant la date limite.", [("Puis tu paies par carte", None), ("avant la date limite.", None)]),
 ("Le montant minimum ? Il est dans l'appli du parrain.", [("Le montant minimum ?", None), ("Il est dans l'appli", None), ("du parrain.", None)]),
 ("Envoie-moi Revolut en privé, je t'envoie mon lien.", [("Envoie-moi", None), ("REVOLUT", None), ("en privé,", None), ("je t'envoie mon lien.", None)]),
]
SPLITS = [(0.0, 3.05), (3.52, 6.89), (7.37, 11.07), (11.45, 14.10), (14.51, 16.68), (17.0, 19.69), (20.26, 22.75)]
GSTART = [[0.0, 1.1, 2.53], [3.52, 4.5, 5.25, 6.45], [7.37, 8.65, 9.55], [11.45, 12.55, 13.15], [14.51, 15.55], [17.0, 18.45, 19.2], [20.26, 20.65, 21.05, 21.75]]
MINLEN = 1.6
GAP = 0.3
TAIL = 2.6

def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'

CSS = '''
.em{color:#5fe3a8;text-shadow:0 0 18px rgba(80,220,160,.5)}
.inv{position:absolute;left:170px;top:760px;width:740px;padding:40px 46px 50px;border-radius:30px;background:#f5f1e8;color:#1a1814;transform:rotate(-3deg);box-shadow:0 30px 90px rgba(0,0,0,.65)}
.inv .k{font:800 30px Inter;letter-spacing:6px;color:#6b665e;text-align:center}
.inv .r{display:flex;justify-content:space-between;align-items:center;margin-top:26px;font:700 40px Inter;white-space:nowrap;border-bottom:3px dashed #cfc7b8;padding-bottom:16px}
.inv .r b{font:900 64px 'DejaVu Serif',serif;color:#0f6b4a}
.stampx{position:absolute;padding:14px 30px;border:7px solid #e0453a;color:#e0453a;font:900 54px Inter;letter-spacing:3px;transform:rotate(-10deg);border-radius:14px;background:rgba(245,241,232,.9);white-space:nowrap}
.col{position:absolute;top:760px;width:400px;height:520px;border-radius:30px;border:3px solid rgba(217,162,76,.7);background:rgba(30,24,15,.6);text-align:center;padding-top:40px}
.col .who{font:800 34px Inter;letter-spacing:4px;color:#e9e4da}
.col .ic{margin:30px auto 20px;width:200px;height:200px;border-radius:50%;display:flex;align-items:center;justify-content:center;font:900 120px Inter}
.col .v{font:800 40px Inter;white-space:nowrap}
.ph{position:absolute;left:300px;top:690px;width:480px;height:800px;background:#0d0c0b;border:10px solid #2c2925;border-radius:64px;box-shadow:0 0 0 2px #514a40,0 30px 90px rgba(0,0,0,.7);overflow:hidden;color:#fff}
.ph .notch{width:140px;height:30px;background:#000;border-radius:0 0 20px 20px;margin:0 auto 26px}
.ph .tt{font:800 26px Inter;letter-spacing:4px;color:#8f877a;text-align:center;margin-bottom:18px}
.st{display:flex;align-items:center;gap:18px;margin:0 26px 16px;padding:18px 18px;border-radius:22px;background:#1a1814;font:700 30px Inter;white-space:nowrap}
.st i{flex:none;width:52px;height:52px;border-radius:50%;border:4px solid #5c5548;display:flex;align-items:center;justify-content:center;font:900 30px Inter;font-style:normal;color:transparent}
.st i.ok{background:#1f9d6b;border-color:#5fe3a8;color:#fff}
.st small{display:block;font:500 21px Inter;color:#9a917f;margin-top:2px}
.lens{position:absolute;width:260px;height:260px;border-radius:50%;border:16px solid #d9a24c;background:rgba(95,227,168,.10);box-shadow:0 0 40px rgba(240,180,80,.35)}
.lens:after{content:'';position:absolute;left:190px;top:210px;width:34px;height:150px;border-radius:14px;background:#8a6428;transform:rotate(-45deg);transform-origin:50% 0}
.minb{margin:20px 26px;padding:26px 20px;border-radius:22px;border:3px dashed #5fe3a8;text-align:center;font:800 34px Inter;color:#5fe3a8;white-space:nowrap}
.minb small{display:block;font:500 22px Inter;color:#9a917f;margin-top:8px}
'''

def st(n, lab, sub, g):
    return f'<div class="st"><i class="ok" data-g="{g}" data-fx="stamp">✓</i><div>{lab}<small>{sub}</small></div></div>'

def st0(lab, sub):
    return f'<div class="st"><i></i><div>{lab}<small>{sub}</small></div></div>'

PHONE = '''<div class="ph"><div class="notch"></div><div class="tt">TES 5 ÉTAPES</div>''' + \
    st(1, "Lien d'invitation", "1er compte Revolut", '2.0') + st(2, 'Identité vérifiée', "dans l'appli", '2.2') + \
    st(3, 'Argent ajouté', 'carte, Apple Pay, virement', '3.0') + st(4, 'Carte physique', 'commandée à temps', '3.2') + \
    st(5, 'Paiements carte', 'avant la date limite', '4.1') + '</div>'

BODY = hud('FRANCE · REVOLUT', 'VRAI OU FAUX') + '''
  <div class="floor"></div>
  <div class="scene" data-s="0">''' + hd(215, [('h1', 'PARRAINAGE REVOLUT', None, 'font-size:70px'), ('big gold', 'une prime ?', None, 'font-size:122px'), ('it em', 'pour toi, le filleul ?', None, 'font-size:62px')]) + '''
   <div class="inv"><div class="k">INVITATION · FILLEUL</div><div class="r"><span>Compte ouvert</span><b>✓</b></div><div class="r"><span>Prime pour toi</span><b style="color:#9a917f">?</b></div></div>
   <div class="stampx" style="left:330px;top:1130px" data-g="0.1" data-fx="stamp">PAS VRAIMENT</div></div>
  <div class="scene" data-s="1" data-in="right">''' + hd(240, [('h1', 'SEUL LE PARRAIN', '1.0', 'font-size:72px'), ('it em', 'est récompensé', '1.2', 'font-size:70px')]) + '''
   <div class="col" style="left:90px" data-g="1.0" data-fx="left"><div class="who">LE PARRAIN</div><div class="ic gold" style="border:6px solid #e0ac55">✓</div><div class="v gold">récompensé</div></div>
   <div class="col" style="left:590px" data-g="1.3" data-fx="right"><div class="who">TOI</div><div class="ic" style="border:6px solid #e0453a;color:#e0453a">✗</div><div class="v" style="color:#ff8a80">pas de prime</div></div></div>
  <div class="scene" data-s="2-4" data-in="up">''' + PHONE + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + hd(240, [('h1', 'ÉTAPES 1 ET 2', '2.0', 'font-size:66px'), ('it em', 'son lien, puis ton identité', '2.1', 'font-size:58px')]) + '''</div>
  <div class="scene" data-s="3" data-in="right">''' + hd(240, [('h1', 'ÉTAPES 3 ET 4', '3.0', 'font-size:66px'), ('it em', "de l'argent, puis la carte", '3.1', 'font-size:58px')]) + '''</div>
  <div class="scene" data-s="4" data-in="right">''' + hd(240, [('h1', 'ÉTAPE 5', '4.0', 'font-size:66px'), ('it em', 'avant la date limite', '4.1', 'font-size:58px')]) + '''</div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(240, [('h1', 'LE MONTANT MINIMUM', '5.0', 'font-size:66px'), ('it em', "dans l'appli du parrain", '5.1', 'font-size:60px')]) + '''
   <div class="ph"><div class="notch"></div><div class="tt">INVITER DES AMIS</div>
    <div class="minb" data-g="5.1" data-fx="stamp" data-slow="5.1" style="box-shadow:0 0 40px rgba(95,227,168,.45)">paiement minimum :<br>voir l'appli<small>conditions de la campagne</small></div>
    <div class="st"><i class="ok">✓</i><div>Ton lien d'invitation<small>à partager</small></div></div>
    <div class="st"><i></i><div>5 filleuls max<small>par campagne</small></div></div></div>
   </div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« REVOLUT »', '6.1', 'font-size:110px'), ('it gold', 'en privé', '6.2', '')]) + '''
   <div class="pill" style="top:760px;left:150px;width:770px;border-color:rgba(95,227,168,.85)" data-g="6.3" data-fx="up"><div class="pin" style="background:#5fe3a8;color:#06231a">✉</div><div><b>JE T'ENVOIE MON LIEN</b><span>ton compte en 5 étapes</span></div></div>
   <div class="cond" style="top:920px;left:150px;width:770px;font-size:26px">Offre soumise aux conditions en vigueur · Parrainage Revolut : seul le parrain est récompensé (sauf autre récompense annoncée par Revolut). Le filleul ouvre son 1er compte avec le lien d'invitation, vérifie son identité, ajoute de l'argent, commande une carte physique et fait les paiements carte demandés avant la date limite (montant minimum dans l'appli du parrain) · 5 parrainages max par campagne · Lien de parrainage : je touche une prime.</div></div>
'''
