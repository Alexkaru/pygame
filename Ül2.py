# Alex Karu
import pygame  # impordib pygami

pygame.init()
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption('2')
font = pygame.font.Font(pygame.font.match_font('Times New Roman'), 50)

bg = pygame.image.load('bg_shop.jpg')
screen.blit(bg,[0,0])

seller = pygame.image.load('seller.png')
seller = pygame.transform.scale(seller, [265, 308])
screen.blit(seller,[100, 155])

chat = pygame.image.load('chat.png')
chat = pygame.transform.scale(chat, [150, 60])
screen.blit(chat,[0,0])

pygame.display.flip()
# jätab avatud akna ekraanile
running = True
while running:
    for event in pygame.event.get():
        # laseb avatud akna kinni panna
        if event.type == pygame.QUIT:
            running = False