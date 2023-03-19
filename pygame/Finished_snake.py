import pygame   # Importib pygame'i
import random  # Importib random'i
import sys  # Importib sys'i

pygame.init()  # Initsialiseeri Pygame

WINDOW_WIDTH = 640  # Määrake mänguakna laius
WINDOW_HEIGHT = 480  # Määrake mänguakna kõrgus
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Looge mänguaken määratud laiuse ja kõrgusega
pygame.display.set_caption('Snake Game - Alex Karu')  # Seadke akna pealkirjaks "Snake Game - Alex Karu"

BLACK = (0, 0, 0)  # Määrab musta värvi RGB väärtused
WHITE = (255, 255, 255)  # Määrab valge värvi RGB väärtused
GREEN = (0, 255, 0)  # Määrab musta rohelise RGB väärtused
RED = (255, 0, 0)  # Määrab punase värvi RGB väärtused

clock = pygame.time.Clock()  # Loob mängu ajastuse haldamiseks kellaobjekt

BLOCK_SIZE = 20  # Määrake mängu iga ploki suurus
SNAKE_SPEED = 5  # Määratlege ussi+ kiirus
FOOD_SIZE = BLOCK_SIZE  # Määrake toiduploki suurus samaks kui ussiploki suurus
FOOD_COLOR = RED  # Määrab toiduploki värv punaseks


def draw_grid():  # Määrab funktsiooni mänguruudustiku joonistamiseks
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):  # Joonistab ruudustiku vasakult paremale
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):  # Joonistab ruudustiku ulevalt alla
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)  # Maarab ruudustiku omadused
            pygame.draw.rect(game_window, BLACK, rect, 1)  # Joonistab ruudustiku


def draw_snake(snake_list):  # Määrab funktsiooni ussi joonistamiseks
    for block in snake_list:  # Iga ussi ploki jaoks
        rect = pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE)  # Maarab ruudu omadused
        pygame.draw.rect(game_window, GREEN, rect)  # Joonistab ussi


def game_loop():  # Määrab mängutsükli funktsiooni
    snake_x = WINDOW_WIDTH / 2  # Seadke ussi X lähteasend akna keskele
    snake_y = WINDOW_HEIGHT / 2  # Seadke ussi Y lähteasend akna keskele
    snake_x_change = 0  # Seab ussi algus X-suund 0-ks (ei liigu horisontaalselt)
    snake_y_change = -BLOCK_SIZE  # Seab ussi algus Y-suunaks -BLOCK_SIZE-ks (liigub ülespoole)
    snake_list = []  # Loob ussi keha salvestamiseks tühja listi
    snake_length = 1  # Määrab ussi pikkuseks 1 (ainult pea)

    food_x = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE  # Määrab toiduploki X-positsiooni ploki suuruse juhuslikuks kordseks akna laiuse piires
    food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE  # Määrab toiduploki Y-positsiooni ploki suuruse juhuslikuks kordseks akna kõrguses

    game_over = False  # lähtestab mängu oleku
    snake_speed = SNAKE_SPEED  # määrake ussi algkiirus
    food_count = 0  # lähtestage skoori

    while not game_over:  # peamine mängutsükkel
        for event in pygame.event.get():  # saab kõik mängus toimuvad sündmused
            if event.type == pygame.QUIT:  # kontrollib, kas kasutaja soovib mängust väljuda
                game_over = True  # suleb mängu

            # Käsitleb kasutaja sisendit ussi suuna muutmiseks
            if event.type == pygame.KEYDOWN:  # kontrollib, kas kasutaja vajutab mingit nuppu
                if event.key == pygame.K_LEFT:  # kui vajutad vasakut noolt
                    snake_x_change = -BLOCK_SIZE  # liigutab ussi vasakule
                    snake_y_change = 0  # muudab ussi y kiiruse 0-ks
                elif event.key == pygame.K_RIGHT:  # kui vajutad paremat noolt
                    snake_x_change = BLOCK_SIZE  # liigutab ussi paremale
                    snake_y_change = 0  # muudab ussi y kiiruse 0-ks
                elif event.key == pygame.K_UP:  # kui vajutad üles noolt
                    snake_y_change = -BLOCK_SIZE  # liigutab ussi ülesse
                    snake_x_change = 0  # muudab ussi X kiiruse 0-ks
                elif event.key == pygame.K_DOWN:  # kui vajutad alla noolt
                    snake_y_change = BLOCK_SIZE  # liigutab ussi alla
                    snake_x_change = 0  # muudab ussi X kiiruse 0-ks

        snake_x += snake_x_change  # värskendab mao X-koordinaati
        snake_y += snake_y_change  # värskendab mao y-koordinaati

        if snake_x < 0 or snake_x >= WINDOW_WIDTH or snake_y < 0 or snake_y >= WINDOW_HEIGHT:  # kontrollige, kas uss tabas mänguakna piire
            game_over = True  # suleb mängu

        if snake_x == food_x and snake_y == food_y:  # kontrollib, kas uss tabas toitu
            food_x = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE  # randomiseerib toidu x-koordinaadi
            food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE  # randomiseerib toidu y-koordinaadi
            snake_length += 1  # suurendab ussi pikkust
            food_count += 1  # suurendab skoori
            if food_count % 2 == 0:  # suurendab ussi kiirust iga kahe söögikorra järel
                snake_speed += 1  # suurendab ussi kiirust 1 võrra

        snake_head = [snake_x, snake_y]  # loob uuendatud asukohas uue ussipea
        snake_list.append(snake_head)  # lisab uue pea ussi listi

        if len(snake_list) > snake_length:  # kui ussi pikkus ületab lubatud pikkuse
            del snake_list[0]  # eemaldab ussi saba (st loendi esimese elemendi)

        for block in snake_list[:-1]:  # kordab läbi kõik ussi kehas olevad plokid peale pea
            if block == snake_head:  # kontrollib, kas ussi pea tabab mõnda muud plokki tema kehas
                game_over = True  # kui see nii on, suleb mängu

        game_window.fill(WHITE)  # täidab mänguakna valge värviga

        draw_grid()  # joonistab mänguaknale ruudustiku jooned

        rect = pygame.Rect(food_x, food_y, BLOCK_SIZE, BLOCK_SIZE)  # loob toidu jaoks Rect objekti

        pygame.draw.rect(game_window, RED, rect)  # joonistab mänguaknale toidu

        draw_snake(snake_list)  # joonistab mao mänguaknale, kasutades funktsiooni draw_snake ja snake_list

        pygame.display.update()  # värskendage mänguakna kuva

        clock.tick(snake_speed)  # ootab lühikest aega, enne kui snake_speed väärtuse alusel uuesti värskendab

        font = pygame.font.Font(None, 36)  # määrab mängu fondi ja fondi suuruse teksti asemel
        text = font.render("Game Over! Your score: " + str(food_count), True, BLACK)  # loob mängu teksti peale mängija punktisummaga
        text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))  # loob mängu jaoks Rect objekti teksti peale ja asetab selle mänguakna keskele
        game_window.fill(WHITE)  # täidab mänguakna valge värviga
        game_window.blit(text, text_rect)  # joonistab mängu mänguaknas oleva teksti peale, kasutades Rect objekti
        pygame.display.update()  # värskendab mänguakna kuva

        while True:  # kui tõene
            for event in pygame.event.get():  # saab kõik mängus toimuvad sündmused
                if event.type == pygame.QUIT:  # kontrollib, kas kasutaja soovib mängust väljuda
                    pygame.quit()  # lõpetab Pygame'i
            sys.exit()  # väljub programmist


game_loop()  # Käivitab mängutsükli
