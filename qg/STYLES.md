# Catalogue des styles des vidéos QG

Statuts : disponible · à construire · écarté. Mets à jour « dernière utilisation » à chaque vidéo.

## Disponibles (dans le dépôt)
| Code | Nom | Fichiers | Description | Dernière utilisation |
|---|---|---|---|---|
| T | Tuto illustré (personnages blancs) | cfg/tuto.py, base_tuto.css (exemple cfg/hacoo32.py ; QG : cfg/qg_figs.py, cfg/qg_hellobank1.py) | Fond papier blanc, bonhomme dessiné au trait qui bouge, annotations au feutre rouge qui se tracent, surligneur jaune, étapes numérotées (QG du 20/11 : cfg/qg_fortuneo2.py, panneau STOP dessiné + étiquettes « ERREUR N°x ») | 20/11/2026 |
| D | Duo 3D (mannequins blancs) | cfg/duo.py, duo3d.js, base_duo.css (exemple cfg/hacoo30.py) | 2 mannequins 3D blancs qui dialoguent, sous-titres géants, cartes qui surgissent ; a besoin de Three.js : r149 embarqué dans le dépôt depuis le 20/11 (`outils/vendor/three.min.js`, chargé sans réseau). QG du 21/11 : cfg/qg_duel2.py (étiquettes « LE CONNAISSEUR » / « L'INDÉCIS », cartes comparatives `.cmp`, puces de montants `.chips`, carte de fin avec les 2 mots-clés) ; rendu lent (≈ 17 min pour 28 s sur 2 cœurs) | 21/11/2026 |
| V3 | Nuit & or | cfg/luxe.py, base_luxe.css | Fond noir mat, accents dorés, habillage caméra ; utilisé tous les jours par la routine Claude chat, donc max 1 jour sur 3 ici. QG du 21/11 : cfg/qg_revolut2.py (accent vert émeraude, carte « INVITATION · FILLEUL » + tampon, colonnes parrain ✓ / toi ✗, téléphone « TES 5 ÉTAPES » qui se coche) | 21/11/2026 |
| E | Écran d'appli en gros plan | cfg/qg_ecran.py, qg_base_ecran.css, qg_sfx_ecran_template.py (exemple cfg/qg_boursorama1.py) | Bureau clair bleu-gris à points, barre de recherche « parrainage <banque> » avec curseur (mot-clé lisible dès 0 s), gros téléphone dessiné sans logo, doigt qui tape avec ondulation bleue (`hand(x, y, g)`), zoom « punch » sur la case importante (`<div class="zm" data-zg data-zs>`), pastille « ÉTAPE n/4 », gains verts qui surgissent, autocollant jaune « ATTENDS ! » dès la 1re image, sous-titres blancs cerclés de noir ; son plus léger (accords majeurs, clics de tap). Construit le 19/11/2026, mécanique repérée chez @hacooultra14. QG du 20/11 : cfg/qg_monabanq2.py (écran verrouillé + notification « Virement reçu », compteur de paiements, barre de progression, case « MOIS 13 »). | 20/11/2026 |
| D2 | Duo dessiné (personnages blancs, 2D) | cfg/duo2d.py, duo2d.js, base_duo2d.css (exemple cfg/hacoo40.py ; construit par la routine Claude chat le 20/11, à utiliser tel quel ou copié en qg_) | Le dialogue du style D (malin vs pigeon, poses, plans wide / M / P) dessiné au trait sur papier ligné, trait qui « bouille », sous-titres noirs, sans Three.js (rendu bien plus rapide) | — |

## À construire
(aucun pour l'instant)

## Envoyés par Badr
(vide pour l'instant : Badr enverra de futurs styles, à construire en priorité)

## Repérés chez la concurrence
(l'agent ajoute ici au plus 1 style par semaine)
