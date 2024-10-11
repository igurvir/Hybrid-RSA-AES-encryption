#Created by Gurvir Singh Sheridan College - Oct, 2024

import random
from sympy import randprime

# Function to generate large prime numbers using sympy's randprime
def generate_prime(size=1024):
    lower_bound = 2**(size - 1)
    upper_bound = 2**size - 1
    return randprime(lower_bound, upper_bound)

# Function to calculate the greatest common divisor (GCD) using Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to compute modular inverse using the extended Euclidean algorithm
def mod_inverse(e, phi):
    a, b = phi, e
    x0, x1 = 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
    return x0 % phi  # Return the modular inverse of e mod phi
