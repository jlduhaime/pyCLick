import pygame
from pygame.locals import *

class Game:
    width = 640
    height = 480

    def __init__(self):
        print("Creating game object")
        pygame.init()
        self._display = None
        self._running = True
        self._display = pygame.display.set_mode((self.width, self.height))

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False


    def on_loop(self):
        pass

    def on_render(self):
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def run(self):

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

        self.on_cleanup()

if __name__ == "__main__":
    game = Game()
    game.run()
