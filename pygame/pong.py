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
        self.radius = 30
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(
            self.image, (255, 255, 255), (self.radius, self.radius), self.radius
        )
        self.rect = self.image.get_rect()
        self.rect.move_ip(screen.width / 2, screen.height / 2)
        self.speed = 10
        self.velocity = pygame.math.Vector2()
        self.velocity.x = random.choice((-self.speed, self.speed))
        self.velocity.y = random.choice((-self.speed, self.speed))

    def update(self, pressed_keys):
        self.__move()
        self.check_bounds(offset=0)

    def __move(self):
        """Move ball randomly"""
        self.rect.move_ip(self.velocity)

    def handle_paddle_collision(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.flip_x()

    def check_bounds(self, offset=screen.offset):
        """Keep character on the screen"""
        if self.rect.x >= screen.width - 2 * self.radius or self.rect.x <= 0:
            self.flip_x()
        if self.rect.y >= screen.height - 2 * self.radius or self.rect.y <= 0:
            self.flip_y()

    def flip_x(self) -> None:
        self.velocity = (-self.velocity[0], self.velocity[1])

    def flip_y(self) -> None:
        self.velocity = (self.velocity[0], -self.velocity[1])


class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode([screen.width, screen.height])
        self.fps = 60

        self.sprites = pygame.sprite.Group()
        self.player = Player()
        self.enemy = Enemy()
        self.ball = Ball()
        self.sprites.add(self.player)
        self.sprites.add(self.enemy)
        self.sprites.add(self.ball)

    def run(self):
        pygame.init()
        while self.running:
            self.handle_events()
            self.update()
        pygame.quit()

    def update(self):
        self.sprites.update(pygame.key.get_pressed())
        self.ball.handle_paddle_collision(self.player)
        self.ball.handle_paddle_collision(self.enemy)
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
