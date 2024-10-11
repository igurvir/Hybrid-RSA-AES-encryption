#Created by Gurvir Singh Sheridan College - Oct, 2024

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
import os

# Function to generate RSA keys (public and private)
def generate_rsa_keys():
    # Generating 2048-bit RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,  # Common choice for the public exponent
        key_size=2048,  # Key size in bits (2048 is secure for most applications)
        backend=default_backend()
    )
    public_key = private_key.public_key()  # Extracting the public key from private
    return public_key, private_key

# AES encryption function
def aes_encrypt(data, aes_key):
    # Generating an initialization vector (IV) to ensure randomness
    iv = os.urandom(16)  # 16 bytes for AES (CFB mode)
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()  # Create encryptor object
    ciphertext = encryptor.update(data) + encryptor.finalize()  # Encrypt the data
    return iv + ciphertext  # Prepend IV to ciphertext for decryption later

# AES decryption function
def aes_decrypt(ciphertext, aes_key):
    iv = ciphertext[:16]  # Extracting IV (first 16 bytes)
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()  # Create decryptor object
    return decryptor.update(ciphertext[16:]) + decryptor.finalize()  # Decrypt data

# Encrypt a file using AES, then encrypt the AES key with RSA (with OAEP padding)
def encrypt_file(file_path, public_key):
    # Read the file data
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Debugging: print original file size
    print(f"Original File Data Size: {len(file_data)} bytes")

    # Generate a random AES key (256 bits = 32 bytes)
    aes_key = os.urandom(32)

    # Encrypt the file data using AES
    encrypted_data = aes_encrypt(file_data, aes_key)

    # Debugging: print encrypted data size
    print(f"Encrypted File Data Size: {len(encrypted_data)} bytes")

    # Encrypt the AES key using RSA with OAEP padding for security
    encrypted_aes_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Mask generation function (MGF)
            algorithm=hashes.SHA256(),  # Hashing algorithm for padding
            label=None  # No additional label
        )
    )

    # Write both the encrypted AES key and encrypted file data to disk
    with open(file_path + '.enc', 'wb') as file:
        file.write(encrypted_aes_key + encrypted_data)

    print(f"File {file_path} encrypted and saved as {file_path}.enc")

# Decrypt an encrypted file using RSA (with OAEP) to decrypt the AES key
def decrypt_file(encrypted_file_path, private_key):
    # Read the encrypted file data
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()

    # Extract the RSA-encrypted AES key (256 bytes)
    encrypted_aes_key = encrypted_data[:256]
    encrypted_file_data = encrypted_data[256:]

    # Debugging: print the size of the encrypted file data
    print(f"Encrypted File Data Size (read from .enc file): {len(encrypted_file_data)} bytes")

    # Decrypt the AES key using RSA (with OAEP padding)
    aes_key = private_key.decrypt(
        encrypted_aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Same padding as encryption
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # Debugging: print the decrypted AES key
    print(f"Decrypted AES Key: {aes_key.hex()}")

    # Decrypt the file data using the AES key
    decrypted_data = aes_decrypt(encrypted_file_data, aes_key)

    # Debugging: print the decrypted file size
    print(f"Decrypted File Data Size: {len(decrypted_data)} bytes")

    # Write the decrypted data to a new file
    output_file_path = encrypted_file_path.replace('.enc', '_decrypted')
    with open(output_file_path, 'wb') as file:
        file.write(decrypted_data)

    print(f"File decrypted and saved as {output_file_path}")
