# Alex Karu
import pygame

screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")


GREEN = [153, 255, 153]
RED = [255, 0, 0]
screen.fill(RED)

y = 1
for i in range(100):
    x = 1
    for i in range(100):
        pygame.draw.rect(screen, GREEN, [x, y, 15, 15])
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
