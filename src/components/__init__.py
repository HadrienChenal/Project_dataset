"""
Package des composants Dash réutilisables.
"""
from .header import create_header
from .navbar import create_navbar
from .footer import create_footer
from .histogrammes import (
    tracer_histogramme_notes,
    tracer_histogramme_proprete,
    tracer_histogramme_score_base,
    tracer_histogramme_confort,
    tracer_histogramme_installations,
    tracer_histogramme_emplacement
    
)
from .cartes import (
    generer_carte_hotels,
    tracer_carte_utilisateurs,
)

__all__ = [
    'create_header',
    'create_navbar',
    'create_footer',
    'tracer_histogramme_notes',
    'tracer_histogramme_proprete',
    'generer_carte_hotels',
    'tracer_carte_utilisateurs',
    'tracer_histogramme_score_base',
    'tracer_histogramme_confort',
    'tracer_histogramme_installations',
    'tracer_histogramme_emplacement',
]
