import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parraine import *
# 3 banques, 28/11/2026 (vidéo A) - style v3 nuit & or, accent améthyste. Format F18 « Parraine à ton tour », version 3 banques
# (règles de Badr du 26/11) : décor de gare de nuit (tableau des départs à volets, 3 « trains » = 3 banques), mascotte améthyste à noeud doré
# -> 1 je te parraine en privé + 2 tu ouvres ton compte -> 3 une fois client ton lien + 4 tu le partages -> Hello bank (voie 1)
# -> Fortuneo (voie 2) -> BoursoBank (voie 3) : prime par ami et plafond fixés par chaque banque, présentés un par un, jamais additionnés
# -> « un seul niveau » -> appel discret. AUCUN montant écrit : montants à l'oral seulement. Pas de total (voir legendes).
# Sources consultées le 28/11/2026 :
#   hellobank.fr/fr/votre-offre-parrainage : parrain 150 € par parrainage validé, limité à 20 parrainages par an ; invitation avant le 30/11/2026 15 h
#   fortuneo.fr/parrainage : parrain 120 € (filleul en Gold CB Mastercard) ou 80 € (Fosfo), jusqu'à 10 personnes par an ; offre du 01/11 au 30/11/2026
#   boursobank.com/bon-plan/parrainage-boursobank : récompense de l'offre en cours (montant non publié), limite de 20 primes sur 12 mois glissants
# Corrigé après contrôle (28/11) : mascotte vert menthe, « mon tour ? », pas de 2e niveau dessiné, carte BoursoBank « client équipé ».
# Voix : Speko (voix par défaut, speechify simba-3.5), speed 1.08, une synthèse par réplique, atempo 1.2, silences internes plafonnés à 0,18 s.
NAME = 'trio17'
TITLE = 'Trois banques parraine a ton tour amethyste'
ROOT = ':root{--bg:#07050b;--ac:#c49bff}'
LINES = [
 ("Parrainage Hello bank, Bourso Bank, Fortunéo : et si c'était toi, le parrain ?", [("Parrainage Hello bank, BoursoBank, Fortuneo :", None), ("et si c'était toi, le parrain ?", None)]),
 ("Un : je te parraine en privé. Deux : tu ouvres ton compte et tu remplis les conditions.", [("1 : je te parraine en privé.", None), ("2 : tu ouvres ton compte", None), ("et tu remplis les conditions.", None)]),
 ("Trois : une fois client, tu as ton propre lien. Quatre : tu le partages à tes amis.", [("3 : une fois client,", None), ("tu as ton propre lien.", None), ("4 : tu le partages à tes amis.", None)]),
 ("Hello bank : jusqu'à cent cinquante euros par ami, vingt par an.", [("Hello bank :", None), ("une prime par ami,", None), ("20 par an.", None)]),
 ("Fortunéo : jusqu'à cent vingt euros par ami, dix par an.", [("Fortuneo :", None), ("une prime par ami,", None), ("10 par an.", None)]),
 ("Bourso Bank : montant dans l'appli, vingt primes sur douze mois.", [("BoursoBank :", None), ("montant dans l'appli,", None), ("20 primes sur 12 mois.", None)]),
 ("Un seul niveau : je ne touche rien sur les amis de mes filleuls.", [("Un seul niveau :", None), ("je ne touche rien", None), ("sur les amis de mes filleuls.", None)]),
 ("Si tu veux que je te parraine, écris-moi en privé.", [("Si tu veux", None), ("que je te parraine,", None), ("écris-moi en privé.", None)]),
]
SPLITS = [(0.2, 3.521), (3.841, 7.37), (7.69, 10.865), (11.185, 13.657), (13.977, 16.621), (16.941, 19.328), (19.648, 21.887), (22.207, 23.895)]
MINLEN = 1.6
GAP = 0.28
TAIL = 1.5

CSS = PCSS + '''
.am{color:#c49bff;text-shadow:0 0 18px rgba(180,130,255,.5)}
.station{position:absolute;left:0;top:0;width:1080px;height:1920px;background:
 linear-gradient(180deg,rgba(0,0,0,0) 0,rgba(0,0,0,0) 1180px,rgba(196,155,255,.05) 1180px,rgba(0,0,0,0) 1500px)}
.pillar{position:absolute;top:150px;width:34px;height:1100px;background:linear-gradient(90deg,#141019,#241c30,#141019);opacity:.8}
.rail{position:absolute;left:-40px;width:1160px;height:8px;border-radius:4px;background:linear-gradient(90deg,rgba(224,172,85,.1),rgba(224,172,85,.55),rgba(224,172,85,.1))}
.clock{position:absolute;width:150px;height:150px;border-radius:50%;border:6px solid #e0ac55;background:#0c0a10;box-shadow:0 0 30px rgba(240,180,80,.35)}
.clock i{position:absolute;left:72px;top:22px;width:6px;height:53px;background:#f3c766;border-radius:3px;transform-origin:3px 53px}
.clock b{position:absolute;left:72px;top:40px;width:6px;height:35px;background:#fff;border-radius:3px;transform-origin:3px 35px;transform:rotate(-60deg)}
.board{position:absolute;left:100px;width:860px;border-radius:22px;background:#0d0b11;border:4px solid #2e2638;box-shadow:0 30px 80px rgba(0,0,0,.7);padding:22px 26px}
.board .hdr{display:flex;justify-content:space-between;font:800 24px Inter;color:#e0ac55;letter-spacing:3px;margin-bottom:10px}
.row{display:flex;align-items:center;gap:16px;margin-top:12px}
.flap{display:inline-block;padding:10px 14px;border-radius:8px;background:#1b1622;border-bottom:3px solid #000;font:800 34px 'DejaVu Sans Mono',monospace;color:#f3efe6;letter-spacing:2px;white-space:nowrap}
.flap.v{color:#c49bff;width:64px;text-align:center}
.flap.n{flex:1}
.flap.s{font-size:24px;color:#9fe0a0}
.row.hi .flap{background:#2a1f3a;color:#fff}.row.hi .flap.v{color:#f3c766}
.ticket{position:absolute;width:780px;border-radius:30px;background:#f4ede0;color:#191419;padding:30px 40px;box-shadow:0 26px 60px rgba(0,0,0,.6)}
.ticket .t{font:900 46px Inter;letter-spacing:1px;white-space:nowrap}
.ticket .t small{font:800 26px Inter;color:#7d5bb5;margin-left:14px;letter-spacing:2px}
.ticket .l{font:700 32px Inter;margin-top:16px;white-space:nowrap}
.ticket .l i{font-style:normal;display:inline-block;width:40px;height:40px;border-radius:50%;background:#7d5bb5;color:#fff;text-align:center;line-height:40px;font:900 24px Inter;margin-right:14px;vertical-align:3px}
.ticket .perf{position:absolute;left:0;right:0;top:-14px;height:28px;background:radial-gradient(circle at 14px 14px,#07050b 9px,transparent 10px) 0 0/40px 28px repeat-x}
.env{position:absolute;width:260px;height:170px;border-radius:16px;background:#f4ede0;box-shadow:0 26px 60px rgba(0,0,0,.6);overflow:hidden}
.env:before{content:'';position:absolute;left:0;top:0;border-left:130px solid transparent;border-right:130px solid transparent;border-top:92px solid #ddd0ea}
.env b{position:absolute;left:0;right:0;bottom:18px;text-align:center;font:900 22px Inter;color:#6b47a8;letter-spacing:2px}
.phone{position:absolute;width:300px;height:520px;border-radius:46px;background:#141012;border:6px solid #3a2f48;box-shadow:0 30px 80px rgba(0,0,0,.7)}
.phone .scr{position:absolute;left:18px;top:50px;right:18px;bottom:34px;border-radius:26px;background:linear-gradient(180deg,#1d1724,#100c14);text-align:center;color:#f3efe6}
.phone .scr .t{font:900 26px Inter;color:#c49bff;margin-top:28px;letter-spacing:1px}
.qr{width:170px;height:170px;margin:28px auto 0;border-radius:14px;background:#f4ede0;padding:14px;box-sizing:border-box;display:grid;grid-template-columns:repeat(7,1fr);gap:3px}
.qr i{background:#151010;border-radius:2px}.qr i.o{background:transparent}
.phone .btn{margin:30px auto 0;width:200px;padding:14px 0;border-radius:36px;background:#c49bff;color:#141010;font:900 24px Inter}
'''
QR = '<div class="qr">' + ''.join('<i class="o"></i>' if c == '0' else '<i></i>' for c in '1110111101010110111011000101101011100111011010111') + '</div>'
ME = '#7fd6a8'
DECOR = '<div class="station"></div><div class="pillar" style="left:30px"></div><div class="pillar" style="left:1016px"></div><div class="rail" style="top:1330px"></div><div class="rail" style="top:1380px"></div>'


def board(top, hi=None, g=None):
    a = f' data-g="{g}" data-fx="up"' if g else ''
    rows = [('1', 'HELLO BANK', "JUSQU'AU 30/11"), ('2', 'FORTUNEO', "JUSQU'AU 30/11"), ('3', 'BOURSOBANK', 'EN COURS')]
    out = ''.join(f'<div class="row{" hi" if hi == k else ""}"><span class="flap v">{v}</span><span class="flap n">{n}</span><span class="flap s">{s}</span></div>' for k, (v, n, s) in enumerate(rows))
    return f'<div class="board" style="top:{top}px"{a}><div class="hdr"><span>DÉPARTS · PARRAINAGE</span><span>VOIE</span></div>{out}</div>'


def ticket(top, name, voie, lines, g):
    ls = ''.join(f'<div class="l"{f" data-g={chr(34)}{gg}{chr(34)} data-fx={chr(34)}fade{chr(34)}" if gg else ""}><i>{ic}</i>{t}</div>' for ic, t, gg in lines)
    return f'<div class="ticket" style="left:150px;top:{top}px" data-g="{g}" data-fx="up"><div class="perf"></div><div class="t">{name}<small>VOIE {voie}</small></div>{ls}</div>'


BODY = hud('GARE DE NUIT · PARRAINE À TON TOUR', '3 BANQUES') + BANNER + '''
  <div class="scene" data-s="0">''' + DECOR + hdx(220, [('h1 am', 'PARRAINAGE', None, 'font-size:68px'), ('h1', 'HELLO BANK · BOURSOBANK', None, 'font-size:50px'), ('h1', 'FORTUNEO', None, 'font-size:50px'), ('it gold', "et si c'était toi, le parrain ?", None, 'font-size:56px')]) + \
    board(600) + mascot(400, 1040, 260, ME, 'bow') + '''
   <div class="bubble2" style="left:640px;top:1050px;transform:rotate(5deg)">mon tour ?</div></div>
  <div class="scene" data-s="1" data-in="right">''' + DECOR + '''
   <div class="num" style="left:100px;top:240px" data-g="1.0" data-fx="stamp">1</div>''' + hdx(255, [('h1', 'JE TE PARRAINE', '1.0', 'font-size:58px'), ('it am', 'en privé.', '1.0', 'font-size:62px')], left=270, width=660) + '''
   <div class="env" style="left:400px;top:470px" data-g="1.0" data-fx="right"><b>INVITATION</b></div>
   <div class="num" style="left:100px;top:720px" data-g="1.1" data-fx="stamp">2</div>''' + hdx(735, [('h1', 'TU OUVRES', '1.1', 'font-size:58px'), ('h1', 'TON COMPTE', '1.1', 'font-size:58px')], left=270, width=660) + '''
   <div class="card2" style="left:150px;top:960px;width:760px" data-g="1.2" data-fx="up"><div class="chk"><i>✓</i>ouverture avec l'invitation</div><div class="chk"><i>✓</i>conditions de l'offre remplies</div></div>
   ''' + mascot(800, 1200, 170, ME, 'bow', g='1.2') + '''</div>
  <div class="scene" data-s="2" data-in="up">''' + DECOR + '''
   <div class="num" style="left:100px;top:240px" data-g="2.0" data-fx="stamp">3</div>''' + hdx(255, [('h1', 'UNE FOIS CLIENT,', '2.0', 'font-size:56px'), ('it am', 'ton propre lien.', '2.1', 'font-size:62px')], left=270, width=660) + '''
   <div class="phone" style="left:110px;top:480px" data-g="2.1" data-fx="up"><div class="scr"><div class="t">MON LIEN</div>''' + QR + '''<div class="btn">Partager</div></div></div>
   <div class="num" style="left:500px;top:520px" data-g="2.2" data-fx="stamp">4</div>
   <div class="h1" style="position:absolute;left:470px;top:690px;width:440px;text-align:center;font-size:44px" data-g="2.2" data-fx="tw">TU LE PARTAGES</div>
   ''' + '<div class="share" style="position:absolute;left:640px;top:790px;font:900 64px Inter;color:#c49bff" data-g="2.2" data-fx="pop">↓</div>' + friend(470, 940, 170, ME, g='2.2') + friend(720, 940, 170, ME, g='2.2') + '''
   <div class="tagp" style="left:300px;top:1180px" data-g="2.2" data-fx="pop">à tes amis</div></div>
  <div class="scene" data-s="3" data-in="right">''' + DECOR + board(230, hi=0) + ticket(640, 'HELLO BANK', 1, [('✓', 'une prime par ami validé', '3.1'), ('✓', '20 parrainages par an', '3.2'), ('!', 'invitation avant le 30/11, 15 h', '3.2')], '3.0') + '''
   <div class="tagp" style="left:220px;top:1170px" data-g="3.2" data-fx="stamp" data-slow="3.2">plafond fixé par la banque</div></div>
  <div class="scene" data-s="4" data-in="right">''' + DECOR + board(230, hi=1) + ticket(640, 'FORTUNEO', 2, [('✓', 'une prime par ami, selon sa carte', '4.1'), ('✓', "jusqu'à 10 filleuls par an", '4.2'), ('!', 'offre du 01/11 au 30/11', '4.2')], '4.0') + '''
   <div class="tagp" style="left:220px;top:1170px" data-g="4.2" data-fx="pop">plafond fixé par la banque</div></div>
  <div class="scene" data-s="5" data-in="right">''' + DECOR + board(230, hi=2) + ticket(640, 'BOURSOBANK', 3, [('✓', "prime indiquée dans l'appli", '5.1'), ('✓', '20 primes sur 12 mois glissants', '5.2'), ('!', 'parrain : client équipé (carte, livret…)', '5.2')], '5.0') + '''
   <div class="tagp" style="left:220px;top:1170px" data-g="5.2" data-fx="pop">plafond fixé par la banque</div></div>
  <div class="scene" data-s="6" data-in="up">''' + DECOR + hdx(230, [('h1 am', 'UN SEUL NIVEAU', '6.0', 'font-size:72px'), ('it gold', 'je ne touche rien sur', '6.1', 'font-size:58px'), ('it gold', 'les amis de mes filleuls.', '6.2', 'font-size:58px')]) + \
    mascot(130, 640, 230, ME, 'bow') + link(360, 760, 500, 760) + friend(500, 680, 170, '#f3c766') + '''
   <div class="tagp" style="left:230px;top:1000px" data-g="6.1" data-fx="pop">toi → tes amis, c'est tout</div></div>
  <div class="scene" data-s="7" data-in="pop">''' + DECOR + '''<div class="clock" style="left:465px;top:250px"><i></i><b></b></div>''' + hdx(460, [('h1', 'SI TU VEUX QUE', '7.0', 'font-size:62px'), ('h1', 'JE TE PARRAINE,', '7.1', 'font-size:62px'), ('it am', 'écris-moi en privé.', '7.2', 'font-size:68px')]) + mascot(410, 780, 250, ME, 'bow', g='7.2') + '''
   <div class="cond" style="top:1080px;font-size:24px;color:#cfc8ba">Offres soumises aux conditions en vigueur · nouveaux clients<br>Hello bank et Fortuneo : offres jusqu'au 30/11/2026</div></div>
'''
