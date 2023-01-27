#  Alex Karu
import pygame  # impordib pygami

pygame.init()  # käivitab pygamei

screen = pygame.display.set_mode([300, 620])  # teeb uue akna mille kõrgus ja paksus on 300
pygame.display.set_caption('Foor - Alex Karu')  # annab aknale mine
pygame.draw.circle(screen, [255, 0, 0], [150, 62.5], 35, )  # teeb punase ringi
pygame.draw.circle(screen, [255, 255, 0], [150, 137.5], 35, )  # teeb kollase ringi
pygame.draw.circle(screen, [0, 255, 0], [150, 212.5], 35, )  # teeb rohelise ringi
pygame.draw.rect(screen, [91, 109, 125], [100, 12.5, 100, 250], 2)  # teeb ümbritseva ristkülliku
pygame.draw.rect(screen, [91, 109, 125], [145, 260, 10, 260])  # teeb posti
pygame.draw.polygon(screen, [91, 109, 125], [[148, 515], [100, 595], [200, 595], [150, 515]], 5)  # teeb postialuse
pygame.draw.polygon(screen, [0, 0, 255], [[149, 515], [134, 541.6], [165, 541.6], [149, 515]], 0)  # teeb sinise kolmnurga
pygame.draw.polygon(screen, [255, 255, 255], [[119, 568.26], [102, 595], [198, 595], [181, 568.26]], 0)  # teeb valge trapetsi

pygame.display.flip()  # uuendab ekraani
# jätab avatud akna ekraanile
running = True
while running:
    for event in pygame.event.get():
        #  laseb avatud akna kinni panna
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()