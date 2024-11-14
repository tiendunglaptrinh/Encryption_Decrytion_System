import textwrap
from caesar_cipher import CaesarCipher
from rail_fence_cipher import RailFenceCipher
from multiple_caesar_railfence_cipher import MultipleCaesarRailFence
from random_ciphertext import RandomCiphertext

def run_caesar_cipher(plaintext: str, key: int):
    caesar_cipher_obj = CaesarCipher(key=key)
    encrypted_text = caesar_cipher_obj.encrypt(plaintext)
    decrypted_text = caesar_cipher_obj.decrypt(encrypted_text)
    
    print('----------------------------------------------------------------------------------------------------')
    print("Caesar Cipher is running...")
    print("Ciphertext: ", encrypted_text)
    print("Plaintext: ", decrypted_text)
    
def run_rail_fence_cipher(plaintext: str, rails: int):
    rail_fence_cipher_obj = RailFenceCipher(rails=rails)
    encrypted_text = rail_fence_cipher_obj.encrypt(plaintext)
    decrypted_text = rail_fence_cipher_obj.decrypt(encrypted_text)
    
    print('----------------------------------------------------------------------------------------------------')
    print("Rail Fence is running...")
    print("Ciphertext: ", encrypted_text)
    print("Plaintext: ", decrypted_text)
    
def run_multiple_caesar_railfence_cipher(plaintext: str, caesar_key: int,  rails_rail_fence: int):
    caesar_rail_fence_cipher_obj = MultipleCaesarRailFence(caesar_key=caesar_key, rails_rail_fence=rails_rail_fence)
    encrypted_text = caesar_rail_fence_cipher_obj.encrypt(plaintext)
    decrypted_text = caesar_rail_fence_cipher_obj.decrypt(encrypted_text)
    
    print('----------------------------------------------------------------------------------------------------')
    print("Multiple Caesar and Rail fence is running...")
    print("Ciphertext: ", encrypted_text)
    print("Plaintext: ", decrypted_text)
    
def main():
    #  plaintext = "HELLO EVERYONE, TODAY I WILL RESEARCH ABOUT TWO METHODS ECRYPTION AND DECRYPTION. THERE ARE CAESAR CIPHER AND RAIL FENCE CIPHER."
    #  plaintext = "GeeksforGeeks"
    #  plaintext = "JhhnviruJhhnv"
    print("------------------------------------------------------------------")
    print("|         A PROGRAMMING ENCRYPTION AND DECRYPTION                |")
    print("------------------------------------------------------------------")
    print("|                                                                |")
    print("|      CHOOSING YOUR OPTION BELOW                                |")
    print("| 1. CASESAR CIPHER                                              |")
    print("| 2. RAIL FENCE CIPHER                                           |")
    print("| 3. MULTIPLE CAESAR AND RAIL FENCE CIPHER                       |")
    print("| 4. CREATE A RANDOM PLAINTEXT                                   |")
    print("|                                                                |")
    print("------------------------------------------------------------------")
    option = int(input("|     YOUR OPTION IS:                                         | ",))
    print("------------------------------------------------------------------")
    if option == 1:
        print("|   CASAESAR CIPHER IS RUNNING...                                |")
        print("|                                                                |")
        print("|   CHOOSING YOUR OPTION BELOW:                                  |")
        print("| 1. ENCRYPTION                                                  |")
        print("| 2. DECRYPTION                                                  |")
        print("|                                                                |")
        print("------------------------------------------------------------------")
        func_value = int(input("|   YOUR OPTION IS:                                           | ",))
        if func_value == 1:
            print("------------------------------------------------------------------")
            plaintext = input("|   ENTER YOUR PLAINTEXT FOR THE ENCRYPTION: ",)
            key = int(input("|   ENTER YOUR KEY FOR THE ENCRYPTION: ",))
            caesar_obj = CaesarCipher(key)
            text_decrypted = caesar_obj.encrypt(plaintext)
            wrapped_text = textwrap.fill(text_decrypted, width=50)  # width là độ dài mỗi dòng
            print("------------------------------------------------------------------")
            print("|                                                                |")
            print("|           ------------RESULT CIPHERTEXT-----------             |")
            print("|                                                                |")
            for line in wrapped_text.splitlines():
                print(f"|    {line:<59} |")  # In từng dòng với độ rộng khung là 60 ký tự
            print("|                                                                |")
            print("------------------------------------------------------------------")
        elif func_value == 2:
            print("------------------------------------------------------------------")
            ciphertext = input("|   ENTER YOUR CIPHERTEXT FOR THE DECRYPTION: ",)
            key = int(input("|   ENTER YOUR KEY FOR THE DECRYPTION: ",))
            caesar_obj = CaesarCipher(key)
            text_encrypted = caesar_obj.decrypt(ciphertext)
            wrapped_text = textwrap.fill(text_encrypted, width=50)  # width là độ dài mỗi dòng
            print("------------------------------------------------------------------")
            print("|                                                                |")
            print("|           ------------RESULT PLAINTEXT-----------              |")
            print("|                                                                |")
            for line in wrapped_text.splitlines():
                print(f"|    {line:<59} |")  # In từng dòng với độ rộng khung là 60 ký tự
            print("|                                                                |")
            print("------------------------------------------------------------------")
            
    elif option == 2:
        print("|   RAIL FENCE CIPHER IS RUNNING...                              |")
        print("|                                                                |")
        print("|   CHOOSING YOUR OPTION BELOW:                                  |")
        print("| 1. ENCRYPTION                                                  |")
        print("| 2. DECRYPTION                                                  |")
        print("|                                                                |")
        print("------------------------------------------------------------------")
        func_value = int(input("|   YOUR OPTION IS:                                           | ",))
        if func_value == 1:
            print("------------------------------------------------------------------")
            plaintext = input("|   ENTER YOUR PLAINTEXT FOR THE ENCRYPTION: ",)
            rails = int(input("|   ENTER YOUR RAILS FOR THE ENCRYPTION: ",))
            railfence_obj = RailFenceCipher(rails)
            text_decrypted = railfence_obj.encrypt(plaintext)
            wrapped_text = textwrap.fill(text_decrypted, width=50)  # width là độ dài mỗi dòng
            print("------------------------------------------------------------------")
            print("|                                                                |")
            print("|           ------------RESULT CIPHERTEXT-----------             |")
            print("|                                                                |")
            for line in wrapped_text.splitlines():
                print(f"|    {line:<59} |")  # In từng dòng với độ rộng khung là 60 ký tự
            print("|                                                                |")
            print("------------------------------------------------------------------")
        elif func_value == 2:
            print("------------------------------------------------------------------")
            ciphertext = input("|   ENTER YOUR CIPHERTEXT FOR THE DECRYPTION: ",)
            rails = int(input("|   ENTER YOUR RAILS FOR THE ENCRYPTION: ",))
            railfence_obj = RailFenceCipher(rails)
            text_encrypted = railfence_obj.decrypt(ciphertext)
            wrapped_text = textwrap.fill(text_encrypted, width=50)  # width là độ dài mỗi dòng
            print("------------------------------------------------------------------")
            print("|                                                                |")
            print("|           ------------RESULT PLAINTEXT-----------              |")
            print("|                                                                |")
            for line in wrapped_text.splitlines():
                print(f"|    {line:<59} |")  # In từng dòng với độ rộng khung là 60 ký tự
            print("|                                                                |")
            print("------------------------------------------------------------------")
            
    elif option == 3:
        print("|   MULTIPLE CAESAR AND RAIL FENCE CIPHER IS RUNNING...          |")
        print("|                                                                |")
        print("|   CHOOSING YOUR OPTION BELOW:                                  |")
        print("| 1. ENCRYPTION                                                  |")
        print("| 2. DECRYPTION                                                  |")
        print("|                                                                |")
        print("------------------------------------------------------------------")
        func_value = int(input("|   YOUR OPTION IS:                                           | ",))
        if func_value == 1:
            print("------------------------------------------------------------------")
            plaintext = input("|   ENTER YOUR PLAINTEXT FOR THE ENCRYPTION: ",)
            key = int(input("|   ENTER YOUR KEY FOR THE ENCRYPTION: ",))
            rails = int(input("|   ENTER YOUR RAILS FOR THE ENCRYPTION: ",))
            multiple_obj = MultipleCaesarRailFence(key, rails)
            text_decrypted = multiple_obj.encrypt(plaintext)
            wrapped_text = textwrap.fill(text_decrypted, width=50)  # width là độ dài mỗi dòng
            print("------------------------------------------------------------------")
            print("|                                                                |")
            print("|           ------------RESULT CIPHERTEXT-----------             |")
            print("|                                                                |")
            for line in wrapped_text.splitlines():
                print(f"|    {line:<59} |")  # In từng dòng với độ rộng khung là 60 ký tự
            print("|                                                                |")
            print("------------------------------------------------------------------")
        elif func_value == 2:
            print("------------------------------------------------------------------")
            ciphertext = input("|   ENTER YOUR CIPHERTEXT FOR THE DECRYPTION: ",)
            key = int(input("|   ENTER YOUR KEY FOR THE DECRYPTION: ",))
            rails = int(input("|   ENTER YOUR RAILS FOR THE DECRYPTION: ",))
            multiple_obj = MultipleCaesarRailFence(key, rails)
            text_encrypted = multiple_obj.decrypt(ciphertext)
            wrapped_text = textwrap.fill(text_encrypted, width=50)  # width là độ dài mỗi dòng
            print("------------------------------------------------------------------")
            print("|                                                                |")
            print("|           ------------RESULT PLAINTEXT-----------              |")
            print("|                                                                |")
            for line in wrapped_text.splitlines():
                print(f"|    {line:<59} |")  # In từng dòng với độ rộng khung là 60 ký tự
            print("|                                                                |")
            print("------------------------------------------------------------------")
    elif option == 4:
        plaintext = input("|   ENTER YOUR PLAINTEXT  YOU WANT: ",)
        text_encrypted = RandomCiphertext(plaintext)
        wrapped_text = textwrap.fill(text_encrypted, width=50)
        print("|                                                                |")
        print("|         ------------RESULT RANDOM CIPHERTEXT-----------        |")
        print("|                                                                |")
        print(f"    {text_encrypted}")
        # for line in wrapped_text.splitlines():
        #     print(f"|    {line:<59} |")  # In từng dòng với độ rộng khung là 60 ký tự
        print("                                                                  ")
        print("------------------------------------------------------------------")
    #  run_caesar_cipher(plaintext, key=3)
    #  run_rail_fence_cipher(plaintext, rails=5)
    #  run_multiple_caesar_railfence_cipher(plaintext, caesar_key=3, rails_rail_fence=5)
    
    