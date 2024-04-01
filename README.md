# PRODIGY-TrackCode-01
**Implement Caesar Ciper**
Create a Python program that can encrypt and decrypt text using the caesar cipher alogorithm. Allow uses to input a message and shift value to performs encryption and decryption.

# Impelement
The code provided is a simple implementation of the Caesar Cipher encryption and decryption method using Python. The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. In this implementation, the shift value can be specified by the user, and the program supports both uppercase and lowercase letters, as well as numbers and special characters.

# Here's a summary of the code:
1.The chars variable contains all possible characters that can be used in the encryption/decryption process.
2.The encrypt function takes a plaintext and shift value as input, and returns the ciphertext by shifting each character in the plaintext by the specified shift value.
3.The decrypt function takes a ciphertext and shift value as input, and returns the plaintext by shifting each character in the ciphertext by the inverse of the shift value.
4.The user is prompted to choose between encryption and decryption mode.
5.If the user chooses encryption mode, they are prompted to enter the shift value and the text to be encrypted.
6.If the user chooses decryption mode, they are prompted to enter the shift value and the text to be decrypted.

# Example:

****Caesar Cipher Program****

Do you want to Encrypt and Decrypt?

e/d:e
Encryption Mode Selected

Enter the shift(1 throuth 95):5
Enter The text to Encrypt:hello
CIPHERTEXT :mjqqt

****Caesar Cipher Program****

Do you want to Encrypt and Decrypt?

e/d:d
Decryption Mode Selected

Enter the shift(1 through 95):5
Enter the text to Decrypt:mjqqt
PLAINTEXT :hello

# Note
The shift value is limited to 1 through 95, but you can easily modify the code to support any shift value. Also, this implementation does not handle spaces in the plaintext, so you might want to modify it to handle spaces as well.
