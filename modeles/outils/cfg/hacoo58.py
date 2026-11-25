import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from duo2d import *
from hacoo_items import icon
# Hacoo n°4 du 25/11/2026 (tâche « 2 vidéos Hacoo en plus », vidéo 4) - style D2 « Duo dessiné », accent bleu roi.
# Format F1 « STOP » dans un dialogue F10 : « STOP, il valide son panier Hacoo sans le code » : le pigeon s'apprête à payer
# son panier cocooning plein pot, la maligne l'arrête et lui montre la case code promo Hacoo avant de payer.
# Prix d'exemple : plaid 31 € + chaussons 19 € + bouillotte 13 € = 63,00 € ; -14 % = 8,82 € (63 x 0,14) ; total 54,18 € (63 x 0,86).
# Articles génériques, sans marque ni logo.
# Voix : la maligne (M) = Soleil (azure, fr-FR-Soleil:MAI-Voice-2.1, ne dit que le code, pas de montant), atempo 1.12 ;
# le pigeon (P) = Mathieu (inworld), atempo 1.06 ; speed 1.08, une synthèse par réplique, silences de bord coupés,
# silences internes plafonnés à 0,16 s, 0,2 s au début et 0,45 s entre répliques.
NAME = 'hacoo58'
TITLE = 'Hacoo duo dessine stop bleu roi'
LINES = [
 ("Mon panier sur l'appli Hacou est prêt. Je valide !", [("Mon panier", None), ("sur l'appli <em>Hacoo</em>", None), ("est prêt.", None), ("Je <em>valide&nbsp;!</em>", None)]),
 ("Stop ! Tu paies combien, là ?", [("<em>Stop&nbsp;!</em>", None), ("Tu paies combien, là ?", None)]),
 ("Plaid, chaussons, bouillotte : soixante-trois euros.", [("Plaid, chaussons,", None), ("bouillotte :", None), ("<em>63&nbsp;€</em>", "soixante-trois euros.")]),
 ("Et le code promo, tu l'as mis ?", [("Et le <em>code promo</em>,", None), ("tu l'as mis ?", None)]),
 ("Quel code promo ?", [("Quel <em>code promo&nbsp;?</em>", None)]),
 ("Code promo Hacou : H, Z, K, link. Dans la case, avant de payer. Appliquer.", [("<em>Code promo Hacoo</em>", None), ("<i>hzklink</i>", "H, Z, K, link."), ("Dans la case,", None), ("avant de payer.", None), ("<em>Appliquer.</em>", None)]),
 ("Huit euros quatre-vingt-deux de moins ?! Cinquante-quatre euros et dix-huit centimes !", [("<em>8,82&nbsp;€</em>", "Huit euros quatre-vingt-deux"), ("de <em>moins&nbsp;?!</em>", None), ("<em>54,18&nbsp;€&nbsp;!</em>", "Cinquante-quatre euros et dix-huit centimes !")]),
 ("Envoie ça au pote qui valide trop vite. Code promo Hacou, H, Z, K, link. Les liens sont dans ma bio.", [("Envoie ça au pote", None), ("qui valide trop vite.", None), ("<em>Code promo Hacoo</em>", None), ("<i>hzklink</i>", "H, Z, K, link."), ("Les liens sont", None), ("dans ma <em>bio</em>.", None)]),
]
SPLITS = [(0.2, 2.399), (2.849, 4.401), (4.851, 7.531), (7.981, 9.02), (9.47, 10.118), (10.568, 16.07), (16.52, 19.986), (20.436, 27.144)]
DUO_LINES = [
 {'who': 'P', 'M': 'idle', 'P': 'talk', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'point', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'idle', 'P': 'cool', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'hip', 'P': 'idle', 'shot': 'M'},
 {'who': 'P', 'M': 'idle', 'P': 'think', 'shot': 'P'},
 {'who': 'M', 'M': 'point', 'P': 'think', 'shot': 'wide', 'lbl': False},
 {'who': 'P', 'M': 'cool', 'P': 'shock', 'shot': 'wide', 'lbl': False},
 {'who': 'M', 'M': 'talk', 'P': 'idle', 'shot': 'wide', 'lbl': False},
]
JS = duo2d_js(DUO_LINES, p_bun=False, cap='#2b59c3')

MINT = '#2b59c3'  # bleu roi
CSS = '''
#sub{left:90px;width:840px;font-size:68px}
.hook{left:90px;width:840px;font-size:70px}
#sub em{background:''' + MINT + '''}
.hook em{color:''' + MINT + '''}
.hook mark{background:#d6e2ff}
.tag.blue{background:#d6e2ff;color:#173a8a}
.tag.green{background:''' + MINT + '''}
.tk{position:absolute;width:600px;padding:14px 34px 12px;background:#fff;border:6px solid #111;border-radius:22px;box-shadow:9px 11px 0 #111;font:700 34px 'Inter',sans-serif;color:#111;white-space:nowrap;transform:rotate(-2deg)}
.tk .h{font:900 26px Inter;letter-spacing:3px;text-align:center;color:#555;border-bottom:4px dashed #bbb;padding-bottom:10px;margin-bottom:10px}
.tk .r{display:flex;justify-content:space-between;line-height:1.5}
.tk .r.no{position:relative;color:#e63946;font-weight:900;font-size:34px;margin:8px 0}
.tk .r.cd{position:relative;color:''' + MINT + ''';font-weight:900;font-size:40px;margin:8px 0}
.tk .r.cd b{position:relative}
.tk .r.cd b:after{content:'';position:absolute;left:-14px;top:-6px;right:-10px;bottom:-6px;border:5px solid #e63946;border-radius:50%;transform:rotate(-4deg)}
.tk .r.tt{border-top:4px dashed #bbb;margin-top:8px;padding-top:6px;font:900 38px Inter}
.tk .x{text-align:center;font:700 18px Inter;letter-spacing:2px;color:#888;text-transform:uppercase;margin-top:6px}
.endc .nt{margin-top:12px;font:700 32px 'Comic Relief','Comic Sans MS',cursive;color:#e63946}
.stampo{position:absolute;padding:6px 22px;border:7px solid #e63946;border-radius:14px;color:#e63946;font:900 50px Inter;letter-spacing:2px;transform:rotate(-12deg);background:rgba(255,255,255,.85);white-space:nowrap}
'''



def prod(ic, name, price, g, x, y, w=240):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;padding:10px 0 12px" data-g="{g}" data-fx="pop">'
            f'<span class="ico">{icon(ic, 115)}</span><div class="t">{name}</div><div class="p" style="font-size:58px">{price}</div><div class="x">prix d\'exemple</div></div>')




def panier(x, y):
    return (f'<div class="tk pn" style="left:{x}px;top:{y}px"><div class="h">PANIER · APPLI HACOO</div>'
            '<div class="r"><span>plaid</span><span>31,00 €</span></div>'
            '<div class="r"><span>chaussons</span><span>19,00 €</span></div>'
            '<div class="r"><span>bouillotte</span><span>13,00 €</span></div>'
            '<div class="r no"><span>code promo</span><span>aucun</span></div>'
            '<div class="r tt"><span>total</span><span>63,00 €</span></div><div class="x">prix d\'exemple</div></div>')


BODY = duo2d_body('la maligne', 'le pigeon') + '''
  <div class="scene" data-s="0"><div class="hook"><em>STOP</em>, il valide<br>son panier <mark>Hacoo</mark></div>''' + panier(230, 400) + '''
   <div class="stampo" style="left:395px;top:840px;font-size:40px">PLEIN POT</div></div>
''' + anc('M', '<div class="tag red" style="left:-150px;top:-150px" data-g="1.0" data-fx="stamp">STOP !</div>', '1') + '''
  <div class="scene" data-s="2" data-in="pop">''' + prod('Plaid', 'plaid', '31 €', '2.0', 110, 230) + prod('Chaussons', 'chaussons', '19 €', '2.0', 420, 210) + prod('Bouillotte', 'bouillotte', '13 €', '2.1', 700, 230, 220) + '''
   <div class="tag" style="left:395px;top:560px" data-g="2.2" data-fx="stamp">= 63,00 €</div></div>
''' + anc('M', '<div class="tag blue" style="left:-230px;top:-150px" data-g="3.0" data-fx="stamp">CODE PROMO HACOO ?</div>', '3') + '''
''' + anc('P', '<div class="bub" style="left:-120px;top:-230px" data-g="4.0" data-fx="stamp">?!</div>', '4') + '''
  <div class="scene" data-s="5" data-in="pop">
   <div class="phone" style="left:270px;top:230px" data-g="5.0" data-fx="up"><div class="t">CODE PROMO HACOO</div>
    <div class="f"><span data-g="5.1" data-fx="type">hzklink</span></div><div class="ok" data-g="5.4" data-fx="fade">Appliquer ✓ -14 %</div></div>
  </div>
  <div class="scene" data-s="6" data-in="pop">
   <div class="tag green" style="left:330px;top:220px" data-g="6.0" data-fx="stamp">-14 % = -8,82 €</div>
   <div class="card" style="left:240px;top:330px;width:600px;padding:18px 0" data-g="6.2" data-fx="stamp" data-slow="6.2"><div class="t">avec le code promo hacoo</div><div class="p" style="font-size:120px;color:''' + MINT + '''">54,18 €</div><div class="x"><span style="text-transform:none">hzklink</span> · -14 % · prix d'exemple</div></div>
  </div>
  <div class="scene" data-s="7" data-in="pop" style="z-index:7">
   <div class="endc" style="top:215px;left:95px;width:820px" data-g="7.0" data-fx="up"><div class="k">CODE PROMO HACOO</div><div class="c">hzklink</div><div class="d">-14 % sur l'appli Hacoo</div>
    <div class="b" data-g="7.4" data-fx="pop">liens des articles tendance en bio</div><div class="nt" data-g="7.1" data-fx="pop">envoie ça au pote qui valide trop vite</div><div class="x">Prix d'exemple · -14 % avec le code promo Hacoo hzklink · Offre soumise aux conditions en vigueur sur l'appli Hacoo</div></div>
  </div>
'''
CSS += '.tk.pn{font-size:30px;padding:10px 30px 8px}.tk.pn .r{line-height:1.32}'
