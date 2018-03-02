class SchoolMember:
    '''общее представление человека '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0}'.format(self.name))
    def tell(self):
        #вывод информации о себе
        print('Имя'))