import threading
import  time

class infinityComand(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self)
        self.n = n
        stroka =''
        while True:
            n = n + 1
            #"Команда выполняется уже " + str(n) + ' раз')
            stroka = "Команда выполняется уже " + str(n) + ' раз'
            time.sleep(1)

def main():
    t = threading.Thread(target=infinityComand)
    t.start()

    i = 10
    for i in range(0, 1000):
        time.sleep(0.3)
        print('Основа')
        print()

main()