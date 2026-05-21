# discrete_log_attack.py
#
# Brute force discrete logarithm attack against Diffie-Hellman.
#
# Given public parameters p and g, and a target public key A = g^a mod p,
# this attack attempts to recover the private key a by trying every
# possible value until g^x mod p equals A.
#
# For small primes this completes quickly. For large primes it becomes
# completely infeasible. Observing this transition is the core of the
# exercise.

import time

MAX_ITERATIONS = 10_000_000


def attack(p: int, g: int, public_key: int) -> tuple[int, int, float]:
    """
    Attempts to recover the private key from a public key.

    Returns a tuple of:
        recovered_key  - the recovered private key, or -1 if unsuccessful
        iterations     - number of iterations performed
        elapsed_ms     - time taken in milliseconds

    Implementation guidance:
        Find x such that g^x mod p equals public_key.
        Use an iterative approach: maintain a running value and update
        it with a single multiplication and modulo per step rather than
        recomputing g^x mod p from scratch each iteration.
        See the brute force attack tutorial for a full explanation.
    """

    # TODO: Implement the brute force discrete logarithm attack.
    raise NotImplementedError("Implement the attack here.")