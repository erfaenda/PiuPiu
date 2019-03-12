from cryptography.fernet import Fernet
import transliterate

#cipher_key = Fernet.generate_key() # это сгенерирует новый ключ

CHIPER_KEY = 'APM1JDVgT8WDGOWBgQv6EIhvxl4vDYvUnVdg-Vjdt0o=' # ключ который я сгенерил в открытом виде
cipher = Fernet(CHIPER_KEY)
rawtext = 'Короче теперь можно делать все что угодно лалала крутотень'
text = transliterate.translit(rawtext, reversed=True)
ntext = bytes(text, 'utf8')
print(ntext)
encrypted_text = cipher.encrypt(ntext)

def write_dat(encrypted_text):
    handle = open("encrypted.bin", "wb")
    handle.write(encrypted_text)
    handle.close()
    print(encrypted_text)

def read_dat():
    handle = open("encrypted.bin", "rb")
    decrypt_data = handle.read()
    data = cipher.decrypt(decrypt_data).decode('utf8')
    handle.close()
    return data

write_dat(encrypted_text)
print(read_dat())


