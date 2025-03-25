"""
Basic config, to be updated
"""

# Window settings
WINDOW_TITLE = "Roguelike Dungeon Crawler"
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

# Map settings
MAP_WIDTH = 80
MAP_HEIGHT = 43
ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30

# FOV settings
FOV_ALGORITHM = 0  # Default algorithm
FOV_LIGHT_WALLS = True
FOV_RADIUS = 8

# Game settings
LEVEL_UP_BASE = 200
LEVEL_UP_FACTOR = 150

# Colors
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_BLUE = (0, 0, 255)

# Game messages
WELCOME_TEXT = "Welcome to the Roguelike Dungeon Crawler!"

# Player settings
PLAYER_START_HP = 30
PLAYER_START_DEFENSE = 2
PLAYER_START_POWER = 5

# Enemy settings
ENEMY_TYPES = {
    "orc": {
        "char": "o",
        "color": (63, 127, 63),
        "name": "Orc",
        "hp": 10,
        "defense": 0,
        "power": 3
    },
    "troll": {
        "char": "T",
        "color": (0, 127, 0),
        "name": "Troll",
        "hp": 16,
        "defense": 1,
        "power": 4
    }
}

# Item settings
ITEM_TYPES = {
    "health_potion": {
        "char": "!",
        "color": (127, 0, 255),
        "name": "Health Potion",
        "heal_amount": 4
    },
    "lightning_scroll": {
        "char": "#",
        "color": (255, 255, 0),
        "name": "Lightning Scroll",
        "damage": 20,
        "max_range": 5
    }
}