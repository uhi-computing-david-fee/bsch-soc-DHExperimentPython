# experiment_runner.py
#
# Runs Diffie-Hellman exchange and discrete logarithm attack experiments
# across a range of prime bit lengths.

import time
from prime_generator import generate_prime, find_primitive_root
from diffie_hellman import DiffieHellman
from discrete_log_attack import attack as discrete_log_attack
from experiment_result import ExperimentResult


def run_experiment(bit_length: int, runs: int, seed: int = 42) -> list[ExperimentResult]:
    """
    Runs a complete experiment for a given prime bit length.
    Returns a list of results, one per run.
    """
    print(f"\n  Bit length: {bit_length}")
    results = []

    for run in range(1, runs + 1):
        print(f"  Run {run}/{runs}")

        prime_start = time.perf_counter()
        p = generate_prime(bit_length, seed=seed + run)
        g = 2 if bit_length > 64 else find_primitive_root(p)
        print(f"    g = {g} ({'fixed generator, see notes' if bit_length > 64 else 'primitive root'})")
        prime_ms = (time.perf_counter() - prime_start) * 1000

        print(f"    p = {p}")
        print(f"    g = {g}")
        print(f"    Prime generated in {prime_ms:.2f}ms")

        dh = DiffieHellman(p, g, seed=seed + run)
        exchange_start = time.perf_counter()
        success, shared_secret = dh.perform_exchange()
        exchange_ms = (time.perf_counter() - exchange_start) * 1000

        print(f"    Exchange: {'succeeded' if success else 'failed'}, "
              f"Time: {exchange_ms:.4f}ms")

        alice_private = dh.generate_private_key()
        alice_public = dh.compute_public_key(alice_private)

        recovered, iterations, attack_ms = discrete_log_attack(p, g, alice_public)
        attack_succeeded = recovered != -1

        if attack_succeeded and dh.compute_public_key(recovered) != alice_public:
            print("    WARNING: Recovered key does not verify correctly.")
            attack_succeeded = False

        print(f"    Attack: {'succeeded' if attack_succeeded else 'failed within limit'}, "
              f"Iterations: {iterations:,}, Time: {attack_ms:.2f}ms")

        results.append(ExperimentResult(
            bit_length=bit_length,
            run_number=run,
            prime_generation_ms=prime_ms,
            exchange_ms=exchange_ms,
            attack_succeeded=attack_succeeded,
            attack_iterations=iterations,
            attack_ms=attack_ms
        ))

    return results