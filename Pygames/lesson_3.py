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

def Intersec(x1, x2, y1, y2):
    if (x1 > x2-50) and (x1 < x2+50) and (y1 < y2+50):
        return 1
    else:
        return 0

penguin = Sprite(300, 430, 'penguin.png')
snake = Sprite(300, 0, 'snake.png')
penguin.up = True
snake.down = True

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    screen.fill((0, 0, 0))  # закраска цветом

    # движение
    if penguin.up == True:
        penguin.y -= 1
        if penguin.y == 0:
            penguin.up = False
    else:
        penguin.y += 1
        if penguin.y == 430:
            penguin.up = True

    if snake.down == True:
        snake.y += 1
        if snake.y == 430:
            snake.down = False
    else:
        snake.y -= 1
        if snake.y == 0:
            snake.down = True

    if Intersec(snake.x, penguin.x, snake.y, penguin.y) == True:
       penguin.up = True
       snake.down = True

    # рендерим спраты
    penguin.render()
    snake.render()

    windows.blit(screen, (0, 0)) # функция отображения, задется кординатами
    pygame.display.flip() # функция показа окна, думаб что то типо show
    pygame.time.delay(3) # задержка