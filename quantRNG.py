import secrets
import random

def display_coin(face):
    if face == "Heads":
        print("""
         _______
        /       \\
       |  HEADS  |
        \\_______/
        """)
    else:
        print("""
         _______
        /       \\
       |  TAILS  |
        \\_______/
        """)

def prng_flip():
    result = "Heads" if random.randint(0, 1) else "Tails"
    print("PRNG Flip Result:")
    display_coin(result)

def qrng_flip():
    result = "Heads" if secrets.randbits(1) else "Tails"
    print("QRNG Flip Result:")
    display_coin(result)

def main():
    print("Interactive Coin Flip Game: PRNG vs QRNG")
    print("-----------------------------------------------------------")
    while True:
        print("\nChoose an option:")
        print("1. Flip PRNG Coin")
        print("2. Flip QRNG Coin")
        print("3. Set PRNG Seed")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            prng_flip()
        elif choice == "2":
            qrng_flip()
        elif choice == "3":
            seed = int(input("Enter a seed for PRNG: "))
            random.seed(seed)
            print(f"PRNG seed set to {seed}.")
        elif choice == "4":
            print("Thanks for playing! 🔐")
            break
        else:
            print("Invalid input. Please choose a valid option.")

main()
