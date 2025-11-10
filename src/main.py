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

def tracer_histogramme_score_base(dataframes: dict[str, "pd.DataFrame"]) -> None:
    """
    Trace un histogramme de la distribution du score de base moyen par hôtel.
    Le score de base moyen est calculé comme la moyenne des colonnes de base présentes
    dans hotels.csv (par exemple cleanliness_base, comfort_base, facilities_base).
    """
    # Récupération du DataFrame des hôtels
    df_hotels = dataframes.get("hotels.csv")
    if df_hotels is None:
        print("Erreur : le DataFrame 'hotels.csv' est introuvable.")
        return

    # Vérification des colonnes nécessaires
    colonnes_bases = ["cleanliness_base", "comfort_base", "facilities_base"]
    for col in colonnes_bases:
        if col not in df_hotels.columns:
            print(f"Erreur : la colonne '{col}' est absente du fichier hotels.csv.")
            return

    # Conversion en numérique et calcul du score moyen
    for col in colonnes_bases:
        df_hotels[col] = pd.to_numeric(df_hotels[col], errors="coerce")

    df_hotels["base_score_mean"] = df_hotels[colonnes_bases].mean(axis=1, skipna=True)

    # Suppression des valeurs manquantes
    df_valid = df_hotels.dropna(subset=["base_score_mean"])

    # Tracé de l'histogramme
    plt.figure(figsize=(10, 6))
    plt.hist(df_valid["base_score_mean"], bins=20, edgecolor="black", alpha=0.75, color="steelblue")
    plt.title("Distribution du score de base moyen par hôtel")
    plt.xlabel("Score de base moyen")
    plt.ylabel("Nombre d'hôtels")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()

def tracer_histogramme_proprete(dataframes: dict[str, pd.DataFrame]) -> None:
    """
    Trace un histogramme de la répartition des notes de propreté des hôtels.
    Permet de visualiser la perception de la propreté dans l'ensemble des avis.
    """
    df_reviews = dataframes.get("reviews.csv")
    if df_reviews is None:
        print("Erreur : le DataFrame 'reviews.csv' est introuvable.")
        return

    # Conversion et nettoyage
    df_reviews["score_cleanliness"] = pd.to_numeric(df_reviews["score_cleanliness"], errors="coerce")
    df_reviews = df_reviews.dropna(subset=["score_cleanliness"])

    plt.figure(figsize=(10, 6))
    plt.hist(df_reviews["score_cleanliness"], bins=20, color="orange", edgecolor="black", alpha=0.7)
    plt.title("Répartition des notes de propreté des hôtels")
    plt.xlabel("Score de propreté")
    plt.ylabel("Nombre de clients")
    plt.grid(True, linestyle="--", alpha=0.5)
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