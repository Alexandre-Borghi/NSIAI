#coding utf-8
import sys
import os
import pygame
import random
import time

# Our Function
def percentage(percent, whole):
    return int((percent * whole) / 100.0)

#Our Classes
class Player():
    def __init__(self):
        self.score = 0

class Plateform(pygame.sprite.Sprite):
    #This class define platforms

    def __init__(self):
        self.speed = percentage(6,y_GameSurface)
        self.image = pygame.image.load(os.path.join(current_path, 'plateform.png'))
        self.rect = self.image.get_rect()
        self.rect.x = percentage(90, x_GameSurface)
        self.rect.y = percentage(38, y_GameSurface)

    def move_up(self):
        if self.speed < 0 :
            self.speed *= -1
        #print(f'speed: {self.speed}')
        if self.rect.y + self.speed > percentage(2.7, y_GameSurface):
            self.rect.y -= self.speed
            #print(f"Y: {plateform.rect.y}")

    def move_down(self):
        if self.speed > 0 :
            self.speed *= -1
        #print(f'speed: {self.speed}')
        if self.rect.y - self.speed < percentage(68, y_GameSurface):
            self.rect.y -= self.speed
            #print(f"Y: {plateform.rect.y}")

    def position_start(self, x):
        self.rect.x = percentage(x, x_GameSurface)
        self.rect.y = percentage(38, y_GameSurface)

class Ball(pygame.sprite.Sprite):
    # This class define the ball
    
    def __init__(self):
        self.image = pygame.image.load(os.path.join(current_path, 'ball.png'))
        self.rect = self.image.get_rect()
        self.rect.y = percentage(47, y_GameSurface)
        self.rect.x = percentage(random.choice([14,86]), x_GameSurface)
        self.speed_x = percentage(0.19, x_GameSurface)
        self.speed_y = percentage(0.4, y_GameSurface)

class Play(pygame.sprite.Sprite):
    #This class define play button

    def __init__(self):
        self.button = pygame.image.load(os.path.join(current_path, 'play.png'))
        self.rect = self.button.get_rect()
        self.rect.x = percentage(35, x_GameSurface)
        self.rect.y = percentage(45, y_GameSurface)

class Train(pygame.sprite.Sprite):
    #This class define the training_button

    def __init__(self):
        self.button = pygame.image.load(os.path.join(current_path, 'train.png'))
        self.rect = self.button.get_rect()
        self.rect.x = percentage(30,x_GameSurface)
        self.rect.y = percentage(70, y_GameSurface)

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
game_is_playing = False
game_is_training = False
#Our items
plateform = Plateform()
plateform2 = Plateform()
plateform2.rect.x = percentage(10,x_GameSurface)
plateforms = [plateform, plateform2]
ball = Ball()
player1 = Player()
player2 = Player()
banner = pygame.image.load(os.path.join(current_path, 'banner.png'))
play = Play()
training = Train()
background = pygame.image.load(os.path.join(current_path,'background.jpg'))

#Graphic interface
pygame.init()
pygame.display.init()
pygame.display.set_caption("Ping Pong AI")
Window = pygame.display.set_mode((x_screen,y_screen))

#Our Surface
GameSurface = pygame.Surface((x_GameSurface, y_GameSurface))

#Game loop
running = True
while running :

    pygame.display.update()
    GameSurface.blit(background, (0,0))

    if game_is_playing:
        #Blit items and surface
        def blit_items():
            GameSurface.blit(plateform.image, plateform.rect)
            GameSurface.blit(plateform2.image, plateform2.rect)
            GameSurface.blit(ball.image, ball.rect)
            Window.blit(GameSurface, (0,0))

        blit_items()

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
                if ball.rect.x > percentage(50, x_GameSurface):
                    ball.rect.y += plateform.speed
                else:
                    ball.rect.y += plateform2.speed
                #print(f'collision: speed_y= {ball.speed_y} ')

            if ball.rect.y < percentage(2.7, y_GameSurface) or ball.rect.y > percentage(68, y_GameSurface):
                ball.speed_y *= -1

        elif ball.rect.x <= plateform2.rect.x:
            player2.score += 1
            if player2.score == 10:
                player2.score = 0
                print('Game Over, the winner is Player 2')
            else:
                print(f'The scores are: {player1.score} point(s) for the left player and {player2.score} point(s) for the right player.')
                ball.rect.y = percentage(47, y_GameSurface)
                ball.rect.x = percentage(random.choice([14,86]), x_GameSurface)
                plateform.position_start(90)
                plateform2.position_start(10)
                blit_items()
                pygame.display.update()
                time.sleep(1)
                #print (f'X: {ball.rect.x}   |   Y: {ball.rect.y}')

        elif ball.rect.x >= plateform.rect.x:
            player1.score += 1
            if player1.score == 10:
                player1.score = 0
                print('Game Over, the winner is Player 1')
            else:
                print(f'The scores are: {player1.score} point(s) for the left player and {player2.score} point(s) for the right player.')
                ball.rect.y = percentage(47, y_GameSurface)
                ball.rect.x = percentage(random.choice([14,86]), x_GameSurface)
                plateform.position_start(90)
                plateform2.position_start(10)
                blit_items()
                pygame.display.update()
                time.sleep(1)
                #print (f'X: {ball.rect.x}   |   Y: {ball.rect.y}')

        #Events loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                        plateform.move_up()
                elif event.key == pygame.K_DOWN:
                        plateform.move_down()
                elif event.key == pygame.K_z:
                        plateform2.move_up()
                elif event.key == pygame.K_s:
                        plateform2.move_down()

    elif game_is_playing == False:
        GameSurface.blit(banner, (percentage(10,x_GameSurface),percentage(10, y_GameSurface)))
        GameSurface.blit(play.button, play.rect)
        GameSurface.blit(training.button, training.rect)
        Window.blit(GameSurface, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play.rect.collidepoint(event.pos):
                game_is_playing = True
            elif training.rect.collidepoint(event.pos):
                game_is_training = True

pygame.quit()
sys.exit()