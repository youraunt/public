# import dependencies
import string
import sys
import time


# Global function
def offset(char, relative_address):
    return uppercase_alphabet[(uppercase_alphabet.index(char) + relative_address) % 26]


# Global variable = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
uppercase_alphabet = string.ascii_uppercase


class Caesar:
    @staticmethod
    def encrypt(plain_text, key):
        return ''.join(map(offset, list(plain_text), [key, ] * len(plain_text)))

    @staticmethod
    def decrypt(encrypted_text, key):
        return ''.join(map(offset, list(encrypted_text), [26 - key, ] * len(encrypted_text)))

    @staticmethod
    def get_message_and_key():
        plain_text = str(input("\nPlease enter a message: "))
        plain_text = plain_text.replace(' ', '').upper().strip()  # The message is saved in uppercase sans whitespace
        plain_text = plain_text.translate(str.maketrans('', '', string.punctuation))
        original_key = int(input("\nPlease enter an integer shift value: "))

        print('Original message: ' + plain_text)
        print('Keyword: ' + str(original_key))
        return plain_text, original_key

    @staticmethod
    def display_menu():
        user_choice = str(input("\nWould you like to: \n1.Encrypt\n2.Decrypt\n3.Exit Program\n> "))

        if user_choice not in ('1', '2', '3'):  # Only take valid input.
            print('Invalid input.')
            Caesar.display_menu()

        if user_choice == '1':
            plain_text, key = Caesar.get_message_and_key()
            encrypted = Caesar.encrypt(plain_text, key)
            print("\nSwapping time and space...")
            time.sleep(2)  # Sleep function to fake slow processing time.
            print(encrypted)

        elif user_choice == '2':
            encrypted_text, key = Caesar.get_message_and_key()
            deciphered = Caesar.decrypt(encrypted_text, key)
            print("\nI swear it\'s almost done.")
            time.sleep(2)  # Sleep function to fake slow processing time.
            print('Decrypted message: ' + deciphered)

        elif user_choice == '3':
            print('Goodbye')
            sys.exit(0)


def main():
    while True:
        Caesar.display_menu()
        while True:
            user_input = str(input('Do you want to run the program again? (y/n): '))
            if user_input in ('y', 'n'):
                break
            print('Invalid input.')

        if user_input == 'y':
            continue
        else:
            print('Goodbye!')
            break
    plain_text = str(input("\nPlease enter a message: "))
    s = int(input("\nPlease enter a shift: "))
    print("Text  : " + plain_text)
    print("Shift : " + str(s))
    print("Cipher: " + Caesar.encrypt(plain_text, s))


if __name__ == "__main__":
    main()
