# experiment_result.py
#
# Data class holding the result of a single experimental run.
# You do not need to modify this file.

from dataclasses import dataclass


@dataclass
class ExperimentResult:
    bit_length: int
    run_number: int
    prime_generation_ms: float
    exchange_ms: float
    attack_succeeded: bool
    attack_iterations: int
    attack_ms: float