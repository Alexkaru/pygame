# Alex Karu
import pygame  # impordib pygami

pygame.init()
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption('2')

bg = pygame.image.load('bg_shop.jpg')
screen.blit(bg, [0, 0])

seller = pygame.image.load('seller.png')
seller = pygame.transform.scale(seller, [265, 308])
screen.blit(seller, [100, 155])

chat = pygame.image.load('chat.png')
chat = pygame.transform.scale(chat, [250, 200])
screen.blit(chat, [250, 70])

vikklogo = pygame.image.load('vikklogo2.jpg')
vikklogo = pygame.transform.scale(vikklogo, [300, 50])
screen.blit(vikklogo, [0, 0])

font = pygame.font.Font(pygame.font.match_font('Times New Roman'), 20)
text = font.render("Tere, olen Alex Karu", True, [255, 255, 255])
text_width = text.get_rect().width
text_height = text.get_rect().height
screen.blit(text, [300-text_width/10, 150-text_height/5])


pygame.display.flip()
# jätab avatud akna ekraanile
running = True
while running:
    for event in pygame.event.get():
        # laseb avatud akna kinni panna
        if event.type == pygame.QUIT:
            running = False
