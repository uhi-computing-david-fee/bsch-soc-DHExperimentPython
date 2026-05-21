# prime_generator.py
#
# Handles prime number generation using the Miller-Rabin probabilistic
# primality test. See the discrete logarithm tutorial for an explanation
# of why efficient prime generation requires a probabilistic approach.

import random

MILLER_RABIN_ROUNDS = 20


def generate_prime(bit_length: int, seed: int = 42) -> int:
    """
    Generates a prime number of approximately the specified bit length.
    Larger bit lengths take longer to generate; this is expected and
    is itself an interesting observation for your investigation.
    """
    if bit_length < 8:
        raise ValueError("Bit length must be at least 8.")

    rng = random.Random(seed)

    while True:
        candidate = _generate_random_odd(bit_length, rng)
        if _is_miller_rabin_prime(candidate, MILLER_RABIN_ROUNDS, rng):
            return candidate


def find_primitive_root(p: int) -> int:
    """
    Finds a primitive root for the given prime p.
    A primitive root g ensures that g^k mod p cycles through all
    values from 1 to p-1, which is required for Diffie-Hellman security.
    """
    phi = p - 1
    prime_factors = _get_prime_factors(phi)

    for g in range(2, p):
        is_primitive_root = True

        for factor in prime_factors:
            if pow(g, phi // factor, p) == 1:
                is_primitive_root = False
                break

        if is_primitive_root:
            return g

    raise ValueError("No primitive root found.")


def _is_miller_rabin_prime(n: int, rounds: int, rng: random.Random) -> bool:
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False

    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(rounds):
        a = rng.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        composite = True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                composite = False
                break

        if composite:
            return False

    return True


def _generate_random_odd(bit_length: int, rng: random.Random) -> int:
    n = rng.getrandbits(bit_length)
    n |= (1 << (bit_length - 1))
    n |= 1
    return n


def _get_prime_factors(n: int) -> list[int]:
    factors = []
    temp = n
    i = 2
    while i * i <= temp:
        if temp % i == 0:
            factors.append(i)
            while temp % i == 0:
                temp //= i
        i += 1
    if temp > 1:
        factors.append(temp)
    return factors