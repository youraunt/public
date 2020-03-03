import string
import sys
import time

# Global variable = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
uppercase_alphabet = string.ascii_uppercase


# Global function
def offset(char, relative_address):
    return uppercase_alphabet[(uppercase_alphabet.index(char) + relative_address) % 26]


# VigenereCipher class contains four staticmethod instances
# encrypt single-precision floating-point number (f4) data type, is the parent of the lambda function
# it maps the letters of the key to there respective values eg A = 0, B = 1, C = 2, ..., Y = 24, Z = 25
# it then maps the letters of the message to the relative_address of the key to the uppercase_alphabet
# example: plain_text = "BRICE" key = "HEY" which will be extended to "HEYHE" to match the length of message
#           H maps to 7 because its the 8th letter of the alphabet and we start at zero here.
#           H = index 7, E = index 4, Y = index 24, H = index 7, E = index 4
#           then it takes the index of the current letter from plain_text and sums it with its relative_address
#           and modulo it by 26
#           so for key = HEYHE and plain_text = BRICE
#           We have B index at 2 + the relative_index of H at 7   2 + 7 = 9
#           Then modulo 26 still equals 9. So, the cipher for B is I
#           R = index 18 + relative index of E at 4.  18 + 4 = 22 mod 26 = 22. So, the cipher for R is V
#           I = 9; Y = 24; 9 + 24 = 33; 33%26 = 7. So, the cipher for I is G the seventh letter of the alphabet.
#           C = 3; H = 7; 3 + 7 = 10; 10%26 = 10. So, the cipher for C is J the tenth letter of the alphabet.
#           E = 5; E = 4; 5 + 4 + 9; 9%26 = 9. So, the cipher for E is I the 9th letter of the alphabet.
#           plain_text = "BRICE", key = "heyhe", encrypted = "IVGJI"

# decrypt same as encrypt but backwards
# display_menu handles user i/o
# get_message_and_key returns tuple containing
# index 0 = plain_text which has been capitalized
# index 1 = key which has been capitalized and either truncated or extended to match length of message
class VigenereCipher:
    @staticmethod
    def encrypt(plain_text, key):
        return ''.join(map(offset, plain_text,
                           list(map(lambda x: uppercase_alphabet.index(x), key))))

    @staticmethod
    def decrypt(encrypted_text, key):
        return ''.join(map(offset, encrypted_text,
                           list(map(lambda x: 26 - uppercase_alphabet.index(x), key))))

    @staticmethod
    def get_message_and_key():
        plain_text = str(input("\nPlease enter a message: "))
        plain_text = plain_text.replace(' ', '').upper()  # The message is saved in uppercase sans whitespace
        original_key = str(input("\nPlease enter a keyword: "))
        original_key = original_key.replace(' ', '').upper()  # The key is saved in uppercase sans whitespace
        key = ''
        if len(plain_text) > len(original_key):  # If the message length is greater than that of the key
            for i in range(int(len(plain_text) / len(original_key))):
                key += original_key  # The key is extended, duplicating it and concatenated
            key += original_key[:len(plain_text) % len(original_key)]  # make length is same as message

        elif len(plain_text) < len(original_key):  # If the length of the message is less than that of the key
            key = original_key[:len(plain_text)]  # The key is truncated to have the same length as the message

        elif len(plain_text) == len(original_key):  # If the message length is the same as the key
            key = original_key  # The key is saved as is in key

        else:  # idk something went wrong display error message and exit program with code 1 abnormal exit
            print('\nHello IT, have you tried turning it off and on again?')
            sys.exit(1)

        print('Original message: ' + plain_text)
        print('Keyword: ' + original_key)
        return plain_text, key

    @staticmethod
    def display_menu():
        user_choice = str(input("\nWould you like to: \n1.Encrypt\n2.Decrypt\n3.Exit Program\n> "))

        if user_choice not in ('1', '2', '3'):  # Only take valid input.
            print('Invalid input.')
            VigenereCipher.display_menu()

        if user_choice == '1':
            plain_text, key = VigenereCipher.get_message_and_key()
            encrypted = VigenereCipher.encrypt(plain_text, key)
            print("\nSwapping time and space...")
            time.sleep(2)  # Sleep function to fake slow processing time.
            print(encrypted)

        elif user_choice == '2':
            encrypted_text, key = VigenereCipher.get_message_and_key()
            deciphered = VigenereCipher.decrypt(encrypted_text, key)
            print("\nI swear it\'s almost done.")
            time.sleep(2)  # Sleep function to fake slow processing time.
            print('Decrypted message: ' + deciphered)

        elif user_choice == '3':
            print('Goodbye')
            sys.exit(0)


# define main method while loop to continue program until user opts to exit
def main():
    while True:
        VigenereCipher.display_menu()
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


if __name__ == "__main__":
    main()
