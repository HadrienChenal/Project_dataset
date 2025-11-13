"""
Page d'analyses - histogrammes et statistiques.
"""
from dash import html, dcc
from src.components.histogrammes import (
    tracer_histogramme_notes,
    tracer_histogramme_proprete,
)

def layout(dataframes: dict):
    """Crée la page d'analyses."""
    
    # Appels sécurisés pour générer les graphiques Plotly
    hist_notes = tracer_histogramme_notes(dataframes)
    hist_notes_component = dcc.Graph(figure=hist_notes, style={'height': '500px'}) if hist_notes else html.P("❌ Impossible d'afficher l'histogramme des notes globales.")

    hist_proprete = tracer_histogramme_proprete(dataframes)
    hist_proprete_component = dcc.Graph(figure=hist_proprete, style={'height': '500px'}) if hist_proprete else html.P("❌ Impossible d'afficher l'histogramme de la propreté.")

    # Construction du layout
    return html.Div([
        html.H2('Analyses détaillées', style={'marginTop': '20px'}),
        
        html.Div([
            html.Div([
                html.H3('Notes globales'),
                hist_notes_component
            ], style={'flex': '1', 'margin': '10px'}),
        ], style={'display': 'flex', 'flexWrap': 'wrap'}),

        html.Div([
            html.Div([
                html.H3('Scores de propreté'),
                hist_proprete_component
            ], style={'flex': '1', 'margin': '10px'}),
        ], style={'display': 'flex', 'flexWrap': 'wrap'}),
        
    ], style={'padding': '20px'})

