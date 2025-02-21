def generate_prime_factors(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")

    if n == 1:
        return []

    prime_factors = []

    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2 

    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            prime_factors.append(factor)
            n //= factor
        factor += 2 
        
    if n > 2:
        prime_factors.append(n)

    return prime_factors
