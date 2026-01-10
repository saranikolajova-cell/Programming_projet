# Music Listening Habits Analyzer

## Projet : Analyse de Données Personnelles (GDPR)
Ce projet a été réalisé dans le cadre d'un travail académique visant à créer un outil générique d'analyse de données extraites via les droits RGPD (GDPR). 

**Problématique :** *Comment mon activité sur Spotify révèle-t-elle mes habitudes d'écoute et mes artistes préférés tout au long de la journée ?*

**Structure des données**
 * {
    "endTime" : "AAAA-MM-JJ HH:MM",
    "artistName" : "Nom d'artiste",
    "trackName" : "Titre",
    "msPlayed" : ssss
  }
---

## Fonctionnalités
L'outil transforme les fichiers JSON bruts de Spotify en un portrait comportemental :
* **Nettoyage Automatique** : Filtre les musiques passées ou erreurs de lecture (0 ms) pour ne garder que l'engagement réel.
* **Analyse Temporelle** : Identifie l'heure de pointe (Peak Hour) pour révéler les cycles de routine de l'utilisateur.
* **Top Artiste Contextuel** : Détermine l'artiste dominant durant l'heure la plus active.
* **Visualisation Horaire** : Affiche la répartition complète du volume d'écoute sur 24h.

---

## Confidentialité & RGPD
Conformément aux consignes de protection des données :
* **Données Privées** : Les fichiers d'historique (.json) ne sont JAMAIS envoyés sur le dépôt GitHub.
* **Sécurité** : Un fichier .gitignore est utilisé pour exclure automatiquement les données sensibles.
* **Traitement Local** : L'analyse s'effectue entièrement sur votre machine personnelle.

---

## Installation et Utilisation

1. Prérequis : Installez la bibliothèque Pandas avec la commande : pip install pandas

2. Configuration : Placez votre fichier d'export Spotify (ex: StreamingHistory_music_1.json) dans le dossier du projet.

3. Modification : Dans le script Python, changez la variable FILE_TO_ANALYZE avec le nom de votre fichier.

4. Exécution : Lancez le script avec la commande : python votre_script.py

---

## Exemple de Rapport de Sortie

REPORT FOR: StreamingHistory_music_1.json
Total songs analyzed: 1245
Your peak listening hour is: 18:00
Top artist during that hour: Daft Punk
------------------------------
LISTENING VOLUME BY HOUR:
17    140
18    245
19    110
------------------------------

---

## Structure du Dépôt
* script.py : Le moteur d'analyse (Pipeline de nettoyage et calculs).
* .gitignore : Protection des données personnelles (exclut les fichiers JSON).
* README.md : Documentation et problématique du projet.

---
Projet réalisé par NIKOLAJOVA Sara, KRAVCHENKO Daria et TISNES Francesca - M1 APE - Université de Strasbourg
