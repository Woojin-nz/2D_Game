import pygame, sys
from pygame.locals import *

pygame.init()

SIZE = WIDTH, HEIGHT = 1920, 1080
FPS = 60
FramePerSec = pygame.time.Clock()
pygame.display.set_caption("2D Shooter")
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode(SIZE)
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Press "SPACE" to restart', True, YELLOW, RED)
textRect = text.get_rect()
textRect.center = (WIDTH // 2, HEIGHT // 2)


class Hunter(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Hunter, self).__init__()

        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)
        self.speed = 2

    def hunt_player(self, player):
        player_position = player.rect.topleft
        direction = player_position - self.position
        velocity = direction.normalize() * self.speed

        self.position += velocity
        self.rect.topleft = self.position

    def update(self, player):
        self.hunt_player(player)


class Player(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Player, self).__init__()

        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect(center=screen_rect.center)

        self.position = pygame.math.Vector2(position)
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = 3

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < 1080:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 1920:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


player = Player(position=(350, 220))
monster = Hunter(position=(680, 400))

enemies = pygame.sprite.Group()
enemies.add(monster)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(monster)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False

    player.update()
    monster.update(player)

    screen.fill(WHITE)
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        screen.fill(RED)
        screen.blit(text, textRect)
        print("ded")
        for entity in all_sprites:
            entity.kill()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        screen.fill(WHITE)
                        for entity in all_sprites:
                            entity.alive()

            pygame.display.update()

    pygame.display.update()
    FramePerSec.tick(FPS)
