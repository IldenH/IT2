import pygame
import pygame.mixer
import random
import math
import time

class GameScreen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.hidden_object = HiddenObject(self.screen)

    def draw(self):
        self.screen.fill((0, 0, 0))
        # teikn det skjulte objektet for debugging ...
        pygame.display.flip()

    def handle_click(self, pos):
        if self.hidden_object.is_clicked(pos):
            print("Gratulerar, du fant det skjulte objektet!")

class HiddenObject:
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(0, 600)
        self.y = random.randint(0, 600)
        self.speed = 5

    def move(self):
        self.x = (self.x + random.choice([-1, 1]) * self.speed) % 600
        self.y = (self.y + random.choice([-1, 1]) * self.speed) % 600

    def play_sound(self, pos):
        distance = math.hypot(self.x - pos[0], self.y - pos[1])
        # Juster lydstyrken etter avstanden til det skjulte objektet ...

    def is_clicked(self, pos):
        return math.hypot(self.x - pos[0], self.y - pos[1]) < 50

def main():
    game_screen = GameScreen()
    running = True

    # Starttidspunkt for spelet ..
    #runtime = ... # Lengde på lydsample = tida du har på å finne det skjulte objektet

    # Ved oppstart av spelet, spel av lydfila tone.mp3 ..

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game_screen.handle_click(pygame.mouse.get_pos())
                # Avslutt spelet og skriv ut kor lang tid det tok å finne det skjulte objektet
        
        # Dersom tida er ute, avslutt spelet ...

        game_screen.hidden_object.move()
        game_screen.hidden_object.play_sound(pygame.mouse.get_pos())
        game_screen.draw()
        game_screen.clock.tick(60)

if __name__ == "__main__":
    main()