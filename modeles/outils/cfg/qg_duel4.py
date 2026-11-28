import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Vidéos QG du 28/11/2026, vidéo 2 : duel Monabanq / Revolut. Format F14 « Pourquoi la banque te paie » (3e F14, 1re en duel).
# Style V3 « nuit & or », variante améthyste, SANS l'habillage caméra (REC · CAM 01) de la routine Claude chat, avec sous-titres
# en pastille (pour ne pas refaire le gabarit quotidien du compte). Règles anti-bannissement du 26/11 : aucun montant écrit ni dit
# (le « jusqu'à 280 € » Monabanq a été retiré de l'oral : lu « 240 € » par la voix, 2e fois en 2 essais), pas de billets,
# bandeau de mentions permanent. Aucun chiffre de coût de pub (pas de source officielle).
# Sources consultées le 28/11/2026 : https://www.monabanq.com/fr/parrainage.html (filleul jusqu'à 280 € sous conditions, parrain
# jusqu'à 50 € par filleul, 5 par année glissante) ; https://help.revolut.com/fr-FR/help/referrals/more-help-with-referrals/referrals-new/what-are-the-conditions-of-the-referral-campaign/
# (« Seule la personne qui invite des amis peut prétendre à la récompense, sauf si nous vous avons informé(e) d'autres récompenses » ;
# 5 parrainages réussis max par campagne).
# Après contrôle et gardien (28/11) : cartes du début dans la zone sûre, plus de sol quadrillé (fond points dorés + halo améthyste),
# « la banque récompense ses clients » à l'écran, schéma et 1re carte dès le début de leur phrase, mois en cercles (pas de carrés dorés), mentions plus lisibles.
# Voix : Manon (smallest lightning_v3.1_pro), une synthèse par réplique, atempo 0.8-1.02.
NAME = 'qg_duel4'
TITLE = 'QG duel Monabanq Revolut pourquoi la banque paie'
ROOT = ':root{--bg:#07060a}'
JS = 'const CAM=0.45, PUSH=0.012;' + '''
function extra(t){document.querySelectorAll('.flo').forEach((e,i)=>{e.style.translate=`0 ${Math.sin(t*3+i*1.7)*9}px`});
 const d=document.querySelectorAll('.mo i'); d.forEach((e,k)=>{const s=S[5]+0.35+k*0.12;e.classList.toggle('on',t>=s)});}
'''
GAP = 0.28
TAIL = 1.3
MINLEN = 1.5
LINES = [
 ("Parrainage Monabanque ou Revolut : pourquoi ces banques paient ?",
  [("<em>Parrainage Monabanq</em>", None), ("ou <em>Revolut</em> :", None), ("pourquoi ces banques", None), ("<i>paient</i> ?", None)]),
 ("Rien de louche : la pub leur coûte très cher.",
  [("Rien de <em>louche</em> :", None), ("la pub leur coûte", None), ("<i>très cher</i>.", None)]),
 ("Avec le parrainage, cet argent va aux clients, pas aux affiches.",
  [("Avec le <em>parrainage</em>,", None), ("cet argent va aux clients,", None), ("pas aux <i>affiches</i>.", None)]),
 ("Monabanque paie les deux : une prime pour toi si tu remplis les conditions, et une pour ton parrain.",
  [("<em>Monabanq</em> paie les deux :", None), ("une prime pour <em>toi</em>", None), ("si tu remplis les conditions,", None), ("et une pour ton <em>parrain</em>.", None)]),
 ("Revolut, elle, récompense surtout le parrain. Pour toi, pas de prime en argent.",
  [("<em>Revolut</em>, elle,", None), ("récompense surtout le parrain.", None), ("Pour toi,", None), ("<i>pas de prime en argent</i>.", None)]),
 ("Leur pari : que tu restes client longtemps.",
  [("Leur <em>pari</em> :", None), ("que tu restes client", None), ("<em>longtemps</em>.", None)]),
 ("Si tu veux que je te parraine, écris-moi en privé.",
  [("Si tu veux", None), ("que je te parraine,", None), ("écris-moi", None), ("en <em>privé</em>.", None)]),
]
SPLITS = [(0.0, 2.912), (3.412, 5.9), (6.4, 9.954), (10.454, 15.769), (16.269, 20.491), (20.991, 23.182), (23.682, 26.664)]

A = '#b98cff'  # accent améthyste

CSS = '''
#bgtex{background:radial-gradient(ellipse 70% 45% at 50% 52%,rgba(120,80,190,.28),transparent 70%),radial-gradient(circle,rgba(217,162,76,.10) 2px,transparent 2.5px) 0 0/36px 36px,#09070d !important}
#sub{display:block;position:absolute;left:110px;top:1400px;width:780px;padding:14px 26px;border-radius:44px;background:rgba(14,11,20,.88);border:2px solid rgba(217,162,76,.55);
 text-align:center;font:800 50px/1.15 Inter;color:#f4efe6;z-index:7}
#sub:empty{display:none}
#sub em{font-style:normal;color:#f3c766}
#sub i{font-style:normal;color:#c9a6ff}
.ment{position:absolute;left:110px;top:196px;width:780px;padding:10px 16px 12px;border:2px solid rgba(217,162,76,.75);border-radius:18px;background:rgba(10,8,14,.92);text-align:center;z-index:9}
.ment b{display:block;font:800 27px Inter;color:#f4efe6;white-space:nowrap}
.ment span{display:block;font:700 23px Inter;color:#f3c766;white-space:nowrap}
.hd{left:80px;width:840px}
.am{color:#c9a6ff;text-shadow:0 0 20px rgba(185,140,255,.55)}
.vs{position:absolute;left:400px;top:700px;width:200px;height:200px;border-radius:50%;border:6px solid #e0ac55;display:flex;align-items:center;justify-content:center;font:900 84px 'DejaVu Serif',serif;
 color:#f3c766;background:radial-gradient(circle,#2a1f10,#0c0a08);box-shadow:0 0 60px rgba(240,180,80,.45)}
.bk{position:absolute;top:640px;width:300px;height:320px;border-radius:40px;border:3px solid rgba(217,162,76,.7);background:rgba(28,22,36,.75);text-align:center;padding-top:40px}
.bk .n{font:900 42px Inter;color:#f4efe6;letter-spacing:2px;margin-top:22px;white-space:nowrap}
.ico{stroke:#f3c766;stroke-width:7;fill:none;stroke-linecap:round;stroke-linejoin:round}
.ic{position:absolute;width:250px;height:250px}
.lab{position:absolute;font:800 38px Inter;color:#e9e4da;white-space:nowrap;text-align:center}
.stp{position:absolute;padding:12px 30px;border:7px solid #c9a6ff;color:#c9a6ff;font:900 60px Inter;letter-spacing:2px;transform:rotate(-7deg);border-radius:16px;background:rgba(14,11,20,.85);white-space:nowrap}
.xbar{position:absolute;height:14px;border-radius:7px;background:#e0453a;transform-origin:0 50%;box-shadow:0 0 18px rgba(224,69,58,.6)}
.who{position:absolute;width:150px;height:200px}
.card{position:absolute;left:110px;width:780px;height:180px;border-radius:30px;border:3px solid rgba(217,162,76,.7);background:rgba(28,22,36,.8);display:flex;align-items:center;gap:30px;padding:0 34px}
.card .bd{flex:none;width:96px;height:96px;border-radius:50%;display:flex;align-items:center;justify-content:center;font:900 58px Inter}
.card .bd.ok{background:#1f9d6b;color:#fff;box-shadow:0 0 26px rgba(95,227,168,.5)}
.card .bd.no{background:#5a1d1a;color:#ff8a80;border:4px solid #e0453a}
.card b{display:block;font:900 46px Inter;color:#f4efe6;white-space:nowrap}
.card span{display:block;font:600 32px Inter;color:#cfc6b6;margin-top:6px;white-space:nowrap}
.mo{position:absolute;left:130px;top:760px;width:740px;display:grid;grid-template-columns:repeat(6,1fr);gap:22px}
.mo i{display:block;height:100px;border-radius:50%;border:3px solid rgba(217,162,76,.45);background:rgba(28,22,36,.7)}
.mo i.on{background:rgba(185,140,255,.12);border:5px solid #c9a6ff;box-shadow:0 0 22px rgba(185,140,255,.45)}
.ch2{position:absolute;left:110px;width:720px}
.bb{max-width:560px;padding:22px 30px;border-radius:34px;font:700 40px/1.2 Inter;margin-bottom:22px}
.bb.me{margin-left:auto;background:linear-gradient(180deg,#f6d27a,#d9a24c);color:#1a1408;border-bottom-right-radius:8px}
.bb.you{background:#2a2433;color:#f4efe6;border-bottom-left-radius:8px}
.cond{left:110px;width:780px;font-size:29px;color:#d6cfc2}
'''


def ico(kind, x, y, g, s=250):
    P = {
        'bank': '<path d="M30 92 L125 34 L220 92 Z"/><path d="M40 100 L210 100"/><path d="M62 112 L62 190 M104 112 L104 190 M146 112 L146 190 M188 112 L188 190"/><path d="M30 204 L220 204"/>',
        'tv': '<rect x="20" y="60" width="210" height="140" rx="18"/><path d="M95 26 L125 60 L155 26"/><path d="M70 200 L58 230 M180 200 L192 230"/><path d="M62 150 l30 -30 l30 30 l30 -30 l30 30"/>',
        'pub': '<rect x="35" y="20" width="180" height="170" rx="8"/><path d="M125 190 L125 232 M80 232 L170 232"/><text x="125" y="128" text-anchor="middle" style="font:900 66px Inter;fill:#f3c766;stroke:none">PUB</text>',
        'phone': '<rect x="70" y="16" width="110" height="214" rx="22"/><circle cx="125" cy="86" r="26"/><path d="M90 160 Q125 120 160 160"/><path d="M112 196 L138 196"/>',
        'person': '<circle cx="125" cy="70" r="44"/><path d="M50 230 Q50 130 125 130 Q200 130 200 230"/>',
    }[kind]
    return (f'<svg class="ic flo" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px" viewBox="0 0 250 250" data-g="{g}" data-fx="pop"><g class="ico">{P}</g></svg>')


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


BODY = '''
  <div class="ment"><b>Lien de parrainage : je touche une prime</b><span>Offre soumise à conditions</span></div>
  <div class="scene" data-s="0">''' + hd(320, [('h1', 'PARRAINAGE', None, 'font-size:70px'), ('h1 gold', 'MONABANQ', None, 'font-size:92px'), ('h1 am', 'OU REVOLUT', None, 'font-size:80px')]) + '''
   <div class="bk" style="left:80px"><svg width="170" height="170" viewBox="0 0 250 250"><g class="ico">''' + \
    '<path d="M30 92 L125 34 L220 92 Z"/><path d="M40 100 L210 100"/><path d="M62 112 L62 190 M104 112 L104 190 M146 112 L146 190 M188 112 L188 190"/><path d="M30 204 L220 204"/>' + \
    '''</g></svg><div class="n">MONABANQ</div></div>
   <div class="bk" style="left:620px"><svg width="170" height="170" viewBox="0 0 250 250"><g class="ico" style="stroke:#c9a6ff">''' + \
    '<rect x="70" y="16" width="110" height="214" rx="22"/><circle cx="125" cy="86" r="26"/><path d="M112 196 L138 196"/>' + \
    '''</g></svg><div class="n">REVOLUT</div></div>
   <div class="vs" data-g="0.0" data-fx="stamp">VS</div>
   <div class="it gold" style="position:absolute;left:80px;width:840px;text-align:center;top:1060px;font-size:70px" data-g="0.2" data-fx="up">pourquoi elles paient ?</div></div>
  <div class="scene" data-s="1" data-in="right">''' + hd(330, [('h1', 'RIEN DE LOUCHE', '1.0', 'font-size:78px'), ('it gold', 'la pub coûte très cher', '1.1', 'font-size:66px')]) + \
    ico('tv', 70, 640, '1.1') + ico('pub', 380, 600, '1.1') + ico('phone', 690, 640, '1.2') + '''
   <div class="lab" style="left:110px;top:910px" data-g="1.1" data-fx="up">télé</div><div class="lab" style="left:425px;top:880px" data-g="1.1" data-fx="up">affiches</div>
   <div class="lab" style="left:680px;top:910px" data-g="1.2" data-fx="up">influenceurs</div>
   <div class="stp" style="left:300px;top:1060px" data-g="1.2" data-fx="stamp" data-slow="1.2">TRÈS CHER</div></div>
  <div class="scene" data-s="2" data-in="up">''' + hd(330, [('h1', 'AVEC LE PARRAINAGE', '2.0', 'font-size:70px'), ('it gold', 'la banque récompense ses clients', '2.1', 'font-size:56px')]) + \
    ico('pub', 90, 640, '2.0', 230) + '''
   <div class="xbar" style="left:90px;top:760px;width:250px;transform:rotate(-30deg) translateX(30px)" data-g="2.2" data-fx="strike"></div>''' + \
    ico('person', 560, 600, '2.0', 200) + ico('person', 740, 700, '2.0', 170) + '''
   <svg class="abs" style="left:350px;top:700px" width="200" height="120" viewBox="0 0 200 120" data-g="2.0" data-fx="left"><path d="M10 60 L170 60 M140 30 L176 60 L140 90" class="ico" style="stroke-width:10"/></svg>
   <div class="lab" style="left:90px;top:900px;color:#ff8a80" data-g="2.2" data-fx="up">moins d'affiches</div><div class="lab" style="left:590px;top:900px;color:#f3c766" data-g="2.0" data-fx="up">ses clients</div></div>
  <div class="scene" data-s="3" data-in="right">''' + hd(330, [('h1 gold', 'MONABANQ', '3.0', 'font-size:84px'), ('it', 'paie les deux', '3.0', 'font-size:66px')]) + '''
   <div class="card" style="top:640px" data-g="3.0" data-fx="left"><div class="bd ok">✓</div><div><b>TOI, LE FILLEUL</b><span>une prime si conditions remplies</span></div></div>
   <div class="card" style="top:860px" data-g="3.3" data-fx="left"><div class="bd ok">✓</div><div><b>TON PARRAIN</b><span>une prime lui aussi</span></div></div>
   <div class="lab" style="left:110px;width:780px;top:1080px;font-size:32px;color:#cfc6b6;white-space:normal" data-g="3.2" data-fx="up">montants et conditions sur le site de la banque</div></div>
  <div class="scene" data-s="4" data-in="right">''' + hd(330, [('h1 am', 'REVOLUT', '4.0', 'font-size:84px'), ('it', 'surtout le parrain', '4.1', 'font-size:66px')]) + '''
   <div class="card" style="top:640px" data-g="4.0" data-fx="right"><div class="bd ok">✓</div><div><b>LE PARRAIN</b><span>récompensé si tu remplis les étapes</span></div></div>
   <div class="card" style="top:860px" data-g="4.2" data-fx="right"><div class="bd no">✗</div><div><b>TOI, LE FILLEUL</b><span>pas de prime en argent</span></div></div>
   <div class="lab" style="left:110px;width:780px;top:1080px;font-size:32px;color:#cfc6b6;white-space:normal" data-g="4.3" data-fx="up">sauf autre avantage annoncé par Revolut</div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(330, [('h1', 'LEUR PARI', '5.0', 'font-size:80px'), ('it gold', 'un client fidèle', '5.1', 'font-size:70px')]) + '''
   <div class="mo">''' + ''.join('<i></i>' for _ in range(12)) + '''</div>
   <div class="lab" style="left:110px;width:780px;top:1060px" data-g="5.2" data-fx="up">mois après mois, <span style="color:#f3c766">gagnant-gagnant</span></div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(320, [('h1 s', 'TU VEUX UN PARRAIN ?', '6.0', 'font-size:64px')]) + '''
   <div class="ch2" style="top:460px"><div class="bb you" data-g="6.0" data-fx="left">Tu peux me parrainer ?</div>
    <div class="bb me" data-g="6.2" data-fx="right">Oui, écris-moi en privé</div></div>
   <div class="pill" style="top:780px;left:110px;width:780px" data-g="6.3" data-fx="up"><div class="pin">@</div><div><b>@htm.invest</b><span>Monabanq ou Revolut : je t'explique</span></div></div>
   <div class="cond" style="top:930px">Offres soumises aux conditions en vigueur · Monabanq : prime de bienvenue pour le filleul sous conditions (ouverture, versements, paiements carte…) et prime pour le parrain, 5 parrainages par année glissante · Revolut : seul le parrain est récompensé, sauf autre récompense annoncée par Revolut ; 5 parrainages réussis maximum par campagne · Lien de parrainage : je touche une prime.</div></div>
'''
