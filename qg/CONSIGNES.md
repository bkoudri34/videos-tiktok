# Vidéos « QG » : consignes (règles de Badr du 18/11/2026)

Ces vidéos sont fabriquées par la routine « Vidéos QG », à part de la routine Claude chat (qui continue seule avec `videos/`). Elles ne sont ni programmées ni publiées : elles sont livrées à Badr.

## Rangement
- Vidéos : `videos-qg/AAAA-MM-JJ/<n>_<sujet>_<format>.mp4` ; légendes : `videos-qg/AAAA-MM-JJ/LEGENDES.md` ; journal : `qg/QUALITE.md`.
- Configs préfixées `qg_`. Ne jamais modifier les fichiers de la routine Claude chat.

## Mot-clé de recherche (priorité n°1)
La Recherche TikTok fait ≈ +65 % de vues sur @htm.invest. Mot-clé : « parrainage <banque> ». Il doit être lisible à l'écran au plus tard à 0,5 s (accroche fixe ou bandeau), dit à l'oral dans les 2 premières secondes, dans le titre TikTok, dans la 1re ligne de la description et en hashtags (#parrainage + #<banque>).

## Formats (inspirés de @hacooultra14 et @pileinfo.tv : la mécanique, jamais le texte, les visuels ni les codes)
| Code | Format | Exemple d'accroche (à reformuler) |
|---|---|---|
| F1 | STOP / erreur à éviter | « STOP avant d'ouvrir ton compte Fortuneo » |
| F2 | Démystification | « Comment marche VRAIMENT le parrainage Hello bank » |
| F3 | Anti-arnaque / confiance | « 500 € de prime ? Le vrai maximum, c'est… » |
| F4 | Argent laissé sur la table | « Tu laisses 150 € à Hello bank sans le savoir » |
| F5 | Défi chrono | « Compte ouvert en moins de 5 minutes, chrono » |
| F6 | Le chemin de ta prime | de l'ouverture au virement, étape par étape, avec les délais |
| F7 | Tuto écran 1-2-3 | téléphone illustré, étapes numérotées, sans logo |
| F8 | Résultat d'abord | notification « Virement reçu +80 € » ou solde avant/après dès la 1re image |
| F9 | Duel / comparatif | « Gold ou Fosfo ? », « BoursoBank ou Fortuneo ? » |
| F10 | Le connaisseur vs l'ignorant | 2 personnages qui dialoguent (style Duo 3D) |

## Contrôle qualité (sous-agent qui n'a pas fabriqué la vidéo)
Vérifie : ffprobe (1080x1920, 18 à 26 s) ; images fixes à 0 / 0,5 / 1 / 2 / 3 s puis toutes les 2 s (planche de contact, regardée) ; voix (Speko audio.transcribe, word_timestamps) ; crête audio ≤ -1 dB.
Note /100 : accroche 0-1,5 s (25) · mot-clé (20 : 5 écran, 5 oral, 4 titre, 4 1re ligne, 2 hashtags) · rythme/rétention (20) · clarté offre + appel à l'action (15) · variété (10) · technique (10).
Bloquants : montant non vérifié, mention des conditions absente, texte illisible ou qui déborde, son absent ou saturé, logo, Revolut « illimité » ou prime filleul en argent.
Décision : ≥ 70 et aucun bloquant = OK ; sinon corriger et refaire une fois ; toujours bloquant = livrer avec « ⚠️ À NE PAS PUBLIER ».
