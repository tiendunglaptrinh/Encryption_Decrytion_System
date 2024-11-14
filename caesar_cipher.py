class CaesarCipher:
    def __init__(self, key: int):
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        result_ciphertext = ""
        plaintextTrim = plaintext.replace(" ", "")
        for char_plaintext in plaintextTrim:
            # ord: convert char to utf-8 code, chr:convert utf-8 code to char 
            # utf-8: 1114112 chars, but 1112064 availble
            encrypted_char = chr((ord(char_plaintext) + self.key) % 1114112)
            result_ciphertext += encrypted_char
        return result_ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        result_plaintext = ""
        for char_ciphertext in ciphertext:
            dcrypted_char_value = ord(char_ciphertext) - self.key
            dcrypted_char_value = dcrypted_char_value if dcrypted_char_value > 0 else -dcrypted_char_value
            dcrypted_char = chr(dcrypted_char_value % 1114112)
            result_plaintext += dcrypted_char
        return result_plaintext
    