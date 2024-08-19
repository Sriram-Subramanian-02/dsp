from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

def encrypt_text(plain_text: str, key: bytes) -> (bytes, bytes):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plain_text.encode()) + padder.finalize()
    cipher_text = encryptor.update(padded_data) + encryptor.finalize()

    return cipher_text, iv

def decrypt_text(cipher_text: bytes, iv: bytes, key: bytes) -> str:
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()

    padded_plain_text = decryptor.update(cipher_text) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plain_text = unpadder.update(padded_plain_text) + unpadder.finalize()

    return plain_text.decode()

if __name__ == "__main__":
    key = os.urandom(32)
    plain_text = "This is a secret message."
    cipher_text, iv = encrypt_text(plain_text, key)
    print(f"Encrypted: {cipher_text}")
    decrypted_text = decrypt_text(cipher_text, iv, key)
    print(f"Decrypted: {decrypted_text}")
