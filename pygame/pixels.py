"""
Largly inspired by:
https://github.com/hausnes/it2-2024-2025/blob/3c43753328cd72bb0fbc2c57485275cb88383b8b/pygame/teikning-pixelart/pixels-oop.py
"""

import pygame


class Screen:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height


class PixelArtApp:
    def __init__(self, screen: Screen, pixel_size: int) -> None:
        self.screen = screen
        self.pixel_size = pixel_size
        self.surface = pygame.display.set_mode((screen.width, screen.height))

        self.background_color = pygame.Color("white")
        self.text_color = pygame.Color("black")

        self.drawing_color = pygame.Color("black")
        self.help_shown = False
        self.font = pygame.font.Font(None, 36)
        self.running = True

        self.clear_surface()

    def change_color(self, key) -> pygame.Color:
        match key:
            case pygame.K_1:
                return pygame.Color("black")
            case pygame.K_1:
                return pygame.Color("black")
            case pygame.K_2:
                return pygame.Color("red")
            case pygame.K_3:
                return pygame.Color("green")
            case pygame.K_4:
                return pygame.Color("blue")
            case pygame.K_5:
                return pygame.Color("white")
            case _:
                return self.drawing_color

    def clear_surface(self) -> None:
        """Generate a 2D array of white pixels"""
        self.pixels = [
            [self.background_color for _ in range(self.screen.width // self.pixel_size)]
            for _ in range(self.screen.width // self.pixel_size)
        ]

    def draw_help(self) -> None:
        self.surface.fill(self.background_color)
        commands = [
            ("1", "Change color to black"),
            ("2", "Change color to red"),
            ("3", "Change color to green"),
            ("4", "Change color to blue"),
            ("5", "Change color to white"),
            ("c", "Clear the screen"),
            ("s", "Save the screen to a PNG file"),
            ("h", "Toggle this help screen"),
        ]
        for index, (key, description) in enumerate(commands):
            text = self.font.render(f"{key}: {description}", True, self.text_color)
            padding = 50
            gap = (self.screen.height - padding) // len(commands)
            self.surface.blit(
                text,
                (padding, padding + index * gap),
            )

    def run(self) -> None:
        while self.running:
            self.draw()
            self.handle_events()

    def draw(self) -> None:
        if self.help_shown:
            self.draw_help()
        else:
            self.draw_pixels()
        pygame.display.flip()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            self.handle_mouse(event)
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handle_keys(event)

    def handle_mouse(self, event) -> None:
        x, y = pygame.mouse.get_pos()
        x_pixel = x // self.pixel_size
        y_pixel = y // self.pixel_size
        mouse_button_down = pygame.mouse.get_pressed()[0]
        if event.type == pygame.MOUSEMOTION and mouse_button_down:
            self.pixels[y_pixel][x_pixel] = self.drawing_color

    def handle_keys(self, event) -> None:
        if event.key == pygame.K_h:
            self.toggle_help()
        elif not self.help_shown:
            self.drawing_color = self.change_color(event.key)
            if event.key == pygame.K_c:
                self.clear_surface()
            elif event.key == pygame.K_s:
                pygame.image.save(self.surface, "pixelart.png")

    def toggle_help(self) -> None:
        self.help_shown = not self.help_shown

    def draw_pixels(self) -> None:
        for y, row in enumerate(self.pixels):
            for x, color in enumerate(row):
                pygame.draw.rect(
                    self.surface,
                    pygame.Color(color),
                    pygame.Rect(
                        x * self.pixel_size,
                        y * self.pixel_size,
                        self.pixel_size,
                        self.pixel_size,
                    ),
                )


if __name__ == "__main__":
    pygame.init()
    app = PixelArtApp(Screen(800, 600), 10)
    app.run()
    pygame.quit()
