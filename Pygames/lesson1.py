import pygame

#инициализировал окно
windows = pygame.display.set_mode((640, 480))
#обозвал окно
pygame.display.set_caption('hello')
#создал экран для рисования
screen = pygame.Surface((640, 480))
square = pygame.Surface((50, 50)) # область для рисования в моем случае это объект

square_go_right = True # рычаг
x = 0

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    screen.fill((0,0,0)) # закраска цветом
    square.fill((0, 250, 10))

    if square_go_right == True:
        x += 3
        if x > 590:
            square_go_right = False
    else:
        x -= 3
        if x < 1:
            square_go_right = True


    windows.blit(screen, (0, 0)) # функция отображения, задется кординатами
    windows.blit(square, (x, 150))
    pygame.display.flip() # функция показа окна, думаб что то типо show
    pygame.time.delay(1) # задержка 