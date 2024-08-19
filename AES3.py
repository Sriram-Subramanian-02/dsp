from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def encrypt_text_cfb(plain_text: str, key: bytes) -> (bytes, bytes):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()

    cipher_text = encryptor.update(plain_text.encode()) + encryptor.finalize()

    return cipher_text, iv

def decrypt_text_cfb(cipher_text: bytes, iv: bytes, key: bytes) -> str:
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    decryptor = cipher.decryptor()

    plain_text = decryptor.update(cipher_text) + decryptor.finalize()

    return plain_text.decode()

if __name__ == "__main__":
    key = os.urandom(32)  # 256-bit key for AES
    plain_text = "XXAABBXXAABB"
    cipher_text, iv = encrypt_text_cfb(plain_text, key)
    print(f"Encrypted (CFB): {cipher_text}")
    decrypted_text = decrypt_text_cfb(cipher_text, iv, key)
    print(f"Decrypted (CFB): {decrypted_text}")
