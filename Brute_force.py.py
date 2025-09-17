import random
import string
import time
import itertools
import getpass

def is_valid_secret(secret, min_length=6, max_length=7):
    charset = string.ascii_letters + string.digits
    if not (min_length <= len(secret) <= max_length):
        return False
    return all(c in charset for c in secret)

def brute_force_sim(secret, print_frequency=1):
    length = len(secret)
    charset = string.ascii_letters + string.digits
    print(charset)  # charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    print(f"Starting brute-force sim on {length}-char password...")
    print(f"Character set size: {len(charset)} (letters + digits)")
    print(f"Max possible combos: {len(charset) ** length } (this might take time for 4 chars)")

    start_time = time.time()
    attempt=0

# Genrate and Try all the combos
   
    for combo in itertools.product(charset, repeat=length):
        attempt = attempt + 1
        guess = ''.join(combo)

        if attempt % print_frequency == 0 or guess == secret:
            print(f"Attempt #{attempt:06d}: Trying '{guess}'")

        if guess == secret:
            end_time = time.time()
            print(f"\nCracked! Password: {guess}")
            print(f"Attempts: {attempt}")
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            print("Vulnerability: Short passwords are easily cracked. Recommend 12+ chars, rate limiting.")
            return True
        
    print("Failed (error in the sim).")
    return False

# Main Program

secret = getpass.getpass("Enter a 3-4 character secret password (Letters/digits only, hidden): ")
while not is_valid_secret(secret):
    print("Invalid Must be 3-4 letters/digits only")
    secret = getpass.getpass("Try Again: ")

brute_force_sim(secret)







# print(is_valid_secret("Am24"))