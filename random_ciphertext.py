import random
import string
from caesar_cipher import CaesarCipher
from rail_fence_cipher import RailFenceCipher
from multiple_caesar_railfence_cipher import MultipleCaesarRailFence


def RandomCiphertext(plaintext) -> str:
    random_num = random.randint(1, 3)
    random_text = ""
    
    # Caesar cipher
    if random_num == 1:
        key =  random.randrange(1, 1001)
        caesar_obj = CaesarCipher(key)
        random_text = caesar_obj.encrypt(plaintext)
        
    # Rail fence cipher
    elif random_num == 2:
        rails =  random.randrange(1, 1001)
        railfence_obj = RailFenceCipher(rails)
        random_text = railfence_obj.encrypt(plaintext)
        
    # Multiple cipher
    elif random_num == 3:
        rails =  random.randrange(1, 1001)
        key =  random.randrange(1, 1001)
        multiple_obj = MultipleCaesarRailFence(key, rails)
        random_text = multiple_obj.encrypt(plaintext)
        
    return random_text
