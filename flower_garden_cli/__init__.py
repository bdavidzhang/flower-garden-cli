# Directory structure for your package:
# flower-garden-cli/
# ├── flower_garden_cli/
# │   ├── __init__.py
# │   └── main.py
# ├── pyproject.toml
# ├── README.md
# ├── LICENSE
# └── setup.py (optional, for older pip versions)

# =============================================================================
# File: flower_garden_cli/__init__.py
# =============================================================================

"""
Beautiful CLI Flower Garden Game
Water your flowers and watch them grow into stunning patterns!
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .main import main

__all__ = ["main"]
