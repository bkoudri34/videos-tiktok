import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# BoursoBank, 25/11/2026 16:00 - style v3 nuit & or, accent rouge rubis. Format F4 « argent laissé sur la table » :
# table de jeu feutrée avec 4 billets retournés dès la 1re image -> chaque billet se retourne (60 € ouverture, 80 € versement >= 300 €,
# 80 € carte 3 mois, 80 € EasyMove) avec le compteur « sur la table » qui monte -> total 300 € (ralenti) « seulement avec un lien
# de parrainage » -> appel à l'action.
# Offre parrainage filleul « prime maximale de 300 € » (boursobank.com/bon-plan/parrainage-boursobank, consultée le 25/11/2026) :
# 60 € ouverture + 80 € 1er versement >= 300 € (pendant l'ouverture ou dans les 30 jours) + 80 € carte (20 + 30 + 30 sur 3 mois)
# + 80 € 1re mobilité EasyMove (formulaire signé dans le mois suivant l'ouverture).
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'bourso16'
TITLE = 'BoursoBank table rubis'
ROOT = ':root{--bg:#0a0406}'
LINES = [
 ("Parrainage Bourso Bank : trois cents euros que tu laisses sur la table.", [("Parrainage BoursoBank :", None), ("300 €", None), ("que tu laisses sur la table.", None)]),
 ("Soixante euros, rien que pour ouvrir ton compte.", [("60 €,", None), ("rien que pour ouvrir ton compte.", None)]),
 ("Quatre-vingts euros si ton premier versement fait au moins trois cents euros.", [("80 €", None), ("si ton 1er versement", None), ("fait au moins 300 €.", None)]),
 ("Quatre-vingts euros en payant par carte, chaque mois pendant trois mois.", [("80 €", None), ("en payant par carte,", None), ("chaque mois pendant 3 mois.", None)]),
 ("Et quatre-vingts euros si tu changes de banque avec Easy Move.", [("Et 80 €", None), ("si tu changes de banque", None), ("avec EasyMove.", None)]),
 ("Total : trois cents euros, mais seulement avec un lien de parrainage.", [("Total :", None), ("300 €,", None), ("mais seulement avec", None), ("un lien de parrainage.", None)]),
 ("Envoie-moi BOURSO en privé, je t'envoie le lien.", [("Envoie-moi", None), ("BOURSO", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 2.73), (3.11, 5.06), (5.46, 7.95), (8.64, 11.29), (12.0, 14.19), (14.82, 17.63), (18.13, 19.74)]
GSTART = [[0.0, 1.2, 1.9], [3.11, 3.9], [5.46, 6.0, 6.9], [8.64, 9.3, 10.3], [12.0, 12.8, 13.6], [14.82, 15.4, 16.2, 16.9], [18.13, 18.4, 18.8, 19.2]]
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
.rb{color:#ff6b7d;text-shadow:0 0 18px rgba(255,70,100,.5)}
.felt{position:absolute;left:70px;width:860px;height:560px;border-radius:60px;background:radial-gradient(80% 70% at 50% 45%,#5a1422,#2c0810 75%);border:10px solid #3a2a16;box-shadow:0 0 0 4px #c99a4a,0 40px 90px rgba(0,0,0,.75),inset 0 0 80px rgba(0,0,0,.6)}
.felt:before{content:'';position:absolute;inset:24px;border-radius:40px;border:3px dashed rgba(255,215,150,.25)}
.bill{position:absolute;width:300px;height:160px;border-radius:16px;background:linear-gradient(135deg,#f6e7c1,#e2c27c);border:5px solid #b8863a;box-shadow:0 14px 30px rgba(0,0,0,.6);color:#3a2408;text-align:center;white-space:nowrap}
.bill .v{margin-top:18px;font:900 74px 'DejaVu Serif',serif;line-height:1}
.bill .l{margin-top:10px;font:800 22px Inter;letter-spacing:2px;color:#6b4a18}
.bill.dn{background:repeating-linear-gradient(45deg,#3b0d18 0 14px,#4c1220 14px 28px);border-color:#c99a4a;color:#f3c766}
.bill.dn .v{margin-top:30px;font-size:90px}
.meter{position:absolute;left:190px;width:700px;height:110px;border-radius:55px;background:#16070b;border:4px solid #ff6b7d;display:flex;align-items:center;justify-content:space-between;padding:0 40px;font:800 32px Inter;color:#f6e6e8;white-space:nowrap}
.meter b{font:900 58px 'DejaVu Serif',serif;color:#f3c766}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:700 24px Inter;color:#c9a3a9;letter-spacing:2px}
.tot{position:absolute;left:0;width:1080px;text-align:center}
.tot .v{font:900 210px 'DejaVu Serif',serif;line-height:1}
.lnk{position:absolute;left:200px;width:680px;height:120px;border-radius:60px;background:#fff;color:#1a0a0e;display:flex;align-items:center;justify-content:center;gap:22px;font:900 40px Inter;white-space:nowrap;box-shadow:0 0 0 6px #ff6b7d,0 20px 60px rgba(0,0,0,.6)}
.lnk i{font-style:normal;width:70px;height:70px;border-radius:50%;background:#ff6b7d;color:#fff;display:flex;align-items:center;justify-content:center;font:900 36px Inter}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
BILLS = [('60 €', 'OUVERTURE'), ('80 €', '1er VERSEMENT'), ('80 €', 'CARTE · 3 MOIS'), ('80 €', 'EASYMOVE')]
POS = [(130, 70, -6), (480, 50, 5), (140, 290, 4), (490, 300, -5)]


def table(top, n_up, gi=None, ga=None):
    """felt table; bills 0..n_up-1 face up; bill n_up-1 animated at group gi (fx ga)"""
    out = f'<div class="felt" style="top:{top}px">'
    for k, ((v, l), (x, y, r)) in enumerate(zip(BILLS, POS)):
        if k < n_up:
            a = f' data-g="{gi}" data-fx="{ga}"' if (gi and k == n_up - 1) else ''
            out += f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({r}deg)"><div class="bill"{a}><div class="v">{v}</div><div class="l">{l}</div></div></div>'
        else:
            out += f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({r}deg)"><div class="bill dn"><div class="v">?</div></div></div>'
    return out + '</div>'


def meter(top, val, g):
    return f'<div class="meter" style="top:{top}px" data-g="{g}" data-fx="tick"><span>Sur la table</span><b>{val} €</b></div>'


BODY = hud('FRANCE · TABLE DES PRIMES', 'BOURSOBANK') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(215, [('h1 rb', 'PARRAINAGE BOURSOBANK :', None, 'font-size:54px'), ('big gold', '300 €', None, 'font-size:150px'), ('it gold', 'que tu laisses sur la table.', None, 'font-size:62px')]) + table(700, 0) + '''</div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('big gold', '60 €,', '1.0', 'font-size:130px'), ('it rb', 'rien que pour ouvrir ton compte.', '1.1', 'font-size:56px')]) + table(640, 1, '1.0', 'pop') + meter(1250, 60, '1.1') + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('big gold', '80 €', '2.0', 'font-size:130px'), ('it rb', 'si ton 1er versement', '2.1', 'font-size:58px'), ('it gold', 'fait au moins 300 €.', '2.2', 'font-size:58px')]) + table(720, 2, '2.0', 'pop') + meter(1330, 140, '2.2') + '''</div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('big gold', '80 €', '3.0', 'font-size:130px'), ('it rb', 'en payant par carte,', '3.1', 'font-size:58px'), ('it gold', 'chaque mois pendant 3 mois.', '3.2', 'font-size:56px')]) + table(720, 3, '3.0', 'pop') + meter(1330, 220, '3.2') + '''</div>
  <div class="scene" data-s="4" data-in="up">''' + hd(230, [('big gold', 'Et 80 €', '4.0', 'font-size:130px'), ('it rb', 'si tu changes de banque', '4.1', 'font-size:58px'), ('it gold', 'avec EasyMove.', '4.2', 'font-size:58px')]) + table(720, 4, '4.0', 'pop') + meter(1330, 300, '4.2') + '''</div>
  <div class="scene" data-s="5" data-in="pop"><div class="rays" style="top:300px"></div>''' + hd(215, [('h1 rb', 'TOTAL :', '5.0', 'font-size:80px')]) + '''
   <div class="tot" style="top:330px" data-g="5.1" data-fx="stamp" data-slow="5.1" data-count="300"><div class="v gold">0 €</div></div>
   <div class="ex" style="top:570px;font-size:26px" data-g="5.1" data-fx="fade">60 + 80 + 80 + 80 € · conditions remplies</div>
   ''' + hd(650, [('it gold', 'mais seulement avec', '5.2', 'font-size:62px'), ('it rb', 'un lien de parrainage.', '5.3', 'font-size:62px')]) + '''
   <div class="lnk" style="top:900px" data-g="5.3" data-fx="pop"><i>✓</i>LIEN DE PARRAINAGE</div>
   <div class="ex" style="top:1060px" data-g="5.3" data-fx="fade">offre parrainage filleul · via l'invitation reçue</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« BOURSO »', '6.1', 'font-size:110px'), ('it rb', 'en privé,', '6.2', ''), ('it gold', "je t'envoie le lien.", '6.3', 'font-size:64px')]) + '''
   <div class="search" style="top:720px" data-g="6.3" data-fx="fade">''' + SEARCH + '''<span data-g="6.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:860px;font-size:24px">Offre soumise aux conditions en vigueur<br>Jusqu'à 300 € pour le filleul : 1re ouverture d'un compte individuel,<br>1er versement d'au moins 300 € sous 30 jours, 1 opération carte<br>par mois pendant 3 mois, 1re mobilité EasyMove sous 1 mois</div>
   <div class="meter" style="top:1100px" data-g="6.3" data-fx="up"><span>Sur la table</span><b>300 €</b></div></div>
'''
