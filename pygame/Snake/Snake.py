# Alex Karu
import pygame
import random

pygame.init()

# Värvide väärtused
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 153, 0)
blue = (50, 153, 213)
snakle = (204, 0, 153)

# ekraani suurused
dis_width = 900
dis_height = 600

# teeb ekraani ja lisab sellele pealkirja
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game - Alex Karu')


clock = pygame.time.Clock()  # teeb kella

add_speed = 0
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("Times New Roman", 20)
score_font = pygame.font.SysFont("times New Roman", 30)

# teeb skoori
def skoor(score):
    value = score_font.render("Sinu skoor: " + str(score), True, black)
    dis.blit(value, [0, 0])

# teeb mao
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, snakle, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# teeb mängu taasmängitavaks
def manguloop():
    game_over = False  # mäng lõppeb
    game_close = False  # suleb mängu

    # teeb ekraani pooleks
    x1 = dis_width / 2
    y1 = dis_height / 2

    # teeb ussi
    x1_change = 0
    y1_change = 0

    # taastab ussi pikkuse 1-ks
    uss = []
    ussi_pikkus = 1

    # annab toidule uuse asukoha
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # kui mäng käib
    while not game_over:
        # kui kaotad
        while game_close == True:
            dis.fill(yellow)  # täidab ekraani kollasega
            message("You Lost! Press C-Play Again or Q-Quit", red)  # annab kaotamise sõnumi
            skoor(ussi_pikkus - 1)  # annab lõpp skoori
            pygame.display.update()

            # Kui vajutatakse Q-d siis mäng sulgeb, kui vajutad C-d siis mäng alustab uuesti
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        manguloop()

        # Kui vajutad alla siis uss hakkab liikuma alla, kui paremale, siis paremale, kui vasakule, siis vasakule ja kui ülesse siis ülesse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(green)
        pygame.draw.rect(dis, black, [foodx, foody, snake_block, snake_block])
        ussi_pea = []
        ussi_pea.append(x1)
        ussi_pea.append(y1)
        uss.append(ussi_pea)
        if len(uss) > ussi_pikkus:
            del uss[0]

        for x in uss[:-1]:
            if x == ussi_pea:
                game_close = True

        our_snake(snake_block, uss)
        skoor(ussi_pikkus - 1)

        pygame.display.update()

        # Kui uss sõöö ära söögi, siis see söök tekkib uues asukohas
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            ussi_pikkus += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

manguloop()
