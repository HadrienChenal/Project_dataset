import os
import matplotlib
# Utiliser un backend non-interactif pour générer des PNG fiables même en environnement headless
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import folium
import plotly.express as px
from typing import Dict, Tuple
from utils.get_data import charger_csvs
from utils.common_functions import telecharger_dataset
import numpy as np

def tracer_histogramme_notes(dataframes: dict[str, pd.DataFrame]) -> None:
    """
    Trace un histogramme de la répartition des notes globales des hôtels.
    """
     # Données
    df_reviews = dataframes.get("reviews.csv")
    if df_reviews is None:
        print("Erreur : le DataFrame 'reviews.csv' est introuvable.")
        return

    df_reviews["score_overall"] = pd.to_numeric(df_reviews["score_overall"], errors="coerce")
    df_reviews = df_reviews.dropna(subset=["score_overall"])

    # Bornes arrondies au dixième et bins réguliers de 0.1
    min_score = np.floor(df_reviews["score_overall"].min() * 10) / 10
    max_score = np.ceil(df_reviews["score_overall"].max() * 10) / 10
    bins = np.arange(min_score, max_score + 0.1, 0.1)

    # Tracé
    fig, ax = plt.subplots(figsize=(10, 6))
    n, bins_used, patches = ax.hist(df_reviews["score_overall"], bins=bins,
                                    edgecolor="black", alpha=0.7)

    ax.set_title("Répartition des notes globales des hôtels")
    ax.set_xlabel("Score global")
    ax.set_ylabel("Nombre de clients")
    ax.grid(True, linestyle="--", alpha=0.5)

    # Ticks alignés sur les limites des barres + limites x propres
    ax.set_xticks(bins)
    ax.tick_params(axis="x", labelrotation=45)
    ax.set_xlim(min_score, max_score)

    # Sauvegarde (inchangée)
    try:
        out_dir = os.path.join(
            os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
            "outputs", "figures"
        )
        os.makedirs(out_dir, exist_ok=True)
        fig.tight_layout()
        out_path = os.path.join(out_dir, "hist_scores_globales.png")
        fig.savefig(out_path, bbox_inches="tight")
        print(f"Saved: {out_path}")
    except Exception as e:
        print(f"Warning: impossible de sauver hist_scores_globales.png: {e}")
    finally:
        plt.close(fig)

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

    colonnes_bases = ["cleanliness_base", "comfort_base", "facilities_base"]
    for col in colonnes_bases:
        if col not in df_hotels.columns:
            print(f"Erreur : la colonne '{col}' est absente du fichier hotels.csv.")
            return

    for col in colonnes_bases:
        df_hotels[col] = pd.to_numeric(df_hotels[col], errors="coerce")

    df_hotels["base_score_mean"] = df_hotels[colonnes_bases].mean(axis=1, skipna=True)
    df_valid = df_hotels.dropna(subset=["base_score_mean"])
    if df_valid.empty:
        print("Aucune valeur valide pour 'base_score_mean'.")
        return

    # Définition des bornes et bins à pas de 0.1
    min_score = np.floor(df_valid["base_score_mean"].min() * 10) / 10
    max_score = np.ceil(df_valid["base_score_mean"].max() * 10) / 10
    bins = np.arange(min_score, max_score + 0.1, 0.1)

    # Tracé
    fig, ax = plt.subplots(figsize=(10, 6))
    n, bins_used, patches = ax.hist(df_valid["base_score_mean"], bins=bins,
                                    edgecolor="black", alpha=0.75, color="steelblue")

    ax.set_title("Distribution du score de base moyen par hôtel")
    ax.set_xlabel("Score de base moyen")
    ax.set_ylabel("Nombre d'hôtels")
    ax.grid(True, linestyle="--", alpha=0.5)

    # Ticks alignés sur les limites des barres, arrondis au dixième
    ax.set_xticks(bins)
    ax.set_xticklabels([f"{b:.1f}" for b in bins])
    ax.tick_params(axis="x", labelrotation=45)
    ax.set_xlim(min_score, max_score)

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
    # Données 
    df_reviews = dataframes.get("reviews.csv")
    if df_reviews is None:
        print("Erreur : le DataFrame 'reviews.csv' est introuvable.")
        return

    df_reviews["score_cleanliness"] = pd.to_numeric(df_reviews["score_cleanliness"], errors="coerce")
    df_reviews = df_reviews.dropna(subset=["score_cleanliness"])
    if df_reviews.empty:
        print("Aucune valeur valide pour 'score_cleanliness'.")
        return

    # Définition des bornes et bins à pas de 0.1
    min_score = np.floor(df_reviews["score_cleanliness"].min() * 10) / 10
    max_score = np.ceil(df_reviews["score_cleanliness"].max() * 10) / 10
    bins = np.arange(min_score, max_score + 0.1, 0.1)

    # Tracé
    fig, ax = plt.subplots(figsize=(10, 6))
    n, bins_used, patches = ax.hist(df_reviews["score_cleanliness"], bins=bins,
                                    color="orange", edgecolor="black", alpha=0.7)

    ax.set_title("Répartition des notes de propreté des hôtels")
    ax.set_xlabel("Score de propreté")
    ax.set_ylabel("Nombre de clients")
    ax.grid(True, linestyle="--", alpha=0.5)

    # Ticks alignés sur les limites des barres, arrondis au dixième
    ax.set_xticks(bins)
    ax.set_xticklabels([f"{b:.1f}" for b in bins])
    ax.tick_params(axis="x", labelrotation=45)
    ax.set_xlim(min_score, max_score)

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


def generer_carte_hotels(dataframes: dict[str, pd.DataFrame]) -> None:
    """
    Génère une carte interactive des hôtels à partir de leurs coordonnées géographiques.
    Les points sont placés en fonction des colonnes 'lat' et 'lon' du fichier hotels.csv.
    """
    df_hotels = dataframes.get("hotels.csv")
    if df_hotels is None:
        print("Erreur : le DataFrame 'hotels.csv' est introuvable.")
        return

    # Vérifier la présence des colonnes nécessaires
    if "lat" not in df_hotels.columns or "lon" not in df_hotels.columns:
        print("Erreur : les colonnes 'lat' et 'lon' sont requises pour générer la carte.")
        return

    # Nettoyage des coordonnées
    df_hotels["lat"] = pd.to_numeric(df_hotels["lat"], errors="coerce")
    df_hotels["lon"] = pd.to_numeric(df_hotels["lon"], errors="coerce")
    df_valid = df_hotels.dropna(subset=["lat", "lon"])

    if df_valid.empty:
        print("Aucune donnée géographique valide trouvée dans hotels.csv.")
        return

    # Calcul du centre de la carte
    lat_moy = df_valid["lat"].mean()
    lon_moy = df_valid["lon"].mean()

    # Création de la carte
    carte = folium.Map(location=[lat_moy, lon_moy], zoom_start=3, tiles="OpenStreetMap")

    # Ajout des marqueurs pour chaque hôtel
    for _, row in df_valid.iterrows():
        nom = row.get("hotel_name", "Hôtel sans nom")
        etoiles = row.get("stars", "N/A")
        pays = row.get("country", "Inconnu")

        popup_content = f"""
        <b>{nom}</b><br>
        ⭐ {etoiles} étoiles<br>
        📍 {pays}
        """
        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=popup_content,
            icon=folium.Icon(color="blue", icon="info-sign"),
        ).add_to(carte)

    # Sauvegarde
    try:
        out_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), "outputs", "maps")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "carte_hotels.html")
        carte.save(out_path)
        print(f"Saved: {out_path}")
    except Exception as e:
        print(f"Warning: impossible de sauver carte_hotels.html: {e}")

def tracer_carte_utilisateurs(dataframes: dict[str, pd.DataFrame]) -> None:
    """
    Génère une carte géolocalisée des utilisateurs par pays à partir du fichier users.csv.
    Chaque pays est représenté par un marqueur indiquant le nombre d'utilisateurs.
    La fonction inclut une table de coordonnées étendue et une normalisation des noms de pays.
    Args:
        dataframes (dict[str, pd.DataFrame]): dictionnaire des DataFrames chargés.
    """
    df_users = dataframes.get("users.csv")
    if df_users is None:
        print("Erreur : le DataFrame 'users.csv' est introuvable.")
        return

    if "country" not in df_users.columns:
        print(f"Colonnes disponibles : {list(df_users.columns)}")
        print("Erreur : la colonne 'country' est absente du fichier users.csv.")
        return

    # Normalisation simple des noms (trim + title)
    df_users["country"] = df_users["country"].astype(str).str.strip()

    # Comptage du nombre d'utilisateurs par pays
    user_counts = df_users["country"].dropna().value_counts().reset_index()
    user_counts.columns = ["country", "user_count"]

    print("Aperçu user_counts :")
    print(user_counts.head())

    # Table de coordonnées étendue (latitude, longitude)
    coords: Dict[str, Tuple[float, float]] = {
        "United States": (37.0902, -95.7129),
        "United Kingdom": (55.3781, -3.4360),
        "Germany": (51.1657, 10.4515),
        "China": (35.8617, 104.1954),
        "France": (46.603354, 1.888334),
        "South Korea": (36.6333, 127.7669),
        "Republic of Korea": (36.6333, 127.7669),
        "Korea, South": (36.6333, 127.7669),
        "United Arab Emirates": (23.4241, 53.8478),
        "UAE": (23.4241, 53.8478),
        "Russia": (61.5240, 105.3188),
        "Russian Federation": (61.5240, 105.3188),
        "Mexico": (23.6345, -102.5528),
        "New Zealand": (-40.9006, 174.8860),
        "Argentina": (-38.4161, -63.6167),
        "Thailand": (15.8700, 100.9925),
        "Netherlands": (52.1326, 5.2913),
        "South Africa": (-30.5595, 22.9375),
        "Nigeria": (9.0820, 8.6753),
        "Egypt": (26.8206, 30.8025),
        "Singapore": (1.3521, 103.8198),
        "Canada": (56.1304, -106.3468),
        "Australia": (-25.2744, 133.7751),
        "Japan": (36.2048, 138.2529),
        "India": (20.5937, 78.9629),
        "Brazil": (-14.2350, -51.9253),
        "Spain": (40.4637, -3.7492),
        "Italy": (41.8719, 12.5674),
        "Turkey": (38.9637, 35.2433),
        "Switzerland": (46.8182, 8.2275),
        "Austria": (47.5162, 14.5501),
        "Portugal": (39.3999, -8.2245),
        "Greece": (39.0742, 21.8243),
        # Ajoute d'autres pays si nécessaire...
    }

    # table d'alias pour normaliser les variantes courantes
    alias: Dict[str, str] = {
        "Korea Republic": "South Korea",
        "Korea, Republic of": "South Korea",
        "S. Korea": "South Korea",
        "U.A.E.": "United Arab Emirates",
        "UAE": "United Arab Emirates",
        "U.S.": "United States",
        "USA": "United States",
        "UK": "United Kingdom",
        "England": "United Kingdom",
        "Great Britain": "United Kingdom",
        "Russian Federation": "Russia",
        "Viet Nam": "Vietnam",  # exemple si tu l'ajoutes aux coords
        # Ajouter d'autres alias si nécessaire
    }

    # Création de la carte centrée sur le monde
    carte = folium.Map(location=[20, 0], zoom_start=2)

    # Itération et ajout des marqueurs (avec normalisation)
    unknown_countries = set()
    for _, row in user_counts.iterrows():
        raw_country = str(row["country"]).strip()
        country = alias.get(raw_country, raw_country)  # remplacer via alias si présent
        count = int(row["user_count"])

        if country in coords:
            lat, lon = coords[country]
            folium.CircleMarker(
                location=[lat, lon],
                radius=6 + (count ** 0.3),
                color="blue",
                fill=True,
                fill_opacity=0.6,
                popup=f"{country}: {count} utilisateurs",
            ).add_to(carte)
        else:
            unknown_countries.add(raw_country)

    # Log des pays non reconnus (pour que tu puisses compléter la table coords)
    for c in sorted(unknown_countries):
        print(f"⚠️ Pays non reconnu (ajouter aux coords si souhaité) : {c}")

    # Sauvegarde de la carte
    try:
        out_dir = os.path.join(
            os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
            "outputs",
            "maps",
        )
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "carte_utilisateurs.html")
        carte.save(out_path)
        print(f"✅ Carte des utilisateurs sauvegardée : {out_path}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde de la carte des utilisateurs : {e}")


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

    # Carte géolocalisée des hôtels
    generer_carte_hotels(dataframes)

    # Carte 2 : répartition des utilisateurs par pays
    tracer_carte_utilisateurs(dataframes)