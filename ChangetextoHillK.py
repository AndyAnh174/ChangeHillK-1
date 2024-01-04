import numpy as np

def encrypt_hill_cipher(plaintext, key_matrix):
    text_numbers = [ord(char) - ord('A') for char in plaintext]
    n = len(key_matrix)

    while len(text_numbers) % n != 0:
        text_numbers.append(ord('X') - ord('A'))

    text_blocks = [text_numbers[i:i + n] for i in range(0, len(text_numbers), n)]

    encrypted_text = ""    
    for block in text_blocks:
        encrypted_block = np.dot(key_matrix, block) % 26
        encrypted_text += ''.join([chr(char + ord('A')) for char in encrypted_block])

    return encrypted_text

plaintext = "HOWDOYOUKNOW"
key_matrix = np.array([[8, 2], [3, 1]])

encrypted_text = encrypt_hill_cipher(plaintext, key_matrix)
print("TEXT:", encrypted_text)
