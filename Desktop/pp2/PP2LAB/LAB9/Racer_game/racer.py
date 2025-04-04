# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initializing pygame and mixer
pygame.init()
pygame.mixer.init()  # Initialize mixer for sound effects

# Game constants
FPS = 60  # Frames per second
FramePerSec = pygame.time.Clock()  # Clock object for controlling frame rate

# Color definitions
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)  # For coins
SILVER = (192, 192, 192)  # For silver coins
GOLD = (255, 215, 0)  # For gold coins

# Game variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5  # Initial game speed
SCORE = 0  # Score based on passed enemies
COIN_SCORE = 0  # Track collected coins
COIN_SPAWN_RATE = 0.02  # 2% chance per frame to spawn a coin
SPEED_BOOST_THRESHOLD = 5  # Number of coins needed to increase enemy speed

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)  # Large font for game over
font_small = pygame.font.SysFont("Verdana", 20)  # Small font for scores
game_over = font.render("Game Over", True, BLACK)

# Load background image
background = pygame.image.load("AnimatedStreet.png")

# Load sounds
try:
    pygame.mixer.music.load("background.wav")  # Background music
    crash_sound = pygame.mixer.Sound("crash.wav")  # Crash sound effect
    coin_sound = pygame.mixer.Sound("coin.mp3")  # Coin collection sound
    pygame.mixer.music.play(-1)  # Play background music in loop
    pygame.mixer.music.set_volume(0.5)  # Lower background music volume
except:
    print("Warning: Could not load sound files")

# Create display surface
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Enhanced Racer Game")

class Enemy(pygame.sprite.Sprite):
    """Enemy car class that moves down the screen"""
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

    def move(self):
        """Move enemy down the screen and respawn at top when off screen"""
        global SCORE
        self.rect.move_ip(0, SPEED)  # Move down at current game speed
        if (self.rect.top > SCREEN_HEIGHT):
            SCORE += 1  # Increment score when enemy passes
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    """Player car class controlled by arrow keys"""
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)  # Starting position
        
    def move(self):
        """Move player left or right based on key presses"""
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)  # Move left
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)  # Move right

class Coin(pygame.sprite.Sprite):
    """Coin class with different types and weights"""
    def __init__(self):
        super().__init__()
        # Randomly determine coin type (70% bronze, 20% silver, 10% gold)
        coin_type = random.choices(
            ["bronze", "silver", "gold"],
            weights=[70, 20, 10],
            k=1
        )[0]
        
        # Set properties based on coin type
        if coin_type == "bronze":
            self.color = YELLOW
            self.value = 1
            self.size = 10
        elif coin_type == "silver":
            self.color = SILVER
            self.value = 2
            self.size = 15
        else:  # gold
            self.color = GOLD
            self.value = 3
            self.size = 20
            
        # Create coin surface
        self.image = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.size, self.size), self.size)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, SCREEN_WIDTH-30), 0)
        self.speed = random.randint(2, 4)  # Coins move slower than enemies
    
    def move(self):
        """Move coin down the screen and remove if off screen"""
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # Remove coin if it goes off screen

# Setting up Sprites        
P1 = Player()  # Create player
E1 = Enemy()   # Create first enemy

# Creating Sprites Groups
enemies = pygame.sprite.Group()  # Group for enemy cars
enemies.add(E1)
coins = pygame.sprite.Group()    # Group for coins
all_sprites = pygame.sprite.Group()  # Group for all sprites
all_sprites.add(P1)
all_sprites.add(E1)

# Custom event for increasing speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # Trigger every 1000ms

# Game Loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            # Gradually increase base speed over time
            SPEED += 0.2     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background, (0,0))
    
    # Randomly spawn coins with a maximum of 3 on screen
    if random.random() < COIN_SPAWN_RATE and len(coins) < 3:
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
        COIN_SCORE += coin.value  # Add coin's value to total
        coin_sound.play()  # Play collection sound
        
        # Speed boost when reaching threshold
        if COIN_SCORE % SPEED_BOOST_THRESHOLD == 0:
            SPEED += 0.5  # Increase game speed
            # Visual feedback for speed boost
            boost_text = font_small.render("Speed Boost!", True, RED)
            DISPLAYSURF.blit(boost_text, (SCREEN_WIDTH//2 - 80, 70))
            pygame.display.update()
            time.sleep(0.5)  # Brief pause to show message

    # Check for collision with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()  # Stop background music
        crash_sound.play()  # Play crash sound
        
        # Game over screen
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        
        # Display final scores
        final_score = font_small.render(f"Final Score: {SCORE}", True, BLACK)
        final_coins = font_small.render(f"Coins Collected: {COIN_SCORE}", True, BLACK)
        DISPLAYSURF.blit(final_score, (100, 350))
        DISPLAYSURF.blit(final_coins, (80, 380))
        
        pygame.display.update()
        
        # Remove all sprites and quit after delay
        for entity in all_sprites:
            entity.kill() 
        time.sleep(3)
        pygame.quit()
        sys.exit()        
    
    pygame.display.update()  # Update the display
    FramePerSec.tick(FPS)  # Maintain 60 FPS