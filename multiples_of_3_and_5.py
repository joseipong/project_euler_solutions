def get_multiples_of_3_and_5(number):
    sum = 0
    for i in range (1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(get_multiples_of_3_and_5(1000))