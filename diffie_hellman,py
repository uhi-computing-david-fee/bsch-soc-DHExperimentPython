# diffie_hellman.py
#
# Implements the Diffie-Hellman key exchange protocol.
#
# Protocol summary:
#   1. Both parties agree on public parameters: prime p and generator g
#   2. Alice chooses private key a, computes public key A = g^a mod p
#   3. Bob chooses private key b, computes public key B = g^b mod p
#   4. Alice computes shared secret: B^a mod p
#   5. Bob computes shared secret:  A^b mod p
#   Both arrive at the same value: g^(ab) mod p

import random


class DiffieHellman:

    def __init__(self, p: int, g: int, seed: int = 42):
        self.p = p
        self.g = g
        self._rng = random.Random(seed)

    def generate_private_key(self) -> int:
        return self._rng.randint(2, self.p - 2)

    def compute_public_key(self, private_key: int) -> int:
        return pow(self.g, private_key, self.p)

    def compute_shared_secret(self, received_public_key: int, private_key: int) -> int:
        return pow(received_public_key, private_key, self.p)

    def perform_exchange(self) -> tuple[bool, int]:
        alice_private = self.generate_private_key()
        bob_private = self.generate_private_key()

        alice_public = self.compute_public_key(alice_private)
        bob_public = self.compute_public_key(bob_private)

        alice_shared = self.compute_shared_secret(bob_public, alice_private)
        bob_shared = self.compute_shared_secret(alice_public, bob_private)

        return alice_shared == bob_shared, alice_shared