import pygame
from random import randint


class Tube:
    width_of_tube = 80
    def __init__(self, screen, x_pos, height_of_upper_tube):
        super().__init__()
        self.screen = screen
        self.width_of_tube = 80
        self.height_of_upper_tube = height_of_upper_tube
        self.distancew = 145
        self.distanceh = 140
        pygame.draw.rect(screen, pygame.Color('red'), (x_pos, 0, self.width_of_tube, self.height_of_upper_tube))
        pygame.draw.rect(screen, pygame.Color('red'), (x_pos, self.height_of_upper_tube + self.distanceh,
                                                       self.width_of_tube,
                                                       800 - self.height_of_upper_tube - 80))


screen_w, screen_h = 800, 800
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((screen_w, screen_h))
    screen.fill((0, 0, 0))
    x_pos = screen_w
    fps = 60
    velocity = 400
    height_of_upper_tube = randint(20, screen_h - 120)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if x_pos <= -Tube.width_of_tube:
            x_pos = screen_w
            height_of_upper_tube = randint(20, screen_h - 120)
        screen.fill(pygame.Color('black'))
        tube = Tube(screen, x_pos, height_of_upper_tube)
        x_pos -= velocity / fps
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
