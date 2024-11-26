import pygame
import pygame.locals as key
import random


class Screen:
    def __init__(self) -> None:
        self.width = 800
        self.height = 600


SCREEN = Screen()
TIME_SECONDS = 2


class Game:
    def __init__(self) -> None:
        self.running = True
        self.screen = pygame.display.set_mode([SCREEN.width, SCREEN.height])
        self.fps = 60
        self.clicks = 0
        self.background_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        self.game_end_event = pygame.USEREVENT
        self.beste_resultat = 0

    def run(self) -> None:
        pygame.init()
        pygame.time.set_timer(self.game_end_event, TIME_SECONDS * 1000)
        while self.running:
            self.handle_events()
            self.update()
        pygame.quit()

    def update(self) -> None:
        self.draw()

        pygame.display.update()
        pygame.time.Clock().tick(self.fps)

    def draw(self) -> None:
        self.screen.fill(self.background_color)

    def handle_events(self) -> None:
        for event in pygame.event.get():
            escape = event.type == key.KEYDOWN and event.key == key.K_ESCAPE
            if event.type == pygame.QUIT or escape:
                self.running = False
            elif event.type == self.game_end_event:
                self.handle_new_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.clicks += 1

    def handle_new_game(self) -> None:
        print(f"Du trykket {self.clicks} ganger!")

        if self.clicks > self.beste_resultat:
            print("Ny rekord!")
            self.beste_resultat = self.clicks
        else:
            print("Ikke ny rekord, prøv igjen!")

        self.background_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )


if __name__ == "__main__":
    print(f"Trykk så fort som mulig på {TIME_SECONDS} sekunder!")
    game = Game()
    game.run()

    resultat_tekst = f"Beste resultat: {game.beste_resultat}"
    print(resultat_tekst)
    # https://www.geeksforgeeks.org/writing-to-file-in-python/
    resultat_fil = open("resultat.txt", "w")
    resultat_fil.write(resultat_tekst)
