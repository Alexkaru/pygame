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


class Square:

    def __int__(self, squarecolor, linecolor, sizea, sizeb):
        self.squarecolor = squarecolor
        self.linecolor = linecolor
        self.sizea = sizea
        self.siseb = sizeb
        

pygame.display.flip()
# jätab avatud akna ekraanile
running = True
while running:
    for event in pygame.event.get():
        # laseb avatud akna kinni panna
        if event.type == pygame.QUIT:
            running = False
