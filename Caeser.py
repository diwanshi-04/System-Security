alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Encryption
plain_text = input("Plain Text: ")
cipher_text = ''
k = 3
for char in plain_text:
    if char.upper() in alpha:
        p_idx = alpha.index(char.upper())
        ct_idx = (p_idx + k)%26
        cipher_text+=alpha[ct_idx]
    else:
        cipher_text+=char
    
print("Cipher Text:", cipher_text)

# Decryption
plain_text = ''
for char in cipher_text:
    if char.upper() in alpha:
        ct_idx = alpha.index(char.upper())
        p_idx = (ct_idx - k)%26
        plain_text+=alpha[p_idx]
    else:
        plain_text+=char

print("Dechiphered Text:", plain_text
