def caesar(s, k):
    res = ""
    for c in s:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            res += chr((ord(c) - base + k) % 26 + base)
        else:
            res += c
    return res
text = input("Enter text: ")
key = int(input("Enter caesar key: "))
print("Cipher text:", caesar(text, key))

def rot13(s):
    res = ""
    for c in s:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            res += chr((ord(c) - base + 13) % 26 + base)
        else:
            res += c
    return res
text = input("Enter ROT13 text: ")
print("Cipher text:", rot13(text))

def atbash(s):
    res = ""
    for c in s:
        if c.islower():
            res += chr(ord('z') - (ord(c) - ord('a')))
        elif c.isupper():
            res += chr(ord('Z') - (ord(c) - ord('A')))
        else:
            res += c
    return res
text = input("Enter ATBASH text: ")
print("Cipher text:", atbash(text))
