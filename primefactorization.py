def prime_factorization(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

# Example usage:
number_to_factorize = 56
result = prime_factorization(number_to_factorize)

print(f"Prime factorization of {number_to_factorize}: {result}")
