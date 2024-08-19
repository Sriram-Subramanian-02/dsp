import math
import random 

def encrypt(plaintext, e, n):
    return pow(plaintext, e, n)

def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

def chosen_cipher_attack(intercepted_ciphertext, e, n, bob_decrypt):
    X = random.randint(1, n-1)
    while math.gcd(X, n) != 1:
        X = random.randint(1, n-1)

    Y = (intercepted_ciphertext * pow(X, e, n)) % n
    Z = bob_decrypt(Y)
    plaintext =(Z * pow(X, -1, n)) % n

    return plaintext

def bob_decrypt(ciphertext):
    d = 103
    return decrypt(ciphertext, d, n)

# Given parameters
e = 7
n = 143
intercepted_ciphertext = 57

recovered_plaintext = chosen_cipher_attack(intercepted_ciphertext, e, n, bob_decrypt)
plaintext = 8

if recovered_plaintext == plaintext:
    print("Success..")
else:
    print("Failure..")