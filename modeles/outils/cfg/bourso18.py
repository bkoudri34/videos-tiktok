import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parraine import *
# BoursoBank, 28/11/2026 (vidéo B, 18:00) - style v3 nuit & or, accent rouge rubis. Format F18 « Parraine à ton tour » (règles de Badr du 26/11) :
# décor nouveau « ville de nuit » (silhouettes d'immeubles, fenêtres dorées allumées, lune) au lieu du sol quadrillé ; mascotte rubis à écharpe dorée
# -> 1 je t'invite en privé (fenêtre de message privé + maillon de lien) -> 2 tu ouvres ton compte (carte des étapes de la prime de bienvenue)
# -> 3 une fois client avec une carte active, ton propre lien (carte bancaire dessinée + bouton) -> 4 tu le partages à tes amis
# (un seul niveau, « montant dans l'appli », « plafond fixé par la banque », ralenti) -> « je ne touche rien sur les amis de mes filleuls »
# (schéma vertical) -> appel à l'action discret. AUCUN montant écrit : montants à l'oral seulement.
# Source (boursobank.com/bon-plan/parrainage-boursobank, consultée le 28/11/2026) : filleul « prime maximale de 300 € » (60 € ouverture,
# jusqu'à 80 € 1er versement, 1 opération carte par mois pendant 3 mois, EasyMove sous 30 jours ; primes reprises si clôture sous 24 mois) ;
# parrain : récompense de l'offre en cours (montant non publié sur la page), limite de 20 primes parrainage sur 12 mois glissants,
# parrain = client détenant notamment une carte active. Pas de total (prime parrain non publiée sur le site officiel).
# Voix : Speko (voix par défaut, speechify simba-3.5), speed 1.08, une synthèse par réplique, atempo 1.15, silences internes plafonnés à 0,2 s, -19 dB moyen.
NAME = 'bourso18'
TITLE = 'BoursoBank parraine a ton tour rubis ville de nuit'
ROOT = ':root{--bg:#07040a;--ac:#ff5d73}'
LINES = [
 ("Parrainage Bourso Bank : un jour, c'est toi qui invites.", [("Parrainage BoursoBank :", None), ("un jour, c'est toi", None), ("qui invites.", None)]),
 ("Un : je t'invite en privé, avec mon lien.", [("1 : je t'invite", None), ("en privé,", None), ("avec mon lien.", None)]),
 ("Deux : tu ouvres ton compte. Jusqu'à trois cents euros de prime de bienvenue, si tu remplis les conditions.", [("2 : tu ouvres ton compte.", None), ("Jusqu'à … de prime de bienvenue,", None), ("si tu remplis les conditions.", None)]),
 ("Trois : une fois client, avec une carte active, tu as ton propre lien.", [("3 : une fois client,", None), ("avec une carte active,", None), ("tu as ton propre lien.", None)]),
 ("Quatre : tu le partages à tes amis. La banque prévoit une prime pour chaque ami, montant dans l'appli, vingt primes au maximum sur douze mois.", [("4 : tu le partages à tes amis.", None), ("Une prime pour chaque ami,", None), ("montant dans l'appli,", None), ("plafond fixé par la banque.", None)]),
 ("Un seul niveau : je ne touche rien sur les amis de mes filleuls.", [("Un seul niveau :", None), ("je ne touche rien", None), ("sur les amis de mes filleuls.", None)]),
 ("Si tu veux que je te parraine, écris-moi en privé.", [("Si tu veux", None), ("que je te parraine,", None), ("écris-moi en privé.", None)]),
]
SPLITS = [(0.2, 2.495), (2.895, 4.826), (5.226, 9.294), (9.694, 12.806), (13.206, 18.607), (19.007, 21.373), (21.773, 23.548)]
MINLEN = 1.6
GAP = 0.28
TAIL = 1.9

CSS = PCSS + '''
.ru{color:#ff5d73;text-shadow:0 0 18px rgba(255,80,110,.5)}
.city{position:absolute;left:0;top:930px;width:1080px;height:520px;pointer-events:none}
.bld{position:absolute;bottom:0;background:linear-gradient(180deg,#151018,#0b080d);border-top:2px solid rgba(240,190,110,.25)}
.win{position:absolute;width:14px;height:18px;border-radius:2px;background:#f3c766;box-shadow:0 0 10px 2px rgba(243,199,102,.45)}
.win.off{background:#2a2228;box-shadow:none}
.moon{position:absolute;width:110px;height:110px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#fff3d6,#e8c88a 70%);box-shadow:0 0 60px 20px rgba(240,200,120,.25)}
.chat{position:absolute;width:560px;border-radius:30px;background:rgba(20,14,20,.95);border:3px solid var(--ac);box-shadow:0 24px 70px rgba(0,0,0,.6);padding:24px 28px;color:#f3efe6}
.chat .t{font:800 26px Inter;color:#cfc8ba;border-bottom:2px solid rgba(255,255,255,.12);padding-bottom:12px;white-space:nowrap}
.chat .b{margin-top:20px;display:inline-block;padding:16px 24px;border-radius:24px 24px 24px 6px;background:var(--ac);color:#140a0c;font:800 32px Inter;white-space:nowrap}
.chain{position:absolute;font:900 34px Inter;color:#f3c766;padding:12px 26px;border-radius:40px;border:3px dashed #f3c766;background:rgba(20,14,8,.85);white-space:nowrap}
.rcard{position:absolute;width:430px;height:268px;border-radius:26px;background:linear-gradient(135deg,#3a0f18,#1a070c 60%,#4a1520);border:3px solid #ff5d73;box-shadow:0 30px 70px rgba(0,0,0,.6);transform:rotate(-6deg)}
.rcard:before{content:'';position:absolute;left:40px;top:82px;width:74px;height:56px;border-radius:10px;background:linear-gradient(135deg,#f3e2b8,#b8955a)}
.rcard b{position:absolute;left:40px;bottom:34px;font:900 28px Inter;color:#ff9aa8;letter-spacing:3px}
.lbtn{position:absolute;padding:20px 36px;border-radius:44px;background:var(--ac);color:#140a0c;font:900 36px Inter;white-space:nowrap;box-shadow:0 0 30px rgba(255,93,115,.45)}
'''
ME = '#ff5d73'


def city(seed=3, dim=False):
    import random
    r = random.Random(seed)
    out = ['<div class="city"' + (' style="opacity:.55"' if dim else '') + '>']
    x = -20
    while x < 1080:
        w = r.choice([110, 130, 150, 170]); h = r.choice([200, 260, 320, 380, 440])
        out.append(f'<div class="bld" style="left:{x}px;width:{w}px;height:{h}px">')
        for yy in range(30, h - 40, 46):
            for xx in range(18, w - 24, 34):
                c = '' if r.random() < 0.42 else ' off'
                out.append(f'<i class="win{c}" style="left:{xx}px;top:{yy}px"></i>')
        out.append('</div>')
        x += w + r.choice([6, 10, 14])
    out.append('</div>')
    return ''.join(out)


MOON = '<div class="moon" style="left:90px;top:600px"></div>'

BODY = hud('PARIS · VILLE DE NUIT', 'BOURSOBANK') + BANNER + '''
  <div class="scene" data-s="0">''' + city(3) + MOON + hdx(230, [('h1 ru', 'PARRAINAGE BOURSOBANK :', None, 'font-size:54px'), ('it gold', "un jour, c'est toi", None, 'font-size:78px'), ('it gold', 'qui invites.', None, 'font-size:78px')]) + mascot(330, 640, 420, ME, 'scarf') + '''
   <div class="bubble2" style="left:640px;top:610px;transform:rotate(5deg)">moi ?</div></div>
  <div class="scene" data-s="1" data-in="left">''' + city(7, True) + '<div class="num" style="left:110px;top:230px" data-g="1.0" data-fx="stamp">1</div>' + hdx(250, [('h1', "JE T'INVITE", '1.0', 'font-size:68px'), ('it ru', 'en privé,', '1.1', 'font-size:70px')], left=280, width=650) + '''
   <div class="chat" style="left:300px;top:560px" data-g="1.1" data-fx="up"><div class="t">Message privé</div><div class="b" data-g="1.2" data-fx="pop">voici mon lien d'invitation</div></div>
   <div class="chain" style="left:400px;top:820px" data-g="1.2" data-fx="stamp">avec mon lien</div>''' + mascot(80, 760, 260, ME, 'scarf') + '''</div>
  <div class="scene" data-s="2" data-in="up">''' + '<div class="num" style="left:465px;top:230px" data-g="2.0" data-fx="stamp">2</div>' + hdx(410, [('h1', 'TU OUVRES TON COMPTE', '2.0', 'font-size:62px')]) + '''
   <div class="card2" style="left:120px;top:560px;width:800px" data-g="2.1" data-fx="up"><div class="t">Prime de bienvenue</div>
    <div class="chk"><i>✓</i>ouverture avec l'invitation</div><div class="chk"><i>✓</i>1er versement</div><div class="chk" data-g="2.2" data-fx="fade"><i>✓</i>carte utilisée chaque mois, 3 mois</div><div class="chk" data-g="2.2" data-fx="fade"><i>✓</i>EasyMove sous 30 jours</div></div>
   <div class="tagp" style="left:250px;top:1150px" data-g="2.2" data-fx="pop">si tu remplis les conditions</div></div>
  <div class="scene" data-s="3" data-in="right">''' + city(11, True) + '<div class="num" style="left:110px;top:230px" data-g="3.0" data-fx="stamp">3</div>' + hdx(250, [('h1', 'UNE FOIS CLIENT,', '3.0', 'font-size:64px'), ('it ru', 'avec une carte active,', '3.1', 'font-size:58px')], left=280, width=650) + '''
   <div class="rcard" style="left:130px;top:560px" data-g="3.1" data-fx="pop"><b>CARTE ACTIVE</b></div>
   <div class="lbtn" style="left:300px;top:930px" data-g="3.2" data-fx="stamp">ton propre lien</div>''' + mascot(640, 600, 260, ME, 'scarf') + '''</div>
  <div class="scene" data-s="4" data-in="pop">''' + city(5, True) + '<div class="num" style="left:110px;top:230px" data-g="4.0" data-fx="stamp">4</div>' + hdx(250, [('h1', 'TU LE PARTAGES', '4.0', 'font-size:62px'), ('it ru', 'à tes amis.', '4.0', 'font-size:66px')], left=280, width=650) + \
    link(540, 640, 230, 820, '4.1') + link(540, 640, 540, 860, '4.1') + link(540, 640, 850, 820, '4.1') + \
    mascot(450, 470, 180, ME, 'scarf') + friend(150, 800, 160, '#f3c766', g='4.1') + friend(460, 840, 160, '#f3c766', g='4.1') + friend(770, 800, 160, '#f3c766', g='4.1') + '''
   <div class="cond" style="top:1030px;color:#e6cfd2;font-size:30px" data-g="4.1" data-fx="fade">une prime pour chaque ami</div>
   <div class="tagp" style="left:200px;top:1100px" data-g="4.2" data-fx="pop">montant dans l'appli</div>
   <div class="tagp" style="left:170px;top:1220px;background:#f3c766" data-g="4.3" data-fx="stamp" data-slow="4.3">plafond fixé par la banque</div></div>
  <div class="scene" data-s="5" data-in="up">''' + city(9, True) + hdx(230, [('h1 ru', 'UN SEUL NIVEAU', '5.0', 'font-size:72px'), ('it gold', 'je ne touche rien sur', '5.1', 'font-size:60px'), ('it gold', 'les amis de mes filleuls.', '5.2', 'font-size:60px')]) + \
    mascot(440, 520, 200, ME, 'scarf') + link(540, 720, 540, 790) + friend(460, 790, 160, '#f3c766') + link(500, 950, 330, 1040, '5.2') + link(580, 950, 750, 1040, '5.2') + friend(250, 1030, 130, '#9a8fae', g='5.2', cls='grey') + friend(700, 1030, 130, '#9a8fae', g='5.2', cls='grey') + '''
   <div class="x" style="left:282px;top:1010px" data-g="5.2" data-fx="stamp">✕</div><div class="x" style="left:732px;top:1010px" data-g="5.2" data-fx="stamp">✕</div>
   <div class="cond" style="top:640px;left:40px;width:360px;color:#e6cfd2;font-size:28px" data-g="5.1" data-fx="fade">toi → tes amis,<br>c'est tout</div></div>
  <div class="scene" data-s="6" data-in="pop">''' + city(3) + MOON + hdx(230, [('h1', 'SI TU VEUX QUE', '6.0', 'font-size:66px'), ('h1', 'JE TE PARRAINE,', '6.1', 'font-size:66px'), ('it ru', 'écris-moi en privé.', '6.2', 'font-size:72px')]) + mascot(360, 640, 340, ME, 'scarf', g='6.2') + '''
   <div class="cond" style="top:1000px;font-size:24px;color:#d8c9c2;background:rgba(8,6,10,.85);border-radius:18px;padding:10px 0">Offres soumises aux conditions en vigueur · 1re ouverture d'un compte<br>individuel via une invitation · primes reprises si clôture sous 24 mois</div></div>
'''
