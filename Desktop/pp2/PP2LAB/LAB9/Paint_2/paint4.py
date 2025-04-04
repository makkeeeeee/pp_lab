import pygame
import math
import sys

# 初始化pygame / Initialize pygame
pygame.init()

# 屏幕设置 / Screen setup
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Enhanced Drawing App")

# 工具枚举 / Tools enumeration
DRAW = 0              # 自由绘制 / Free drawing
RECTANGLE = 1         # 矩形 / Rectangle
CIRCLE = 2            # 圆形 / Circle
ERASER = 3            # 橡皮擦 / Eraser
SQUARE = 4            # 正方形 / Square
RIGHT_TRIANGLE = 5    # 直角三角形 / Right triangle
EQUILATERAL_TRIANGLE = 6  # 等边三角形 / Equilateral triangle
RHOMBUS = 7           # 菱形 / Rhombus

# 当前工具和状态 / Current tool and state
current_tool = DRAW   # 默认工具是画笔 / Default tool is draw
drawing = False       # 是否正在绘制 / Whether currently drawing
start_pos = (0, 0)    # 绘制起点 / Drawing start position
current_color = (0, 0, 0)  # 默认黑色 / Default black color
eraser_size = 20      # 橡皮擦大小 / Eraser size

# 画布 / Canvas surface
canvas = pygame.Surface((screen_width, screen_height))
canvas.fill((255, 255, 255))  # 白色背景 / White background

# 形状历史记录(用于撤销) / Shape history (for undo)
shapes = []

# 调色板 / Color palette
colors = [
    (0, 0, 0),      # 黑色 / Black
    (255, 0, 0),    # 红色 / Red
    (0, 255, 0),    # 绿色 / Green
    (0, 0, 255),    # 蓝色 / Blue
    (255, 255, 0),  # 黄色 / Yellow
    (255, 0, 255),  # 紫色 / Magenta
    (0, 255, 255),  # 青色 / Cyan
    (255, 255, 255) # 白色(橡皮擦) / White (eraser)
]

clock = pygame.time.Clock()  # 控制帧率 / For controlling frame rate

# ========== 形状绘制函数 / Shape drawing functions ==========

def draw_rect(surface, color, start, end, width=1):
    """绘制矩形 / Draw rectangle from start to end position"""
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(surface, color, rect, width)

def draw_circle(surface, color, start, end, width=1):
    """绘制圆形 / Draw circle with center at start and radius to end"""
    radius = int(math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2))
    pygame.draw.circle(surface, color, start, radius, width)

def draw_eraser(surface, pos, size, color=(255, 255, 255)):
    """绘制橡皮擦 / Draw eraser circle at given position"""
    pygame.draw.circle(surface, color, pos, size // 2)

def draw_square(surface, color, start, end, width=1):
    """绘制正方形 / Draw square (equal width and height)"""
    size = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
    # 确定方向 / Determine direction
    dx = 1 if end[0] > start[0] else -1
    dy = 1 if end[1] > start[1] else -1
    rect = pygame.Rect(start, (size * dx, size * dy))
    pygame.draw.rect(surface, color, rect, width)

def draw_right_triangle(surface, color, start, end, width=1):
    """绘制直角三角形 / Draw right triangle with right angle at start"""
    points = [
        start,                  # 直角点 / Right angle point
        (start[0], end[1]),    # 垂直点 / Vertical point
        end                    # 终点 / End point
    ]
    pygame.draw.polygon(surface, color, points, width)

def draw_equilateral_triangle(surface, color, start, end, width=1):
    """绘制等边三角形 / Draw equilateral triangle"""
    # 计算底边长度 / Calculate base length
    base_length = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    height = (math.sqrt(3)/2) * base_length  # 等边三角形高度 / Equilateral triangle height
    
    # 计算方向向量 / Calculate direction vector
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    
    # 计算垂直向量 / Calculate perpendicular vector
    perp_dx = dy
    perp_dy = -dx
    
    # 归一化 / Normalize
    length = math.sqrt(perp_dx**2 + perp_dy**2)
    if length > 0:
        perp_dx /= length
        perp_dy /= length
    
    # 计算顶点 / Calculate apex point
    mid_point = ((start[0] + end[0])/2, (start[1] + end[1])/2)
    apex = (mid_point[0] + perp_dx * height, mid_point[1] + perp_dy * height)
    
    points = [start, end, apex]
    pygame.draw.polygon(surface, color, points, width)

def draw_rhombus(surface, color, start, end, width=1):
    """绘制菱形 / Draw rhombus"""
    center = ((start[0] + end[0])/2, (start[1] + end[1])/2)  # 中心点 / Center point
    width = abs(end[0] - start[0])  # 宽度 / Width
    height = abs(end[1] - start[1])  # 高度 / Height
    
    # 四个顶点 / Four vertices
    points = [
        (center[0], center[1] - height/2),  # 上 / Top
        (center[0] + width/2, center[1]),    # 右 / Right
        (center[0], center[1] + height/2),   # 下 / Bottom
        (center[0] - width/2, center[1])     # 左 / Left
    ]
    pygame.draw.polygon(surface, color, points, width)

def draw_tool_indicators(surface):
    """Draw tool indicators"""
    font = pygame.font.SysFont(None, 24)
    tools_text = [
        f"D: Draw {'(active)' if current_tool == DRAW else ''}",
        f"R: Rectangle {'(active)' if current_tool == RECTANGLE else ''}",
        f"C: Circle {'(active)' if current_tool == CIRCLE else ''}",
        f"E: Eraser {'(active)' if current_tool == ERASER else ''}",
        f"S: Square {'(active)' if current_tool == SQUARE else ''}",
        f"T: Right Triangle {'(active)' if current_tool == RIGHT_TRIANGLE else ''}",
        f"Q: Equilateral Triangle {'(active)' if current_tool == EQUILATERAL_TRIANGLE else ''}",
        f"H: Rhombus {'(active)' if current_tool == RHOMBUS else ''}",
        f"U: Undo",
        f"Current Tool: {'Draw' if current_tool == DRAW else 'Rectangle' if current_tool == RECTANGLE else 'Circle' if current_tool == CIRCLE else 'Eraser' if current_tool == ERASER else 'Square' if current_tool == SQUARE else 'Right Triangle' if current_tool == RIGHT_TRIANGLE else 'Equilateral Triangle' if current_tool == EQUILATERAL_TRIANGLE else 'Rhombus'}"
    ]
    
    # 渲染文本 / Render text
    for i, text in enumerate(tools_text):
        text_surface = font.render(text, True, (0, 0, 0))
        surface.blit(text_surface, (10, 50 + i * 25))

# ========== 主循环 / Main loop ==========
running = True
while running:
    # 事件处理 / Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 鼠标按下 / Mouse button down
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左键 / Left button
                drawing = True
                start_pos = event.pos
                
                # 检查颜色选择 / Check color selection
                for i, color in enumerate(colors):
                    rect = pygame.Rect(10 + i * 40, 10, 30, 30)
                    if rect.collidepoint(event.pos):
                        current_color = color
                        if i == len(colors) - 1:  # 白色是橡皮擦 / White is eraser
                            current_tool = ERASER
                        else:
                            if current_tool == ERASER:
                                current_tool = DRAW  # 选择颜色后切换回画笔 / Switch back to draw when selecting color
        
        # 鼠标释放 / Mouse button up
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                drawing = False
                end_pos = event.pos
                
                # 添加形状到历史记录 / Add shape to history
                if current_tool == RECTANGLE:
                    shapes.append(("rect", current_color, start_pos, end_pos, 2))
                    draw_rect(canvas, current_color, start_pos, end_pos, 2)
                elif current_tool == CIRCLE:
                    shapes.append(("circle", current_color, start_pos, end_pos, 2))
                    draw_circle(canvas, current_color, start_pos, end_pos, 2)
                elif current_tool == SQUARE:
                    shapes.append(("square", current_color, start_pos, end_pos, 2))
                    draw_square(canvas, current_color, start_pos, end_pos, 2)
                elif current_tool == RIGHT_TRIANGLE:
                    shapes.append(("right_triangle", current_color, start_pos, end_pos, 2))
                    draw_right_triangle(canvas, current_color, start_pos, end_pos, 2)
                elif current_tool == EQUILATERAL_TRIANGLE:
                    shapes.append(("equilateral_triangle", current_color, start_pos, end_pos, 2))
                    draw_equilateral_triangle(canvas, current_color, start_pos, end_pos, 2)
                elif current_tool == RHOMBUS:
                    shapes.append(("rhombus", current_color, start_pos, end_pos, 2))
                    draw_rhombus(canvas, current_color, start_pos, end_pos, 2)
        
        # 鼠标移动 / Mouse motion
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if current_tool == DRAW:
                    pygame.draw.line(canvas, current_color, event.pos, event.pos, 5)
                elif current_tool == ERASER:
                    draw_eraser(canvas, event.pos, eraser_size)
        
        # 键盘输入 / Keyboard input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  # 绘制模式 / Draw mode
                current_tool = DRAW
            elif event.key == pygame.K_r:  # 矩形模式 / Rectangle mode
                current_tool = RECTANGLE
            elif event.key == pygame.K_c:  # 圆形模式 / Circle mode
                current_tool = CIRCLE
            elif event.key == pygame.K_e:  # 橡皮擦模式 / Eraser mode
                current_tool = ERASER
            elif event.key == pygame.K_s:  # 正方形模式 / Square mode
                current_tool = SQUARE
            elif event.key == pygame.K_t:  # 直角三角形模式 / Right triangle mode
                current_tool = RIGHT_TRIANGLE
            elif event.key == pygame.K_q:  # 等边三角形模式 / Equilateral triangle mode
                current_tool = EQUILATERAL_TRIANGLE
            elif event.key == pygame.K_h:  # 菱形模式 / Rhombus mode
                current_tool = RHOMBUS
            elif event.key == pygame.K_u:  # 撤销 / Undo
                if shapes:
                    last_shape = shapes.pop()
                    # 重绘所有形状(除了最后一个) / Redraw all shapes except last one
                    canvas.fill((255, 255, 255))
                    for shape in shapes:
                        if shape[0] == "rect":
                            draw_rect(canvas, shape[1], shape[2], shape[3], shape[4])
                        elif shape[0] == "circle":
                            draw_circle(canvas, shape[1], shape[2], shape[3], shape[4])
                        elif shape[0] == "square":
                            draw_square(canvas, shape[1], shape[2], shape[3], shape[4])
                        elif shape[0] == "right_triangle":
                            draw_right_triangle(canvas, shape[1], shape[2], shape[3], shape[4])
                        elif shape[0] == "equilateral_triangle":
                            draw_equilateral_triangle(canvas, shape[1], shape[2], shape[3], shape[4])
                        elif shape[0] == "rhombus":
                            draw_rhombus(canvas, shape[1], shape[2], shape[3], shape[4])
    
    # 绘制界面 / Draw interface
    screen.fill((255, 255, 255))
    screen.blit(canvas, (0, 0))
    
    # 绘制调色板 / Draw color palette
    for i, color in enumerate(colors):
        rect = pygame.Rect(10 + i * 40, 10, 30, 30)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # 边框 / Border
    
    # 绘制工具指示器 / Draw tool indicators
    draw_tool_indicators(screen)
    
    # 绘制预览形状(矩形等工具) / Draw preview shape (for rectangle tools)
    if drawing and current_tool in (RECTANGLE, CIRCLE, SQUARE, RIGHT_TRIANGLE, EQUILATERAL_TRIANGLE, RHOMBUS):
        temp_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        mouse_pos = pygame.mouse.get_pos()
        
        if current_tool == RECTANGLE:
            draw_rect(temp_surface, (*current_color, 128), start_pos, mouse_pos, 2)
        elif current_tool == CIRCLE:
            draw_circle(temp_surface, (*current_color, 128), start_pos, mouse_pos, 2)
        elif current_tool == SQUARE:
            draw_square(temp_surface, (*current_color, 128), start_pos, mouse_pos, 2)
        elif current_tool == RIGHT_TRIANGLE:
            draw_right_triangle(temp_surface, (*current_color, 128), start_pos, mouse_pos, 2)
        elif current_tool == EQUILATERAL_TRIANGLE:
            draw_equilateral_triangle(temp_surface, (*current_color, 128), start_pos, mouse_pos, 2)
        elif current_tool == RHOMBUS:
            draw_rhombus(temp_surface, (*current_color, 128), start_pos, mouse_pos, 2)
        
        screen.blit(temp_surface, (0, 0))
    
    pygame.display.flip()  # 更新显示 / Update display
    clock.tick(60)        # 60 FPS

pygame.quit()
sys.exit()