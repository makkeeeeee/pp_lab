# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initializing 
pygame.init()
pygame.mixer.init()  # Initialize mixer for sound

# Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)  # For coins

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0  # Track collected coins
COIN_SPAWN_RATE = 0.02  # 2% chance per frame to spawn a coin

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load assets
background = pygame.image.load("AnimatedStreet.png")

# Load sounds
try:
    pygame.mixer.music.load("background.wav")  # Background music
    crash_sound = pygame.mixer.Sound("crash.wav")
    coin_sound = pygame.mixer.Sound("coin.mp3")  # Temporary - replace with "coin.wav" if available
    pygame.mixer.music.play(-1)  # Play background music in loop
    pygame.mixer.music.set_volume(0.5)  # Lower background music volume
except:
    print("Warning: Could not load sound files")

# Create display surface
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer Game with Coins")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create coin surface (replace with image if available)
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, SCREEN_WIDTH-30), 0)
        self.speed = random.randint(2, 4)  # Coins move slower than enemies
    
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # Remove coin if it goes off screen

# Setting up Sprites        
P1 = Player()
E1 = Enemy()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()  # Group for coins
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background, (0,0))
    
    # Randomly spawn coins
    if random.random() < COIN_SPAWN_RATE and len(coins) < 3:  # Max 3 coins on screen
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
    
    # Display scores
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_scores = font_small.render(f"Coins: {COIN_SCORE}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coin_scores, (10, 40))

    # Update and draw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Check for coin collection
    coins_collected = pygame.sprite.spritecollide(P1, coins, True)
    for coin in coins_collected:
        COIN_SCORE += 1
        coin_sound.play()  # Play coin collection sound
        # Optional: Add visual effect here (like +1 text)

    # Check for collision with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        crash_sound.play()
        time.sleep(0.5)
        
        # Game over screen
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        final_score = font_small.render(f"Final Score: {SCORE}", True, BLACK)
        final_coins = font_small.render(f"Coins Collected: {COIN_SCORE}", True, BLACK)
        DISPLAYSURF.blit(final_score, (100, 350))
        DISPLAYSURF.blit(final_coins, (80, 380))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(3)
        pygame.quit()
        sys.exit()        
    
    pygame.display.update()
    FramePerSec.tick(FPS)