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



if __name__ == "__main__":
    # Télécharger le dataset
    chemin = telecharger_dataset("alperenmyung/international-hotel-booking-analytics")

    # Charger tous les CSV
    dataframes = charger_csvs(chemin)

    # Tracer le premier histogramme
    tracer_histogramme_notes(dataframes)