import pygame, sys
from pygame.locals import *
import threading

pygame.init()

SIZE = WIDTH, HEIGHT = 1280,1000
FPS = 60
FramePerSec = pygame.time.Clock()
pygame.display.set_caption("2D Shooter")
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
TRANSPARENT = (0,0,0,0)
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


    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < 1000:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 1280:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class right_Bullet(pygame.sprite.Sprite):

    def __init__(self,position):
        super(right_Bullet, self).__init__()

        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect(center = position)


    def update(self):
        self.rect.move_ip(5,0)
        if self.rect.right >= 1280:
            self.kill()

class left_Bullet(pygame.sprite.Sprite):

    def __init__(self,position):
        super(left_Bullet, self).__init__()

        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect(center = position)


    def update(self):
        self.rect.move_ip(-5,0)
        if self.rect.left <= 0:
            self.kill()



player = Player(position=(350, 220))
monster = Hunter(position=(500, 200))
bullet_pos = player.rect.center
bullet_right = right_Bullet(bullet_pos)
bullet_left = left_Bullet(bullet_pos)


enemies = pygame.sprite.Group()
enemies.add(monster)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(monster)
all_sprites.add(bullet_right)
all_sprites.add(bullet_left)

running = True
while running:
    clock.tick(FPS)
    level = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False



    player.update()
    monster.update(player)
    bullet_right.update()
    bullet_left.update()

    screen.fill(WHITE)
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    text_level = font.render('Level {}'.format(level), True, BLACK, WHITE)
    text_level_rec = text_level.get_rect()
    text_level_rec.center = (1080,900)
    screen.blit(text_level,text_level_rec)


    if pygame.sprite.spritecollideany(player, enemies):
        screen.fill(RED)
        screen.blit(text, textRect)
        print("ded")
        for entity in all_sprites:
            entity.kill()

        space_loop = ""

        while space_loop == "":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        screen.fill(WHITE)
                        player = Player(position=(100, 220))
                        monster = Hunter(position=(200,200))
                        bullet_pos = player.rect.center
                        bullet_right = right_Bullet(bullet_pos)
                        bullet_left = left_Bullet(bullet_pos)
                        enemies.add(monster)
                        all_sprites.add(player)
                        all_sprites.add(monster)
                        all_sprites.add(bullet_right)
                        all_sprites.add(bullet_left)
                        space_loop = "a"

            pygame.display.update()

    pygame.display.update()
    FramePerSec.tick(FPS)
