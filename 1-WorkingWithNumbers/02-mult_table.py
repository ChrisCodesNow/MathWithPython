'''
Date: Monday July 30, 2018
'''

'''
For positive integers a and b, print the multiplication table
of a up to the b row
'''
def make_table(a, b = 10):
    if a > 0 and b > 0:
        for i in range(1, b + 1):
            print(a, "X", i, "=", a * i)

    else:
        print(a, "and", b, "both need to be positive integers")


## Test Method
if __name__ == "__main__":
    def test_make_table():
        make_table(1)

    test_make_table()
