import pandas as pd
import os
import kagglehub

# Récupère le chemin sans re-télécharger (grâce au cache local)
path = kagglehub.dataset_download("jockeroika/life-style-data")

# Trouve automatiquement le CSV
csv_files = [f for f in os.listdir(path) if f.endswith(".csv")]
csv_path = os.path.join(path, csv_files[0])

# Charge les données
df = pd.read_csv(csv_path)

# Exemple : afficher un aperçu
#print(df.head())

# Exemple d’analyse simple
#print("\n--- Statistiques sur les calories brûlées ---")
#print(df["Calories_Burned"].describe())
print(df["Height (m)"].describe())