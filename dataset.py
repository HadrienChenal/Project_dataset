import pandas as pd
import os
import kagglehub

def telecharger_dataset(nom_dataset: str) -> str:
    """
    Télécharge (ou récupère depuis le cache) un dataset Kaggle via kagglehub.
    Retourne le chemin du dossier contenant les fichiers CSV.
    """
    print(f"Téléchargement ou récupération du dataset '{nom_dataset}'...")
    path = kagglehub.dataset_download(nom_dataset)
    print(f"Dataset disponible dans : {path}")
    return path

def charger_csvs(path: str) -> dict:
    """
    Charge tous les fichiers CSV d’un dossier dans un dictionnaire de DataFrames.
    """
    csv_files = [f for f in os.listdir(path) if f.endswith(".csv")]
    dfs = {}
    for csv_file in csv_files:
        csv_path = os.path.join(path, csv_file)
        dfs[csv_file] = pd.read_csv(csv_path)
        print(f"Chargé : {csv_file} ({dfs[csv_file].shape[0]} lignes, {dfs[csv_file].shape[1]} colonnes)")
    return dfs

def _auto_convert_dates(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """
    Tente de convertir les colonnes object en datetime si la proportion de valeurs converties
    dépasse `threshold` (ex : 0.5 = 50%).
    """
    for col in df.select_dtypes(include=["object"]).columns:
        parsed = pd.to_datetime(df[col], errors="coerce", format="%Y-%m-%d")
        non_null_parsed = parsed.notna().sum()
        if non_null_parsed > 0 and (non_null_parsed / len(df)) >= threshold:
            df[col] = parsed
            print(f"Colonne convertie en datetime : {col} ({non_null_parsed}/{len(df)} valeurs)")
    return df

def analyser_dataset(dfs: dict):
    """
    Analyse chaque DataFrame : aperçu, statistics, valeurs manquantes, types, conversions date.
    Utilise un describe() sans arguments incompatibles pour assurer la compatibilité pandas.
    """
    for name, df in dfs.items():
        print(f"\n=== {name} ===")
        print("\nAperçu des 5 premières lignes :")
        print(df.head())

        # Tentative de conversion automatique des dates
        df = _auto_convert_dates(df, threshold=0.5)

        # Describe pour numériques
        print("\nStatistiques descriptives (numériques) :")
        try:
            print(df.describe(include=["number"]))
        except Exception as e:
            print(f"Impossible d'obtenir describe() numériques : {e}")

        # Describe pour objets/catégoriques/datetimes
        print("\nStatistiques descriptives (non-numériques) :")
        try:
            print(df.describe(include=["object", "category", "datetime"]))
        except Exception as e:
            # fallback : simple describe()
            try:
                print(df.describe(include="all"))
            except Exception as e2:
                print(f"Impossible d'obtenir describe() non-numériques : {e2}")

        # Valeurs manquantes et types
        print("\nValeurs manquantes par colonne :")
        print(df.isna().sum())
        print("\nTypes de données :")
        print(df.dtypes)
        print("\n" + "-" * 60)

if __name__ == "__main__":
    dataset_nom = "alperenmyung/international-hotel-booking-analytics"
    chemin = telecharger_dataset(dataset_nom)
    dataframes = charger_csvs(chemin)
    analyser_dataset(dataframes)