'''
Date: Monday July 30, 2018
'''

'''
Print the multiplication table of a up to the b row
'''
def make_table(a, b = 10):
    spacing = 5
    if a > 0 and b > 0:
        print(f'{"a":5}{"b":5}{"a x b"}')

        for i in range(1, b + 1):
            print(f'{a:<5}{i:<5}{a*i}')

    else:
        print(a, "and", b, "both need to be positive integers")

    print()


if __name__ == '__main__':
    a = 5
    make_table(a)

    a = 7
    b = 3
    make_table(a, b)