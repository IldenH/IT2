import pygame
import pygame.locals as key
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_OFFSET = 30


pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


class Character(pygame.sprite.Sprite):
    def __init__(self):
        super(Character, self).__init__()
        self.image = pygame.Surface((25, 75))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.speed = 10

    def update(self):
        pass

    def check_bounds(self):
        """Keep character on the screen"""
        if self.rect.top <= SCREEN_OFFSET:
            self.rect.top = SCREEN_OFFSET
        if self.rect.bottom >= SCREEN_HEIGHT - SCREEN_OFFSET:
            self.rect.bottom = SCREEN_HEIGHT - SCREEN_OFFSET


class Player(Character):
    def __init__(self):
        super().__init__()
        self.rect.move_ip(SCREEN_OFFSET, SCREEN_OFFSET)

    def update(self, pressed_keys):
        self.__move(pressed_keys)
        self.check_bounds()

    def __move(self, pressed_keys):
        """Take pygame inputs and make player move"""
        if pressed_keys[key.K_UP] or pressed_keys[key.K_w] or pressed_keys[key.K_k]:
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[key.K_DOWN] or pressed_keys[key.K_s] or pressed_keys[key.K_j]:
            self.rect.move_ip(0, self.speed)


class Enemy(Character):
    def __init__(self):
        super().__init__()
        self.rect.move_ip(SCREEN_WIDTH - 2 * SCREEN_OFFSET, SCREEN_OFFSET)

    def update(self, pressed_keys):
        self.__move()
        self.check_bounds()

    def __move(self):
        """Move enemy towards ball"""
        self.rect.move_ip(0, self.speed)


class Ball(Character):
    def __init__(self):
        super().__init__()
        self.radius = 50
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(
            self.image, (255, 255, 255), (self.radius, self.radius), self.radius
        )
        self.rect = self.image.get_rect()
        self.rect.move_ip(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.speed = random.randint(1, 10)
        self.velocity = (
            random.choice((-self.speed, self.speed)),
            random.choice((-self.speed, self.speed)),
        )

    def update(self, pressed_keys):
        self.__move()
        self.check_bounds()

    def __move(self):
        """Move ball randomly"""
        self.rect.move_ip(self.velocity)

    def check_bounds(self):
        """Keep ball on screen"""
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH


sprites = pygame.sprite.Group()
sprites.add(Player())
sprites.add(Enemy())
sprites.add(Ball())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == key.KEYDOWN:
            if event.key == key.K_ESCAPE:
                running = False

    pressed_keys = pygame.key.get_pressed()
    sprites.update(pressed_keys)

    screen.fill((0, 0, 0))
    sprites.draw(screen)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
