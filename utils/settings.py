# Importing pygame
import pygame
# Initializing pygame
pygame.init()
pygame.font.init()
# Defining colors
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = 	(0,0,255)
ORANGE = (255,165,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
GREEN = (0,255,0)
PURPLE = (128,0,128)

# Constant variables of our game
FPS = 60
WIDTH, HEIGHT = 600, 700

ROWS = COLS = 100

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = False

def get_font(size):
    """
    Returns the font with a specific size
    """
    return pygame.font.SysFont("comicsans", size)