# Style des vidéos (v2, à partir du 28/10/2026)

Objectif : un rendu moins « IA / pub », plus natif TikTok et plus viral. S'applique aux vidéos parrainage (@htm.invest) et Hacoo.

## Accroche (0 à 1,5 s)
- Le texte d'accroche est lisible dès la première image (pas de fondu depuis le noir, pas d'intro de logo).
- Une seule idée choc, 6 à 9 mots maximum, qui crée une curiosité ou une tension, par exemple :
  - « Ta banque te paie pour l'ouvrir. Sérieux. »
  - « 390 € que la plupart des gens laissent sur la table »
  - « Arrête de payer plein tarif sur Hacoo »
  - « Personne ne t'a dit ça pour ton compte en banque »
- Change d'accroche chaque jour. Ne réutilise jamais celle de la veille.
- Interdit : fausses histoires personnelles (« j'ai gagné… »), faux avis, faux témoignages, montants non vérifiés.

## Rythme
- 13 à 18 s au total, avec un changement visuel toutes les 1,5 à 3 s : coupe, zoom « punch », secousse ou changement d'écran.
- Peu de ralentis : un seul moment fort maximum (le montant ou le code), pas plus.
- Une fin qui boucle : la dernière image doit pouvoir enchaîner naturellement sur la première, pour favoriser le revisionnage.

## Look natif TikTok (moins « IA »)
- Sous-titres façon TikTok : texte blanc en gras avec un contour noir ou un fond en pastille, affiché mot par mot ou par groupe de 2-3 mots, calé exactement sur la voix off. Ils remplacent les gros titres décoratifs.
- Moins d'effets « premium » génériques : pas de halos, de bokeh ni de dégradés néon partout. Une ou deux couleurs d'accent, des fonds plus mats.
- Des éléments concrets et lisibles plutôt qu'abstraits :
  - parrainage : une notification de virement de prime ou une checklist d'étapes ;
  - Hacoo : un panier dont le total baisse au moment où on tape le code.
- Composition un peu imparfaite : léger mouvement de caméra à la main, cadrage pas toujours parfaitement centré, grain conservé.
- Peu d'emojis (2 ou 3 maximum dans toute la vidéo).
- Zones de sécurité TikTok : aucun texte important dans les 380 px du bas, ni dans les 150 px de droite (boutons j'aime / commentaire), ni dans les 200 px du haut.

## Voix off
- Ton oral et conversationnel, en tutoyant, avec des formulations parlées (« t'as », « regarde », « franchement ») mais sans excès.
- Une phrase courte par plan. Aucune liste lue d'une traite.
- Vitesse Speko 1.12. Le texte affiché à l'écran reprend la voix off mot pour mot.
- Code Hacoo : à l'oral « H Z K link », à l'écran toujours `hzklink`.

## Appels à l'action
- Banques : « Envoie-moi « PARRAINAGE » en privé » (ou le nom de la banque). Mention « Offre(s) soumise(s) aux conditions en vigueur » toujours visible à la fin.
- Hacoo : « -14 % avec le code hzklink », « liens des articles tendance en bio ».
- Tu peux ajouter une relance d'engagement : « Enregistre la vidéo pour plus tard » ou « Envoie-la à quelqu'un qui paie trop de frais bancaires ».

## Description du post
- La première ligne reprend l'accroche, puis 1 ou 2 lignes utiles, puis l'appel à l'action et les conditions.
- 5 à 7 hashtags, dont 2 ou 3 larges (#bonplan, #argent, #astuce) et le reste ciblé.

## Contrôle avant rendu
- Vérifie les images fixes : aucun texte ne déborde, ne se chevauche ni ne sort des zones de sécurité, et les sous-titres sont synchronisés avec la voix.

# Style v3 « nuit & or » (règle de Badr du 08/11/2026, s'applique à partir du 09/11/2026)

Badr a validé la voix et l'univers visuel de sa vidéo de référence (pâtisserie, fond noir et or). **On copie le style, pas la vidéo** : ni son script, ni son enchaînement de scènes, ni ses formules (« Marre de payer… / Le seul truc qui… / Et si on te disait… / sans te ruiner ») ne doivent être repris tels quels. Chaque vidéo a son propre scénario, ses propres scènes et sa propre accroche.

## Voix off (obligatoire)
- Voix clonée Speko « voix-htm-luxe » : `voice: "Y5OEiyuzo8xoTlHF9G5k"`, `constraints: {allowedProviders: {tts: ["elevenlabs"]}}`, `speed: 1.05`, intent `{language:"fr", region:"FR", optimizeFor:"accuracy"}`.
- Tout le script en un seul appel, une réplique par paragraphe (ligne vide entre les répliques). Écrire « Hacou » pour que « Hacoo » soit bien prononcé, « H Z K link » pour le code.
- Vérifier chaque rendu avec `audio.transcribe` (url signée du résultat, `language: "fr"`, `word_timestamps: true`) : si un mot est mal prononcé ou manquant, refaire la réplique seule. Les temps des mots servent à caler les titres (`SPLITS` et `GSTART` dans la config).

## Univers visuel (à garder)
- Fond noir mat, lumière et accents dorés (dégradé or, halo léger), grain ; sol quadrillé doré en perspective et rayons dorés pour les moments forts.
- Habillage caméra : coins de cadre, « ● REC · CAM 01 » + lieu/thème à gauche, compteur qui défile à droite.
- Titres : capitales blanches très grasses avec léger halo, tapées lettre par lettre au rythme de la voix ; 2e ligne en italique serif dorée ; gros montants en serif doré.
- Objets illustrés en aplat (personnages, comptoir, ticket, téléphone, cartes, cadrans, pièces, étiquettes reliées par des traits, barre de recherche qui se tape, pastilles d'infos) : des éléments concrets, pas de logos de marques.
- Musique de fond douce (nappe + pulsation) sous la voix, bruitages discrets (cloches, clics, impact sur le moment fort), un seul ralenti.

## À varier d'une vidéo à l'autre
- Le scénario et l'accroche (6 à 9 mots), l'ordre et le type de scènes : par ex. personnage devant son relevé, file d'attente au guichet, appli ouverte sur le téléphone, coffre-fort, balance avant/après, chronomètre de fin d'offre, comparatif en colonnes, carte de fidélité, colis qui arrive, essayage, etc. Le personnage peut changer (tenue, coiffure, femme/homme, âge).
- Couleur d'accent secondaire possible (rouge, bleu nuit, vert émeraude) mais le noir et or reste dominant.
- Durée 18 à 26 s.
- Garder : fin qui boucle sur l'accroche, mentions légales visibles à la fin, zones de sécurité (texte important hors des 380 px du bas, 150 px de droite, 200 px du haut ; l'habillage caméra peut y rester).

## Outils
`modeles/outils/` : `build.py` (découpe de la voix, timeline, génération du modèle HTML + sfx, images fixes, mixage, rendu 60 i/s en 2 morceaux + grain), `engine.js`, `base_luxe.css`, `sfx_luxe_template.py`, et `cfg/luxe.py` (briques : habillage caméra, titres tapés, personnage, comptoir). Exemples : `cfg/luxe_fortuneo.py`, `cfg/luxe_hacoo.py` (tests du 08/11, à ne pas recopier tels quels).
