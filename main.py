import pygame, sys, random
from pygame.locals import *

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
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Press "SPACE" to restart', True, YELLOW, RED)
vic = font.render("YOU WON!", True, YELLOW,RED)
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

        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect(center=position)

    def update(self):
        self.rect.move_ip(5, 0)
        if self.rect.right >= 1280:
            self.kill()


class left_Bullet(pygame.sprite.Sprite):

    def __init__(self, position):
        super(left_Bullet, self).__init__()

        self.image = pygame.image.load("bullet.png")
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
monster4 = Hunter(position=(0,100))
monster5 = Hunter(position=(0,200))
monster6 = Hunter(position=(0,300))
monster7 = Hunter(position=(0,400))
monster8 = Hunter(position=(0,500))
monster9 = Hunter(position=(0,600))
monster10 = Hunter(position=(0,700))
monster11 = Hunter(position=(0,800))
monster12 = Hunter(position=(0,900))
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

monster37 = Hunter(position=(1280, 1000))
monster38 = Hunter(position=(1280, 1000))
monster39 = Hunter(position=(1280, 1000))
monster40 = Hunter(position=(1280, 1000))
monster41 = Hunter(position=(1280, 1000))
monster42 = Hunter(position=(300, 1000))
monster43 = Hunter(position=(400, 1000))
monster44 = Hunter(position=(500, 1000))
monster45 = Hunter(position=(600, 1000))
monster46 = Hunter(position=(700, 1000))
monster47 = Hunter(position=(800, 1000))
monster48 = Hunter(position=(900, 1000))
monster49 = Hunter(position=(1000, 1000))
monster50 = Hunter(position=(1100, 1000))
monster51 = Hunter(position=(1200, 1000))

bullet_pos = player.rect.center
bullet_right = right_Bullet(bullet_pos)
bullet_left = left_Bullet(bullet_pos)

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

while running:
    clock.tick(FPS)
    victory = 0
    space_loop = "a"
    last = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False
        elif event.type == my_event_id:
            for entity in bullet:
                entity.kill()

            bullet_pos = player.rect.center
            bullet_right = right_Bullet(bullet_pos)
            bullet_left = left_Bullet(bullet_pos)
            all_sprites.add(bullet_right)
            all_sprites.add(bullet_left)
            bullet.add(bullet_right)
            bullet.add(bullet_left)

    player.update()
    monster.update(player)
    monster1.update(player)
    monster2.update(player)
    monster3.update(player)
    monster4.update(player)
    monster5.update(player)
    monster6.update(player)
    monster7.update(player)
    monster8.update(player)
    monster9.update(player)
    monster10.update(player)
    monster11.update(player)
    monster12.update(player)
    monster13.update(player)
    monster14.update(player)
    monster15.update(player)
    monster16.update(player)
    monster17.update(player)
    monster18.update(player)
    monster19.update(player)
    monster20.update(player)
    monster21.update(player)
    monster22.update(player)
    monster23.update(player)
    monster24.update(player)
    monster25.update(player)
    monster26.update(player)
    monster27.update(player)
    monster28.update(player)
    monster29.update(player)
    monster30.update(player)
    monster31.update(player)
    monster32.update(player)
    monster33.update(player)
    monster34.update(player)
    monster35.update(player)
    monster36.update(player)
    monster37.update(player)
    monster38.update(player)
    monster39.update(player)
    monster40.update(player)
    monster41.update(player)
    monster42.update(player)
    monster43.update(player)
    monster44.update(player)
    monster45.update(player)
    monster46.update(player)
    monster47.update(player)
    monster48.update(player)
    monster49.update(player)
    monster50.update(player)
    monster51.update(player)

    bullet_right.update()
    bullet_left.update()

    screen.fill(WHITE)

    if level == 2 and a == 1:
        monster = Hunter(position=(0, 0))
        monster1 = Hunter(position=(1280, 1000))
        all_sprites.add(monster)
        all_sprites.add(monster1)
        enemies.add(monster)
        enemies.add(monster1)
        number_of_enemy = len(enemies)
        a += 1

    if level == 3 and a == 2:
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

    if level == 4 and a == 3:
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

    if level == 5 and a == 4:
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
        monster13 = Hunter(position=(100,0))
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

        monster37 = Hunter(position=(1280, 1000))
        monster38 = Hunter(position=(1280, 1000))
        monster39 = Hunter(position=(1280, 1000))
        monster40 = Hunter(position=(1280, 1000))
        monster41 = Hunter(position=(1280, 1000))
        monster42 = Hunter(position=(300, 1000))
        monster43 = Hunter(position=(400, 1000))
        monster44 = Hunter(position=(500, 1000))
        monster45 = Hunter(position=(600, 1000))
        monster46 = Hunter(position=(700, 1000))
        monster47 = Hunter(position=(800, 1000))
        monster48 = Hunter(position=(900, 1000))
        monster49 = Hunter(position=(1000, 1000))
        monster50 = Hunter(position=(1100, 1000))
        monster51 = Hunter(position=(1200, 1000))

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
        all_sprites.add(monster41)
        all_sprites.add(monster42)
        all_sprites.add(monster43)
        all_sprites.add(monster44)
        all_sprites.add(monster45)
        all_sprites.add(monster46)
        all_sprites.add(monster47)
        all_sprites.add(monster48)
        all_sprites.add(monster49)
        all_sprites.add(monster50)
        all_sprites.add(monster51)
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
        enemies.add(monster41)
        enemies.add(monster42)
        enemies.add(monster43)
        enemies.add(monster44)
        enemies.add(monster45)
        enemies.add(monster46)
        enemies.add(monster47)
        enemies.add(monster48)
        enemies.add(monster49)
        enemies.add(monster50)
        enemies.add(monster51)

        number_of_enemy = len(enemies)
        a += 1

    if level == 6 and a == 5:
        screen.blit(vic, textRect)
        screen.fill(WHITE)
        victory = ""

    if pygame.sprite.spritecollideany(player, enemies):
        screen.blit(text, textRect)

        space_loop = ""

        for entity in all_sprites:
            entity.kill()

    elif pygame.sprite.groupcollide(bullet, enemies, False, True):
        number_of_enemy -= 1

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    text_level = font.render('Level {}'.format(level), True, BLACK, WHITE)
    text_level_rec = text_level.get_rect()
    text_level_rec.center = (1080, 900)
    screen.blit(text_level, text_level_rec)

    if len(enemies) == 0 and space_loop != "":
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
                    respawn_level = 1
                    screen.fill(WHITE)
                    for entity in bullet:
                        entity.kill()
                    player = Player(position=(500, 300))
                    monster = Hunter(position=(200, 200))
                    bullet_pos = player.rect.center
                    bullet_right = right_Bullet(bullet_pos)
                    bullet_left = left_Bullet(bullet_pos)
                    enemies.add(monster)
                    all_sprites.add(player)
                    all_sprites.add(monster)


            pygame.display.update()
    while space_loop == "":

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    respawn_level = 1
                    screen.fill(WHITE)
                    for entity in bullet:
                        entity.kill()
                    player = Player(position=(500, 300))
                    monster = Hunter(position=(200, 200))
                    bullet_pos = player.rect.center
                    bullet_right = right_Bullet(bullet_pos)
                    bullet_left = left_Bullet(bullet_pos)
                    enemies.add(monster)
                    all_sprites.add(player)
                    all_sprites.add(monster)


            pygame.display.update()

    pygame.display.update()
    FramePerSec.tick(FPS)
