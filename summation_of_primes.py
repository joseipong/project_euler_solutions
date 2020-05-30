def get_sum_of_primes(num):
    # assume every number is prime at the start
    prime_check = [True for i in range (1,num + 1)]

    # then we filter out non-primes
    for i in range(2, len(prime_check)):
        current_num = i
        if prime_check[i-1]:
            count = 2
            current_num = i * count
            
            while (current_num < len(prime_check) + 1):
                prime_check[current_num - 1] = False
                count += 1
                current_num = i * count
    
    sum = 0
    count = 0
    for i in range(1, len(prime_check)):
        if prime_check[i]:
            sum += (i + 1)
    return sum

print (get_sum_of_primes(2000000))