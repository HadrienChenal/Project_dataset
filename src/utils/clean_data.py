import os
import pandas as pd
import kagglehub # type: ignore
from datetime import datetime
import shutil

## Constantes de chemins et configurations ##

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
# Définit des chemins absolus
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
RAW_DATA_PATH = os.path.join(DATA_DIR, "raw")
CLEAN_DATA_PATH = os.path.join(DATA_DIR, "cleaned")

KAGGLE_MODEL_SLUG = "alperenmyung/international-hotel-booking-analytics"
DATA_FILES = ["hotels.csv", "users.csv", "reviews.csv"]

#############################################

def ensure_directories() -> None:
    """
    Crée les répertoires de sortie.
    """
    os.makedirs(RAW_DATA_PATH, exist_ok=True)
    os.makedirs(CLEAN_DATA_PATH, exist_ok=True)

def clean_hotels(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoyage spécifique du tableau hotels.csv
    """
    print(f"{len(df)} lignes initiales")
    df = df.dropna(subset=["hotel_name", "city", "country"])
    numeric_cols = [
        "star_rating", "lat", "lon",
        "cleanliness_base", "comfort_base",
        "facilities_base", "location_base",
        "staff_base", "value_for_money_base"
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    print(f"{len(df)} lignes restantes.")
    return df

def clean_users(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoyage spécifique du tableau users.csv"""
    print(f"{len(df)} lignes initiales")
    df = df.drop_duplicates(subset="user_id")
    df = df.dropna(subset=["user_id", "country"])
    df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce")
    df["user_gender"] = df["user_gender"].str.title().fillna("Unknown")
    df["traveller_type"] = df["traveller_type"].str.title().fillna("Unknown")
    
    print(f"{len(df)} lignes restantes.")
    return df

def clean_reviews(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoyage spécifique du tableau reviews.csv"""
    print(f"{len(df)} lignes initiales")
    df = df.dropna(subset=["review_id", "hotel_id", "user_id", "score_overall"])
    numeric_cols = [
        "score_overall", "score_cleanliness",
        "score_comfort", "score_facilities",
        "score_location", "score_staff",
        "score_value_for_money"
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["review_date"] = pd.to_datetime(df["review_date"], errors="coerce")

    print(f"{len(df)} lignes restantes.")
    return df

# Mapping des fichiers aux fonctions de nettoyage
CLEANING_FUNCTIONS = {
    "hotels.csv": clean_hotels,
    "users.csv": clean_users,
    "reviews.csv": clean_reviews,
}

def download_data() -> None:
    """
    Télécharge le jeu de données depuis KaggleHub et le copie dans data/raw/.
    """
    try:
        dataset_path = kagglehub.dataset_download(KAGGLE_MODEL_SLUG)
        print(f"Dataset téléchargé dans le cache : {dataset_path}")
        for file_name in os.listdir(dataset_path):
            if file_name.endswith(".csv"):
                src = os.path.join(dataset_path, file_name)
                dst = os.path.join(RAW_DATA_PATH, file_name)
                shutil.copy(src, dst)

        print("Téléchargement et copie terminés avec succès !")

    except Exception as e:
        print(f"Erreur lors du téléchargement des données : {e}")

def process_data() -> None:
    """
    Charge, nettoie et sauvegarde chaque fichier CSV.
    """
    for filename in DATA_FILES:
        raw_path = os.path.join(RAW_DATA_PATH, filename)
        cleaned_path = os.path.join(CLEAN_DATA_PATH, filename)

        # 1. Récupération des données brutes
        try:
            print(f"\nChargement du fichier brut : {raw_path}")
            df = pd.read_csv(raw_path)
        except FileNotFoundError:
            print(f"Fichier non trouvé : {raw_path}.")
            continue
        except Exception as e:
            print(f"Erreur lors du chargement de {filename} : {e}")
            continue

        # 2. Nettoyage des données
        print(f"Nettoyage des données...")
        clean_func = CLEANING_FUNCTIONS.get(filename)
        if clean_func:
            df_cleaned = clean_func(df)
        else:
            print(f"Aucune fonction de nettoyage trouvée pour {filename}.")
            df_cleaned = df.copy()

        # 3. Renommage et sauvegarde
        cleaned_name = f"cleaned_{filename}"
        cleaned_path = os.path.join(CLEAN_DATA_PATH, cleaned_name)

        # 4. Sauvegarde des données nettoyées dans un nouveau dossier
        try:
            df_cleaned.to_csv(cleaned_path, index=False)
            print(f"fichier nettoyé sauvegardé : {cleaned_path}")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde de {filename} : {e}")
            
    print("\nProcessus de nettoyage des données terminé.")

# --- Point d'entrée principal ---

if __name__ == "__main__":
    ensure_directories()
    download_data()
    process_data()