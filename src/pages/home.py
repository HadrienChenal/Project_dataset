"""
Page d'accueil du dashboard.
Affiche un résumé des données et des KPIs.
"""
import pandas as pd
from dash import html, dcc

def layout(dataframes: dict):
    """Crée la page d'accueil."""
    
    # Calcul des KPIs
    total_hotels = len(dataframes.get('hotels.csv', pd.DataFrame()))
    total_reviews = len(dataframes.get('reviews.csv', pd.DataFrame()))
    total_users = len(dataframes.get('users.csv', pd.DataFrame()))

    return html.Div([

        # --- Section explicative ---
        html.Div([
            html.H2("- Pourquoi ce projet est important - ", style={
                'textAlign': 'center',
                'marginTop': '10px',
                'color': '#333'
            }),
            html.P(
                "Le tourisme joue un rôle clé dans l’économie mondiale et dans la vitalité des territoires. "
                "Grâce à l’analyse des données de réservations hôtelières internationales, ce projet aide à mieux "
                "comprendre les habitudes de voyage, les périodes de forte affluence et les comportements des clients. "
                "Ces analyses contribuent à un tourisme plus durable et plus responsable, au bénéfice des voyageurs "
                "et des communautés locales.",
                style={
                    'textAlign': 'center',
                    'maxWidth': '850px',
                    'margin': '20px auto',
                    'color': '#444',
                    'lineHeight': '1.6',
                    'fontSize': '18px'
                }
            )
        ], style={
            'backgroundColor': '#FAFAFA',
            'padding': '40px 20px',
            'borderRadius': '12px',
            'marginTop': '40px',
            'boxShadow': '0 4px 10px rgba(0,0,0,0.05)',
            'backgroundImage': 'url("/images/voyage.jpg")'

        }),


        # --- Cartes de statistiques ---
        html.Div([
            html.H2('3 jeux de données interconnectés recensant :', style={
                'textAlign': 'center',
                'marginTop': '20px',
                'color': '#333'
            }),
            
            html.Div([
                html.Div([
                    html.H3('Hôtels'),
                    html.H4(f'{total_hotels:,}', style={'fontSize': '28px', 'marginTop': '10px'})
                ], style={'flex': '1',
                'minWidth': '220px',
                'textAlign': 'center',
                'padding': '25px',
                'backgroundColor': "#B0DFEE",
                'borderRadius': '12px',
                'boxShadow': '0 4px 8px rgba(0,0,0,0.1)',
                'transition': 'transform 0.2s ease',
                'margin': '10px'}),
                
                html.Div([
                    html.H3('Avis'),
                    html.H4(f'{total_reviews:,}', style={'fontSize': '28px', 'marginTop': '10px'})
                ], style={'flex': '1',
                'minWidth': '220px',
                'textAlign': 'center',
                'padding': '25px',
                'backgroundColor': "#B0DFEE",
                'borderRadius': '12px',
                'boxShadow': '0 4px 8px rgba(0,0,0,0.1)',
                'transition': 'transform 0.2s ease',
                'margin': '10px'}),
                
                html.Div([
                    html.H3('Utilisateurs'),
                    html.H4(f'{total_users:,}', style={'fontSize': '28px', 'marginTop': '10px'})
                ], style={'flex': '1',
                'minWidth': '220px',
                'textAlign': 'center',
                'padding': '25px',
                'backgroundColor': "#B0DFEE",
                'borderRadius': '12px',
                'boxShadow': '0 4px 8px rgba(0,0,0,0.1)',
                'transition': 'transform 0.2s ease',
                'margin': '10px'}),

            ], style={
                'display': 'flex',
                'justifyContent': 'center',
                'flexWrap': 'wrap',
                'gap': '20px',
                'marginBottom': '40px'
            })
        ]),

    ], style={'padding': '20px', 'marginTop': '40px'})
