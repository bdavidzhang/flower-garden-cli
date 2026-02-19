"""
Pattern generation engine for Flower Garden CLI v2.0
10 unique mathematical flower patterns with enhanced ASCII art.
"""

import math
import random
from typing import List


def spiral_rose_pattern(growth: int) -> List[str]:
    """Fibonacci spiral rose with layered petals."""
    size = max(7, growth * 2 + 5)
    center = size // 2
    pattern = []

    for y in range(size):
        line = ""
        for x in range(size):
            dx, dy = x - center, y - center
            distance = math.sqrt(dx * dx + dy * dy)
            angle = math.atan2(dy, dx)

            spiral_val = (angle + distance * 0.5) % (math.pi * 2)
            petal_layer = (angle * 3 + distance * 0.8) % (math.pi * 2)

            if distance <= center - 1:
                if distance < center * 0.2 and growth > 2:
                    line += "◉" if (x + y) % 2 == 0 else "❀"
                elif spiral_val < math.pi * 0.35 * (growth / 10 + 0.1):
                    if petal_layer < math.pi * 0.5:
                        line += "❀"
                    else:
                        line += "✿"
                elif petal_layer < math.pi * 0.2 and growth > 5:
                    line += "·"
                else:
                    line += "·" if growth > 3 else " "
            else:
                line += " "
        pattern.append(line)
    return pattern


def fractal_tree_pattern(growth: int) -> List[str]:
    """Recursive fractal tree with leaves and blossoms."""
    height = max(10, growth + 7)
    width = max(20, growth * 3 + 14)
    grid = [[" " for _ in range(width)] for _ in range(height)]

    def draw_branch(x, y, length, angle, depth):
        if depth <= 0 or length < 1:
            return
        end_x = x + int(length * math.cos(angle))
        end_y = y - int(length * math.sin(angle))
        steps = max(abs(end_x - x), abs(end_y - y))
        if steps > 0:
            for i in range(steps + 1):
                cx = x + int((end_x - x) * i / steps)
                cy = y + int((end_y - y) * i / steps)
                if 0 <= cx < width and 0 <= cy < height:
                    if depth > growth * 0.4:
                        grid[cy][cx] = "█"
                    elif depth > growth * 0.2:
                        grid[cy][cx] = "▓"
                    else:
                        grid[cy][cx] = "░"
        if depth <= 2 and growth > 3:
            if 0 <= end_x < width and 0 <= end_y < height:
                if growth > 7:
                    grid[end_y][end_x] = "❀"
                elif growth > 5:
                    grid[end_y][end_x] = "✿"
                else:
                    grid[end_y][end_x] = "·"
        if depth > 1:
            new_len = length * 0.68
            spread = 0.45 + growth * 0.02
            draw_branch(end_x, end_y, new_len, angle - spread, depth - 1)
            draw_branch(end_x, end_y, new_len, angle + spread, depth - 1)
            if depth > 3 and growth > 6:
                draw_branch(end_x, end_y, new_len * 0.7, angle, depth - 2)

    start_x = width // 2
    start_y = height - 1
    trunk_len = max(3, growth * 0.8 + 2)
    max_depth = min(6, growth // 2 + 2)
    draw_branch(start_x, start_y, trunk_len, math.pi / 2, max_depth)

    return ["".join(row) for row in grid]


def mandala_bloom_pattern(growth: int) -> List[str]:
    """Geometric mandala with concentric petal rings."""
    size = max(11, growth * 2 + 7)
    if size % 2 == 0:
        size += 1
    center = size // 2
    pattern = []

    for y in range(size):
        line = ""
        for x in range(size):
            dx, dy = x - center, y - center
            distance = math.sqrt(dx * dx + dy * dy)
            angle = math.atan2(dy, dx)

            ring = int(distance)
            petal_count = max(4, ring * 2 + 2)
            petal_angle = (angle * petal_count) % (math.pi * 2)

            if distance <= center:
                if ring == 0:
                    line += "◉"
                elif ring <= growth // 2 + 2:
                    if petal_angle < math.pi * 0.35:
                        chars = ["❀", "✿", "●", "○"]
                        idx = ring % len(chars)
                        if growth > 6 - idx:
                            line += chars[idx]
                        else:
                            line += "·"
                    else:
                        line += "·" if growth > 2 else " "
                else:
                    line += " "
            else:
                line += " "
        pattern.append(line)
    return pattern


def wave_garden_pattern(growth: int) -> List[str]:
    """Layered sine waves with flowers cresting on top."""
    width = max(25, growth * 3 + 18)
    height = max(10, growth + 8)
    pattern = []

    for y in range(height):
        line = ""
        for x in range(width):
            wave1 = math.sin(x * 0.3 + growth * 0.5) * (growth / 10 + 0.5)
            wave2 = math.sin(x * 0.15 + growth * 0.3) * (growth / 12 + 0.3)
            wave3 = math.sin(x * 0.08 + growth * 0.7) * (growth / 15 + 0.2)
            wave_h = (wave1 + wave2 + wave3) * 1.8 + height // 2

            diff = abs(y - wave_h)
            if diff < 0.6:
                if growth > 7:
                    line += "❀" if x % 3 == 0 else "~"
                elif growth > 4:
                    line += "✿" if x % 4 == 0 else "~"
                else:
                    line += "~"
            elif diff < 1.2 and growth > 2:
                line += "·"
            elif diff < 2.0 and growth > 6:
                line += " " if x % 2 else "·"
            else:
                line += " "
        pattern.append(line)
    return pattern


def star_burst_pattern(growth: int) -> List[str]:
    """Radiating star with pulsing rays."""
    size = max(11, growth * 2 + 7)
    if size % 2 == 0:
        size += 1
    center = size // 2
    pattern = []

    for y in range(size):
        line = ""
        for x in range(size):
            dx, dy = x - center, y - center
            distance = math.sqrt(dx * dx + dy * dy)
            angle = math.atan2(dy, dx)

            ray_count = max(6, growth + 4)
            ray_angle = (angle * ray_count / (2 * math.pi)) % 1
            pulse = math.sin(distance * 0.5) * 0.5 + 0.5

            if distance <= center:
                if distance < 1.5:
                    line += "★"
                elif ray_angle < 0.08 + pulse * 0.04 and distance <= growth + 3:
                    if distance < growth // 2 + 2:
                        line += "✦" if growth > 5 else "✧"
                    else:
                        line += "·"
                elif distance <= growth // 3 + 1:
                    line += "·" if growth > 3 else " "
                else:
                    line += " "
            else:
                line += " "
        pattern.append(line)
    return pattern


# ── New v2.0 flowers ──


def crystal_lotus_pattern(growth: int) -> List[str]:
    """Symmetric crystal lotus with diamond facets."""
    size = max(11, growth * 2 + 7)
    if size % 2 == 0:
        size += 1
    center = size // 2
    pattern = []

    for y in range(size):
        line = ""
        for x in range(size):
            dx, dy = x - center, y - center
            distance = math.sqrt(dx * dx + dy * dy)
            angle = math.atan2(dy, dx)

            # Diamond shape using taxicab distance
            diamond = abs(dx) + abs(dy)
            petals = 8
            petal_val = math.cos(angle * petals) * (growth / 10 + 0.3)

            if distance < 1:
                line += "◆"
            elif diamond <= growth + 2 and petal_val > 0.2:
                if distance < growth * 0.4:
                    line += "◇" if (x + y) % 2 == 0 else "◆"
                elif distance < growth * 0.7:
                    line += "◇"
                else:
                    line += "·"
            elif diamond <= growth + 1 and growth > 4:
                line += "·"
            else:
                line += " "
        pattern.append(line)
    return pattern


def phoenix_fern_pattern(growth: int) -> List[str]:
    """Curling fern fronds that spiral upward like flames."""
    height = max(12, growth + 8)
    width = max(25, growth * 3 + 15)
    grid = [[" " for _ in range(width)] for _ in range(height)]

    cx = width // 2

    # Main stem
    for y in range(height):
        if y >= height - growth - 2:
            if 0 <= cx < width:
                grid[y][cx] = "│"

    # Fern fronds curling from stem
    num_fronds = min(growth, 8)
    for i in range(num_fronds):
        side = 1 if i % 2 == 0 else -1
        start_y = height - 2 - i
        frond_len = min(growth - i // 2, 8)
        for j in range(frond_len):
            fy = start_y - j
            fx = cx + side * (j + 1)
            curl = int(math.sin(j * 0.8) * (j * 0.3))
            fy += curl
            if 0 <= fx < width and 0 <= fy < height:
                if j >= frond_len - 2 and growth > 5:
                    grid[fy][fx] = "❋"
                elif j >= frond_len - 3:
                    grid[fy][fx] = "✦"
                else:
                    grid[fy][fx] = "╲" if side > 0 else "╱"
            # Sub-fronds
            if j > 1 and j < frond_len - 1 and growth > 3:
                sy = fy - 1
                sx = fx + side
                if 0 <= sx < width and 0 <= sy < height:
                    grid[sy][sx] = "·"

    return ["".join(row) for row in grid]


def galaxy_orchid_pattern(growth: int) -> List[str]:
    """Swirling galaxy-shaped orchid with nebula dust."""
    size = max(13, growth * 2 + 9)
    if size % 2 == 0:
        size += 1
    center = size // 2
    pattern = []

    for y in range(size):
        line = ""
        for x in range(size):
            dx, dy = x - center, y - center
            distance = math.sqrt(dx * dx + dy * dy)
            angle = math.atan2(dy, dx)

            # Spiral arms
            arm_count = 3
            spiral = (angle + distance * 0.4) % (math.pi * 2 / arm_count)
            arm_width = math.pi * 0.15 * (growth / 10 + 0.2)

            if distance < 1.5:
                line += "✶"
            elif distance <= center - 1:
                if spiral < arm_width and distance <= growth + 3:
                    if distance < growth * 0.3:
                        line += "✦"
                    elif distance < growth * 0.6:
                        line += "✧"
                    else:
                        line += "·"
                elif (distance * 7 + angle * 5) % 6 < 0.5 and growth > 5:
                    line += "·"  # Nebula dust
                else:
                    line += " "
            else:
                line += " "
        pattern.append(line)
    return pattern


def thunder_vine_pattern(growth: int) -> List[str]:
    """Lightning-bolt vines crackling with energy."""
    height = max(12, growth + 8)
    width = max(30, growth * 3 + 18)
    grid = [[" " for _ in range(width)] for _ in range(height)]

    # Generate zigzag vine paths
    num_vines = min(2 + growth // 3, 5)
    random.seed(42)  # Consistent pattern

    for v in range(num_vines):
        x = width // (num_vines + 1) * (v + 1)
        for y in range(height - 1, max(0, height - growth - 3), -1):
            if 0 <= x < width and 0 <= y < height:
                grid[y][x] = "║" if growth > 4 else "│"
            # Zigzag
            zag = random.choice([-2, -1, 0, 1, 2])
            x = max(1, min(width - 2, x + zag))

            # Side branches
            if y % 3 == 0 and growth > 2:
                bdir = random.choice([-1, 1])
                for bx in range(1, min(growth // 2 + 1, 5)):
                    nx = x + bdir * bx
                    ny = y - (bx % 2)
                    if 0 <= nx < width and 0 <= ny < height:
                        if bx == min(growth // 2, 4):
                            grid[ny][nx] = "✦" if growth > 6 else "·"
                        else:
                            grid[ny][nx] = "─"

            # Sparks
            if growth > 7 and y % 4 == 0:
                for _ in range(2):
                    sx = x + random.randint(-3, 3)
                    sy = y + random.randint(-1, 1)
                    if 0 <= sx < width and 0 <= sy < height and grid[sy][sx] == " ":
                        grid[sy][sx] = "·"

    random.seed()  # Reset seed
    return ["".join(row) for row in grid]


def aurora_lily_pattern(growth: int) -> List[str]:
    """Flowing aurora borealis shaped like a lily."""
    width = max(30, growth * 3 + 20)
    height = max(12, growth + 8)
    pattern = []

    for y in range(height):
        line = ""
        for x in range(width):
            # Multiple flowing bands
            band1 = math.sin(x * 0.15 + growth * 0.3) * 2.5
            band2 = math.sin(x * 0.1 + 1.5 + growth * 0.2) * 2.0
            band3 = math.sin(x * 0.2 + 3.0 + growth * 0.4) * 1.5

            # Shift bands vertically
            h1 = height * 0.25 + band1
            h2 = height * 0.45 + band2
            h3 = height * 0.65 + band3

            d1 = abs(y - h1)
            d2 = abs(y - h2)
            d3 = abs(y - h3)

            threshold = 0.6 + growth * 0.1
            char = " "

            if d1 < threshold and growth > 1:
                if d1 < 0.3:
                    char = "▓"
                else:
                    char = "░"
            elif d2 < threshold and growth > 3:
                if d2 < 0.3:
                    char = "▓"
                else:
                    char = "░"
            elif d3 < threshold and growth > 5:
                if d3 < 0.3:
                    char = "▓"
                else:
                    char = "░"

            # Shimmer highlights
            if char != " " and growth > 7:
                shimmer = math.sin(x * 0.5 + y * 0.3) > 0.7
                if shimmer:
                    char = "✧"

            # Lily blooms on the bands
            if char != " " and x % (12 - growth) == 0 and growth > 4:
                char = "❀"

            line += char
        pattern.append(line)
    return pattern


# Pattern registry
PATTERNS = {
    "spiral_rose": spiral_rose_pattern,
    "fractal_tree": fractal_tree_pattern,
    "mandala_bloom": mandala_bloom_pattern,
    "wave_garden": wave_garden_pattern,
    "star_burst": star_burst_pattern,
    "crystal_lotus": crystal_lotus_pattern,
    "phoenix_fern": phoenix_fern_pattern,
    "galaxy_orchid": galaxy_orchid_pattern,
    "thunder_vine": thunder_vine_pattern,
    "aurora_lily": aurora_lily_pattern,
}


def generate_pattern(flower_type: str, growth: int) -> List[str]:
    """Generate the pattern for a given flower type and growth level."""
    fn = PATTERNS.get(flower_type)
    if fn is None:
        return [f"Unknown flower type: {flower_type}"]
    return fn(growth)
