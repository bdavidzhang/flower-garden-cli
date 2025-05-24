#!/usr/bin/env python3
"""
Beautiful CLI Flower Garden Game
Water your flowers and watch them grow into stunning patterns!
"""

import math
import time
import os
import json
from typing import Dict, List, Tuple
import random
import sys

# Try to import colorama, fall back to no colors if not available
try:
    from colorama import init, Fore, Back, Style
    init()
    COLORS_AVAILABLE = True
except ImportError:
    # Fallback if colorama is not installed
    class MockFore:
        RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = ""
    class MockStyle:
        BRIGHT = DIM = RESET_ALL = ""
    Fore = MockFore()
    Style = MockStyle()
    COLORS_AVAILABLE = False

class FlowerGarden:
    def __init__(self):
        self.flowers = {
            'spiral_rose': {'growth': 0, 'name': 'Spiral Rose', 'color': Fore.RED},
            'fractal_tree': {'growth': 0, 'name': 'Fractal Tree', 'color': Fore.GREEN},
            'mandala_bloom': {'growth': 0, 'name': 'Mandala Bloom', 'color': Fore.MAGENTA},
            'wave_garden': {'growth': 0, 'name': 'Wave Garden', 'color': Fore.CYAN},
            'star_burst': {'growth': 0, 'name': 'Star Burst', 'color': Fore.YELLOW}
        }
        self.load_garden()
    
    def save_garden(self):
        """Save garden state to file"""
        try:
            # Save to user's home directory for cross-platform compatibility
            save_path = os.path.expanduser('~/.flower_garden_save.json')
            with open(save_path, 'w') as f:
                save_data = {k: v['growth'] for k, v in self.flowers.items()}
                json.dump(save_data, f)
        except:
            pass  # Ignore save errors
    
    def load_garden(self):
        """Load garden state from file"""
        try:
            save_path = os.path.expanduser('~/.flower_garden_save.json')
            with open(save_path, 'r') as f:
                save_data = json.load(f)
                for flower_type, growth in save_data.items():
                    if flower_type in self.flowers:
                        self.flowers[flower_type]['growth'] = min(10, max(0, growth))
        except:
            pass  # Ignore load errors
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def spiral_rose_pattern(self, growth: int) -> List[str]:
        """Generate a spiral rose pattern"""
        size = max(5, growth * 2 + 3)
        center = size // 2
        pattern = []
        
        for y in range(size):
            line = ""
            for x in range(size):
                dx, dy = x - center, y - center
                distance = math.sqrt(dx*dx + dy*dy)
                angle = math.atan2(dy, dx)
                
                # Create spiral effect
                spiral_val = (angle + distance * 0.5) % (math.pi * 2)
                
                if distance <= center - 1:
                    if spiral_val < math.pi * 0.3 * (growth / 10 + 0.1):
                        if distance < center * 0.3:
                            line += "❀"  # Center bloom
                        else:
                            line += "✿" if (x + y) % 2 == 0 else "❀"
                    else:
                        line += "·" if growth > 3 else " "
                else:
                    line += " "
            pattern.append(line)
        
        return pattern
    
    def fractal_tree_pattern(self, growth: int) -> List[str]:
        """Generate a fractal tree pattern"""
        height = max(8, growth + 5)
        width = max(15, growth * 3 + 10)
        pattern = [[' ' for _ in range(width)] for _ in range(height)]
        
        def draw_branch(x, y, length, angle, depth):
            if depth <= 0 or length < 1:
                return
            
            end_x = x + int(length * math.cos(angle))
            end_y = y - int(length * math.sin(angle))
            
            # Draw line from (x,y) to (end_x, end_y)
            steps = max(abs(end_x - x), abs(end_y - y))
            if steps > 0:
                for i in range(steps + 1):
                    curr_x = x + int((end_x - x) * i / steps)
                    curr_y = y + int((end_y - y) * i / steps)
                    if 0 <= curr_x < width and 0 <= curr_y < height:
                        if depth > growth * 0.3:
                            pattern[curr_y][curr_x] = '█'
                        elif depth > growth * 0.1:
                            pattern[curr_y][curr_x] = '▓'
                        else:
                            pattern[curr_y][curr_x] = '░'
            
            # Add leaves/flowers at branch ends
            if depth <= 2 and growth > 3:
                if 0 <= end_x < width and 0 <= end_y < height:
                    pattern[end_y][end_x] = '❀' if growth > 6 else '·'
            
            # Recursive branches
            if depth > 1:
                new_length = length * 0.7
                draw_branch(end_x, end_y, new_length, angle - 0.5, depth - 1)
                draw_branch(end_x, end_y, new_length, angle + 0.5, depth - 1)
        
        # Start tree from bottom center
        start_x = width // 2
        start_y = height - 1
        draw_branch(start_x, start_y, max(3, growth), math.pi/2, min(5, growth // 2 + 2))
        
        return [''.join(row) for row in pattern]
    
    def mandala_bloom_pattern(self, growth: int) -> List[str]:
        """Generate a mandala bloom pattern"""
        size = max(9, growth * 2 + 5)
        if size % 2 == 0:
            size += 1
        center = size // 2
        pattern = []
        
        for y in range(size):
            line = ""
            for x in range(size):
                dx, dy = x - center, y - center
                distance = math.sqrt(dx*dx + dy*dy)
                angle = math.atan2(dy, dx)
                
                # Create mandala rings
                ring = int(distance)
                petal_count = max(4, ring * 2)
                petal_angle = (angle * petal_count) % (math.pi * 2)
                
                if distance <= center:
                    if ring == 0:
                        line += "◉"  # Center
                    elif ring <= growth // 2 + 1:
                        if petal_angle < math.pi * 0.4:
                            if ring % 2 == 0:
                                line += "❀" if growth > 5 else "●"
                            else:
                                line += "✿" if growth > 3 else "○"
                        else:
                            line += "·" if growth > 2 else " "
                    else:
                        line += " "
                else:
                    line += " "
            pattern.append(line)
        
        return pattern
    
    def wave_garden_pattern(self, growth: int) -> List[str]:
        """Generate a wave garden pattern"""
        width = max(20, growth * 3 + 15)
        height = max(8, growth + 6)
        pattern = []
        
        for y in range(height):
            line = ""
            for x in range(width):
                # Create multiple overlapping waves
                wave1 = math.sin(x * 0.3 + growth * 0.5) * (growth / 10 + 0.5)
                wave2 = math.sin(x * 0.1 + growth * 0.3) * (growth / 15 + 0.3)
                wave_height = (wave1 + wave2) * 2 + height // 2
                
                if abs(y - wave_height) < 1:
                    if growth > 6:
                        line += "❀" if x % 3 == 0 else "~"
                    elif growth > 3:
                        line += "✿" if x % 4 == 0 else "~"
                    else:
                        line += "~"
                elif abs(y - wave_height) < 1.5 and growth > 2:
                    line += "·"
                else:
                    line += " "
            pattern.append(line)
        
        return pattern
    
    def star_burst_pattern(self, growth: int) -> List[str]:
        """Generate a star burst pattern"""
        size = max(9, growth * 2 + 5)
        if size % 2 == 0:
            size += 1
        center = size // 2
        pattern = []
        
        for y in range(size):
            line = ""
            for x in range(size):
                dx, dy = x - center, y - center
                distance = math.sqrt(dx*dx + dy*dy)
                angle = math.atan2(dy, dx)
                
                # Create star rays
                ray_count = max(6, growth + 4)
                ray_angle = (angle * ray_count / (2 * math.pi)) % 1
                
                if distance <= center:
                    if distance < 1:
                        line += "★"  # Center star
                    elif ray_angle < 0.1 and distance <= growth + 2:
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
    
    def display_flower(self, flower_type: str):
        """Display a single flower pattern"""
        flower = self.flowers[flower_type]
        growth = flower['growth']
        
        print(f"\n{flower['color']}{Style.BRIGHT}{flower['name']}{Style.RESET_ALL}")
        print(f"Growth Level: {growth}/10 {'█' * growth}{'░' * (10 - growth)}")
        
        if growth == 0:
            print("🌱 A tiny seed waiting to be watered...")
            return
        
        # Generate pattern based on flower type
        if flower_type == 'spiral_rose':
            pattern = self.spiral_rose_pattern(growth)
        elif flower_type == 'fractal_tree':
            pattern = self.fractal_tree_pattern(growth)
        elif flower_type == 'mandala_bloom':
            pattern = self.mandala_bloom_pattern(growth)
        elif flower_type == 'wave_garden':
            pattern = self.wave_garden_pattern(growth)
        elif flower_type == 'star_burst':
            pattern = self.star_burst_pattern(growth)
        
        print(f"\n{flower['color']}")
        for line in pattern:
            print(f"  {line}")
        print(Style.RESET_ALL)
    
    def water_flower(self, flower_type: str):
        """Water a flower and show growth animation"""
        if flower_type not in self.flowers:
            print("Unknown flower type!")
            return
        
        flower = self.flowers[flower_type]
        if flower['growth'] >= 10:
            print(f"\n{flower['color']}✨ {flower['name']} is already fully grown! ✨{Style.RESET_ALL}")
            return
        
        print(f"\n{Fore.CYAN}💧 Watering {flower['name']}... 💧{Style.RESET_ALL}")
        time.sleep(0.5)
        
        # Show growth animation
        old_growth = flower['growth']
        flower['growth'] = min(10, flower['growth'] + random.randint(1, 3))
        
        if flower['growth'] > old_growth:
            print(f"{Fore.GREEN}🌱 Growth! Level {old_growth} → {flower['growth']} 🌱{Style.RESET_ALL}")
            time.sleep(1)
            self.display_flower(flower_type)
            
            if flower['growth'] == 10:
                print(f"\n{flower['color']}🎉 {flower['name']} has reached full bloom! 🎉{Style.RESET_ALL}")
        
        self.save_garden()
    
    def display_garden(self):
        """Display the entire garden"""
        self.clear_screen()
        print(f"{Style.BRIGHT}🌺 Welcome to Your Magical Flower Garden! 🌺{Style.RESET_ALL}")
        print("=" * 50)
        
        for flower_type in self.flowers:
            self.display_flower(flower_type)
    
    def show_menu(self):
        """Show the main menu"""
        print("\n" + "=" * 50)
        print("What would you like to do?")
        print("1. Water Spiral Rose")
        print("2. Water Fractal Tree") 
        print("3. Water Mandala Bloom")
        print("4. Water Wave Garden")
        print("5. Water Star Burst")
        print("6. View Garden")
        print("7. Water All Flowers")
        print("8. Reset Garden")
        print("9. Quit")
        print("=" * 50)
    
    def reset_garden(self):
        """Reset all flowers to seed state"""
        for flower in self.flowers.values():
            flower['growth'] = 0
        self.save_garden()
        print(f"\n{Fore.YELLOW}🌱 Garden reset! All flowers are now seeds. 🌱{Style.RESET_ALL}")
    
    def water_all(self):
        """Water all flowers"""
        print(f"\n{Fore.CYAN}💧 Watering the entire garden... 💧{Style.RESET_ALL}")
        for flower_type in self.flowers:
            time.sleep(0.3)
            self.water_flower(flower_type)
    
    def run(self):
        """Main game loop"""
        self.display_garden()
        
        while True:
            self.show_menu()
            try:
                choice = input("\nEnter your choice (1-9): ").strip()
                
                if choice == '1':
                    self.water_flower('spiral_rose')
                elif choice == '2':
                    self.water_flower('fractal_tree')
                elif choice == '3':
                    self.water_flower('mandala_bloom')
                elif choice == '4':
                    self.water_flower('wave_garden')
                elif choice == '5':
                    self.water_flower('star_burst')
                elif choice == '6':
                    self.display_garden()
                elif choice == '7':
                    self.water_all()
                elif choice == '8':
                    confirm = input("Are you sure you want to reset the garden? (y/N): ")
                    if confirm.lower() == 'y':
                        self.reset_garden()
                elif choice == '9':
                    print(f"\n{Fore.GREEN}🌸 Thanks for tending your garden! Goodbye! 🌸{Style.RESET_ALL}")
                    break
                else:
                    print("Invalid choice! Please enter 1-9.")
                    
            except KeyboardInterrupt:
                print(f"\n\n{Fore.GREEN}🌸 Thanks for tending your garden! Goodbye! 🌸{Style.RESET_ALL}")
                break
            except EOFError:
                break

def main():
    """Entry point for the CLI command"""
    if not COLORS_AVAILABLE:
        print("Note: For the best experience, install colorama: pip install colorama")
        print()
    
    try:
        garden = FlowerGarden()
        garden.run()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()