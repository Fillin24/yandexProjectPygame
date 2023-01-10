import pygame
from random import randint
import os


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(player_sprites)
        self.image = bird_image
        self.pos = [200, 400]
        self.rect = self.image.get_rect().move(200, 400)

    def move_of_bird(self, movement):
        if movement == 'up' and self.pos[1] != 0:
            self.pos[1] -= 40
            self.rect = self.image.get_rect().move(self.pos[0], self.pos[1])
        elif movement == 'down' and self.pos[1] != 720:
            self.pos[1] += 40
            self.rect = self.image.get_rect().move(self.pos[0], self.pos[1])


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


player_sprites = pygame.sprite.Group()
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
    fullname = os.path.join('data', "flappy bird.png")
    bird_image = pygame.image.load(fullname)
    bird_image.set_colorkey(-1)
    bird = Bird()
    running = True
    while running:
        if x_pos <= -Tube.width_of_tube:
            x_pos = screen_w
            height_of_upper_tube = randint(20, screen_h - 120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                bird.move_of_bird('up')
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                bird.move_of_bird('down')
        screen.fill(pygame.Color('white'))
        tube = Tube(screen, x_pos, height_of_upper_tube)
        x_pos -= velocity / fps
        clock.tick(fps)
        player_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
