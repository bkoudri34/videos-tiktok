# Carnet des voix off (Speko)

Toujours : language fr, intent {language:"fr", region:"FR", optimizeFor:"accuracy"}, et le fournisseur épinglé dans constraints.allowedProviders.tts. Note réalisme/fluidité sur 10 après chaque utilisation.

Astuces apprises : écrire les montants avec le symbole « € » (« 260 € ») et pas « euros » en toutes lettres avec Etienne (sinon « euro-sse ») ; écrire les heures en lettres (« quinze heures ») ; pour Cartesia, `speed` 1.15-1.2 pour atteindre 150-175 mots/min ; ne pas commencer par une interjection (« Attends ! ») qui retarde le mot-clé et se prononce mal.

## En rotation (voix françaises natives, mesurées propres par Speko)
| Voix | Fournisseur / modèle | voice | Genre | Notes | Dernière utilisation |
|---|---|---|---|---|---|
| Etienne (Precise Specialist) | cartesia / sonic-3.5 | c6ccfe32-6bee-484a-a8a2-7a51bee93f99 | homme | claire, régulière, très constante. 19/11 (Boursorama, speed 1.2) : réalisme 7, fluidité 7 ; ≈ 150 mots/min ; 1er essai avec « euros » en lettres mal lu, « Attends » compris « Atteins » à speed 1.05 | 19/11/2026 |
| Manon (Bright Belle) | cartesia / sonic-3.5 | 2f8e82c4-cb94-4e6d-8b6a-29bf58ceb60a | femme | claire, constante. 19/11 (Hello bank, speed 1.15) : réalisme 8, fluidité 8 ; ≈ 170 mots/min, tout bien prononcé (Hello Prime, Hello Start plus, 13e) ; niveau faible (≈ -26 dB moyen) : +7 dB avant le découpage | 19/11/2026 |
| Agathe | deepgram / aura-2 | aura-2-agathe-fr | femme | claire, régulière | — |
| Hélène | inworld / inworld-tts-2 | Hélène | femme | claire, constante. 19/11 (essai Hello bank, non retenue) : réalisme 6, fluidité 5 ; début haché (« Tarrainage », « Hello bank » avalé), « 15 heures » compris « 18h » ; 1re note < 6 | 19/11/2026 (essai) |
| Mathieu | inworld / inworld-tts-2 | Mathieu | homme | débit rapide (≈ 185 mots/min) ; déjà utilisé pour le « pigeon » du Duo 3D | 18/11/2026 |
| Soleil | azure / MAI-Voice-2.1 | fr-FR-Soleil:MAI-Voice-2.1 | femme | voix française native, pas encore mesurée | — |
| Marc | azure / MAI-Voice-2.1 | fr-FR-Marc:MAI-Voice-2.1 | homme | 19/11 (essai Boursorama, non retenu) : servi par le modèle DragonHDLatestNeural ; pauses de 0,5 à 1,1 s entre presque tous les groupes, ≈ 135 mots/min, voix hachée : réalisme 6, fluidité 4 ; 1re note < 6 | 19/11/2026 (essai) |

## À tester
| Voix | Fournisseur / modèle | voice | Genre | Remarque |
|---|---|---|---|---|
| Cosmo | xai / tts | cosmo | homme | multilingue, déjà utilisé pour le « malin » du Duo 3D |
| Eve / Leo | xai / tts | eve / leo | femme / homme | multilingues |
| Isabelle | speechify / simba-3.5 | isabelle-agent | femme | voix par défaut utilisée le 18/11 |
| Louis / Manon | smallest / lightning_v3.1_pro | louis / manon | homme / femme | non mesurées |
| Aurelie | rime / arcanav3 | aurelie | femme | débit lent (≈ 136 mots/min) : à accélérer |

## Bloquées pour l'instant
| Voix | Fournisseur | Raison |
|---|---|---|
| voix clonée « voix-htm-luxe », Michael (parisien), Amelie, Richie Tekan, Sunshine | elevenlabs / eleven_v3_conversational | erreur 402 (encore le 19/11) : Badr doit faire une première recharge de 5 $ sur Speko. Dès que ça marche, les tester en priorité. |

## Écartées
(aucune)
