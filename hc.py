# PROGRAMI KRYESOR 

from hill_cipher import hill_encrypt, hill_decrypt
from sct import columnar_encrypt, columnar_decrypt

def main():
    print("   PROJEKT - Siguri e te dhenave")
    print("-----------------------------------------------")
    print("\nKy program implementon dy algoritme kriptografike:")
    print("1. Hill Cipher - Enkriptim me matrica")
    print("2. Columnar Transposition - Riorganizim i shkronjave")
    print("------------------------------------------------------")
    
    while True:
        print("\n--- ALGORITMET ---")
        print("1. Perdor Hill Cipher")
        print("2. Perdor Columnar Transposition")
        print("0. Dil nga programi")
        
        choice = input("\nZgjidhni (0-2): ")
        
        if choice == '0':
            print("\nFaleminderit! Mirupafshim!")
            break
            
        elif choice == '1':
            # HILL CIPHER
            print("\n--- HILL CIPHER ---")
            print("Çelesi i paracaktuar eshte matrica: [[3, 3], [2, 5]]")
            
            text = input("Shkruani tekstin qe doni te perpunoni: ")
            
            # Matrica çeles
            key = [[3, 3], [2, 5]]
            
            print("\n1. Enkripto")
            print("2. Dekripto")
            option = input("Zgjidhni (1 ose 2): ")
            
            if option == '1':
                result = hill_encrypt(text, key)
                print(f"\nTeksti origjinal: {text}")
                print(f"Teksti i enkriptuar: {result}")
            elif option == '2':
                result = hill_decrypt(text, key)
                print(f"\nTeksti i enkriptuar: {text}")
                print(f"Teksti i dekriptuar: {result}")
            else:
                print("Opsion i gabuar!")
                
        elif choice == '2':
            # COLUMNAR TRANSPOSITION
            print("\n--- COLUMNAR TRANSPOSITION ---")
            
            text = input("Shkruani tekstin qe doni: ")
            
            try:
                columns = int(input("Numri i kolonave (p.sh. 3, 4, 5): "))
            except:
                columns = 4
                print("Perdoret numri i paracaktuar: 4 kolona")
            
            print("\n1. Enkripto")
            print("2. Dekripto")
            option = input("Zgjidhni (1 ose 2): ")
            
            if option == '1':
                result = columnar_encrypt(text, columns)
                print(f"\nTeksti origjinal: {text}")
                print(f"Teksti i enkriptuar: {result}")
            elif option == '2':
                result = columnar_decrypt(text, columns)
                print(f"\nTeksti i enkriptuar: {text}")
                print(f"Teksti i dekriptuar: {result}")
            else:
                print("Opsion i gabuar!")
                   
        else:
            print("Opsion i pavlefshem! Zgjidhni 0-2.")
            
# EKZEKUTIMI I PROGRAMIT
if __name__ == "__main__":
    main()