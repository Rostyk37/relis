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

win_width = 1200
win_height = 700
rect_width, rect_height = 570, 87

menugame = False
gamestart = False
gamemenufon = True

opensettings = True
openmenu = False

showfps_off_on = True

img_enemy = 'ast.png'

speed5 = 13
speed2 = 9

BLACK = (0, 0, 0)

pygame.display.set_caption('Alien Invasion')

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

#button_start = Button('button.png', 50, 100,)
#button_settings = Button('button.png', 50, 250,)
#button_ShowScores = Button('button.png', 50, 400,)
#button_quit = Button('button.png', 50, 550,)

button_start = Button('button.png', 50, 100,)
button_settings = Button('button.png', 50, 250,)
button_ShowScores = Button('button.png', 50, 400,)
button_quit = Button('button.png', 50, 550,)

show_fps = Button('button.png', 50, 100,)

ready_button = Button('readybutton.png', 0, 0,)

def handle_button_click(button_rect, action):
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        action()

def start_game():
    go_start_game.play()
    print("Start Game")

def open_settings():
    global open_menu,opensettings
    clickbutton.play()
    open_menu = True
    opensettings = False
    print("Open Settings")

def show_scores():
    clickbutton.play()
    print("Show Scores")


def quit_game():
    clickbutton.play()
    global menugame
    print("Quit Game")
    menugame = True

def menufon():   
    sprite1.rect.x +=10

def show__fps():
    print("show fps")

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
while not menugame:
    fon.rect.x -= 3
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menugame = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            if not openmenu:
                handle_button_click(button_start.rect, start_game)
                handle_button_click(button_settings.rect, open_settings)
                handle_button_click(button_ShowScores.rect, show_scores)
                handle_button_click(button_quit.rect, quit_game)
            if not opensettings:
                handle_button_click(button_settings.rect, show__fps)

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
    
    if not openmenu:
        button_start.reset()
        button_start.update()
        newgame = font.render(f"NEW GAME", True, (70, 70, 70))
        window.blit(newgame , (180, 110))

        button_settings.reset()
        button_settings.update()
        settings = font.render(f"SETTINGS", True, (70, 70, 70))
        window.blit(settings, (190, 260))

        button_ShowScores.reset()
        button_ShowScores.update()
        showscore = font.render(f"SHOWSCORE", True, (70, 70, 70))
        window.blit(showscore, (160, 410))
    
        button_quit.reset()
        button_quit.update()
        quot = font.render(f"QUOT", True, (70, 70, 70))
        window.blit(quot, (250, 560))

    if not opensettings:
        show_fps.reset()
        show_fps.update()
        showfps = font.render(f"SHOW FPS", True, (70, 70, 70))
        window.blit(showfps, (180, 110))        
    
    versia = font.render(f"версія 2.0", True, (255, 255, 255))
    window.blit(versia, (950, 620))

    
    display.update()
    clock.tick(60)
