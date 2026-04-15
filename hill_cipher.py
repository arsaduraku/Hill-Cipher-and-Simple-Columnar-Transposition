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