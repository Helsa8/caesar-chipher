def encrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + k) % 26
            result += chr(base + shifted)
        else:
            result += char
    return result

def decrypt(text, k):
    return encrypt(text, -k)

original_text = "Enhypen"
key = 3

encrypted_text = encrypt(original_text, key)
decrypted_text = decrypt(encrypted_text, key)

print("Original Text :", original_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
