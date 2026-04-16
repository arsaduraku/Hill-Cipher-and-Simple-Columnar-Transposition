# HILL CIPHER

def text_to_numbers(text):
    text = text.upper().replace(" ", "") 
    numbers = []
    for char in text:
        numbers.append(ord(char) - ord('A'))
    return numbers

def numbers_to_text(numbers):
    text = ""
    for num in numbers:
        text += chr(num + ord('A')) 
    return text

def multiply_matrix_vector(matrix, vector):
    result = []

    r1 = (matrix[0][0] * vector[0] + matrix[0][1] * vector[1]) % 26
    r2 = (matrix[1][0] * vector[0] + matrix[1][1] * vector[1]) % 26
    result.append(r1)
    result.append(r2)
    
    return result

def find_determinant(matrix):
    return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None  

def matrix_inverse_2x2(matrix, modulus=26):

    det = find_determinant(matrix)
    det_inv = mod_inverse(det, modulus)
    
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]
    
    inverse = [
        [(d * det_inv) % modulus, (-b * det_inv) % modulus],
        [(-c * det_inv) % modulus, (a * det_inv) % modulus]
    ]
    return inverse

def hill_encrypt(plaintext, key_matrix):
    #1
    numbers = text_to_numbers(plaintext)
    
    #2
    if len(numbers) % 2 != 0:
        numbers.append(23)
    
    #3
    encrypted_numbers = []
    for i in range(0, len(numbers), 2):  
        # Marrim dy numra
        pair = [numbers[i], numbers[i+1]]
        # Shumezojme me matricen
        encrypted_pair = multiply_matrix_vector(key_matrix, pair)
        # Shtojme ne liste
        encrypted_numbers.extend(encrypted_pair)
    
    #4
    return numbers_to_text(encrypted_numbers)

def hill_decrypt(ciphertext, key_matrix):

    #1
    inverse_matrix = matrix_inverse_2x2(key_matrix)
    
    #2
    numbers = text_to_numbers(ciphertext)
    
    #3
    decrypted_numbers = []
    for i in range(0, len(numbers), 2):
        pair = [numbers[i], numbers[i+1]]
        decrypted_pair = multiply_matrix_vector(inverse_matrix, pair)
        decrypted_numbers.extend(decrypted_pair)
    
    #4
    return numbers_to_text(decrypted_numbers)

# TESTIMI 
if __name__ == "__main__":
    print("----------------------------------")
    print("TESTIMI I HILL CIPHER")
    print("----------------------------------")
    
    key = [[3, 3], [2, 5]]
    
    print(f"Matrica çelës: {key}")
    print(f"Determinanti: {find_determinant(key)}")
    
    text = "DATA SECURITY"
    print(f"\nTeksti origjinal: {text}")
    
    encrypted = hill_encrypt(text, key)
    print(f"Teksti i enkriptuar: {encrypted}")
    
    decrypted = hill_decrypt(encrypted, key)
    print(f"Teksti i dekriptuar: {decrypted}")