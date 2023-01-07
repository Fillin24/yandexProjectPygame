import pygame
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


player_sprites = pygame.sprite.Group()
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Перемещение птички')
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    fullname = os.path.join('data', "flappy bird.png")
    bird_image = pygame.image.load(fullname)
    bird_image.set_colorkey(-1)
    bird = Bird()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bird.move_of_bird('up')
                elif event.key == pygame.K_DOWN:
                    bird.move_of_bird('down')
        screen.fill(pygame.Color('white'))
        player_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
