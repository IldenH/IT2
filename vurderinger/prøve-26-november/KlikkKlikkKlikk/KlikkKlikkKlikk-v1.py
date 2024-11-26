import pygame
import pygame.locals as key


class Screen:
    def __init__(self) -> None:
        self.width = 800
        self.height = 600


SCREEN = Screen()
TIME_SECONDS = 10


class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode([SCREEN.width, SCREEN.height])
        self.fps = 60
        self.clicks = 0

    def run(self):
        pygame.init()
        pygame.time.set_timer(pygame.QUIT, TIME_SECONDS * 1000)
        while self.running:
            self.handle_events()
            self.update()
        pygame.quit()

    def update(self):
        self.draw()

        pygame.display.update()
        pygame.time.Clock().tick(self.fps)

    def draw(self):
        self.screen.fill("black")

    def handle_events(self):
        for event in pygame.event.get():
            escape = event.type == key.KEYDOWN and event.key == key.K_ESCAPE
            if event.type == pygame.QUIT or escape:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.clicks += 1


if __name__ == "__main__":
    game = Game()
    print(f"Trykk så fort som mulig på {TIME_SECONDS} sekunder!")
    game.run()
    print(f"Du trykket {game.clicks} ganger!")
