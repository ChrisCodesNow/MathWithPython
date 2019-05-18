'''
Date: Monday July 30, 2018
'''

'''
Determines if a is a factor of b.
Assumes a and b are integers
'''
def is_factor(a, b):
    return b % a == 0;


'''
Find all factors of the integer num
'''
def get_factors(num):
    ## For a positive integer num, all its possible factors are the integer i,

    ## List with found factors
    L = []

    ## Search all possible factors
    for i in range(1, num + 1):
        if is_factor(i, num):
            L.append(i)
    return L

## Test code


if __name__ == "__main__":
    from random import randint
    def test_is_factor():
        for i in range(50):
            a = randint(2, 11)
            b = randint(1, 97)
            if is_factor(a, b):
                print(a, "and", b, "are factors")
            else:
                pass
                #print(a, "NOT in", b)

    def test_get_factors():
        ## Generate 10 random numbers, find their factors
        numbers = [randint(1, 97) for i in range(10)]
        for num in numbers:
            ## Print factors, if any
            factors = get_factors(num)
            if len(factors) > 0:
                print(num, "has the follow factors:")
                print(factors)

    test_is_factor()
    test_get_factors()
