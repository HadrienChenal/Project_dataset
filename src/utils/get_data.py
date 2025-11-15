import os
import pandas as pd
import kagglehub
import shutil

# Racine du projet (2 dossiers au-dessus du dossier utils)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Dossiers de données
DATA_DIR = os.path.join(PROJECT_ROOT, "data") # Dossier principal des données
RAW_DATA_PATH = os.path.join(DATA_DIR, "raw") # Données brutes
# Lien CSV des données
KAGGLE_MODEL_SLUG = "alperenmyung/international-hotel-booking-analytics"

def telecharger_dataset(nom_dataset: str) -> str:
    """
    Télécharge (ou récupère depuis le cache) un dataset Kaggle via kagglehub.
    Retourne le chemin du dossier contenant les fichiers CSV.
    param nom_dataset: Nom du dataset Kaggle (format "utilisateur/dataset").
    """
    os.makedirs(RAW_DATA_PATH, exist_ok=True)
    # Si des CSV nettoyés sont présents localement, les utiliser en priorité
    if os.path.isdir(RAW_DATA_PATH):
        csvs = [f for f in os.listdir(RAW_DATA_PATH) if f.endswith('.csv')]
        if csvs:
            print(f"Utilisation des données locales dans {RAW_DATA_PATH}")
            return RAW_DATA_PATH

    # Sinon tenter de télécharger via kagglehub (peut nécessiter configuration Kaggle)
    path = kagglehub.dataset_download(nom_dataset)

    fichiers_csv = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".csv"):
                src = os.path.join(root, file)
                dst = os.path.join(RAW_DATA_PATH, file)
                shutil.copy(src, dst)
                fichiers_csv.append(file)

    if not fichiers_csv:
        print("Aucun fichier CSV trouvé dans le dataset Kaggle.")
    else:
        print(f"CSV copiés dans {RAW_DATA_PATH} : {fichiers_csv}")
    return path

def charger_csvs(path: str) -> dict[str, pd.DataFrame]:
    """
    Charge tous les fichiers CSV présents dans un dossier en DataFrames pandas.
    """
    csv_files = [f for f in os.listdir(path) if f.endswith(".csv")]
    dfs: dict[str, pd.DataFrame] = {}
    for csv_file in csv_files:
        csv_path = os.path.join(path, csv_file)
        # Lire le CSV
        df = pd.read_csv(csv_path)
        # Normaliser la clé : si les fichiers sont préfixés par 'cleaned_'
        # on expose la version sans préfixe pour correspondre aux clés
        # attendues (par ex. 'reviews.csv', 'hotels.csv').
        key = csv_file
        if csv_file.startswith("cleaned_"):
            key = csv_file[len("cleaned_"):]
        dfs[key] = df
    return dfs

if __name__ == "__main__":
    # Test rapide de la fonction
    dataset_path = telecharger_dataset(KAGGLE_MODEL_SLUG)
    dataframes = charger_csvs(dataset_path)
    for name, df in dataframes.items():
        print(f"{name}: {len(df)} lignes")