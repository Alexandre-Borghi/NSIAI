#coding utf-8
import sys
import os
import pygame
import random
import time
# Our Function
def percentage(percent, whole):
    return int((percent * whole) / 100.0)

class Player():
    def __init__(self):
        self.score = 0

class Plateform(pygame.sprite.Sprite):
    #This class define platforms
    
    def __init__(self):
        self.speed = percentage(2,y_GameSurface)
        self.image = pygame.image.load(os.path.join(current_path, 'plateform.png'))
        self.rect = self.image.get_rect()
        self.rect.x = percentage(90, x_GameSurface)
        self.rect.y = percentage(38, y_GameSurface)
    
    def move_up(self):
        if self.rect.y + self.speed > percentage(2.7, y_GameSurface):
            self.rect.y -= self.speed
            #print(f"Y: {plateform.rect.y}")
    def move_down(self):
        if self.rect.y - self.speed < percentage(68, y_GameSurface):
            self.rect.y += self.speed
            #print(f"Y: {plateform.rect.y}")

class Ball(pygame.sprite.Sprite):
    # This class define the ball
    
    def __init__(self):
        self.image = pygame.image.load(os.path.join(current_path, 'ball.png'))
        self.rect = self.image.get_rect()
        self.rect.y = percentage(47, y_GameSurface)
        self.rect.x = percentage(random.choice([14,86]), x_GameSurface)
        self.speed_x = percentage(0.2, x_GameSurface)
        self.speed_y = percentage(0.4, y_GameSurface)

# Our Variables
x_screen = 1080
y_screen = 720
x_GameSurface = percentage(50,x_screen)
y_GameSurface = percentage(50,y_screen)
current_path = os.path.dirname(__file__)
number_bricks = 135
brick_rect_x = 0
brick_rect_y = 0
keys_pressed = {}

#Our items
plateform = Plateform()
plateform2 = Plateform()
plateform2.rect.x = percentage(10,x_GameSurface)
plateforms = [plateform, plateform2]
ball = Ball()
player1 = Player()
player2 = Player()

#Graphic interface
pygame.display.init()
pygame.display.set_caption("Ping Pong AI")
Window = pygame.display.set_mode((x_screen,y_screen))

#Our Surface
GameSurface = pygame.Surface((x_GameSurface, y_GameSurface))

#Game loop
running = True
while running :
    
    pygame.display.update()
    GameSurface.fill((255,255,255))

    #Blit items and surface
    GameSurface.blit(plateform.image, plateform.rect)
    GameSurface.blit(plateform2.image, plateform2.rect)
    GameSurface.blit(ball.image, ball.rect)
    Window.blit(GameSurface, (0,0))

    #Ball move
    if ball.rect.x > plateform2.rect.x and ball.rect.x < plateform.rect.x:
        if len(pygame.sprite.spritecollide(ball, plateforms, False, pygame.sprite.collide_mask)) == 0:
            ball.rect.x += ball.speed_x
            ball.rect.y += ball.speed_y
            #print(f'Speed_Y: {ball.speed_y}   |    Y: {ball.rect.y}')
            #print('normal')
        else:
            ball.speed_x *= -1
            ball.rect.x += ball.speed_x
            ball.rect.y += ball.speed_y
            #print(f'collision: speed_y= {ball.speed_y} ')

        if ball.rect.y < percentage(2.7, y_GameSurface) or ball.rect.y > percentage(68, y_GameSurface):
            ball.speed_y *= -1
    
    elif ball.rect.x <= plateform2.rect.x:
        player2.score += 1
        print(f'Les scores sont: {player1.score} point(s) pour le joueur de gauche et {player2.score} pour le joueur de droite')
        ball.rect.y = percentage(47, y_GameSurface)
        ball.rect.x = percentage(random.choice([14,86]), x_GameSurface)
        pygame.display.update()
        time.sleep(1)
        #print (f'X: {ball.rect.x}   |   Y: {ball.rect.y}')

    elif ball.rect.x >= plateform.rect.x:
        player1.score += 1
        print(f'Les scores sont: {player1.score} point(s) pour le joueur de gauche et {player2.score} pour le joueur de droite')
        ball.rect.y = percentage(47, y_GameSurface)
        ball.rect.x = percentage(random.choice([14,86]), x_GameSurface)
        pygame.display.update()
        time.sleep(1)
        #print (f'X: {ball.rect.x}   |   Y: {ball.rect.y}')

    #Events loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                plateform.move_up()
            elif event.key == pygame.K_DOWN:
                plateform.move_down()
            elif event.key == pygame.K_z:
                plateform2.move_up()
            elif event.key == pygame.K_s:
                plateform2.move_down()

sys.exit()