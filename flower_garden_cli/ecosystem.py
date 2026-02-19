"""
Ecosystem system for Flower Garden CLI v2.0
Butterflies, bees, and fireflies visit your garden based on flower growth.
"""

import random
import math


CREATURES = {
    "butterfly": {
        "sprites": ["~^~", "~v~", "-^-", "-v-"],
        "icon": "~^~",
        "name": "Butterfly",
        "min_garden_growth": 15,
        "rarity": 0.6,
    },
    "bee": {
        "sprites": ["=B>", "<B=", "=B="],
        "icon": "=B>",
        "name": "Bee",
        "min_garden_growth": 10,
        "rarity": 0.7,
    },
    "firefly": {
        "sprites": ["*", ".", "o", "."],
        "icon": "*",
        "name": "Firefly",
        "min_garden_growth": 20,
        "rarity": 0.4,
    },
    "ladybug": {
        "sprites": ["@", "o"],
        "icon": "@",
        "name": "Ladybug",
        "min_garden_growth": 5,
        "rarity": 0.8,
    },
    "hummingbird": {
        "sprites": [">o>", "<o<", ">O>"],
        "icon": ">o>",
        "name": "Hummingbird",
        "min_garden_growth": 30,
        "rarity": 0.3,
    },
    "dragonfly": {
        "sprites": ["==x==", "==+=="],
        "icon": "==x==",
        "name": "Dragonfly",
        "min_garden_growth": 40,
        "rarity": 0.2,
    },
}


class Creature:
    """A creature that moves around the garden."""

    def __init__(self, creature_type, x, y, garden_width, garden_height):
        self.type = creature_type
        self.data = CREATURES[creature_type]
        self.x = x
        self.y = y
        self.width = garden_width
        self.height = garden_height
        self.frame = 0
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 0, 1])
        self.lifespan = random.randint(20, 60)
        self.age = 0

    def update(self):
        """Move the creature one step."""
        self.age += 1
        self.frame = (self.frame + 1) % len(self.data["sprites"])

        # Wander with slight randomness
        if random.random() < 0.3:
            self.dx = random.choice([-1, 0, 1])
        if random.random() < 0.2:
            self.dy = random.choice([-1, 0, 1])

        self.x = max(0, min(self.width - 4, self.x + self.dx))
        self.y = max(0, min(self.height - 1, self.y + self.dy))

    @property
    def sprite(self):
        return self.data["sprites"][self.frame]

    @property
    def alive(self):
        return self.age < self.lifespan


class Ecosystem:
    """Manages all creatures in the garden."""

    def __init__(self):
        self.creatures = []
        self.total_visitors = {k: 0 for k in CREATURES}
        self.spawn_cooldown = 0

    def update(self, total_garden_growth, width=60, height=20):
        """Update ecosystem state - spawn and move creatures."""
        # Update existing creatures
        for c in self.creatures:
            c.update()
        self.creatures = [c for c in self.creatures if c.alive]

        # Maybe spawn new creatures
        self.spawn_cooldown = max(0, self.spawn_cooldown - 1)
        if self.spawn_cooldown <= 0 and len(self.creatures) < 5:
            for ctype, cdata in CREATURES.items():
                if total_garden_growth >= cdata["min_garden_growth"]:
                    if random.random() < cdata["rarity"] * 0.1:
                        x = random.randint(0, width - 5)
                        y = random.randint(0, height - 1)
                        self.creatures.append(
                            Creature(ctype, x, y, width, height)
                        )
                        self.total_visitors[ctype] += 1
                        self.spawn_cooldown = random.randint(3, 8)
                        break

    def get_visitor_summary(self):
        """Return a summary of all visitors."""
        active = {}
        for c in self.creatures:
            active[c.type] = active.get(c.type, 0) + 1
        return active

    def get_total_visitors(self):
        """Return total visitors of each type."""
        return {k: v for k, v in self.total_visitors.items() if v > 0}

    def render_creatures(self, width, height):
        """Render all creatures onto a grid. Returns list of (x, y, sprite) tuples."""
        result = []
        for c in self.creatures:
            result.append((c.x, c.y, c.sprite))
        return result
