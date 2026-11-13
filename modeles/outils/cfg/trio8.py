import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# 3 banques, 13/11/2026 16:00 - style v3 nuit & or, accent corail. Plus de 700 € cumulés (770 € max) :
# Hello bank jusqu'à 330 € (80 € + 50 € Hello Prime + 200 € bon d'achat Hello Start +, demande validée au plus tard le 08/12/2026 ; moneyvox.fr 05/11/2026)
# + Fortuneo jusqu'à 260 € (160 € Gold CB après 5 paiements en 90 jours + 80 € mobilité + 20 € Livret +, du 02/11 au 20/12/2026 ; moneyvox.fr 12/11/2026)
# + BoursoBank jusqu'à 180 € (offre de parrainage filleul, comparabanques.fr mis à jour le 10/11/2026).
# Voix : Speko (speechify, voix par défaut), la voix clonée ElevenLabs était refusée (402, recharge nécessaire) le 13/11.
# Trois cartes retournées une à une -> deux pages de calendrier -> jauge qui monte à 770 € -> appel à l'action.
NAME = 'trio8'
TITLE = '3 banques corail'
ROOT = ':root{--bg:#07060a}'
LINES = [
 ("Trois banques veulent te payer. Tu dis non ?", [("3 banques veulent te payer.", None), ("Tu dis non ?", None)]),
 ("Première carte : Hello bank, jusqu'à trois cent trente euros.", [("Première carte :", None), ("Hello bank,", None), ("jusqu'à 330 €.", None)]),
 ("Deuxième carte : Fortunéo, jusqu'à deux cent soixante euros.", [("Deuxième carte :", None), ("Fortuneo,", None), ("jusqu'à 260 €.", None)]),
 ("Troisième carte : Bourso Bank, jusqu'à cent quatre-vingts euros.", [("Troisième carte :", None), ("BoursoBank,", None), ("jusqu'à 180 €.", None)]),
 ("Attention, Hello bank s'arrête le huit décembre, Fortunéo le vingt.", [("Attention,", None), ("Hello bank s'arrête", None), ("le 8 décembre,", None), ("Fortuneo le 20.", None)]),
 ("En cumulé, plus de sept cents euros à gagner.", [("En cumulé,", None), ("plus de 700 €", None), ("à gagner.", None)]),
 ("Envoie-moi PARRAINAGE en privé, je t'envoie les trois liens.", [("Envoie-moi", None), ("PARRAINAGE", None), ("en privé,", None), ("je t'envoie les 3 liens.", None)]),
]
SPLITS = [(0.0, 1.71), (2.18, 4.79), (5.56, 8.25), (8.96, 11.47), (12.06, 14.85), (15.29, 17.16), (17.67, 19.81)]
GSTART = [[0.05, 1.3], [2.18, 3.0, 3.8], [5.56, 6.4, 7.2], [8.96, 9.7, 10.4], [12.06, 12.7, 13.4, 14.2], [15.29, 16.0, 16.8], [17.67, 18.0, 18.4, 19.1]]
MINLEN = 2.2
GAP = 0.34
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.co{color:#ff7a59;text-shadow:0 0 18px rgba(255,122,89,.45)}
.cd{position:absolute;width:250px;height:360px;border-radius:22px;background:linear-gradient(160deg,#2b1712,#120a08);border:5px solid #d9a24c;box-shadow:0 30px 70px rgba(0,0,0,.7);overflow:hidden}
.cd:before{content:'';position:absolute;inset:16px;border-radius:14px;border:2px solid rgba(255,122,89,.55);background:repeating-linear-gradient(45deg,rgba(255,122,89,.10) 0 10px,transparent 10px 20px)}
.cd .n{position:absolute;left:0;top:130px;width:100%;text-align:center;font:900 90px 'DejaVu Serif',serif;color:#f3c766}
.big1{position:absolute;left:250px;top:700px;width:580px;height:760px;border-radius:36px;background:#f4efe4;color:#1c1310;box-shadow:0 50px 110px rgba(0,0,0,.75);transform:rotate(-3deg);text-align:center;overflow:hidden}
.big1 .k{margin-top:46px;font:800 26px 'DejaVu Sans Mono',monospace;letter-spacing:6px;color:#b0532f}
.big1 .bk{margin-top:18px;font:900 64px Inter;letter-spacing:1px;white-space:nowrap}
.big1 .am{margin-top:20px;font:900 150px 'DejaVu Serif',serif;color:#c2401f;line-height:1.1;white-space:nowrap}
.big1 .up{font:700 30px Inter;color:#6d5f55;margin-top:-6px}
.big1 .li{margin:26px 50px 0;text-align:left}
.big1 .li div{display:flex;justify-content:space-between;font:700 30px Inter;padding:13px 0;border-bottom:2px dashed rgba(28,19,16,.25);white-space:nowrap}
.big1 .li b{color:#c2401f}
.big1:before,.big1:after{content:'♦';position:absolute;font:900 44px 'DejaVu Sans';color:#ff7a59}
.big1:before{left:26px;top:20px}.big1:after{right:26px;bottom:20px}
.cal{position:absolute;top:720px;width:380px;height:440px;border-radius:26px;background:#f4efe4;color:#1c1310;text-align:center;box-shadow:0 40px 90px rgba(0,0,0,.7);overflow:hidden}
.cal .h{height:110px;background:#ff7a59;color:#fff;font:900 40px Inter;letter-spacing:4px;line-height:110px}
.cal .d{font:900 170px 'DejaVu Serif',serif;line-height:1.25}
.cal .m{font:800 34px Inter;letter-spacing:6px;color:#6d5f55}
.cal .x{position:absolute;left:30px;top:150px;width:320px;height:8px;background:#c2401f;border-radius:4px;transform-origin:0 50%}
.jar{position:absolute;left:330px;top:700px;width:420px;height:640px;border:6px solid #d9a24c;border-top:0;border-radius:0 0 60px 60px;overflow:hidden;background:rgba(255,255,255,.03)}
.jar .f{position:absolute;left:0;bottom:0;width:100%;height:100%;background:linear-gradient(180deg,#ff9b7e,#ff7a59 40%,#b9462a);transform-origin:50% 100%}
.jar .s1{position:absolute;left:0;width:100%;text-align:center;font:800 30px Inter;color:#fff;white-space:nowrap}
.tot{position:absolute;left:0;top:1360px;width:1080px;text-align:center}
'''


def big(tag, bank, amt, rows, g):
    r = ''.join(f'<div data-g="{g}.2" data-fx="left"><span>{a}</span><b>{v}</b></div>' for a, v in rows)
    return f'''<div class="big1" data-g="{g}.0" data-fx="stamp"><div class="k">{tag}</div><div class="bk" data-g="{g}.1" data-fx="pop">{bank}</div>
    <div class="up">jusqu'à</div><div class="am" data-g="{g}.2" data-fx="tick">{amt}</div><div class="li">{r}</div></div>'''


def side(open_ix):
    xs = [(60, -8), (790, 7)]
    out = ''
    k = 0
    for i in range(3):
        if i == open_ix: continue
        x, r = xs[k]; k += 1
        out += f'<div class="cd" style="left:{x}px;top:1180px;transform:rotate({r}deg) scale(.62);transform-origin:50% 50%"><div class="n">{i + 1}</div></div>'
    return out


BODY = hud('FRANCE · 3 BANQUES', 'CARTES') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(220, [('big gold', '3 BANQUES', None, 'font-size:150px'), ('it gold', 'veulent te payer.', None, 'font-size:80px'), ('h1 co', 'TU DIS NON ?', None, 'margin-top:14px')]) + '''
   <div class="cd" style="left:150px;top:860px;transform:rotate(-12deg)"><div class="n">?</div></div>
   <div class="cd" style="left:415px;top:820px"><div class="n">?</div></div>
   <div class="cd" style="left:680px;top:860px;transform:rotate(12deg)"><div class="n">?</div></div></div>
  <div class="scene" data-s="1" data-in="right">''' + hd(230, [('h1 s', 'PREMIÈRE CARTE :', '1.0', ''), ('it gold', 'Hello bank,', '1.1', 'font-size:84px'), ('it gold', "jusqu'à 330 €.", '1.2', 'font-size:70px')]) + side(0) + '''
   ''' + big('CARTE N° 1', 'HELLO BANK', '330 €', [('ouverture', '80 €'), ('Hello Prime', '+ 50 €'), ("bon d'achat", '+ 200 €')], 1) + '''</div>
  <div class="scene" data-s="2" data-in="left">''' + hd(230, [('h1 s', 'DEUXIÈME CARTE :', '2.0', ''), ('it gold', 'Fortuneo,', '2.1', 'font-size:84px'), ('it gold', "jusqu'à 260 €.", '2.2', 'font-size:70px')]) + side(1) + '''
   ''' + big('CARTE N° 2', 'FORTUNEO', '260 €', [('carte Gold', '160 €'), ('mobilité', '+ 80 €'), ('Livret +', '+ 20 €')], 2) + '''</div>
  <div class="scene" data-s="3" data-in="right">''' + hd(230, [('h1 s', 'TROISIÈME CARTE :', '3.0', ''), ('it gold', 'BoursoBank,', '3.1', 'font-size:84px'), ('it gold', "jusqu'à 180 €.", '3.2', 'font-size:70px')]) + side(2) + '''
   ''' + big('CARTE N° 3', 'BOURSOBANK', '180 €', [('ouverture + versement', '✓'), ('carte 3 mois', '✓'), ('EasyMove', '✓')], 3) + '''</div>
  <div class="scene" data-s="4" data-in="up">''' + hd(230, [('h1 co', 'ATTENTION,', '4.0', ''), ('it gold', "Hello bank s'arrête", '4.1', 'font-size:70px'), ('it gold', 'le 8 décembre,', '4.2', 'font-size:70px'), ('it gold', 'Fortuneo le 20.', '4.3', 'font-size:70px')]) + '''
   <div class="cal" style="left:110px;transform:rotate(-5deg)" data-g="4.1" data-fx="up"><div class="h">HELLO BANK</div><div class="d">08</div><div class="m">DÉCEMBRE</div></div>
   <div class="cal" style="left:590px;top:760px;transform:rotate(5deg)" data-g="4.3" data-fx="up"><div class="h">FORTUNEO</div><div class="d">20</div><div class="m">DÉCEMBRE</div></div>
   <div class="abs" style="left:0;top:1300px;width:1080px;text-align:center;font:800 32px Inter;letter-spacing:4px;color:#e9e4da" data-g="4.3" data-fx="fade">BOURSOBANK : SANS DATE ANNONCÉE</div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="rays" style="top:560px"></div>''' + hd(230, [('h1', 'EN CUMULÉ,', '5.0', ''), ('it gold', 'plus de 700 €', '5.1', 'font-size:96px'), ('it gold', 'à gagner.', '5.2', 'font-size:64px')]) + '''
   <div class="jar"><div class="f" data-g="5.0" data-fx="growY"></div>
    <div class="s1" style="bottom:40px">Hello bank 330 €</div><div class="s1" style="bottom:110px">Fortuneo 260 €</div><div class="s1" style="bottom:180px">BoursoBank 180 €</div></div>
   <div class="tot" data-g="5.1" data-fx="stamp" data-slow="5.1" data-count="770"><div style="font:800 32px Inter;letter-spacing:6px;color:#e9e4da">TOTAL MAXIMUM</div><div class="v gold" style="font:900 140px 'DejaVu Serif',serif;line-height:1.15">0 €</div></div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« PARRAINAGE »', '6.1', 'font-size:100px'), ('it gold', 'en privé,', '6.2', '')]) + '''
   <div class="pill" style="top:720px;border-color:rgba(255,122,89,.8)" data-g="6.3" data-fx="up"><div class="pin" style="background:#ff7a59">3</div><div><b>JE T'ENVOIE LES 3 LIENS</b><span>Hello bank · Fortuneo · BoursoBank</span></div></div>
   <div class="cond" style="top:870px">Offres soumises aux conditions en vigueur<br>montants maximum, nouveaux clients<br>Hello bank : dont 200 € en bon d'achat, demande validée au plus tard le 08/12<br>Fortuneo : carte Gold, jusqu'au 20/12 · BoursoBank : offre de parrainage</div></div>
'''
