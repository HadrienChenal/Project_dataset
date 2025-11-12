"""
Composants pour afficher les cartes géographiques et autres visualisations.
"""
import pandas as pd
import folium


def generer_carte_hotels(dataframes: dict[str, pd.DataFrame]) -> folium.Map | None:
    """
    Génère une carte interactive des hôtels à partir de leurs coordonnées géographiques.
    Les points sont placés en fonction des colonnes 'lat' et 'lon' du fichier hotels.csv.
    Retourne une folium.Map (objet carte interactive).
    """
    df_hotels = dataframes.get("hotels.csv")
    if df_hotels is None:
        print("Erreur : le DataFrame 'hotels.csv' est introuvable.")
        return None

    # Vérifier la présence des colonnes nécessaires
    if "lat" not in df_hotels.columns or "lon" not in df_hotels.columns:
        print("Erreur : les colonnes 'lat' et 'lon' sont requises pour générer la carte.")
        return None

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

    print(f"Carte générée avec {len(df_valid)} hôtels.")
    return carte
