import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo2d import *
from hacoo_items import icon
# Hacoo n°2 du 27/11/2026 (tâche du jour, vidéo 2) - style D2 « Duo dessiné », accent rouge bordeaux (brief veille du 27/11).
# Format F1 « la case oubliée » en dialogue, décor Black Friday : « Black Friday partout… et il oublie encore ça » :
# le pigeon fait ses cadeaux « tout est déjà en promo », le malin lui rappelle la case code promo avant de payer (peu importe le jour),
# ticket 71,00 € -> ligne -9,94 € -> gros total 61,06 € (le seul ralenti) -> fin « envoie cette vidéo au pote ».
# Aucune annonce d'opération promo sur l'appli ni de cumul de réductions (« peu importe le jour »).
# RÈGLE DU 26/11 : le nom de l'appli n'est JAMAIS écrit (écran, sous-titres) : seulement dit à l'oral.
# Prix d'exemple : bottines 43 € + écharpe 16 € + gants 12 € = 71,00 € ; -14 % = 9,94 € (71 x 0,14) ; total 61,06 € (71 x 0,86).
# Articles génériques, sans marque ni logo.
# Voix : le malin (M) = cosmo (xai), le pigeon (P) = Mathieu (inworld) ; speed 1.1, une synthèse par réplique, silences de bord coupés,
# silences internes plafonnés à 0,16 s, atempo 1.1, -19 dB moyen, 0,2 s au début et 0,45 s entre répliques.
NAME = 'hacoo64'
TITLE = 'Duo dessine black friday bordeaux'
TAIL = 1.9
LINES = [
 ("C'est le Black Friday partout, je fais tous mes cadeaux aujourd'hui !", [("C'est le <em>Black&nbsp;Friday</em>", None), ("partout,", None), ("je fais tous", None), ("mes <em>cadeaux</em>", None), ("aujourd'hui&nbsp;!", None)]),
 ("Et sur l'appli Hacou, t'as tapé le code promo ?", [("Et sur l'appli,", "Et sur l'appli Hacou,"), ("t'as tapé", None), ("le <em>code promo&nbsp;?</em>", None)]),
 ("Un code ? Tout est déjà en promo !", [("Un code&nbsp;?", None), ("Tout est déjà", None), ("en <em>promo&nbsp;!</em>", None)]),
 ("Peu importe le jour : avant de payer, t'as une case code promo.", [("Peu importe", None), ("le jour :", None), ("avant de payer,", None), ("t'as une case", None), ("<em>code promo.</em>", None)]),
 ("Code promo Hacou : H, Z, K, link. Moins quatorze pour cent.", [("<em>Code promo</em>", "Code promo Hacou :"), ("<i>hzklink</i>.", "H, Z, K, link."), ("Moins", None), ("<em>14&nbsp;%.</em>", "quatorze pour cent.")]),
 ("Mes bottines, mon écharpe et mes gants… soixante et onze euros.", [("Mes bottines,", None), ("mon écharpe", None), ("et mes gants…", None), ("<em>71&nbsp;€.</em>", "soixante et onze euros.")]),
 ("Ça fait neuf euros quatre-vingt-quatorze de moins.", [("Ça fait", None), ("<em>9,94&nbsp;€</em>", "neuf euros quatre-vingt-quatorze"), ("de moins.", None)]),
 ("Soixante et un euros et six centimes ? Je le tape tout de suite !", [("<em>61,06&nbsp;€&nbsp;?</em>", "Soixante et un euros et six centimes ?"), ("Je le tape", None), ("tout de <em>suite&nbsp;!</em>", None)]),
 ("Envoie cette vidéo au pote qui fait ses cadeaux aujourd'hui. Code promo Hacou, H, Z, K, link.", [("Envoie cette vidéo", None), ("au pote qui fait", None), ("ses cadeaux", None), ("aujourd'hui.", None), ("<em>Code promo</em>", "Code promo Hacou,"), ("<i>hzklink</i>.", "H, Z, K, link.")]),
]
SPLITS = [(0.2, 2.672), (3.122, 5.202), (5.652, 7.212), (7.662, 10.744), (11.194, 15.254), (15.704, 18.498), (18.948, 20.74), (21.19, 23.759), (24.209, 29.625)]
DUO_LINES = [
 {'who': 'P', 'M': 'idle', 'P': 'talk', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'think', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'idle', 'P': 'shrug', 'shot': 'P'},
 {'who': 'M', 'M': 'point', 'P': 'idle', 'shot': 'M'},
 {'who': 'M', 'M': 'cool', 'P': 'think', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'idle', 'P': 'think', 'shot': 'P', 'lbl': False},
 {'who': 'M', 'M': 'hip', 'P': 'idle', 'shot': 'M', 'lbl': False},
 {'who': 'P', 'M': 'cool', 'P': 'shock', 'shot': 'P'},
 {'who': 'M', 'M': 'point', 'P': 'idle', 'shot': 'wide', 'lbl': False},
]
BX = '#8e1b3a'  # rouge bordeaux
JS = duo2d_js(DUO_LINES, p_bun=False, cap=BX)

CSS = '''
#sub{left:90px;width:840px;font-size:68px}
.hook{left:90px;width:840px;font-size:60px}
#sub em{background:''' + BX + ''';color:#fff}
.hook em{color:''' + BX + '''}
.hook mark{background:#f6d6de}
.tag.bx{background:''' + BX + ''';color:#fff}
.tag.pk{background:#f6d6de;color:#5c0f24}
.tk{position:absolute;width:600px;padding:14px 34px 12px;background:#fff;border:6px solid #111;border-radius:22px;box-shadow:9px 11px 0 #111;font:700 32px 'Inter',sans-serif;color:#111;white-space:nowrap;transform:rotate(-2deg)}
.tk .h{font:900 26px Inter;letter-spacing:3px;text-align:center;color:#555;border-bottom:4px dashed #bbb;padding-bottom:10px;margin-bottom:10px}
.tk .r{display:flex;justify-content:space-between;line-height:1.4}
.tk .r.cd{color:''' + BX + ''';font-weight:900;font-size:38px;margin:8px 0}
.tk .r.tt{border-top:4px dashed #bbb;margin-top:8px;padding-top:6px;font:900 38px Inter}
.tk .x{text-align:center;font:700 18px Inter;letter-spacing:2px;color:#888;text-transform:uppercase;margin-top:6px}
.list{position:absolute;width:420px;padding:16px 28px;background:#fffbe8;border:5px solid #111;border-radius:16px;box-shadow:8px 9px 0 #111;font:700 34px 'Comic Relief','Comic Sans MS',cursive;color:#111;transform:rotate(3deg);white-space:nowrap}
.list .h{font:900 28px Inter;letter-spacing:2px;color:''' + BX + ''';margin-bottom:6px}
.list s{text-decoration-color:''' + BX + ''';text-decoration-thickness:4px}
.bf{position:absolute;padding:8px 22px;background:#111;color:#fff;font:900 40px Inter;letter-spacing:3px;border-radius:12px;transform:rotate(-6deg);white-space:nowrap}
.endc .nt{margin-top:12px;font:700 32px 'Comic Relief','Comic Sans MS',cursive;color:''' + BX + '''}
'''


def ticket(x, y, g=None, disc=False, gd=None):
    a = f' data-g="{g}" data-fx="pop"' if g else ''
    d = ''
    if disc:
        ad = f' data-g="{gd}" data-fx="right"' if gd else ''
        d = f'<div class="r cd"{ad}><span>code promo -14 %</span><span>-9,94 €</span></div>'
    return (f'<div class="tk" style="left:{x}px;top:{y}px"{a}><div class="h">MON PANIER CADEAUX</div>'
            '<div class="r"><span>bottines</span><span>43,00 €</span></div>'
            '<div class="r"><span>écharpe</span><span>16,00 €</span></div>'
            '<div class="r"><span>gants</span><span>12,00 €</span></div>' +
            ('<div class="r"><span>sous-total</span><span>71,00 €</span></div>' + d +
             '<div class="r tt" data-g="6.2" data-fx="fade"><span>total</span><span>61,06 €</span></div>' if disc else
             '<div class="r tt"><span>total</span><span>71,00 €</span></div>') + '<div class="x">prix d\'exemple</div></div>')


def prod(ic, name, price, g, x, y, w=240):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;padding:10px 0 12px" data-g="{g}" data-fx="pop">'
            f'<span class="ico">{icon(ic, 110)}</span><div class="t">{name}</div><div class="p" style="font-size:56px">{price}</div><div class="x">prix d\'exemple</div></div>')


BODY = duo2d_body('le malin', 'le pigeon') + '''
  <div class="scene" data-s="0"><div class="hook">Black Friday partout…<br>et il <em>oublie</em> encore <mark>ça</mark></div>
   <div class="list" style="left:310px;top:420px"><div class="h">LISTE DE CADEAUX</div>bottines ✓<br>écharpe ✓<br>gants ✓<br><s>code promo</s> ?</div></div>
''' + anc('M', '<div class="tag pk" style="left:-200px;top:-150px" data-g="1.2" data-fx="stamp">CODE PROMO ?</div>', '1') + '''
''' + anc('P', '<div class="bub" style="left:-120px;top:-230px" data-g="2.0" data-fx="stamp">?!</div><div class="bf" style="left:-200px;top:-330px" data-g="2.2" data-fx="pop">TOUT EST EN PROMO</div>', '2') + '''
  <div class="scene" data-s="3" data-in="pop">
   <div class="phone" style="left:270px;top:230px" data-g="3.2" data-fx="up"><div class="t">CODE PROMO</div>
    <div class="f"></div><div class="ok" data-g="3.3" data-fx="fade">avant de payer</div><div class="ok" data-g="3.4" data-fx="fade">peu importe le jour</div></div>
  </div>
  <div class="scene" data-s="4" data-in="pop">
   <div class="phone" style="left:270px;top:230px" data-g="4.0" data-fx="up"><div class="t">CODE PROMO</div>
    <div class="f"><span data-g="4.1" data-fx="type">hzklink</span></div><div class="ok" data-g="4.3" data-fx="fade">Appliquer ✓ -14 %</div></div>
  </div>
  <div class="scene" data-s="5" data-in="pop">''' + prod('Bottines', 'bottines', '43 €', '5.0', 110, 230) + prod('Écharpe', 'écharpe', '16 €', '5.1', 420, 210) + prod('Gants', 'gants', '12 €', '5.2', 700, 230, 220) + '''
   <div class="tag" style="left:395px;top:540px" data-g="5.3" data-fx="stamp">= 71,00 €</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + ticket(230, 220, disc=True, gd='6.1') + '''</div>
  <div class="scene" data-s="7" data-in="pop">
   <div class="tag bx" style="left:330px;top:220px" data-g="7.0" data-fx="stamp">-14 % = -9,94 €</div>
   <div class="card" style="left:240px;top:330px;width:600px;padding:18px 0" data-g="7.0" data-fx="stamp" data-slow="7.0"><div class="t">avec le code promo</div><div class="p" style="font-size:120px;color:''' + BX + '''">61,06 €</div><div class="x"><span style="text-transform:none">hzklink</span> · -14 % · prix d'exemple</div></div>
  </div>
  <div class="scene" data-s="8" data-in="pop" style="z-index:7">
   <div class="endc" style="top:215px;left:95px;width:820px" data-g="8.0" data-fx="up"><div class="k">CODE PROMO</div><div class="c">hzklink</div><div class="d">-14 % avec le code hzklink</div>
    <div class="b" data-g="8.2" data-fx="pop">liens des articles tendance en bio</div><div class="nt" data-g="8.1" data-fx="pop">envoie ça au pote qui fait ses cadeaux</div><div class="x">Prix d'exemple · -14 % avec le code promo hzklink · Offre soumise aux conditions en vigueur</div></div>
  </div>
'''
