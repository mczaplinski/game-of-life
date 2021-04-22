import random
import pygame

# global
col = 160
row = 90
s_width = 1280
s_height = 790
block_size = 10
top_left_x = 0
top_left_y = 0

# colors
grid_line_color = (120, 125, 130)
alive_color = (255, 255, 255)
border_color = (180, 185, 190)
background_color = (55, 57, 67)

# game parameters
num_seeds = 40


class CellState:
    DEAD = 0
    ALIVE = 1

def draw(window, grid):

    # Black Background
    window.fill(background_color)

    # Draw Grid Lines
    for i in range(col):
        # draw grey vertical lines
        pygame.draw.line(window, grid_line_color, (top_left_x + i * block_size, top_left_y),
                         (top_left_x + i * block_size, top_left_y + s_height))
    for j in range(row):
        # draw grey horizontal lines
        pygame.draw.line(window, grid_line_color, (top_left_x, top_left_y + j * block_size),
                         (top_left_x + s_width, top_left_y + j * block_size))

    # Draw Cells
    for i in range(col):
        for j in range(row):
            if grid[i][j] == CellState.ALIVE:
                pygame.draw.rect(window,
                                 alive_color,
                                 (top_left_x + i * block_size, top_left_y + j * block_size,
                                  block_size, block_size)
                                 )

    # draw rectangular border around play area
    pygame.draw.rect(window, border_color, (top_left_x, top_left_y, s_width, s_height), 2)

    pygame.display.update()


def update_grid(grid):
    new_grid = grid.copy()
    for i in range(col):
        for j in range(row):

            # count number of alive cells in neighborhood
            num_alive_neighbors = 0
            for m in range(-1, 2, 1):
                # check left/right border
                if i + m < 0 or i + m >= col - 1:
                    continue
                for n in range(-1, 2, 1):
                    # check top down border
                    if j + n < 0 or j + n >= row - 1:
                        continue
                    # ignore self
                    if m == 0 and n == 0:
                        continue

                    if grid[i + m][j + n] == CellState.ALIVE:
                        num_alive_neighbors = num_alive_neighbors + 1

            if num_alive_neighbors == 2 or num_alive_neighbors == 3:
                new_grid[i][j] = CellState.ALIVE
            else:
                new_grid[i][j] = CellState.DEAD

    return new_grid


def plant_seed(grid):
    for _ in range(num_seeds):
        grid[random.randint(0, col - 1)][random.randint(0, row - 1)] = CellState.ALIVE


def main(window):
    rerun = True
    while rerun:
        rerun = False

        # empty grid
        grid = [[CellState.DEAD for x in range(row)] for y in range(col)]  # grid representing state of the cell

        # init seed
        plant_seed(grid)

        running = True
        # clock = pygame.time.Clock()

        while running:
            grid = update_grid(grid)

            # clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.quit()
                    quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        pass

                    elif event.key == pygame.K_RIGHT:
                        pass

                    elif event.key == pygame.K_DOWN:
                        pass

                    elif event.key == pygame.K_UP:
                        pass

                    elif event.key == pygame.K_r:
                        running = False
                        rerun = True

            draw(window, grid)

            pygame.display.update()

    pygame.display.update()
    pygame.time.delay(1000)  # 1 sec
    pygame.quit()


if __name__ == '__main__':
    win = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('Game of Life')
    main(win)