# Journal de bord — Projet JARVIS

Résumé des décisions prises au fil des conversations avec ChatGPT, Gemini
et Claude, dans l'ordre chronologique.

## 14 août 2026 — Cadrage initial

- Objectif : construire un assistant personnel inspiré de JARVIS
  (Iron Man / MCU), pas un simple chatbot.
- Contrainte fondamentale : **local-first, free-first**. Pas d'API
  payante obligatoire, pas d'abonnement nécessaire.
- Périmètre initial : PC Windows uniquement. Pas de domotique, pas
  de multi-appareils. iPad envisagé comme terminal secondaire plus
  tard, pas prioritaire.
- Architecture logique envisagée : Core, Mind, Identity, Voice,
  Memory, Skills, HUD.
- Routage à deux vitesses : Fast Path (commandes simples, sans LLM)
  et Deep Path (demandes complexes, envoyées à un LLM local).

## 18 août 2026 — Blueprint figé pour la Phase 1

- Fusion des propositions ChatGPT + Claude en un blueprint unique :
  **JARVIS Core v0.1**.
- Fichiers prévus : `jarvis.py`, `intents.py`, `apps_registry.py`,
  `skills/open_app.py`, `skills/close_app.py`, `skills/get_time.py`,
  `skills/exit_jarvis.py`.
- Premier objectif absolu : taper `ouvre spotify` → Spotify s'ouvre.
- Explicitement exclu de la Phase 1 : Ollama, LLM, Gemini, API
  ChatGPT, Whisper, Piper, wake word, micro, mémoire, HUD,
  animations, vision, PDF, Spotify avancé, iPad, domotique.
- Six tests de validation (Definition of Done) définis pour la
  Phase 1.
- Décision : ne pas rediscuter l'architecture une fois au PC, la
  construire telle quelle.

## 22 août 2026 — Construction réelle et validation de la Phase 1

- Installation de Python 3.14 et VS Code sur le PC (Asus VivoBook,
  i3-10110U, 4 Go RAM).
- Construction fichier par fichier, dans l'ordre prévu, avec
  l'aide de Claude (explications pédagogiques pas à pas, car
  débutant en informatique).
- Les 6 tests de la Phase 1 sont validés un par un. L'objectif n°1
  du projet (`ouvre spotify` → Spotify s'ouvre) est atteint.
- **Checkpoint posé : Phase 1 terminée à 100 %.**
- Décision : ne pas enchaîner automatiquement sur la voix (Whisper)
  comme "Phase 2" par défaut — revoir d'abord le blueprint global
  pour choisir l'ordre le plus judicieux des briques restantes.

## Fin août / début septembre 2026 — Extension du Core

- Décision : élargir les capacités PC (plus d'apps, plus de skills)
  avant d'ajouter la voix, pour avoir un assistant utile au
  quotidien avant d'affronter les inconnues techniques du matériel
  actuel.
- Ajout de Chrome dans `apps_registry.py` (méthode d'ouverture par
  chemin exécutable, différente de l'URI utilisée pour Spotify) —
  généralisation de `open_app.py` pour gérer plusieurs méthodes.
- Ajout d'une nouvelle intention `SEARCH_WEB` (mots-clés
  "cherche"/"recherche") et de la skill `search_web.py`, qui ouvre
  une recherche Google dans le navigateur.
- Correction d'un bug d'encodage d'URL (accents, caractères
  spéciaux) via `urllib.parse.quote_plus`.

## Point de décision en cours — Le "Mind"

- Demande de Zyad : que JARVIS comprenne des phrases libres et
  tienne de vraies conversations (pas juste des mots-clés fixes).
  Cela correspond à la brique "Mind" / Deep Path du blueprint
  initial, qui nécessite un vrai LLM.
- Constat : le PC actuel (4 Go RAM, pas de GPU dédié) est un facteur
  limitant fort pour faire tourner un LLM local de façon confortable.
- Deux options à trancher plus tard : LLM 100 % local (Ollama, mais
  modèles très limités sur ce PC) vs API gratuite en appoint (ex :
  free tier Gemini, meilleure qualité mais pas 100 % local).
- Recommandation matérielle si nouveau PC envisagé : 16 Go RAM
  minimum (32 Go confortable) + GPU Nvidia avec 8 Go de VRAM
  minimum (ex. RTX 3060 12 Go, RTX 4060).
- Décision non encore prise à ce stade.
