"""
Dashboard Dash - Hotel Booking Analytics
Structure modulaire avec composants et pages réutilisables.

Utilisation:
    python app.py
    Puis ouvrir http://127.0.0.1:8050 dans le navigateur.
"""

import os
import sys
from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd

# Ajouter le répertoire src au path pour les imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from src.components.header import create_header
from src.components.navbar import create_navbar
from src.components.footer import create_footer
from src.pages import home, simple_page, about
from src.utils.get_data import charger_csvs
from src.utils.common_functions import RAW_DATA_PATH

# ---------------------------
# Chargement des données
# ---------------------------

def load_data():
    """Charge les CSV depuis le dossier data/raw."""
    try:
        dataframes = charger_csvs(RAW_DATA_PATH)
        if not dataframes:
            print(f"⚠️  Aucun CSV trouvé dans {RAW_DATA_PATH}. Utilisation du dossier local 'data/'.")
            # Fallback : chercher dans data/ local
            if os.path.exists('data'):
                dataframes = charger_csvs('data')
        return dataframes
    except Exception as e:
        print(f"❌ Erreur lors du chargement des données: {e}")
        return {}

dataframes = load_data()

if not dataframes:
    print("⚠️  Aucune donnée n'a pu être chargée. Assurez-vous que les fichiers CSV sont présents.")
    dataframes = {
        'hotels.csv': pd.DataFrame(),
        'reviews.csv': pd.DataFrame(),
        'users.csv': pd.DataFrame()
    }

# ---------------------------
# Initialisation de l'application Dash
# ---------------------------

app = Dash(__name__, suppress_callback_exceptions=True)
app.title = 'Hotel Booking Analytics Dashboard'

# ---------------------------
# Layout de l'application
# ---------------------------

app.layout = html.Div([
    # Navbar avec Location pour le routing
    create_navbar(),
    
    # Header
    create_header(),
    
    # Contenu principal (changé selon la page)
    html.Div(id='page-content', style={'minHeight': '60vh'}),
    
    # Footer
    create_footer(),
], style={'fontFamily': 'Arial, sans-serif', 'maxWidth': '1400px', 'margin': '0 auto'})

# ---------------------------
# Callback pour le routing
# ---------------------------

@callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    """Affiche la bonne page selon l'URL."""
    if pathname == '/analytics':
        return simple_page.layout(dataframes)
    elif pathname == '/maps':
        return about.layout(dataframes)
    else:  # '/' ou autre
        return home.layout(dataframes)

# ---------------------------
# Lancement de l'application
# ---------------------------

if __name__ == '__main__':
    print("Démarrage du dashboard...")
    print(f"DataFrames chargés: {list(dataframes.keys())}")
    print("Accès: http://127.0.0.1:8050")
    app.run(debug=True, host='127.0.0.1', port=8050)
