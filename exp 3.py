# Experiment 03: Blowfish Encryption/Decryption (Menu Driven - Simplified Version)

# Example P-array (keys) – in real Blowfish there are 18 subkeys
P = [0x243F6A88, 0x85A308D3, 0x13198A2E, 0x03707344]

S = [0xA4093822, 0x299F31D0, 0x082EFA98, 0xEC4E6C89]


def F(x):
    """Simplified F-function"""
    return ((S[0] ^ x) + (S[1] ^ x)) & 0xFFFFFFFF


def blowfish_encrypt(L, R, rounds=4):
    """Encrypt two 32-bit halves"""
    for i in range(rounds):
        L = L ^ P[i % len(P)]      # XOR with subkey
        R = R ^ F(L)               # XOR with F-function output
        L, R = R, L                # Swap halves
    return L, R


def blowfish_decrypt(L, R, rounds=4):
    """Decrypt two 32-bit halves"""
    for i in reversed(range(rounds)):
        L, R = R, L                # Undo swap
        R = R ^ F(L)               # Undo F-function
        L = L ^ P[i % len(P)]      # Undo subkey
    return L, R


def text_to_blocks(text):
    """Convert text into two 32-bit halves (only first 8 chars used)"""
    text = text.ljust(8, '\0')      # pad to 8 chars
    L = int.from_bytes(text[:4].encode(), 'big')
    R = int.from_bytes(text[4:8].encode(), 'big')
    return L, R


def blocks_to_text(L, R):
    """Convert halves back to text"""
    left = L.to_bytes(4, 'big').decode(errors='ignore')
    right = R.to_bytes(4, 'big').decode(errors='ignore')
    return (left + right).rstrip('\0')


# ---------------- MAIN MENU ----------------
while True:
    print("\n--- Blowfish Encryption Demo ---")
    print("1. Encrypt Text")
    print("2. Decrypt Cipher (Hex Input)")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        text = input("Enter text (max 8 chars): ")
        L, R = text_to_blocks(text)
        print(f"Plaintext blocks: {hex(L)}, {hex(R)}")
        Lc, Rc = blowfish_encrypt(L, R)
        print("Ciphertext (HEX):", hex(Lc), hex(Rc))

    elif choice == '2':
        Lc = int(input("Enter Left Cipher (hex, e.g. 0x1234abcd): "), 16)
        Rc = int(input("Enter Right Cipher (hex): "), 16)
        Ld, Rd = blowfish_decrypt(Lc, Rc)
        text = blocks_to_text(Ld, Rd)
        print("Decrypted Text:", text)

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
