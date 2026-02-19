#!/usr/bin/env python3
"""
Flower Garden CLI v2.0
A living, breathing terminal garden with weather, seasons, ecosystems, and achievements.
"""

import math
import time
import os
import json
import sys
import random
from typing import Dict, List, Tuple
from datetime import datetime

from .colors import (
    Fore,
    Back,
    Style,
    COLORS_AVAILABLE,
    THEMES,
    FLOWER_COLORS,
    gradient_text,
    colorize,
)
from .patterns import generate_pattern, PATTERNS
from .weather import (
    get_current_season,
    get_random_weather,
    render_weather_overlay,
    render_season_border,
    get_weather_greeting,
    WEATHER_TYPES,
)
from .ecosystem import Ecosystem, CREATURES
from .achievements import (
    check_achievements,
    format_achievement,
    get_achievement_progress,
    ACHIEVEMENTS,
)


# ── Flower Definitions ──

FLOWERS = {
    "spiral_rose": {"name": "Spiral Rose", "icon": "🌹", "tier": 1},
    "fractal_tree": {"name": "Fractal Tree", "icon": "🌳", "tier": 1},
    "mandala_bloom": {"name": "Mandala Bloom", "icon": "🌺", "tier": 1},
    "wave_garden": {"name": "Wave Garden", "icon": "🌊", "tier": 1},
    "star_burst": {"name": "Star Burst", "icon": "⭐", "tier": 1},
    "crystal_lotus": {"name": "Crystal Lotus", "icon": "💎", "tier": 2},
    "phoenix_fern": {"name": "Phoenix Fern", "icon": "🔥", "tier": 2},
    "galaxy_orchid": {"name": "Galaxy Orchid", "icon": "🌌", "tier": 2},
    "thunder_vine": {"name": "Thunder Vine", "icon": "⚡", "tier": 2},
    "aurora_lily": {"name": "Aurora Lily", "icon": "🌈", "tier": 2},
}

FLOWER_ORDER = [
    "spiral_rose",
    "fractal_tree",
    "mandala_bloom",
    "wave_garden",
    "star_burst",
    "crystal_lotus",
    "phoenix_fern",
    "galaxy_orchid",
    "thunder_vine",
    "aurora_lily",
]

VERSION = "2.0.0"
SAVE_FILE = os.path.expanduser("~/.flower_garden_v2_save.json")
MAX_GROWTH = 10


class FlowerGarden:
    def __init__(self):
        # Growth state for all flowers
        self.growth = {k: 0 for k in FLOWER_ORDER}

        # Stats tracking
        self.stats = {
            "total_waterings": 0,
            "total_growth": 0,
            "max_grown": 0,
            "weather_seen": [],
            "stormy_waterings": 0,
            "starry_waterings": 0,
            "visitors": {},
            "garden_created": datetime.now().isoformat(),
            "sessions": 0,
        }

        # Achievements
        self.unlocked_achievements = []

        # Systems
        self.ecosystem = Ecosystem()
        self.season = get_current_season()
        self.weather = get_random_weather(self.season)
        self.theme_name = "garden"
        self.theme = THEMES[self.theme_name]

        # Load saved state
        self.load_garden()
        self.stats["sessions"] += 1

        # Track weather
        if self.weather not in self.stats["weather_seen"]:
            self.stats["weather_seen"].append(self.weather)

    # ── Save / Load ──

    def save_garden(self):
        try:
            data = {
                "growth": self.growth,
                "stats": self.stats,
                "achievements": self.unlocked_achievements,
                "theme": self.theme_name,
                "ecosystem_visitors": self.ecosystem.total_visitors,
            }
            with open(SAVE_FILE, "w") as f:
                json.dump(data, f, indent=2)
        except Exception:
            pass

    def load_garden(self):
        try:
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
            for k, v in data.get("growth", {}).items():
                if k in self.growth:
                    self.growth[k] = min(MAX_GROWTH, max(0, v))
            saved_stats = data.get("stats", {})
            for k, v in saved_stats.items():
                if k in self.stats:
                    self.stats[k] = v
            self.unlocked_achievements = data.get("achievements", [])
            theme = data.get("theme", "garden")
            if theme in THEMES:
                self.theme_name = theme
                self.theme = THEMES[theme]
            eco_vis = data.get("ecosystem_visitors", {})
            for k, v in eco_vis.items():
                if k in self.ecosystem.total_visitors:
                    self.ecosystem.total_visitors[k] = v
        except Exception:
            pass

    # ── Helpers ──

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def total_growth(self):
        return sum(self.growth.values())

    def max_grown_count(self):
        return sum(1 for v in self.growth.values() if v >= MAX_GROWTH)

    # ── Display ──

    def print_header(self):
        t = self.theme
        season_border = render_season_border(60, self.season)
        print(f"{t['border']}{season_border}{t['reset']}")
        title = f"  Flower Garden v{VERSION}  "
        print(f"{t['title']}{'=' * 10}{title}{'=' * 10}{t['reset']}")
        print(
            f"{t['subtitle']}  {get_weather_greeting(self.weather, self.season)}{t['reset']}"
        )
        print(f"{t['border']}{season_border}{t['reset']}")
        print()

    def print_stats_bar(self):
        t = self.theme
        total = self.total_growth()
        maxed = self.max_grown_count()
        ach_done, ach_total = get_achievement_progress(
            self.stats, self.unlocked_achievements
        )

        # Compact stats line
        bar_filled = int(total / (MAX_GROWTH * len(FLOWER_ORDER)) * 20)
        bar_empty = 20 - bar_filled
        bar = f"{'█' * bar_filled}{'░' * bar_empty}"

        print(
            f"{t['subtitle']}  Garden [{bar}] "
            f"{total}/{MAX_GROWTH * len(FLOWER_ORDER)}  "
            f"| Full Blooms: {maxed}/{len(FLOWER_ORDER)}  "
            f"| Achievements: {ach_done}/{ach_total}  "
            f"| Waterings: {self.stats['total_waterings']}"
            f"{t['reset']}"
        )

        # Show active creatures
        active = self.ecosystem.get_visitor_summary()
        if active:
            creatures_str = "  ".join(
                f"{CREATURES[k]['icon']}x{v}" for k, v in active.items()
            )
            print(f"{t['dim']}  Visitors: {creatures_str}{t['reset']}")
        print()

    def display_flower(self, flower_type: str):
        """Display a single flower with its pattern."""
        fdef = FLOWERS[flower_type]
        growth = self.growth[flower_type]
        colors = FLOWER_COLORS.get(flower_type, [Fore.WHITE])
        primary = colors[0]

        # Header
        tier_label = "Tier II" if fdef["tier"] == 2 else "Tier I"
        bar = f"{'█' * growth}{'░' * (MAX_GROWTH - growth)}"
        print(
            f"  {primary}{Style.BRIGHT}"
            f"{fdef['icon']} {fdef['name']} [{tier_label}]{Style.RESET_ALL}"
        )
        print(
            f"  {primary}  Growth: [{bar}] {growth}/{MAX_GROWTH}{Style.RESET_ALL}"
        )

        if growth == 0:
            print(f"  {Style.DIM}  A tiny seed waiting to be watered...{Style.RESET_ALL}")
            print()
            return

        # Pattern
        pattern_lines = generate_pattern(flower_type, growth)
        for i, line in enumerate(pattern_lines):
            color = colors[i % len(colors)] if len(colors) > 1 else primary
            print(f"  {color}  {line}{Style.RESET_ALL}")
        print()

    def display_garden_compact(self):
        """Show all flowers in a compact overview grid."""
        t = self.theme
        print(f"{t['menu_header']}  Garden Overview:{t['reset']}")
        print()

        # Two columns
        for i in range(0, len(FLOWER_ORDER), 2):
            left = FLOWER_ORDER[i]
            right = FLOWER_ORDER[i + 1] if i + 1 < len(FLOWER_ORDER) else None

            l_def = FLOWERS[left]
            l_g = self.growth[left]
            l_bar = f"{'█' * l_g}{'░' * (MAX_GROWTH - l_g)}"
            l_colors = FLOWER_COLORS.get(left, [Fore.WHITE])
            l_status = "FULL BLOOM!" if l_g >= MAX_GROWTH else ("Seed" if l_g == 0 else f"Lv.{l_g}")

            left_str = (
                f"  {l_colors[0]}{l_def['icon']} {l_def['name']:<16} "
                f"[{l_bar}] {l_status:<12}{Style.RESET_ALL}"
            )

            if right:
                r_def = FLOWERS[right]
                r_g = self.growth[right]
                r_bar = f"{'█' * r_g}{'░' * (MAX_GROWTH - r_g)}"
                r_colors = FLOWER_COLORS.get(right, [Fore.WHITE])
                r_status = "FULL BLOOM!" if r_g >= MAX_GROWTH else ("Seed" if r_g == 0 else f"Lv.{r_g}")
                right_str = (
                    f"{r_colors[0]}{r_def['icon']} {r_def['name']:<16} "
                    f"[{r_bar}] {r_status:<12}{Style.RESET_ALL}"
                )
            else:
                right_str = ""

            print(f"{left_str}  {right_str}")

        print()

    def display_garden_full(self):
        """Display every flower's full pattern."""
        self.clear_screen()
        self.print_header()
        self.print_stats_bar()

        for flower_type in FLOWER_ORDER:
            self.display_flower(flower_type)

    def display_dashboard(self):
        """Main dashboard view."""
        self.clear_screen()
        self.print_header()
        self.print_stats_bar()
        self.display_garden_compact()

    # ── Actions ──

    def water_flower(self, flower_type: str):
        """Water a single flower with weather-influenced growth."""
        if flower_type not in self.growth:
            print(f"  {self.theme['error']}Unknown flower!{self.theme['reset']}")
            return

        fdef = FLOWERS[flower_type]
        colors = FLOWER_COLORS.get(flower_type, [Fore.WHITE])
        growth = self.growth[flower_type]

        if growth >= MAX_GROWTH:
            print(
                f"\n  {colors[0]}{Style.BRIGHT}"
                f"  {fdef['icon']} {fdef['name']} is already in full bloom!"
                f"{Style.RESET_ALL}"
            )
            return

        # Weather bonus
        w_bonus = WEATHER_TYPES[self.weather]["growth_bonus"]
        base_growth = random.randint(1, 3)
        total_gain = min(base_growth + w_bonus, MAX_GROWTH - growth)

        # Watering animation
        w_icon = WEATHER_TYPES[self.weather]["icon"]
        print(
            f"\n  {self.theme['water']}"
            f"  💧 Watering {fdef['name']}... {w_icon}"
            f"{self.theme['reset']}"
        )
        time.sleep(0.4)

        # Apply growth
        old = growth
        self.growth[flower_type] = min(MAX_GROWTH, growth + total_gain)
        new = self.growth[flower_type]

        if new > old:
            print(
                f"  {self.theme['growth']}"
                f"  🌱 Growth! Level {old} → {new}"
                f"{Style.RESET_ALL}"
            )
            if w_bonus > 0:
                print(
                    f"  {self.theme['dim']}"
                    f"    (+{w_bonus} weather bonus from {WEATHER_TYPES[self.weather]['name']})"
                    f"{self.theme['reset']}"
                )

            time.sleep(0.5)
            self.display_flower(flower_type)

            if new >= MAX_GROWTH:
                print(
                    f"  {colors[0]}{Style.BRIGHT}"
                    f"  🎉 {fdef['name']} has reached FULL BLOOM! 🎉"
                    f"{Style.RESET_ALL}"
                )

        # Update stats
        self.stats["total_waterings"] += 1
        self.stats["total_growth"] = self.total_growth()
        self.stats["max_grown"] = self.max_grown_count()
        if self.weather == "stormy":
            self.stats["stormy_waterings"] += 1
        if self.weather == "starry":
            self.stats["starry_waterings"] += 1

        # Update ecosystem
        self.ecosystem.update(self.total_growth())
        self.stats["visitors"] = self.ecosystem.total_visitors

        # Check achievements
        new_achs = check_achievements(self.stats, self.unlocked_achievements)
        for a in new_achs:
            self.unlocked_achievements.append(a)
            print(
                f"\n  {self.theme['highlight']}"
                f"  🏅 Achievement Unlocked: {format_achievement(a)}"
                f"{self.theme['reset']}"
            )

        self.save_garden()

    def water_all(self):
        """Water every flower."""
        t = self.theme
        print(f"\n  {t['water']}  💧 Watering the entire garden... 💧{t['reset']}")
        for ft in FLOWER_ORDER:
            time.sleep(0.2)
            self.water_flower(ft)

    def change_weather(self):
        """Cycle to new random weather."""
        old = self.weather
        self.weather = get_random_weather(self.season)
        if self.weather not in self.stats["weather_seen"]:
            self.stats["weather_seen"].append(self.weather)
        w = WEATHER_TYPES[self.weather]
        print(
            f"\n  {self.theme['subtitle']}"
            f"  {w['icon']} The weather changed to {w['name']}!"
            f"  {w['description']}"
            f"{self.theme['reset']}"
        )
        self.save_garden()

    def change_theme(self):
        """Cycle through available themes."""
        names = list(THEMES.keys())
        idx = (names.index(self.theme_name) + 1) % len(names)
        self.theme_name = names[idx]
        self.theme = THEMES[self.theme_name]
        print(
            f"\n  {self.theme['highlight']}"
            f"  Theme changed to: {self.theme_name.title()}"
            f"{self.theme['reset']}"
        )
        self.save_garden()

    def show_achievements(self):
        """Display achievement list."""
        t = self.theme
        done, total = get_achievement_progress(self.stats, self.unlocked_achievements)
        print(f"\n  {t['menu_header']}  Achievements ({done}/{total}):{t['reset']}")
        print()
        for aid, ach in ACHIEVEMENTS.items():
            if aid in self.unlocked_achievements:
                print(f"  {t['highlight']}  [x] {format_achievement(aid)}{t['reset']}")
            else:
                print(f"  {t['dim']}  [ ] {ach['icon']}  {ach['name']} - {ach['description']}{t['reset']}")
        print()

    def show_ecosystem(self):
        """Display ecosystem info."""
        t = self.theme
        total_v = self.ecosystem.get_total_visitors()
        active = self.ecosystem.get_visitor_summary()

        print(f"\n  {t['menu_header']}  Garden Ecosystem:{t['reset']}")
        print()

        if not total_v:
            print(
                f"  {t['dim']}  No visitors yet. "
                f"Grow your flowers to attract wildlife!{t['reset']}"
            )
        else:
            print(f"  {t['subtitle']}  Total Visitors:{t['reset']}")
            for ctype, count in total_v.items():
                c = CREATURES[ctype]
                active_count = active.get(ctype, 0)
                active_str = f" ({active_count} here now)" if active_count else ""
                print(
                    f"    {c['icon']}  {c['name']}: {count} visits{active_str}"
                )

        print()
        print(f"  {t['dim']}  Creature attraction thresholds:{t['reset']}")
        for ctype, c in CREATURES.items():
            print(
                f"    {c['icon']}  {c['name']}: "
                f"{c['min_garden_growth']} total growth needed"
            )
        print()

    def reset_garden(self):
        """Reset all progress."""
        for k in self.growth:
            self.growth[k] = 0
        self.stats = {
            "total_waterings": 0,
            "total_growth": 0,
            "max_grown": 0,
            "weather_seen": [self.weather],
            "stormy_waterings": 0,
            "starry_waterings": 0,
            "visitors": {},
            "garden_created": datetime.now().isoformat(),
            "sessions": 1,
        }
        self.unlocked_achievements = []
        self.ecosystem = Ecosystem()
        self.save_garden()
        print(
            f"\n  {self.theme['warning']}"
            f"  🌱 Garden reset! All flowers returned to seeds."
            f"{self.theme['reset']}"
        )

    # ── Menu ──

    def show_menu(self):
        t = self.theme
        print(f"{t['border']}{'─' * 60}{t['reset']}")
        print(f"{t['menu_header']}  What would you like to do?{t['reset']}")
        print()

        # Water flowers section
        print(f"  {t['subtitle']}  Water a Flower:{t['reset']}")
        for i, ft in enumerate(FLOWER_ORDER, 1):
            fdef = FLOWERS[ft]
            g = self.growth[ft]
            colors = FLOWER_COLORS.get(ft, [Fore.WHITE])
            status = "FULL" if g >= MAX_GROWTH else f"Lv.{g}"
            print(
                f"  {t['menu_item']}  {i:>2}. "
                f"{colors[0]}{fdef['icon']} {fdef['name']:<16} "
                f"({status}){Style.RESET_ALL}"
            )

        print()
        print(f"  {t['subtitle']}  Garden:{t['reset']}")
        print(f"  {t['menu_item']}  11. 🌻 View Full Garden (all patterns)")
        print(f"  {t['menu_item']}  12. 💧 Water All Flowers")
        print()
        print(f"  {t['subtitle']}  World:{t['reset']}")
        print(f"  {t['menu_item']}  13. 🌤  Change Weather")
        print(f"  {t['menu_item']}  14. 🎨 Switch Theme ({self.theme_name.title()})")
        print()
        print(f"  {t['subtitle']}  Progress:{t['reset']}")
        print(f"  {t['menu_item']}  15. 🏅 Achievements")
        print(f"  {t['menu_item']}  16. 🦋 Ecosystem")
        print()
        print(f"  {t['menu_item']}  18. 🔄 Reset Garden")
        print(f"  {t['menu_item']}   0. 🚪 Quit")
        print(f"{t['border']}{'─' * 60}{t['reset']}")

    # ── Main Loop ──

    def run(self):
        self.display_dashboard()

        while True:
            self.show_menu()
            try:
                choice = input(
                    f"\n  {self.theme['highlight']}Enter choice: {self.theme['reset']}"
                ).strip()

                if choice in [str(i) for i in range(1, 11)]:
                    idx = int(choice) - 1
                    self.water_flower(FLOWER_ORDER[idx])
                elif choice == "11":
                    self.display_garden_full()
                elif choice == "12":
                    self.water_all()
                elif choice == "13":
                    self.change_weather()
                elif choice == "14":
                    self.change_theme()
                elif choice == "15":
                    self.show_achievements()
                elif choice == "16":
                    self.show_ecosystem()
                elif choice == "18":
                    confirm = input(
                        "  Are you sure you want to reset? (y/N): "
                    ).strip()
                    if confirm.lower() == "y":
                        self.reset_garden()
                elif choice == "0":
                    t = self.theme
                    print(
                        f"\n  {t['growth']}"
                        f"  🌸 Thanks for tending your garden! Goodbye! 🌸"
                        f"{t['reset']}"
                    )
                    break
                else:
                    print(
                        f"  {self.theme['error']}"
                        f"  Invalid choice.{self.theme['reset']}"
                    )

            except KeyboardInterrupt:
                t = self.theme
                print(
                    f"\n\n  {t['growth']}"
                    f"  🌸 Thanks for tending your garden! Goodbye! 🌸"
                    f"{t['reset']}"
                )
                break
            except EOFError:
                break


def main():
    """Entry point for the CLI command."""
    if not COLORS_AVAILABLE:
        print(
            "Note: For the best experience, install colorama: pip install colorama"
        )
        print()

    try:
        garden = FlowerGarden()
        garden.run()
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
