import pygame
import sys

# Ініціалізація pygame
pygame.init()

# Розміри вікна
WIDTH, HEIGHT = 900, 700

# Створення вікна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гра: Рухомий фон і обертання спрайта")

# Завантаження фону
background_image = pygame.image.load('final.png')
background_rect1 = background_image.get_rect(topleft=(0, 0))  # Перший фон
background_rect2 = background_image.get_rect(topleft=(0, -HEIGHT))  # Другий фон над першим

# Завантаження спрайта
sprite_image = pygame.image.load("ast.png")
sprite_image = pygame.transform.scale(sprite_image, (150, 150))  # Масштабування до 150x150
sprite_rect = sprite_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Центр спрайта

# Швидкість руху фону
background_speed = 10

# Початковий кут повороту
rotation_angle = 0
rotation_speed = 8  # Швидкість обертання

# Основний цикл гри
clock = pygame.time.Clock()
running = True

while running:
    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Рух фону
    background_rect1.y += background_speed
    background_rect2.y += background_speed

    # Переміщення фону, якщо він виходить за межі
    if background_rect1.top >= HEIGHT:
        background_rect1.y = background_rect2.y - HEIGHT
    if background_rect2.top >= HEIGHT:
        background_rect2.y = background_rect1.y - HEIGHT

    # Обертання спрайта
    rotation_angle += rotation_speed  # Поворот проти годинникової стрілки
    rotated_image = pygame.transform.rotate(sprite_image, rotation_angle)
    rotated_rect = rotated_image.get_rect(center=sprite_rect.center)

    # Оновлення екрана
    screen.fill((0, 0, 0))  # Очистка екрана (чорний фон)
    screen.blit(background_image, background_rect1)  # Відображення першого фону
    screen.blit(background_image, background_rect2)  # Відображення другого фону
    screen.blit(rotated_image, rotated_rect)  # Відображення повернутого спрайта
    pygame.display.flip()

    # Затримка для 60 кадрів на секунду
    clock.tick(60)

# Завершення роботи
pygame.quit()
sys.exit()
