from pygame import *
from random import randint, choice
import time
import sys
import pygame

window = display.set_mode((1200, 700))
display.set_caption('galaxy')
clock = pygame.time.Clock()

pygame.init()
mixer.init()
mixer.music.load('mus_menu (2).ogg')
pygame.mixer.music.set_volume(0.3)
mixer.music.play(-1)
clickbutton = mixer.Sound('BX0D.mp3')
#clickbutton = mixer.music.set_volume(0.1)
back = mixer.Sound('EXIT.mp3')
go_start_game = mixer.Sound('go_start_game.mp3')
VERSIA = 'версія2.1'

win_width = 1200
win_height = 700
rect_width, rect_height = 570, 87

menugame = True
menusettings = False
komix_start = False

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

pygame.display.set_caption('Alien Invasion')

class Komix(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (2500,4700))
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
        self.image = transform.scale(image.load(player_image), (2400, 700))
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
        self.image = transform.scale(image.load(player_image), (144, 100))
        self.speed = player_speed
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

class Enemy(Sprite):
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < -1500:
            self.rect.x += 2700
            self.rect.y = randint(10, 700 - 70)

fon = Fon ('menufon.png', 0, 0, 0)

sprite1 = GameSprite('rocket.png', 0, 325, 0)

text = Text('nametext.png', 650, 100,0)

komix = Komix('komix.png', 0, 0,0)
button_start = Button('button.png', 50, 100,)
button_settings = Button('button.png', 50, 250,)
button_ShowScores = Button('button.png', 50, 400,)
button_quit = Button('button.png', 50, 550,)

buttonshow_fps = Button('button.png', 50, 100,)

button_back_showfps = Button('button.png', 550, 550,)

ready_button = Button('readybutton.png', 0, 0,)

def handle_button_click(button_rect, action):
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        action()

def start_game():
    global komix_start,menugame
    go_start_game.play()
    komix_start = True
    menugame = False
    print("Start Game")

def open_settings():
    global menugame,menusettings
    clickbutton.play()
    print("Open Settings")
    menusettings = True
    menugame = False

def show_scores():
    clickbutton.play()
    print("Show Scores")

def quit_game():
    clickbutton.play()
    global menugame,menusettings
    print("Quit Game")
    menugame = False
    menusettings = False

def menufon():   
    sprite1.rect.x +=10

def show__fps():
    clickbutton.play()
    print("show fps")

#def back_settings():
#    clickbutton.play()
#    global menusettings,menugame
#    menugame = True
    #menusettings = False
#    print("back settings")

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
        50, win_width - 1150), 300, 120, 120, randint(5, 15))
    asts.add(ast)

font = pygame.font.SysFont("Arial", 18)
while menugame:
    fon.rect.x -= 3
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
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
    window.blit(newgame , (200, 110))

    button_settings.reset()
    button_settings.update()
    settings = font.render(f"НЕ РОБОЧЕ", True, (70, 70, 70))
    window.blit(settings, (190, 260))

    button_ShowScores.reset()
    button_ShowScores.update()
    showscore = font.render(f"SHOWSCORE", True, (70, 70, 70))
    window.blit(showscore, (160, 410))
    
    button_quit.reset()
    button_quit.update()
    quot = font.render(f"QUOT", True, (70, 70, 70))
    window.blit(quot, (250, 560))       
    
    versia = font.render(VERSIA, True, (255, 255, 255))
    window.blit(versia, (950, 620))

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
                #handle_button_click(button_back_showfps.rect, back_settings)

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
    
    buttonshow_fps.reset()
    buttonshow_fps.update()
    showfps = font.render(f"SHOW FPS", True, (70, 70, 70))
    window.blit(showfps, (180, 110))        
    
    button_back_showfps.reset()
    button_back_showfps.update()
    Backsettings = font.render(f"BACK", True, (70, 70, 70))
    window.blit(Backsettings, (760, 560))

    versia = font.render(VERSIA, True, (255, 255, 255))
    window.blit(versia, (950, 620))

    display.update()
    clock.tick(60)
a = False
komixlevel = 1
t1 = 1
t2 = 2
t3 = 3
t4 = 4
t5 = 5
t6 = 6
t7 = 7
t8 = 8
t9 = 9
t10 = 10
t11 = 11
t12 = 12
t13 = 13
t14 = 14
timekomix = 0


while komix_start:
    komix.reset()
    komix.update()
    timekomix += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            komix_start = False
        if komixlevel == t1:
            t1 += 100
            komix.rect.x += 1300
        if komixlevel == t2:
            t2 += 100
            komix.rect.x -= 1300
            komix.rect.y -= 750
        if komixlevel == t3:
            t3 += 100
            komix.rect.x += 1300
        if komixlevel == t4:
            t4 += 100
            komix.rect.x -= 1300
            komix.rect.y -= 750
        if komixlevel == t5:
            t5 += 100
            komix.rect.x += 1300
        if komixlevel == t6:
            t6 += 100
            komix.rect.x -= 1300
            komix.rect.y -= 750
        if komixlevel == t7:
            t7 += 100
            komix.rect.x += 1300
        if komixlevel == t8:
            t8 += 100
            komix.rect.x -= 1300
            komix.rect.y -= 750
        if komixlevel == t9:
            t9 += 100
            komix.rect.x += 1300
        if komixlevel == t10:
            t10 += 100
            komix.rect.x -= 1300
            komix.rect.y -= 750
        if komixlevel == t11:
            t11 += 100
            komix.rect.x += 1300
        if komixlevel == t12:
            t12 += 100
            komix.rect.x -= 1300
            komix.rect.y -= 750
        if komixlevel == t13:
            t13 += 100
            komix.rect.x += 1300
        if komixlevel == t14:
            t14 += 100
            komix.rect.x -= 1300
            komix.rect.y -= 750
                  
        if timekomix == 300:
            timekomix -= 300
            komixlevel += 1
        
    display.update()
    clock.tick(60)