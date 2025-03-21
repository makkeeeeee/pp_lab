
import pygame
import math
import datetime
import os

# 初始化 Pygame
pygame.init()

# 设置窗口大小
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock, Music Player, and Red Ball")

# 加载 Mickey 的图像
mickey_body = pygame.image.load("/Users/mariyaerzhan/Desktop/pp2/PP2LAB/LAB7/clock.png")
minute_hand = pygame.image.load("/Users/mariyaerzhan/Desktop/pp2/PP2LAB/LAB7/min_hand.png")
second_hand = pygame.image.load("/Users/mariyaerzhan/Desktop/pp2/PP2LAB/LAB7/sec_hand.png")

# 获取图像的矩形区域
mickey_rect = mickey_body.get_rect(center=(WIDTH // 2, HEIGHT // 2))
minute_rect = minute_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))
second_rect = second_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 初始化音乐播放器
pygame.mixer.init()
music_files = ["/Users/mariyaerzhan/Desktop/pp2/PP2LAB/LAB7/music1.mp3", "/Users/mariyaerzhan/Desktop/pp2/PP2LAB/LAB7/music2.mp3", "/Users/mariyaerzhan/Desktop/pp2/PP2LAB/LAB7/music3.mp3"] # 音乐文件列表
current_music_index = 0
pygame.mixer.music.load(music_files[current_music_index])

# 初始化红球
ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed = 20

# 主循环
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 音乐播放器控制
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # 播放/暂停
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:  # 停止
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:  # 下一首
                current_music_index = (current_music_index + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_music_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_b:  # 上一首
                current_music_index = (current_music_index - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_music_index])
                pygame.mixer.music.play()

        # 红球移动控制
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - ball_speed, ball_radius)
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + ball_speed, HEIGHT - ball_radius)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - ball_speed, ball_radius)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + ball_speed, WIDTH - ball_radius)

    # 清屏
    screen.fill(WHITE)

    # 绘制 Mickey 时钟
    now = datetime.datetime.now()
    minute = now.minute
    second = now.second

    # 计算指针的角度
    minute_angle = -math.radians((minute / 60) * 360)  # 分钟指针角度
    second_angle = -math.radians((second / 60) * 360)  # 秒针角度

    # 旋转指针
    rotated_minute = pygame.transform.rotate(minute_hand, math.degrees(minute_angle))
    rotated_second = pygame.transform.rotate(second_hand, math.degrees(second_angle))

    # 获取旋转后的矩形区域
    minute_rect = rotated_minute.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    second_rect = rotated_second.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # 绘制 Mickey 的身体和指针
    screen.blit(mickey_body, mickey_rect)
    screen.blit(rotated_minute, minute_rect)
    screen.blit(rotated_second, second_rect)

    # 绘制红球
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出 Pygame
pygame.quit()