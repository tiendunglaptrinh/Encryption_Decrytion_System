class RailFenceCipher:
    def __init__(self, rails: int):
        self.rails = rails
    def encrypt(self, plaintext: str) -> str:
        # Declaration variable:
        # direction=1: go down, direction=-1: go up
        result_ciphertext = ""
        plaintextTrim = plaintext.replace(" ","")
        length_matrix = len(plaintextTrim)    
        num_rails = self.rails
        matrix_cipher = [["" for _ in range(length_matrix)] for _ in range(num_rails)]
        direction = -1
        row=0
        col=0
        
        # Implement
        # Write in matrix
        for i in range(length_matrix):
            print('row: ', row)
            print('col: ', col)
            matrix_cipher[row][col] = plaintextTrim[i]
            if row==0 or row==num_rails-1:
                 direction *= -1
            row += direction
            col += 1
        
        # Read from matrix
        for i in range(num_rails):
            for j in range(length_matrix):
                if matrix_cipher[i][j] != '':
                    result_ciphertext += matrix_cipher[i][j]
                    
        return result_ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        
        # Declaration:
        result_plaintext = ""
        num_rails = self.rails
        length_matrix = len(ciphertext)
        direction = -1
        row, col = 0, 0
        matrix_plaintext = [["" for _ in range(length_matrix)] for _ in range(num_rails)]
        
        # Mark the point:
        for i in range(length_matrix):
            matrix_plaintext[row][col] = "*"
            if row==0 or row==num_rails-1:
                direction *= -1
            row += direction
            col += 1
            count = 0
        
        # Fill in matrix
        for i in range(num_rails):
            for j in range(length_matrix):
                if matrix_plaintext[i][j] == "*":
                    matrix_plaintext[i][j] = ciphertext[count]
                    count += 1
        
        # Read plaintext
        direction = -1
        row, col = 0, 0
        for col in range(length_matrix):
            result_plaintext += matrix_plaintext[row][col]
            if row==0 or row==num_rails-1:
                direction *= -1
            row += direction
            
        return result_plaintext
    