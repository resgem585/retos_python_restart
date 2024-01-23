def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(start, end):
    """Generate prime numbers in the given range."""
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

def main():
    """Generate and display prime numbers between 1 to 250, and store in results.txt."""
    primes = generate_primes(1, 250)

    # Display primes
    print("Prime numbers between 1 to 250:")
    print(primes)

    # Store primes in results.txt
    with open("results.txt", "w") as file:
        for prime in primes:
            file.write(str(prime) + "\n")

if __name__ == "__main__":
    main()