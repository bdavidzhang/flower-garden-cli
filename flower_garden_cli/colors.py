"""
Color system for Flower Garden CLI v2.0
Supports gradient colors, themes, and fallback for terminals without color support.
"""

import sys

try:
    from colorama import init, Fore, Back, Style

    init()
    COLORS_AVAILABLE = True
except ImportError:

    class MockFore:
        RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = ""
        LIGHTRED_EX = LIGHTGREEN_EX = LIGHTYELLOW_EX = LIGHTBLUE_EX = ""
        LIGHTMAGENTA_EX = LIGHTCYAN_EX = LIGHTWHITE_EX = ""

    class MockBack:
        RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = ""

    class MockStyle:
        BRIGHT = DIM = RESET_ALL = ""

    Fore = MockFore()
    Back = MockBack()
    Style = MockStyle()
    COLORS_AVAILABLE = False


# Theme color palettes
THEMES = {
    "garden": {
        "title": Fore.GREEN + Style.BRIGHT,
        "subtitle": Fore.LIGHTGREEN_EX,
        "border": Fore.GREEN,
        "menu_header": Fore.LIGHTYELLOW_EX + Style.BRIGHT,
        "menu_item": Fore.WHITE,
        "highlight": Fore.YELLOW + Style.BRIGHT,
        "water": Fore.CYAN,
        "growth": Fore.GREEN + Style.BRIGHT,
        "warning": Fore.YELLOW,
        "error": Fore.RED,
        "dim": Style.DIM if hasattr(Style, "DIM") else "",
        "reset": Style.RESET_ALL,
    },
    "midnight": {
        "title": Fore.LIGHTBLUE_EX + Style.BRIGHT,
        "subtitle": Fore.LIGHTCYAN_EX,
        "border": Fore.BLUE,
        "menu_header": Fore.LIGHTMAGENTA_EX + Style.BRIGHT,
        "menu_item": Fore.LIGHTWHITE_EX,
        "highlight": Fore.LIGHTCYAN_EX + Style.BRIGHT,
        "water": Fore.LIGHTBLUE_EX,
        "growth": Fore.LIGHTCYAN_EX + Style.BRIGHT,
        "warning": Fore.LIGHTYELLOW_EX,
        "error": Fore.LIGHTRED_EX,
        "dim": Style.DIM if hasattr(Style, "DIM") else "",
        "reset": Style.RESET_ALL,
    },
    "sunset": {
        "title": Fore.LIGHTRED_EX + Style.BRIGHT,
        "subtitle": Fore.LIGHTYELLOW_EX,
        "border": Fore.RED,
        "menu_header": Fore.YELLOW + Style.BRIGHT,
        "menu_item": Fore.LIGHTYELLOW_EX,
        "highlight": Fore.LIGHTRED_EX + Style.BRIGHT,
        "water": Fore.LIGHTMAGENTA_EX,
        "growth": Fore.LIGHTYELLOW_EX + Style.BRIGHT,
        "warning": Fore.YELLOW,
        "error": Fore.RED,
        "dim": Style.DIM if hasattr(Style, "DIM") else "",
        "reset": Style.RESET_ALL,
    },
}

# Flower-specific color sets
FLOWER_COLORS = {
    "spiral_rose": [Fore.RED, Fore.LIGHTRED_EX, Fore.MAGENTA],
    "fractal_tree": [Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.YELLOW],
    "mandala_bloom": [Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX],
    "wave_garden": [Fore.CYAN, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX],
    "star_burst": [Fore.YELLOW, Fore.LIGHTYELLOW_EX, Fore.WHITE],
    "crystal_lotus": [Fore.LIGHTCYAN_EX, Fore.WHITE, Fore.LIGHTBLUE_EX],
    "phoenix_fern": [Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.YELLOW],
    "galaxy_orchid": [Fore.LIGHTMAGENTA_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX],
    "thunder_vine": [Fore.LIGHTYELLOW_EX, Fore.WHITE, Fore.LIGHTGREEN_EX],
    "aurora_lily": [Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTMAGENTA_EX],
}


def gradient_text(text, colors):
    """Apply a gradient effect across text using a list of colors."""
    if not COLORS_AVAILABLE or not colors:
        return text
    result = ""
    chunk_size = max(1, len(text) // len(colors))
    for i, char in enumerate(text):
        color_idx = min(i // chunk_size, len(colors) - 1)
        result += colors[color_idx] + char
    return result + Style.RESET_ALL


def colorize(text, color):
    """Apply a single color to text."""
    if not COLORS_AVAILABLE:
        return text
    return f"{color}{text}{Style.RESET_ALL}"
