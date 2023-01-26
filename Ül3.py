# Alex Karu
import pygame

screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")


GREEN = [153, 255, 153]
RED = [255, 0, 0]
BLUE = [0, 102, 255]
YELLOW = [255, 255, 0]
PINK = [255, 51, 204]
PURPLE = [204, 0, 255]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
screen.fill(RED)


class Square:
    def __init__(self, color, sizea, sizeb):
        self.color = color
        self.sizea = sizea
        self.sizeb = sizeb

    def make_square(self):
        y = 1
        for i in range(35):
            x = 1
            for j in range(38):
                pygame.draw.rect(screen, self.color, [x, y, self.sizea, self.sizeb])
                x += 18
            y += 18


pygame.display.flip()
# jätab avatud akna ekraanile
running = True
while running:
    for event in pygame.event.get():
        # laseb avatud akna kinni panna
        if event.type == pygame.QUIT:
            running = False
