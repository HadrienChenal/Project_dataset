"""
import pandas as pd
import kagglehub
import os

# Télécharge le dataset depuis Kaggle (ou récupère depuis le cache)
path = kagglehub.dataset_download("alperenmyung/international-hotel-booking-analytics")

# Liste tous les CSV du dossier téléchargé
csv_files = [f for f in os.listdir(path) if f.endswith(".csv")]

# On peut choisir de charger chacun des CSV séparément
dfs = {}
for csv_file in csv_files:
    csv_path = os.path.join(path, csv_file)
    dfs[csv_file] = pd.read_csv(csv_path)
    print(f"\n--- Aperçu de {csv_file} ---")
    print(dfs[csv_file].head())

"""