import pygame

windows = pygame.display.set_mode((640, 480))
pygame.display.set_caption('hello')

screen = pygame.Surface((50, 50))

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
    screen.fill((0,250,50))
    windows.blit(screen, (40, 110))
    pygame.display.flip()