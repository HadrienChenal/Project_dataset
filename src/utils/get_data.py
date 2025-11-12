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
        # Lire le CSV
        df = pd.read_csv(csv_path)
        # Normaliser la clé : si les fichiers sont préfixés par 'cleaned_'
        # on expose la version sans préfixe pour correspondre aux clés
        # attendues (par ex. 'reviews.csv', 'hotels.csv').
        key = csv_file
        if csv_file.startswith("cleaned_"):
            key = csv_file[len("cleaned_"):]
        dfs[key] = df
<<<<<<< HEAD
    return dfs

=======
    return dfs
>>>>>>> main
