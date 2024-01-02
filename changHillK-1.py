import numpy as np
from sympy import Matrix
def inverse_modulo(det, m):

    for i in range(1, m):
        if (det * i) % m == 1:
            return i
    return None

def decrypt_hill_cipher(ciphertext, key_matrix):

    det = int(round(Matrix(key_matrix).det()))
    mod_inverse = inverse_modulo(det, 26)

    if mod_inverse is None:
        print("cant nghịch đảo modulo, cant giải mã.")
        return


    inverse_matrix = Matrix(key_matrix).inv_mod(26)

    decrypted_text = ""
    n = len(key_matrix)

    for i in range(0, len(ciphertext), n):
        block = ciphertext[i:i+n]
        encrypted_block = np.dot(inverse_matrix, [ord(char) - ord('A') for char in block]) % 26
        decrypted_text += ''.join([chr(char + ord('A')) for char in encrypted_block])

    return decrypted_text


ciphertext = "HVQMIQEFNA"
key_matrix = [[2, 3], [3, 6]]

decrypted_text = decrypt_hill_cipher(ciphertext, key_matrix)
print("TEST THANH =>", decrypted_text)
