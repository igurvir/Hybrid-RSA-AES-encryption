# Hybrid RSA + AES File Encryption System
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Cryptography](https://img.shields.io/badge/cryptography-3.x-blue?style=for-the-badge&logo=cryptography&logoColor=white)
![SymPy](https://img.shields.io/badge/SymPy-1.x-blue?style=for-the-badge&logo=sympy&logoColor=white)

### Overview

This project implements a hybrid encryption system that combines the security of RSA (asymmetric encryption) with the speed and efficiency of AES (symmetric encryption). The system allows for the encryption of files using AES, while securely encrypting the AES key with RSA. This approach balances strong security for key exchange (RSA) with high performance for file encryption (AES).

## Why RSA + AES Hybrid Encryption?

RSA is an asymmetric encryption system that is secure for encrypting small pieces of data, like an AES key. AES, a symmetric encryption system, is much faster and more efficient for encrypting large files. By combining the two, we get the best of both worlds: RSA for secure key exchange and AES for efficient file encryption.

### Features
- **RSA Encryption:** Securely encrypts the AES key using RSA with OAEP padding (Optimal Asymmetric Encryption Padding).
  
- **AES Encryption:** Handles file encryption using AES in CFB mode (Cipher Feedback Mode) with a 256-bit AES key.
  
- **File Encryption and Decryption:** Supports encrypting and decrypting files of any type.
  
- **Hybrid Approach:**  Combines the strengths of RSA and AES for optimal security and performance.
  
### Technology Stack
- Python 3.x

- Cryptography Library: Used for RSA and AES encryption.

- SymPy: Used for prime number generation and other mathematical operations.

### Project Structure


rsa-encryption
│

├── rsa.py  

├── test_rsa.py 

├── utils.py     

├── sample_file.txt 

 

### How It Works

 - RSA Key Generation:

A 2048-bit RSA key pair is generated. The public key is used to encrypt the AES key, and the private key is used to decrypt it.

- AES Encryption:

Files are encrypted using AES (Advanced Encryption Standard) with a randomly generated 256-bit key. AES is faster and suitable for encrypting large amounts of data.

- Hybrid Encryption:

The AES key is encrypted using the RSA public key, ensuring secure transmission of the key.
The AES-encrypted file data and the RSA-encrypted AES key are combined and saved.

- Decryption:

The RSA private key decrypts the AES key, which is then used to decrypt the file data.

### Installation

Clone the repository:

`
git clone https://github.com/yourusername/hybrid-rsa-aes-encryption.git
`

`
cd hybrid-rsa-aes-encryption
`

Install dependencies: The project uses the cryptography and sympy libraries, so make sure to install them:

`
pip install cryptography sympy
`

### Commands for Tasks

1. Encryption:
   
To encrypt a file, run the following script:

`
python test_rsa.py
`

This script will:

1. Generate an RSA key pair.
   
2. Encrypt sample_file.txt using AES.
   
3. Encrypt the AES key using RSA.
   
4. Save the encrypted file as sample_file.txt.enc.
   
5. Decryption:
   
To decrypt the file:

The test_rsa.py script will automatically decrypt the encrypted file (sample_file.txt.enc) and save the decrypted version as sample_file.txt_decrypted.

### Example Output:

`
Original File Data Size: 20 bytes
`
`
Encrypted File Data Size: 36 bytes
`
`
File sample_file.txt encrypted and saved as sample_file.txt.enc
`
`
Decrypted AES Key: 7a0d74c607151ff2cc7474079c06767682612e7ae50edba4d2f9f07482ce8542
`
`
Decrypted File Data Size: 20 bytes
`
`
File decrypted and saved as sample_file.txt_decrypted
`


### Code Overview
1. rsa.py
  
This file contains the core encryption and decryption functions:

- generate_rsa_keys(): Generates a 2048-bit RSA key pair.
  
- aes_encrypt(): Encrypts file data using AES.
  
- aes_decrypt(): Decrypts AES-encrypted file data.
  
- encrypt_file(): Encrypts a file using AES, then encrypts the AES key with RSA.
  
- decrypt_file(): Decrypts a file by first decrypting the AES key with RSA, then decrypting the file with AES.
  
2. test_rsa.py
   
A test script that demonstrates the encryption and decryption process using sample_file.txt.

3. utils.py
   
Contains helper functions such as:

- Prime generation for RSA.
  
- Greatest common divisor calculation.
  
- Modular inverse calculation using the extended Euclidean algorithm.
  
### Security Details
RSA with OAEP Padding: The project uses OAEP padding with RSA, which provides additional security by adding randomness to the encryption process. 
This protects against chosen-ciphertext attacks.

AES with CFB Mode: AES is used in CFB mode, which ensures that even if the same data is encrypted multiple times, the ciphertext will be different due to the initialization vector (IV).

Key Sizes:

RSA: 2048 bits (secure for most use cases).

AES: 256 bits (industry standard for high security).

## Use Cases
This encryption system can be used for:
- Secure file transmission where both the file and the encryption key need to be protected.
- Protecting sensitive data in storage (e.g., healthcare records, financial data).
- Encryption and decryption of large files without the performance hit of RSA-only encryption.


### Future Improvements
Digital Signatures: Add functionality for signing and verifying files to ensure data authenticity.

Performance Testing: Benchmark encryption/decryption performance for different RSA key sizes (e.g., 1024-bit, 2048-bit, 4096-bit) and file sizes.

GUI Interface: Create a simple GUI for easier file selection and encryption/decryption.

## Project Documentation

The full project documentation is available [here](Hybrid_RSA___AES_File_Encryption_System.pdf).


### Contributing
Feel free to submit issues, fork the project, and create pull requests. Contributions and suggestions are always welcome!

### Connect With Me On LinkedIn
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gurvir-singh5)


