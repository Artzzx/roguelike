# Roguelike Dungeon Crawler

A turn-based dungeon exploration game with procedurally generated levels built in Python.

## Features

- Procedural level generation
- Turn-based combat system
- Character progression/stats
- Item and equipment system
- Enemy variety with different behaviors

## Requirements

- Python 3.11+
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository
   ```
   git clone <your-repository-url>
   cd roguelike
   ```

2. Set up a virtual environment
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

## Running the Game

```
python main.py
```

## Project Structure

- `engine/`: Core game engine functionality
- `map/`: Map generation and management
- `entity/`: Game entities (player, enemies, items)
- `components/`: Component system for entities
- `factories/`: Factory classes for creating game objects
- `systems/`: Game systems (combat, progression, etc.)
- `ui/`: User interface elements
- `utils/`: Utility functions and helpers

## Development

### Testing

```
pytest
```

### Code Formatting

```
black .
```

## License

[MIT License](LICENSE)