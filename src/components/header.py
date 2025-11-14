"""
Composant Header pour le dashboard Dash.
Affiche le titre principal et la description.
"""
from dash import html

def create_header():
    """Crée le header du dashboard."""
    return html.Div([

        # --- Titre principal ---
        html.H1(
            "International Hotel Booking Analytics",
            style={
                'textAlign': 'center',
                'marginTop': '30px',
                'color': '#333',
                'fontFamily': 'Arial, sans-serif',
                'fontWeight': 'bold',
                'fontSize': '36px'
            }
        ),

        # --- Sous-titre / phrase d'accroche ---
        html.P(
            "Un projet d’analyse des réservations hôtelières internationales pour comprendre "
            "les comportements des voyageurs et les dynamiques du tourisme mondial.",
            style={
                'textAlign': 'center',
                'maxWidth': '850px',
                'margin': '15px auto',
                'color': '#555',
                'fontSize': '18px',
                'lineHeight': '1.5'
            }
        ),

        # --- Ligne de séparation ---
        html.Hr(style={
            'width': '55%',
            'margin': '25px auto',
            'borderColor': '#ddd'
        })
    ])
