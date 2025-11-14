"""
Page de cartes géographiques.
"""
from dash import html
from src.components.cartes import (
    generer_carte_hotels,
    tracer_carte_utilisateurs,
    
)

def layout(dataframes: dict):
    """Crée la page avancée avec la carte."""
    
    # Générer la carte Folium
    carte = generer_carte_hotels(dataframes)
    carte_utilisateurs = tracer_carte_utilisateurs(dataframes)
    
    if carte is None:
        carte_component = html.Div([
            html.P("Impossible de générer la carte."),
            html.P("Vérifiez que le DataFrame 'hotels.csv' contient les colonnes 'lat' et 'lon'.")
        ])
    else:
        # Convertir la carte Folium en HTML et l'afficher dans un IFrame
        try:
            carte_html = carte.get_root().render()
            carte_component = html.Iframe(
                srcDoc=carte_html,
                style={'width': '100%', 'height': '700px', 'border': 'none'}
            )
            print("Carte Folium générée et affichée avec succès.")
        except Exception as e:
            carte_component = html.Div([
                html.P(f"Erreur lors de l'affichage de la carte : {e}"),
                html.P("Vérifiez que folium est correctement installé.")
            ])
    
    return html.Div([
        html.H2('Carte Géographique des Hôtels', style={'marginTop': '20px'}),
        
        html.Div([
            carte_component
        ], style={'marginBottom': '30px'}),


        html.Div([
            html.H3('Répartition des utilisateurs par pays'),
            html.Iframe(
                srcDoc=carte_utilisateurs.get_root().render() if carte_utilisateurs else "",
                style={'width': '100%', 'height': '700px', 'border': 'none'}
            )
        ], style={'marginBottom': '30px'}),
        
    ], style={'padding': '20px'})