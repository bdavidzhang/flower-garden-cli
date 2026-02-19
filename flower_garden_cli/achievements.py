"""
Achievement system for Flower Garden CLI v2.0
Track milestones and reward players for their gardening progress.
"""


ACHIEVEMENTS = {
    "first_water": {
        "name": "First Drop",
        "icon": "💧",
        "description": "Water your first flower",
        "check": lambda stats: stats.get("total_waterings", 0) >= 1,
    },
    "green_thumb": {
        "name": "Green Thumb",
        "icon": "🌿",
        "description": "Fully grow your first flower",
        "check": lambda stats: stats.get("max_grown", 0) >= 1,
    },
    "full_garden": {
        "name": "Master Gardener",
        "icon": "🏆",
        "description": "Fully grow all 10 flowers",
        "check": lambda stats: stats.get("max_grown", 0) >= 10,
    },
    "dedicated": {
        "name": "Dedicated Gardener",
        "icon": "🌟",
        "description": "Water flowers 50 times",
        "check": lambda stats: stats.get("total_waterings", 0) >= 50,
    },
    "patient": {
        "name": "Patient Soul",
        "icon": "🧘",
        "description": "Water flowers 100 times",
        "check": lambda stats: stats.get("total_waterings", 0) >= 100,
    },
    "butterfly_friend": {
        "name": "Butterfly Whisperer",
        "icon": "🦋",
        "description": "Attract 5 butterflies to your garden",
        "check": lambda stats: stats.get("visitors", {}).get("butterfly", 0) >= 5,
    },
    "bee_keeper": {
        "name": "Bee Keeper",
        "icon": "🐝",
        "description": "Attract 5 bees to your garden",
        "check": lambda stats: stats.get("visitors", {}).get("bee", 0) >= 5,
    },
    "hummingbird_haven": {
        "name": "Hummingbird Haven",
        "icon": "🐦",
        "description": "Attract a hummingbird",
        "check": lambda stats: stats.get("visitors", {}).get("hummingbird", 0) >= 1,
    },
    "dragonfly_dream": {
        "name": "Dragonfly Dream",
        "icon": "🪁",
        "description": "Attract a dragonfly",
        "check": lambda stats: stats.get("visitors", {}).get("dragonfly", 0) >= 1,
    },
    "weather_watcher": {
        "name": "Weather Watcher",
        "icon": "🌤",
        "description": "Experience all 6 weather types",
        "check": lambda stats: len(stats.get("weather_seen", [])) >= 6,
    },
    "storm_chaser": {
        "name": "Storm Chaser",
        "icon": "⛈",
        "description": "Water during a storm for bonus growth",
        "check": lambda stats: stats.get("stormy_waterings", 0) >= 1,
    },
    "night_gardener": {
        "name": "Night Gardener",
        "icon": "🌙",
        "description": "Water under starry skies",
        "check": lambda stats: stats.get("starry_waterings", 0) >= 1,
    },
    "half_way": {
        "name": "Halfway There",
        "icon": "🌱",
        "description": "Reach 50 total growth levels across all flowers",
        "check": lambda stats: stats.get("total_growth", 0) >= 50,
    },
    "century": {
        "name": "Century Garden",
        "icon": "💐",
        "description": "Reach 100 total growth levels",
        "check": lambda stats: stats.get("total_growth", 0) >= 100,
    },
}


def check_achievements(stats, unlocked):
    """Check for newly unlocked achievements. Returns list of newly unlocked."""
    newly_unlocked = []
    for aid, ach in ACHIEVEMENTS.items():
        if aid not in unlocked:
            if ach["check"](stats):
                newly_unlocked.append(aid)
    return newly_unlocked


def format_achievement(aid):
    """Format an achievement for display."""
    ach = ACHIEVEMENTS[aid]
    return f"{ach['icon']}  {ach['name']} - {ach['description']}"


def get_achievement_progress(stats, unlocked):
    """Get progress summary."""
    total = len(ACHIEVEMENTS)
    done = len(unlocked)
    return done, total
