
# Check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def choose_public_exponent(phi):
    for e in range(2, phi):
        if is_prime(e) and phi % e != 0:
            return e
    raise Exception("No valid public exponent found.")
  
def compute_private_key(e, phi):
    k = 1
    while True:
        d = (1 + k * phi) / e
        if d.is_integer():
            return int(d)
        k += 1

def encrypt_message(text, e, n):
    return [(ord(char) ** e) % n for char in text]

def decrypt_message(cipher, d, n):
    return ''.join([chr((num ** d) % n) for num in cipher])

def main():
    print("RSA Encryption Program by Diwanshi Pandey\n")

    message = "Diwanshi"
    print(f"Message to encrypt: {message}")

    p, q = map(int, input("Enter two prime numbers (p q): ").split())

    while not (is_prime(p) and is_prime(q)):
        print("One or both numbers are not prime.")
        p, q = map(int, input("Re-enter two prime numbers: ").split())

    n = p * q
    phi = (p - 1) * (q - 1)

    e = choose_public_exponent(phi)
    d = compute_private_key(e, phi)

    encrypted = encrypt_message(message, e, n)
    decrypted = decrypt_message(encrypted, d, n)

    print(f"\nPublic Key (e, n): ({e}, {n})")
    print(f"Private Key (d): {d}")
    print(f"Encrypted Message: {encrypted}")

    choice = input("\nDo you want to decrypt the message? (Yes/No): ")
    if choice.lower() == 'yes':
        print(f"Decrypted Message: {decrypted}")
    else:
        print("Nice to meet you")
      
if __name__ == "__main__":
    main()
