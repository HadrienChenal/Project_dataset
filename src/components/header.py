"""
Composant Header pour le dashboard Dash.
Affiche le titre principal et la description.
"""
from dash import html

def create_header():
    """Crée le header du dashboard."""
    return html.Div([
        html.H1(
            'International Hotel Booking Analytics',
            style={
                'textAlign': 'center',
                'marginBottom': '10px',
                'color': '#1f77b4'
            }
        ),
        html.P(
            'Analyse interactive des réservations, annulations, revenus et segments de marché',
            style={
                'textAlign': 'center',
                'fontSize': '16px',
                'color': '#666',
                'marginBottom': '30px'
            }
        ),
    ], style={'paddingTop': '20px', 'paddingBottom': '20px', 'borderBottom': '1px solid #ddd'})
