import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qg_ecran import *
# Vidéos QG du 25/11/2026, vidéo 2 : Monabanq. Style E « écran d'appli en gros plan ».
# Format F17 « Problème / solution (FAQ) » (1re F17) : « je suis déjà client, je peux être parrainé ? » -> réponse tirée des
# conditions officielles (non : ni client, ni ancien client ; compte joint exclu si un co-titulaire est déjà client) -> jamais
# client : jusqu'à 280 € si conditions remplies -> garder le compte 1 an -> question à commenter -> appel à l'action -> mentions.
# Aucun conseil pour contourner la banque : renvoi vers le service client et les conditions officielles.
# Source : https://www.monabanq.com/fr/parrainage.html (consultée le 25/11/2026) : parrainage effectif pour toute 1re ouverture
# définitive d'un compte courant Pratiq+, Uniq ou Uniq+ ; « Les filleuls doivent être majeurs, résider en France, ne pas être client
# de Monabanq, ancien client ou collaborateur de Monabanq » ; offre de bienvenue (depuis le 01/07/2026) réservée aux personnes
# majeures n'ayant jamais détenu de compte courant Monabanq, non applicable au compte joint si l'un des co-titulaires est déjà client ;
# jusqu'à 280 € = 20 € à l'ouverture + 60 € (300 € versés dans le mois) + 60 € (carte Visa, 30 paiements en 2 mois) + 80 € (mobilité
# bancaire signée dans le mois) + 60 € de fidélité au 13e mois (compte conservé + 2 autres produits dont 1 épargne) ; primes reprises
# si clôture à l'initiative du client dans les 12 mois.
# Voix : Manon (cartesia sonic-3.5, speed 1.15), une synthèse par réplique, +5 dB, atempo 1.07, pauses internes ramenées à 0,22 s.
NAME = 'qg_monabanq5'
TITLE = 'QG Monabanq FAQ deja client'
GAP = 0.28
TAIL = 1.2
MINLEN = 1.5
LINES = [
 ("Parrainage Monabanque : je suis déjà client, je peux être parrainé ?",
  [("<em>Parrainage Monabanq</em> :", None), ("je suis déjà client,", None), ("je peux être parrainé ?", None)]),
 ("Non : le filleul ne doit être ni client, ni ancien client.",
  [("<i>Non</i> :", None), ("le filleul ne doit être", None), ("ni <i>client</i>,", None), ("ni <i>ancien client</i>.", None)]),
 ("Un compte joint ? Pas d'offre si l'un des deux est déjà client.",
  [("Un <em>compte joint</em> ?", None), ("Pas d'offre si l'un des deux", None), ("est <i>déjà client</i>.", None)]),
 ("Jamais été client ? Alors c'est jusqu'à 280 €, si tu remplis les conditions.",
  [("<em>Jamais été client</em> ?", None), ("Alors c'est jusqu'à <em>280 €</em>,", None), ("si tu remplis les conditions.", None)]),
 ("Et garde ton compte au moins un an.", [("Et garde ton compte", None), ("au moins <em>1 an</em>.", None)]),
 ("Et toi, c'est quoi ta question sur le parrainage ? Écris-la en commentaire.",
  [("Et toi, c'est quoi ta question", None), ("sur le parrainage ?", None), ("<em>Écris-la en commentaire</em>", None)]),
 ("Et envoie-moi le mot Monabanque, en message privé.", [("Et envoie-moi le mot <em>MONABANQ</em>,", None), ("en message privé.", None)]),
]
SPLITS = [(0.0, 3.208), (3.708, 7.277), (7.777, 10.919), (11.419, 16.261), (16.761, 18.914), (19.414, 23.304), (23.804, 26.655)]

CSS = '''
#sub{left:60px;width:840px;font-size:60px;-webkit-text-stroke:0;text-shadow:5px 0 0 #0f172a,-5px 0 0 #0f172a,0 5px 0 #0f172a,0 -5px 0 #0f172a,4px 4px 0 #0f172a,-4px 4px 0 #0f172a,4px -4px 0 #0f172a,-4px -4px 0 #0f172a,0 9px 0 #0f172a}
.ex{position:absolute;padding:6px 18px;border-radius:12px;background:#0f172a;color:#fff;font:800 26px Inter;letter-spacing:1px;z-index:7;white-space:nowrap}
.ap .r5 span sup{font-size:60%}
.faqh{font:900 46px Inter;margin-bottom:24px}
.qb{border-radius:30px;background:#eff6ff;border:4px solid #2563eb;padding:24px 26px;font:800 40px/1.2 Inter;white-space:normal}
.qb small{display:block;font:700 26px Inter;color:#64748b;margin-bottom:8px}
.qrow{height:92px;border-radius:24px;background:#f1f5f9;margin:16px 0;display:flex;align-items:center;padding:0 24px;font:700 30px Inter;color:#64748b;white-space:nowrap}
.doc .l{font:700 30px/1.35 Inter;color:#475569;margin:10px 0}
.doc .hlr{border-radius:22px;background:#fee2e2;border:4px solid #dc2626;padding:20px 22px;font:900 38px/1.2 Inter;color:#0f172a;margin:18px 0}
.doc .hlr b{color:#dc2626}
.xbig{position:absolute;font:900 190px/1 Inter;color:#dc2626;-webkit-text-stroke:8px #0f172a;paint-order:stroke fill;z-index:7}
.av{display:flex;gap:30px;justify-content:center;margin-top:30px}
.av .p{width:240px;text-align:center;font:800 30px Inter;color:#475569}
.av .p i{display:block;width:170px;height:170px;margin:0 auto 14px;border-radius:50%;background:#cbd5e1;position:relative}
.av .p i:after{content:'';position:absolute;left:50px;top:30px;width:70px;height:70px;border-radius:50%;background:#94a3b8}
.av .p.c i{background:#fecaca}.av .p.c i:after{background:#f87171}
.av .p b{display:block;color:#dc2626;font:900 30px Inter;margin-top:6px}
.offx{margin-top:40px;border-radius:24px;border:4px solid #dc2626;color:#dc2626;font:900 42px Inter;text-align:center;padding:22px}
.ap .r5{display:flex;justify-content:space-between;align-items:center;height:84px;border-bottom:3px solid #eef2f7;font:800 34px Inter;white-space:nowrap}
.ap .r5 b{color:#16a34a;font:900 38px Inter}
.ap .tt5{display:flex;justify-content:space-between;align-items:center;margin-top:18px;font:900 50px Inter;white-space:nowrap}
.ap .tt5 b{background:#ffd43b;padding:0 14px;border-radius:12px}
.small{position:absolute;padding:10px 22px;border-radius:16px;background:#fff;border:4px solid #0f172a;font:800 32px Inter;white-space:nowrap;z-index:7}
.calm{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:20px}
.calm i{height:96px;border-radius:18px;background:#e2e8f0;font:800 28px/96px Inter;font-style:normal;text-align:center;color:#475569}
.calm i.on{background:#16a34a;color:#fff}
.cond{font:700 27px/1.35 Inter}
.cm{position:absolute;left:80px;top:430px;width:780px;border-radius:44px;background:#fff;border:5px solid #0f172a;box-shadow:12px 12px 0 #0f172a;padding:34px 34px 30px;z-index:7}
.cm .h{font:900 40px Inter;display:flex;align-items:center;gap:16px}
.cm .h span{font:900 34px Inter;color:#64748b;margin-left:auto}
.cm .c{display:flex;gap:18px;align-items:flex-start;margin-top:26px}
.cm .c i{width:76px;height:76px;border-radius:50%;background:#cbd5e1;flex:none}
.cm .c div{font:800 34px/1.3 Inter;color:#0f172a}
.cm .c div small{display:block;font:700 24px Inter;color:#64748b}
.cm .f{margin-top:30px;height:96px;border-radius:48px;background:#f1f5f9;border:4px solid #2563eb;display:flex;align-items:center;padding:0 30px;font:800 34px Inter;color:#64748b;white-space:nowrap}
'''

BODY = search('parrainage monabanq') + '''
  <div class="scene" data-s="0">
   <div class="zm" data-zg="0.1" data-zs="1.1" style="transform-origin:470px 760px">''' + phone('''<div class="faqh">Questions fréquentes</div>
     <div class="qb"><small>Ta question</small><span data-g="0.0" data-fx="type">Je suis déjà client…</span><br><span data-g="0.1" data-fx="type">je peux être parrainé ?</span></div>
     <div class="qrow">Combien de temps garder le compte ?</div><div class="qrow">Compte joint ?</div><div class="qrow">Quand arrive la prime ?</div>''') + '''</div>
   <div class="stk" style="left:640px;top:318px;transform:rotate(5deg)" data-g="0.0" data-fx="stamp">FAQ</div></div>
  <div class="scene" data-s="1" data-in="right">''' + step(1, 3, 'DÉJÀ CLIENT') + '''
   <div class="zm" data-zg="1.2" data-zs="1.12" style="transform-origin:470px 820px">''' + phone('''<div class="hd"><span class="bk">‹</span>Conditions</div><div class="doc">
     <div class="l">Parrainage effectif : 1<sup>re</sup> ouverture d'un compte courant Pratiq+, Uniq ou Uniq+.</div>
     <div class="hlr">Le filleul ne doit <b>pas</b> être client, <b>ni ancien client</b> de Monabanq.</div>
     <div class="l">Offre applicable une seule fois.</div></div>''') + '''</div>
   <div class="xbig" style="left:330px;top:1080px;font-size:160px;transform:rotate(-8deg)" data-g="1.0" data-fx="stamp">NON</div>
   <div class="ex" style="left:150px;top:1290px">source : monabanq.com, 25/11/2026</div></div>
  <div class="scene" data-s="2" data-in="right">''' + step(2, 3, 'COMPTE JOINT') + '''
   <div class="zm" data-zg="2.1" data-zs="1.08" style="transform-origin:470px 800px">''' + phone('''<div class="hd"><span class="bk">‹</span>Compte joint</div>
     <div class="av"><div class="p"><i></i>Toi<b>nouveau</b></div><div class="p c"><i></i>L'autre titulaire<b data-g="2.1" data-fx="pop">déjà client</b></div></div>
     <div class="offx" data-g="2.2" data-fx="stamp">✗ pas d'offre de bienvenue</div>''') + '''</div></div>
  <div class="scene" data-s="3" data-in="up">''' + step(3, 3, 'JAMAIS CLIENT') + '''
   <div class="zm" data-zg="3.1" data-zs="1.06" style="transform-origin:470px 1000px">''' + phone('''<div class="hd">Offre de bienvenue</div>''' +
    ''.join(f'<div class="r5" data-g="3.{1 if k < 3 else 2}" data-fx="left"><span>{l}</span><b>{v}</b></div>' for k, (l, v) in enumerate([('Ouverture', '20 €'), ('300 € versés (1 mois)', '60 €'), ('30 paiements carte', '60 €'), ('Mobilité bancaire', '80 €'), ('13<sup>e</sup> mois (fidélité)', '60 €')])) +
    '''<div class="tt5" data-g="3.1" data-fx="pop">Jusqu'à<b>280 €</b></div>''') + '''</div>
   <div class="gain" style="left:500px;top:440px;font-size:46px;transform:rotate(3deg)" data-g="3.0" data-fx="stamp">✓ jamais client</div>
   <div class="small" style="left:300px;top:1240px" data-g="3.2" data-fx="pop">prime si conditions remplies</div></div>
  <div class="scene" data-s="4" data-in="right">
   <div class="zm" data-zg="4.1" data-zs="1.08" style="transform-origin:470px 800px">''' + phone('''<div class="hd"><span class="bk">‹</span>Mon compte</div>
     <div class="lb">Garde-le au moins 12 mois</div><div class="calm">''' + ''.join(f'<i data-g="4.{0 if k < 6 else 1}" data-fx="pop" class="on">{k + 1}</i>' for k in range(12)) + '''</div>
     <div class="lb" style="margin-top:30px">Clôture dans les 12 mois : primes reprises</div>''') + '''</div>
   <div class="stk" style="left:420px;top:420px;transform:rotate(4deg)" data-g="4.1" data-fx="stamp">1 an minimum</div>
   <div class="small" style="left:110px;top:1240px" data-g="4.1" data-fx="pop">Un doute ? Service client + conditions</div></div>
  <div class="scene" data-s="5" data-in="pop">
   <div class="cm" data-g="5.0" data-fx="up"><div class="h">💬 Commentaires<span>×</span></div>
    <div class="c"><i></i><div><small>toi</small><span data-g="5.1" data-fx="type">Ma question : …</span></div></div>
    <div class="f" data-g="5.2" data-fx="tick">Écris ta question ici…</div></div>
   <div class="stk" style="left:110px;top:1060px;font-size:46px;transform:rotate(-3deg)" data-g="5.2" data-fx="stamp">ÉCRIS-LA EN COMMENTAIRE 👇</div>
   <div class="small" style="left:110px;top:900px" data-g="5.1" data-fx="left">déjà client ?</div><div class="small" style="left:370px;top:930px" data-g="5.1" data-fx="up">combien de temps ?</div><div class="small" style="left:300px;top:810px;transform:rotate(-2deg)" data-g="5.0" data-fx="pop">quand arrive la prime ?</div></div>
  <div class="scene" data-s="6" data-in="pop">
   <div class="endc" data-g="6.0" data-fx="up"><div class="k">ENVOIE-MOI EN PRIVÉ</div><div class="c">« MONABANQ »</div><div class="d">je t'envoie le lien</div><div class="b">@htm.invest</div></div>
   <div class="cond" style="top:800px" data-g="6.0" data-fx="fade">Offre soumise aux conditions en vigueur.<br>Conditions consultées le 25/11/2026 sur monabanq.com : le filleul ne doit pas être client, ancien client ou collaborateur de Monabanq ; compte joint exclu si un co-titulaire est déjà client. Offre de bienvenue (1<sup>er</sup> compte courant, depuis le 01/07/2026) jusqu'à 280 € : 20 € à l'ouverture + 60 € (300 € versés dans le mois) + 60 € (carte Visa, 30 paiements en 2 mois) + 80 € (mobilité bancaire) + 60 € au 13<sup>e</sup> mois (compte conservé + 2 autres produits dont 1 d'épargne). Primes reprises si clôture sous 12 mois.<br>Lien de parrainage : je touche une prime.</div></div>
'''
