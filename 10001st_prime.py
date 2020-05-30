def get_prime_number():
    # generate large enough list that would hopefully contain the prime number
    # assume every number is prime at the start
    prime_check = [True for i in range (1,1000000)]

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
    
    last_prime = 2
    count = 0
    for i in range(1, len(prime_check)):
        if prime_check[i]:
            last_prime = i + 1
            count += 1
        if count == 10001:
            return i + 1
    return "Did not reach 10001, last prime is " + str(last_prime) + " at position " + str(count)

print (get_prime_number())
