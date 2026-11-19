# Catalogue des voix Hacoo (tâche « 2 vidéos Hacoo en plus », vidéos 3 et 4)

Règle de Badr du 18/11/2026 : varier les voix d'un jour à l'autre. Chaque vidéo prend une voix que cette tâche n'a pas utilisée les 2 jours précédents ; style D : deux voix bien distinctes.

Synthèse : `audio.synthesize` (Speko), `voice` = identifiant ci-dessous, `constraints.allowedProviders.tts = [fournisseur]`,
`intent {language:"fr", region:"FR", optimizeFor:"accuracy"}`, vitesse 1.05 à 1.1. Une synthèse par réplique ; le WAV est enregistré
à part par l'outil (blob `.wav`), l'URL signée (15 min) sert à `audio.transcribe` (language "fr").
Dans le texte lu : « l'appli Hacou » et « H Z K link » (« H, Z, K, link » avec des virgules si la voix colle les lettres).
La transcription écrit souvent « Hacou » en « Akou », « à coup » ou « Akoo » : c'est la bonne prononciation (le transcripteur ne connaît pas la marque) ;
« Auchan » ou « Rakuten » = à refaire.

| Voix | Genre | Fournisseur | Identifiant | Dernière utilisation | Remarques |
|---|---|---|---|---|---|
| Etienne | homme | cartesia | `c6ccfe32-6bee-484a-a8a2-7a51bee93f99` | – | validée le 18/11 |
| Manon | femme | cartesia | `2f8e82c4-cb94-4e6d-8b6a-29bf58ceb60a` | 19/11 (hacoo35, V3) | modèle sonic-3.5 ; claire et posée. « sur l'appli Hacou » en fin de phrase a été compris « Auchan » : mettre « Code promo Hacou » en tête de phrase. « Tu tapes H Z K link » sans virgules a été mal reconnu : écrire « H, Z, K, link ». Montants bien reconnus. |
| Hélène | femme | inworld | `Hélène` | – | validée le 18/11 |
| Mathieu | homme | inworld | `Mathieu` | – | validée le 18/11 (le pigeon du style D) |
| Marc | homme | azure | `fr-FR-Marc:MAI-Voice-2.1` | 19/11 (hacoo36, E) | servi par azure DragonHDLatestNeural ; très naturelle, débit plutôt lent (la vitesse 1.08 semble peu appliquée : vidéo de 37 s) ; « H Z K link » et tous les montants bien reconnus du premier coup. |
| Soleil | femme | azure | `fr-FR-Soleil:MAI-Voice-2.1` | – | validée le 18/11 |
| Louis | homme | smallest | `louis` | – | validée le 18/11 |
| Leo | homme | xai | `leo` | – | validée le 18/11 |
| Eve | femme | xai | `eve` | – | validée le 18/11 |
| Cosmo | homme | xai | `cosmo` | – | validée le 18/11 (le malin du style D) |
| Speechify par défaut | – | speechify | (sans `voice`) | utilisée par la tâche de 12:47 | voix par défaut des vidéos 1 et 2 |

## À éviter
- Agathe (deepgram) et Isabelle (speechify `isabelle-agent`) : ont mal prononcé le code.
- ElevenLabs : refusé (402) tant que le compte Speko n'est pas rechargé.

## Journal
- 19/11 : vidéo 3 (hacoo35, V3) = Manon (cartesia) ; vidéo 4 (hacoo36, E) = Marc (azure). Pas de nouvelle voix essayée.
