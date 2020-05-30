import math

def get_prime_factors(num):
    is_prime = True
    factors1 = []
    factors2 = []
    if num == 1:
        return []
    if num == 2:
        return [2]
    for i in range (2, num):
        if num % i == 0:
            factors1 = get_prime_factors(i)
            factors2 = get_prime_factors(int(num / i))
            is_prime = False
            break
    if is_prime:
        return [num]
    else:
        return factors1 + factors2

def get_smallest_multiple(nums):
    smallest_multiple = 1
    prime_factor_frequency = {}
    for num in nums:
        prime_factors = get_prime_factors(num)
        for factor in prime_factors:
            if factor not in prime_factor_frequency:
                prime_factor_frequency[factor] = prime_factors.count(factor)
            else:
                count = prime_factors.count(factor)
                if count > prime_factor_frequency[factor]:
                    prime_factor_frequency[factor] = count
    for factor in prime_factor_frequency:
        smallest_multiple = smallest_multiple * (factor ** prime_factor_frequency[factor])
    
    return smallest_multiple

print (get_smallest_multiple([num for num in range(1,21)]))