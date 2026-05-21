# result_reporter.py
#
# Writes experiment results to a CSV file.
# Results are appended if the output file already exists.

import os
from experiment_result import ExperimentResult


def write_results(results: list[ExperimentResult], output_file: str) -> None:
    os.makedirs(os.path.dirname(output_file) if os.path.dirname(output_file) else ".", exist_ok=True)
    file_exists = os.path.isfile(output_file)

    with open(output_file, "a") as f:
        if not file_exists:
            f.write("BitLength,RunNumber,PrimeGenerationMs,ExchangeMs,"
                    "AttackSucceeded,AttackIterations,AttackMs\n")

        for r in results:
            f.write(
                f"{r.bit_length},"
                f"{r.run_number},"
                f"{r.prime_generation_ms:.4f},"
                f"{r.exchange_ms:.4f},"
                f"{r.attack_succeeded},"
                f"{r.attack_iterations},"
                f"{r.attack_ms:.4f}\n"
            )