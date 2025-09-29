import random
from math import gcd

# ---------- Prime utilities ----------
def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime(bits=16):
    while True:
        num = random.randint(2**(bits-1), 2**bits-1)
        if is_prime(num):
            return num

# ---------- Modular inverse ----------
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0

# ---------- RSA key generation ----------
def generate_keys(bits=16):
    p = generate_prime(bits)
    q = generate_prime(bits)
    while q == p:
        q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    d = modinv(e, phi)
    return ((e, n), (d, n))

# ---------- RSA encryption/decryption ----------
def encrypt(m, public_key):
    return pow(m, public_key[0], public_key[1])

def decrypt(cipher, private_key):
    return pow(cipher, private_key[0], private_key[1])

# ---------- Menu-driven interface ----------
def main_menu():
    public_key = private_key = None
    while True:
        print("\n===== RSA Menu =====")
        print("1) Generate RSA Keys")
        print("2) Encrypt Message")
        print("3) Decrypt Message")
        print("4) Exit")
        choice = input("Enter choice [1-4]: ").strip()

        if choice == "1":
            public_key, private_key = generate_keys(bits=16)
            print("Public key:", public_key)
            print("Private key:", private_key)
        elif choice == "2":
            if public_key is None:
                print("Generate keys first!")
                continue
            try:
                message = int(input("Enter plaintext (integer only): "))
            except ValueError:
                print("Invalid input. Enter an integer.")
                continue
            cipher = encrypt(message, public_key)
            print("Encrypted message:", cipher)
        elif choice == "3":
            if private_key is None:
                print("Generate keys first!")
                continue
            try:
                cipher = int(input("Enter encrypted message (integer): "))
            except ValueError:
                print("Invalid input. Enter an integer.")
                continue
            decrypted = decrypt(cipher, private_key)
            print("Decrypted message:", decrypted)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
