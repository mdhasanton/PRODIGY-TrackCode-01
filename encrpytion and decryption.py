def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    if choice == 'e':
        message = input("Enter the message to encrypt: ")
        key = int(input("Enter the key value: "))
        encrypted_message = encrypt(message, key)
        print("Encrypted message:", encrypted_message)
    elif choice == 'd':
        encrypted_message = input("Enter the message to decrypt: ")
        key = int(input("Enter the key value: "))
        decrypted_message = decrypt(encrypted_message, key)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
