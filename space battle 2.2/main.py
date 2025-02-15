from pygame import *
from random import randint, choice
import random
import time
import sys
import pygame
win_width = 1200
win_height = 700
window = display.set_mode((win_width,win_height))
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
clickbutton.set_volume(0.3)
gameovermus = mixer.Sound('gameover.mp3')
gameovermus.set_volume(0.2)
finalmus = mixer.Sound('finalzcenee.mp3')
finalmus.set_volume(0.2)
#clickbutton = mixer.music.set_volume(0.1)
back = mixer.Sound('EXIT.mp3')
go_start_game = mixer.Sound('go_start_game.mp3')
go_start_game.set_volume(0.1)
VERSIA = 'версія2.1'
back = (0,0,0)

rect_width, rect_height = 570, 87

logo = True
menugame = False
menusettings = False
komix_start = False
Controler = False
startgame = False
final = False
gamemode = False
gamemodefon = False

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
sizex,sizey = 506,282

class Spri(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,sizex,sizey):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (sizex,sizey))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Sprites(sprite.Sprite):
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

class Fon(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (win_width * 2,win_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        if fon.rect.x <= -1200:
            self.rect.x += 1200

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (100,100))
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

timekomix = 0

class Enemy(GameSprite):
    def update(self):
        if timekomix <= 1:
            self.rect.x -= self.speed
            if self.rect.x < -1500:
                self.rect.x += 3000
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

black = Spri('black.jpg', 0, 0 - 0, 0,1200, 700)


fon = Fon ('menufon.png', 0, 0, 0)
logoo = Spri ('logo.png', 335, -900, 0,506,282)

sprite1 = Spri('rocket.png', 0, 325, 0,2000,100)
sprite2 = Spri('rocket90.png', 500, 300, 0,200,300)

text = Spri('nametext.png', 650, 100,0,500,300)

skip = Spri('skip.png', 900, 600,0,250,70)

controler = Spri('control.png', 0, 0,0,1200,700)

komix = Spri('komix.png', 0, 0,0,2397,3484)
button_start = Spri('button.png', win_width / 24,win_height / 7,0,570,87)
button_settings = Spri('button.png', win_width / 24,win_height / 2.8,0,570,87)
button_ShowScores = Spri('button.png', win_width / 24,win_height / 1.75,0,570,87)
button_quit = Spri('button.png', win_width / 24,win_height/ 1.27,0,570,87)

buttonshow_fps = Spri('button.png', 50, 100,0,570,87)

button_back_settings = Spri('button.png', 550, 550,0,570,87)

ready_button = Spri('readybutton.png', 0, 0,0,570,87)

def handle_button_click(button_rect, action):
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        action()

def start_game():
    global komix_start,menugame,gamemenufon
    go_start_game.play()
    komix_start = True
    menugame = False
    gamemenufon = False
    print("Start Game")

def open_settings():
    global menugame,menusettings
    clickbutton.play()
    menusettings = True
    menugame = False
    print("Open Settings")

def show_scores():
    clickbutton.play()
    print("Show Scores")

r = 0
darkening = False
spritee2 = pygame.image.load("black.jpg")
spritee2 = pygame.transform.scale(spritee2, (win_width,win_height))
quitting = False
timeblack = 0
QUIT = False
 
def quit_game():
    global QUIT,logo,startgame,menugame,menusettings,Controler,final,gamemode,gamemodefon,gamestart,gamemenufon,opensettings,openmenu,showfps_off_on,komix_start
    logo = False
    clickbutton.play()
    menugame = False
    menusettings = False
    komix_start = False
    Controler = False
    startgame = False
    final = False
    gamemode = False
    gamemodefon = False
    gamestart = False
    gamemenufon = True
    opensettings = False
    openmenu = False
    showfps_off_on = True

showfps_off_on = True
def menufon():   
    sprite1.rect.x +=10

def show__fps():
    clickbutton.play()
    print("show fps")

def back_seti():
    clickbutton.play()
    global menugame,menusettings
    menugame = True
    menusettings = False
    print('back settings')

def reset_pipe(pipe_top, pipe_positions):
    pipe_height = choice(pipe_positions)
    pipe_top.rect.y = pipe_height[0]
    pipe_top.rect.x = pipe_height[1]

pipe_positions = [
    (0,-200),
    (200,-200),
    (300,-200),
    (400,-200),
    (500,-200),
    (600,-200),
    (700,-200),
]

square_size = 150
square_x = (win_width - square_size) // 4
square_y = (win_height - square_size) // 4

asts = sprite.Group()
for i in range(1, 6):
    ast = Enemy(img_enemy, randint(
        50, win_width - 1150), 300,  randint(5, 15))
    asts.add(ast)

alpha = 255
direction = -1  
speed = 2

background = pygame.image.load("logo.png")  
background = pygame.transform.scale(background, (win_width, win_height))

dark_surface = pygame.Surface((win_width, win_height))
dark_surface.fill((0, 0, 0))  

lololo = 0
keybord = True

sequence = [pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_DOWN, pygame.K_a]
index = 0
onmode = True
while logo:
    alpha += direction * speed
    black.reset()
    black.update()
    logoo.reset()
    logoo.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            logo = False
        if event.type == pygame.KEYDOWN:
            if onmode == True:
                if event.key == sequence[index]:
                    index += 1
                    if index == len(sequence):
                        onmode = False
                        rings.play()
                        gamemode = True
                else:
                    index = 0
    if QUIT == True:
        timeblack = 0
        alph2 = 0
        timeblack += 1
        alph2 += 5
        if timeblack == 100:
            print("Quit Game")
            logo = False
            menugame = False

    if logoo.rect.y <= 200:
        logoo.rect.y += 10

    if lololo == 200:
        rings.play()

    if lololo >= 400:
        lololo += 1
        if alpha <= 0: 
            direction = 4
    else:
        lololo += 1

    if lololo == 550:
        if gamemode == False:            
            lololo -= 551
            mixer.music.play(-1)
            menugame = True
            logo = False
        else:
            gamemode = True
            lololo -= 551
            mixer.music.play(-1)
            menugame = True
            logo = False

    dark_surface.set_alpha(alpha)
    window.blit(dark_surface, (0, 0))

        
    if QUIT == True:
        alph2 = max(0, min(255, alph2))
        spritee2.set_alpha(alph2)
        window.blit(spritee2, (0, 0))
    display.update()
    clock.tick(60)

#якщо нажати на логотпі автора на кнопки верх,право,ліво,низ,А, то запуститься gamemode 
#        A
#       AAA
#      A A A
#        A
#        A
#        A

#        AAA
#          AAA
#  AAAAAAAAAAAAA
#          AAA
#        AAA 

#      AAA  
#    AAA      
#  AAAAAAAAAAA
#    AAA   
#      AAA 

#        A
#        A
#        A 
#      A A A
#       AAA
#        A

#        A
#       A A
#      A   A
#     AAAAAAA
#    A       A
#   A         A

#якщо зробили все правильно то почуєте ще раз звук логотипа

while menugame:
    font = pygame.font.SysFont("Arial", 18)
    fon.rect.x -= 3
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menugame = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            if menugame:
                handle_button_click(button_start.rect, start_game)
                #handle_button_click(button_settings.rect, open_settings)
                handle_button_click(button_ShowScores.rect, show_scores)
                handle_button_click(button_quit.rect, quit_game)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    fon.reset()
    fon.update()
    sprite1.reset()
    sprite1.update()
    
    if gamemenufon == True:
        menufon()
        asts.update()
        asts.draw(window)
        if sprite1.rect.x >= 2500:
            reset_pipe(sprite1, pipe_positions)

    text.reset()
    text.update()

    fps = str(int(clock.get_fps()))
    fps_text = font.render(f"FPS: {fps}", True, (255, 255, 255))
    window.blit(fps_text, (10, 10))

    font = pygame.font.SysFont("Arial", 60)
    
    button_start.reset()
    button_start.update()
    newgame = font.render(f"NEW GAME", True, (70, 70, 70))
    window.blit(newgame , (win_width / 6, win_height / 6.4))

    button_settings.reset()
    button_settings.update()
    settings = font.render(f"SETTINGS", True, (70, 70, 70))
    window.blit(settings, (win_width / 5.8, win_height / 2.7))

    button_ShowScores.reset()
    button_ShowScores.update()
    showscore = font.render(f"SHOWSCORE", True, (70, 70, 70))
    window.blit(showscore, (win_width / 7, win_height / 1.7))
    
    button_quit.reset()
    button_quit.update()
    quot = font.render(f"QUOT", True, (70, 70, 70))
    window.blit(quot, (win_width / 4.5, win_height / 1.25))       
    
    versia = font.render(VERSIA, True, (255, 255, 255))
    window.blit(versia, (win_width / 1.25, win_height / 1.15))


    display.update()
    clock.tick(60)


while menusettings:
    fon.rect.x -= 3
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menusettings = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            if menusettings:
                handle_button_click(buttonshow_fps.rect, show__fps)
                handle_button_click(button_back_settings.rect, back_seti)
                #handle_button_click(button_start.rect, start_game)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    fon.reset()
    fon.update()
    sprite1.reset()
    sprite1.update()
    
    if gamemenufon == True:
        menufon()
        asts.update()
        asts.draw(window)
        if sprite1.rect.x >= 2500:
            reset_pipe(sprite1, pipe_positions)

    text.reset()
    text.update()

    button_start.reset()
    button_start.update()
    newgame = font.render(f"NEW GAME", True, (70, 70, 70))
    window.blit(newgame , (200, 110))

    fps = str(int(clock.get_fps()))
    fps_text = font.render(f"FPS: {fps}", True, (255, 255, 255))
    window.blit(fps_text, (10, 10))

    font = pygame.font.SysFont("Arial", 60)
    
    #buttonshow_fps.reset()
    #buttonshow_fps.update()
    #showfps = font.render(f"SHOW FPS", True, (70, 70, 70))
    #window.blit(showfps, (180, 110))        
    
    button_back_settings.reset()
    button_back_settings.update()
    Backsettings = font.render(f"BACK", True, (70, 70, 70))
    window.blit(Backsettings, (760, 560))

    versia = font.render(VERSIA, True, (255, 255, 255))
    window.blit(versia, (950, 620))

    display.update()
    clock.tick(60)



    display.update()
    clock.tick(60)

komixlevel = 2
komixsex = 0

poletkomix = 0
tkm = 0
TIMErr = 59
t59 = 0
plusspr = 0
polet = 0

def komixrectx():
    komix.rect.x -=1200

def komixrecty():
    komix.rect.x +=1200
    komix.rect.y -=700

while komix_start:
    komix.reset()
    komix.update()
    skip.reset()
    skip.update()
    pygame.mixer.music.set_volume(0.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            komix_start = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Controler = True
                komix_start = False

    #if timekomix <= 6: 
    if komixsex == 300:
        if komixlevel >= 1:
            komixrectx()
            komixlevel -=2
            timekomix += 1
        else:
            komixrecty()
            komixlevel +=2
            timekomix += 1

    komixsex += 1
    if komixsex == 301:
            komixsex -= 301

    if timekomix == 4:
        t59 += 1
        if t59 == 60:
            t59 -= 60
            TIMErr -= 1
    
        score_text1x = Label(290,0,0,0,back)
        score_text1x.set_text("10:59:", 210, (250, 0, 0))
        score1x = Label(400,0,0,0,back)

        score1x.set_text(str(TIMErr), 210, (250, 0, 0))
        score1x.draw(330,290)
        score_text1x.draw(10,290)
    
    if plusspr <= 7:
        #spry += 0
        #sprx += 0
        plusspr -=10

    if timekomix == 7:
       sprite2.reset()
       sprite2.update()
       polet += 1
       if polet >= 150:
           sprite2.rect.y -=20

    if timekomix == 10:
        Controler = True
        komix_start = False
    
    fps = str(int(clock.get_fps()))
    fps_text = font.render(f"FPS: {fps}", True, (255, 255, 255))
    window.blit(fps_text, (10, 10))
    display.update()
    clock.tick(60)



text11 = 5
speed1 = 10
speed2 = 9
speed3 = 11
speed4 = 20
speed5 = 13
speed20 = 400
off = 0
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

class Player(GameSprite):
    def update(self):
        if startgame == True:
            if off <= 1:
                if POWER >= 1:
                    keys = key.get_pressed()
                    if keys[K_LEFT] and self.rect.x > 5:
                        self.rect.x -= speed5
                    if keys[K_RIGHT] and self.rect.x < 1200 - 150:
                        self.rect.x += speed2          
                    if keys[K_UP] and self.rect.y > 5:
                        self.rect.y -= speed2            
                    if keys[K_DOWN] and self.rect.y < 775 - 175:
                        self.rect.y += speed2    
                  

class GameEnemy(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()   
        self.image = transform.scale(image.load(player_image), (350, 200))
        self.speed = player_speed      
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
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
rocket1 = Player('rocket.png', -200, 0 - -325, 0)

class GameOverG(Gamesara):
    def update(self):
        if GAMEOVER == True:
            rocket1.rect.y -= 0

Power = GamePow('power.png', -200, 0 - -325, 0)

fonugru = GameFon('fon.png', 0, 50 - 50, 50)

rectx = 0

while Controler:
    fonugru.rect.x -= 10
    fonugru.reset()
    fonugru.update()
    controler.reset()
    controler.update()
    rocket1.reset()
    rocket1.update()
    skip.reset()
    skip.update()
    Power.reset()
    Power.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Controler = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mixer.music.stop()
                rectx += 3

    if rectx >= 1:
        rocket1.rect.x += 5

    if rocket1.rect.x >= 5:
        menumus.play(-1)
        startgame = True
        Controler = False

    font = pygame.font.SysFont("Arial", 60)
    fps = str(int(clock.get_fps()))
    fps_text = font.render(f"FPS: {fps}", True, (255, 255, 255))
    window.blit(fps_text, (10, 10))

    if fonugru.rect.x <= -1200:
        fonugru.rect.x += 1200
    
    display.update()
    clock.tick(60)

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

boss = GameEnemy('enemy.png', 1200, 0 - -275, 0)

shutcolor = Gamesara('sara.png', 0, 0 - -625, 0,)

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

alph = 0
gorect = 0
mus = False
BOSS = False
rrr = 0
e = 0
rectast = False
reast= 0
ydarboss = 4
spritee = pygame.image.load("black.jpg")
spritee = pygame.transform.scale(spritee2, (win_width,win_height))
while startgame:
    window.fill((0, 0, 0)) 
    fonugru.rect.x -= 13
    Power.rect.x -= speed3
    ast22.rect.x -= speed3
    ast33.rect.x -= speed3
    ast44.rect.x -= speed3
    ast55.rect.x -= speed3
    ast66.rect.x -= speed3
    ast77.rect.x -= speed3
    if BOSS == False:
        ast00.rect.x -= speed3
        ast11.rect.x -= speed3
        ast88.rect.x -= speed3
        ast99.rect.x -= speed3
    if rectast == True:
        ast00.rect.y -= 2000
        ast11.rect.y -= 2000
        ast88.rect.y -= 2000
        ast99.rect.y -= 2000
        rectast = False
    

    for event in pygame.event.get():
        if event.type == QUIT:
            startgame = False
        if event.type == pygame.KEYDOWN:
            #щит ракети за допомогою нього можна ламати сірі астероїди(проблема як зробити так щоб коли щит буде працювати то змінився спрайт ракети на 'щит'а коли закінчиться сам щит то змінеться на спрайт 'ракета)
            if event.key == pygame.K_e:
                if off <= 1:
                    if shon == 250:
                        if shan == 400:
                            shutcolor.rect.y += 200
                            shutnocolor.rect.y -= 200
                            shon -= 250
                            shan -= 400
                            shut -=2
                            ydarboss += 1
        if gamemode == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    POWER += 1
                if event.key == pygame.K_x:
                    POWER -= 1
                if event.key == pygame.K_1:
                    TIMEM += 1
                if event.key == pygame.K_2:
                    TIMEM -= 1
                if event.key == pygame.K_3:
                    TIME += 1
                if event.key == pygame.K_4:
                    TIME -= 1
    if POWER < 0:
        POWER += 1
    if POWER > 999:
        POWER -= 1

    if TIMEM < 0:
        TIMEM += 1
    if TIMEM > 9:
        TIMEM -= 1

    if TIME < 0:
        TIME += 1
    if TIME > 60:
        TIME -= 1

    if TIMEM == 3:
        BOSS = True
        reast += 2

    if reast == 2:
        rectast = True
        reast -= 3

    if BOSS == True:
        if boss.rect.x >= 1000:
            boss.rect.x -= 10
        if boss.rect.x <= 1000:
            direcrion = 'left'
            if boss.rect.y <= -100:
                direction = 'right'
            if boss.rect.y >= 600:
                direction = 'left'

            if direction == 'left':
                boss.rect.y -= 7
            else:
                boss.rect.y += 7

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

    if off <= 1:
        if Power.rect.x <= -700:
            reset_pipee(Power, pipe_positionss)

    if shut >= 4:
        if off <= 1:
            if ast66.rect.colliderect(rocket1.rect):
                GAMEOVER = True
    else: 
        if off <= 1:
            if ast66.rect.colliderect(rocket1.rect):
                reset_pipee(ast66, pipe_positionss)
                BAL += 150

    if shut >= 4:
        if off <= 1:
            if ast77.rect.colliderect(rocket1.rect):
                GAMEOVER = True
    else:
        if off <= 1:
            if ast77.rect.colliderect(rocket1.rect):
                reset_pipee(ast77, pipe_positionss)
                BAL += 150

    if shut >= 4:
        if off <= 1:
            if ast88.rect.colliderect(rocket1.rect):
                GAMEOVER = True
    else:
        if off <= 1:
            if ast88.rect.colliderect(rocket1.rect):
                reset_pipee(ast88, pipe_positionss)
                BAL += 150

    if shut >= 4:
        if off <= 1:
            if ast99.rect.colliderect(rocket1.rect):
                GAMEOVER = True
                mus = True
    else:
        if off <= 1:
            if ast99.rect.colliderect(rocket1.rect):
                reset_pipee(ast99, pipe_positionss)
                BAL += 150

    if off <= 1:
        if rocket1.rect.colliderect(Power.rect):
            Power.rect.x -= 1600
            POWER += 7
        
    if POWER < 1:
        GAMEOVER = True
        off += 3

    if off <= 1:
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
    
    if ydarboss == 5:
        off += 3
        alph += 3
        timeblack += 1

    if timeblack == 150:
        ydarboss -= ydarboss
        timeblack -= timeblack
        off -= off 
        menumus.stop()
        finalmus.play()
        final = True
        reast += 1
        alph -= alph
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
    boss.update()


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
    boss.reset()

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

    alph = max(0, min(255, alph))
    spritee.set_alpha(alph)
    window.blit(spritee, (0, 0))

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


shake_intensity = 2  
shake_duration = 300 
shake_timer = shake_duration
Bsruv = 2
rect_ran = -3
rect__ran = 3
def quit_game():
    global QUIT,logo,startgame,menugame,menusettings,Controler,final,gamemode,gamemodefon,gamestart,gamemenufon,opensettings,openmenu,showfps_off_on,komix_start
    logo = False
    clickbutton.play()
    menugame = False
    menusettings = False
    komix_start = False
    Controler = False
    startgame = False
    final = False
    gamemode = False
    gamemodefon = False
    gamestart = False
    gamemenufon = True
    opensettings = False
    openmenu = False
    showfps_off_on = True
while final:
    #sprite_image = pygame.image.load('enemy.png') 
    #sprite_image = pygame.transform.scale(sprite_image, (350, 200)) 
    #sprite_rect = sprite_image.get_rect(center=(1100,360))
    #komixfinal = pygame.image.load('Bsruv.png') 
    #komixfinal = pygame.transform.scale(komixfinal, (10, 70)) 
    #komixfinalrect = komixfinal.get_rect(center=(0,0))
    rocket1 = Player('rocket.png', 300, 0 - -325, 0)
    fonugru.rect.x -= 10
    for event in pygame.event.get():
        if event.type == QUIT:
            #quit_game()
            fonugru.rect.x += 111

    fonugru.update()
    rocket1.update()


    fonugru.reset()
    rocket1.reset()
  

    if fonugru.rect.x <= -1200:
        fonugru.rect.x += 1200
    
    #offset_x = random.randint(rect_ran, rect__ran)
    #offset_y = random.randint(rect_ran, rect__ran)

    #window.blit(sprite_image, (sprite_rect.x + offset_x, sprite_rect.y + offset_y))


    #if Bsruv >= 1:
    #    Bsruv += 1

    #if Bsruv == 200:
    #    rect__ran += 3
    #    rect_ran += -3
        

    display.update()
    clock.tick(60)

def quit_game():
    global QUIT,logo,startgame,menugame,menusettings,Controler,final,gamemode,gamemodefon,gamestart,gamemenufon,opensettings,openmenu,showfps_off_on,komix_start
    logo = False
    clickbutton.play()
    menugame = False
    menusettings = False
    komix_start = False
    Controler = False
    startgame = False
    final = False
    gamemode = False
    gamemodefon = False
    gamestart = False
    gamemenufon = True
    opensettings = False
    openmenu = False
    showfps_off_on = True