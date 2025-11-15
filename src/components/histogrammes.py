"""
Composants pour afficher les histogrammes du dashboard.
Utilise Plotly pour générer des graphiques interactifs.
"""
import pandas as pd
import plotly.graph_objects as go

def tracer_histogramme_notes(dataframes: dict[str, pd.DataFrame]) -> go.Figure | None:
    """
    Trace un histogramme interactif de la répartition des notes globales des hôtels.
    Retourne une Figure Plotly.
    """
    df_reviews = dataframes.get("reviews.csv")
    if df_reviews is None:
        print("Erreur : le DataFrame 'reviews.csv' est introuvable.")
        return None

    df_reviews["score_overall"] = pd.to_numeric(df_reviews["score_overall"], errors="coerce")
    df_reviews = df_reviews.dropna(subset=["score_overall"])

    if df_reviews.empty:
        print("Aucune donnée valide pour score_overall.")
        return None

    # Création de l'histogramme Plotly
    fig = go.Figure(data=[
        go.Histogram(
            x=df_reviews["score_overall"],
            nbinsx=20,
            marker=dict(color="steelblue", line=dict(color="black", width=1)),
            opacity=0.7,
            name="Nombre de clients"
        )
    ])

    fig.update_layout(
        title="Répartition des notes globales des hôtels",
        xaxis_title="Score global",
        yaxis_title="Nombre de clients",
        hovermode="x unified",
        template="plotly_white",
        height=500
    )

    return fig


def tracer_histogramme_score_base(dataframes: dict[str, pd.DataFrame]) -> go.Figure | None:
    """
    Trace un histogramme interactif de la distribution du score de base moyen par hôtel.
    Retourne une Figure Plotly.
    """
    df_hotels = dataframes.get("hotels.csv")
    if df_hotels is None:
        print("Erreur : le DataFrame 'hotels.csv' est introuvable.")
        return None

    colonnes_bases = ["cleanliness_base", "comfort_base", "facilities_base"]
    for col in colonnes_bases:
        if col not in df_hotels.columns:
            print(f"Erreur : la colonne '{col}' est absente du fichier hotels.csv.")
            return None

    for col in colonnes_bases:
        df_hotels[col] = pd.to_numeric(df_hotels[col], errors="coerce")

    df_hotels["base_score_mean"] = df_hotels[colonnes_bases].mean(axis=1, skipna=True)
    df_valid = df_hotels.dropna(subset=["base_score_mean"])
    
    if df_valid.empty:
        print("Aucune valeur valide pour 'base_score_mean'.")
        return None

    # Création de l'histogramme Plotly
    fig = go.Figure(data=[
        go.Histogram(
            x=df_valid["base_score_mean"],
            nbinsx=20,
            marker=dict(color="lightblue", line=dict(color="steelblue", width=1)),
            opacity=0.8,
            name="Nombre d'hôtels"
        )
    ])

    fig.update_layout(
        title="Distribution du score de base moyen par hôtel",
        xaxis_title="Score de base moyen",
        yaxis_title="Nombre d'hôtels",
        hovermode="x unified",
        template="plotly_white",
        height=500
    )

    return fig


def tracer_histogramme_proprete(dataframes: dict[str, pd.DataFrame]) -> go.Figure | None:
    """
    Trace un histogramme interactif de la répartition des notes de propreté des hôtels.
    Retourne une Figure Plotly.
    """
    df_reviews = dataframes.get("reviews.csv")
    if df_reviews is None:
        print("Erreur : le DataFrame 'reviews.csv' est introuvable.")
        return None

    df_reviews["score_cleanliness"] = pd.to_numeric(df_reviews["score_cleanliness"], errors="coerce")
    df_reviews = df_reviews.dropna(subset=["score_cleanliness"])

    if df_reviews.empty:
        print("Aucune donnée valide pour score_cleanliness.")
        return None

    fig = go.Figure(data=[
        go.Histogram(
            x=df_reviews["score_cleanliness"],
            nbinsx=20,
            marker=dict(color="mediumseagreen", line=dict(color="darkgreen", width=1)),
            opacity=0.75,
            name="Nombre de clients"
        )
    ])

    fig.update_layout(
        title="Répartition des notes de propreté",
        xaxis_title="Score propreté",
        yaxis_title="Nombre de clients",
        hovermode="x unified",
        template="plotly_white",
        height=500
    )

    return fig


def tracer_histogramme_confort(dataframes: dict[str, pd.DataFrame]) -> go.Figure | None:
    """
    Trace un histogramme interactif de la répartition des notes de confort des hôtels.
    Retourne une Figure Plotly.
    """
    df_reviews = dataframes.get("reviews.csv")
    if df_reviews is None:
        print("Erreur : le DataFrame 'reviews.csv' est introuvable.")
        return None

    df_reviews["score_comfort"] = pd.to_numeric(df_reviews["score_comfort"], errors="coerce")
    df_reviews = df_reviews.dropna(subset=["score_comfort"]) 
    if df_reviews.empty:
        print("Aucune donnée valide pour score_comfort.")
        return None

    fig = go.Figure(data=[
        go.Histogram(
            x=df_reviews["score_comfort"],
            nbinsx=20,
            marker=dict(color="teal", line=dict(color="black", width=1)),
            opacity=0.75,
            name="Nombre de clients"
        )
    ])

    fig.update_layout(
        title="Répartition des notes de confort",
        xaxis_title="Score confort",
        yaxis_title="Nombre de clients",
        hovermode="x unified",
        template="plotly_white",
        height=500
    )

    return fig


def tracer_histogramme_installations(dataframes: dict[str, pd.DataFrame]) -> go.Figure | None:
    """
    Trace un histogramme interactif de la répartition des notes des installations.
    Retourne une Figure Plotly.
    """
    df_reviews = dataframes.get("reviews.csv")
    if df_reviews is None:
        print("Erreur : le DataFrame 'reviews.csv' est introuvable.")
        return None

    df_reviews["score_facilities"] = pd.to_numeric(df_reviews["score_facilities"], errors="coerce")
    df_reviews = df_reviews.dropna(subset=["score_facilities"]) 
    if df_reviews.empty:
        print("Aucune donnée valide pour score_facilities.")
        return None

    fig = go.Figure(data=[
        go.Histogram(
            x=df_reviews["score_facilities"],
            nbinsx=20,
            marker=dict(color="mediumpurple", line=dict(color="black", width=1)),
            opacity=0.75,
            name="Nombre de clients"
        )
    ])

    fig.update_layout(
        title="Répartition des notes des installations",
        xaxis_title="Score installations",
        yaxis_title="Nombre de clients",
        hovermode="x unified",
        template="plotly_white",
        height=500
    )

    return fig


def tracer_histogramme_emplacement(dataframes: dict[str, pd.DataFrame]) -> go.Figure | None:
    """
    Trace un histogramme interactif de la répartition des notes d'emplacement.
    Retourne une Figure Plotly.
    """
    df_reviews = dataframes.get("reviews.csv")
    if df_reviews is None:
        print("Erreur : le DataFrame 'reviews.csv' est introuvable.")
        return None

    df_reviews["score_location"] = pd.to_numeric(df_reviews["score_location"], errors="coerce")
    df_reviews = df_reviews.dropna(subset=["score_location"]) 
    if df_reviews.empty:
        print("Aucune donnée valide pour score_location.")
        return None

    fig = go.Figure(data=[
        go.Histogram(
            x=df_reviews["score_location"],
            nbinsx=20,
            marker=dict(color="coral", line=dict(color="black", width=1)),
            opacity=0.75,
            name="Nombre de clients"
        )
    ])

    fig.update_layout(
        title="Répartition des notes d'emplacement",
        xaxis_title="Score emplacement",
        yaxis_title="Nombre de clients",
        hovermode="x unified",
        template="plotly_white",
        height=500
    )

    return fig
