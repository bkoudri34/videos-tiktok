# videos-tiktok

Vidéos TikTok de @htm.invest et modèles utilisés pour les fabriquer.

- `videos/` : vidéos parrainage (@htm.invest, publiées automatiquement via Metricool)
- `videos-hacoo/` : vidéos Hacoo (compte affiliation, 2 par jour envoyées à Badr, publiées à la main)
- `STYLE.md` : règles de style v2 (accroche, rythme, sous-titres, zones de sécurité) à appliquer à toutes les vidéos
- Format des vidéos finales (MP4 9:16, 60 i/s), nommées `AAAA-MM-JJ_sujet.mp4`. Metricool les récupère par leur lien `raw.githubusercontent.com`.
- `modeles/` : modèles motion design (pages HTML animées image par image), script de rendu et scripts de bruitages.

## Fabrication d'une vidéo

1. Copier un modèle de `modeles/` et adapter textes, montants et timings (`renderAt(t)`).
2. Vérifier en images fixes : `HTMLFILE=modele.html python3 render.py stills <dossier> 1.0 5.0 ...`
3. Rendu en 2 morceaux en parallèle : `HTMLFILE=modele.html python3 render.py video 60 <durée> part0.mp4 0 <n/2>` puis `... part1.mp4 <n/2> <n>`, assemblage avec ffmpeg concat + grain (`noise=c0s=6:c0f=t+u`).
4. Voix off : Speko `audio.synthesize` (fr-FR), une réplique par scène, posée au début de chaque scène, bruitages à 45 %.
5. Déposer le MP4 dans `videos/`, pousser, puis programmer le post dans Metricool (TikTok, contenu commercial activé).

## Règles

- Cadence (règle de Badr du 05/11/2026) : 3 vidéos parrainage par jour sur @htm.invest, publiées automatiquement à 16:00, 18:00 et 21:00 (Europe/Paris), sur 3 sujets consécutifs de la rotation. Chaque vidéo est ajoutée dans son propre commit, dans l'ordre de publication : la rotation repart du fichier le plus récemment ajouté selon git (`git log --diff-filter=A --name-only --format= -- videos/ | head -1`), pas de l'ordre alphabétique.

- Hacoo, cadence (règle de Badr du 07/11/2026) : 2 vidéos Hacoo par jour, nettement différentes entre elles (palette, accroche, articles, prix d'exemple, type d'écrans), enregistrées dans `videos-hacoo/AAAA-MM-JJ_hacoo.mp4` et `videos-hacoo/AAAA-MM-JJ_hacoo-2.mp4`.
- Hacoo (règle de Badr du 03/11/2026) : ne JAMAIS publier ni programmer de vidéo Hacoo sur @htm.invest (ni Metricool, ni `videos/`). Dans la rotation de la tâche quotidienne, le sujet « hacoo » est sauté : après « 3-banques » on revient à « boursorama ». Les vidéos Hacoo vont dans `videos-hacoo/` et sont seulement envoyées à Badr (SendUserFile) ; il les publie lui-même.
- Code Hacoo : toujours `hzklink`, en minuscules, sans espace.
- Montants des offres bancaires : vérifiés en ligne avant chaque vidéo ; pas de logos de marques ; mention « Offre(s) soumise(s) aux conditions en vigueur ».
- Pas de vidéos pour des produits contrefaits.
