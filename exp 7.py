import hashlib

# ---------- Hash computation ----------
def compute_hashes(data):
    md5_hash = hashlib.md5(data.encode()).hexdigest()
    sha256_hash = hashlib.sha256(data.encode()).hexdigest()
    return md5_hash, sha256_hash

# ---------- Menu-driven interface ----------
def main_menu():
    while True:
        print("\n===== Hashing Menu =====")
        print("1) Compute MD5 and SHA-256 for a single string")
        print("2) Compare two strings (MD5 and SHA-256)")
        print("3) Exit")
        choice = input("Enter choice [1-3]: ").strip()

        if choice == "1":
            data = input("Enter string to hash: ")
            md5_hash, sha256_hash = compute_hashes(data)
            print(f"\nString: {data}")
            print(f"MD5 Hash:     {md5_hash}")
            print(f"SHA-256 Hash: {sha256_hash}")
        elif choice == "2":
            data1 = input("Enter first string: ")
            data2 = input("Enter second string: ")
            md5_1, sha256_1 = compute_hashes(data1)
            md5_2, sha256_2 = compute_hashes(data2)
            print("\n--- Hash Comparison ---")
            print(f"Original Data:     {data1}")
            print(f"MD5 Hash:          {md5_1}")
            print(f"SHA-256 Hash:      {sha256_1}")
            print(f"\nModified Data:     {data2}")
            print(f"MD5 Hash:          {md5_2}")
            print(f"SHA-256 Hash:      {sha256_2}")
            print("\nAre MD5 hashes equal?     ", md5_1 == md5_2)
            print("Are SHA-256 hashes equal? ", sha256_1 == sha256_2)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
