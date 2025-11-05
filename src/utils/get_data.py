import pandas as pd
import kagglehub
from pathlib import Path

# Télécharge le dataset depuis Kaggle (ou récupère depuis le cache)
path = Path(kagglehub.dataset_download("alperenmyung/international-hotel-booking-analytics"))

# Liste tous les CSV du dossier téléchargé
csv_files = list(path.glob("*.csv"))

# On peut choisir de charger chacun des CSV séparément
dfs = {}
for csv_file in csv_files:
    dfs[csv_file.name] = pd.read_csv(csv_file)
    print(f"\n--- Aperçu de {csv_file.name} ---")
    print(dfs[csv_file.name].head())
