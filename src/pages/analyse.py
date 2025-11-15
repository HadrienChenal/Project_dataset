"""
Page d'analyses - histogrammes et statistiques.
"""
from dash import html, dcc
from src.components.histogrammes import (
    tracer_histogramme_notes,
    tracer_histogramme_proprete,
    tracer_histogramme_score_base
    , tracer_histogramme_confort
    , tracer_histogramme_installations
    , tracer_histogramme_emplacement
)

def layout(dataframes: dict):
    """Crée la page d'analyses."""
    
    # Appels sécurisés pour générer les graphiques Plotly
    hist_notes = tracer_histogramme_notes(dataframes)
    hist_notes_component = dcc.Graph(figure=hist_notes, style={'height': '500px'}) if hist_notes else html.P("Impossible d'afficher l'histogramme des notes globales.")

    hist_proprete = tracer_histogramme_proprete(dataframes)
    hist_proprete_component = dcc.Graph(figure=hist_proprete, style={'height': '500px'}) if hist_proprete else html.P("Impossible d'afficher l'histogramme de la propreté.")

    hist_score_base = tracer_histogramme_score_base(dataframes)
    hist_score_base_component = dcc.Graph(figure=hist_score_base, style={'height': '500px'}) if hist_score_base else html.P("Impossible d'afficher l'histogramme du score de base.")

    # Construction du layout
    return html.Div([
    html.H2('Analyses détaillées', style={'marginTop': '20px', 'textAlign': 'center'}),

    # --- Premier graphique seul ---
    html.Div([
        html.Div([
            html.H3('Scores de base moyens', style={'textAlign': 'center'}),
            hist_score_base_component
        ], style={
            'width': '100%',          # prend toute la largeur
            'margin': '10px',
            'padding': '15px',
            'borderRadius': '12px',
            'boxShadow': '0 4px 10px rgba(0,0,0,0.05)',
            'backgroundColor': '#FAFAFA'
        })
    ], style={
        'display': 'flex',
        'justifyContent': 'center'
    }),

    # --- Deux graphiques côte à côte ---
    html.Div([
        html.Div([
            html.H3('Notes globales', style={'textAlign': 'center'}),
            hist_notes_component
        ], style={
            'flex': '1',
            'minWidth': '350px',     # pour garantir un bon comportement responsive
            'margin': '10px',
            'padding': '15px',
            'borderRadius': '12px',
            'boxShadow': '0 4px 10px rgba(0,0,0,0.05)',
            'backgroundColor': '#FAFAFA'
        }),

        html.Div([
            html.H3('Scores de propreté', style={'textAlign': 'center'}),
            hist_proprete_component
        ], style={
            'flex': '1',
            'minWidth': '350px',
            'margin': '10px',
            'padding': '15px',
            'borderRadius': '12px',
            'boxShadow': '0 4px 10px rgba(0,0,0,0.05)',
            'backgroundColor': '#FAFAFA'
        }),
    ], style={
        'display': 'flex',
        'flexWrap': 'wrap',
        'justifyContent': 'center',
        'gap': '20px'
    })

    # --- Troisième rangée : confort, installations, emplacement ---
    hist_confort = tracer_histogramme_confort(dataframes)
    hist_install = tracer_histogramme_installations(dataframes)
    hist_location = tracer_histogramme_emplacement(dataframes)

    hist_confort_component = dcc.Graph(figure=hist_confort, style={'height': '450px'}) if hist_confort else html.P("Impossible d'afficher l'histogramme de confort.")
    hist_install_component = dcc.Graph(figure=hist_install, style={'height': '450px'}) if hist_install else html.P("Impossible d'afficher l'histogramme des installations.")
    hist_location_component = dcc.Graph(figure=hist_location, style={'height': '450px'}) if hist_location else html.P("Impossible d'afficher l'histogramme d'emplacement.")

    # Ajout à l'affichage
    layout_extra = html.Div([
        html.Div([html.H3('Notes confort', style={'textAlign': 'center'}), hist_confort_component], style={'flex': '1', 'minWidth': '300px'}),
        html.Div([html.H3('Notes installations', style={'textAlign': 'center'}), hist_install_component], style={'flex': '1', 'minWidth': '300px'}),
        html.Div([html.H3('Notes emplacement', style={'textAlign': 'center'}), hist_location_component], style={'flex': '1', 'minWidth': '300px'}),
    ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center', 'gap': '20px', 'marginTop': '20px'})

    # Insérer la section additionnelle avant la fin
    children = []
    children.extend([html.H2('Analyses détaillées', style={'marginTop': '20px', 'textAlign': 'center'})])
    # Rebuild the layout using previously constructed parts
    # [We will simply append the extra block to the existing layout returned above]
    return html.Div([
        html.H2('Analyses détaillées', style={'marginTop': '20px', 'textAlign': 'center'}),
        # Keep the original existing blocks by reusing previous HTML (we'll replicate the previous return structure)
        html.Div([html.Div([html.H3('Scores de base moyens', style={'textAlign': 'center'}), hist_score_base_component], style={'width': '100%', 'margin': '10px','padding': '15px','borderRadius': '12px','boxShadow': '0 4px 10px rgba(0,0,0,0.05)','backgroundColor': '#FAFAFA'})], style={'display': 'flex','justifyContent': 'center'}),
        html.Div([
            html.Div([html.H3('Notes globales', style={'textAlign': 'center'}), hist_notes_component], style={'flex': '1','minWidth': '350px','margin': '10px','padding': '15px','borderRadius': '12px','boxShadow': '0 4px 10px rgba(0,0,0,0.05)','backgroundColor': '#FAFAFA'}),
            html.Div([html.H3('Scores de propreté', style={'textAlign': 'center'}), hist_proprete_component], style={'flex': '1','minWidth': '350px','margin': '10px','padding': '15px','borderRadius': '12px','boxShadow': '0 4px 10px rgba(0,0,0,0.05)','backgroundColor': '#FAFAFA'}),
        ], style={'display': 'flex','flexWrap': 'wrap','justifyContent': 'center','gap': '20px'}),

        # Nouvelle rangée
        layout_extra
    ], style={'padding': '20px'})

], style={'padding': '20px'})


