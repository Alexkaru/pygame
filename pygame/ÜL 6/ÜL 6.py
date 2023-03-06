# Impordime vajalikud moodulid
import pygame
import sys
pygame.init()  # alustame pygame'i

screenX = 640  # ekraani laius
screenY = 480  # ekraani pikkus
screen = pygame.display.set_mode([screenX, screenY])  # ekraani loomine
pygame.display.set_caption("ÜL5 - Alex Karu")  # ekraanile pealkirja lisamine
screen.fill([173, 216, 230])  # täidab ekraani hele sinisega
clock = pygame.time.Clock()  # clock objekti loomin

pygame.mixer.music.load("BGM.mp3")
pygame.mixer.music.play(-1)

Hit_effect = pygame.mixer.Sound("HIT.mp3")
white = [255, 255, 255]
ball_x = 0  # balli x kordinaat
ball_y = 0  # balli y kordinaat
kiirus_x = 3  # balli x kiirus
kiirus_y = 4  # balli y kiirus
pad_x = 0  # aluse x kordinaat
pad_y = screenY/1.5  # aluse y kordinaat
kiirus_pad = 4  # aluse kiirus

ball_rect = pygame.Rect(ball_x, ball_y, 20, 20)  # palli kordinaadi ristküllik
ball_img = pygame.image.load("ball.png")  # palli pildi laadimine
ball_img = pygame.transform.scale(ball_img, (20, 20))  # palli pildi suuruse muutmine
pad_rect = pygame.Rect(pad_x, pad_y, 120, 20)  # aluse kordinaadi ristküllik
pad_img = pygame.image.load("pad.png")  # aluse pildi laadimine
pad_img = pygame.transform.scale(pad_img, (120, 20))  # aluse pildi suuruse muutmine
skoor = 0  # skoori seadistamine

gameover = False  # gameover muutuja vääraks muutmine
while not gameover:  # kordub kuni gameover muutuja on väär
    clock.tick(60)  # fps'i seadistamine
    for event in pygame.event.get():  # for loop sündmuse saamiseks
        if event.type == pygame.QUIT:  # kui sündmus on akna sulemine
            sys.exit()  # lõpetame mängu

        elif event.type == pygame.KEYDOWN:  # kui vajutatakse alla klahv
            if event.key == pygame.K_RIGHT:  # ja kui see klahv on parem nool
                kiirus_pad = 3  # siis paneme aluse paremale liikuma
            elif event.key == pygame.K_LEFT:  # ja kui see klahv on vasak nool
                kiirus_pad = -3  # siis paneme aluse vasakule liikuma
            if event.key == pygame.K_d:  # ja kui see klahv d
                kiirus_pad = 3  # siis paneme aluse paremale liikuma
            elif event.key == pygame.K_a:  # ja kui see klahv on a
                kiirus_pad = -3  # siis paneme aluse vasakule liikuma

    pall = pygame.Rect(ball_x, ball_y, 20, 20)  # palli asukoha seadistamine
    screen.blit(ball_img, pall)  # palli asukoha muutmine
    ball_x += kiirus_x  # palli x teljel liikumine
    ball_y += kiirus_y  # palli y telje liikumine

    pad_rect = pygame.Rect(pad_x, pad_y, 120, 20)  # aluse asukoha seadistamine
    screen.blit(pad_img, pad_rect)  # aluse asukoha muutmine
    pad_x += kiirus_pad  # aluse liigutamine

    screen.blit(pygame.font.Font(None, 30).render(f"Skoor: {skoor}", True, [255, 255, 255]), [10, 20])  # skoori kuvamine

    if ball_x > screenX - ball_img.get_rect().width or ball_x < 0:  # kui pall puudutab ekraani vasakut või paremat äärt
        kiirus_x = -kiirus_x  # muudab see oma suunda
        pygame.mixer.Sound.play(Hit_effect)  # ja mängib löömis hääle

    if ball_y > screenY-ball_img.get_rect().height or ball_y < 0:  # kui pall puudutab ekraani ülemist või alumist äärt
        kiirus_y = -kiirus_y  # muudab see oma suunda
        pygame.mixer.Sound.play(Hit_effect)  # ja mängib löömis hääle

    if ball_y > screenY - ball_img.get_rect().height:  # Kui pall puudutab alumist äärt
        gameover = True

    if pall.colliderect(pad_rect) and kiirus_y > 0:  # kui palli kordinaadi ristküllik puutub aluse kordinaadi ristküllikut
        kiirus_y = -kiirus_y  # muudab see suunda
        skoor += 1  # ja lisab skoorile 1
        pygame.mixer.Sound.play(Hit_effect)  # ja mängib löömis hääle

    if pad_x > screenX - pad_img.get_rect().width or pad_x < 0:  # kui alus puudutab ekraani äärt
        kiirus_pad = -kiirus_pad  # muudab see oma suunda

    pygame.display.flip()  # ekraani uuendamine
    screen.fill([173, 216, 230])  # ekraani täitmine hele sinisega

pygame.quit()  # pygame'i sulgemine
