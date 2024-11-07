import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_a,
    K_s,
    K_d,
    K_ESCAPE,
    KEYDOWN,
)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.Surface((75, 25))
        self.surface.fill((255, 255, 255))
        self.rectangle = self.surface.get_rect()
        self.speed = 1

    def update(self, pressed_keys):
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            self.rectangle.move_ip(0, -self.speed)
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            self.rectangle.move_ip(0, self.speed)
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.rectangle.move_ip(-self.speed, 0)
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.rectangle.move_ip(self.speed, 0)

        # Keep player on the screen
        if self.rectangle.left < 0:
            self.rectangle.left = 0
        if self.rectangle.right > SCREEN_WIDTH:
            self.rectangle.right = SCREEN_WIDTH
        if self.rectangle.top <= 0:
            self.rectangle.top = 0
        if self.rectangle.bottom >= SCREEN_HEIGHT:
            self.rectangle.bottom = SCREEN_HEIGHT


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    screen.fill((0, 0, 0))
    screen.blit(player.surface, player.rectangle.topleft)

    pygame.display.flip()

pygame.quit()
