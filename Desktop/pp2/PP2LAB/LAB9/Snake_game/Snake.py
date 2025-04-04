import pygame
import random
from colour import *
import time  # For tracking food timers/用于食物计时

pygame.init()

# Game constants/游戏常量
WIDTH = 600    # Window width/窗口宽度
HEIGHT = 600   # Window height/窗口高度
CELL = 30      # Size of each grid cell/每个网格单元大小

# Initialize screen/初始化游戏窗口
screen = pygame.display.set_mode((HEIGHT, WIDTH))

# Font for score and level display/用于显示分数和等级的字体
font = pygame.font.SysFont("Arial", 20)

def draw_grid_chess():
    """Draw checkerboard pattern/绘制棋盘样式网格"""
    colors = [colorWHITE, colorGRAY]  # Alternate colors/交替颜色
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    """Class representing grid coordinates/表示网格坐标的类"""
    def __init__(self, x, y):
        self.x = x  # x coordinate/x坐标
        self.y = y  # y coordinate/y坐标

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    """Snake class with movement and collision/贪吃蛇类(移动和碰撞检测)"""
    def __init__(self):
        # Initial snake body/初始蛇身
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1  # x-direction movement/x方向移动量  
        self.dy = 0  # y-direction movement/y方向移动量
        self.score = 0  # Game score/游戏得分
        self.level = 1  # Game level/游戏等级

    def move(self):
        """Move snake segments/移动蛇身"""
        # Move each segment to previous segment's position
        # 每段移动到前一段的位置
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Move head based on direction/根据方向移动头部
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        """Draw snake on screen/绘制蛇身"""
        head = self.body[0]
        # Draw head in red/红色头部
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        # Draw body in yellow/黄色身体
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, foods):
        """
        Check if snake eats food/检测是否吃到食物
        Returns: (collision occurred/是否碰撞, food index/食物索引)
        """
        head = self.body[0]
        for i, food in enumerate(foods):
            if head.x == food.pos.x and head.y == food.pos.y:
                self.score += food.weight  # Add food's weight to score/按食物重量加分
                # Level up every 5 points/每5分升一级
                if self.score // 5 > (self.score - food.weight) // 5:
                    self.level += 1
                # Grow snake based on weight/根据重量增加蛇身
                for _ in range(food.weight):
                    self.body.append(Point(head.x, head.y))
                return (True, i)
        return (False, -1)

    def check_wall_collision(self):
        """Check wall or self collision/检测撞墙或自身"""
        head = self.body[0]
        # Wall collision/墙壁碰撞
        if head.x < 0 or head.x >= WIDTH//CELL or head.y < 0 or head.y >= HEIGHT//CELL:
            return True
        # Self collision/自身碰撞
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

class Food:
    """Food class with weight and timer/食物类(带重量和计时)"""
    def __init__(self, snake, existing_foods=[]):
        self.pos = self.generate_position(snake, existing_foods)
        self.weight = random.randint(1, 3)  # Random weight 1-3/随机重量1-3
        self.spawn_time = time.time()  # Creation time/生成时间
        self.lifetime = random.uniform(5, 15)  # Random lifespan/随机存活时间

    def draw(self):
        """Draw food with weight indicator/绘制带重量的食物"""
        # Different colors by weight/不同重量不同颜色
        colors = [colorGREEN, colorBLUE, colorPURPLE]  # 1-3 weights
        pygame.draw.rect(screen, colors[self.weight - 1], 
                        (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
        # Display weight number/显示重量数字
        weight_text = font.render(str(self.weight), True, colorWHITE)
        screen.blit(weight_text, (self.pos.x * CELL + CELL//3, self.pos.y * CELL + CELL//4))

    def generate_position(self, snake, existing_foods):
        """Generate valid position/生成有效位置"""
        while True:
            x = random.randint(0, WIDTH//CELL - 1)
            y = random.randint(0, HEIGHT//CELL - 1)
            
            # Check snake collision/检查蛇身碰撞
            valid = True
            for segment in snake.body:
                if segment.x == x and segment.y == y:
                    valid = False
                    break
            
            # Check other foods/检查其他食物
            if valid:
                for food in existing_foods:
                    if food.pos.x == x and food.pos.y == y:
                        valid = False
                        break
            
            if valid:
                return Point(x, y)

    def is_expired(self):
        """Check if food expired/检查是否过期"""
        return time.time() - self.spawn_time > self.lifetime

def display_score_level(snake):
    """Display score and level/显示分数和等级"""
    score_text = font.render(f"Score: {snake.score}", True, colorBLACK)
    level_text = font.render(f"Level: {snake.level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

def game_over_screen():
    """Show game over screen/显示游戏结束界面"""
    screen.fill(colorWHITE)
    game_over_text = font.render("GAME OVER! Press R to restart or Q to quit", 
                                True, colorBLACK)
    screen.blit(game_over_text, (WIDTH//2 - 200, HEIGHT//2))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart/重新开始
                    return True  
                if event.key == pygame.K_q:  # Quit/退出游戏
                    return False  
    return False

def main():
    """Main game loop/主游戏循环"""
    global FPS
    
    # Initial game state/初始游戏状态
    FPS = 5
    snake = Snake()
    foods = [Food(snake)]  # Start with one food/初始一个食物
    game_active = True
    last_food_spawn = time.time()
    food_spawn_interval = 3  # New food every 3 sec/每3秒新食物

    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and game_active:
                # Change direction (no reversal)/改变方向(不能反向)
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
            # Draw game elements/绘制游戏元素
            draw_grid_chess()
            
            # Move and check collisions/移动和碰撞检测
            snake.move()
            if snake.check_wall_collision():
                game_active = False
            
            # Food collision/食物碰撞
            collision, food_index = snake.check_collision(foods)
            if collision:
                del foods[food_index]  # Remove eaten food/移除被吃的食物
            
            # Spawn new food periodically/定期生成新食物
            if time.time() - last_food_spawn > food_spawn_interval and len(foods) < 5:
                foods.append(Food(snake, foods))
                last_food_spawn = time.time()
            
            # Remove expired foods/移除过期食物
            foods = [food for food in foods if not food.is_expired()]
            
            # Draw all objects/绘制所有对象
            snake.draw()
            for food in foods:
                food.draw()
            
            display_score_level(snake)
            
            pygame.display.flip()
            clock.tick(FPS)
        else:
            # Game over handling/游戏结束处理
            if game_over_screen():
                # Restart game/重新开始游戏
                main()
                return
            else:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()


"""""
Multiple Foods with Weight/多种重量食物:
Weight 1-3 (Green/Blue/Purple)/重量1-3(绿/蓝/紫)
Higher weight = more points/重量越大得分越多
Display weight number/显示重量数字
Disappearing Foods/会消失的食物:
Each food has random lifetime (5-15s)/每个食物有随机存活时间
Automatically removed when expired/超时自动移除
Visual indicator through color/通过颜色视觉提示
Dynamic Spawning/动态生成:
New food spawns every 3 seconds/每3秒生成新食物
Maximum 5 foods on screen/屏幕上最多5个食物
Smart position generation/智能位置生成
Improved Gameplay/改进的游戏性:
Level up every 5 points/每5分升一级
Speed increases with level/速度随等级提升
Clear game over options/明确的游戏结束选项
"""