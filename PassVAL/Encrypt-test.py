from cryptography.fernet import Fernet

#cipher_key = Fernet.generate_key()

CHIPER_KEY = 'APM1JDVgT8WDGOWBgQv6EIhvxl4vDYvUnVdg-Vjdt0o='
cipher = Fernet(CHIPER_KEY)
text = b'Kakoito super puper text 4to takoe'
encrypted_text = cipher.encrypt(text)

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


