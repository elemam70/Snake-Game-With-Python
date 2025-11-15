import pygame
import random
import sys
from typing import List, Tuple

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (0, 200, 0)

class Snake:
    def __init__(self):
        self.length: int = 1
        self.positions: List[Tuple[int, int]] = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction: Tuple[int, int] = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        self.color = GREEN
        self.score: int = 0

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + x) % GRID_WIDTH, (cur[1] + y) % GRID_HEIGHT)
        
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        self.score = 0

    def render(self, surface):
        for i, p in enumerate(self.positions):
            color = self.color if i == 0 else DARK_GREEN
            rect = pygame.Rect(p[0] * GRID_SIZE, p[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.direction != (0, 1):
            self.direction = (0, -1)
        elif keys[pygame.K_DOWN] and self.direction != (0, -1):
            self.direction = (0, 1)
        elif keys[pygame.K_LEFT] and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif keys[pygame.K_RIGHT] and self.direction != (-1, 0):
            self.direction = (1, 0)

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def render(self, surface):
        rect = pygame.Rect(self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, BLACK, rect, 1)

def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    
    snake = Snake()
    food = Food()
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        snake.handle_keys()
        snake.update()

        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()

        screen.fill(BLACK)
        snake.render(screen)
        food.render(screen)
        
        score_text = font.render(f'Score: {snake.score}', True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
