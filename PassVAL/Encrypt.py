from cryptography.fernet import Fernet
import transliterate, csv
from transliterate import detect_language


#cipher_key = Fernet.generate_key() # это сгенерирует новый ключ

# класс отвечает за перевод рус в транслит, шифроку запись в файл и рашифровку
# как выяснилось можно шифровать и русские символы, главное перевести в байты
# часть функции не актуальна
class Encription():
    FILENAME = "test_csv.csv"
    # ключ которым будет все шифроваться
    CHIPER_KEY = 'APM1JDVgT8WDGOWBgQv6EIhvxl4vDYvUnVdg-Vjdt0o=' # ключ который я сгенерил в открытом виде
    CHIPER = Fernet(CHIPER_KEY)

    def encrypt_trans(self, rawtext):
        for i in rawtext:
            # нельзя определить язык лишь по одному символу по этому i+i
            if detect_language(i + i) == 'ru':
                print('ru')
                #text = transliterate.translit(rawtext, reversed=True)
                text = rawtext
                btext = bytes(text, 'utf8')
            else:
                print('en')
                btext = bytes(rawtext, 'utf8')
            encrypted_text_bytes = self.CHIPER.encrypt(btext)
            encrypted_text_string = encrypted_text_bytes.decode('utf8')
            print("это зашифрованый текст " + str(encrypted_text_bytes))
            print("Читый текст тут " + encrypted_text_string)
        return encrypted_text_string

    def write_dat(self, encrypted_text):
        handle = open("encrypted.bin", "wb")
        handle.write(encrypted_text)
        handle.close()
        print(encrypted_text)

    def read_dat(self):
        handle = open("encrypted.bin", "rb")
        decrypt_data = handle.read()
        data = self.CHIPER.decrypt(decrypt_data).decode('utf8')
        #fdata = transliterate.translit(data, 'ru')
        print(data)
        handle.close()
        return data

    def decrypt(self, encrypt_data):
        decrypt_data = self.CHIPER.decrypt(encrypt_data).decode('utf8')
        return decrypt_data


    #write_dat(encrypted_text)
    #print(read_dat())

if __name__ == "__main__":
    app = Encription()
    app.write_dat(app.encrypt_trans('A112'))
    app.read_dat()
