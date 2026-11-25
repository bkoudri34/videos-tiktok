import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Revolut, 25/11/2026 21:00 - style v3 nuit & or, accent rose framboise. Format F9 « duel / comparatif » :
# deux colonnes PARRAIN vs FILLEUL avec « ? » dès la 1re image -> le parrain : récompense indiquée dans l'invitation (appli)
# -> le filleul : pas de prime en argent, compte Revolut Personnel ouvert avec le lien -> checklist des étapes de l'invitation dans les délais
# -> tampon « SANS LIEN = NE COMPTE PAS » (ralenti) -> appel à l'action.
# Aucun montant (revolut.com/fr-FR/legal/referrals-terms consultée le 25/11/2026 : récompense indiquée dans l'invitation,
# l'invité ouvre un compte Revolut Personnel à l'aide du lien de parrainage et suit les étapes dans les délais indiqués).
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'revolut16'
TITLE = 'Revolut duel framboise'
ROOT = ':root{--bg:#0a0408}'
LINES = [
 ("Parrainage Revolut : parrain ou filleul, qui gagne quoi ?", [("Parrainage Revolut :", None), ("parrain ou filleul,", None), ("qui gagne quoi ?", None)]),
 ("Le parrain : la récompense indiquée dans son invitation, dans l'appli.", [("Le parrain :", None), ("la récompense indiquée", None), ("dans son invitation,", None), ("dans l'appli.", None)]),
 ("Le filleul : pas de prime en argent. Il ouvre un compte Revolut Personnel avec le lien.", [("Le filleul :", None), ("pas de prime en argent.", None), ("Il ouvre un compte Revolut Personnel", None), ("avec le lien.", None)]),
 ("Ensuite, il suit les étapes de l'invitation, dans les délais.", [("Ensuite, il suit les étapes", None), ("de l'invitation,", None), ("dans les délais.", None)]),
 ("Sans le lien au départ, le parrainage ne compte pas.", [("Sans le lien au départ,", None), ("le parrainage ne compte pas.", None)]),
 ("Envoie-moi REVOLUT en privé, je t'envoie le lien.", [("Envoie-moi", None), ("REVOLUT", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 2.84), (3.31, 6.42), (6.94, 10.57), (11.02, 13.20), (13.64, 15.55), (16.01, 18.2)]
GSTART = [[0.0, 1.2, 2.2], [3.31, 4.04, 5.0, 6.1], [6.94, 7.6, 8.82, 10.2], [11.02, 12.1, 12.8], [13.64, 14.6], [16.01, 16.3, 16.6, 17.1]]
MINLEN = 1.9
GAP = 0.3
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px;left:90px;width:840px">' + ''.join(out) + '</div>'


CSS = '''
.fb{color:#ff7ab4;text-shadow:0 0 18px rgba(255,90,160,.5)}
.col{position:absolute;width:360px;height:440px;border-radius:36px;text-align:center;white-space:nowrap;padding-top:34px;box-shadow:0 30px 80px rgba(0,0,0,.65)}
.col .t{font:900 40px Inter;letter-spacing:3px}
.col .av{margin:26px auto 0;width:130px;height:130px;border-radius:50%;display:flex;align-items:center;justify-content:center;font:900 64px Inter}
.col .q{margin-top:30px;font:900 110px 'DejaVu Serif',serif;line-height:1}
.col .r{margin-top:26px;font:800 28px Inter;line-height:1.35;color:#f6e9f0}
.cp{left:110px;background:#1c0b14;border:5px solid #ff7ab4}.cp .av{background:#ff7ab4;color:#1c0b14}.cp .t{color:#ff9ac6}
.cf{left:610px;background:#17130a;border:5px solid #e0ac55}.cf .av{background:#e0ac55;color:#17130a}.cf .t{color:#f3c766}
.vs{position:absolute;left:470px;width:140px;height:140px;border-radius:50%;background:#0a0408;border:5px solid #f3c766;display:flex;align-items:center;justify-content:center;font:900 52px 'DejaVu Serif',serif;color:#f3c766;box-shadow:0 0 40px rgba(240,180,80,.45)}
.inv{position:absolute;left:170px;width:740px;border-radius:30px;background:#fbf2f6;color:#22101a;padding:28px 36px;white-space:nowrap;box-shadow:0 30px 80px rgba(0,0,0,.7),0 0 0 5px rgba(255,122,180,.6)}
.inv .h{font:900 32px Inter}.inv .h span{display:block;font:600 22px Inter;color:#7a5a6a;margin-top:4px}
.inv .rw{margin-top:22px;height:92px;border-radius:22px;background:#ffe3ef;border:3px dashed #ff7ab4;display:flex;align-items:center;justify-content:center;font:900 34px Inter;color:#b0216a}
.row{position:absolute;left:150px;width:780px;height:116px;border-radius:30px;display:flex;align-items:center;gap:24px;padding:0 30px;font:800 34px Inter;white-space:nowrap}
.row i{flex:none;width:70px;height:70px;border-radius:50%;font-style:normal;display:flex;align-items:center;justify-content:center;font:900 40px Inter}
.no{background:#220a12;border:4px solid #ff4d6d;color:#ffd9e1}.no i{background:#ff4d6d;color:#fff}
.ok{background:#0d1a12;border:4px solid #46d28a;color:#dcffe9}.ok i{background:#46d28a;color:#062012}
.wt{background:#1d1608;border:4px solid #e0ac55;color:#f6e7c6}.wt i{background:#e0ac55;color:#1d1608}
.stamp{position:absolute;left:170px;width:740px;height:220px;border-radius:26px;border:10px solid #ff4d6d;color:#ff5f7c;display:flex;flex-direction:column;align-items:center;justify-content:center;font:900 64px Inter;letter-spacing:2px;white-space:nowrap;transform:rotate(-4deg);background:rgba(40,6,14,.75)}
.stamp span{font:800 24px Inter;color:#ffc1cd;letter-spacing:1px;margin-top:8px}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:700 24px Inter;color:#c9a6b8;letter-spacing:2px}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'


def duel(top, rp='?', rf='?', gp=None, gf=None):
    def col(cls, t, ic, r, g):
        a = f' data-g="{g}" data-fx="pop"' if g else ''
        inner = f'<div class="q gold">?</div>' if r == '?' else f'<div class="r">{r}</div>'
        return f'<div class="col {cls}" style="top:{top}px"{a}><div class="t">{t}</div><div class="av">{ic}</div>{inner}</div>'
    return col('cp', 'PARRAIN', 'P', rp, gp) + col('cf', 'FILLEUL', 'F', rf, gf) + f'<div class="vs" style="top:{top + 150}px">VS</div>'


BODY = hud('FRANCE · DUEL', 'REVOLUT') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(215, [('h1 fb', 'PARRAINAGE REVOLUT :', None, 'font-size:60px'), ('it gold', 'parrain ou filleul,', None, 'font-size:76px'), ('it gold', 'qui gagne quoi ?', None, 'font-size:76px')]) + duel(620) + '''</div>
  <div class="scene" data-s="1" data-in="up">''' + hd(215, [('h1 fb', 'LE PARRAIN :', '1.0', 'font-size:72px'), ('it gold', 'la récompense indiquée', '1.1', 'font-size:60px'), ('it gold', 'dans son invitation,', '1.2', 'font-size:60px')]) + '''
   <div class="inv" style="top:560px" data-g="1.1" data-fx="up"><div class="h">Invitation à la promotion<span>dans l'appli · illustration</span></div><div class="rw">RÉCOMPENSE : VOIR L'INVITATION</div></div>
   ''' + duel(880, 'récompense<br>indiquée dans<br>l\'invitation', '?', '1.2') + '''
   <div class="ex" style="top:1350px" data-g="1.3" data-fx="fade">dans l'appli · période de la promotion</div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(215, [('h1 fb', 'LE FILLEUL :', '2.0', 'font-size:72px')]) + '''
   <div class="row no" style="top:340px" data-g="2.1" data-fx="left"><i>✕</i>Prime en argent : non</div>
   <div class="row ok" style="top:480px" data-g="2.2" data-fx="left"><i>✓</i>Compte Revolut Personnel</div>
   <div class="row ok" style="top:620px" data-g="2.3" data-fx="left"><i>✓</i>Ouvert avec le lien</div>
   ''' + duel(800, 'récompense<br>indiquée dans<br>l\'invitation', 'pas de prime<br>en argent,<br>compte via le lien', None, '2.1') + '''</div>
  <div class="scene" data-s="3" data-in="left">''' + hd(215, [('it gold', 'Ensuite, il suit les étapes', '3.0', 'font-size:64px'), ('it fb', "de l'invitation,", '3.1', 'font-size:64px'), ('h1', 'DANS LES DÉLAIS.', '3.2', 'font-size:56px')]) + '''
   <div class="row ok" style="top:560px" data-g="3.0" data-fx="left"><i>1</i>Lien de parrainage ouvert</div>
   <div class="row ok" style="top:700px" data-g="3.0" data-fx="left"><i>2</i>Compte Revolut Personnel</div>
   <div class="row wt" style="top:840px" data-g="3.1" data-fx="left"><i>3</i>Étapes de l'invitation</div>
   <div class="row wt" style="top:980px" data-g="3.2" data-fx="left"><i>⏱</i>Dans les délais indiqués</div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:560px"></div>''' + hd(215, [('it gold', 'Sans le lien au départ,', '4.0', 'font-size:70px'), ('it fb', 'le parrainage ne compte pas.', '4.1', 'font-size:62px')]) + '''
   <div class="row no" style="top:520px" data-g="4.0" data-fx="left"><i>✕</i>Inscription sans le lien</div>
   <div class="stamp" style="top:760px" data-g="4.1" data-fx="stamp" data-slow="4.1">NE COMPTE PAS<span>LE LIEN D'ABORD, L'INSCRIPTION ENSUITE</span></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('big gold', '« REVOLUT »', '5.1', 'font-size:110px'), ('it fb', 'en privé,', '5.2', ''), ('it gold', "je t'envoie le lien.", '5.3', 'font-size:64px')]) + '''
   <div class="search" style="top:720px" data-g="5.3" data-fx="fade">''' + SEARCH + '''<span data-g="5.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:860px;font-size:24px">Offre soumise aux conditions en vigueur<br>Filleul : pas de prime en argent · compte Revolut Personnel<br>ouvert avec le lien de parrainage, étapes de l'invitation<br>dans les délais · récompense du parrain indiquée dans l'invitation</div>
   <div class="row ok" style="top:1100px" data-g="5.3" data-fx="up"><i>✓</i>Le lien d'abord, l'inscription ensuite</div></div>
'''
