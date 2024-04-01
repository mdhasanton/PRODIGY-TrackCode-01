import random
import string 

chars = " "+string.punctuation + string.digits + string.ascii_letters
num_chars = len(chars)
chars = list(chars)
shift = chars.copy()
print(chars)
print(shift)


def encrypt(plaintext, shift):
    ciphertext = ''

    for char in plaintext:
        char = char.lower()
        if not char == '':
            index = chars.index(char)
            new_index = (index + shift) % num_chars
            ciphertext += chars[new_index]
            
    return ciphertext 


def decrypt(ciphertext, shift):
    plaintext = ''

    for char in ciphertext:
        char = char.upper()
        if not char == '':
            index = chars.index(char)
            new_index = (index - shift) % num_chars
            plaintext += chars[new_index]
    return plaintext 


print()
print('****Caesar Cipher Program****')
print()

print('Do you want to Encrypt and Decrypt?')
print()
user_input = input('e/d:').lower()

if user_input == 'e':
    print('Encryption Mode Selected')
    print()
    print()

    shift = int(input('Enter the shift(1 throuth 95):'))

    text = input('Enter The text to Encrypt:')

    ciphertext = encrypt(text, shift)
    print(f'CIPHERTEXT :{ciphertext}')

elif user_input == 'd':
    print('Decryption Mode Selected')
    print()
    print()

    shift = int(input('Enter the shift(1 through 95):'))

    text = input('Enter the text to Decrypt:')

    plaintext = decrypt(text, shift)
    print(f'PLAINTEXT :{plaintext}')
