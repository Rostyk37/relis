from pygame import *
from random import randint, choice
import time
import sys
import pygame
window = display.set_mode((1200, 700))
display.set_caption('space battle')
clock = pygame.time.Clock()

pygame.init()
mixer.init()
mixer.music.load('mus_menu (2).ogg')
pygame.mixer.music.set_volume(0.1)
rings = mixer.Sound('rings.mp3')
rings.set_volume(5)

menumus = mixer.Sound('vv.ogg')
menumus.set_volume(0.2)
clickbutton = mixer.Sound('BX0D.mp3')
clickbutton.set_volume(0.1)
gameovermus = mixer.Sound('gameover.mp3')
gameovermus.set_volume(0.2)
#clickbutton = mixer.music.set_volume(0.1)
back = mixer.Sound('EXIT.mp3')
go_start_game = mixer.Sound('go_start_game.mp3')
go_start_game.set_volume(0.1)
VERSIA = 'версія2.1'
back = (0,0,0)

win_width = 1200
win_height = 700
rect_width, rect_height = 570, 87

startgame = True

snece_komix = 1

gamestart = False
gamemenufon = True

opensettings = False
openmenu = False

showfps_off_on = True

img_enemy = 'ast.png'

speed5 = 13
speed2 = 9

BLACK = (0, 0, 0)
spry = 144
sprx = 100

class Logo(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (506,282))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Komix(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (2397,3484))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Sprite2(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (200, 300))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Text(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (500, 300))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (spry, sprx))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Skip(sprite.Sprite):
    #КОНСТРУКТОР КЛАСУ
    def __init__(self, player_image, player_x, player_y,player_speed):
        super().__init__()
        #кожен спрайт повинен зберігати влістивість image - зображення
        self.image = transform.scale(image.load(player_image), (250,70))
        self.speed = player_speed
        #кожен спрайт повинен зберігати властивість rect - прямокутника
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Controlerr(sprite.Sprite):
    #КОНСТРУКТОР КЛАСУ
    def __init__(self, player_image, player_x, player_y,player_speed):
        super().__init__()
        #кожен спрайт повинен зберігати влістивість image - зображення
        self.image = transform.scale(image.load(player_image), (1200,700))
        self.speed = player_speed
        #кожен спрайт повинен зберігати властивість rect - прямокутника
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Sprite(sprite.Sprite):
    #КОНСТРУКТОР КЛАСУ
    def __init__(self, player_image, player_x, player_y, size_x,size_y,player_speed):
        super().__init__()
        #кожен спрайт повинен зберігати влістивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        #кожен спрайт повинен зберігати властивість rect - прямокутника
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Button(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (rect_width, rect_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

timekomix = 0

class Enemy(Sprite):
    def update(self):
        if timekomix <= 1:
            self.rect.x -= self.speed
            if self.rect.x < -1500:
                self.rect.x += 2700
                self.rect.y = randint(10, 700 - 70)

class Area():
    def __init__(self,x=0,y=0,width=10, height=0, color=(255, 255, 255)):
        self.rect =pygame.Rect(x,y,width,height)
        self.fill_color = color
    def color(self,new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window,self.fill_color,self.rect)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(window,frame_color,self.rect, thickness)
class Label(Area):
    def set_text(self, text,fsize=12,text_color=BLACK):
        self.image = pygame.font.Font(None, fsize).render(text,True, text_color)
    def draw(self, shift_x=0,shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x,self.rect.y + shift_y))
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
class Picture(Area):
    def __init__(self,filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width ,height=height)
        self.image = pygame.image.load(filename)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GameBlack(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()   
        self.image = transform.scale(image.load(player_image), (1200, 700))
        self.speed = player_speed      
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

black = GameBlack('black.jpg', 0, 0 - 0, 0)

komixlevel = 2
komixsex = 0

poletkomix = 0
tkm = 0
TIMErr = 59
t59 = 0
plusspr = 0
polet = 0

text11 = 5
speed1 = 10
speed2 = 9
speed3 = 11
speed4 = 20
speed5 = 13
speed20 = 400
off = 2
textime = 0
shut = 5
POWER = 51
l = 50
TIME = 0 
TIMEM = 0 
BAL = 0
BLACK = 0, 0, 0
gm = 0
ov = 0
shon = 250
shan = 400

class Gamesara(sprite.Sprite):   
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()       
        self.image = transform.scale(image.load(player_image), (230, 64))
        self.speed = player_speed       
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def reset2(self):
        window.blit('shut.png', (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        if startgame == True:
            if off <= 3:
                if POWER >= 1:
                    keys = key.get_pressed()
                    if keys[K_a] and self.rect.x > 5:
                        self.rect.x -= speed5
                    if keys[K_d] and self.rect.x < 1200 - 150:
                        self.rect.x += speed2
                    if keys[K_w] and self.rect.y > 5:
                        self.rect.y -= speed2
                    if keys[K_s] and self.rect.y < 775 - 175:
                        self.rect.y += speed2        
class GameBlack(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()   
        self.image = transform.scale(image.load(player_image), (1200, 700))
        self.speed = player_speed      
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GameFon(sprite.Sprite):  
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()     
        self.image = transform.scale(image.load(player_image), (2400, 700))
        self.speed = player_speed       
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GameText(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()   
        self.image = transform.scale(image.load(player_image), (840, 32))
        self.speed = player_speed      
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GameAst(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (128, 124))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GameFync(GameAst):
    def update(self):
        if off <= 3:
            if self.rect.x <= -1200:
                reset_pipe(self, pipe_positions)
            if self.rect.colliderect(rocket1.rect):
                global GAMEOVER
                GAMEOVER = True
    
class GameFyncc(GameAst):
    def update(self):
        if off <= 3:
            if self.rect.x <= -1200:
                reset_pipe(self, pipe_positions)

class GamePow(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()       
        self.image = transform.scale(image.load(player_image), (108, 50))
        self.speed = player_speed       
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

GAMEOVER =  False
rocket1 = Player('rocket.png', 5, 0 - -325, 0)

class GameOverG(Gamesara):
    def update(self):
        if GAMEOVER == True:
            rocket1.rect.y -= 0



Power = GamePow('power.png', -200, 0 - -325, 0)

fonugru = GameFon('fon.png', 0, 50 - 50, 50)

rectx = 0

def reset_pipe(pipe_top, pipe_positions):
    pipe_height = choice(pipe_positions)
    pipe_top.rect.y = pipe_height[0]
    pipe_top.rect.x = pipe_height[1]


pipe_positions = [
    (-50,1250),
    (0,1250),
    (50,1250),
    (100,1250),
    (150,1250),
    (200,1250),
    (250,1250),
    (300,1250),
    (350,1250),
    (400,1250),
    (450,1250),
    (500,1250),
    (550,1250),
    (600,1250),
    (650,1250),
    (700,1250),

    (-50,1500),
    (0,1500),
    (50,1500),
    (100,1500),
    (150,1500),
    (200,1500),
    (250,1500),
    (300,1500),
    (350,1500),
    (400,1500),
    (450,1500),
    (500,1500),
    (550,1500),
    (600,1500),
    (650,1500),
    (700,1500),

    (-50,1750),
    (0,1750),
    (50,1750),
    (100,1750),
    (150,1750),
    (200,1750),
    (250,1750),
    (300,1750),
    (350,1750),
    (400,1750),
    (450,1750),
    (500,1750),
    (550,1750),
    (600,1750),
    (650,1750),
    (700,1750),

    (-50,2000),
    (0,2000),
    (50,2000),
    (100,2000),
    (150,2000),
    (200,2000),
    (250,2000),
    (300,2000),
    (350,2000),
    (400,2000),
    (450,2000),
    (500,2000),
    (550,2000),
    (600,2000),
    (650,2000),
    (700,2000),

    (-50,2250),
    (0,2250),
    (50,2250),
    (100,2250),
    (150,2250),
    (200,2250),
    (250,2250),
    (300,2250),
    (350,2250),
    (400,2250),
    (450,2250),
    (500,2250),
    (550,2250),
    (600,2250),
    (650,2250),
    (700,2250),

    (-50,2500),
    (0,2500),
    (50,2500),
    (100,2500),
    (150,2500),
    (200,2500),
    (250,2500),
    (300,2500),
    (350,2500),
    (400,2500),
    (450,2500),
    (500,2500),
    (550,2500),
    (600,2500),
    (650,2500),
    (700,2500),

    (-50,2750),
    (0,2750),
    (50,2750),
    (100,2750),
    (150,2750),
    (200,2750),
    (250,2750),
    (300,2750),
    (350,2750),
    (400,2750),
    (450,2750),
    (500,2750),
    (550,2750),
    (600,2750),
    (650,2750),
    (700,2750),

    (-50,3000),
    (0,3000),
    (50,3000),
    (100,3000),
    (150,3000),
    (200,3000),
    (250,3000),
    (300,3000),
    (350,3000),
    (400,3000),
    (450,3000),
    (500,3000),
    (550,3000),
    (600,3000),
    (650,3000),
    (700,3000),

    (-50,3250),
    (0,3250),
    (50,3250),
    (100,3250),
    (150,3250),
    (200,3250),
    (250,3250),
    (300,3250),
    (350,3250),
    (400,3250),
    (450,3250),
    (500,3250),
    (550,3250),
    (600,3250),
    (650,3250),
    (700,3250),

    (-50,3500),
    (0,3500),
    (50,3500),
    (100,3500),
    (150,3500),
    (200,3500),
    (250,3500),
    (300,3500),
    (350,3500),
    (400,3500),
    (450,3500),
    (500,3500),
    (550,3500),
    (600,3500),
    (650,3500),
    (700,3500),

    (-50,3750),
    (0,3750),
    (50,3750),
    (100,3750),
    (150,3750),
    (200,3750),
    (250,3750),
    (300,3750),
    (350,3750),
    (400,3750),
    (450,3750),
    (500,3750),
    (550,3750),
    (600,3750),
    (650,3750),
    (700,3750),

    (-50,4000),
    (0,4000),
    (50,4000),
    (100,4000),
    (150,4000),
    (200,4000),
    (250,4000),
    (300,4000),
    (350,4000),
    (400,4000),
    (450,4000),
    (500,4000),
    (550,4000),
    (600,4000),
    (650,4000),
    (700,4000),

    (-50,4250),
    (0,4250),
    (50,4250),
    (100,4250),
    (150,4250),
    (200,4250),
    (250,4250),
    (300,4250),
    (350,4250),
    (400,4250),
    (450,4250),
    (500,4250),
    (550,4250),
    (600,4250),
    (650,4250),
    (700,4250),

    (-50,4500),
    (0,4500),
    (50,4500),
    (100,4500),
    (150,4500),
    (200,4500),
    (250,4500),
    (300,4500),
    (350,4500),
    (400,4500),
    (450,4500),
    (500,4500),
    (550,4500),
    (600,4500),
    (650,4500),
    (700,4500),

    (-50,4750),
    (0,4750),
    (50,4750),
    (100,4750),
    (150,4750),
    (200,4750),
    (250,4750),
    (300,4750),
    (350,4750),
    (400,4750),
    (450,4750),
    (500,4750),
    (550,4750),
    (600,4350),
    (650,4750),
    (700,4750),
    
    (-50,5000),
    (0,5000),
    (50,5000),
    (100,5000),
    (150,5000),
    (200,5000),
    (250,5000),
    (300,5000),
    (350,5000),
    (400,5000),
    (450,5000),
    (500,5000),
    (550,5000),
    (600,5000),
    (650,5000),
    (700,5000),
]

shutcolor = Gamesara('sara.png', 0, 0 - -625, 0)

shutnocolor = Gamesara('sar.png', 0, 0 - -825, 0)

gamet = GameOverG('game.png', -300, 0 - -325, 0)
overt = Gamesara('over.png', 1200, 0 - -325, 0)

textshut = GameText('text1.png', 200, 0 - -150, 0)

black1 = GameBlack('black.jpg', 0, 0 - 700, 0)
black2 = GameBlack('black.jpg', 0, 0 - -700, 0)

ast00 = GameFync('ast.png', -1000, 160 - -255, 155)
ast11 = GameFync('ast.png', -1000, 160 - -255, 155)
ast22 = GameFync('ast.png', -1000, 160 - -255, 155)
ast33 = GameFync('ast.png', -1000, 160 - -255, 155)
ast44 = GameFync('ast.png', -1000, 160 - -255, 155)
ast55 = GameFync('ast.png', -1000, 160 - -250, 155)
#4 сірих астероїди
ast66 = GameFyncc('astg.png', -1000, 160 - -255, 155)
ast77 = GameFyncc('astg.png', -1000, 160 - -255, 155)
ast88 = GameFyncc('astg.png', -1000, 160 - -255, 155)
ast99 = GameFyncc('astg.png', -1000, 160 - -255, 155)


def reset_pipee(pipe_topp, pipe_positionss):
    pipe_heightt = choice(pipe_positionss)
    pipe_topp.rect.y = pipe_heightt[0]
    pipe_topp.rect.x = pipe_heightt[1]

pipe_positionss = [
    (-50,1250),
    (0,1250),
    (50,1250),
    (100,1250),
    (150,1250),
    (200,1250),
    (250,1250),
    (300,1250),
    (350,1250),
    (400,1250),
    (450,1250),
    (500,1250),
    (550,1250),
    (600,1250),
    (650,1250),
    (700,1250),

    (-50,1500),
    (0,1500),
    (50,1500),
    (100,1500),
    (150,1500),
    (200,1500),
    (250,1500),
    (300,1500),
    (350,1500),
    (400,1500),
    (450,1500),
    (500,1500),
    (550,1500),
    (600,1500),
    (650,1500),
    (700,1500),

    (-50,1750),
    (0,1750),
    (50,1750),
    (100,1750),
    (150,1750),
    (200,1750),
    (250,1750),
    (300,1750),
    (350,1750),
    (400,1750),
    (450,1750),
    (500,1750),
    (550,1750),
    (600,1750),
    (650,1750),
    (700,1750),

    (-50,2000),
    (0,2000),
    (50,2000),
    (100,2000),
    (150,2000),
    (200,2000),
    (250,2000),
    (300,2000),
    (350,2000),
    (400,2000),
    (450,2000),
    (500,2000),
    (550,2000),
    (600,2000),
    (650,2000),
    (700,2000),

    (-50,2250),
    (0,2250),
    (50,2250),
    (100,2250),
    (150,2250),
    (200,2250),
    (250,2250),
    (300,2250),
    (350,2250),
    (400,2250),
    (450,2250),
    (500,2250),
    (550,2250),
    (600,2250),
    (650,2250),
    (700,2250),

    (-50,2500),
    (0,2500),
    (50,2500),
    (100,2500),
    (150,2500),
    (200,2500),
    (250,2500),
    (300,2500),
    (350,2500),
    (400,2500),
    (450,2500),
    (500,2500),
    (550,2500),
    (600,2500),
    (650,2500),
    (700,2500),

    (-50,2750),
    (0,2750),
    (50,2750),
    (100,2750),
    (150,2750),
    (200,2750),
    (250,2750),
    (300,2750),
    (350,2750),
    (400,2750),
    (450,2750),
    (500,2750),
    (550,2750),
    (600,2750),
    (650,2750),
    (700,2750),

    (-50,3000),
    (0,3000),
    (50,3000),
    (100,3000),
    (150,3000),
    (200,3000),
    (250,3000),
    (300,3000),
    (350,3000),
    (400,3000),
    (450,3000),
    (500,3000),
    (550,3000),
    (600,3000),
    (650,3000),
    (700,3000),

    (-50,3250),
    (0,3250),
    (50,3250),
    (100,3250),
    (150,3250),
    (200,3250),
    (250,3250),
    (300,3250),
    (350,3250),
    (400,3250),
    (450,3250),
    (500,3250),
    (550,3250),
    (600,3250),
    (650,3250),
    (700,3250),

    (-50,3500),
    (0,3500),
    (50,3500),
    (100,3500),
    (150,3500),
    (200,3500),
    (250,3500),
    (300,3500),
    (350,3500),
    (400,3500),
    (450,3500),
    (500,3500),
    (550,3500),
    (600,3500),
    (650,3500),
    (700,3500),

    (-50,3750),
    (0,3750),
    (50,3750),
    (100,3750),
    (150,3750),
    (200,3750),
    (250,3750),
    (300,3750),
    (350,3750),
    (400,3750),
    (450,3750),
    (500,3750),
    (550,3750),
    (600,3750),
    (650,3750),
    (700,3750),

    (-50,4000),
    (0,4000),
    (50,4000),
    (100,4000),
    (150,4000),
    (200,4000),
    (250,4000),
    (300,4000),
    (350,4000),
    (400,4000),
    (450,4000),
    (500,4000),
    (550,4000),
    (600,4000),
    (650,4000),
    (700,4000),

    (-50,4250),
    (0,4250),
    (50,4250),
    (100,4250),
    (150,4250),
    (200,4250),
    (250,4250),
    (300,4250),
    (350,4250),
    (400,4250),
    (450,4250),
    (500,4250),
    (550,4250),
    (600,4250),
    (650,4250),
    (700,4250),

    (-50,4500),
    (0,4500),
    (50,4500),
    (100,4500),
    (150,4500),
    (200,4500),
    (250,4500),
    (300,4500),
    (350,4500),
    (400,4500),
    (450,4500),
    (500,4500),
    (550,4500),
    (600,4500),
    (650,4500),
    (700,4500),

    (-50,4750),
    (0,4750),
    (50,4750),
    (100,4750),
    (150,4750),
    (200,4750),
    (250,4750),
    (300,4750),
    (350,4750),
    (400,4750),
    (450,4750),
    (500,4750),
    (550,4750),
    (600,4350),
    (650,4750),
    (700,4750),
    
    (-50,5000),
    (0,5000),
    (50,5000),
    (100,5000),
    (150,5000),
    (200,5000),
    (250,5000),
    (300,5000),
    (350,5000),
    (400,5000),
    (450,5000),
    (500,5000),
    (550,5000),
    (600,5000),
    (650,5000),
    (700,5000),
]

start=time.time()
cur_time=start
end=time.time()

time_text = Label(0,0,0,0,back)
time_text.set_text("time", 75, (250, 250, 0))

#це для секунд
timers = Label(0,0,0,0,back)
timers.set_text("0",75, (250, 250, 0))

#це для хвилини
timerm = Label(0,0,0,0,back)
timerm.set_text("0",75, (250, 250, 0))

#для красоти дво крапка
iss = Label(0,0,0,0,back)
iss.set_text(":",75, (250, 250, 0))

#текст power і таймер енергії
poweR_text = Label(290,0,0,0,back)
poweR_text.set_text("power", 75, (250, 250, 0))

#таймер енергії
poweR = Label(400,0,0,0,back)
poweR.set_text("0", 75, (250, 250, 0))

#бали або score і текст(за них можна буде сбирати життя)
BALu_TEXT = Label(290,0,0,0,back)
BALu_TEXT.set_text("score", 75, (250, 250, 0))

#бали score
BALu = Label(400,0,0,0,back)
BALu.set_text("0", 75, (250, 250, 0))


gorect = 0
mus = False
rrr = 0
e = 0


while startgame:

    fonugru.rect.x -= 13
    Power.rect.x -= speed3
    ast00.rect.x -= speed3
    ast11.rect.x -= speed3
    ast22.rect.x -= speed3
    ast33.rect.x -= speed3
    ast44.rect.x -= speed3
    ast55.rect.x -= speed3
    ast66.rect.x -= speed3
    ast77.rect.x -= speed3
    ast88.rect.x -= speed3
    ast99.rect.x -= speed3

    for event in pygame.event.get():
        if event.type == QUIT:
            startgame = False
        if event.type == pygame.KEYDOWN:
            #щит ракети за допомогою нього можна ламати сірі астероїди(проблема як зробити так щоб коли щит буде працювати то змінився спрайт ракети на 'щит'а коли закінчиться сам щит то змінеться на спрайт 'ракета)
            if event.key == pygame.K_e:
                if off <= 3:
                    if shon == 250:
                        if shan == 400:
                            shutcolor.rect.y += 200
                            shutnocolor.rect.y -= 200
                            shon -= 250
                            shan -= 400
                            shut -=2
    if shan <= 399:
        shan += 1

    if shan == 399:
        shutcolor.rect.y -= 200
        shutnocolor.rect.y += 200

    if shon <= 249:
        shon += 1
    
    if shon == 249:
        shut +=2
        #(тут щоб змінився на спрайт 'rocket')код
    
    if fonugru.rect.x <= -1200:
        fonugru.rect.x += 1200

    if off <= 3:
        if Power.rect.x <= -700:
            reset_pipee(Power, pipe_positionss)

    if shut >= 4:
        if off <= 3:
            if ast66.rect.colliderect(rocket1.rect):
                GAMEOVER = True
    else: 
        if off <= 3:
            if ast66.rect.colliderect(rocket1.rect):
                reset_pipee(ast66, pipe_positionss)
                BAL += 150

    if shut >= 4:
        if off <= 3:
            if ast77.rect.colliderect(rocket1.rect):
                GAMEOVER = True
    else:
        if off <= 3:
            if ast77.rect.colliderect(rocket1.rect):
                reset_pipee(ast77, pipe_positionss)
                BAL += 150

    if shut >= 4:
        if off <= 3:
            if ast88.rect.colliderect(rocket1.rect):
                GAMEOVER = True
    else:
        if off <= 3:
            if ast88.rect.colliderect(rocket1.rect):
                reset_pipee(ast88, pipe_positionss)
                BAL += 150

    if shut >= 4:
        if off <= 3:
            if ast99.rect.colliderect(rocket1.rect):
                GAMEOVER = True
                mus = True
    else:
        if off <= 3:
            if ast99.rect.colliderect(rocket1.rect):
                reset_pipee(ast99, pipe_positionss)
                BAL += 150

    if off <= 3:
        if rocket1.rect.colliderect(Power.rect):
            Power.rect.x -= 1600
            POWER += 7

    if POWER < 1:
        rocket1.rect.y +=30
        off += 3

    if off <= 3:
        if l == 50:
            l -= 50
            POWER -= 1
        else:
            l += 1

    if l == 5:
        TIME += 1

    if TIME ==60:
        TIME -=60
        TIMEM += 1

    if TIME == 5:
        textshut.rect.y -= speed20 

    if rrr == 1:
        if mus == True:
            gameovermus.play()
            menumus.stop()
            mus = False

    if GAMEOVER == True:  
        rocket1.rect.y += 20
        off += 3
        if rocket1.rect.y >= 1500:
            mus = True
            rrr += 1
            if gorect >= 300:
                gorect += 1
                gamet.rect.x -= 10
                overt.rect.x += 10
                if black1.rect.y <= -100:
                    black1.rect.y += 12
                if black2.rect.y >= 350:
                    black2.rect.y -= 12
            else:
                gorect += 1
                if gamet.rect.x <= 300:
                    gamet.rect.x += 10
                if overt.rect.x >= 600:
                    overt.rect.x -= 10

            if gorect == 400:
                menugame = True
                rrr -= rrr
                gorect -= 400
                off -= 3
                startgame = False

    fonugru.update()
    shutcolor.update()
    shutnocolor.update()
    rocket1.update()

    ast00.update() 
    ast11.update() 
    ast22.update() 
    ast33.update() 
    ast44.update() 
    ast55.update() 
    ast66.update() 
    ast77.update() 
    ast88.update() 
    ast99.update() 
    textshut.update()
    Power.update()


    fonugru.reset()
    shutcolor.reset()
    shutnocolor.reset()
    rocket1.reset()

    ast00.reset()
    ast11.reset()
    ast22.reset()
    ast33.reset()
    ast44.reset()
    ast55.reset()
    ast66.reset()
    ast77.reset()
    ast88.reset()
    ast99.reset()
    textshut.reset()
    Power.reset()

    poweR.set_text(str(POWER), 75, (250, 250, 0))
    poweR.draw(-220,100)
    poweR_text.draw(-275,100)

    timers.set_text(str(TIME), 75, (250, 250, 0))
    timers.draw(180,50)
    timerm.set_text(str(TIMEM), 75, (250, 250, 0))
    timerm.draw(130,50)
    time_text.draw(18,50)
    iss.draw(160,50)
    
    BALu.set_text(str(BAL), 75, (250, 250, 0))
    BALu.draw(-230,0)
    BALu_TEXT.draw(-275,0)

    font = pygame.font.SysFont("Arial", 60)
    fps = str(int(clock.get_fps()))
    fps_text = font.render(f"FPS: {fps}", True, (255, 255, 255))
    window.blit(fps_text, (10, 10))

    black1.reset()
    black2.reset()
    black1.update()
    black2.update()
    gamet.reset()
    overt.reset()
    gamet.update()
    overt.update()

    display.update()
    clock.tick(60)

