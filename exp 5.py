# Experiment 05: Diffie-Hellman Key Exchange - Menu Driven with User Input for p and g

def dh_demo():
    print("\n--- Diffie-Hellman Key Exchange Demo ---")

    # User inputs prime and generator
    try:
        p = int(input("Enter a prime number p: "))
        g = int(input("Enter a generator g (primitive root modulo p): "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    # Input private keys
    try:
        a = int(input("Enter Alice's private key (integer): "))
        b = int(input("Enter Bob's private key (integer): "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    # Compute public keys
    A = pow(g, a, p)  # Alice's public key
    B = pow(g, b, p)  # Bob's public key
    print(f"\nAlice's public key A = {A}")
    print(f"Bob's public key   B = {B}")

    # Compute shared secret
    s_alice = pow(B, a, p)
    s_bob = pow(A, b, p)
    print(f"\nAlice computes shared secret: {s_alice}")
    print(f"Bob computes shared secret:   {s_bob}")

    if s_alice == s_bob:
        print("Success! Shared secret established.")
    else:
        print("Error: Secrets do not match!")

# Menu-driven interface
def main_menu():
    while True:
        print("\n===== Diffie-Hellman Menu =====")
        print("1) Run Diffie-Hellman Demo")
        print("2) Exit")
        choice = input("Enter choice [1-2]: ").strip()

        if choice == "1":
            dh_demo()
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
