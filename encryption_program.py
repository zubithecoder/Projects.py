# Making a Encryption Program Using Only Python

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()


random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}") 


# ENCRYPT
plain_text = input("Enter a message to Encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# DECRYPT 
cipher_text = input("Enter a message to Decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}") 



"""
# OR WITH COMMENTS FOR BETTER UNDERSTANDING:
# Making an Encryption Program Using Only Python

import random  # Import random module to shuffle characters
import string  # Import string module for letters, digits, and punctuation

# Create a list of all characters (space, punctuation, digits, letters)
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)  # Convert string to list
key = chars.copy()  # Make a copy of the list for the encryption key

random.shuffle(key)  # Shuffle the key list to create a random mapping

print(f"chars: {chars}")  # Display original character list
print(f"key: {key}")      # Display shuffled key list

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")  # Get message from user
cipher_text = ""  # Create an empty string for the encrypted message

for letter in plain_text:  # Loop through each letter in the message
    index = chars.index(letter)  # Find the letter’s index in chars
    cipher_text += key[index]  # Replace it with the letter at same index in key

print(f"Original message: {plain_text}")       # Show original message
print(f"Encrypted message: {cipher_text}")     # Show encrypted message

# DECRYPT
cipher_text = input("Enter a message to decrypt: ")  # Get encrypted message
plain_text = ""  # Create an empty string for the decrypted message

for letter in cipher_text:  # Loop through each letter in encrypted message
    index = key.index(letter)  # Find letter’s index in key
    plain_text += chars[index]  # Replace it with the letter at same index in chars

print(f"Encrypted message: {cipher_text}")      # Show encrypted message
print(f"Original message: {plain_text}")        # Show decrypted (original) message
"""
