"""
Page d'accueil du dashboard.
Affiche un résumé des données et des KPIs.
"""
import pandas as pd
from dash import html, dcc
from src.components.histogrammes import tracer_histogramme_notes, tracer_histogramme_proprete

def layout(dataframes: dict):
    """Crée la page d'accueil."""
    
    # Calcul des KPIs
    total_hotels = len(dataframes.get('hotels.csv', pd.DataFrame()))
    total_reviews = len(dataframes.get('reviews.csv', pd.DataFrame()))
    total_users = len(dataframes.get('users.csv', pd.DataFrame()))
    
    # Générer les graphiques Plotly
    fig_notes = tracer_histogramme_notes(dataframes)
    
    return html.Div([
        html.H2('Bienvenue sur le Dashboard d\'Analyse Hôtelière', style={'marginTop': '20px'}),
        
        html.Div([
            html.Div([
                html.H3('Hôtels'),
                html.H4(f'{total_hotels:,}')
            ], style={
                'flex': '1',
                'textAlign': 'center',
                'padding': '20px',
                'backgroundColor': '#f0f0f0',
                'borderRadius': '8px',
                'margin': '10px'
            }),
            html.Div([
                html.H3('Avis'),
                html.H4(f'{total_reviews:,}')
            ], style={
                'flex': '1',
                'textAlign': 'center',
                'padding': '20px',
                'backgroundColor': '#f0f0f0',
                'borderRadius': '8px',
                'margin': '10px'
            }),
            html.Div([
                html.H3('Utilisateurs'),
                html.H4(f'{total_users:,}')
            ], style={
                'flex': '1',
                'textAlign': 'center',
                'padding': '20px',
                'backgroundColor': '#f0f0f0',
                'borderRadius': '8px',
                'margin': '10px'
            }),
        ], style={'display': 'flex', 'justifyContent': 'space-around', 'marginBottom': '30px'}),
        
        html.Div([
            html.H3('Aperçu : Répartition des notes globales'),
            dcc.Graph(figure=fig_notes, style={'height': '500px'}) if fig_notes else html.P("Impossible de générer le graphique.")
        ], style={'maxWidth': '900px', 'margin': '0 auto'})
    ], style={'padding': '20px'})
