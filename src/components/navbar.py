"""
Composant Navbar pour la navigation Dash.
Permet de naviguer entre les pages du dashboard.
"""
from dash import html, dcc

from dash import html, dcc

def create_navbar():
    """Crée une barre de navigation stylisée et centrée."""
    return html.Div([
        dcc.Location(id='url', refresh=False),
        # Import de la police Google Fonts
        html.Link(
            href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap",
            rel="stylesheet"
        ),
        html.Div([
            html.A('Accueil', href='/', className='nav-link', style={'textDecoration': 'none',  'color': 'black'}),
            html.A('Analyses', href='/analytics', className='nav-link', style={'textDecoration': 'none',  'color': 'black'}),
            html.A('Cartes', href='/maps', className='nav-link', style={'textDecoration': 'none',  'color': 'black'}),
        ], style={
            'padding': '15px 20px',
            'backgroundColor': "#ffffff",
            'borderBottom': '1px solid #ddd',
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center',
            'fontFamily': "'Poppins', sans-serif",
            'gap': '20px'
        }),
    ])
