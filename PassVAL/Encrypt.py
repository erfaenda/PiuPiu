from cryptography.fernet import Fernet
import transliterate

#cipher_key = Fernet.generate_key() # это сгенерирует новый ключ

# класс отвечает за перевод рус в транслит, шифроку запись в файл и рашифровку
class Encription():
    # ключ которым будет все шифроваться
    CHIPER_KEY = 'APM1JDVgT8WDGOWBgQv6EIhvxl4vDYvUnVdg-Vjdt0o=' # ключ который я сгенерил в открытом виде
    CHIPER = Fernet(CHIPER_KEY)

    def encrypt_trans(self, rawtext):
        #rawtext = 'Короче теперь можно делать все что угодно лалала крутотень'
        text = transliterate.translit(rawtext, reversed=True)
        ntext = bytes(text, 'utf8')
        print(ntext)
        encrypted_text = self.CHIPER.encrypt(ntext)
        print("это зашифрованый текст " + str(encrypted_text))
        return encrypted_text

    def write_dat(self, encrypted_text):
        handle = open("encrypted.bin", "wb")
        handle.write(encrypted_text)
        handle.close()
        print(encrypted_text)

    def read_dat(self):
        handle = open("encrypted.bin", "rb")
        decrypt_data = handle.read()
        data = self.CHIPER.decrypt(decrypt_data).decode('utf8')
        fdata = transliterate.translit(data, 'ru')
        print(fdata)
        handle.close()
        return fdata

    #write_dat(encrypted_text)
    #print(read_dat())

if __name__ == "__main__":
    app = Encription()
    app.write_dat(app.encrypt_trans('Прорssdf1'))
    app.read_dat()
