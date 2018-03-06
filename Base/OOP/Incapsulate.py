class teen:
    def __init__(self):
        self.__age = 16


    def say(self):
        print('Мне {}'.format(self.__age))

    def say2(self):
        print('Мне {} и пиво мне уже продают'.format(self.__age))

    def setAge(self, age):
        self.__age = age
        if age >= 18:
            self.say2()
        else:
            self.say()

alex = teen()
alex.say()
alex.setAge(31)