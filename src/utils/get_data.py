import os
import pandas as pd
import kagglehub


def charger_csvs(path: str) -> dict[str, pd.DataFrame]:
    """
    Charge tous les fichiers CSV présents dans un dossier en DataFrames pandas.
    """
    csv_files = [f for f in os.listdir(path) if f.endswith(".csv")]
    dfs: dict[str, pd.DataFrame] = {}
    for csv_file in csv_files:
        csv_path = os.path.join(path, csv_file)
        dfs[csv_file] = pd.read_csv(csv_path)
    return dfs

def telecharger_dataset(nom_dataset: str) -> str:
    """
    Télécharge (ou récupère depuis le cache) un dataset Kaggle via kagglehub.
    Retourne le chemin du dossier contenant les fichiers CSV.
    param nom_dataset: Nom du dataset Kaggle (format "utilisateur/dataset").
    """
    path = kagglehub.dataset_download(nom_dataset)
    return path