import os
import matplotlib
# Utiliser un backend non-interactif pour générer des PNG fiables même en environnement headless
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from utils.get_data import charger_csvs
from utils.common_functions import telecharger_dataset

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

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df_reviews["score_overall"], bins=20, edgecolor="black", alpha=0.7)
    ax.set_title("Répartition des notes globales des hôtels")
    ax.set_xlabel("Score global")
    ax.set_ylabel("Nombre de clients")
    ax.grid(True, linestyle="--", alpha=0.5)

    # Sauvegarder la figure dans outputs/figures pour inspection
    try:
        out_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), "outputs", "figures")
        os.makedirs(out_dir, exist_ok=True)
        fig.tight_layout()
        out_path = os.path.join(out_dir, "hist_scores_globales.png")
        fig.savefig(out_path, bbox_inches="tight")
        print(f"Saved: {out_path}")
    except Exception as e:
        print(f"Warning: impossible de sauver hist_scores_globales.png: {e}")
    finally:
        plt.close(fig)

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
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df_valid["base_score_mean"], bins=20, edgecolor="black", alpha=0.75, color="steelblue")
    ax.set_title("Distribution du score de base moyen par hôtel")
    ax.set_xlabel("Score de base moyen")
    ax.set_ylabel("Nombre d'hôtels")
    ax.grid(True, linestyle="--", alpha=0.5)

    # Sauvegarder la figure
    try:
        out_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), "outputs", "figures")
        os.makedirs(out_dir, exist_ok=True)
        fig.tight_layout()
        out_path = os.path.join(out_dir, "hist_scores_base.png")
        fig.savefig(out_path, bbox_inches="tight")
        print(f"Saved: {out_path}")
    except Exception as e:
        print(f"Warning: impossible de sauver hist_scores_base.png: {e}")
    finally:
        plt.close(fig)

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

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df_reviews["score_cleanliness"], bins=20, color="orange", edgecolor="black", alpha=0.7)
    ax.set_title("Répartition des notes de propreté des hôtels")
    ax.set_xlabel("Score de propreté")
    ax.set_ylabel("Nombre de clients")
    ax.grid(True, linestyle="--", alpha=0.5)

    # Sauvegarder la figure
    try:
        out_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), "outputs", "figures")
        os.makedirs(out_dir, exist_ok=True)
        fig.tight_layout()
        out_path = os.path.join(out_dir, "hist_proprete.png")
        fig.savefig(out_path, bbox_inches="tight")
        print(f"Saved: {out_path}")
    except Exception as e:
        print(f"Warning: impossible de sauver hist_proprete.png: {e}")
    finally:
        plt.close(fig)

if __name__ == "__main__":
    # Télécharger le dataset (ou utiliser les CSV locaux si présents)
    chemin = telecharger_dataset("alperenmyung/international-hotel-booking-analytics")

    # Charger tous les CSV
    dataframes = charger_csvs(chemin)

    # Dossier de sortie pour les figures (utile si l'affichage interactif ne s'ouvre pas)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    output_dir = os.path.join(project_root, "outputs", "figures")
    os.makedirs(output_dir, exist_ok=True)

    # Diagnostic : backend matplotlib et clés chargées
    print(f"Matplotlib backend: {plt.get_backend()}")
    print(f"Fichiers chargés: {list(dataframes.keys())}")

    # Histogramme 1 : notes globales
    tracer_histogramme_notes(dataframes)

    # Histogramme 2 : répartition des scores de base
    tracer_histogramme_score_base(dataframes)

    # Histogramme 3 : répartition des notes de propreté
    tracer_histogramme_proprete(dataframes)