# Vidéos « QG » : consignes (règles de Badr du 18/11/2026)

Ces vidéos sont fabriquées par la routine « Vidéos QG », à part de la routine Claude chat (qui continue seule avec `videos/`). Elles ne sont ni programmées ni publiées : elles sont livrées à Badr.

## Styles et voix
Varier : 2 styles et 2 voix différents chaque jour, choisis dans qg/STYLES.md et qg/VOIX.md (au moins 1 vidéo sur 2 en « personnages blancs », V3 « nuit & or » au plus 1 jour sur 3).

## Rangement
- Vidéos : `videos-qg/AAAA-MM-JJ/<n>_<sujet>_<format>.mp4` ; légendes : `videos-qg/AAAA-MM-JJ/LEGENDES.md` ; journal : `qg/QUALITE.md`.
- Configs préfixées `qg_`. Ne jamais modifier les fichiers de la routine Claude chat.

## Mot-clé de recherche (priorité n°1)
La Recherche TikTok fait ≈ +65 % de vues sur @htm.invest. Mot-clé : « parrainage <banque> ». Il doit être lisible à l'écran au plus tard à 0,5 s (accroche fixe ou bandeau), dit à l'oral dans les 2 premières secondes, dans le titre TikTok, dans la 1re ligne de la description et en hashtags (#parrainage + #<banque>).

## Formats
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
| F11 | POV / mème | « POV : tu montres le parrainage Hello bank à ton pote » (2 personnages, humour) |
| F12 | Info choc / actu | « Nouvelle condition chez BoursoBank : attention » (une info vérifiée du jour) |
| F13 | Réaction express (10-14 s) | « Arrête-toi : parrainage Hello bank à 150 € » (1 seule idée, rythme très rapide) |

## Comptes d'inspiration (on reprend la mécanique, jamais le texte, les visuels, les sons ni les codes promo)
- @pileinfo.tv : personnages blancs animés (tuto illustré sur fond blanc, duo « le connaisseur vs l'ignorant »), sous-titres géants mot par mot, rythme très rapide, légende très courte.
- @hacooultra14 : tutos éducatifs, « STOP avant de payer » (≈ 161 k vues), « comment ça marche VRAIMENT » (≈ 50 k), anti-arnaque, défi chrono.
- @cryptoboye (parrainage) : POV / mèmes humoristiques, légende ultra courte « lien en bio / DM », beaucoup d'interactions.
- @theo.lesbonstuyaux (parrainage) : réactions express très courtes et enthousiastes (« Arrête-toi là… », « la folie »), une seule offre par vidéo.
- @labanquieredesreseaux (finance) : info choc / actu et pédagogie, ton de confiance.
- @monde_du_parrainage1 (parrainage) : urgence de fin d'offre (« fin demain 10h »), quand la date de fin est vérifiée.

## Contrôle qualité (sous-agent qui n'a pas fabriqué la vidéo)
Vérifie : ffprobe (1080x1920, 18 à 28 s ; F13 : 10 à 14 s) ; images fixes à 0 / 0,5 / 1 / 2 / 3 s puis toutes les 2 s (planche de contact, regardée) ; voix (Speko audio.transcribe, word_timestamps) ; crête audio ≤ -1 dB.
Note /100 : accroche 0-1,5 s (25) · mot-clé (20 : 5 écran, 5 oral, 4 titre, 4 1re ligne, 2 hashtags) · rythme/rétention (20) · clarté offre + appel à l'action (15) · variété (10) · technique (10).
Bloquants : montant non vérifié, mention des conditions absente, texte illisible ou qui déborde, son absent ou saturé, logo, Revolut « illimité » ou prime filleul en argent.
Décision : ≥ 70 et aucun bloquant = OK ; sinon corriger et refaire une fois ; toujours bloquant = livrer avec « ⚠️ À NE PAS PUBLIER ».
