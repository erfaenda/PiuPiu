import threading, time

class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        i = 0
        while True:
            print('Пиьска ' + str(i))
            i = i + 1
            time.sleep(0.3)

class B(threading.Thread):
    a = 'Привет я основной поток'
    def __init__(self):
        threading.Thread.__init__(self)
        i = 1


    def starter(self):
        print('F')

if __name__ == '__main__':
    t = threading.Thread(target=A)
    t.start()
    w = threading.Thread(target=B)
    w.start()

