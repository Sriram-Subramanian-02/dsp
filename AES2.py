from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

def encrypt_text_ecb(plain_text: str, key: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plain_text.encode()) + padder.finalize()
    cipher_text = encryptor.update(padded_data) + encryptor.finalize()

    return cipher_text

def decrypt_text_ecb(cipher_text: bytes, key: bytes) -> str:
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()

    padded_plain_text = decryptor.update(cipher_text) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plain_text = unpadder.update(padded_plain_text) + unpadder.finalize()

    return plain_text.decode()

if __name__ == "__main__":
    key = os.urandom(32)  # 256-bit key for AES
    plain_text = "This is a secret message."
    cipher_text = encrypt_text_ecb(plain_text, key)
    print(f"Encrypted (ECB): {cipher_text}")
    decrypted_text = decrypt_text_ecb(cipher_text, key)
    print(f"Decrypted (ECB): {decrypted_text}")
