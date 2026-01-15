import math
# import sympy



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return -1
    return a / b

def power(base, exponent):
    return math.pow(base, exponent)

def sqrt(value):
    if value < 0:
        return -1
    return math.sqrt(value)

def factorial(n):
    if n < 0:
        return -1
    return math.factorial(n)

def logarithm(value, base=10):
    if value <= 0 or base <= 1:
        return -1
    return math.log(value, base)

def sine(angle_rad):
    return math.sin(angle_rad)

def cosine(angle_rad):
    return math.cos(angle_rad)

def tangent(angle_rad):
    return math.tan(angle_rad)

def is_prime(n):
    """Return True if `n` is prime, False otherwise.

    Strategy:
    - Handle small values and simple divisibility checks (2 and 3).
    - For numbers that fit within 64 bits, use optimized trial division
      testing divisors of the form 6k +/- 1 up to sqrt(n).
    - For very large integers (bit length > 64) delegate to
      `sympy.isprime()` for a fast, well-tested result.
    """
    try:
        n = int(n)
    except (TypeError, ValueError):
        return False

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # For very large numbers, delegate to sympy which implements
    # fast probabilistic/deterministic tests suited for big integers.
    # i basically dont even know i saw this approach on stack

    # if n.bit_length() > 64:
    #     return bool(sympy.isprime(n))

    # triak division for smaller ints
    limit = math.isqrt(n)
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

