import pygame

#инициализировал окно
windows = pygame.display.set_mode((640, 480))
#обозвал окно
pygame.display.set_caption('hello')
#создал экран для рисования
screen = pygame.Surface((640, 480))

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0))

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

penguin = Sprite(0, 0, 'penguin.png')
snake = Sprite(0, 0, 'snake.png')

penguin.go_right = True

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    # движение пенгвина
    if penguin.go_right == True:
        penguin.x += 1
        if penguin.x > 590:
            penguin.go_right = False
    else:
        penguin.x -= 1
        if penguin.x < 0:
            penguin.go_right = True

    screen.fill((0,0,0)) # закраска цветом

    # рендерим спраты
    penguin.render()
    snake.render()

    windows.blit(screen, (0, 0)) # функция отображения, задется кординатами
    pygame.display.flip() # функция показа окна, думаб что то типо show
    pygame.time.delay(1) # задержка