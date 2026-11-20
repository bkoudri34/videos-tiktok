import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from luxe import *
# Revolut, 20/11/2026 21:00 - style v3 nuit & or, accent bleu électrique. Format F7 « tuto écran 1-2-3 » :
# téléphone illustré (sans logo) avec les 3 étapes dès la 1re image -> 1 lien de parrainage avant l'inscription -> 2 compte + identité
# -> 3 étapes de l'invitation dans les délais -> 0 € en argent pour le filleul (ralenti) -> parrain récompensé selon l'offre de l'appli -> appel à l'action.
# Aucun montant : pas de prime en argent pour le filleul ; récompense du parrain indiquée dans l'invitation de l'appli
# (revolut.com/fr-FR/legal/referrals-terms consulté le 20/11/2026 ; selectra.info et comparabanques.fr 16/11/2026 : le filleul ne touche pas de prime).
# Voix : Speko (speechify simba-3.5, voix par défaut), speed 1.08.
NAME = 'revolut13'
TITLE = 'Revolut tuto bleu electrique'
ROOT = ':root{--bg:#06070c}'
LINES = [
 ("Parrainage Revolut : le tuto en trois étapes.", [("Parrainage Revolut :", None), ("le tuto", None), ("en 3 étapes.", None)]),
 ("Un : tu cliques sur un lien de parrainage, avant de t'inscrire.", [("1 : tu cliques", None), ("sur un lien de parrainage,", None), ("avant de t'inscrire.", None)]),
 ("Deux : tu ouvres ton compte et tu vérifies ton identité.", [("2 : tu ouvres ton compte", None), ("et tu vérifies", None), ("ton identité.", None)]),
 ("Trois : tu suis les étapes de l'invitation, dans les délais.", [("3 : tu suis les étapes", None), ("de l'invitation,", None), ("dans les délais.", None)]),
 ("À savoir : pas de prime en argent pour le filleul.", [("À savoir :", None), ("pas de prime en argent", None), ("pour le filleul.", None)]),
 ("C'est le parrain qui est récompensé, selon l'offre affichée dans l'appli.", [("C'est le parrain", None), ("qui est récompensé,", None), ("selon l'offre affichée", None), ("dans l'appli.", None)]),
 ("Envoie-moi REVOLUT en privé, je t'envoie mon lien.", [("Envoie-moi", None), ("REVOLUT", None), ("en privé,", None), ("je t'envoie mon lien.", None)]),
]
SPLITS = [(0.0, 2.32), (2.73, 4.91), (5.5, 8.14), (9.01, 11.43), (12.0, 13.87), (14.34, 16.6), (17.08, 18.95)]
MINLEN = 1.9
GAP = 0.3
TAIL = 2.0


def hd(top, items):
    out = []
    for cls, txt, g, st in items:
        a = f' data-g="{g}" data-fx="tw"' if g else ''
        s = f' style="{st}"' if st else ''
        out.append(f'<div class="{cls}"{s}{a}>{txt}</div>')
    return f'<div class="hd" style="top:{top}px">' + ''.join(out) + '</div>'


CSS = '''
.bl{color:#9aa6ff;text-shadow:0 0 18px rgba(110,125,255,.55)}
.ph{position:absolute;left:300px;top:640px;width:480px;height:860px;background:#0b0c14;border:10px solid #262838;border-radius:64px;box-shadow:0 0 0 2px #4a4d66,0 30px 90px rgba(0,0,0,.75);overflow:hidden;color:#fff}
.ph .notch{width:150px;height:34px;background:#000;border-radius:0 0 20px 20px;margin:0 auto}
.ph .tt{margin:40px 36px 20px;font:900 40px Inter;color:#eef0ff;white-space:nowrap}
.ph .row{margin:0 26px 20px;height:120px;border-radius:26px;background:#171a2b;display:flex;align-items:center;gap:16px;padding:0 18px;font:800 26px Inter;overflow:hidden;color:#dfe3ff;white-space:nowrap}
.ph .row .n{flex:none;width:70px;height:70px;border-radius:50%;background:#5b6cff;color:#fff;font:900 36px Inter;display:flex;align-items:center;justify-content:center}
.ph .row small{display:block;font:600 22px Inter;color:#8f96c2;margin-top:4px}
.ph .msg{margin:30px 30px 0;border-radius:30px 30px 30px 8px;background:#e9ebff;color:#14162a;padding:26px;font:600 28px Inter;line-height:1.35}
.ph .msg u{display:block;margin-top:12px;color:#3346e0;font:700 27px 'DejaVu Sans Mono',monospace;white-space:nowrap;text-decoration:underline}
.ph .bt{margin:40px auto 0;width:380px;height:100px;border-radius:50px;background:#5b6cff;color:#fff;font:900 36px Inter;display:flex;align-items:center;justify-content:center;white-space:nowrap}
.tap{position:absolute;width:120px;height:120px;border-radius:50%;border:8px solid rgba(255,255,255,.9);box-shadow:0 0 30px rgba(140,155,255,.8)}
.badge{position:absolute;left:110px;top:700px;width:170px;height:170px;border-radius:50%;background:linear-gradient(135deg,#fff1c4,#e9b456 50%,#a8701f);color:#2a1a05;font:900 110px 'DejaVu Serif',serif;display:flex;align-items:center;justify-content:center;box-shadow:0 20px 60px rgba(0,0,0,.6),0 0 40px rgba(240,180,80,.35)}
.idc{margin:50px auto 0;width:400px;height:250px;border-radius:24px;background:#e9ebff;position:relative}
.idc .pic{position:absolute;left:30px;top:40px;width:120px;height:150px;border-radius:16px;background:#a9b1e8}
.idc .pic:after{content:'';position:absolute;left:35px;top:24px;width:50px;height:50px;border-radius:50%;background:#6c76c4}
.idc i{position:absolute;left:180px;height:18px;border-radius:9px;background:#b7bde6}
.scan{position:absolute;left:30px;top:120px;width:400px;height:6px;background:#5b6cff;box-shadow:0 0 20px #5b6cff}
.ok{margin:40px auto 0;width:380px;height:90px;border-radius:45px;background:#1fbf75;color:#fff;font:900 32px Inter;display:flex;align-items:center;justify-content:center;white-space:nowrap}
.ex{display:block;margin:6px 36px 0;font:700 20px Inter;color:#8f96c2;letter-spacing:2px}
.zero{position:absolute;left:0;width:1080px;text-align:center}
.zero .v{font:900 260px 'DejaVu Serif',serif;line-height:1}
.zero .x{position:absolute;left:330px;top:120px;width:420px;height:22px;background:#ff4d5e;border-radius:11px;transform:rotate(-12deg);box-shadow:0 0 30px rgba(255,77,94,.6)}
.tag{position:absolute;left:150px;width:780px;height:120px;border-radius:30px;background:#f2f3ff;color:#1a1d3a;display:flex;align-items:center;justify-content:center;font:900 36px Inter;white-space:nowrap;box-shadow:0 0 0 5px #5b6cff}
.gift{position:absolute;left:390px;top:700px;width:300px;height:300px}
.gift .bx{position:absolute;left:20px;top:110px;width:260px;height:190px;border-radius:16px;background:linear-gradient(135deg,#7d8cff,#3443c9)}
.gift .lid{position:absolute;left:0;top:60px;width:300px;height:70px;border-radius:14px;background:linear-gradient(135deg,#a3adff,#5b6cff)}
.gift .rb{position:absolute;left:130px;top:60px;width:40px;height:240px;background:linear-gradient(#fff1c4,#e9b456)}
.gift .bw{position:absolute;left:90px;top:0;width:120px;height:70px;border:16px solid #e9b456;border-radius:50% 50% 10px 10px}
.app{position:absolute;left:190px;width:700px;height:150px;border-radius:36px;background:#171a2b;border:4px solid #5b6cff;display:flex;align-items:center;gap:26px;padding:0 34px;white-space:nowrap}
.app .ic{flex:none;width:86px;height:86px;border-radius:22px;background:#5b6cff;display:flex;align-items:center;justify-content:center}
.app b{display:block;font:900 36px Inter;color:#eef0ff}
.app span{font:600 28px Inter;color:#9aa0c8}
'''
SEARCH = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="17" cy="17" r="11" stroke="#111" stroke-width="4" fill="none"/><line x1="25" y1="25" x2="35" y2="35" stroke="#111" stroke-width="4"/></svg>'
BELL = '<svg width="50" height="50" viewBox="0 0 50 50"><path d="M25 6c-8 0-13 6-13 14v9l-5 7h36l-5-7v-9c0-8-5-14-13-14z" fill="#fff"/><circle cx="25" cy="42" r="5" fill="#fff"/></svg>'


def row(n, t, s, g=None, fx='left'):
    a = f' data-g="{g}" data-fx="{fx}"' if g else ''
    return f'<div class="row"{a}><div class="n">{n}</div><div>{t}<small>{s}</small></div></div>'


BODY = hud('FRANCE · TUTO', 'REVOLUT') + '''
  <div class="scene" data-s="0"><div class="floor"></div>''' + hd(215, [('h1 bl', 'PARRAINAGE REVOLUT :', None, 'font-size:62px'), ('it gold', 'le tuto', None, 'font-size:84px'), ('big gold', 'en 3 étapes.', None, 'font-size:104px')]) + '''
   <div class="ph" style="top:640px"><div class="notch"></div><div class="tt">Mon parrainage</div>''' + row(1, 'Lien de parrainage', "avant l'inscription") + row(2, 'Compte + identité', 'vérification') + row(3, "Suivre l'invitation", 'dans les délais') + '''</div></div>
  <div class="scene" data-s="1" data-in="up">''' + hd(215, [('h1 bl', '1 : TU CLIQUES', '1.0', 'font-size:66px'), ('it gold', 'sur un lien de parrainage,', '1.1', 'font-size:64px'), ('it gold', "avant de t'inscrire.", '1.2', 'font-size:64px')]) + '''
   <div class="ph" style="top:660px"><div class="notch"></div><div class="tt">Messages</div><div class="msg" data-g="1.0" data-fx="pop">Voilà mon lien de parrainage :<u>lien-de-parrainage</u></div><div class="bt" data-g="1.2" data-fx="stamp">S'inscrire</div></div>
   <div class="tap" style="left:580px;top:1010px" data-g="1.1" data-fx="pop"></div>
   <div class="badge" style="top:1180px;left:90px" data-g="1.0" data-fx="stamp">1</div></div>
  <div class="scene" data-s="2" data-in="right">''' + hd(215, [('h1 bl', '2 : TU OUVRES TON COMPTE', '2.0', 'font-size:58px'), ('it gold', 'et tu vérifies', '2.1', 'font-size:70px'), ('it gold', 'ton identité.', '2.2', 'font-size:70px')]) + '''
   <div class="ph" style="top:660px"><div class="notch"></div><div class="tt">Identité</div><div class="idc" data-g="2.1" data-fx="pop"><div class="pic"></div><i style="top:60px;width:180px"></i><i style="top:100px;width:140px"></i><i style="top:140px;width:170px"></i><div class="scan" style="left:0;top:120px" data-g="2.1" data-fx="grow"></div></div><div class="ok" data-g="2.2" data-fx="stamp">✓ IDENTITÉ VÉRIFIÉE</div></div>
   <div class="badge" style="top:1180px;left:90px" data-g="2.0" data-fx="stamp">2</div></div>
  <div class="scene" data-s="3" data-in="left">''' + hd(215, [('h1 bl', '3 : TU SUIS LES ÉTAPES', '3.0', 'font-size:60px'), ('it gold', "de l'invitation,", '3.1', 'font-size:70px'), ('it gold', 'dans les délais.', '3.2', 'font-size:70px')]) + '''
   <div class="ph" style="top:660px"><div class="notch"></div><div class="tt">Ton invitation</div><span class="ex">EXEMPLE D'ÉTAPES</span>''' + row('✓', 'Activer la carte', "selon l'invitation", '3.1') + row('✓', 'Payer par carte', "selon l'invitation", '3.1', 'right') + row('⏱', 'Respecter le délai', "indiqué dans l'appli", '3.2') + '''</div>
   <div class="badge" style="top:1180px;left:90px" data-g="3.0" data-fx="stamp">3</div></div>
  <div class="scene" data-s="4" data-in="pop"><div class="rays" style="top:640px"></div>''' + hd(215, [('h1 bl', 'À SAVOIR :', '4.0', ''), ('it gold', 'pas de prime en argent', '4.1', 'font-size:70px'), ('it gold', 'pour le filleul.', '4.2', 'font-size:70px')]) + '''
   <div class="zero" style="top:720px" data-g="4.1" data-fx="stamp" data-slow="4.1"><div class="v gold">0 €</div><div class="x" data-g="4.2" data-fx="grow"></div></div>
   <div class="tag" style="top:1060px" data-g="4.2" data-fx="pop">FILLEUL : PAS DE PRIME EN ARGENT</div></div>
  <div class="scene" data-s="5" data-in="right">''' + hd(215, [('h1 bl', "C'EST LE PARRAIN", '5.0', 'font-size:66px'), ('it gold', 'qui est récompensé,', '5.1', 'font-size:70px')]) + '''
   <div class="gift" style="top:620px" data-g="5.1" data-fx="pop"><div class="bx"></div><div class="lid"></div><div class="rb"></div><div class="bw"></div></div>
   <div class="app" style="top:1000px" data-g="5.2" data-fx="up"><div class="ic">''' + BELL + '''</div><div><b>selon l'offre affichée</b><span>dans l'appli, au moment de l'invitation</span></div></div>
   <div class="tag" style="top:1200px" data-g="5.3" data-fx="pop">DANS L'APPLI</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + hd(230, [('h1', 'ENVOIE-MOI', '6.0', ''), ('big gold', '« REVOLUT »', '6.1', 'font-size:110px'), ('it gold', 'en privé,', '6.2', '')]) + '''
   <div class="pill" style="top:760px;border-color:rgba(110,125,255,.85)" data-g="6.3" data-fx="up"><div class="pin" style="background:#5b6cff;color:#fff">✉</div><div><b>JE T'ENVOIE MON LIEN</b><span>directement en message privé</span></div></div>
   <div class="search" style="top:900px" data-g="6.3" data-fx="fade">''' + SEARCH + '''<span data-g="6.3" data-fx="type">@htm.invest</span></div>
   <div class="cond" style="top:1040px;font-size:23px">Offre soumise aux conditions en vigueur · pas de prime en argent pour le filleul<br>étapes et délais indiqués dans l'invitation de l'appli<br>récompense du parrain selon l'offre en cours · écrans d'illustration</div></div>
'''
