import os
import pandas as pd
from src.utils.common_functions import (
    KAGGLE_MODEL_SLUG,
    CLEAN_DATA_PATH,
    DATA_FILES,
    ensure_directories,
    telecharger_dataset
)

####### CLEANING FUNCTIONS ########

def clean_hotels(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoyage spécifique du tableau hotels.csv.
    param df: DataFrame brut à nettoyer.
    return: DataFrame nettoyé.
    """
    print(f"{len(df)} lignes initiales")
    # Suppression des lignes avec des valeurs manquantes critiques
    df = df.dropna(subset=["hotel_name", "city", "country"])
    # Conversion des colonnes numériques
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
    """
    Nettoyage spécifique du tableau users.csv.
    param df: DataFrame brut à nettoyer.
    return: DataFrame nettoyé.
    """
    print(f"{len(df)} lignes initiales")
    # Suppression des doublons
    df = df.drop_duplicates(subset="user_id")
    # Suppression des lignes avec des valeurs manquantes critiques
    df = df.dropna(subset=["user_id", "country"])
    # Nettoyage des colonnes spécifiques : conversion de types et gestion des valeurs manquantes
    df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce")
    df["user_gender"] = df["user_gender"].str.title().fillna("Unknown")
    df["traveller_type"] = df["traveller_type"].str.title().fillna("Unknown")
    
    print(f"{len(df)} lignes restantes.")
    return df

def clean_reviews(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoyage spécifique du tableau reviews.csv
    param df: DataFrame brut à nettoyer.
    return: DataFrame nettoyé.
    """
    print(f"{len(df)} lignes initiales")
    # Suppression des lignes avec des valeurs manquantes critiques
    df = df.dropna(subset=["review_id", "hotel_id", "user_id", "score_overall"])
    # Conversion des colonnes numériques
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

def process_data() -> None:
    """
    Charge, nettoie et sauvegarde chaque fichier CSV.
    """
    for filename in DATA_FILES:
        cleaned_path = os.path.join(CLEAN_DATA_PATH, filename)

        # 1. Récupération des données brutes
        try:
            print(f"\nChargement du fichier brut")
            # Téléchargement du dataset depuis Kaggle
            path = telecharger_dataset(KAGGLE_MODEL_SLUG)
            df = pd.read_csv(os.path.join(path, filename))
        except FileNotFoundError:
            print(f"Fichier non trouvé.")
            continue
        except Exception as e:
            print(f"Erreur lors du chargement de {filename} : {e}")
            continue

        # 2. Nettoyage des données
        print(f"Nettoyage des données...")
        # Application de la fonction de nettoyage spécifique
        clean_func = CLEANING_FUNCTIONS.get(filename)
        if clean_func:
            df_cleaned = clean_func(df)
        else:
            print(f"Aucune fonction de nettoyage trouvée pour {filename}.")
            df_cleaned = df.copy()

        # 3. Renommage et sauvegarde des fichiers nettoyés dans le dossier cleaned
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
    ensure_directories(CLEAN_DATA_PATH)
    process_data()