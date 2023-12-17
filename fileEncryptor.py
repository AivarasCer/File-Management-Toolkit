# File Encryption/Decryption Tool
# Script to encrypt sensitive files and decrypt them as needed.
# This can add an extra layer of security to your important documents.

from cryptography.fernet import Fernet


class FileEncryptor:

    def __init__(self, key=None):
        self.key = key if key else Fernet.generate_key()

    @staticmethod
    def generate_key():
        return Fernet.generate_key()

    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            data = file.read()
        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        fernet = Fernet(self.key)
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)


def main():
    user_choice = int(input('Choose action:'
                            '\n1. Encrypt file'
                            '\n2. Decrypt file'
                            '\n3. Exit'
                            '\n> '))
    file_path = input('Enter the full path of the file: ')
    key_input = input('Enter the encryption/decryption key (leave blank to generate a new one): ')

    if not key_input:
        key_input = FileEncryptor.generate_key()
        print(f'Generated key: {key_input.decode()} - Keep it safe!')

    encryptor = FileEncryptor(key_input)

    if user_choice == 1:
        encryptor.encrypt_file(file_path)
        print(f'File {file_path} encrypted.')

    elif user_choice == 2:
        encryptor.decrypt_file(file_path)
        print(f'File {file_path} decrypted.')

    else:
        print('Invalid choice.')

if __name__ == "__main__":
    main()
