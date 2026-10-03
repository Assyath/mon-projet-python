# Exercice 3 : Programme interactif avec le SDK RodiumAi via Python

Ce projet réimplémente le script interactif de l'exercice 2 en utilisant cette fois le SDK Python officiel de RodiumAi.

## Fonctionnalités
- Etape 1 (Chat) : Envoi d'une question à openai/gpt-4o-mini avec gestion de la température via le SDK.
- Etape 2 (Image) : Appel du module client.images.generate pour créer un visuel avec google/gemini-3.1-flash-lite-image.
- Etape 3 (Video) : Appel du module de génération vidéo asynchrone avec google/veo-3.1-lite.

## Installation
Pour installer et exécuter ce projet, vous devez disposer de Python 3.10 ou supérieur.

1. Installez le SDK officiel et les outils requis :

   pip install -r requirements.txt
 
## Configuration
1. Dupliquez le fichier d'exemple :

   cp .env.example .env
   
2. Ajoutez votre clé secrète dans le fichier `.env` :
   
   RODIUMAI_API_KEY=votre_cle_ici

## Lancement
Pour démarrer le script interactif version SDK, exécutez :

python3 main.py

