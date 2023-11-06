import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
ROWS = SCREEN_HEIGHT // CELL_SIZE
COLS = SCREEN_WIDTH // CELL_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Cell:
    def __init__(self, is_alive):
        self.status = is_alive

    def is_alive(self):
        return self.status

    def set_status(self, new_status):
        self.status = new_status


class GridFactory:
    """Class representing a Grids"""

    def __init__(self):
        pass

    def create(self, height, width):
        return [[Cell(False) for _ in range(width)] for _ in range(height)]


class Board:
    def __init__(self):
        self.grid_factory = GridFactory()
        self.rows = ROWS
        self.cols = COLS
        self.game = self.grid_factory.create(self.rows, self.cols)
        for i in range(len(self.game)):
            for j in range(len(self.game[0])):
                self.game[i][j].set_status(random.randint(0, 1))

    def set_all_cells_status(self, status):
        for row in self.game:
            for cell in row:
                cell.set_status(status)

    def draw_board(self, screen):
        for i in range(len(self.game)):
            for j in range((len(self.game[0]))):
                cell = self.game[i][j]
                color = BLACK if cell.is_alive() else WHITE
                pygame.draw.rect(
                    screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )

    def count_neighbors(self, x, y):
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < self.rows and 0 <= y + j < self.cols:
                    if not (i == 0 and j == 0) and self.game[x + i][y + j].is_alive():
                        neighbors += 1
        return neighbors

    def update(self):
        new_game = self.grid_factory.create(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.game[i][j]
                neighbors = self.count_neighbors(i, j)

                if cell.is_alive():
                    if neighbors < 2 or neighbors > 3:
                        new_game[i][j].set_status(False)

                    else:
                        new_game[i][i].set_status(True)

                else:
                    if neighbors == 3:
                        new_game[i][j].set_status(True)
        self.game = new_game


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game of Life")

    board = Board()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        board.draw_board(screen)
        pygame.display.update()
        board.update()
        pygame.time.delay(500)

    pygame.quit()
