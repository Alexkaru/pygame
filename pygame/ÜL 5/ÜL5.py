# Impordime vajalikud moodulid
import pygame
import sys
pygame.init()  # alustame pygame mooduli


# Seadistame ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("ÜL4 - Alex Karu")
screen.fill([173, 216, 230])
clock = pygame.time.Clock()

# Seadistame palli kiiruse ja positsiooni
ball_x = 0
ball_y = 0
kiirus_x = 3
kiirus_y = 4

# Seadistame aluse kiiruse ja positsiooni
pad_x = 0
pad_y = screenY/1.5
kiirus_pad = 4

# Piltide laadimine
ball_rect = pygame.Rect(ball_x, ball_y, 20, 20)
ball_img = pygame.image.load("ball.png")
ball_img = pygame.transform.scale(ball_img, (20, 20))
pad_rect = pygame.Rect(pad_x, pad_y, 120, 20)
pad_img = pygame.image.load("pad.png")
pad_img = pygame.transform.scale(pad_img, (120, 20))

# Scoori muutuja seadistamine
skoor = 0

gameover = False  # gameover muutuja seadistamine
while not gameover:  # kordub, kuni gameover muutuja on False
    clock.tick(60)  # seadistame kaadrisageduse
    for event in pygame.event.get():  # sündmuse käitlemine
        if event.type == pygame.QUIT:  # kui aken suletakse
            sys.exit()  # lõpetame mängu

    # Palli liikumine
    pall = pygame.Rect(ball_x, ball_y, 20, 20)
    screen.blit(ball_img, pall)
    ball_x += kiirus_x
    ball_y += kiirus_y

    # Aluse liikumine
    pad_rect = pygame.Rect(pad_x, pad_y, 120, 20)
    screen.blit(pad_img, pad_rect)
    pad_x += kiirus_pad

    # Skoori kuvamine
    screen.blit(pygame.font.Font(None, 30).render(f"Skoor: {skoor}", True, [255, 255, 255]), [10, 20])

    # Kui puudutab ekraani ääri, muudab palli suunda
    if ball_x > screenX - ball_img.get_rect().width or ball_x < 0:
        kiirus_x = -kiirus_x
    if ball_y > screenY-ball_img.get_rect().height or ball_y < 0:
        kiirus_y = -kiirus_y

    # Kui puudutab alust, muudab palli suunda ja suurendab skoori
    if pall.colliderect(pad_rect) and kiirus_y > 0:
        kiirus_y = -kiirus_y
        skoor += 1

    # Kui puudutab ekraani ääri, muudab aluse suunda
    if pad_x > screenX - pad_img.get_rect().width or pad_x < 0:
        kiirus_pad = -kiirus_pad

    pygame.display.flip()  # ekraani uuendamine
    screen.fill([173, 216, 230])  # ekraani täitmine hele sinisega

pygame.quit()