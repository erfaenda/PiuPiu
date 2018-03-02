class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print('(Inisialization {0})'.format(self.name))

        Robot.population += 1

    def __del__(self):
        print('{0} self destroy'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} this is last robot'.format(self.name))
        else:
            print('Have a {0:d} worked robots'.format((Robot.population)))

    def sayHi(self):
        print('Greetings! My masters calls me {0}'.format(self.name))

    @staticmethod
    def howMany():
        print(' We have {0:d} robots'.format(Robot.population))



droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

print('\nThis is robots workout =)\n')

print('Robots ends self work. Lets destroy them all!!!')

del droid1
del droid2

Robot.howMany()
