import pygame
import random
import psycopg2
import sys
from colour import *
import time 
import sqlite3  # 数据库模块

# 数据库连接信息
DB_NAME = "snake_game"
DB_USER = "mariyaerzhan"
DB_PASSWORD = "123456"  # <-- 改成你的数据库密码
DB_HOST = "localhost"
DB_PORT = "5432"

# 初始化 pygame
pygame.init()

# 游戏窗口设置
WIDTH = 600    # Window width/窗口宽度
HEIGHT = 600   # Window height/窗口高度
CELL = 30      # Size of each grid cell/每个网格单元大小

# Initialize screen/初始化游戏窗口
screen = pygame.display.set_mode((HEIGHT, WIDTH))

pygame.display.set_caption("贪吃蛇游戏 + 数据库")

# 颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 字体
# Font for score and level display/用于显示分数和等级的字体
font = pygame.font.SysFont("Arial", 20)


# ========== 数据库功能 ==========
# 初始化数据库
def init_db():
    conn = sqlite3.connect("snake_game.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS game_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            score INTEGER,
            level INTEGER,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def get_or_create_user(username):
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                            password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
    cur.close()
    conn.close()
    return user_id


def get_latest_score(user_id):
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                            password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("""
        SELECT score, level FROM user_score
        WHERE user_id = %s ORDER BY timestamp DESC LIMIT 1
    """, (user_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result if result else (0, 1)


def save_game_state(user_id, level_id, score, game_state):
    """保存游戏状态到PostgreSQL"""
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER,
        password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO user_score 
                (user_id, level_id, score, game_state)
            VALUES (%s, %s, %s, %s::jsonb)
            ON CONFLICT (user_id, level_id) 
            DO UPDATE SET
                score = EXCLUDED.score,
                game_state = EXCLUDED.game_state,
                saved_at = CURRENT_TIMESTAMP
        """, (user_id, level_id, score, json.dumps(game_state)))
        conn.commit()
    except Exception as e:
        print("保存失败:", e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def get_user_progress(username):
    """获取用户进度"""
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER,
        password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cur = conn.cursor()
    
    # 获取或创建用户
    cur.execute("""
        INSERT INTO users (username) 
        VALUES (%s) 
        ON CONFLICT (username) DO UPDATE SET username=EXCLUDED.username
        RETURNING user_id
    """, (username,))
    user_id = cur.fetchone()[0]
    
    # 获取最新进度
    cur.execute("""
        SELECT l.level_id, l.level_name, l.speed, l.walls,
               COALESCE(us.score, 0), COALESCE(us.level_id, 1)
        FROM users u
        LEFT JOIN user_score us ON u.user_id = us.user_id
        JOIN levels l ON l.level_id = COALESCE(us.level_id, 1)
        WHERE u.user_id = %s
        ORDER BY us.saved_at DESC LIMIT 1
    """, (user_id,))
    result = cur.fetchone()
    
    cur.close()
    conn.close()
    
    if result:
        return {
            'user_id': user_id,
            'level_id': result[0],
            'level_name': result[1],
            'speed': result[2],
            'walls': json.loads(result[3]),
            'score': result[4],
            'current_level': result[5]
        }
    return None





# ========== 棋盘格 ==========
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


# ========== 贪吃蛇游戏类 ==========
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

def game_over_screen(snake, user_id, level_id):
    save_game_state(user_id, level_id, snake.score, {'game_over': True})
    # ...显示界面逻辑...
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

def unlock_next_level(user_id, current_level):
    """解锁下一关"""
    conn = psycopg2.connect(...)
    cur = conn.cursor()
    cur.execute("""
        SELECT level_id FROM levels 
        WHERE level_id > %s ORDER BY level_id LIMIT 1
    """, (current_level,))
    next_level = cur.fetchone()
    if next_level:
        # 初始化新关卡进度
        cur.execute("""
            INSERT INTO user_score (user_id, level_id, score)
            VALUES (%s, %s, 0)
        """, (user_id, next_level[0]))
        conn.commit()
    conn.close()

def main():
    """Main game loop/主游戏循环"""
    username = input("请输入你的用户名：")
   
    
    # 连接数据库并获取用户 ID
    user_id = get_or_create_user(username)
    last_score, last_level = get_latest_score(user_id)
    
    print(f"欢迎 {username}，你的上次得分：{last_score}，等级：{last_level}")

    clock = pygame.time.Clock()
    snake = Snake()
    snake.score = last_score
    snake.level = last_level
    last_food_spawn = time.time()

    # Initial game state/初始游戏状态
    FPS = 5
    snake = Snake()
    foods = [Food(snake)]  # Start with one food/初始一个食物
    game_active = True
    food_spawn_interval = 3  # New food every 3 sec/每3秒新食物

   
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
            if game_over_screen(snake, user_id):
                # Restart game/重新开始游戏
                main()
                return
            else:
                running = False

    pygame.quit()

if __name__ == "__main__":
    init_db()
    main()