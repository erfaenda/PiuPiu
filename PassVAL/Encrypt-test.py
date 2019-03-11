from Crypto.Cipher import DES

key = b'abcdefgh'

def pad(text):
    while len(text) % 64 != 0:
        text += b' '
    return text

des = DES.new(key, DES.MODE_ECB)
text = b'Pizdaebanyasushami loh'
padded_text = pad(text)

encrypted_text = des.encrypt(padded_text)
handle = open("encrypted.bin", "wb")
handle.write(encrypted_text)
handle.close()
#print(encrypted_text)

data = des.decrypt(encrypted_text)
#print(data) # Python rocks!

handle = open("encrypted.bin", "rb")
decrypt_data = handle.read()
print(des.decrypt(decrypt_data))
handle.close()
