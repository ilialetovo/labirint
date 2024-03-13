import pygame
from queue import Queue

maze = [[1, 3, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2], ]

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Размер ячейки в лабиринте
CELL_SIZE = 40
ROWS = len(maze)
COLS = len(maze[0])
# Размер окна
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
# Инициализация окна Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shortest Path in Maze")


# Функция для отображения лабиринта на экране
def draw_maze():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if maze[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))


# Функция для отображения найденного пути на экране
def draw_path(parent, start, end):
    current = end
    while current != start:
        row, col = current
        pygame.draw.rect(screen, GREEN, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        current = parent[current]
    pygame.draw.rect(screen, GREEN, (start[1] * CELL_SIZE, start[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))


# Функция для нахождения кратчайшего пути в лабиринте с использованием BFS
def find_shortest_path(maze, start, end):
    q = Queue()
    q.put(start)
    visited = set()
    parent = {}

    while not q.empty():
        current = q.get()

        if current == end:
            return parent

        row, col = current
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

        for neighbor in neighbors:
            n_row, n_col = neighbor
            if 0 <= n_row < ROWS and 0 <= n_col < COLS and maze[n_row][n_col] != 1 and neighbor not in visited:
                q.put(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

    return None


# Нахождение стартовой и финишной позиций в лабиринте
start = None
end = None
for i in range(ROWS):
    for j in range(COLS):
        if maze[i][j] == 3:
            start = (i, j)
        elif maze[i][j] == 2:
            end = (i, j)

# Вызов функции для нахождения и отображения кратчайшего пути
if start is not None and end is not None:
    path = find_shortest_path(maze, start, end)
    if path is not None:
        draw_maze()
        draw_path(path, start, end)

# Основной игровой цикл Pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
