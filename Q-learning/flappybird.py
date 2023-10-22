import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Crear la ventana
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Clase para el pájaro
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (100, SCREEN_HEIGHT // 2)
        self.velocity = 0

    def update(self):
        self.velocity += 1
        self.rect.move_ip(0, self.velocity)

# Grupos de sprites
all_sprites = pygame.sprite.Group()
birds = pygame.sprite.Group()

# Crear el pájaro
bird = Bird()
all_sprites.add(bird)
birds.add(bird)

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

running = True
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.velocity = -10

    # Colisión con el suelo
    if bird.rect.bottom >= SCREEN_HEIGHT:
        running = False

    # Actualizar
    all_sprites.update()

    # Dibujar
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(30)

# Fin del juego
pygame.quit()
sys.exit()

