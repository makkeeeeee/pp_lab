import pygame
import random
from colour import *

pygame.init()

# Game constants
WIDTH = 600
HEIGHT = 600
CELL = 30

# Initialize screen
screen = pygame.display.set_mode((HEIGHT, WIDTH))

# Font for score and level display
font = pygame.font.SysFont("Arial", 20)

def draw_grid_chess():
    """Draw checkerboard pattern for the game grid"""
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    """Class to represent coordinates on the grid"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    """Snake class with movement, drawing, and collision detection"""
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.score = 0
        self.level = 1

    def move(self):
        """Move the snake body segments"""
        # Move each segment to the position of the segment in front of it
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Move head according to direction
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        """Draw the snake on the screen"""
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        """Check if snake head collides with food"""
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.score += 1
            # Level up every 3 foods
            if self.score % 3 == 0:
                self.level += 1
            # Add new segment to snake
            self.body.append(Point(head.x, head.y))
            return True
        return False

    def check_wall_collision(self):
        """Check if snake hits the wall or itself"""
        head = self.body[0]
        # Check wall collision
        if head.x < 0 or head.x >= WIDTH//CELL or head.y < 0 or head.y >= HEIGHT//CELL:
            return True
        # Check self collision (head hits body)
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

class Food:
    """Food class with position and drawing"""
    def __init__(self, snake):
        self.pos = self.generate_position(snake)

    def draw(self):
        """Draw food on the screen"""
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_position(self, snake):
        """Generate random position that doesn't overlap with snake"""
        while True:
            x = random.randint(0, WIDTH//CELL - 1)
            y = random.randint(0, HEIGHT//CELL - 1)
            # Check if position is not on snake
            valid_position = True
            for segment in snake.body:
                if segment.x == x and segment.y == y:
                    valid_position = False
                    break
            if valid_position:
                return Point(x, y)

def display_score_level(snake):
    """Display current score and level on screen"""
    score_text = font.render(f"Score: {snake.score}", True, colorBLACK)
    level_text = font.render(f"Level: {snake.level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

def game_over_screen():
    """Display game over message"""
    screen.fill(colorWHITE)
    game_over_text = font.render("GAME OVER! Press R to restart or Q to quit", True, colorBLACK)
    screen.blit(game_over_text, (WIDTH//2 - 200, HEIGHT//2))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Restart game
                if event.key == pygame.K_q:
                    return False  # Quit game
    return False

def main():
    """Main game loop"""
    global FPS
    
    # Initial game state
    FPS = 5
    snake = Snake()
    food = Food(snake)
    game_active = True

    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and game_active:
                # Change snake direction (can't reverse)
                if event.key == pygame.K_RIGHT and snake.dx != -1:
                    snake.dx = 1
                    snake.dy = 0
                elif event.key == pygame.K_LEFT and snake.dx != 1:
                    snake.dx = -1
                    snake.dy = 0
                elif event.key == pygame.K_DOWN and snake.dy != -1:
                    snake.dx = 0
                    snake.dy = 1
                elif event.key == pygame.K_UP and snake.dy != 1:
                    snake.dx = 0
                    snake.dy = -1

        if game_active:
            # Draw game elements
            draw_grid_chess()
            
            # Move snake and check collisions
            snake.move()
            if snake.check_wall_collision():
                game_active = False
            
            if snake.check_collision(food):
                food = Food(snake)
                # Increase speed with level (capped at 15)
                FPS = min(5 + snake.level * 2, 15)
            
            snake.draw()
            food.draw()
            display_score_level(snake)
            
            pygame.display.flip()
            clock.tick(FPS)
        else:
            # Game over state
            if game_over_screen():
                # Restart game
                main()
                return
            else:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()