"""
Weather and seasons system for Flower Garden CLI v2.0
Dynamic weather affects garden visuals and growth rates.
"""

import random
import math
import time
from datetime import datetime


SEASONS = ["Spring", "Summer", "Autumn", "Winter"]

WEATHER_TYPES = {
    "sunny": {
        "icon": "☀",
        "name": "Sunny",
        "growth_bonus": 1,
        "overlay_char": "·",
        "description": "Warm sunshine bathes your garden",
    },
    "rainy": {
        "icon": "🌧",
        "name": "Rainy",
        "growth_bonus": 2,
        "overlay_char": "│",
        "description": "Gentle rain nourishes your flowers",
    },
    "windy": {
        "icon": "🌬",
        "name": "Windy",
        "growth_bonus": 0,
        "overlay_char": "~",
        "description": "A brisk wind sweeps through the garden",
    },
    "misty": {
        "icon": "🌫",
        "name": "Misty",
        "growth_bonus": 1,
        "overlay_char": "░",
        "description": "A soft mist drifts through the flowers",
    },
    "starry": {
        "icon": "✨",
        "name": "Starry Night",
        "growth_bonus": 1,
        "overlay_char": "✧",
        "description": "Stars twinkle above your moonlit garden",
    },
    "stormy": {
        "icon": "⛈",
        "name": "Stormy",
        "growth_bonus": 3,
        "overlay_char": "╪",
        "description": "Thunder rumbles as lightning illuminates the sky",
    },
}

# Season-specific weather probabilities
SEASON_WEATHER = {
    "Spring": {"sunny": 0.25, "rainy": 0.35, "windy": 0.15, "misty": 0.15, "starry": 0.05, "stormy": 0.05},
    "Summer": {"sunny": 0.45, "rainy": 0.10, "windy": 0.10, "misty": 0.05, "starry": 0.15, "stormy": 0.15},
    "Autumn": {"sunny": 0.15, "rainy": 0.20, "windy": 0.30, "misty": 0.25, "starry": 0.05, "stormy": 0.05},
    "Winter": {"sunny": 0.10, "rainy": 0.15, "windy": 0.20, "misty": 0.35, "starry": 0.15, "stormy": 0.05},
}


def get_current_season():
    """Get the current season based on real-world month."""
    month = datetime.now().month
    if month in (3, 4, 5):
        return "Spring"
    elif month in (6, 7, 8):
        return "Summer"
    elif month in (9, 10, 11):
        return "Autumn"
    else:
        return "Winter"


def get_random_weather(season=None):
    """Pick a random weather type weighted by current season."""
    if season is None:
        season = get_current_season()
    weights = SEASON_WEATHER.get(season, SEASON_WEATHER["Spring"])
    types = list(weights.keys())
    probs = list(weights.values())
    return random.choices(types, weights=probs, k=1)[0]


def render_weather_overlay(width, height, weather_type, frame=0):
    """Generate a weather overlay as a list of strings."""
    overlay = []
    w = WEATHER_TYPES[weather_type]

    for y in range(height):
        line = ""
        for x in range(width):
            if weather_type == "rainy":
                if (x + y + frame) % 4 == 0:
                    line += "│"
                elif (x + y + frame) % 7 == 0:
                    line += ","
                else:
                    line += " "
            elif weather_type == "windy":
                if (x + frame) % 6 == 0 and (y % 3 == 0):
                    line += "~"
                elif (x + frame + 2) % 8 == 0 and (y % 2 == 0):
                    line += "≈"
                else:
                    line += " "
            elif weather_type == "misty":
                if (x * 3 + y * 7 + frame) % 11 == 0:
                    line += "░"
                elif (x * 5 + y * 3 + frame) % 13 == 0:
                    line += "▒"
                else:
                    line += " "
            elif weather_type == "starry":
                seed = (x * 17 + y * 31) % 97
                if seed < 3 and y < height // 2:
                    twinkle = (seed + frame) % 3
                    line += ["✧", "✦", "·"][twinkle]
                else:
                    line += " "
            elif weather_type == "stormy":
                if frame % 6 == 0 and random.random() < 0.01:
                    line += "╪"
                elif (x + y + frame) % 5 == 0:
                    line += "│"
                elif (x + y + frame) % 9 == 0:
                    line += ","
                else:
                    line += " "
            else:  # sunny
                if (x * 7 + y * 11) % 47 == 0 and y < height // 3:
                    line += "·"
                else:
                    line += " "
        overlay.append(line)
    return overlay


def render_season_border(width, season):
    """Create a decorative border based on the current season."""
    if season == "Spring":
        flowers = "✿ ❀ ✿ ❀ "
        border = (flowers * (width // len(flowers) + 1))[:width]
    elif season == "Summer":
        suns = "☀ · ☀ · "
        border = (suns * (width // len(suns) + 1))[:width]
    elif season == "Autumn":
        leaves = "🍂 🍁 🍂 🍁 " if False else "{ } ~ { } ~ "
        border = (leaves * (width // len(leaves) + 1))[:width]
    else:  # Winter
        snow = "* . * . "
        border = (snow * (width // len(snow) + 1))[:width]
    return border


def get_weather_greeting(weather_type, season):
    """Get a contextual greeting for the current weather and season."""
    w = WEATHER_TYPES[weather_type]
    return f"{w['icon']}  {season} | {w['name']} - {w['description']}"
