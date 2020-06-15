#coding utf-8
import sys
import os
import pygame

# Our Function
def percentage(percent, whole):
  return int((percent * whole) / 100.0)

# Our Variables
x_screen = 1080
y_screen = 720
x_GameSurface = percentage(50,x_screen)
y_GameSurface = percentage(50,y_screen)
current_path = os.path.dirname(__file__)
number_bricks = 135
brick_rect_x = 0
brick_rect_y = 0

#Our Class
class Player(pygame.sprite.Sprite):
    #This class define the current player

    def __init__(self):
        self.life = 5
        self.score = 0

class Plateform(pygame.sprite.Sprite):
    #This class define the platform
    
    def __init__(self):
        self.speed = percentage(5,x_GameSurface)
        self.image = pygame.image.load(os.path.join(current_path, 'plateform.png'))
        self.rect = self.image.get_rect()
        self.rect.x = percentage(38, x_GameSurface)
        self.rect.y = percentage(85,y_GameSurface)

class Ball(pygame.sprite.Sprite):
    # This class define the ball

    def __init__(self):
        self.image = pygame.image.load(os.path.join(current_path, 'ball.png'))
        self.rect = self.image.get_rect()
        self.rect.x = percentage(47, x_GameSurface)
        self.rect.y = percentage(80, y_GameSurface)

class Brick(pygame.sprite.Sprite):
    #This class define bricks

    def __init__(self):
        self.image = pygame.image.load(os.path.join(current_path, 'brick.png'))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

#Our items
player = Player()
plateform = Plateform()
ball = Ball()
list_bricks = []

for i in range(number_bricks):
    i = Brick()
    i.rect.x = brick_rect_x
    i.rect.y = brick_rect_y
    brick_rect_x +=10
    if (brick_rect_x + 100) > x_GameSurface:
        brick_rect_y += 30
        brick_rect_x = 0
    list_bricks.append(i)

#Graphic interface
pygame.display.init()
pygame.display.set_caption("Breakout AI")
Window = pygame.display.set_mode((x_screen,y_screen))

#Our Surface
GameSurface = pygame.Surface((x_GameSurface, y_GameSurface))
GameSurface.fill((255,255,255))


#Game loop
running = True
while running :
    pygame.display.update()
    Window.blit(GameSurface, (0,0))
    GameSurface.blit(plateform.image, plateform.rect)
    GameSurface.blit(ball.image, ball.rect)
    
    for items in list_bricks:
        GameSurface.blit(items.image, items.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

sys.exit()