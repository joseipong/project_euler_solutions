def get_largest_palindrome_product():
    largest_palindrome_product = 1
    for i in range (100, 1000):
        for j in range (100, 1000):
            product = i * j
            string_prod = str(product)[::-1]
            if str(product) == string_prod:
                if product > largest_palindrome_product:
                    largest_palindrome_product = product
                    
    return largest_palindrome_product

print (get_largest_palindrome_product())
