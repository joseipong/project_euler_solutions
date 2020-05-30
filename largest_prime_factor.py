import math

def get_factors(num):
    factors = set()
    factor_limit = math.floor(math.sqrt(num)) + 1
    for i in range (2, factor_limit):
        if num % i == 0:
            factors.add(i)
            factors.add(int(num / i))
    return factors

def get_greatest_prime_factor(num):
    greatest_prime_factor = 2
    factors = get_factors(num)
    for factor in factors:
        is_prime = True
        for i in range(2, math.floor(math.sqrt(factor)) + 1):
            if factor % i == 0:
                is_prime = False
                break
        
        if is_prime and factor > greatest_prime_factor:
            greatest_prime_factor = factor
    
    return greatest_prime_factor

print (get_greatest_prime_factor(600851475143))