import itertools
import time

def single_encrypt(message, key):
    message = message.replace(" ", "")
    num_rows = -(-len(message) // len(key))
    grid = [["" for _ in range(len(key))] for _ in range(num_rows)]
    
    message_index = 0
    for row in range(num_rows):
        for col in range(len(key)):
            if message_index < len(message):
                grid[row][col] = message[message_index]
                message_index += 1
    
    ciphertext = ''
    for k in sorted(set(key)):
        col = key.index(k)
        for row in range(num_rows):
            if grid[row][col]:
                ciphertext += grid[row][col]
    
    return ciphertext

def double_transposition(message, key):
    first_encryption = single_encrypt(message, key)
    second_encryption = single_encrypt(first_encryption, key)
    return second_encryption
    
message = "Enemy attacks tonight"
key = "31452"
double_transposition(message, key)