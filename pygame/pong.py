import pygame
import pygame.locals as key

SCREEN_OFFSET = 30


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.Surface((25, 75))
        self.surface.fill((255, 255, 255))
        self.rectangle = self.surface.get_rect()
        self.rectangle.move_ip(SCREEN_OFFSET, SCREEN_OFFSET)
        self.speed = 1.5

    def update(self, pressed_keys):
        self.__take_input(pressed_keys)
        self.__check_bounds()

    def __take_input(self, pressed_keys):
        """Take pygame inputs and make player move"""
        if pressed_keys[key.K_UP] or pressed_keys[key.K_w] or pressed_keys[key.K_k]:
            self.rectangle.move_ip(0, -self.speed)
        if pressed_keys[key.K_DOWN] or pressed_keys[key.K_s] or pressed_keys[key.K_j]:
            self.rectangle.move_ip(0, self.speed)

    def __check_bounds(self):
        """Keep player on the screen"""
        if self.rectangle.top <= SCREEN_OFFSET:
            self.rectangle.top = SCREEN_OFFSET
        if self.rectangle.bottom >= SCREEN_HEIGHT - SCREEN_OFFSET:
            self.rectangle.bottom = SCREEN_HEIGHT - SCREEN_OFFSET


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
        elif event.type == key.KEYDOWN:
            if event.key == key.K_ESCAPE:
                running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    screen.fill((0, 0, 0))
    screen.blit(player.surface, player.rectangle.topleft)

    pygame.display.flip()

pygame.quit()
