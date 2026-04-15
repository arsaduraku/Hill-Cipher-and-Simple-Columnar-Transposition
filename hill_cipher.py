# HILL CIPHER - ALGORITMI I ENKRIPTIMIT ME MATRICË


def text_to_numbers(text):
    """
    Kthen çdo shkronjë në numër: A=0, B=1, ..., Z=25
    """
    text = text.upper().replace(" ", "")  # Bëjmë shkronjat e mëdha dhe heqim hapësirat
    numbers = []
    for char in text:
        # ord('A') = 65, kështu që 'A' - 65 = 0
        numbers.append(ord(char) - ord('A'))
    return numbers

def numbers_to_text(numbers):
    """
    Kthen numrat përsëri në shkronja: 0=A, 1=B, ...
    """
    text = ""
    for num in numbers:
        text += chr(num + ord('A'))  # 0+65='A', 1+65='B', etj.
    return text