"""
Composants pour afficher les cartes géographiques et autres visualisations.
"""
import pandas as pd
import folium
import branca.colormap as cm
from typing import Dict, Tuple
import os


def generer_carte_hotels(dataframes: dict[str, pd.DataFrame]) -> folium.Map | None:
    """
    Génère une carte interactive des hôtels à partir de leurs coordonnées géographiques.
    Les points sont placés en fonction des colonnes 'lat' et 'lon' du fichier hotels.csv.
    Retourne une folium.Map (objet carte interactive).
    """
    df_users = dataframes.get("users.csv")
    df_hotels = dataframes.get("hotels.csv")
    if df_hotels is None:
        print("Erreur : le DataFrame 'hotels.csv' est introuvable.")
        return None

    # Vérifier la présence des colonnes nécessaires
    if "lat" not in df_hotels.columns or "lon" not in df_hotels.columns:
        print("Erreur : les colonnes 'lat' et 'lon' sont requises pour générer la carte.")
        return None

    # --- Comptage visiteurs ---
    if df_users is not None and "id_hotel" in df_users.columns:
        visiteurs_par_hotel = df_users.groupby("id_hotel").size().rename("visitors")
        df_hotels = df_hotels.merge(visiteurs_par_hotel, left_on="id_hotel", right_index=True, how="left")
    else:
        df_hotels["visitors"] = None

    df_hotels["visitors"] = df_hotels["visitors"].fillna(0).astype(int)

    # Nettoyage des coordonnées
    df_hotels["lat"] = pd.to_numeric(df_hotels["lat"], errors="coerce")
    df_hotels["lon"] = pd.to_numeric(df_hotels["lon"], errors="coerce")
    df_valid = df_hotels.dropna(subset=["lat", "lon"])

    if df_valid.empty:
        print("Aucune donnée géographique valide trouvée dans hotels.csv.")
        return None

    # Calcul du centre de la carte
    lat_moy = df_valid["lat"].mean()
    lon_moy = df_valid["lon"].mean()

    # Création de la carte
    carte = folium.Map(location=[lat_moy, lon_moy], zoom_start=3, tiles="OpenStreetMap")

    # Ajout des marqueurs pour chaque hôtel
    for _, row in df_valid.iterrows():
        nom = row.get("hotel_name", "Hôtel sans nom")
        etoiles = row.get("stars", "5")
        pays = row.get("country", "Inconnu")
        visiteurs = int(row.get("visitors", 0))

        popup_content = f"""
        <b>{nom}</b><br>
        {etoiles} étoiles<br>
        📍 {pays}
        <b> {visiteurs}</b> visteurs
        """
        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=popup_content,
            icon=folium.Icon(color="blue", icon="info-sign"),
        ).add_to(carte)

    print(f"Carte générée avec {len(df_valid)} hôtels.")
    return carte

def tracer_carte_utilisateurs(dataframes: dict[str, pd.DataFrame]) -> folium.Map | None:
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
        return None

    if "country" not in df_users.columns:
        print(f"Colonnes disponibles : {list(df_users.columns)}")
        print("Erreur : la colonne 'country' est absente du fichier users.csv.")
        return None

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
        "Viet Nam": "Vietnam",
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
        max_users = user_counts["user_count"].max()
        colormap = cm.LinearColormap(['blue', 'yellow', 'red'], vmin=0, vmax=max_users)
        color = colormap(count)
        #carte.add_child(cm) # ajouter la légende  
        if country in coords:
            lat, lon = coords[country]
            folium.CircleMarker(
                location=[lat, lon],
                radius=6 + (count ** 0.3),
                color=color,
                fill=True,
                fill_color = color,
                fill_opacity=0.6,
                popup=f"{country}: {count} utilisateurs",
            ).add_to(carte)
        else:
            unknown_countries.add(raw_country)

    # Log des pays non reconnus (pour que tu puisses compléter la table coords)
    for c in sorted(unknown_countries):
        print(f"Pays non reconnu (ajouter aux coords si souhaité) : {c}")

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
        print(f"Carte des utilisateurs sauvegardée : {out_path}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde de la carte des utilisateurs : {e}")
    # Retourner la carte (permet son affichage direct via folium.get_root().render())
    return carte
