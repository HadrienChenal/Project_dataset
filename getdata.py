import pandas as pd
import kagglehub
import os

# Chemin récupéré via kagglehub
path = kagglehub.dataset_download("jockeroika/life-style-data")

# Localise le fichier CSV (à adapter selon le nom exact)
csv_path = os.path.join(path, "Final_data.csv")

# Charger le DataFrame
df = pd.read_csv(csv_path)
print(df.head())