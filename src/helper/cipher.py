from .Encrypter import Encrypter
from .Decrypter import Decrypter

def encrypt_aes(cipher, key):
    x = Encrypter(cipher, key)
    cipher = x.encrypt_image()
    return cipher


def decrypt_aes(cipher, key):
    x = Decrypter(cipher)
    plain = x.decrypt_image(key)
    return plain
