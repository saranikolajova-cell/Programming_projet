# Music Listening Habits Analyzer

Ce script Python permet d'analyser vos données d'écoute musicale à partir de fichiers JSON (exportation de l'historique de streaming). Il traite les données pour extraire des statistiques sur vos habitudes de d'écoute.

## Fonctionnalités
* **Nettoyage automatique** : Filtre les musiques passées (0 ms).
* **Analyse de pointe** : Identifie l'heure de la journée où vous écoutez le plus de musique.
* **Top Artiste** : Détermine votre artiste préféré durant votre heure de pointe.
* **Répartition complète** : Affiche le volume d'écoute pour chaque heure de la journée.

## Installation et Utilisation
1. Installez la bibliothèque Pandas :
   pip install pandas

2. Modifiez la variable `FILE_TO_ANALYZE` dans le script avec le chemin de votre fichier JSON.

3. Lancez le script :
   python nom_du_script.py

## Exemple de Rapport
----------------------------------------------
🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧
 REPORT FOR: StreamingHistory_music_1.json
🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧
Total songs analyzed: 1245
Your peak listening hour is: 18:00
Top artist during that hour: Daft Punk
------------------------------
LISTENING VOLUME BY HOUR:
0     12
18    245
------------------------------

## Structure
* script.py : Le code d'analyse.
* README.md : Documentation.

---
*Projet d'analyse de données personnelles.*
