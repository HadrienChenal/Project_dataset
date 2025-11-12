"""
Package des composants Dash réutilisables.
"""
from .header import create_header
from .navbar import create_navbar
from .footer import create_footer
from .component1 import (
    tracer_histogramme_notes,
    tracer_histogramme_proprete,
)
from .component2 import (
    generer_carte_hotels
)

__all__ = [
    'create_header',
    'create_navbar',
    'create_footer',
    'tracer_histogramme_notes',
    'tracer_histogramme_proprete',
    'generer_carte_hotels',
]
