import pygame
import random
import time

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
width, height = 600, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Тремтячий спрайт")

# Завантаження основного спрайту
sprite_image = pygame.image.load('ast.png')  # Основний спрайт (масштабований до 350x200)
sprite_image = pygame.transform.scale(sprite_image, (350, 200))

# Завантаження спрайту для маленьких копій
small_sprite_image = pygame.image.load('astg.png')  # Заміна на 'fire.png' для малих спрайтів
small_sprite_image = pygame.transform.scale(small_sprite_image, (50, 50))  # Масштабування до 50x50

# Прямокутники для спрайтів
sprite_rect = sprite_image.get_rect(center=(width // 2, height // 2))
small_sprites = []

# Час для телепортації малих спрайтів
last_teleport_time = time.time()
teleport_interval = 0.5  # Телепортація кожні 0.5 секунд

# Головний цикл гри
running = True
clock = pygame.time.Clock()

# Логіка телепортації для кожного малого спрайту
last_teleport_times = []  # Список для зберігання часу останньої телепортації для кожного спрайту
teleport_delays = []  # Список для зберігання затримки між телепортаціями для кожного спрайту

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заповнення екрану
    window.fill((255, 255, 255))

    # Тремтіння основного спрайту
    offset_x = random.randint(-2, 2)
    offset_y = random.randint(-2, 2)

    # Малюємо основний спрайт на екрані
    window.blit(sprite_image, (sprite_rect.x + offset_x, sprite_rect.y + offset_y))

    # Оновлюємо список малих спрайтів кожні 0.5 секунди
    if time.time() - last_teleport_time >= teleport_interval:
        num_small_sprites = random.randint(5, 9)  # Від 5 до 9 малих спрайтів
        small_sprites.clear()  # Очищаємо старі спрайти

        # Створюємо нові малі спрайти
        for _ in range(num_small_sprites):
            # Випадкові затримки для кожного малого спрайту
            delay = random.uniform(0.1, 0.4)
            teleport_delays.append(delay)
            last_teleport_times.append(time.time())  # Час першої телепортації

            # Початкове випадкове розташування малих спрайтів біля основного спрайту
            offset_x = random.randint(-100, 100)
            offset_y = random.randint(-100, 100)
            small_sprite_rect = small_sprite_image.get_rect(center=(sprite_rect.centerx + offset_x, sprite_rect.centery + offset_y))
            small_sprites.append(small_sprite_rect)

        last_teleport_time = time.time()  # Оновлюємо час для наступної групової телепортації

    # Телепортуємо малі спрайти в різний час
    for i, small_sprite_rect in enumerate(small_sprites):
        if time.time() - last_teleport_times[i] >= teleport_delays[i]:
            # Телепортуємо спрайт на випадкове місце
            offset_x = random.randint(-100, 100)
            offset_y = random.randint(-100, 100)
            small_sprite_rect.center = (sprite_rect.centerx + offset_x, sprite_rect.centery + offset_y)

            # Оновлюємо час телепортації
            last_teleport_times[i] = time.time()

        # Малюємо малий спрайт поверх основного
        window.blit(small_sprite_image, small_sprite_rect)

    # Оновлення екрану
    pygame.display.update()
    clock.tick(60)

pygame.quit()
