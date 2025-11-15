"""
Dashboard Dash - Hotel Booking Analytics
Structure modulaire avec composants et pages réutilisables.

Pipeline: récupération des données → nettoyage → dashboard Dash interactif

Utilisation:
    python main.py
    Puis ouvrir http://127.0.0.1:8050 dans le navigateur.
"""

import os
import sys
from dash import Dash, html, Input, Output, callback
import pandas as pd

# Ajouter le répertoire src au path pour les imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from src.pages import analyse, geographie, home
from src.components.header import create_header
from src.components.navbar import create_navbar
from src.components.footer import create_footer
from src.utils.get_data import charger_csvs, telecharger_dataset, RAW_DATA_PATH
from src.utils.clean_data import process_data


def load_data():
    """Charge les CSV depuis le dossier data/raw."""
    try:
        dataframes = charger_csvs(RAW_DATA_PATH)
        if not dataframes:
            print(f"Aucun CSV trouvé dans {RAW_DATA_PATH}. Utilisation du dossier local 'data/'.")
            if os.path.exists('data'):
                dataframes = charger_csvs('data')
        return dataframes
    except Exception as e:
        print(f"Erreur lors du chargement des données: {e}")
        return {}


def create_app(dataframes):
    """Crée et configure l'application Dash."""
    app = Dash(__name__, suppress_callback_exceptions=True)
    app.title = 'Hotel Booking Analytics Dashboard'

    app.layout = html.Div([
        create_navbar(),
        create_header(),
        html.Div(id='page-content', style={'minHeight': '60vh'}),
        create_footer(),
    ], style={'fontFamily': 'Arial, sans-serif', 'maxWidth': '1400px', 'margin': '0 auto'})

    @callback(
        Output('page-content', 'children'),
        Input('url', 'pathname')
    )
    def display_page(pathname):
        """Affiche la bonne page selon l'URL."""
        if pathname == '/analytics':
            return analyse.layout(dataframes)
        elif pathname == '/maps':
            return geographie.layout(dataframes)
        else:
            return home.layout(dataframes)

    return app


if __name__ == '__main__':
    print("=" * 60)
    print("HOTEL BOOKING ANALYTICS - INITIALISATION")
    print("=" * 60)
    
    # ------- 1. Récupération et nettoyage des données -------
    print("\n[1/3] Nettoyage des donnees...")
    try:
        process_data()
        print("[OK] Nettoyage termine avec succes")
    except Exception as e:
        print(f"[WARNING] Erreur lors du nettoyage : {e}")
        print("Continuation avec les donnees disponibles...")
    
    # ------- 2. Chargement des données -------
    print("\n[2/3] Chargement des donnees...")
    dataframes = load_data()
    
    if not dataframes:
        print("[WARNING] Aucune donnee chargee. Creation de DataFrames vides...")
        dataframes = {
            'hotels.csv': pd.DataFrame(),
            'reviews.csv': pd.DataFrame(),
            'users.csv': pd.DataFrame()
        }
    else:
        print(f"[OK] DataFrames charges: {list(dataframes.keys())}")
        for name, df in dataframes.items():
            print(f"  - {name}: {len(df)} lignes")
    
    # ------- 3. Lancement du dashboard -------
    print("\n[3/3] Demarrage du dashboard...")
    app = create_app(dataframes)
    
    print("\n" + "=" * 60)
    print("[OK] Dashboard pret !")
    print("[INFO] Acces: http://127.0.0.1:8050")
    print("=" * 60)
    
    app.run(debug=True, host='127.0.0.1', port=8050, use_reloader=False)
