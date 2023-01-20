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

vikklogo = pygame.image.load('vikklogo.png')
vikklogo = pygame.transform.scale(vikklogo, [320, 45])
screen.blit(vikklogo, [10, 10])
pygame.draw.line(screen, [255, 255, 255], [10, 10], [265, 10], 1)
pygame.draw.line(screen, [255, 255, 255], [10, 55], [265, 55], 1)
pygame.draw.line(screen, [255, 255, 255], [10, 10], [10, 55], 1)
pygame.draw.line(screen, [255, 255, 255], [240, 10], [240, 55], 1)
pygame.draw.arc(screen, [255, 255, 255], [228, 8, 50, 50], -3.14/3, 1)

cake = pygame.image.load('cake.png')
cake = pygame.transform.scale(cake, [100, 100])
screen.blit(cake, [400, 180])

mook = pygame.image.load('mook.png')
mook = pygame.transform.scale(mook, [38, 38])
screen.blit(mook, [390, 320])

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
