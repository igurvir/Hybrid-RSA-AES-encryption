from utils import generate_prime, mod_inverse, gcd

# RSA key generation
def generate_rsa_keys():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Choose public exponent e
    e = 65537  # Standard choice for e
    if gcd(e, phi_n) != 1:
        raise ValueError("e and phi_n are not coprime")

    # Compute private exponent d
    d = mod_inverse(e, phi_n)
    
    # Public and private keys
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

# Encrypt message
def encrypt(message, public_key):
    e, n = public_key
    message_as_int = int.from_bytes(message.encode('utf-8'), 'big')
    cipher = pow(message_as_int, e, n)
    return cipher

# Decrypt cipher
def decrypt(cipher, private_key):
    d, n = private_key
    decrypted_int = pow(cipher, d, n)
    decrypted_message = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, 'big').decode('utf-8')
    return decrypted_message
