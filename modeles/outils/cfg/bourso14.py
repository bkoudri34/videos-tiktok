import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# BoursoBank, 21/11/2026 21:00 - style v3 nuit & or, accent cuivre. Format F3 « anti-arnaque / confiance » (vrai ou faux) :
# boutons VRAI / FAUX dès la 1re image -> « vrai, si tu coches les 4 cases » (checklist vide) -> case 1 ouverture + 300 € versés = 100 €
# -> case 2 carte 3 mois = 80 € -> case 3 EasyMove dans les 30 jours = 80 € -> case 4 garder son compte (primes reprises si clôture < 24 mois)
# -> checklist cochée, 260 € (ralenti) -> appel à l'action.
# Offre parrainage filleul jusqu'à 260 € (boursobank.com/bon-plan/parrainage-boursobank, consultée le 21/11/2026) :
# 20 € ouverture + 80 € 1er versement >= 300 € + 80 € carte (20 + 30 + 30 sur 3 mois) + 80 € mobilité EasyMove dans les 30 jours ;
# primes reprises en cas de clôture dans les 24 mois.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'bourso14'
TITLE = 'BoursoBank vrai faux cuivre'
ROOT = ':root{--bg:#0a0705}'
LINES = [
 ("Parrainage Bourso Bank : deux cent soixante euros, vrai ou faux ?", [("Parrainage BoursoBank :", None), ("260 €,", None), ("vrai ou faux ?", None)]),
 ("Vrai, mais seulement si tu coches les quatre cases.", [("Vrai,", None), ("mais seulement si", None), ("tu coches les 4 cases.", None)]),
 ("Case un : tu ouvres ton compte avec au moins trois cents euros. Cent euros.", [("Case 1 :", None), ("tu ouvres ton compte", None), ("avec au moins 300 €.", None), ("100 €.", None)]),
 ("Case deux : un paiement par carte chaque mois, pendant trois mois. Quatre-vingts euros.", [("Case 2 :", None), ("un paiement par carte", None), ("chaque mois, pendant 3 mois.", None), ("80 €.", None)]),
 ("Case trois : la mobilité bancaire Easy Move, dans les trente jours. Quatre-vingts euros.", [("Case 3 :", None), ("la mobilité bancaire EasyMove,", None), ("dans les 30 jours.", None), ("80 €.", None)]),
 ("Case quatre : tu gardes ton compte, sinon la prime peut être reprise.", [("Case 4 :", None), ("tu gardes ton compte,", None), ("sinon la prime", None), ("peut être reprise.", None)]),
 ("Les quatre cases cochées : deux cent soixante euros.", [("Les 4 cases cochées :", None), ("260 €.", None)]),
 ("Envoie-moi PARRAINAGE en privé, je t'envoie le lien.", [("Envoie-moi", None), ("PARRAINAGE", None), ("en privé,", None), ("je t'envoie le lien.", None)]),
]
SPLITS = [(0.0, 2.67), (3.0, 4.88), (5.38, 8.45), (9.03, 12.29), (13.18, 16.88), (17.65, 20.31), (20.87, 22.89), (23.46, 25.31)]
GSTART = [[0.0, 1.2, 2.2], [3.0, 3.5, 4.0], [5.38, 6.0, 6.7, 8.1], [9.03, 9.8, 10.5, 11.7], [13.18, 13.9, 15.4, 16.3], [17.65, 18.3, 19.1, 19.6], [20.87, 22.0], [23.46, 23.8, 24.2, 24.7]]
MINLEN = 1.9
GAP = 0.25
TAIL = 1.8


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.cu{color:#ffa45c;text-shadow:0 0 18px rgba(255,140,60,.5)}
.vf{position:absolute;top:880px;width:380px;height:200px;border-radius:40px;display:flex;align-items:center;justify-content:center;font:900 84px Inter;letter-spacing:4px;box-shadow:0 30px 80px rgba(0,0,0,.6)}
.vf.v{left:110px;background:#173022;border:6px solid #4fd08a;color:#bff5d6}
.vf.f{left:590px;background:#341612;border:6px solid #ff6a4a;color:#ffd0c4}
.qm{position:absolute;left:465px;top:1110px;width:150px;height:150px;border-radius:50%;background:#ff8a3c;color:#1a0c04;font:900 110px 'DejaVu Serif',serif;display:flex;align-items:center;justify-content:center;box-shadow:0 0 50px rgba(255,140,60,.5)}
.chk{position:absolute;left:170px;width:740px;border-radius:36px;background:#f7f2ec;color:#2a1608;padding:26px 40px;box-shadow:0 30px 80px rgba(0,0,0,.6),0 0 0 5px rgba(255,140,60,.55)}
.chk .h{font:800 28px Inter;color:#8a6a52;letter-spacing:3px;margin-bottom:6px}
.chk .r{display:flex;align-items:center;gap:26px;padding:14px 0;border-bottom:2px dashed #d9c6b4;font:800 36px Inter;white-space:nowrap}
.chk .r:last-child{border-bottom:0}
.chk .r .bx{flex:none;width:62px;height:62px;border-radius:14px;border:5px solid #b98a62;position:relative;background:#fff}
.chk .r .bx i{position:absolute;inset:-5px;border-radius:14px;background:#e0702a;display:flex;align-items:center;justify-content:center}
.chk .r b{margin-left:auto;font:900 44px 'DejaVu Serif',serif;color:#b4521a}
.case{position:absolute;left:150px;width:780px;height:330px;border-radius:40px;background:linear-gradient(160deg,#2a170c,#120a05);border:5px solid #ff9a4a;box-shadow:0 30px 80px rgba(0,0,0,.7),0 0 50px rgba(255,140,60,.2)}
.case .n{position:absolute;left:40px;top:30px;font:900 34px Inter;color:#ffa45c;letter-spacing:4px}
.case .bx{position:absolute;right:44px;top:34px;width:96px;height:96px;border-radius:22px;border:6px solid #ffa45c;background:#1a0f08}
.case .bx i{position:absolute;inset:-6px;border-radius:22px;background:#e0702a;display:flex;align-items:center;justify-content:center}
.case .t{position:absolute;left:40px;right:40px;top:150px;font:800 46px Inter;color:#fff1e4;line-height:1.25}
.case .t small{display:block;font:600 30px Inter;color:#d8b89c;margin-top:10px}
.tile{position:absolute;left:250px;width:580px;height:160px;border-radius:40px;background:#f7f2ec;color:#3a1a08;display:flex;align-items:center;justify-content:center;gap:24px;font:900 100px 'DejaVu Serif',serif;box-shadow:0 20px 60px rgba(0,0,0,.6),0 0 0 5px rgba(255,140,60,.6);white-space:nowrap}
.tile small{font:800 30px Inter;color:#8a6a52;letter-spacing:2px}
.mos{position:absolute;left:150px;width:780px;display:flex;justify-content:space-between}
.mos .m{width:230px;height:120px;border-radius:26px;background:#1a0f08;border:4px solid #8a5a36;display:flex;align-items:center;justify-content:center;gap:14px;font:800 34px Inter;color:#ffe2c8;white-space:nowrap}
.warn{position:absolute;left:190px;width:700px;height:120px;border-radius:30px;background:#3a1410;border:4px solid #ff6a4a;display:flex;align-items:center;justify-content:center;gap:20px;font:800 36px Inter;color:#ffd0c4;white-space:nowrap}
.tot{position:absolute;left:0;width:1080px;text-align:center}
.tot .v{font:900 190px 'DejaVu Serif',serif;line-height:1}
'''
CK = '<svg width="{s}" height="{s}" viewBox="0 0 90 90"><path d="M18 46 L38 66 L74 24" fill="none" stroke="#fff" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
ROWS = [('Ouverture + 300 €', '100 €'), ('Carte · 3 mois', '80 €'), ('EasyMove · 30 jours', '80 €'), ('Garder son compte', '✓')]


def checklist(top, g_rows, g_ticks):
    out = f'<div class="chk" style="top:{top}px"><div class="h">MA CHECKLIST · PARRAINAGE</div>'
    for k, (lbl, v) in enumerate(ROWS):
        tick = f'<i data-g="{g_ticks[k]}" data-fx="tick">{CK.format(s=44)}</i>' if g_ticks else ''
        ga = f' data-g="{g_rows}" data-fx="left"' if g_rows else ''
        out += f'<div class="r"{ga}><div class="bx">{tick}</div>{lbl}<b>{v}</b></div>'
    return out + '</div>'


def case(n, top, title, sub, gi, gtick):
    return (f'<div class="case" style="top:{top}px" data-g="{gi}.0" data-fx="pop"><div class="n">CASE {n} / 4</div>'
            f'<div class="bx"><i data-g="{gtick}" data-fx="tick">{CK.format(s=70)}</i></div>'
            f'<div class="t" data-g="{gi}.1" data-fx="fade">{title}<small>{sub}</small></div></div>')


BODY = hud('FRANCE · VRAI OU FAUX', 'BOURSOBANK') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(205, [('h1 cu', 'PARRAINAGE BOURSOBANK :', None, 'font-size:56px'), ('big gold', '260 €,', None, 'font-size:150px'), ('it gold', 'vrai ou faux ?', None, 'font-size:84px')]) + '''
   <div class="vf v" style="transform:rotate(-4deg)">VRAI</div><div class="vf f" style="transform:rotate(4deg)">FAUX</div>
   <div class="qm">?</div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('big gold', 'Vrai,', '1.0', 'font-size:140px'), ('it gold', 'mais seulement si', '1.1', 'font-size:72px'), ('h1 cu', 'TU COCHES LES 4 CASES.', '1.2', 'font-size:58px')]) + '''
   ''' + checklist(720, '1.2', None) + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 cu', 'CASE 1 :', '2.0', 'font-size:72px'), ('it gold', 'tu ouvres ton compte', '2.1', 'font-size:70px'), ('it gold', 'avec au moins 300 €.', '2.2', 'font-size:70px')]) + '''
   ''' + case(1, 700, 'Ouverture + 300 € versés', '20 € ouverture + 80 € versement', 2, '2.3') + '''
   <div class="tile" style="top:1120px" data-g="2.3" data-fx="stamp">100 €<small>CASE 1</small></div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(230, [('h1 cu', 'CASE 2 :', '3.0', 'font-size:72px'), ('it gold', 'un paiement par carte', '3.1', 'font-size:68px'), ('it gold', 'chaque mois, pendant 3 mois.', '3.2', 'font-size:60px')]) + '''
   ''' + case(2, 680, 'Au moins 1 opération carte par mois', '20 € + 30 € + 30 € sur 3 mois', 3, '3.3') + '''
   <div class="mos" style="top:1050px"><div class="m" data-g="3.2" data-fx="pop">MOIS 1</div><div class="m" data-g="3.2" data-fx="pop">MOIS 2</div><div class="m" data-g="3.2" data-fx="pop">MOIS 3</div></div>
   <div class="tile" style="top:1210px" data-g="3.3" data-fx="stamp">80 €<small>CASE 2</small></div></div>
  <div class="scene" data-s="4" data-in="right">''' + hd(230, [('h1 cu', 'CASE 3 :', '4.0', 'font-size:72px'), ('it gold', 'la mobilité bancaire EasyMove,', '4.1', 'font-size:58px'), ('it gold', 'dans les 30 jours.', '4.2', 'font-size:68px')]) + '''
   ''' + case(3, 700, 'Mobilité bancaire EasyMove', "dans les 30 jours après l'ouverture", 4, '4.3') + '''
   <div class="tile" style="top:1120px" data-g="4.3" data-fx="stamp">80 €<small>CASE 3</small></div></div>
  <div class="scene" data-s="5" data-in="left">''' + hd(230, [('h1 cu', 'CASE 4 :', '5.0', 'font-size:72px'), ('it gold', 'tu gardes ton compte,', '5.1', 'font-size:70px'), ('it gold', 'sinon la prime', '5.2', 'font-size:70px'), ('h1 cu', 'PEUT ÊTRE REPRISE.', '5.3', 'font-size:58px')]) + '''
   ''' + case(4, 760, 'Garder son compte ouvert', 'et sa domiciliation pendant 24 mois', 5, '5.1') + '''
   <div class="warn" style="top:1160px" data-g="5.3" data-fx="stamp">⚠ clôture &lt; 24 mois = reprise</div></div>
  <div class="scene" data-s="6" data-in="pop"><div class="rays" style="top:930px"></div>''' + hd(215, [('h1 cu', 'LES 4 CASES COCHÉES :', '6.0', 'font-size:62px')]) + '''
   ''' + checklist(360, None, ['6.0', '6.0', '6.0', '6.0']) + '''
   <div class="tot" style="top:1010px" data-g="6.1" data-fx="stamp" data-slow="6.1" data-count="260"><div class="v gold">0 €</div></div>
   <div class="cond" style="top:1230px;font-size:28px;color:#d8b89c" data-g="6.1" data-fx="fade">pour le filleul · 1re ouverture de compte individuel</div></div>
  <div class="scene" data-s="7" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '7.0', ''), ('big gold', '« PARRAINAGE »', '7.1', 'font-size:100px'), ('it gold', 'en privé,', '7.2', '')]) + '''
   <div class="pill" style="top:760px;border-color:rgba(255,140,60,.85)" data-g="7.3" data-fx="up"><div class="pin" style="background:#e0702a;color:#fff">✉</div><div><b>JE T'ENVOIE LE LIEN</b><span>directement en message privé</span></div></div>
   <div class="search" style="top:900px" data-g="7.3" data-fx="fade">''' + SEARCH + '''<span data-g="7.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1040px;font-size:23px">Offre soumise aux conditions en vigueur · 1re ouverture de compte individuel<br>jusqu'à 260 € pour le filleul : 20 € ouverture + 80 € 1er versement (≥ 300 €)<br>+ 80 € carte sur 3 mois + 80 € EasyMove (30 j) · primes reprises si clôture &lt; 24 mois</div></div>
'''
