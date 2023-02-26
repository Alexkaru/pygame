# Alex Karu
import pygame
import random
import sys

pygame.init()  # alustame pygame'i
screen = pygame.display.set_mode((640, 480))  # loome ekraani
pygame.display.set_caption("ÜÖ 4 Alex Karu")  # lisame pealkirja
clock = pygame.time.Clock()  # Loome 'clock' objekti
skoor = 0  # loome skoori

bg = pygame.image.load("bg.jpg")  # laadime taustapildi
bg2 = pygame.image.load("bg.jpg")  # laadime teise taustapildi
bgposX = 0  # esimese taustapildi X positsioon
bg2posX = 480  # teise taustapildi X positsioon
BGkiirus = -3  # tausta liikmis kiirus

sinine_auto = pygame.image.load("f1_sinine.jpg")  # laadime sinise auto
sinine_auto2 = pygame.image.load("f1_sinine.jpg")  # laadime teise sinise auto pildi
punane_auto = pygame.image.load("f1_punane.jpg")  # laadime punase auto pildi
gameover = False  # seme gamover muutuja väärtuse vääraks
Kiirus = 3  # sinise auto kiirus

Sinine_posy = random.randint(0, 100)  # sinise auto positsioon Y
Sinine_posy2 = random.randint(0, 100)  # teise sinise auto positsioon Y
Punane_posx, Punane_posy = 298, 390  # punase auto positsioonid
Punane_kiirus = 0  # punase auto kiirus
Sinine_posx = random.randint(310, 450)  # sinise auto positsioon X
Sinine_posx2 = random.randint(140, 270)  # teise sinise auto positsioon X

while not gameover:  # kordub, kuni gameover muutuja on väär
    clock.tick(100)  # seadistame fps-i

    for event in pygame.event.get():  # for loop
        if event.type == pygame.QUIT:  # kui aken suletakse
            sys.exit()  # lõpetame mängu

    # taustapiltide lisamine
    screen.blit(bg, (0, bgposX))
    screen.blit(bg2, (0, bg2posX))

    # kiiruse kasutamine
    bgposX -= BGkiirus
    bg2posX -= BGkiirus

    # kui taustapilt jõuab lõppu, viime tagasi algusesse
    if bgposX >= 480:
        bgposX = -480
    if bg2posX >= 480:
        bg2posX = -480

    # siniste autode lisamine
    screen.blit(sinine_auto, (Sinine_posx, Sinine_posy))
    screen.blit(sinine_auto2, (Sinine_posx2, Sinine_posy2))

    # autode liigutamine
    Sinine_posy += Kiirus + 0.8
    Sinine_posy2 += Kiirus + 1

    # punase auto lisamine
    screen.blit(punane_auto, (Punane_posx, Punane_posy))
    Punane_posy += Punane_kiirus  # auto liigutamine

    # skoori näitamine
    screen.blit(pygame.font.Font(None, 30).render(f"Skoor: {skoor}", True, [255, 255, 255]), [10, 20])

    # autode positsiooni taastamine
    if Sinine_posy >= 480:  # kui auto jõuab lõppu
        Sinine_posy = -120  # taastame auto positsiooni
        skoor += 1  # suurendame skoori
        Sinine_posx = random.randint(130, 280)  # paneme auto suvalisse kohta

    if Sinine_posy2 >= 480:  # kui teine auto jõuab lõppu
        Sinine_posy2 = -120  # taastame positsiooni
        skoor += 1  # suurendame skoori
        Sinine_posx2 = random.randint(300, 480)  # paneme auto suvalisse kohta

    if Punane_posx >= 640:  # kui punane auto lahkub ekraanilt
        Punane_posx = 520  # liigutame selle tagasi

    if Punane_posx <= 0:  # kui punane auto lahkub ekraanilt
        Punane_posx = 80  # liigutame selle tagasi

    # punase auto liigutamine
    key = pygame.key.get_pressed()  # saame vajutatud klahvi
    if key[pygame.K_LEFT]:  # kui vasak klahv
        Punane_posx -= 5  # liigutame autot vasakule
    if key[pygame.K_RIGHT]:  # kui parem klahv
        Punane_posx += 5  # liigutame autot paremale
    if key[pygame.K_a]:  # kui a klahv
        Punane_posx -= 5  # liigutame autot vasakule
    if key[pygame.K_d]:  # kui d klahv
        Punane_posx += 5  # liigutame autot paremale

    # mängu lõpp, kui sinine auto puudutab punast
    if Punane_posy + 55 >= Sinine_posy >= Punane_posy - 55:  # kui sinine ja punane auto on samal kohal
        if Punane_posx + 50 >= Sinine_posx >= Punane_posx - 50:  # kui sinine ja punane auto on ka samal kohal
            gameover = True  # lõpetame mängu

    if Punane_posy + 55 >= Sinine_posy2 >= Punane_posy - 55:  # kui teine sinine auto ja punane auto on samal kohal
        if Punane_posx + 50 >= Sinine_posx2 >= Punane_posx - 50:  # kui teine sinine auto ja punane auto on ka samal kohal
            gameover = True  # lõpetame mängu

    pygame.display.flip()  # värskendame ekraani

while True:  # kontroll, kas mäng on läbi
    if gameover:  # kui mäng on läbi
        # kuvame "Mäng läbi!"
        screen.blit(pygame.font.Font(None, 50).render("Mäng läbi!", True, [255, 255, 255]), [230, 300])
        # kuvame skoori
        screen.blit(pygame.font.Font(None, 50).render(f"Skoor: {skoor}", True, [255, 255, 255]), [240, 200])
        pygame.display.flip()  # uuendame ekraani

    for event in pygame.event.get():  # for loop sündmuse saamiseks
        if event.type == pygame.QUIT:  # kui ekraan suletakse
            sys.exit()  # lõpetame mängu
