def get_sum_of_even_fibonacci_numbers(num):
    prev_num = 1
    cur_num = 1
    sum = 0
    while cur_num < num:
        if cur_num % 2 == 0:
            sum += cur_num
        next_num = prev_num + cur_num
        prev_num = cur_num
        cur_num = next_num
    return sum

print (get_sum_of_even_fibonacci_numbers(4000000))