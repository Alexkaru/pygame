# Alex Karu
import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])

punaneposx = 290

sinine_auto = pygame.image.load("f1_sinine.jpg")
sinine_auto = pygame.transform.scale(sinine_auto, [60, 150])
sinine_posx, sinine_posy = 170, -210

sinine_auto2 = pygame.image.load("f1_sinine.jpg")
sinine_auto2 = pygame.transform.scale(sinine_auto2, [60, 150])
sinine_posx2, sinine_posy2 = 420, -300

kiirus = 3
score_font = pygame.font.SysFont("times New Roman", 30)


def skoor(score):
    value = score_font.render("Sinu skoor: " + str(score), True, [0, 0, 0])
    screen.blit(value, [0, 0])


lopp_skoor = 0
mang_labi = False
while not mang_labi:
    clock.tick(60)
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    if sinine_posy >= 480:
        sinine_posy = -210
        lopp_skoor += 1

    if sinine_posy2 >= 480:
        sinine_posy2 = -300
        lopp_skoor += 1


    screen.blit(sinine_auto, (sinine_posx, sinine_posy))
    sinine_posy += kiirus
    pygame.display.flip()

    screen.blit(sinine_auto2, (sinine_posx2, sinine_posy2))
    sinine_posy2 += kiirus
    pygame.display.flip()

    background = pygame.image.load("bg.jpg")
    background = pygame.transform.scale(background, [640, 480])
    screen.blit(background, [0, 0])

    punane_auto = pygame.image.load("f1_punana.jpg")
    punane_auto = pygame.transform.scale(punane_auto, [60, 150])
    screen.blit(punane_auto, [punaneposx, 310])

    key = pygame.key.get_pressed()  # saame vajutatud klahvi
    if key[pygame.K_LEFT]:  # kui vasak klahv
        punaneposx -= 5  # liigutame autot vasakule
    if key[pygame.K_RIGHT]:  # kui parem klahv
        punaneposx += 5  # liigutame autot paremale

    skoor(lopp_skoor)

pygame.quit()
