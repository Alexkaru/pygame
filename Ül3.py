# Alex Karu
import pygame

screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")


GREEN = [153, 255, 153]  # Annab roherlise rgb väärtused
RED = [255, 0, 0]  # Annab punase rgb väärtused
BLUE = [0, 102, 255]  # Annab sinise rgb väärtused
YELLOW = [255, 255, 0]  # Annab kollase rgb väärtused
PINK = [255, 51, 204]  # Annab roosa rgb väärtused
PURPLE = [204, 0, 255]  # Annab lillga rgb väärtused
BLACK = [0, 0, 0]  # Annab musta rgb väärtused
WHITE = [255, 255, 255]  # Annab valge rgb väärtused
screen.fill(RED)  # Täidab ekraani punasega


class Square:  # Loob Square classi
    def __init__(self, color, sizea, sizeb):  # Loob klassist objekti
        self.color = color
        self.sizea = sizea
        self.sizeb = sizeb

    def make_square(self):  # Funktsioon ruutude tegemiseks
        y = 1
        for i in range(35):
            x = 1
            for j in range(38):
                pygame.draw.rect(screen, self.color, [x, y, self.sizea, self.sizeb])
                x += 18
            y += 18


Square.make_square(Square(GREEN, 15, 15))  # Teeb ruudud

pygame.display.flip()
# jätab avatud akna ekraanile
running = True
while running:
    for event in pygame.event.get():
        # laseb avatud akna kinni panna
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()
