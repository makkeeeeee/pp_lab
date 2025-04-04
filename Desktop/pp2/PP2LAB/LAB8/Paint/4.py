import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing App")

# Tools
DRAW = 0
RECTANGLE = 1
CIRCLE = 2
ERASER = 3

current_tool = DRAW
drawing = False
start_pos = (0, 0)
current_color = (0, 0, 0)  # Start with black
eraser_size = 20

# Store all drawings as a list of surfaces
canvas = pygame.Surface((800, 600))
canvas.fill((255, 255, 255))  # White background

# Store shapes for undo functionality
shapes = []

# Color palette
colors = [
    (0, 0, 0),      # Black
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 255, 255) # White (eraser color)
]

clock = pygame.time.Clock()

def draw_rect(surface, color, start, end, width=1):
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(surface, color, rect, width)

def draw_circle(surface, color, start, end, width=1):
    radius = int(math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2))
    pygame.draw.circle(surface, color, start, radius, width)

def draw_eraser(surface, pos, size, color=(255, 255, 255)):
    pygame.draw.circle(surface, color, pos, size // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                drawing = True
                start_pos = event.pos
                
                # Check if color selection clicked
                for i, color in enumerate(colors):
                    rect = pygame.Rect(10 + i * 40, 10, 30, 30)
                    if rect.collidepoint(event.pos):
                        current_color = color
                        if i == len(colors) - 1:  # Last color is white (eraser)
                            current_tool = ERASER
                        else:
                            if current_tool == ERASER:
                                current_tool = DRAW  # Switch back to draw if selecting a color
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                drawing = False
                if current_tool == RECTANGLE:
                    shapes.append(("rect", current_color, start_pos, event.pos, 2))
                    draw_rect(canvas, current_color, start_pos, event.pos, 2)
                elif current_tool == CIRCLE:
                    shapes.append(("circle", current_color, start_pos, event.pos, 2))
                    draw_circle(canvas, current_color, start_pos, event.pos, 2)
        
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if current_tool == DRAW:
                    pygame.draw.line(canvas, current_color, event.pos, event.pos, 5)
                elif current_tool == ERASER:
                    draw_eraser(canvas, event.pos, eraser_size)
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  # Draw mode
                current_tool = DRAW
            elif event.key == pygame.K_r:  # Rectangle mode
                current_tool = RECTANGLE
            elif event.key == pygame.K_c:  # Circle mode
                current_tool = CIRCLE
            elif event.key == pygame.K_e:  # Eraser mode
                current_tool = ERASER
            elif event.key == pygame.K_u:  # Undo
                if shapes:
                    last_shape = shapes.pop()
                    # Redraw everything except the last shape
                    canvas.fill((255, 255, 255))
                    for shape in shapes:
                        if shape[0] == "rect":
                            draw_rect(canvas, shape[1], shape[2], shape[3], shape[4])
                        elif shape[0] == "circle":
                            draw_circle(canvas, shape[1], shape[2], shape[3], shape[4])
    
    # Draw everything
    screen.fill((255, 255, 255))
    screen.blit(canvas, (0, 0))
    
    # Draw color palette
    for i, color in enumerate(colors):
        rect = pygame.Rect(10 + i * 40, 10, 30, 30)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Border
    
    # Draw tool indicators
    font = pygame.font.SysFont(None, 24)
    tools_text = [
        f"D: Draw ({'active' if current_tool == DRAW else ''})",
        f"R: Rectangle ({'active' if current_tool == RECTANGLE else ''})",
        f"C: Circle ({'active' if current_tool == CIRCLE else ''})",
        f"E: Eraser ({'active' if current_tool == ERASER else ''})",
        f"U: Undo",
        f"Current: {'Drawing' if current_tool == DRAW else 'Rectangle' if current_tool == RECTANGLE else 'Circle' if current_tool == CIRCLE else 'Eraser'}"
    ]
    
    for i, text in enumerate(tools_text):
        text_surface = font.render(text, True, (0, 0, 0))
        screen.blit(text_surface, (10, 50 + i * 25))
    
    # If drawing a preview shape
    if drawing and current_tool in (RECTANGLE, CIRCLE):
        temp_surface = pygame.Surface((800, 600), pygame.SRCALPHA)
        if current_tool == RECTANGLE:
            draw_rect(temp_surface, (*current_color, 128), start_pos, pygame.mouse.get_pos(), 2)
        elif current_tool == CIRCLE:
            draw_circle(temp_surface, (*current_color, 128), start_pos, pygame.mouse.get_pos(), 2)
        screen.blit(temp_surface, (0, 0))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()