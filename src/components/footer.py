"""
Footer du dashboard.
"""
from dash import html

def create_footer():
    """Crée le footer du dashboard."""
    return html.Div([
        html.Hr(),
        html.P(
            '© 2025 Hotel Booking Analytics Dashboard | Données Kaggle: International Hotel Booking Analytics',
            style={
                'textAlign': 'center',
                'color': '#999',
                'fontSize': '12px',
                'marginTop': '30px',
                'marginBottom': '10px'
            }
        )
    ])
