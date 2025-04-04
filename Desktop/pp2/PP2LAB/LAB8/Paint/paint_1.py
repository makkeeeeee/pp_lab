import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    # Drawing properties
    radius = 15
    x = 0
    y = 0
    drawing_color = (0, 0, 255)  # Start with blue
    points = []
    
    # Tools
    tools = ['draw', 'rectangle', 'circle', 'eraser']
    current_tool = 'draw'
    
    # For shape drawing
    drawing_shape = False
    shape_start_pos = (0, 0)
    
    # Color selection
    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'magenta': (255, 0, 255),
        'cyan': (0, 255, 255),
        'white': (255, 255, 255),
        'black': (0, 0, 0)
    }
    
    # Create a surface to store drawings
    canvas = pygame.Surface((800, 600))
    canvas.fill((0, 0, 0))  # Black background
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Tool selection
                if event.key == pygame.K_d:
                    current_tool = 'draw'
                elif event.key == pygame.K_r:
                    current_tool = 'rectangle'
                elif event.key == pygame.K_c:
                    current_tool = 'circle'
                elif event.key == pygame.K_e:
                    current_tool = 'eraser'
                    drawing_color = colors['black']  # Eraser uses background color
                
                # Color selection
                elif event.key == pygame.K_1:
                    drawing_color = colors['red']
                    current_tool = 'draw'
                elif event.key == pygame.K_2:
                    drawing_color = colors['green']
                    current_tool = 'draw'
                elif event.key == pygame.K_3:
                    drawing_color = colors['blue']
                    current_tool = 'draw'
                elif event.key == pygame.K_4:
                    drawing_color = colors['yellow']
                    current_tool = 'draw'
                elif event.key == pygame.K_5:
                    drawing_color = colors['magenta']
                    current_tool = 'draw'
                elif event.key == pygame.K_6:
                    drawing_color = colors['cyan']
                    current_tool = 'draw'
                elif event.key == pygame.K_7:
                    drawing_color = colors['white']
                    current_tool = 'draw'
                elif event.key == pygame.K_8:
                    drawing_color = colors['black']
                    current_tool = 'draw'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if current_tool in ['rectangle', 'circle']:
                        drawing_shape = True
                        shape_start_pos = event.pos
                    elif current_tool == 'draw':
                        # Start drawing line
                        points.append(event.pos)
                    elif current_tool == 'eraser':
                        pygame.draw.circle(canvas, (0, 0, 0), event.pos, radius)
                
                # Radius control
                if event.button == 1:  # Left click grows radius
                    radius = min(50, radius + 1)
                elif event.button == 3:  # Right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing_shape:
                    if current_tool == 'rectangle':
                        pygame.draw.rect(canvas, drawing_color, 
                                         pygame.Rect(shape_start_pos, 
                                                   (event.pos[0] - shape_start_pos[0], 
                                                    event.pos[1] - shape_start_pos[1])), 
                                         radius//5 + 1)
                    elif current_tool == 'circle':
                        circle_radius = int(math.sqrt((event.pos[0] - shape_start_pos[0])**2 + 
                                          (event.pos[1] - shape_start_pos[1])**2))
                        pygame.draw.circle(canvas, drawing_color, shape_start_pos, circle_radius, radius//5 + 1)
                    drawing_shape = False
            
            if event.type == pygame.MOUSEMOTION:
                if current_tool == 'draw' and pygame.mouse.get_pressed()[0]:
                    points.append(event.pos)
                    points = points[-256:]  # Limit number of points
                elif current_tool == 'eraser' and pygame.mouse.get_pressed()[0]:
                    pygame.draw.circle(canvas, (0, 0, 0), event.pos, radius)
        
        # Draw everything
        screen.fill((0, 0, 0))
        screen.blit(canvas, (0, 0))
        
        # Draw current freehand lines
        if current_tool == 'draw' and len(points) > 1:
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, drawing_color)
                i += 1
        
        # Draw preview for shapes
        if drawing_shape and current_tool in ['rectangle', 'circle']:
            temp_surface = pygame.Surface((800, 600), pygame.SRCALPHA)
            if current_tool == 'rectangle':
                pygame.draw.rect(temp_surface, (*drawing_color, 150), 
                               pygame.Rect(shape_start_pos, 
                                         (pygame.mouse.get_pos()[0] - shape_start_pos[0], 
                                          pygame.mouse.get_pos()[1] - shape_start_pos[1])), 
                               radius//5 + 1)
            elif current_tool == 'circle':
                circle_radius = int(math.sqrt((pygame.mouse.get_pos()[0] - shape_start_pos[0])**2 + 
                                    (pygame.mouse.get_pos()[1] - shape_start_pos[1])**2))
                pygame.draw.circle(temp_surface, (*drawing_color, 150), shape_start_pos, circle_radius, radius//5 + 1)
            screen.blit(temp_surface, (0, 0))
        
        # Draw UI
        font = pygame.font.SysFont(None, 24)
        tool_text = [
            f"Tools: D=Draw, R=Rectangle, C=Circle, E=Eraser",
            f"Current: {current_tool.capitalize()}",
            f"Colors: 1=Red, 2=Green, 3=Blue, 4=Yellow, 5=Magenta, 6=Cyan, 7=White, 8=Black",
            f"Radius: {radius} (LMB=+, RMB=-)"
        ]
        
        for i, text in enumerate(tool_text):
            text_surface = font.render(text, True, (255, 255, 255))
            screen.blit(text_surface, (10, 10 + i * 30))
        
        # Draw color preview
        pygame.draw.rect(screen, drawing_color, (700, 10, 80, 30))
        pygame.draw.rect(screen, (255, 255, 255), (700, 10, 80, 30), 2)
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()