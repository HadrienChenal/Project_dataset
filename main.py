import matplotlib.pyplot as plt
import pandas as pd
from utils.get_data import telecharger_dataset, charger_csvs

def tracer_histogramme_notes(dataframes: dict[str, pd.DataFrame]) -> None:
    """
    Trace un histogramme de la répartition des notes globales des hôtels.
    """
    # Clé correcte pour accéder aux reviews
    df_reviews = dataframes.get("reviews.csv")
    if df_reviews is None:
        print("Erreur : le DataFrame 'reviews.csv' est introuvable.")
        return

    # Nettoyage et affichage
    df_reviews["score_overall"] = pd.to_numeric(df_reviews["score_overall"], errors="coerce")
    df_reviews = df_reviews.dropna(subset=["score_overall"])

    plt.figure(figsize=(10, 6))
    plt.hist(df_reviews["score_overall"], bins=20, edgecolor="black", alpha=0.7)
    plt.title("Répartition des notes globales des hôtels")
    plt.xlabel("Score global")
    plt.ylabel("Nombre de clients")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()

if __name__ == "__main__":
    # Télécharger le dataset
    chemin = telecharger_dataset("alperenmyung/international-hotel-booking-analytics")

    # Charger tous les CSV
    dataframes = charger_csvs(chemin)

    # Tracer le premier histogramme
    tracer_histogramme_notes(dataframes)