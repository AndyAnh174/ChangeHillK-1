import numpy as np

def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    return ''.join([chr(num + ord('A')) for num in numbers])

def pad_text(text, block_size):
    padding = (block_size - len(text) % block_size) % block_size
    return text + 'X' * padding

def get_key_matrix():
    try:
        print("Nhập ma trận khóa K:")
        rows = int(input("Số hàng: "))
        cols = int(input("Số cột: "))
        key_matrix = []

        print("Nhập giá trị cho từng phần tử của ma trận:")
        for i in range(rows):
            row = []
            for j in range(cols):
                element = int(input(f"K[{i+1},{j+1}]: "))
                row.append(element)
            key_matrix.append(row)

        return np.array(key_matrix)

    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên cho từng phần tử của ma trận.")
        return get_key_matrix()

def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    matrix_mod_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)) % modulus
    return matrix_mod_inv

def hill_cipher_decode(encoded_text, key_matrix):
    block_size = len(key_matrix)
    key_matrix_inv = matrix_mod_inv(key_matrix, 26)

    numbers = text_to_numbers(encoded_text)
    vectors = [numbers[i:i+block_size] for i in range(0, len(encoded_text), block_size)]

    decoded_vectors = []
    for vector in vectors:
        vector = np.array(vector)
        decoded_vector = np.dot(key_matrix_inv, vector) % 26
        decoded_vectors.extend(decoded_vector)

    decoded_text = numbers_to_text(decoded_vectors)

    return decoded_text


encoded_text = input("Nhập văn bản cần giải mã: ").upper()
key_matrix = get_key_matrix()


decoded_text = hill_cipher_decode(encoded_text, key_matrix)
print("Văn bản đã giải mã:", decoded_text)
