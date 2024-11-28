from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
from Utils.constants import *

def aes_descrypt(encrypted_data, key, iv):
    encrypted_data=base64.b64decode(encrypted_data)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    return decrypted_data.decode("utf-8")

def decrypt(encrypted_data):
    try:
        iv = base64.b64decode(prod_encryption_iv)
        key = base64.b64decode(prod_encryption_key)
        return aes_descrypt(encrypted_data, key, iv)
    except:
        iv = base64.b64decode(dev_encryption_iv)
        key = base64.b64decode(dev_encryption_key)
        return aes_descrypt(encrypted_data, key, iv)        



    



