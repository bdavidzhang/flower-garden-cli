# 🌺 Flower Garden CLI

**Beautiful CLI flower garden game - water flowers and watch them grow into stunning patterns!**

Transform your terminal into a magical garden where you can nurture 5 different types of flowers, each growing into unique mathematical patterns and fractals.

![Flower Garden Demo](https://img.shields.io/badge/demo-terminal-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.7+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🌸 Features

- **5 Unique Flower Types**: Each with distinct mathematical patterns
  - 🌹 **Spiral Rose** - Fibonacci spirals with blooming petals
  - 🌳 **Fractal Tree** - Recursive branching with leaves
  - 🌺 **Mandala Bloom** - Geometric circular patterns
  - 🌊 **Wave Garden** - Flowing sine wave patterns
  - ⭐ **Star Burst** - Radiating star patterns

- **Growth System**: 10 levels of growth for each flower
- **Persistent Save**: Your garden state is automatically saved
- **Colorful Display**: Beautiful terminal colors (with colorama)
- **Interactive Menu**: Easy-to-use command interface

## 🚀 Quick Start

Install and run with a single command:

```bash
pip install flower-garden-cli
flower-garden
```

Alternative command:
```bash
garden
```

## 📦 Installation Methods

### Method 1: pip install (Recommended)
```bash
# Install from PyPI (when published)
pip install flower-garden-cli

# Or install from GitHub
pip install git+https://github.com/yourusername/flower-garden-cli.git
```

### Method 2: Local Development
```bash
# Clone the repository
git clone https://github.com/yourusername/flower-garden-cli.git
cd flower-garden-cli

# Install in development mode
pip install -e .

# Run the game
flower-garden
```

### Method 3: Direct from Source
```bash
# Download and run directly
curl -O https://raw.githubusercontent.com/yourusername/flower-garden-cli/main/flower_garden_cli/main.py
python main.py
```

## 🎮 How to Play

1. **Launch the game**: Run `flower-garden` in your terminal
2. **Choose an action**: Select from the numbered menu options
3. **Water flowers**: Watch them grow from seeds to beautiful patterns
4. **Enjoy the patterns**: Each growth level reveals more complexity
5. **Save automatically**: Your progress is saved between sessions

### Menu Options:
- `1-5`: Water individual flower types
- `6`: View your entire garden
- `7`: Water all flowers at once
- `8`: Reset garden (start over)
- `9`: Quit game

## 🎨 Flower Types Preview

```
🌹 Spiral Rose (Level 5)    🌳 Fractal Tree (Level 7)
    ·✿❀✿·                      ░▓█▓░
   ✿❀ ❀ ❀✿                    ░▓███▓░❀
  ❀  ❀❀❀  ❀                  ░▓█████▓░
   ✿❀ ❀ ❀✿                    ▓███████▓
    ·✿❀✿·                      █████████
```

## 🛠️ Development

### Project Structure
```
flower-garden-cli/
├── flower_garden_cli/
│   ├── __init__.py
│   └── main.py
├── pyproject.toml
├── README.md
├── LICENSE
└── tests/
    └── test_main.py
```

### Local Development Setup
```bash
# Clone and setup
git clone https://github.com/yourusername/flower-garden-cli.git
cd flower-garden-cli

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black flower_garden_cli/
```

## 📋 Requirements

- **Python**: 3.7 or higher
- **Dependencies**: 
  - `colorama` (for colored terminal output)
- **Platform**: Cross-platform (Windows, macOS, Linux)

## 🔧 Publishing Your Package

### To PyPI (Python Package Index):

1. **Prepare your package**:
   ```bash
   python -m build
   ```

2. **Upload to TestPyPI first**:
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

3. **Test the installation**:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ flower-garden-cli
   ```

4. **Upload to PyPI**:
   ```bash
   python -m twine upload dist/*
   ```

### To GitHub Releases:
1. Create a new release on GitHub
2. Upload the built wheel and tar.gz files
3. Users can install with: `pip install https://github.com/user/repo/releases/download/v1.0.0/flower_garden_cli-1.0.0-py3-none-any.whl`

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🌟 Support

If you enjoy this project, please give it a ⭐ on GitHub!

**Issues?** Please report them [here](https://github.com/yourusername/flower-garden-cli/issues).

---

*Grow your digital garden, one flower at a time* 🌱✨
