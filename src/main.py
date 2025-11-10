import matplotlib.pyplot as plt
import pandas as pd
from utils.get_data import telecharger_dataset, charger_csvs
import numpy as np

def tracer_histogramme_notes(dataframes: dict[str, pd.DataFrame]) -> None:
    """
    Trace un histogramme des notes globales des hôtels
    avec alignement précis des barres et ticks réguliers de 0.1.
    """
    
    df_reviews = dataframes.get("reviews.csv")
    if df_reviews is None:
        print("Erreur : le DataFrame 'reviews.csv' est introuvable.")
        return

    # Nettoyage
    df_reviews["score_overall"] = pd.to_numeric(df_reviews["score_overall"], errors="coerce")
    df_reviews = df_reviews.dropna(subset=["score_overall"])

    # Définir bornes des bins arrondies au dixième
    min_score = np.floor(df_reviews["score_overall"].min() * 10) / 10
    max_score = np.ceil(df_reviews["score_overall"].max() * 10) / 10

    # Création des bins par pas de 0.1 (donc parfaitement alignés)
    bins = np.arange(min_score, max_score + 0.1, 0.1)

    # Tracé de l'histogramme
    plt.figure(figsize=(10, 6))
    n, bins, patches = plt.hist(df_reviews["score_overall"], bins=bins, edgecolor="black", alpha=0.7)

    plt.title("Répartition des notes globales des hôtels")
    plt.xlabel("Score global")
    plt.ylabel("Nombre de clients")
    plt.grid(True, linestyle="--", alpha=0.5)

    # Ticks placés exactement sur les limites des bins
    plt.xticks(bins, rotation=45)

    # Ajustement des marges
    plt.xlim(min_score, max_score)
    plt.tight_layout()

    plt.show()

def tracer_histogramme_score_base(dataframes: dict[str, "pd.DataFrame"]) -> None:
    """
    Trace un histogramme de la distribution du score de base moyen par hôtel,
    avec des ticks réguliers de 0.1 et alignement parfait des barres.
    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

    # Récupération du DataFrame des hôtels
    df_hotels = dataframes.get("hotels.csv")
    if df_hotels is None:
        print("Erreur : le DataFrame 'hotels.csv' est introuvable.")
        return

    # Colonnes nécessaires
    colonnes_bases = ["cleanliness_base", "comfort_base", "facilities_base"]
    for col in colonnes_bases:
        if col not in df_hotels.columns:
            print(f"Erreur : la colonne '{col}' est absente du fichier hotels.csv.")
            return

    # Conversion numérique et calcul du score moyen
    for col in colonnes_bases:
        df_hotels[col] = pd.to_numeric(df_hotels[col], errors="coerce")

    df_hotels["base_score_mean"] = df_hotels[colonnes_bases].mean(axis=1, skipna=True)
    df_valid = df_hotels.dropna(subset=["base_score_mean"])

    # Détermination des bornes arrondies
    min_score = np.floor(df_valid["base_score_mean"].min() * 10) / 10
    max_score = np.ceil(df_valid["base_score_mean"].max() * 10) / 10
    bins = np.arange(min_score, max_score + 0.1, 0.1)

    # Tracé
    plt.figure(figsize=(10, 6))
    n, bins, patches = plt.hist(df_valid["base_score_mean"], bins=bins,
    edgecolor="black", alpha=0.75, color="steelblue")

    plt.title("Distribution du score de base moyen par hôtel")
    plt.xlabel("Score de base moyen")
    plt.ylabel("Nombre d'hôtels")
    plt.grid(True, linestyle="--", alpha=0.5)

    # Ticks et limites ajustés
    plt.xticks(bins, rotation=45)
    plt.xlim(min_score, max_score)
    plt.tight_layout()
    plt.show()


def tracer_histogramme_proprete(dataframes: dict[str, pd.DataFrame]) -> None:
    """
    Trace un histogramme de la répartition des notes de propreté des hôtels,
    avec ticks réguliers de 0.1 et alignement précis des barres.
    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

    df_reviews = dataframes.get("reviews.csv")
    if df_reviews is None:
        print("Erreur : le DataFrame 'reviews.csv' est introuvable.")
        return

    # Conversion et nettoyage
    df_reviews["score_cleanliness"] = pd.to_numeric(df_reviews["score_cleanliness"], errors="coerce")
    df_reviews = df_reviews.dropna(subset=["score_cleanliness"])

    # Détermination des bornes arrondies
    min_score = np.floor(df_reviews["score_cleanliness"].min() * 10) / 10
    max_score = np.ceil(df_reviews["score_cleanliness"].max() * 10) / 10
    bins = np.arange(min_score, max_score + 0.1, 0.1)

    # Tracé
    plt.figure(figsize=(10, 6))
    n, bins, patches = plt.hist(df_reviews["score_cleanliness"], bins=bins,
    color="orange", edgecolor="black", alpha=0.7)

    plt.title("Répartition des notes de propreté des hôtels")
    plt.xlabel("Score de propreté")
    plt.ylabel("Nombre de clients")
    plt.grid(True, linestyle="--", alpha=0.5)

    # Ticks et limites alignés sur les bins
    plt.xticks(bins, rotation=45)
    plt.xlim(min_score, max_score)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Télécharger le dataset
    chemin = telecharger_dataset("alperenmyung/international-hotel-booking-analytics")

    # Charger tous les CSV
    dataframes = charger_csvs(chemin)

    # Histogramme 1 : notes globales
    tracer_histogramme_notes(dataframes)

    # Histogramme 2 : répartition des scores de base
    tracer_histogramme_score_base(dataframes)

    # Histogramme 3 : répartition des notes de propreté
    tracer_histogramme_proprete(dataframes)