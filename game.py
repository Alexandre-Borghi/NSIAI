#coding utf-8
import sys
#Our Class
class Player():
    #This class define the current player

    def __init__(self):
        self.life = 5
        self.score = 0

class Plateform():
    #This class define the platform
    
    def __init__(self):
        self.x0 = 325
        self.x1 = 375
        self.y0 = 350
        self.y1 = 360
        self.colour = 'white'

class Ball():
    # This class define the ball

    def __init__(self):
        self.x0 = 345
        self.x1 = 355
        self.y0 = 340
        self.y1 = 350
        self.colour = 'red'

class Brick():
    #This class define bricks

    def __init__(self):
        self.x0 = 0
        self.x1 = 0
        self.y0 = 0
        self.y1 = 0
        self.colour = 'white'

#Our items
player = Player()
plateform = Plateform()
ball = Ball()
list_brick = []
for i in range(110):
    i = Brick()
    list_brick.append(i)

#Graphic interface


sys.exit()