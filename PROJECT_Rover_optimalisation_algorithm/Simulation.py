import sys
import pygame
from pygame.locals import KEYDOWN, K_q
import numpy as np


# CONSTANTS:
SCREENSIZE = WIDTH, HEIGHT = 600, 400
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
RED = (255, 0, 0)
# VARS:
_VARS = {'surf': False}
grid = []
grid_matrix = np.zeros((3,3), dtype=np.int32)
grid_empty = np.zeros((3,3), dtype=np.int32)

def simulation(grid_size,obstacle, states):
    pygame.init()
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    global grid_matrix, grid_empty
    grid_matrix = np.zeros((grid_size, grid_size), dtype=np.int32) #upddate
    grid_empty = np.zeros((grid_size, grid_size), dtype=np.int32)  #upddate
    fill_grid(grid_size)
    while True:
        checkEvents()
        _VARS['surf'].fill(GREY)
        drawGrid(grid_size)
        obstacle_location(obstacle, grid_size)
        drawLine(states, grid_size)
        pygame.display.update()



def fill_grid(grid_size):
    cnt = 0
    global grid_matrix
    for i in range(grid_size, 0, -1):
        for j in range(0, grid_size, 1):
            field_number = (grid_size * i) - grid_size + j
            grid.insert(cnt, field_number)
            cnt += 1
    cnt = 0
    for i in range(grid_size):
        for k in range(grid_size):
            grid_matrix[i][k] = grid[cnt]
            cnt = cnt + 1


def get_position(x):
    row, col = np.where(grid_matrix == x)
    return (int(row), int(col))


def obstacle_location(x, division):
    CONTAINER_WIDTH_HEIGHT = 300  # Not to be confused with SCREENSIZE
    cont_x, cont_y = 18, 18  # TOP LEFT OF CONTAINER
    cellSize = CONTAINER_WIDTH_HEIGHT / division
    offset = cellSize-14
    for iter in x:
        row, col = get_position(iter)

        x_dim = cont_x + (cellSize * col)
        y_dim = cont_x + (cellSize * row)

        drawRect(x_dim, y_dim, offset)


# Draw filled rectangle at coordinates x,y 18,18 with size width,height
# 60,60
def drawRect(x_dim, y_dim, offset):
    pygame.draw.rect(
     _VARS['surf'], BLACK,
     (x_dim, y_dim, offset, offset)
    )


def drawLine(states, division):

    CONTAINER_WIDTH_HEIGHT = 300  # Not to be confused with SCREENSIZE
    cont_x, cont_y = 18, 18  # TOP LEFT OF CONTAINER
    cellSize = CONTAINER_WIDTH_HEIGHT / division
    offsetU = cellSize/4
    offsetD = cellSize - cont_y - cellSize/4

    for x in states:
        row, col = get_position(x)

        x_dim = cont_x + (cellSize * col) + offsetU
        y_dim = cont_x + (cellSize * row) + offsetU
        x2_dim = cont_x + (cellSize * col) + offsetD
        y2_dim = cont_x + (cellSize * row) + offsetD

        pygame.draw.line(_VARS['surf'], RED, (x_dim, y_dim), (x2_dim, y2_dim), 2)
        pygame.draw.line(_VARS['surf'], RED, (x_dim, y2_dim), (x2_dim, y_dim), 2)



def drawGrid(divisions):

    CONTAINER_WIDTH_HEIGHT = 300  # Not to be confused with SCREENSIZE
    cont_x, cont_y = 10, 10  # TOP LEFT OF CONTAINER

    # DRAW Grid Border:
    # TOP lEFT TO RIGHT
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (cont_x, cont_y),
      (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y), 2)
    # # BOTTOM lEFT TO RIGHT
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (cont_x, CONTAINER_WIDTH_HEIGHT + cont_y),
      (CONTAINER_WIDTH_HEIGHT + cont_x, CONTAINER_WIDTH_HEIGHT + cont_y), 2)
    # # LEFT TOP TO BOTTOM
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (cont_x, cont_y),
      (cont_x, cont_y + CONTAINER_WIDTH_HEIGHT), 2)
    # # RIGHT TOP TO BOTTOM
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y),
      (CONTAINER_WIDTH_HEIGHT + cont_x, CONTAINER_WIDTH_HEIGHT + cont_y), 2)

    # Get cell size, just one since its a square grid.
    cellSize = CONTAINER_WIDTH_HEIGHT/divisions

    # VERTICAL DIVISIONS: (0,1,2) for grid(3) for example
    for x in range(divisions):
        pygame.draw.line(
           _VARS['surf'], BLACK,
           (cont_x + (cellSize * x), cont_y),
           (cont_x + (cellSize * x), CONTAINER_WIDTH_HEIGHT + cont_y), 2)
    # # HORIZONTAl DIVISIONS
        pygame.draw.line(
          _VARS['surf'], BLACK,
          (cont_x, cont_y + (cellSize*x)),
          (cont_x + CONTAINER_WIDTH_HEIGHT, cont_y + (cellSize*x)), 2)


def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()


# if __name__ == '__main__':
#     simulation(3)