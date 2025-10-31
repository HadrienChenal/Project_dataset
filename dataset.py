import pandas as pd
import os
import kagglehub

# Récupère le chemin du dataset
path = kagglehub.dataset_download("alperenmyung/international-hotel-booking-analytics")

# Liste tous les CSV
csv_files = [f for f in os.listdir(path) if f.endswith(".csv")]

# Charge tous les CSV dans des DataFrames
dfs = {}
for csv_file in csv_files:
    csv_path = os.path.join(path, csv_file)
    dfs[csv_file] = pd.read_csv(csv_path)

# Exemple d'aperçu et de statistiques pour chaque fichier
for name, df in dfs.items():
    print(f"\n=== {name} ===")
    print("Aperçu des 5 premières lignes :")
    print(df.head())
    print("\nStatistiques descriptives numériques :")
    print(df.describe())