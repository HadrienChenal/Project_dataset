"""
Composant Navbar pour la navigation Dash.
Permet de naviguer entre les pages du dashboard.
"""
from dash import html, dcc

def create_navbar():
    """Crée la barre de navigation."""
    return html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div([
            html.Span('Navigation:', style={'marginRight': '20px', 'fontWeight': 'bold'}),
            html.A('Accueil', href='/', style={'marginRight': '20px', 'textDecoration': 'none', 'color': '#1f77b4'}),
            html.A('Analyses', href='/analytics', style={'marginRight': '20px', 'textDecoration': 'none', 'color': '#1f77b4'}),
            html.A('Cartes', href='/maps', style={'marginRight': '20px', 'textDecoration': 'none', 'color': '#1f77b4'}),
        ], style={
            'padding': '15px 20px',
            'backgroundColor': '#f8f9fa',
            'borderBottom': '1px solid #ddd',
            'display': 'flex',
            'alignItems': 'center'
        })
    ])
