import os
import kagglehub
from typing import List

# Racine du projet (2 dossiers au-dessus du dossier utils)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Dossiers de données
DATA_DIR = os.path.join(PROJECT_ROOT, "data") # Dossier principal des données
RAW_DATA_PATH = os.path.join(DATA_DIR, "raw") # Données brutes
CLEAN_DATA_PATH = os.path.join(DATA_DIR, "cleaned") # Données nettoyées

# Lien CSV des données
KAGGLE_MODEL_SLUG = "alperenmyung/international-hotel-booking-analytics"
DATA_FILES: List[str] = ["hotels.csv", "users.csv", "reviews.csv"] # Liste des fichiers de données

def ensure_directories(path: str) -> None:
    """
    Crée les répertoires de données raw et cleaned si nécessaire.
    param path: Chemin du répertoire à créer.
    """
    os.makedirs(path, exist_ok=True)


def telecharger_dataset(nom_dataset: str) -> str:
    """
    Télécharge (ou récupère depuis le cache) un dataset Kaggle via kagglehub.
    Retourne le chemin du dossier contenant les fichiers CSV.
    param nom_dataset: Nom du dataset Kaggle (format "utilisateur/dataset").
    """
    path = kagglehub.dataset_download(nom_dataset)
    return path




