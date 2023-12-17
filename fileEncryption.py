# File Encryption/Decryption Tool
# Script to encrypt sensitive files and decrypt them as needed.
# This can add an extra layer of security to your important documents.

from cryptography.fernet import Fernet
from pathlib import Path


class FileEncryctor:

    def __init__(self, key=None):
        self.key = key if key else Fernet.generate_key()

    def generate_key(self):
        return Fernet.generate_key()

    def encrypt_file(self, file_path):
        pass

    def decrypt_file(self, file_path):
        pass


def main():
    pass

if __name__ == "__main__":
    main()
