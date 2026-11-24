import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Fortuneo, 24/11/2026 18:00 - style v3 nuit & or, accent vert émeraude. Format F8 « résultat d'abord » :
# notification « Virement reçu +150,00 € » + accroche « PARRAINAGE FORTUNEO : 150 € pour toi » dès la 1re image
# -> 1 : 1re ouverture avec la carte Gold + code parrain -> 2 : versement de 300 € dans les 6 jours (jours qui se cochent)
# -> résultat : 150 € (ralenti) versés au plus tard le 31/12 -> Fosfo : 80 € -> l'offre s'arrête le 30/11, il reste 6 jours
# -> appel à l'action + mini notification +150 € (reboucle sur l'accroche).
# Offre de parrainage Fortuneo (fortuneo.fr/parrainage, consultée le 24/11/2026) : du 01/11 au 30/11/2026, filleul 80 € avec Fosfo,
# 150 € avec Gold CB Mastercard, 1re ouverture, code parrain renseigné à la souscription, versement de 300 € dans les 6 jours
# suivant l'ouverture ; prime versée au plus tard le 31/12/2026.
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'fortuneo14'
TITLE = 'Fortuneo résultat émeraude'
ROOT = ':root{--bg:#03080a}'
LINES = [
 ("Parrainage Fortunéo : cent cinquante euros versés sur ton compte.", [("Parrainage Fortuneo :", None), ("150 € versés", None), ("sur ton compte.", None)]),
 ("Un : tu ouvres ton premier compte avec la carte Gold et mon code parrain.", [("1 : tu ouvres", None), ("ton premier compte", None), ("avec la carte Gold", None), ("et mon code parrain.", None)]),
 ("Deux : tu verses trois cents euros dans les six jours.", [("2 : tu verses 300 €", None), ("dans les 6 jours.", None)]),
 ("Résultat : cent cinquante euros, versés au plus tard le trente et un décembre.", [("Résultat :", None), ("150 €,", None), ("versés au plus tard", None), ("le 31 décembre.", None)]),
 ("Avec la carte Fosfo, c'est quatre-vingts euros.", [("Avec la carte Fosfo,", None), ("c'est 80 €.", None)]),
 ("Mais l'offre s'arrête le trente novembre : il reste six jours.", [("Mais l'offre s'arrête", None), ("le 30 novembre.", None), ("Il reste 6 jours.", None)]),
 ("Envoie-moi FORTUNÉO en privé, je t'envoie mon code parrain.", [("Envoie-moi", None), ("FORTUNEO", None), ("en privé,", None), ("je t'envoie mon code parrain.", None)]),
]
SPLITS = [(0.0, 2.80), (3.10, 6.05), (6.49, 8.31), (8.72, 11.59), (12.12, 14.01), (14.58, 17.05), (17.61, 19.83)]
GSTART = [[0.0, 1.2, 2.3], [3.1, 4.0, 4.7, 5.5], [6.5, 7.9], [8.72, 9.4, 10.2, 10.8], [12.12, 13.3], [14.7, 15.4, 16.3], [17.61, 17.9, 18.4, 19.0]]
MINLEN = 1.8
GAP = 0.28
TAIL = 2.2


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.hd{left:80px;width:880px}
.em{color:#46e0a8;text-shadow:0 0 18px rgba(50,220,160,.5)}
.nt{position:absolute;left:150px;width:760px;height:220px;border-radius:40px;background:linear-gradient(180deg,#0f2a22,#08160f);border:4px solid #46e0a8;box-shadow:0 30px 80px rgba(0,0,0,.7),0 0 60px rgba(50,220,160,.25);display:flex;align-items:center;gap:30px;padding:0 40px}
.nt .ic{flex:none;width:110px;height:110px;border-radius:30px;background:#46e0a8;color:#04140d;display:flex;align-items:center;justify-content:center;font:900 64px 'DejaVu Serif',serif}
.nt .tx{flex:1;white-space:nowrap}
.nt .tx small{display:block;font:700 26px Inter;color:#9fd9c2;letter-spacing:2px}
.nt .tx span{display:block;font:800 34px Inter;color:#eafff6;margin-top:6px}
.nt .tx b{display:block;font:900 72px 'DejaVu Serif',serif;color:#46e0a8;margin-top:4px}
.nt.mini{height:160px;gap:18px;padding:0 24px;border-radius:30px}
.nt.mini .ic{width:76px;height:76px;font-size:44px;border-radius:22px}
.nt.mini .tx small{font-size:20px}
.nt.mini .tx b{font-size:46px}
.stp{position:absolute;left:240px;width:600px;height:84px;border-radius:20px;border:5px solid #e9b456;color:#ffe3a8;display:flex;align-items:center;justify-content:center;font:900 32px Inter;letter-spacing:3px;white-space:nowrap;background:rgba(40,28,10,.7)}
.st3{position:absolute;left:150px;width:760px;display:flex;gap:18px}
.st3 .c{flex:1;height:150px;border-radius:26px;background:#0b1a14;border:3px solid #2e6e57;color:#cfeee2;text-align:center;font:800 26px Inter;letter-spacing:1px;white-space:nowrap;padding-top:18px}
.st3 .c b{display:block;font:900 56px 'DejaVu Serif',serif;color:#46e0a8;margin-bottom:6px}
.cd{position:absolute;width:340px;height:214px;border-radius:22px;box-shadow:0 30px 80px rgba(0,0,0,.7)}
.cd .chip{position:absolute;left:30px;top:78px;width:60px;height:46px;border-radius:9px;background:linear-gradient(135deg,#f6f1e7,#bfa98a)}
.cd .k{position:absolute;left:30px;top:24px;font:800 24px 'DejaVu Sans Mono',monospace;letter-spacing:4px}
.cd .n{position:absolute;left:30px;top:156px;font:700 22px 'DejaVu Sans Mono',monospace;letter-spacing:3px}
.fos{background:linear-gradient(135deg,#3a3f4f,#1b1e27 60%,#0e1016);border:3px solid #5b6275;color:#d8dbe6}
.gld{background:linear-gradient(135deg,#fff1c4,#e9b456 45%,#a8701f);color:#3a2810}
.fld{position:absolute;left:170px;width:740px;height:120px;border-radius:30px;background:#f3faf7;color:#062018;display:flex;align-items:center;gap:22px;padding:0 30px;white-space:nowrap}
.fld small{font:800 26px Inter;color:#3c7a63;letter-spacing:2px}
.fld b{font:900 44px 'DejaVu Sans Mono',monospace;letter-spacing:6px;flex:1}
.fld i{font-style:normal;flex:none;width:70px;height:70px;border-radius:50%;background:#46e0a8;color:#04140d;display:flex;align-items:center;justify-content:center;font:900 40px Inter}
.ok{position:absolute;left:260px;width:560px;height:90px;border-radius:45px;background:#0f2a22;border:4px solid #46e0a8;color:#c9f7e6;display:flex;align-items:center;justify-content:center;font:800 32px Inter;letter-spacing:1px;white-space:nowrap}
.dep{position:absolute;left:180px;width:720px;height:160px;border-radius:34px;background:#0b1a14;border:4px solid #46e0a8;display:flex;align-items:center;justify-content:center;gap:26px;white-space:nowrap}
.dep b{font:900 86px 'DejaVu Serif',serif;color:#fff}
.dep span{font:800 28px Inter;color:#9fe8c9;letter-spacing:2px;line-height:1.3}
.days{position:absolute;left:150px;width:760px;display:flex;justify-content:space-between}
.days .d{width:104px;height:124px;border-radius:22px;background:#0b1a14;border:3px solid #2e6e57;text-align:center;color:#9fd9c2;font:800 24px Inter;padding-top:14px}
.days .d b{display:block;font:900 52px 'DejaVu Serif',serif;color:#eafff6}
.days .d.on{background:#46e0a8;border-color:#46e0a8;color:#04140d}.days .d.on b{color:#04140d}
.tag{position:absolute;left:265px;width:550px;height:230px;border-radius:34px;display:flex;flex-direction:column;align-items:center;justify-content:center}
.tag b{font:900 140px 'DejaVu Serif',serif;line-height:1}
.tag small{font:800 26px Inter;letter-spacing:3px;white-space:nowrap}
.tag.g{background:linear-gradient(180deg,#2a1d0c,#120c05);border:5px solid #e9b456;color:#ffe9c0;box-shadow:0 0 60px rgba(240,180,80,.4)}
.tag.g small{color:#e8c98f}
.tag.f{background:#14171e;border:5px solid #5b6275;color:#e4e7ef;height:200px}
.tag.f b{font-size:120px}.tag.f small{color:#a9afc0}
.cal{position:absolute;width:250px;height:270px;border-radius:26px;background:#f3faf7;overflow:hidden;text-align:center;box-shadow:0 30px 80px rgba(0,0,0,.7)}
.cal .h{height:72px;background:#13865f;color:#fff;font:900 38px Inter;letter-spacing:5px;display:flex;align-items:center;justify-content:center}
.cal b{display:block;font:900 150px 'DejaVu Serif',serif;color:#062018;line-height:1.3}
.sc{position:absolute;left:170px;width:740px;display:flex;gap:20px}
.sc .c{flex:1;height:120px;border-radius:28px;display:flex;align-items:center;justify-content:space-between;padding:0 30px;font:800 34px Inter;white-space:nowrap}
.sc .c b{font:900 52px 'DejaVu Serif',serif}
.sc .f{background:#15161c;border:4px solid #3d4150;color:#b8bccb}
.sc .gg{background:#1d150a;border:4px solid #e9b456;color:#ffe9c0}
.left6{position:absolute;left:190px;width:700px;height:150px;border-radius:40px;background:#3a0f12;border:5px solid #ff6b6b;color:#ffe1e1;display:flex;align-items:center;justify-content:center;gap:24px;white-space:nowrap;font:900 50px Inter;letter-spacing:2px}
.left6 b{font:900 100px 'DejaVu Serif',serif;color:#ff8a8a}
.arrow{position:absolute;left:510px;font:900 60px Inter;color:#46e0a8}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'


def card(cls, left, top, rot, label, g=None, fx='pop'):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    return f'<div class="cd {cls}" style="left:{left}px;top:{top}px;transform:rotate({rot}deg)"{a}><div class="k">{label}</div><div class="chip"></div><div class="n">•••• 2026</div></div>'


def notif(top, extra='', g=None, cls='nt'):
    a = f' data-g="{g}" data-fx="pop"' if g else ''
    return f'<div class="{cls}" style="top:{top}px;{extra}"{a}><div class="ic">€</div><div class="tx"><small>VIREMENT REÇU · MAINTENANT</small><span>Prime de parrainage</span><b>+150,00 €</b></div></div>'


DAYS = ''.join(f'<div class="d" data-g="2.0" data-fx="pop"><b>{k + 1}</b>JOUR</div>' for k in range(6))

BODY = hud('FRANCE · RÉSULTAT', 'FORTUNEO') + '''
  <div class="scene" data-s="0"><div class="floor"></div><div class="rays" style="top:520px"></div>''' + hd(250, [('h1', 'PARRAINAGE', None, 'font-size:70px'), ('h1 em', 'FORTUNEO :', None, 'font-size:84px'), ('it gold', '150 € pour toi', None, 'font-size:76px')]) + '''
   ''' + notif(610) + '''
   <div class="stp" style="top:870px" data-g="0.1" data-fx="stamp">PRIME FILLEUL · CARTE GOLD</div>
   <div class="st3" style="top:1030px"><div class="c" data-g="0.0" data-fx="up"><b>1</b>OUVERTURE</div><div class="c" data-g="0.1" data-fx="up"><b>2</b>300 € VERSÉS</div><div class="c" data-g="0.2" data-fx="up"><b>3</b>LA PRIME</div></div></div>
  <div class="scene" data-s="1" data-in="right">''' + hd(230, [('h1 em', '1 : tu ouvres', '1.0', 'font-size:72px'), ('it gold', 'ton premier compte', '1.1', 'font-size:68px'), ('it gold', 'avec la carte Gold', '1.2', 'font-size:68px'), ('it em', 'et mon code parrain.', '1.3', 'font-size:64px')]) + '''
   ''' + card('gld', 370, 640, 5, 'GOLD', '1.2', 'right') + '''
   <div class="fld" style="top:930px" data-g="1.3" data-fx="up"><small>CODE PARRAIN</small><b data-g="1.3" data-fx="type">••••••••</b><i>✓</i></div>
   <div class="ok" style="top:1100px" data-g="1.1" data-fx="pop">✓ 1re ouverture Fortuneo</div></div>
  <div class="scene" data-s="2" data-in="left">''' + hd(230, [('h1 em', '2 : tu verses 300 €', '2.0', 'font-size:66px'), ('it gold', 'dans les 6 jours.', '2.1', 'font-size:74px')]) + '''
   <div class="dep" style="top:470px" data-g="2.0" data-fx="pop"><b>300 €</b><span>SUR TON<br>NOUVEAU COMPTE</span></div>
   <div class="days" style="top:740px">''' + DAYS + '''</div>
   <div class="ok" style="top:930px" data-g="2.1" data-fx="stamp">✓ versement fait à temps</div>
   <div class="arrow" style="top:1040px" data-g="2.1" data-fx="up">↓</div>
   <div class="stp" style="top:1130px" data-g="2.1" data-fx="pop">PRIME DÉBLOQUÉE</div></div>
  <div class="scene" data-s="3" data-in="pop"><div class="rays" style="top:430px"></div>''' + hd(230, [('h1 em', 'RÉSULTAT :', '3.0', 'font-size:76px')]) + '''
   <div class="tag g" style="top:430px" data-g="3.1" data-fx="stamp" data-slow="3.1" data-count="150"><b class="v gold">0 €</b><small>PRIME FILLEUL · GOLD</small></div>
   ''' + hd(720, [('it gold', 'versés au plus tard', '3.2', 'font-size:70px'), ('it em', 'le 31 décembre.', '3.3', 'font-size:70px')]) + '''
   <div class="cal" style="left:180px;top:960px" data-g="3.3" data-fx="stamp"><div class="h">DÉC.</div><b>31</b></div>
   ''' + notif(1010, 'left:460px;width:450px', '3.2', 'nt mini').replace('VIREMENT REÇU · MAINTENANT', 'VIREMENT REÇU').replace('<span>Prime de parrainage</span>', '') + '''</div>
  <div class="scene" data-s="4" data-in="right">''' + hd(230, [('it gold', 'Avec la carte Fosfo,', '4.0', 'font-size:74px'), ('h1', "C'EST 80 €.", '4.1', 'font-size:76px')]) + '''
   ''' + card('fos', 370, 470, -5, 'FOSFO', '4.0', 'left') + '''
   <div class="tag f" style="top:760px" data-g="4.1" data-fx="stamp"><b>80 €</b><small>PRIME FILLEUL · FOSFO</small></div>
   <div class="sc" style="top:1030px" data-g="4.1" data-fx="up"><div class="c f">FOSFO<b>80 €</b></div><div class="c gg">GOLD<b class="gold">150 €</b></div></div></div>
  <div class="scene" data-s="5" data-in="up">''' + hd(230, [('it gold', "Mais l'offre s'arrête", '5.0', 'font-size:72px'), ('h1 em', 'LE 30 NOVEMBRE.', '5.1', 'font-size:70px')]) + '''
   <div class="cal" style="left:415px;top:480px" data-g="5.1" data-fx="stamp"><div class="h">NOV.</div><b>30</b></div>
   <div class="cond" style="top:780px;font-size:28px;color:#9fd9c2" data-g="5.1" data-fx="fade">offre de parrainage du 01/11 au 30/11/2026</div>
   <div class="left6" style="top:870px" data-g="5.2" data-fx="stamp">IL RESTE <b>6</b> JOURS</div>
   ''' + hd(1060, [('it gold', 'Il reste 6 jours.', '5.2', 'font-size:66px')]) + '''</div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', 'font-size:70px'), ('big gold', '« FORTUNEO »', '6.1', 'font-size:84px'), ('it em', 'en privé,', '6.2', 'font-size:70px')]) + '''
   <div class="pill" style="top:620px;border-color:rgba(70,224,168,.85)" data-g="6.3" data-fx="up"><div class="pin" style="background:#46e0a8;color:#04140d">✉</div><div><b>JE T'ENVOIE MON CODE</b><span>code parrain en message privé</span></div></div>
   <div class="search" style="top:750px" data-g="6.3" data-fx="fade">''' + SEARCH + '''<span data-g="6.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:870px;font-size:22px;color:#b5ad9c">Offre soumise aux conditions en vigueur · du 01/11 au 30/11/2026<br>1re ouverture d'un compte Fortuneo avec code parrain · 150 € (carte Gold)<br>ou 80 € (Fosfo) · versement de 300 € dans les 6 jours suivant l'ouverture<br>Prime versée au plus tard le 31/12/2026</div>
   ''' + notif(1060, 'left:290px;width:500px', '6.3', 'nt mini').replace(' · MAINTENANT', '').replace('<span>Prime de parrainage</span>', '') + '''</div>
'''
