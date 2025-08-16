import random
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = ''.join(random.sample(alpha,len(alpha)))

# Encryption
plain_text = input("Plain Text: ")
print("Key:", key)
cipher_text = ''

for char in plain_text:
    if char.upper() in alpha:
        p_idx = alpha.index(char.upper())
        cipher_text+=key[p_idx]
    else:
        cipher_text+=char
        
print("Cipher Text:", cipher_text)

# Decryption
plain_text = ''
for char in cipher_text:
    if char.upper() in alpha:
        ct_idx = key.index(char.upper())
        plain_text+=alpha[ct_idx]
    else:
        plain_text+=char
        
print("Deciphered Text:", plain_text)
