import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Crear la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FIREBALL")

# Fuentes
font = pygame.font.SysFont(None, 40)
big_font = pygame.font.SysFont(None, 80)

# Variables globales
player_name = ""

# Grupos de sprites
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy_ships = pygame.sprite.Group()

# Clase para la nave del jugador
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 5

    def shoot(self):
        bullet = Fireball(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

# Clase para las balas con fuego (puntos amarillos)
class Fireball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 10], pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (5, 5), 5)  # Hacer que las balas sean puntos amarillos
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y -= 10  # Aumentar la velocidad de las balas
        if self.rect.bottom < 0:
            self.kill()

# Clase para las naves enemigas
class EnemyShip(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y += 4  # Aumentar la velocidad de las naves enemigas
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)

# Función para pedir el nombre del jugador
def get_player_info():
    global player_name
    input_box = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, 300, 40)
    input_active = False
    text = ''
    clock = pygame.time.Clock()

    # Bucle para la interfaz
    while True:
        screen.fill(WHITE)  # Fondo blanco para la interfaz
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False

            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        player_name = text  # Guardar el nombre ingresado
                        return  # Salir de la función, ya que el jugador ha ingresado su nombre
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        
        # Dibuja el cuadro de texto
        pygame.draw.rect(screen, BLACK, input_box, 2)
        txt_surface = font.render(text, True, BLACK)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        
        # Mostrar el título y la instrucción
        welcome_text = big_font.render("¡BIENVENIDO AL FIRE!", True, RED)  # Con signos de exclamación
        screen.blit(welcome_text, (SCREEN_WIDTH // 2 - welcome_text.get_width() // 2, 50))  # Más arriba
        
        instruction_text = font.render("COLOCA TU NOMBRE", True, BLACK)
        screen.blit(instruction_text, (SCREEN_WIDTH // 2 - instruction_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))

        pygame.display.flip()
        clock.tick(30)

# Función para mostrar el menú de "GAME OVER" con opciones
def game_over():
    running = True
    while running:
        screen.fill(WHITE)
        game_over_text = big_font.render("GAME OVER", True, RED)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))

        retry_text = font.render("Reintentar (Presiona R)", True, BLACK)
        exit_text = font.render("Salir (Presiona S)", True, BLACK)

        screen.blit(retry_text, (SCREEN_WIDTH // 2 - retry_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(exit_text, (SCREEN_WIDTH // 2 - exit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 40))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Reintentar
                if event.key == pygame.K_s:
                    pygame.quit()
                    sys.exit()

# Función principal para el juego
def game_loop():
    global player_name
    get_player_info()  # Obtener el nombre del jugador

    # Limpiar los grupos de sprites antes de reiniciar
    all_sprites.empty()
    enemy_ships.empty()
    bullets.empty()

    # Crear la nave del jugador
    ship = Ship()
    all_sprites.add(ship)

    # Crear naves enemigas iniciales
    for _ in range(5):
        color = random.choice([BLUE, GREEN])
        x = random.randint(0, SCREEN_WIDTH - 50)
        y = random.randint(-100, -50)
        enemy_ship = EnemyShip(color, x, y)
        all_sprites.add(enemy_ship)
        enemy_ships.add(enemy_ship)

    # Bucle del juego de las naves
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Crear naves enemigas cada cierto tiempo
        if len(enemy_ships) < 10:  # Asegura que siempre haya al menos 10 naves enemigas
            color = random.choice([BLUE, GREEN])
            x = random.randint(0, SCREEN_WIDTH - 50)
            y = random.randint(-100, -50)
            enemy_ship = EnemyShip(color, x, y)
            all_sprites.add(enemy_ship)
            enemy_ships.add(enemy_ship)

        # Actualizar y dibujar los sprites
        all_sprites.update()
        screen.fill(WHITE)  # Fondo blanco para el juego
        all_sprites.draw(screen)

        # Detectar teclas para disparar
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            ship.shoot()

        # Verificar colisiones entre balas y naves enemigas
        for bullet in bullets:
            enemy_hits = pygame.sprite.spritecollide(bullet, enemy_ships, True)  # Detectar colisiones con naves enemigas
            for hit in enemy_hits:
                bullet.kill()  # Eliminar la bala al impactar
                # Aquí puedes agregar puntos o efectos para cuando una nave enemiga es destruida

        # Verificar si la nave del jugador es tocada por una nave enemiga
        if pygame.sprite.spritecollideany(ship, enemy_ships):
            if game_over():  # Mostrar pantalla de Game Over y reintentar
                game_loop()  # Volver a iniciar el juego

        pygame.display.flip()
        pygame.time.Clock().tick(60)  # FPS fijo

# Iniciar el juego
if __name__ == "__main__":
    game_loop()






