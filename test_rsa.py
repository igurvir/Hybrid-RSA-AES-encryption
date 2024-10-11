from rsa import generate_rsa_keys, encrypt, decrypt

def test_rsa():
    # Generate RSA keys
    public_key, private_key = generate_rsa_keys()

    # Original message
    message = "Hello, RSA encryption!"
    print(f"Original Message: {message}")

    # Encrypt the message
    cipher = encrypt(message, public_key)
    print(f"Encrypted Cipher: {cipher}")

    # Decrypt the cipher
    decrypted_message = decrypt(cipher, private_key)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    test_rsa()
