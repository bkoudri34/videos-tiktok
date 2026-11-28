import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
from hacoo_items import icon
# 2e vidéo Hacoo du 28/11/2026 - style V3 nuit & or, accent vert émeraude. Format F5 défi chrono « Code promo appliqué en 10 secondes, chrono »
# (brief veille/briefs/2026-11-28.md, vidéo 2) : chrono doré qui démarre dès la 1re image -> téléphone neutre avec le panier
# (sacoche 19 € + baskets 39 € + casquette 14 € = 72,00 €) -> « Payer » -> zoom sur la case CODE PROMO -> hzklink tapé + Appliquer
# -> ligne -14 % : -10,08 €, 72,00 € barré -> 61,92 € (seul ralenti), chrono figé à 00:09 -> fin « Ton record ? Dis-le en commentaire ».
# Prix d'exemple : 72,00 x 0,14 = 10,08 ; 72,00 x 0,86 = 61,92. Sans sujet R.
# RÈGLE DU 26/11 : le nom de l'appli n'est JAMAIS écrit (ni à l'image ni dans les sous-titres), seulement dit à l'oral.
# Voix : Speko Louis (smallest lightning_v3.1_pro), speed 1.08, une synthèse par réplique, silences internes plafonnés à 0,12 s,
# atempo 1.1, -19 dB moyen. Aucune réplique refaite.
NAME = 'hacoo68'
TITLE = 'Defi chrono code promo emeraude'
ROOT = ':root{--bg:#030806}'
LINES = [
 ("Dix secondes pour payer moins cher sur l'appli Hacou. Top chrono !", [("Dix secondes", None), ("pour payer moins cher", None), ("sur l'appli.", None), ("Top chrono !", None)]),
 ("Ton panier est prêt : tu appuies sur Payer.", [("Ton panier est prêt :", None), ("tu appuies sur Payer.", None)]),
 ("La case code promo, tout de suite.", [("La case code promo,", None), ("tout de suite.", None)]),
 ("Code promo Hacou : H, Z, K, link. Appliquer !", [("Code promo :", None), ("hzklink.", None), ("Appliquer !", None)]),
 ("Moins quatorze pour cent : soixante et un euros et quatre-vingt-douze centimes au lieu de soixante-douze. Neuf secondes !", [("-14 % :", None), ("61,92 €", None), ("au lieu de 72 €.", None), ("9 secondes !", None)]),
 ("Bats mon record en commentaire. Code promo Hacou, H, Z, K, link.", [("Bats mon record", None), ("en commentaire.", None), ("Code promo", None), ("hzklink.", None)]),
]
SPLITS = [(0.2, 2.881), (3.231, 4.872), (5.222, 6.647), (6.997, 10.387), (10.737, 15.738), (16.088, 20.597)]
MINLEN = 1.6
GAP = 0.3
TAIL = 2.2

# chrono « temps de jeu » : 00:00 pendant l'accroche, démarre sur « Top chrono », ne dépasse jamais 9 s, revient à 00:00 pour la boucle
JS = JS + '''
function extra(t){
 const el=document.getElementById('chr'); if(!el) return;
 const K=[[0,0],[2.55,0],[S[1],1.2],[S[2],3.4],[S[3],5.6],[S[3]+2.6,8.1],[S[4]+0.6,9],[1e9,9]];
 let g=0; for(let i=0;i<K.length-1;i++){ if(t>=K[i][0]&&t<K[i+1][0]){const k=(t-K[i][0])/(K[i+1][0]-K[i][0]);g=K[i][1]+(K[i+1][1]-K[i][1])*k;break;} }
 if(t>END-0.45) g=0;
 g=Math.min(g,9);
 el.querySelector('b').textContent='00:0'+Math.floor(g)+'.'+String(Math.floor((g%1)*100)).padStart(2,'0');
 const stop=t>=S[4]+0.6&&t<END-0.45;
 el.classList.toggle('stop',stop);
 el.style.opacity=(stop&&Math.floor(t*3)%2)?0.55:1;
}'''

CSS = '''
#hud .r{display:none}
.em{color:#46e0a6;text-shadow:0 0 18px rgba(50,220,160,.5)}
#chr{position:absolute;left:330px;top:205px;width:420px;height:104px;border-radius:52px;border:4px solid #e0ac55;background:rgba(14,12,8,.85);box-shadow:0 0 40px rgba(240,180,80,.35);display:flex;align-items:center;justify-content:center;gap:18px;z-index:7}
#chr i{font-style:normal;width:22px;height:22px;border-radius:50%;background:#46e0a6;box-shadow:0 0 14px #46e0a6}
#chr b{font:900 64px 'DejaVu Sans Mono',monospace;color:#f3c766;letter-spacing:1px}
#chr.stop{border-color:#46e0a6;box-shadow:0 0 50px rgba(50,220,160,.5)}
#chr.stop i{background:#ff5a5a;box-shadow:0 0 14px #ff5a5a}
.ph{position:absolute;left:250px;width:560px;border-radius:56px;background:#0c0f0d;border:8px solid #2d2a25;box-shadow:0 0 0 2px #4d473d,0 30px 90px rgba(0,0,0,.7);padding:40px 34px 36px;color:#f1ece2}
.ph .tt{font:800 34px Inter;letter-spacing:2px;color:#9fb5aa;text-align:center;margin-bottom:18px}
.row{display:flex;align-items:center;gap:18px;padding:8px 0;border-bottom:2px solid rgba(255,255,255,.08);white-space:nowrap}
.row svg{flex:none;background:#18201c;border-radius:20px}
.row span{font:700 36px Inter;flex:1}
.row b{font:900 40px 'DejaVu Serif',serif}
.sum{display:flex;justify-content:space-between;margin-top:20px;font:800 38px Inter;white-space:nowrap}
.sum b{font:900 46px 'DejaVu Serif',serif;color:#f3c766}
.pay{margin-top:22px;height:96px;border-radius:48px;background:#46e0a6;color:#06140e;font:900 40px Inter;display:flex;align-items:center;justify-content:center;letter-spacing:2px}
.tap{position:absolute;width:120px;height:120px;border-radius:50%;border:6px solid #fff;box-shadow:0 0 30px rgba(255,255,255,.6)}
.tap:after{content:'';position:absolute;left:34px;top:34px;width:40px;height:40px;border-radius:50%;background:#fff}
.cp{position:absolute;left:150px;width:760px;border-radius:40px;background:#f3f0e8;color:#0e1a14;padding:40px 44px;box-shadow:0 30px 90px rgba(0,0,0,.7)}
.cp .lab{font:900 34px Inter;letter-spacing:4px;color:#0f8a5f}
.cp .fr{display:flex;gap:16px;margin-top:16px}
.cp .in{flex:1;height:120px;border-radius:20px;border:5px solid #0f8a5f;box-shadow:0 0 0 8px rgba(15,138,95,.18);background:#fff;display:flex;align-items:center;padding:0 26px;font:900 66px 'DejaVu Sans Mono',monospace;color:#0e1a14;white-space:nowrap}
.cp .ap{height:120px;padding:0 28px;border-radius:20px;background:#0f8a5f;color:#fff;font:900 34px Inter;display:flex;align-items:center}
.cp .ok{margin-top:22px;font:900 40px Inter;color:#0f8a5f;white-space:nowrap}
.caret{display:inline-block;width:6px;height:70px;background:#0f8a5f;margin-left:6px}
.ln{position:absolute;left:150px;width:780px;height:130px;border-radius:30px;background:#0e1a14;border:4px solid #46e0a6;display:flex;align-items:center;justify-content:space-between;padding:0 38px;white-space:nowrap;box-shadow:0 0 40px rgba(50,220,160,.3)}
.ln span{font:800 40px Inter;color:#d6f5e8}.ln b{font:900 62px 'DejaVu Serif',serif;color:#46e0a6}
.old{position:absolute;left:0;width:1080px;text-align:center;font:900 90px 'DejaVu Serif',serif;color:#7d8a83;text-decoration:line-through;text-decoration-color:#ff5a6a;text-decoration-thickness:8px}
.tot{position:absolute;left:0;width:1080px;text-align:center}
.tot .v{font:900 136px 'DejaVu Serif',serif;line-height:1;white-space:nowrap}
.ex{position:absolute;left:0;width:1080px;text-align:center;font:800 26px Inter;letter-spacing:4px;color:#8fa79b}
.card3{position:absolute;left:170px;width:740px;border-radius:36px;background:#f3f0e8;color:#0e1a14;text-align:center;padding:30px 30px 34px;box-shadow:0 30px 80px rgba(0,0,0,.6)}
.card3 .lab{font:900 34px Inter;letter-spacing:5px;color:#0f8a5f}
.card3 .code{font:900 112px 'DejaVu Sans Mono',monospace;line-height:1.1;margin-top:6px}
.card3 .sm{font:800 34px Inter;color:#0e1a14;margin-top:4px}
.strip3{position:absolute;left:150px;width:780px;display:flex;justify-content:space-between;align-items:flex-end}
.strip3 div{width:220px;text-align:center}.strip3 svg{background:#18201c;border-radius:30px}
.strip3 b{display:block;margin-top:8px;font:900 40px 'DejaVu Serif',serif;color:#f1ece2;white-space:nowrap}
.chip{position:absolute;left:150px;width:780px;height:96px;border-radius:48px;background:#0e1a14;border:4px solid #46e0a6;display:flex;align-items:center;justify-content:center;white-space:nowrap;font:800 30px Inter;letter-spacing:3px;color:#d6f5e8}
'''

ITEMS = [('Sacoche', 'Sacoche', '19 €'), ('Baskets', 'Baskets', '39 €'), ('Casquette', 'Casquette', '14 €')]


def phone(top, g=None, pay_g=None):
    rows = ''.join(f'<div class="row">{icon(n, 104)}<span>{lab}</span><b>{p}</b></div>' for n, lab, p in ITEMS)
    a = f' data-g="{pay_g}" data-fx="stamp"' if pay_g else ''
    return f'''<div class="ph" style="top:{top}px"><div class="tt">MON PANIER</div>{rows}
    <div class="sum"><span>Total</span><b>72,00 €</b></div><div class="pay"{a}>PAYER</div></div>'''


def strip(top, g=None):
    a = f' data-g="{g}" data-fx="up"' if g else ''
    return f'<div class="strip3" style="top:{top}px"{a}>' + ''.join(f'<div>{icon(n, 150)}<b>{p}</b></div>' for n, lab, p in ITEMS) + '</div>'


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px;left:90px;width:840px">' + ''.join(out) + '</div>'


BODY = hud('FRANCE · DÉFI CHRONO', 'CODE PROMO') + '''
  <div id="chr"><i></i><b>00:00.00</b></div>
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(345, [('h1', 'CODE PROMO APPLIQUÉ', None, 'font-size:68px'), ('it em', 'en 10 secondes, chrono', None, 'font-size:66px')]) + phone(560) + '''
   <div class="ex" style="top:1290px">PANIER · PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(345, [('h1', 'PANIER PRÊT :', '1.0', 'font-size:68px'), ('it em', 'tu appuies sur Payer.', '1.1', 'font-size:62px')]) + phone(530, pay_g='1.1') + '''
   <div class="tap" style="left:470px;top:1150px" data-g="1.1" data-fx="pop"></div></div>
  <div class="scene" data-s="2" data-in="pop">''' + hd(345, [('h1', 'LA CASE', '2.0', 'font-size:72px'), ('it em', 'code promo, vite !', '2.1', 'font-size:66px')]) + '''
   <div class="cp" style="top:620px" data-g="2.0" data-fx="pop"><div class="lab">CODE PROMO</div><div class="fr"><div class="in"><span class="caret"></span></div><div class="ap">Appliquer</div></div></div>
   <div class="ex" style="top:960px" data-g="2.1" data-fx="fade">AVANT DE VALIDER LA COMMANDE</div>''' + strip(1060, '2.1') + '''</div>
  <div class="scene" data-s="3" data-in="right">''' + hd(345, [('h1', 'CODE PROMO :', '3.0', 'font-size:72px')]) + '''
   <div class="cp" style="top:560px"><div class="lab">CODE PROMO</div><div class="fr"><div class="in"><span data-g="3.1" data-fx="type">hzklink</span></div><div class="ap">Appliquer</div></div>
    <div class="ok" data-g="3.2" data-fx="up">✓ Code appliqué · -14 %</div></div>
   <div class="tap" style="left:720px;top:690px" data-g="3.2" data-fx="pop"></div>
   <div class="ln" style="top:1000px" data-g="3.1" data-fx="up"><span>Total panier</span><b style="color:#f3c766">72,00 €</b></div>
   <div class="ex" style="top:1160px" data-g="3.1" data-fx="fade">PRIX D'EXEMPLE</div></div>
  <div class="scene" data-s="4" data-in="up"><div class="rays" style="top:700px"></div>''' + hd(345, [('big gold', '-14 %', '4.0', 'font-size:120px')]) + '''
   <div class="ln" style="top:530px" data-g="4.0" data-fx="left"><span>Code promo -14 %</span><b>-10,08 €</b></div>
   <div class="old" style="top:720px" data-g="4.2" data-fx="pop">72,00 €</div>
   <div class="tot" style="top:870px" data-g="4.1" data-fx="stamp" data-slow="4.1"><div class="v gold">61,92 €</div></div>
   <div class="ex" style="top:1080px" data-g="4.1" data-fx="fade">AVEC LE CODE PROMO hzklink · PRIX D'EXEMPLE</div>
   ''' + strip(1170, '4.2') + '''<div class="spark" style="left:200px;top:880px" data-g="4.1" data-fx="pop">✦</div><div class="spark" style="left:840px;top:940px" data-g="4.2" data-fx="pop">✦</div><div class="spark" style="left:260px;top:1010px" data-g="4.3" data-fx="pop">✦</div></div>
  <div class="scene" data-s="5" data-in="pop"><div class="floor"></div>''' + hd(345, [('h1', 'TON RECORD ?', '5.0', 'font-size:76px'), ('it em', 'dis-le en commentaire', '5.1', 'font-size:62px')]) + '''
   <div class="card3" style="top:570px" data-g="5.0" data-fx="stamp"><div class="lab">CODE PROMO</div><div class="code">hzklink</div><div class="sm">-14 % avec le code hzklink</div></div>
   <div class="chip" style="top:930px" data-g="5.1" data-fx="up">LIENS DES ARTICLES TENDANCE EN BIO</div>
   <div class="cond" style="top:1060px">Prix d'exemple · -14 % avec le code promo hzklink<br>Offre soumise aux conditions en vigueur</div></div>
'''
