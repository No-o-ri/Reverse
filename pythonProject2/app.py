import pygame
from random import randint
import sys

pygame.init()
pygame.display.set_caption('Reverse?')
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
game_count = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y


user_x = 300.0
user_y = 250.0
user_width = 50
user_height = 50

run = True
coin = Coin(randint(5, 795), randint(5, 595))
delay_timer = 0

while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (235, 245, 100), (user_x, user_y, user_width, user_height))
    pygame.draw.circle(screen, (235, 255, 40), (coin.x, coin.y), 20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        user_x += 0.1
    if keys[pygame.K_d]:
        user_x -= 0.1
    if keys[pygame.K_w]:
        user_y += 0.1
    if keys[pygame.K_s]:
        user_y -= 0.1

    if delay_timer > 0:
        delay_timer -= 1
        continue

    if pygame.Rect(user_x, user_y, user_width, user_height).colliderect(coin.x - 20, coin.y - 20, 40, 40):
        coin.x = randint(5, 795)
        coin.y = randint(5, 595)
        game_count += 1
        delay_timer = 30

    if game_count >= 5:
        font = pygame.font.SysFont('timesnewroman', 30)
        text = font.render('Game Over', True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (400, 300)
        screen.blit(text, textRect)
        pygame.display.update()
        pygame.time.delay(3000)
        run = False

    pygame.display.update()

pygame.quit()
sys.exit()
