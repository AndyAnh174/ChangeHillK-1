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

def hill_cipher_encode(text, key_matrix):

    numbers = text_to_numbers(text)


    block_size = len(key_matrix)
    padded_text = pad_text(text, block_size)

    vectors = [numbers[i:i+block_size] for i in range(0, len(padded_text), block_size)]


    encoded_vectors = []
    for vector in vectors:
        vector = np.array(vector)
        encoded_vector = np.dot(key_matrix, vector) % 26
        encoded_vectors.extend(encoded_vector)


    encoded_text = numbers_to_text(encoded_vectors)

    return encoded_text


plaintext = input("Nhập văn bản cần mã hóa: ").upper()
key_matrix = get_key_matrix()

encoded_text = hill_cipher_encode(plaintext, key_matrix)
print("Văn bản gốc:", plaintext)
print("Văn bản mã hóa:", encoded_text)
