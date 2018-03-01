number = 23
guess = int(input('Введите число : '))

if guess == number:
    print('Поздравляю, вы угадали, ')
    print('Но призовые я пропил :)')
elif guess < number:
    print('Загаданное число больше вашего.')
else:
    print('Загаданное число меньше вашего.')

print('Завершение!')
