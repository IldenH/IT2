import pygame
import pygame.locals as key
import random


class Screen:
    def __init__(self) -> None:
        self.width = 800
        self.height = 600
        self.offset = 30


screen = Screen()


class Character(pygame.sprite.Sprite):
    def __init__(self):
        super(Character, self).__init__()
        self.image = pygame.Surface((25, 75))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.speed = 10

    def update(self):
        pass

    def check_bounds(self, offset=screen.offset):
        """Keep character on the screen"""
        if self.rect.top <= offset:
            self.rect.top = offset
        if self.rect.bottom >= screen.height - offset:
            self.rect.bottom = screen.height - offset
        if self.rect.left <= offset:
            self.rect.left = offset
        if self.rect.right >= screen.width - offset:
            self.rect.right = screen.width - offset


class Player(Character):
    def __init__(self):
        super().__init__()
        self.rect.move_ip(screen.offset, screen.offset)

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
        self.rect.move_ip(screen.width - 2 * screen.offset, screen.offset)

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
        self.rect.move_ip(screen.width / 2, screen.height / 2)
        self.speed = random.randint(1, 10)
        self.velocity = (
            random.choice((-self.speed, self.speed)),
            random.choice((-self.speed, self.speed)),
        )

    def update(self, pressed_keys):
        self.__move()
        self.check_bounds(offset=0)

    def __move(self):
        """Move ball randomly"""
        self.rect.move_ip(self.velocity)


class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode([screen.width, screen.height])
        self.fps = 60

        self.sprites = pygame.sprite.Group()
        self.sprites.add(Player())
        self.sprites.add(Enemy())
        self.sprites.add(Ball())

    def run(self):
        pygame.init()
        while self.running:
            self.handle_events()
            self.update()
        pygame.quit()

    def update(self):
        self.sprites.update(pygame.key.get_pressed())
        self.draw()

        pygame.display.update()
        pygame.time.Clock().tick(self.fps)

    def draw(self):
        self.screen.fill("black")
        self.sprites.draw(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            escape = event.type == key.KEYDOWN and event.key == key.K_ESCAPE
            if event.type == pygame.QUIT or escape:
                self.running = False


if __name__ == "__main__":
    game = Game()
    game.run()
