import hashlib

class PasswdManipulation():
    def makeThisShit(self, newpassword):
        #randomka = randrange(1, 9)
        passwdd = newpassword.encode('utf-8')
        hash = hashlib.md5(passwdd)
        p = hash.hexdigest()
        print("Новый хэш пароля: " + p)
        handle = open("password.txt", "w")
        handle.write(p)
        handle.close()
        return p

    def checkPasswd(self, passwd):
        passwdd = passwd.encode('utf-8')
        hashTruepass = hashlib.md5(passwdd)
        handle = open("password.txt", "r")
        data = handle.readline()#.split[:-1]
        handle.close()
        FPass = hashTruepass.hexdigest()
        if FPass == data:
            print("Совпали, входим")
            return 'Совпадение заходим'
        else:
            print("Пароль не верный, дозззвидули")
            return 'Неверный пароль'
