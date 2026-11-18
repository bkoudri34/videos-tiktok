import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# 3 banques, 18/11/2026 16:00 - style v3 nuit & or, accent bleu cobalt. Format F8 « résultat d'abord » :
# écran verrouillé avec 3 notifications de primes dès la 1re image, puis une notification par banque, total 770 € (ralenti), appel à l'action.
# Hello bank jusqu'à 330 € (80 € ouverture Hello Prime + 50 € au 13e mois + 200 € bon d'achat Hello Start+, jusqu'au 08/12/2026 ; hellobank.fr consulté le 18/11)
# + Fortuneo jusqu'à 260 € (carte Gold, du 02/11 au 20/12/2026 ; moneyvox.fr, francetransactions.com)
# + BoursoBank jusqu'à 180 € pour le filleul (boursobank.com/bon-plan/parrainage-boursobank consulté le 18/11 : 20 + 40 + 40 + 80 €).
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'trio11'
TITLE = '3 banques notifications cobalt'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Parrainage banque : jusqu'à sept cent soixante-dix euros, en trois primes.", [("Parrainage banque :", None), ("jusqu'à 770 €,", None), ("en 3 primes.", None)]),
 ("Première notif : Hello bank, jusqu'à trois cent trente euros, avant le huit décembre.", [("Première notif :", None), ("Hello bank,", None), ("jusqu'à 330 €,", None), ("avant le 8 décembre.", None)]),
 ("Deuxième : Fortunéo, jusqu'à deux cent soixante euros, avant le vingt décembre.", [("Deuxième :", None), ("Fortuneo,", None), ("jusqu'à 260 €,", None), ("avant le 20 décembre.", None)]),
 ("Troisième : Bourso Bank, jusqu'à cent quatre-vingts euros pour le filleul.", [("Troisième :", None), ("BoursoBank,", None), ("jusqu'à 180 €", None), ("pour le filleul.", None)]),
 ("Au total, sept cent soixante-dix euros au maximum, sous conditions.", [("Au total,", None), ("770 €", None), ("maximum,", None), ("sous conditions.", None)]),
 ("Envoie-moi le mot parrainage en privé, je t'envoie les trois liens.", [("Envoie-moi", None), ("le mot", None), ("PARRAINAGE", None), ("en privé,", None), ("je t'envoie les 3 liens.", None)]),
]
SPLITS = [(0.0, 3.27), (3.85, 7.67), (8.22, 11.70), (12.42, 15.39), (15.97, 18.64), (19.26, 21.44)]
GSTART = [[0.0, 1.0, 2.7], [3.9, 4.8, 5.5, 6.9], [8.22, 8.9, 9.6, 11.0], [12.42, 12.9, 13.8, 14.9], [15.97, 16.6, 17.5, 18.1], [19.3, 19.6, 19.8, 20.2, 20.7]]
MINLEN = 2.0
GAP = 0.32
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.cb{color:#7fa2ff;text-shadow:0 0 18px rgba(77,124,255,.55)}
.lock{position:absolute;left:170px;top:640px;width:740px;height:880px;border-radius:70px;background:linear-gradient(180deg,#0d1530,#070a16 70%);border:10px solid #23262f;box-shadow:0 0 0 2px #4a4f5c,0 30px 90px rgba(0,0,0,.75);overflow:hidden}
.lock .clk{position:absolute;left:0;top:60px;width:100%;text-align:center;font:200 120px Inter;color:#e8ecff;letter-spacing:2px}
.lock .dt{position:absolute;left:0;top:200px;width:100%;text-align:center;font:600 30px Inter;color:#9fb0e0}
.nt{position:absolute;left:30px;width:660px;height:150px;border-radius:34px;background:rgba(240,243,255,.93);color:#141824;display:flex;align-items:center;gap:22px;padding:0 26px;white-space:nowrap;box-shadow:0 12px 30px rgba(0,0,0,.35)}
.nt .ic{flex:none;width:84px;height:84px;border-radius:22px;background:#4d7cff;display:flex;align-items:center;justify-content:center}
.nt .tx{flex:1}
.nt b{display:block;font:800 32px Inter}
.nt span{display:block;font:600 30px Inter;color:#2c3550;margin-top:4px}
.nt small{position:absolute;right:26px;top:22px;font:600 22px Inter;color:#6a7390}
.big1{position:absolute;left:110px;top:760px;width:860px;border-radius:44px;background:#f2f4fb;color:#141824;padding:40px 46px;box-shadow:0 30px 90px rgba(0,0,0,.7),0 0 0 4px rgba(77,124,255,.5)}
.big1 .hdr{display:flex;align-items:center;gap:22px;font:800 38px Inter;white-space:nowrap}
.big1 .hdr .ic{width:84px;height:84px;border-radius:22px;background:#4d7cff;display:flex;align-items:center;justify-content:center}
.big1 .hdr small{margin-left:auto;font:600 24px Inter;color:#6a7390}
.big1 .lab{font:700 30px Inter;color:#4a5570;margin-top:30px;letter-spacing:1px}
.big1 .amt{font:900 104px 'DejaVu Serif',serif;color:#1b2e7a;line-height:1.1;white-space:nowrap}
.big1 .det{font:600 28px Inter;color:#3a4460;white-space:nowrap}
.chip{position:absolute;left:110px;height:92px;border-radius:46px;background:#4d7cff;color:#fff;font:800 38px Inter;display:flex;align-items:center;padding:0 34px;gap:16px;white-space:nowrap}
.step3{position:absolute;right:170px;height:92px;display:flex;gap:16px}
.step3 i{width:46px;height:46px;margin-top:23px;border-radius:50%;border:4px solid #4d7cff;background:transparent}
.step3 i.on{background:#4d7cff;box-shadow:0 0 20px rgba(77,124,255,.8)}
.stack{position:absolute;left:150px;top:700px;width:780px}
.stack .nt{position:relative;left:0;margin-bottom:22px;width:780px;height:130px}
.tot8{position:absolute;left:0;top:1190px;width:1080px;text-align:center}
.tot8 .v{font:900 190px 'DejaVu Serif',serif;line-height:1}
'''
BELL = '<svg width="50" height="50" viewBox="0 0 50 50"><path d="M25 6c-8 0-13 6-13 14v9l-5 7h36l-5-7v-9c0-8-5-14-13-14z" fill="#fff"/><circle cx="25" cy="42" r="5" fill="#fff"/></svg>'
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'


def nt(top, bank, txt, when='maintenant', g=None, fx='right'):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    st = f' style="top:{top}px"' if top is not None else ''
    return f'<div class="nt"{st}{a}><div class="ic">{BELL}</div><div class="tx"><b>{bank}</b><span>{txt}</span></div><small>{when}</small></div>'


def big(sid, bank, amt, det, date, k):
    dots = ''.join(f'<i class="{"on" if i <= k else ""}"></i>' for i in range(3))
    return f'''<div class="big1" data-g="{sid}.1" data-fx="pop"><div class="hdr"><div class="ic">{BELL}</div>{bank}<small>notification</small></div>
     <div class="lab">PRIME DE BIENVENUE</div><div class="amt">{amt}</div><div class="det">{det}</div></div>
   <div class="chip" style="top:1330px" data-g="{sid}.3" data-fx="up">{date}</div><div class="step3" style="top:1330px">{dots}</div>'''


BODY = hud('FRANCE · 3 BANQUES', 'NOTIFS') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(215, [('h1', 'PARRAINAGE BANQUE :', None, 'font-size:72px'), ('big gold', "jusqu'à 770 €", None, 'font-size:118px'), ('it cb', 'en 3 primes.', None, 'font-size:70px')]) + '''
   <div class="lock" style="top:640px"><div class="clk">16:00</div><div class="dt">mercredi 18 novembre</div>
    ''' + nt(300, 'Hello bank', "Prime : jusqu'à 330 €", 'il y a 2 min') + nt(470, 'Fortuneo', "Prime : jusqu'à 260 €", 'il y a 1 min') + nt(640, 'BoursoBank', "Prime : jusqu'à 180 €", 'maintenant') + '''</div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(230, [('h1 cb', 'PREMIÈRE NOTIF :', '1.0', ''), ('h1', 'HELLO BANK,', '1.1', ''), ('it gold', 'avant le 8 décembre.', '1.3', 'font-size:66px')]) + big(1, 'Hello bank', "jusqu'à 330 €", "80 € + 50 € + 200 € en bon d'achat", 'avant le 08/12', 0) + '''</div>
  <div class="scene" data-s="2" data-in="right">''' + hd(230, [('h1 cb', 'DEUXIÈME :', '2.0', ''), ('h1', 'FORTUNEO,', '2.1', ''), ('it gold', 'avant le 20 décembre.', '2.3', 'font-size:66px')]) + big(2, 'Fortuneo', "jusqu'à 260 €", 'avec la carte Gold (sous conditions)', 'avant le 20/12', 1) + '''</div>
  <div class="scene" data-s="3" data-in="right">''' + hd(230, [('h1 cb', 'TROISIÈME :', '3.0', ''), ('h1', 'BOURSOBANK,', '3.1', ''), ('it gold', 'pour le filleul.', '3.3', 'font-size:66px')]) + big(3, 'BoursoBank', "jusqu'à 180 €", '20 € + 40 € + 40 € + 80 €', 'offre de parrainage', 2) + '''</div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:1050px"></div>''' + hd(230, [('h1', 'AU TOTAL,', '4.0', ''), ('it gold', 'maximum, sous conditions.', '4.2', 'font-size:66px')]) + '''
   <div class="stack" style="top:470px">''' + nt(None, 'Hello bank', "jusqu'à 330 €", '1', '4.0', 'left') + nt(None, 'Fortuneo', "jusqu'à 260 €", '2', '4.0', 'right') + nt(None, 'BoursoBank', "jusqu'à 180 €", '3', '4.1', 'left') + '''</div>
   <div class="tot8" data-g="4.1" data-fx="stamp" data-slow="4.1" data-count="770"><div class="v gold">0 €</div></div></div>
  <div class="scene" data-s="5" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '5.0', ''), ('it gold', 'le mot', '5.1', 'font-size:60px'), ('big gold', '« PARRAINAGE »', '5.2', 'font-size:88px'), ('it gold', 'en privé,', '5.3', '')]) + '''
   <div class="pill" style="top:800px;border-color:rgba(77,124,255,.85)" data-g="5.4" data-fx="up"><div class="pin" style="background:#4d7cff;color:#fff">3</div><div><b>JE T'ENVOIE LES 3 LIENS</b><span>Hello bank · Fortuneo · BoursoBank</span></div></div>
   <div class="search" style="top:940px" data-g="5.4" data-fx="fade">''' + SEARCH + '''<span data-g="5.4" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1080px">Offres soumises aux conditions en vigueur · montants maximum, nouveaux clients<br>Hello bank : jusqu'à 330 € dont 200 € en bon d'achat, jusqu'au 08/12<br>Fortuneo : jusqu'à 260 € avec la carte Gold (sous conditions de revenus), jusqu'au 20/12<br>BoursoBank : jusqu'à 180 € pour le filleul (offre de parrainage)</div></div>
'''
