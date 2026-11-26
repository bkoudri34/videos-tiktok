# ⚠️ RÈGLE PRIORITAIRE : le mot « Hacoo » n'est JAMAIS écrit dans les vidéos (règle de Badr du 26/11/2026)

Le compte TikTok d'affiliation s'est fait signaler plusieurs fois. Cette règle passe avant toutes les autres de ce fichier, des briefs de `veille/briefs/` et des modèles existants (qui l'écrivent encore : ne les recopie pas tels quels).
- À l'image, aucune occurrence écrite de « Hacoo », « HACOO », « Hacou » ni d'un logo ou d'une icône d'appli Hacoo : ni dans les titres, bandeaux, étiquettes, cartes, champs de code, reçus, téléphones dessinés, écran de fin, mentions légales à l'écran, ni dans les SOUS-TITRES.
- On le dit seulement à l'oral : « l'appli Hacou », « code promo Hacou, H Z K link » (au moins 2 fois, dont une dans les 3 premières secondes).
- À l'écran, on écrit à la place : « code promo », « CODE PROMO : hzklink », « l'appli », « -14 % avec le code hzklink ». Dans les sous-titres, le mot dit « Hacou » est remplacé par « l'appli » ou simplement retiré (voix « code promo Hacou, H Z K link » -> sous-titre « code promo hzklink »).
- Contrôle qualité : si « Hacoo » (ou « Hacou ») apparaît écrit sur une seule image, c'est un POINT BLOQUANT : la vidéo est corrigée et re-rendue, ou n'est ni publiée ni programmée. Vérifie-le sur la planche de contact ET en cherchant « acoo » / « ACOO » / « acou » dans le BODY, les LINES (2e élément : textes affichés) et le HTML généré (grep -i "haco" sur le fichier HTML ne doit rien trouver d'affiché).
- Message de commit de chaque vidéo Hacoo : ajoute « Hacoo seulement à l'oral » (la tâche qui programme les vidéos s'en sert pour vérifier).
- La section plus bas « Hacoo : dire clairement que c'est un code Hacoo » (règle du 10/11) est remplacée : c'est la voix qui le dit clairement, plus l'image.

---
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

# Hacoo : dire clairement que c'est un code Hacoo (règle de Badr du 10/11/2026)
> Remplacée le 26/11/2026 par la règle prioritaire en haut du fichier : « Hacoo » seulement à l'oral, jamais écrit à l'image.

Dans chaque vidéo Hacoo, le spectateur doit comprendre sans hésiter que `hzklink` est un **code promo à utiliser sur l'appli Hacoo** :
- Voix off : toujours « code promo Hacou H Z K link » (ou « le code Hacou H Z K link »), jamais « le code » tout seul. Le mot « Hacou » est dit au moins 2 fois dans la vidéo, dont une fois dans les 3 premières secondes.
- À l'écran : écrire « CODE PROMO HACOO » à côté de `hzklink` partout où le code apparaît (champ de saisie titré « Code promo Hacoo », pastille « CODE HACOO : hzklink »), et le mot « Hacoo » visible dès l'accroche.
- Écran de fin : grande ligne « CODE PROMO HACOO » + `hzklink` + « -14 % sur l'appli Hacoo ».
- Description du post : une ligne explicite « Code promo Hacoo : hzklink (-14 %) » et le hashtag #codepromohacoo.

# Hacoo : rotation des styles + agent veille (règle de Badr du 17/11/2026)

Les vidéos Hacoo ne doivent plus toutes avoir le même look. Chaque jour, l'agent veille (tâche séparée, avant la tâche vidéo) écrit `veille/briefs/AAAA-MM-JJ.md` : il choisit le style de chaque vidéo Hacoo du jour et explique quoi faire (format, accroche type, rythme, scènes, voix). La tâche vidéo applique ce brief. S'il n'y a pas de brief du jour, elle applique elle-même les règles ci-dessous.

## Styles disponibles (`veille/styles.md` tient le catalogue à jour : V3, D, T, E, D2, A au 22/11)
- **V3 « nuit & or »** (voir plus haut) : motion design noir et or, une voix.
- **D2 « Duo dessiné »** (voir plus bas) : le même duo en 2D au trait sur papier, sans Three.js.
- **D « Duo 3D »** (`cfg/duo.py`, `outils/duo3d.js`, `outils/base_duo.css`, exemple `cfg/hacoo30.py`) : deux mannequins 3D façon pâte à modeler (Three.js) sur un sol quadrillé sombre, « le malin » (sportif, à droite) et « le pigeon » (costaud, à gauche), qui dialoguent. Inspiré du format « le connaisseur vs l'ignorant » repéré chez @pileinfo.tv : on reprend le format et le rythme, jamais son contenu.

## Règles de variation
- Les 2 vidéos Hacoo du jour sont dans 2 styles différents dès qu'il en existe au moins 2.
- Un même créneau (vidéo 1 ou vidéo 2) ne garde pas le même style 2 jours de suite.
- Le reste varie toujours aussi : accroche, articles, prix d'exemple, couleur, ordre des écrans.
- **Sujets de Badr** : lis aussi `veille/sujets.md` et applique sa règle de rotation (sur 3 jours glissants, au moins une vidéo Hacoo traite un de ces sujets, par ex. R « pourquoi éviter de demander un remboursement sur Hacoo »).

## Articles
- Sport et streetwear autorisés et encouragés (baskets de running, survêt, sacoche, casquette, doudoune…), dessinés de façon générique dans `cfg/hacoo_items.py`.
- Jamais de nom de marque, de logo, de bande ou virgule reconnaissable, ni les mots « ref », « réplique », « dupe » ou « copie ». Pas de vidéo pour des contrefaçons, même si un compte d'inspiration en fait.

## Style D « Duo 3D » : fabrication
- 25 à 32 s, 8 à 10 répliques courtes qui alternent entre les 2 personnages, ton oral et vanneur, une mini-histoire (le pigeon paie plein pot, le malin lui sort le code promo Hacoo).
- Voix : une synthèse Speko par réplique, `speed: 1.1`, intent `{language:"fr", region:"FR", optimizeFor:"accuracy"}`.
  - Le malin : `voice: "cosmo"`, `constraints: {allowedProviders: {tts: ["xai"]}}`.
  - Le pigeon : `voice: "Mathieu"`, `constraints: {allowedProviders: {tts: ["inworld"]}}`.
  - Écrire « l'appli Hacou » plutôt que « sur Hacou » seul (sinon c'est compris « Rakuten »).
  - Couper les silences de début et de fin de chaque réplique (ffmpeg silenceremove), les recoller dans `full.wav` avec 0,2 s au début et 0,45 s entre les répliques : les bornes donnent directement `SPLITS`.
  - Config : `MINLEN = 0.9`, `GAP = 0.12`, `TAIL = 2.6`.
- `DUO_LINES` : une entrée par réplique `{'who': 'M'|'P', 'M': pose, 'P': pose, 'shot': 'wide'|'M'|'P'}` et `'lbl': False` pour cacher les étiquettes quand une carte fixe occupe le haut. Poses : idle, talk, point, shrug, hip, shock, head, cool, think. Alterner plan large et plan serré sur celui qui parle (coupe franche + zoom « punch » à chaque réplique).
- Écran :
  - accroche fixe en haut dès la 1re image, avec « Hacoo » dedans ;
  - sous-titres énormes au centre, 2 à 3 mots par groupe, un mot clé en `<em>` (surligné rouge), le code en `<i>hzklink</i>` (jaune, jamais en majuscules) ;
  - cartes qui surgissent au-dessus de la tête de celui qui parle (`anc('M'|'P', ...)`) : article + prix d'exemple, ticket, téléphone avec le champ « CODE PROMO HACOO », bulle « ?! », gros total recalculé (un seul ralenti) ;
  - carte de fin blanche : « CODE PROMO HACOO », `hzklink`, « -14 % sur l'appli Hacoo », « liens des articles tendance en bio » et les conditions.
- Rendu : `render.py` lance Chromium avec `--enable-unsafe-swiftshader --use-angle=swiftshader` pour la 3D ; Three.js r149 est embarqué dans le dépôt (`modeles/outils/vendor/three.min.js`, récupéré le 20/11 par `git clone --sparse` de github.com/mrdoob/three.js, tag r149) et chargé par un chemin relatif (`outils/vendor/three.min.js`) : aucun accès réseau n'est nécessaire au rendu.
- Les règles Hacoo du 10/11 s'appliquent : « Hacou » dit au moins 2 fois, dont une dans les 3 premières secondes, et « code promo Hacou H Z K link ».

## Style D2 « Duo dessiné » : fabrication (construit le 20/11/2026)
- Le format du style D (dialogue « le malin vs le pigeon », 8 à 10 répliques, 25 à 32 s, une synthèse Speko par réplique, `SPLITS`, `MINLEN = 0.9`, `GAP = 0.12`, `TAIL = 2.6`) sur le papier ligné du style T, sans Three.js.
- Briques : `cfg/duo2d.py` (`duo2d_js(DUO_LINES, p_bun=False, cap=couleur)`, `duo2d_body(nom_M, nom_P)`, `anc()`), `duo2d.js` (personnages SVG, poses, bouche qui s'ouvre quand il parle, yeux ronds quand choqué, « boil » du trait par feTurbulence dont la graine change toutes les 0,15 s, plans `wide` / `M` / `P` avec coupe franche et zoom « punch »), `base_duo2d.css` (sous-titres noirs à halo papier, mot clé en `<em>` rouge, code en `<i>` jaune ; cartes, étiquettes, bulle, téléphone et carte de fin au feutre). Exemple : `cfg/hacoo40.py`.
- `DUO_LINES` identiques au style D (mêmes poses : idle, talk, point, shrug, hip, shock, head, cool, think ; `'lbl': False` quand une carte occupe le haut ou sur l'écran de fin). `p_bun=True` ajoute un chignon au pigeon (« la pigeonne », voix féminine).
- Pour éviter qu'un mot surligné passe seul à la ligne, mettre la ponctuation dans la balise (`<em>combien ?</em>`) ou utiliser `&nbsp;`.

## Style A « Alerte stickers » : fabrication (construit le 22/11/2026, style envoyé par Badr)
- Format « mise en garde » : 6 à 8 répliques, 28 à 35 s, une seule voix calme et sérieuse, une synthèse Speko par réplique, `SPLITS`, `MINLEN = 1.6`, `GAP = 0.22`, `TAIL = 2.2`. Une scène par réplique, chacune avec son étiquette de rubrique (`tag()`), un ou deux bandeaux (`ban(texte, top, 'red'|'grn'|'yel'|'', g=…)`) et un dessin autocollant (`stk()`).
- Briques : `cfg/alerte.py` (`chrome()` en tête de BODY = gribouillis + compte à rebours `#cd` qui décompte la durée réelle ; `kara()` pour écrire les groupes de sous-titres : pavés noirs, `<em>` pavé jaune, `<i>` pavé rouge, ponctuation collée automatiquement avec espace insécable ; dessins prêts : `PADLOCK`, `avatar()` + `banned()`, `BOX`, `tee(couleur)`, `GUY` + `ARROWS_IN`, `TAPE`, `BOOKMARK`, `red_circle()` qui se trace), `base_alerte.css` (`.card`, `.pill`, `.tag`, `.ban`, `.stk`). Exemple complet : `cfg/hacoo_alerte1.py`.
- Zones : titres entre 300 et 1050 px, sous-titres à 1180 px (2 lignes max), rien d'important sous 1540 px ni à droite de 950 px. L'accroche (bandeau rouge « ⚠ ATTENTION » ou équivalent + « Hacoo ») est visible dès la 1re image, sans animation.
- Fin : marque-page orange + « ENREGISTRE CETTE VIDÉO » + « ENVOIE-LA ↗ » + pastille « CODE PROMO HACOO : hzklink » + mention des conditions.
- Sujets qui vont bien avec ce style : les mises en garde de `veille/sujets.md` (retours et remboursements, erreurs avant de payer, faux codes…). Ne jamais affirmer un fait non vérifié : écrire « des utilisateurs racontent… » plutôt que « Hacoo bannit à vie ».

# Contrôle qualité AVANT programmation et envoi (règle de Badr du 18/11/2026)

**Obligatoire pour chaque vidéo** (les 3 parrainage et les 2 Hacoo), juste après le rendu final et **avant** : le commit/push, la programmation dans Metricool et l'envoi à Badr (SendUserFile). Une vidéo qui n'a pas passé ce contrôle n'est ni programmée ni envoyée comme « prête ».

## Qui contrôle
Un sous-agent lancé avec l'outil Task, qui n'a pas fabriqué la vidéo (regard neuf). Donne-lui : le chemin du MP4, le sujet, le titre TikTok et la description prévus, le format choisi (voir « Formats parrainage » plus bas) et le fichier `QUALITE.md`.

## Ce qu'il vérifie
1. `ffprobe` : 1080x1920, 9:16, durée (parrainage v3 : 18 à 26 s ; Hacoo Duo : 25 à 32 s).
2. Images fixes à 0,0 s, 0,5 s, 1 s, 2 s, 3 s puis toutes les 2 s, assemblées en planche de contact, **regardées** une par une.
3. Voix : `audio.transcribe` (Speko, `language: "fr"`, `word_timestamps: true`) ; crête audio (`ffmpeg volumedetect`, ≤ -1 dB).
4. **Mot-clé de recherche** (la Recherche TikTok fait ≈ +65 % de vues sur @htm.invest) :
   - parrainage : « parrainage <banque> » (ex. « parrainage Hello bank ») ; Hacoo : « code promo Hacoo » ;
   - il doit être : lisible à l'écran au plus tard à **0,5 s** (accroche fixe ou bandeau, pas seulement tapé lettre par lettre) ; **dit à l'oral dans les 2 premières secondes** ; dans le **titre TikTok** ; dans la **1re ligne de la description** ; en hashtags (#parrainage + #<banque>, ou #hacoo + #codepromohacoo).

## Note sur 100
- Accroche 0-1,5 s (25) : lisible dès les premières images, 6 à 9 mots, déclencheur fort (STOP, perte d'argent, question, résultat montré).
- Mot-clé de recherche (20) : 5 écran + 5 oral + 4 titre + 4 1re ligne + 2 hashtags.
- Rythme / rétention (20) : un changement visuel toutes les 1,5 à 3 s, sous-titres calés sur la voix, un seul ralenti, fin qui boucle.
- Clarté de l'offre + appel à l'action (15).
- Variété (10) : format différent des 2 autres vidéos du jour et de la vidéo précédente du même sujet (voir journal de `QUALITE.md`).
- Technique (10) : rien ne déborde ni ne se chevauche, zones de sécurité respectées, son propre, pas de logo.

**Points bloquants** (vidéo refusée quelle que soit la note) : montant non vérifié ou différent de la source officielle du jour, mention « Offre(s) soumise(s) aux conditions en vigueur » absente, texte illisible ou qui déborde, son absent ou saturé, logo de marque, Revolut « illimité » ou prime en argent pour le filleul, contrefaçon / « ref » / réplique, code promo d'un autre créateur.

## Décision
- **≥ 70/100 et aucun point bloquant** : OK.
- **Sinon** : corrige. Titre et description : corrige directement. Écran, voix ou rythme : corrige le modèle et refais le rendu (une seule fois), puis refais le contrôle.
- **Toujours bloquant après correction** : ne programme pas la vidéo dans Metricool. Envoie-la quand même à Badr avec « ⚠️ NON PROGRAMMÉE » en tête de légende et la raison.

## Après le contrôle
- Ajoute à la fin de chaque description parrainage : « Lien de parrainage : je touche une prime. » (loi influenceurs du 9 juin 2023).
- Dans la légende SendUserFile envoyée à Badr, ajoute une ligne : « Contrôle qualité : <note>/100 · format <Fx> · ✅ <point fort> · ⚠️ <point à améliorer> ».
- Ajoute une ligne par vidéo au journal de `QUALITE.md` (date, compte, sujet, format, note, points bloquants, corrections) et pousse-le avec les vidéos. Dans le message final, donne la note de chaque vidéo.

# Formats parrainage : faire varier les vidéos (règle de Badr du 18/11/2026)

L'univers visuel v3 « nuit & or » reste. Ce qui change chaque jour, c'est **le format** (le scénario). Inspiré des formats qui marchent chez @hacooultra14 et @pileinfo.tv (voir `veille/comptes.md`) : on reprend la mécanique, jamais le texte, les visuels ni les codes.

| Code | Format | Exemple d'accroche (à reformuler) |
|---|---|---|
| F1 | STOP / erreur à éviter | « STOP avant d'ouvrir ton compte Fortuneo » |
| F2 | Démystification | « Comment marche VRAIMENT le parrainage Hello bank » |
| F3 | Anti-arnaque / confiance | « 500 € de prime ? Le vrai maximum, c'est… » |
| F4 | Argent laissé sur la table | « Tu laisses 150 € à Hello bank sans le savoir » |
| F5 | Défi chrono | « Compte ouvert en moins de 5 minutes, chrono » |
| F6 | Le chemin de ta prime | de l'ouverture au virement, étape par étape, avec les délais |
| F7 | Tuto écran 1-2-3 | téléphone illustré, étapes numérotées, sans logo |
| F8 | Résultat d'abord | notification « Virement reçu +80 € » ou solde avant/après en plein écran dès la 1re image |
| F9 | Duel / comparatif | « Gold ou Fosfo ? », « BoursoBank ou Fortuneo ? » |
| F10 | Le connaisseur vs l'ignorant | 2 personnages qui dialoguent (peut réutiliser le style Duo 3D) |

Règles :
- Les 3 vidéos parrainage du jour ont **3 formats différents**, et au moins 1 sur 3 est un F8 (résultat d'abord).
- Un sujet ne reprend pas le format de sa vidéo précédente (regarde le journal de `QUALITE.md`).
- Le mot-clé « parrainage <banque> » est dans l'accroche quel que soit le format.
- Hacoo : la rotation des styles de l'agent veille (`veille/briefs/`) s'applique toujours ; les formats F1 à F10 peuvent servir de scénario à l'intérieur de ces styles.
