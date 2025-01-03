import random
import string


def caesar_cipher(message, k):
    cipher = ""
    for char in message:
        if char.isalpha():  # Get the ASCII code of the character and shift it down the alphabet
            shifted = ord(char.lower()) + k  # Convert the shifted ASCII code back to a character
            if shifted > ord('z'):
                shifted -= 26  # Wrap around if past 'z'
            cipher += chr(shifted).upper() if char.isupper() else chr(shifted)
        else:
            cipher += char  # Non-alphabetic characters are not encrypted
    return cipher


def decrypt_caesar_cipher(encrypted_message, alphabet, k):
    plaintext = ""
    for letter in encrypted_message:
        if letter in alphabet:
            plaintext += alphabet[(ord(letter) - ord('A') - k) % 26]
        else:
            plaintext += letter
    return plaintext


def main():
    print("Welcome to the Caesar Cipher Program!")
    print("Please enter your message. It should contain at least 200 words.")
    message = input("Enter text: ")

    # Check message length
    num_words = len(message.split())
    if num_words < 200:
        print("Message should contain at least 200 words. Please try again.")
        return

    # Encryption
    text = message.upper()
    s = random.randint(1, 25)
    encrypted_message = caesar_cipher(text, s)
    print("\nEncrypted message:")
    print(encrypted_message)

    # Decryption
    alphabet = string.ascii_uppercase
    freq = {letter: 0 for letter in alphabet}  # Count the letter frequencies
    for letter in encrypted_message:
        if letter in alphabet:
            freq[letter] += 1
    most_frequent_letter = max(freq, key=freq.get)  # Find the most frequent letter

    k_values = [(ord(most_frequent_letter) - ord('E')) % 26]  # Find the possible values of k
    for k in k_values:  # Decrypt the message for each possible value of k
        plaintext = decrypt_caesar_cipher(encrypted_message, alphabet, k)
        print(f"\nDecrypted message with k = {k}:")
        print(plaintext)


if __name__ == "__main__":
    main()