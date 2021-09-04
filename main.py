"""
Project: Microsoft Paint
Author: M.Raahim Rizwan
"""


from utils.button import Button
from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Microsoft Paint")

def init_grid(rows, cols, color):
    """
    Initializes and makes our grid

    :param rows: 
    :params cols: 
    :params color: 
    :return: Grid
    """
    grid = []
    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)
    return grid

def draw_grid(win, grid):
    """
    Draws the grid on the screen
    :param win: Window
    :param grid: Grid
    :return: Grid
    """
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE),
                             (WIDTH, i * PIXEL_SIZE))
        for i in range(COLS + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0),
                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))



def get_row_col_from_pos(pos):
    """
    Returns the x and y coordinates.
    :param pos: Position of x and y coordinates
    :return: Rows and columns (coordinates)
    """
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS: 
        raise IndexError
    return row, col



def draw(win, grid, buttons):
    """
    Fills the window with some color

    :param win: Window
    :param grid: Grid
    :return: Window with filled color 
    """
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    pygame.display.update()

run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK
button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, RED),
    Button(130, button_y, 50, 50, YELLOW),
    Button(190, button_y, 50, 50, BLUE),
    Button(250, button_y, 50, 50, GREEN),
    Button(310, button_y, 50, 50, ORANGE),
    Button(370, button_y, 50, 50, PURPLE),
    Button(430, button_y, 50, 50, WHITE, "Erase", BLACK),
    Button(490, button_y, 50, 50, WHITE, "Clear", BLACK)
    
]

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    drawing_color = button.color
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                    



    draw(WIN, grid, buttons)


pygame.quit()