# videos-tiktok

Vidéos TikTok de @htm.invest et modèles utilisés pour les fabriquer.

- `videos/` : vidéos finales (MP4 9:16, 60 i/s), nommées `AAAA-MM-JJ_sujet.mp4`. Metricool les récupère par leur lien `raw.githubusercontent.com`.
- `modeles/` : modèles motion design (pages HTML animées image par image), script de rendu et scripts de bruitages.

## Fabrication d'une vidéo

1. Copier un modèle de `modeles/` et adapter textes, montants et timings (`renderAt(t)`).
2. Vérifier en images fixes : `HTMLFILE=modele.html python3 render.py stills <dossier> 1.0 5.0 ...`
3. Rendu en 2 morceaux en parallèle : `HTMLFILE=modele.html python3 render.py video 60 <durée> part0.mp4 0 <n/2>` puis `... part1.mp4 <n/2> <n>`, assemblage avec ffmpeg concat + grain (`noise=c0s=6:c0f=t+u`).
4. Voix off : Speko `audio.synthesize` (fr-FR), une réplique par scène, posée au début de chaque scène, bruitages à 45 %.
5. Déposer le MP4 dans `videos/`, pousser, puis programmer le post dans Metricool (TikTok, contenu commercial activé).

## Règles

- Code Hacoo : toujours `hzklink`, en minuscules, sans espace.
- Montants des offres bancaires : vérifiés en ligne avant chaque vidéo ; pas de logos de marques ; mention « Offre(s) soumise(s) aux conditions en vigueur ».
- Pas de vidéos pour des produits contrefaits.
