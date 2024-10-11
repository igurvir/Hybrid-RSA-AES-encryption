#Created by Gurvir Singh Sheridan College - Oct, 2024

from rsa import generate_rsa_keys, encrypt_file, decrypt_file

def test_rsa_file_encryption():
    # Step 1: Generate RSA keys (public and private)
    public_key, private_key = generate_rsa_keys()

    # Step 2: File encryption
    file_path = 'sample_file.txt'  # Make sure this file exists
    encrypt_file(file_path, public_key)  # Encrypt the file with the public key
    
    # Step 3: File decryption
    decrypt_file(file_path + '.enc', private_key)  # Decrypt the file with the private key

if __name__ == "__main__":
    test_rsa_file_encryption()
