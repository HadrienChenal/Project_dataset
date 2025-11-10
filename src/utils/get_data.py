import os
import shutil
from .common_functions import (
    RAW_DATA_PATH,
    KAGGLE_MODEL_SLUG,
    ensure_directories,
    telecharger_dataset
)

def charger_csvs() -> None:
    """
    Charge tous les fichiers CSV présents dans le dossier data/raw.
    """
    try:
        #Téléchargement du dataset depuis Kaggle
        dataset_path = telecharger_dataset(KAGGLE_MODEL_SLUG)
        print(f"Dataset téléchargé dans le cache : {dataset_path}")
        # Copie des fichiers CSV dans le dossier RAW_DATA_PATH
        for file_name in os.listdir(dataset_path):
            if file_name.endswith(".csv"):
                src = os.path.join(dataset_path, file_name)
                dst = os.path.join(RAW_DATA_PATH, file_name)
                shutil.copy(src, dst)

        print("Téléchargement et copie terminés avec succès !")

    except Exception as e:
        print(f"Erreur lors du téléchargement des données : {e}")

# --- Point d'entrée principal ---
if __name__ == "__main__":
    ensure_directories(RAW_DATA_PATH)
    charger_csvs()

