i = 10
for i in range(1,10):
    print(i)
    i = i + 1
    text_for_file = i
    my_file = open('snake.txt', 'w')
    my_file.write(str(text_for_file))

    my_file.close()

