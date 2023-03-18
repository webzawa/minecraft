import pygame
import sys

# ゲームの初期設定
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minecraft-like Prototype")

# プレイヤー設定
player_size = 50
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5

# ゲームループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed

    # 画面更新
    screen.fill((135, 206, 250))
    pygame.draw.rect(screen, (139, 69, 19), (player_pos[0], player_pos[1], player_size, player_size))
    pygame.display.flip()

