import pygame

# Ініціалізація Pygame
pygame.init()

# Налаштування вікна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Прямокутники та мишка")

# Клас для спрайтів прямокутників
class RectSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, default_image_path, highlight_image_path):
        super().__init__()
        self.default_image = pygame.image.load(default_image_path).convert_alpha()
        self.highlight_image = pygame.image.load(highlight_image_path).convert_alpha()
        self.image = self.default_image
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.image = self.highlight_image
        else:
            self.image = self.default_image

# Створення спрайтів прямокутників
rect_sprites = pygame.sprite.Group(
    RectSprite((WIDTH - 570) // 2, 50, 'button.png', 'readybutton.png'),
    RectSprite((WIDTH - 570) // 2, 150, 'button.png', 'readybutton.png'),
    RectSprite((WIDTH - 570) // 2, 250, 'button.png', 'readybutton.png'),
    RectSprite((WIDTH - 570) // 2, 350, 'button.png', 'readybutton.png')
)

# Основний цикл програми
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отримуємо позицію мишки
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Оновлення спрайтів
    rect_sprites.update((mouse_x, mouse_y))

    # Малювання на екрані
    screen.fill((0, 0, 0))  # Заливка фону чорним кольором

    # Малюємо спрайти прямокутників
    rect_sprites.draw(screen)

    # Оновлення екрану
    pygame.display.flip()

# Завершення роботи Pygame
pygame.quit()
