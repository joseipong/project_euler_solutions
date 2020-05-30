def get_sum_square_difference(nums):
    square_of_sums = sum(nums) ** 2
    sum_of_squares = sum([i**2 for i in nums])
    return abs(square_of_sums - sum_of_squares)

print (get_sum_square_difference([num for num in range (1,101)]))