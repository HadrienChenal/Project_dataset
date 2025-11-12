"""
Page avancée - Carte géographique des hôtels.
"""
from dash import html, dcc
from src.components.component2 import generer_carte_hotels


def layout(dataframes: dict):
    """Crée la page avancée avec la carte."""
    
    # Générer la carte Folium
    carte = generer_carte_hotels(dataframes)
    
    if carte is None:
        carte_component = html.Div([
            html.P("❌ Impossible de générer la carte."),
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
            print("✅ Carte Folium générée et affichée avec succès.")
        except Exception as e:
            carte_component = html.Div([
                html.P(f"❌ Erreur lors de l'affichage de la carte : {e}"),
                html.P("Vérifiez que folium est correctement installé.")
            ])
    
    return html.Div([
        html.H2('Carte Géographique des Hôtels', style={'marginTop': '20px'}),
        
        html.Div([
            html.P("Explorez la localisation géographique de tous les hôtels du dataset. "
                   "Cliquez sur les marqueurs pour voir les détails (nom, étoiles, pays).")
        ], style={'padding': '10px', 'backgroundColor': '#f0f0f0', 'borderRadius': '8px', 'marginBottom': '20px'}),
        
        html.Div([
            carte_component
        ], style={'marginBottom': '30px'}),
        
    ], style={'padding': '20px'})
