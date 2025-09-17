"""
main_demo.py

Interactive demo for the BruteForceSim repo.

Features:
- "continuous" demo mode: repeatedly generate a 3-4 char secret and brute-force it (educational only).
- Adjustable print frequency to reduce console spam.
- Live-percent progress printing and simple timing stats.
- Safe defaults: only letters+digits, short lengths (3-4) to keep demo fast.

Usage examples:

# Run a single demo (random 3-4 char secret)
python main_demo.py

# Run continuously, small delay between rounds
python main_demo.py --continuous --delay 1

# Control print frequency (print every N attempts)
python main_demo.py --print-frequency 5000

# Provide a secret (non-hidden) for demonstration
python main_demo.py --secret Am24

"""

import argparse
import itertools
import random
import string
import time
import sys


def is_valid_secret(secret, min_length=3, max_length=4):
    charset = string.ascii_letters + string.digits
    if not (min_length <= len(secret) <= max_length):
        return False
    return all(c in charset for c in secret)


def generate_random_secret(length=None):
    if length is None:
        length = random.choice([3, 4])
    charset = string.ascii_letters + string.digits
    return ''.join(random.choice(charset) for _ in range(length))


def brute_force_sim(secret, print_frequency=1000, show_guess=False):
    """Brute-force search for `secret` by iterating the full Cartesian product.

    - print_frequency: only print status every N attempts (to reduce spam)
    - show_guess: if True, prints each printed guess; otherwise prints a compact progress line
    """
    length = len(secret)
    charset = string.ascii_letters + string.digits
    total = len(charset) ** length

    start_time = time.time()
    attempt = 0

    # For nicer output, print a small header
    print(f"\n== Brute-force round: {length}-char secret ({total:,} combos) ==")
    last_print_time = start_time

    for combo in itertools.product(charset, repeat=length):
        attempt += 1
        guess = ''.join(combo)

        # Print status occasionally
        if attempt % print_frequency == 0 or guess == secret:
            now = time.time()
            elapsed = now - start_time
            rate = attempt / elapsed if elapsed > 0 else 0
            pct = (attempt / total) * 100
            remaining = max(total - attempt, 0)
            eta = (remaining / rate) if rate > 0 else float('inf')

            if show_guess:
                print(f"Attempt #{attempt:,}: Trying '{guess}'")
            else:
                # Compact single-line status using carriage return + flush
                status = (
                    f"Attempt: {attempt:,}/{total:,} ({pct:.3f}%) | "
                    f"Rate: {rate:.0f} it/s | Elapsed: {elapsed:.2f}s | ETA: {eta:.2f}s"
                )
                # Use \r to overwrite the same line when possible
                sys.stdout.write('\r' + status)
                sys.stdout.flush()

        if guess == secret:
            end_time = time.time()
            total_time = end_time - start_time
            print()  # newline after compact status
            print(f"\n*** Cracked! Password: {guess}")
            print(f"Attempts: {attempt:,}")
            print(f"Time taken: {total_time:.2f} seconds")
            print("Recommendation: Use longer passphrases (12+ chars), hashing, and server-side rate limiting.")
            return True

    # Should not reach here for valid inputs
    print("\n[!] Failed to crack the secret (unexpected).")
    return False


def demo_loop(args):
    """Run continuous demo rounds until interrupted."""
    round_num = 0
    try:
        while True:
            round_num += 1
            if args.secret:
                secret = args.secret
            else:
                secret = generate_random_secret(args.length)

            if not is_valid_secret(secret, 3, 4):
                print(f"Skipping invalid secret '{secret}' (must be 3-4 alnum chars)")
                continue

            print(f"\n[Round {round_num}] Secret generated: {'(hidden)' if not args.show_secret else secret}")
            brute_force_sim(secret, print_frequency=args.print_frequency, show_guess=args.show_guess)

            if not args.continuous:
                break

            # Delay between rounds (so output is readable)
            time.sleep(args.delay)

    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting demo.")


def parse_args():
    p = argparse.ArgumentParser(description="BruteForceSim interactive demo")
    p.add_argument("--continuous", action="store_true", help="Keep generating secrets and cracking them in a loop")
    p.add_argument("--delay", type=float, default=1.0, help="Delay in seconds between rounds when continuous")
    p.add_argument("--print-frequency", type=int, default=1000, help="Print status every N attempts (increase to reduce spam)")
    p.add_argument("--secret", type=str, default=None, help="Use a specific secret for the demo (non-hidden)")
    p.add_argument("--length", type=int, choices=[3, 4], default=None, help="Force generated secret length (3 or 4)")
    p.add_argument("--show-secret", dest="show_secret", action="store_true", help="Print generated secret in output (not hidden)")
    p.add_argument("--show-guess", dest="show_guess", action="store_true", help="Print each printed guess explicitly (more verbose)")
    return p.parse_args()


if __name__ == '__main__':
    args = parse_args()

    # Quick sanity: if user provided a secret, validate it
    if args.secret and not is_valid_secret(args.secret, 3, 4):
        print("Provided secret is invalid. Must be 3-4 characters, letters and digits only.")
        sys.exit(2)

    demo_loop(args)
