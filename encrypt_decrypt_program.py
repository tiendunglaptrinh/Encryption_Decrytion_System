from caesar_cipher import CaesarCipher
from rail_fence_cipher import RailFenceCipher
from multiple_caesar_railfence_cipher import MultipleCaesarRailFence

def run_caesar_cipher(plaintext: str, key: int):
    caesar_cipher_obj = CaesarCipher(key=key)
    encrypted_text = caesar_cipher_obj.encrypt(plaintext)
    decrypted_text = caesar_cipher_obj.decrypt(encrypted_text)
    
    print('----------------------------------------------------------------------------------------------------')
    print("Caesar Cipher is running:")
    print("Cipherttext: ", encrypted_text)
    print("Plaintext: ", decrypted_text)
    
def run_rail_fence_cipher(plaintext: str, rails: int):
    rail_fence_cipher_obj = RailFenceCipher(rails=rails)
    encrypted_text = rail_fence_cipher_obj.encrypt(plaintext)
    decrypted_text = rail_fence_cipher_obj.decrypt(encrypted_text)
    
    print('----------------------------------------------------------------------------------------------------')
    print("Rail Fence is running:")
    print("Cipherttext: ", encrypted_text)
    print("Plaintext: ", decrypted_text)
    
def run_multiple_caesar_railfence_cipher(plaintext: str, caesar_key: int,  rails_rail_fence: int):
    caesar_rail_fence_cipher_obj = MultipleCaesarRailFence(caesar_key=caesar_key, rails_rail_fence=rails_rail_fence)
    encrypted_text = caesar_rail_fence_cipher_obj.encrypt(plaintext)
    decrypted_text = caesar_rail_fence_cipher_obj.decrypt(encrypted_text)
    
    print('----------------------------------------------------------------------------------------------------')
    print("Multiple Caesar and Rail fence is running:")
    print("Cipherttext: ", encrypted_text)
    print("Plaintext: ", decrypted_text)
    
def main():
     plaintext = "HELLO WORLD"
     
     run_caesar_cipher(plaintext, key=3)
     run_rail_fence_cipher(plaintext, rails=4)
     run_multiple_caesar_railfence_cipher(plaintext, caesar_key=3, rails_rail_fence=5)