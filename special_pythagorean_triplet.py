# this solution is quite slow as it is brute force, might need to improve this
def get_special_pythagorean_triplet():
    for a in range (1, 501):
        for b in range (1, 501):
            for c in range (1, 501):
                if a**2 + b**2 == c**2:
                    print ("Found a pythagorean triplet! " + str(a) + " " + str(b) + " " + str(c))
                    if a + b + c == 1000:
                        print ("Pythagorean triplet equal to 1000: " + str(a) + " " + str(b) + " " + str(c))
                        print ("Product is: " + str(a*b*c))
                        return

get_special_pythagorean_triplet()