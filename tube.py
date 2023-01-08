import pygame
from random import randint


class Tube():
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.width_of_tube = 80
        self.height_of_upper_tube = randint(20, 680)
        self.distancew = 145
        self.distanceh = 140
        pygame.draw.rect(screen, pygame.Color('red'), (400, 0, self.width_of_tube, self.height_of_upper_tube))
        pygame.draw.rect(screen, pygame.Color('red'), (400, self.height_of_upper_tube + self.distanceh,
                                                       self.width_of_tube,
                                                       800 - self.height_of_upper_tube - 80))


if __name__ == '__main__':
    pygame.init()
    size = 800, 800
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    tube = Tube(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()