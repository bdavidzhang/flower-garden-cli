# Flower Garden CLI v2.0

**A living, breathing terminal garden with weather, seasons, ecosystems, and achievements.**

Grow 10 unique flowers with mathematical ASCII art patterns, watch butterflies visit, unlock achievements, and experience dynamic weather -- all from your terminal.

![Python Version](https://img.shields.io/badge/python-3.7+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-2.0.0-orange)

If you have `uv` installed:
```bash
uvx --from flower-garden-cli garden
```

## What's New in v2.0

- **10 Flower Types** -- 5 new Tier II flowers with unique patterns
- **Weather & Seasons** -- sun, rain, wind, mist, storms, and starry nights affect growth
- **Ecosystem** -- butterflies, bees, fireflies, ladybugs, hummingbirds, and dragonflies visit your garden
- **14 Achievements** -- unlock milestones as you grow
- **3 Color Themes** -- Garden, Midnight, and Sunset
- **Dashboard UI** -- compact two-column overview with stats bar
- **Weather Growth Bonus** -- storms give +3 bonus, rain gives +2
- **Persistent Stats** -- tracks total waterings, sessions, visitors, and more

## Flowers

### Tier I (Original)
| Flower | Pattern |
|--------|---------|
| Spiral Rose | Fibonacci spiral with layered petals |
| Fractal Tree | Recursive branching with blossoms |
| Mandala Bloom | Concentric geometric petal rings |
| Wave Garden | Layered sine waves with flower crests |
| Star Burst | Radiating star with pulsing rays |

### Tier II (New in v2.0)
| Flower | Pattern |
|--------|---------|
| Crystal Lotus | Symmetric diamond facets |
| Phoenix Fern | Curling fronds that spiral like flames |
| Galaxy Orchid | Swirling spiral arms with nebula dust |
| Thunder Vine | Lightning-bolt vines with energy sparks |
| Aurora Lily | Flowing aurora bands with shimmer highlights |

## Quick Start

```bash
pip install flower-garden-cli
flower-garden
```

Alternative command:
```bash
garden
```

## Installation

### pip (Recommended)
```bash
pip install flower-garden-cli

# Or from GitHub
pip install git+https://github.com/bdavidzhang/flower-garden-cli.git
```

### Local Development
```bash
git clone https://github.com/bdavidzhang/flower-garden-cli.git
cd flower-garden-cli
pip install -e .
flower-garden
```

## How to Play

1. Launch with `flower-garden` or `garden`
2. Pick a flower to water (1-10)
3. Watch it grow with mathematical ASCII patterns
4. Growth is boosted by weather (storms = +3, rain = +2)
5. Attract wildlife as your garden grows
6. Unlock achievements for milestones
7. Switch themes with option 14
8. Progress saves automatically between sessions

### Menu

```
Water a Flower:
  1-10  Water individual flowers (Tier I and II)

Garden:
  11    View Full Garden (all patterns)
  12    Water All Flowers

World:
  13    Change Weather
  14    Switch Theme (Garden / Midnight / Sunset)

Progress:
  15    Achievements
  16    Ecosystem

  18    Reset Garden
   0    Quit
```

## Weather System

Weather changes based on real-world seasons and affects growth bonuses:

| Weather | Bonus | Description |
|---------|-------|-------------|
| Sunny | +1 | Warm sunshine |
| Rainy | +2 | Gentle rain nourishes flowers |
| Windy | +0 | Brisk wind sweeps through |
| Misty | +1 | Soft mist drifts through |
| Starry Night | +1 | Stars twinkle above |
| Stormy | +3 | Thunder and lightning |

## Ecosystem

As your garden grows, creatures come to visit:

| Creature | Growth Needed |
|----------|---------------|
| Ladybug | 5 |
| Bee | 10 |
| Butterfly | 15 |
| Firefly | 20 |
| Hummingbird | 30 |
| Dragonfly | 40 |

## Achievements

14 achievements to unlock, including:
- **First Drop** -- Water your first flower
- **Master Gardener** -- Fully grow all 10 flowers
- **Storm Chaser** -- Water during a storm
- **Butterfly Whisperer** -- Attract 5 butterflies
- **Century Garden** -- Reach 100 total growth levels

## Project Structure

```
flower-garden-cli/
  flower_garden_cli/
    __init__.py         # Package init, version
    main.py             # Game loop, UI, FlowerGarden class
    patterns.py         # 10 mathematical pattern generators
    colors.py           # Color system, themes, gradients
    weather.py          # Weather and seasons engine
    ecosystem.py        # Creature spawning and movement
    achievements.py     # Achievement definitions and tracking
  pyproject.toml
  README.md
  LICENSE
  Dockerfile
```

## Requirements

- **Python**: 3.7+
- **Dependencies**: colorama (>=0.4.0)
- **Platform**: Windows, macOS, Linux

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions welcome! Please open a Pull Request.

---

*Grow your digital garden, one flower at a time*
