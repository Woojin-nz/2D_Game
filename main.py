import pygame, sys, contextlib, os
from pygame.locals import *
from pygame import mixer

pygame.init()

SIZE = WIDTH, HEIGHT = 1280, 1000
FPS = 60
FramePerSec = pygame.time.Clock()
pygame.display.set_caption("2D Shooter")
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRANSPARENT = (0, 0, 0, 0)
screen = pygame.display.set_mode(SIZE)
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 60)
text = font.render('Press "SPACE" to restart', True, YELLOW, RED)
vic = font.render("CONGRATULATIONS!!", True, YELLOW, RED)
textRect = text.get_rect()
textRect.center = (WIDTH // 2, HEIGHT // 2)
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


asset_url = resource_path('assets/icon.png')
icon_asset = pygame.image.load(asset_url)

asset_url1 = resource_path('assets/enemy.png')
hero_asset1 = pygame.image.load(asset_url1)

asset_url2 = resource_path('assets/bullet.png')
hero_asset2 = pygame.image.load(asset_url2)

asset_url3 = resource_path('assets/Player.png')
hero_asset3 = pygame.image.load(asset_url3)

pew = pygame.mixer.Sound("assets/gun.mp3")
bug_death = pygame.mixer.Sound("assets/bug.mp3")
congrat = pygame.mixer.Sound("assets/congratz.mp3")
death = pygame.mixer.Sound("assets/death.mp3")
defeat = pygame.mixer.Sound("assets/defeat.mp3")
mixer.init

mixer.music.load("assets/background.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.025)

with contextlib.redirect_stdout(None):
    import pygame


class Hunter(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Hunter, self).__init__()

        self.image = pygame.image.load("assets/enemy.png")
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

        self.image = pygame.image.load("assets/Player.png")
        self.rect = self.image.get_rect(center=screen_rect.center)

        self.position = pygame.math.Vector2(position)
        self.velocity = pygame.math.Vector2(0, 0)

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

    def __init__(self, position):
        super(right_Bullet, self).__init__()

        self.image = pygame.image.load("assets/bullet.png")
        self.rect = self.image.get_rect(center=position)

    def update(self):
        self.rect.move_ip(5, 0)
        if self.rect.right >= 1280:
            self.kill()


class left_Bullet(pygame.sprite.Sprite):

    def __init__(self, position):
        super(left_Bullet, self).__init__()

        self.image = pygame.image.load("assets/bullet.png")
        self.rect = self.image.get_rect(center=position)

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.left <= 0:
            self.kill()


player = Player(position=(350, 220))
monster = Hunter(position=(0, 0))
monster1 = Hunter(position=(1280, 1000))
monster2 = Hunter(position=(1280, 0))
monster3 = Hunter(position=(0, 1000))
monster4 = Hunter(position=(0, 100))
monster5 = Hunter(position=(0, 200))
monster6 = Hunter(position=(0, 300))
monster7 = Hunter(position=(0, 400))
monster8 = Hunter(position=(0, 500))
monster9 = Hunter(position=(0, 600))
monster10 = Hunter(position=(0, 700))
monster11 = Hunter(position=(0, 800))
monster12 = Hunter(position=(0, 900))
monster13 = Hunter(position=(100, 0))
monster14 = Hunter(position=(100, 0))
monster15 = Hunter(position=(200, 0))
monster16 = Hunter(position=(300, 0))
monster17 = Hunter(position=(400, 0))
monster18 = Hunter(position=(500, 0))
monster19 = Hunter(position=(600, 0))
monster20 = Hunter(position=(700, 0))
monster21 = Hunter(position=(800, 0))
monster22 = Hunter(position=(900, 0))
monster23 = Hunter(position=(1000, 0))
monster24 = Hunter(position=(1100, 0))
monster25 = Hunter(position=(1200, 0))

monster26 = Hunter(position=(1280, 0))
monster27 = Hunter(position=(1280, 100))
monster28 = Hunter(position=(1280, 200))
monster29 = Hunter(position=(1280, 300))
monster30 = Hunter(position=(1280, 400))
monster31 = Hunter(position=(1280, 500))
monster32 = Hunter(position=(1280, 600))
monster33 = Hunter(position=(1280, 700))
monster34 = Hunter(position=(1280, 800))
monster35 = Hunter(position=(1280, 900))
monster36 = Hunter(position=(1280, 1000))

monster37 = Hunter(position=(200, 1000))
monster38 = Hunter(position=(400, 1000))
monster39 = Hunter(position=(600, 1000))
monster40 = Hunter(position=(800, 1000))
# monster41 = Hunter(position=(1000, 1000))
monster42 = Hunter(position=(1200, 1000))

bullet_pos = player.rect.center
bullet_right = right_Bullet(bullet_pos)
bullet_left = left_Bullet(bullet_pos)

pygame.mixer.Sound.play(pew)

bullet = pygame.sprite.Group()
bullet.add(bullet_right)
bullet.add(bullet_left)

enemies = pygame.sprite.Group()
enemies.add(monster)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(monster)
all_sprites.add(bullet_right)
all_sprites.add(bullet_left)

running = True

my_event_id = pygame.USEREVENT + 1
pygame.time.set_timer(my_event_id, 1001)
global level
level = 1
global number_of_enemy
number_of_enemy = len(enemies)
global a
a = 1
global respawn_level
respawn_level = 0
global end
end = "a"
while running:
    clock.tick(FPS)
    victory = 0

    last = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False
        elif event.type == my_event_id:
            for entity in bullet:
                entity.kill()

            pygame.mixer.Sound.play(pew)

            bullet_pos = player.rect.center
            bullet_right = right_Bullet(bullet_pos)
            bullet_left = left_Bullet(bullet_pos)
            all_sprites.add(bullet_right)
            all_sprites.add(bullet_left)
            bullet.add(bullet_right)
            bullet.add(bullet_left)

    player.update()
    enemies.update(player)

    bullet_right.update()
    bullet_left.update()

    screen.fill(WHITE)

    if level == 2 and a == 1 and respawn_level == 0:
        monster = Hunter(position=(0, 0))
        monster1 = Hunter(position=(1280, 1000))
        all_sprites.add(monster)
        all_sprites.add(monster1)
        enemies.add(monster)
        enemies.add(monster1)
        number_of_enemy = len(enemies)
        a += 1

    if level == 3 and a == 2 and respawn_level == 0:
        monster = Hunter(position=(0, 0))
        monster1 = Hunter(position=(1280, 1000))
        monster2 = Hunter(position=(1280, 0))
        all_sprites.add(monster)
        all_sprites.add(monster1)
        all_sprites.add(monster2)
        enemies.add(monster)
        enemies.add(monster1)
        enemies.add(monster2)
        number_of_enemy = len(enemies)
        a += 1

    if level == 4 and a == 3 and respawn_level == 0:
        monster = Hunter(position=(0, 0))
        monster1 = Hunter(position=(1280, 1000))
        monster2 = Hunter(position=(1280, 0))
        monster3 = Hunter(position=(0, 1000))
        all_sprites.add(monster)
        all_sprites.add(monster1)
        all_sprites.add(monster2)
        all_sprites.add(monster3)
        enemies.add(monster)
        enemies.add(monster1)
        enemies.add(monster2)
        enemies.add(monster3)
        number_of_enemy = len(enemies)
        a += 1

    if level == 5 and a == 4 and respawn_level == 0:
        monster = Hunter(position=(0, 0))
        monster1 = Hunter(position=(1280, 1000))
        monster2 = Hunter(position=(1280, 0))
        monster3 = Hunter(position=(0, 1000))
        monster4 = Hunter(position=(0, 100))
        monster5 = Hunter(position=(0, 200))
        monster6 = Hunter(position=(0, 300))
        monster7 = Hunter(position=(0, 400))
        monster8 = Hunter(position=(0, 500))
        monster9 = Hunter(position=(0, 600))
        monster10 = Hunter(position=(0, 700))
        monster11 = Hunter(position=(0, 800))
        monster12 = Hunter(position=(0, 900))
        monster13 = Hunter(position=(100, 0))
        monster14 = Hunter(position=(100, 0))
        monster15 = Hunter(position=(200, 0))
        monster16 = Hunter(position=(300, 0))
        monster17 = Hunter(position=(400, 0))
        monster18 = Hunter(position=(500, 0))
        monster19 = Hunter(position=(600, 0))
        monster20 = Hunter(position=(700, 0))
        monster21 = Hunter(position=(800, 0))
        monster22 = Hunter(position=(900, 0))
        monster23 = Hunter(position=(1000, 0))
        monster24 = Hunter(position=(1100, 0))
        monster25 = Hunter(position=(1200, 0))

        monster26 = Hunter(position=(1280, 0))
        monster27 = Hunter(position=(1280, 100))
        monster28 = Hunter(position=(1280, 200))
        monster29 = Hunter(position=(1280, 300))
        monster30 = Hunter(position=(1280, 400))
        monster31 = Hunter(position=(1280, 500))
        monster32 = Hunter(position=(1280, 600))
        monster33 = Hunter(position=(1280, 700))
        monster34 = Hunter(position=(1280, 800))
        monster35 = Hunter(position=(1280, 900))
        monster36 = Hunter(position=(1280, 1000))

        monster37 = Hunter(position=(200, 1000))
        monster38 = Hunter(position=(400, 1000))
        monster39 = Hunter(position=(600, 1000))
        monster40 = Hunter(position=(800, 1000))
        # monster41 = Hunter(position=(1000, 1000))
        monster42 = Hunter(position=(1200, 1000))

        all_sprites.add(monster)
        all_sprites.add(monster1)
        all_sprites.add(monster2)
        all_sprites.add(monster3)
        all_sprites.add(monster4)
        all_sprites.add(monster5)
        all_sprites.add(monster6)
        all_sprites.add(monster7)
        all_sprites.add(monster8)
        all_sprites.add(monster9)
        all_sprites.add(monster10)
        all_sprites.add(monster11)
        all_sprites.add(monster12)
        all_sprites.add(monster13)
        all_sprites.add(monster14)
        all_sprites.add(monster15)
        all_sprites.add(monster16)
        all_sprites.add(monster17)
        all_sprites.add(monster18)
        all_sprites.add(monster19)
        all_sprites.add(monster20)
        all_sprites.add(monster21)
        all_sprites.add(monster22)
        all_sprites.add(monster23)
        all_sprites.add(monster24)
        all_sprites.add(monster25)
        all_sprites.add(monster26)
        all_sprites.add(monster27)
        all_sprites.add(monster28)
        all_sprites.add(monster29)
        all_sprites.add(monster30)
        all_sprites.add(monster31)
        all_sprites.add(monster32)
        all_sprites.add(monster33)
        all_sprites.add(monster34)
        all_sprites.add(monster35)
        all_sprites.add(monster36)
        all_sprites.add(monster37)
        all_sprites.add(monster38)
        all_sprites.add(monster39)
        all_sprites.add(monster40)
        # all_sprites.add(monster41)
        all_sprites.add(monster42)

        enemies.add(monster)
        enemies.add(monster1)
        enemies.add(monster2)
        enemies.add(monster3)
        enemies.add(monster4)
        enemies.add(monster5)
        enemies.add(monster6)
        enemies.add(monster7)
        enemies.add(monster8)
        enemies.add(monster9)
        enemies.add(monster10)
        enemies.add(monster11)
        enemies.add(monster12)
        enemies.add(monster13)
        enemies.add(monster14)
        enemies.add(monster15)
        enemies.add(monster16)
        enemies.add(monster17)
        enemies.add(monster18)
        enemies.add(monster19)
        enemies.add(monster20)
        enemies.add(monster21)
        enemies.add(monster22)
        enemies.add(monster23)
        enemies.add(monster24)
        enemies.add(monster25)
        enemies.add(monster26)
        enemies.add(monster27)
        enemies.add(monster28)
        enemies.add(monster29)
        enemies.add(monster30)
        enemies.add(monster31)
        enemies.add(monster32)
        enemies.add(monster33)
        enemies.add(monster34)
        enemies.add(monster35)
        enemies.add(monster36)
        enemies.add(monster37)
        enemies.add(monster38)
        enemies.add(monster39)
        enemies.add(monster40)
        # enemies.add(monster41)
        enemies.add(monster42)

        number_of_enemy = len(enemies)
        a += 1

    if pygame.sprite.spritecollideany(player, enemies):
        screen.fill(WHITE)
        pygame.display.update()
        screen.blit(text, textRect)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        end = ""
        pygame.mixer.Sound.play(death)
        pygame.mixer.Sound.play(defeat)



    elif pygame.sprite.groupcollide(bullet, enemies, False, True):
        number_of_enemy -= 1
        pygame.mixer.Sound.play(bug_death)

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    text_level = font.render('Level {}'.format(level), True, BLACK, WHITE)
    text_level_rec = text_level.get_rect()
    text_level_rec.center = (1080, 900)
    screen.blit(text_level, text_level_rec)

    if level == 6 and a == 5 and respawn_level == 0:

        screen.blit(vic, textRect)
        pygame.mixer.Sound.play(congrat)

        victory = ""

    elif len(enemies) == 0 and end != "" and respawn_level == 0:
        screen.fill((0, 0, 0))
        level += 1
        text_level = font.render('Level {}'.format(level), True, BLACK, WHITE)
        text_level_rec = text_level.get_rect()
        text_level_rec.center = (1080, 900)
        screen.blit(text_level, text_level_rec)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
            for entity in enemies:
                entity.kill()

    while victory == "":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
    while end == "":

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    level = None
                    a = None
                    screen.fill(WHITE)

                    player = Player(position=(350, 220))
                    monster = Hunter(position=(0, 0))

                    bullet_pos = player.rect.center
                    bullet_right = right_Bullet(bullet_pos)
                    bullet_left = left_Bullet(bullet_pos)

                    enemies.add(monster)

                    all_sprites.add(player)
                    all_sprites.add(monster)

                    level = 1
                    a = 1

                    end = "a"

                    pygame.display.update()

    pygame.display.update()
    FramePerSec.tick(FPS)
