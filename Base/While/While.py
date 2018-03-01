num = 23
run = True

while run:
    guess = int(input('Введите число: '))

    if guess == num:
        print('Гриитингз май френд')
        run = False
    elif guess < num:
        print('Загаданное число больше вашего.')
    else:
        print('Загаданное число меньше вашего.')
else:
    print('Цикл while закончен')
print('Terminate')