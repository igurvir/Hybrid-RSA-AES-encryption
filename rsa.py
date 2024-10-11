from utils import generate_prime, mod_inverse, gcd

# RSA key generation with Chinese Remainder Theorem optimization
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

    # Precompute CRT components
    dp = d % (p - 1)  # d mod (p-1)
    dq = d % (q - 1)  # d mod (q-1)
    qinv = mod_inverse(q, p)  # q^(-1) mod p (CRT optimization)

    # Public and private keys
    public_key = (e, n)
    private_key = (d, p, q, dp, dq, qinv)  # Include CRT values
    return public_key, private_key

# Encrypt message
def encrypt(message, public_key):
    e, n = public_key
    message_as_int = int.from_bytes(message.encode('utf-8'), 'big')
    cipher = pow(message_as_int, e, n)
    return cipher

# Decrypt using Chinese Remainder Theorem (CRT)
def decrypt(cipher, private_key):
    d, p, q, dp, dq, qinv = private_key
    n = p * q

    # Compute message mod p and q
    m1 = pow(cipher, dp, p)
    m2 = pow(cipher, dq, q)

    # Use CRT to recombine results
    h = (qinv * (m1 - m2)) % p
    m = m2 + h * q

    # Convert integer back to string
    decrypted_message = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode('utf-8')
    return decrypted_message
