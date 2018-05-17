from threading import Thread

def f():
    for i in range(3):
        print('Я из функции f и я несу ', i)


def f_2():
    for i in range(3):
        print('Я из функции f_2 и я несу ', i)

th_1, th_2 = Thread(target=f), Thread(target = f_2)

if __name__ == '__main__':
    th_1.start(), th_2.start()
    th_1.join(), th_2.join()