class phone:
    def __init__(self):
        self.model = ''
        self.color = ''

    def call(self):
        print('Call is it')

class phone2(phone):
    def __init__(self):
        phone.__init__(self)

    def sendMail(self):
        print('Email be send')

p = phone2()
p.call()
p.sendMail()