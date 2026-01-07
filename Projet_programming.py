import pandas as pd
import json
import os

# 1. PARAMETRES (Importation de data)
FILE_TO_ANALYZE = 'StreamingHistory_music_1.json'

def automated_music_report(target_file):
    """
    Automates the extraction of listening habits from a single JSON file.
    """
    # Check if file exists to prevent crash
    if not os.path.exists(target_file):
        print(f"❌ Error: The file '{target_file}' was not found in: {os.getcwd()}")
        return

    try:
        # Load and parse
        with open(target_file, 'r', encoding='utf-8') as f:
            df = pd.DataFrame(json.load(f))

        # Nettoyage des data automatisé
        # Le temps convertit des ms en heures et création de la colonne "heure"
        df['endTime'] = pd.to_datetime(df['endTime'])
        df = df[df['msPlayed'] > 0]
        df['hour'] = df['endTime'].dt.hour

        # Statistiques calculés
        hourly_data = df['hour'].value_counts().sort_index()
        peak_hour = hourly_data.idxmax()
        total_plays = len(df)
        
        # L'auteur le plus joué a l'heure "peak"
        peak_hour_df = df[df['hour'] == peak_hour]
        top_artist = peak_hour_df['artistName'].mode()[0]

        # Les OUTPUTS
        print(f" REPORT FOR: {target_file}")
        print(f"Total songs analyzed: {total_plays}")
        print(f"Your peak listening hour is: {peak_hour}:00")
        print(f"Top artist during that hour: {top_artist}")
        print("LISTENING VOLUME BY HOUR:")
        print(hourly_data.to_string())

    except Exception as e:
        print(f"❌ An error occurred during automation: {e}")

# 3. Automatisation pour notre fichier 
if __name__ == "__main__":
    automated_music_report(FILE_TO_ANALYZE)
