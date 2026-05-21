# main.py
#
# Entry point for the Diffie-Hellman experiment application.
# Menu-driven interface; follow the prompts to run experiments.

import os
import sys
from experiment_runner import run_experiment
from result_reporter import write_results


def handle_run() -> None:
    print("\n-- Run Experiments --")
    print("Suggested bit lengths:")
    print("  Small (attack feasible):    8, 12, 16, 20, 24")
    print("  Medium (transition zone):   28, 32, 40")
    print("  Large (attack infeasible):  48, 64, 128")
    print("  Note: do not exceed 128 bits. Prime generation above")
    print("  this size becomes impractically slow.")

    bit_lengths = prompt_bit_lengths()
    runs = prompt_int("Number of runs per bit length: ", min_val=1)
    results_file = prompt_path("Results file path (e.g. results/results.csv): ")

    os.makedirs(os.path.dirname(results_file) if os.path.dirname(results_file) else ".", exist_ok=True)

    print(f"\nRunning experiments...")
    print(f"Bit lengths: {', '.join(str(b) for b in bit_lengths)}")
    print(f"Runs per bit length: {runs}")

    for bit_length in bit_lengths:
        results = run_experiment(bit_length, runs)
        write_results(results, results_file)

    print(f"\nResults written to: {results_file}")


def prompt_bit_lengths() -> list[int]:
    while True:
        value = input("Bit lengths: ").strip()
        if not value:
            print("Please enter at least one bit length.")
            continue

        bit_lengths = []
        valid = True

        for s in value.split(","):
            try:
                bl = int(s.strip())
                if bl < 8:
                    raise ValueError
                bit_lengths.append(bl)
            except ValueError:
                print(f"Invalid bit length: {s.strip()}. All values must be integers of at least 8.")
                valid = False
                break

        if valid and bit_lengths:
            return bit_lengths


def prompt_int(message: str, min_val: int = None) -> int:
    while True:
        try:
            value = int(input(message).strip())
            if min_val is not None and value < min_val:
                print(f"Please enter a value of at least {min_val}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")


def prompt_path(message: str) -> str:
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Please enter a valid file path.")


def main() -> None:
    print("\nDiffie-Hellman Experiment")
    print("=========================")

    running = True
    while running:
        print("\nWhat would you like to do?")
        print("  1. Run experiments")
        print("  2. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            handle_run()
        elif choice == "2":
            running = False
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()