import pygame, math, random
from pygame.locals import *

class Score:
    def __init__(self):
        self.val = 0
        self.multiplier = 1
        pygame.font.init()
        self.font = pygame.font.SysFont('ARIAL', 14)

    def draw(self):
        return self.font.render(str(self.val), False, (255, 255, 255))

    def incr(self):
        self.val += 1 * self.multiplier

class Circle:

    def __init__(self, max_x, max_y):
        self._radius = 50
        self._x_pos = random.randint(0 + self._radius, max_x - (self._radius * 2))
        self._y_pos = random.randint(0 + self._radius, max_y - (self._radius * 2))
        self.new_x = self._x_pos
        self.new_y = self._y_pos
        self.max_x = max_x
        self.max_y = max_y
        self._border = 0
        self._color = (0, 255, 255)

    def draw(self, surface):
        pygame.draw.circle(surface, self._color, (self._x_pos, self._y_pos), self._radius, self._border)

    def move(self, amount):
        if self.new_x == self._x_pos and self.new_y == self._y_pos:
            self.new_x = self._x_pos + random.randint(-self._x_pos, self.max_x - self._radius - self._x_pos)
            self.new_y = self._y_pos + random.randint(-self._y_pos, self.max_y - self._radius - self._y_pos)

        else:
            if self.new_x > self._x_pos:
                self._x_pos += amount
            if self.new_x < self._x_pos:
                self._x_pos -= amount
            if self.new_y > self._y_pos:
                self._y_pos += amount
            if self.new_y < self._y_pos:
                self._y_pos -= amount

    def shrink(self):
        if self._radius > 10:
            self._radius -= 1

class Final:
    def __init__(self):
        self.text = "Game Over! Press 'r' to restart"
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 20)

    def draw(self):
        return self.font.render(self.text, False, (255,255,255))

class Game:
    width = 640
    height = 480

    def __init__(self):
        pygame.init()
        self._clock = pygame.time.Clock()
        self._running = True
        self._inside = False
        self._game_over = False
        self._display = pygame.display.set_mode((self.width, self.height))
        self.circle = Circle(self.width, self.height)
        self.score = Score()
        self.final_score = Final()
        pygame.display.set_caption('DON\'T MOVE')

    def reset(self):
        del self.circle
        del self.score
        del self.final_score

        self._running = True
        self._inside = False
        self._game_over = False
        self._display = pygame.display.set_mode((self.width, self.height))
        self.circle = Circle(self.width, self.height)
        self.score = Score()
        self.final_score = Final()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
        if event.type == KEYDOWN:
            if  event.key == pygame.K_ESCAPE:
                self._running = False

            if event.key == pygame.K_r:
                self.reset()

    def on_loop(self):
        position = self._display.get_at(pygame.mouse.get_pos()) == (self.circle._color)

        if self._inside == True:
            self.circle.move(1)

            if position != 1:
                self._inside = False
                self._game_over = True
        else:
            if position == 1:
                self._inside = True
            else:
                self._inside = False

    def on_render(self):
        if not self._game_over:
            self._display.fill((0,0,0))
            self.circle.draw(self._display)
            self._display.blit(self.score.draw(), (0,0))
            pygame.display.flip()
        else:
            self._display.blit(self.final_score.draw(), (self.width/2, self.height - 50))
            pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def run(self):

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)

            if self._inside:
                self.score.incr()

            self.on_loop()
            self.on_render()

            self._clock.tick(100)
        print(self._clock.get_fps())
        self.on_cleanup()

if __name__ == "__main__":
    game = Game()
    game.run()
