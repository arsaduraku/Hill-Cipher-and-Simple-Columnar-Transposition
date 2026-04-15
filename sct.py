# COLUMNAR TRANSPOSITION - TRANSPOZIMI KOLONAR

def columnar_encrypt(plaintext, num_columns):
    """
    ENKRIPTIMI
    """

    # Hapi 1: Përgatisim tekstin
    plaintext = plaintext.replace(" ", "").upper()
    length = len(plaintext)

    # Hapi 2: Llogarisim numrin e rreshtave
    num_rows = (length + num_columns - 1) // num_columns

    # Hapi 3: Krijojmë tabelën
    table = []
    index = 0

    for row in range(num_rows):
        table_row = []
        for col in range(num_columns):
            if index < length:
                table_row.append(plaintext[index])
            else:
                table_row.append('X')
            index += 1
        table.append(table_row)

    # Shfaqim tabelën
    print("\nTabela e krijuar:")
    print("-" * (num_columns * 4))
    for row in table:
        print("| " + " | ".join(row) + " |")
    print("-" * (num_columns * 4))

    # Hapi 4: Lexojmë kolonat
    ciphertext = ""

    for col in range(num_columns):
        for row in range(num_rows):
            ciphertext += table[row][col]

    return ciphertext


def columnar_decrypt(ciphertext, num_columns):
    """
    DEKRIPTIMI
    """

    ciphertext = ciphertext.replace(" ", "").upper()
    length = len(ciphertext)

    # Llogarisim rreshtat
    num_rows = (length + num_columns - 1) // num_columns

    # Krijojmë tabelën boshe
    table = [['' for _ in range(num_columns)]
             for _ in range(num_rows)]

    # Mbushim kolonat
    index = 0

    for col in range(num_columns):
        for row in range(num_rows):
            if index < length:
                table[row][col] = ciphertext[index]
                index += 1

    # Shfaqim tabelën
    print("\nTabela e rikrijuar:")
    print("-" * (num_columns * 4))
    for row in table:
        print("| " + " | ".join(row) + " |")
    print("-" * (num_columns * 4))

    # Lexojmë rreshtat
    plaintext = ""

    for row in range(num_rows):
        for col in range(num_columns):
            plaintext += table[row][col]

    return plaintext.rstrip('X')


# ===== TESTIMI =====

if __name__ == "__main__":

    print("__________________________________")
    print("TESTIMI I COLUMNAR TRANSPOSITION")
    print("__________________________________")

    text = "Siguria e Te Dhenave"
    columns = 5

    print(f"Teksti origjinal: {text}")
    print(f"Numri i kolonave: {columns}")

    encrypted = columnar_encrypt(text, columns)

    print("\nTeksti i enkriptuar:", encrypted)

    decrypted = columnar_decrypt(encrypted, columns)

    print("Teksti i dekriptuar:", decrypted)