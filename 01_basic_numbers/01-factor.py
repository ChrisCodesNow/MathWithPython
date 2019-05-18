'''
Date: Monday July 30, 2018
Update: Saturday May 18, 2019
'''

'''
Determines if b is a factor of a.
(int, int) -> (bool)
'''
def is_factor(a, b):
    if b == 0:
        return False

    return a % b == 0


'''
Find all factors of the integer num
(int) -> (array int)
'''
def get_factors(num):
    factors = []

    for i in range(1, num + 1):
        if is_factor(i, num):
            factors.append(i)
    return factors



# Test
class Test:
    count = 0
    def run(self, result):
        self.count += 1
        if result:
            print(f"Passed test {self.count}")
        else:
            print(f"Failed test {self.count}")


if __name__ == "__main__":
    t = Test()

    a = 100
    b = 25
    t.run(is_factor(a, b) == True)

    a = 49
    b = 7
    t.run(is_factor(a, b) == True)

    a = 103
    b = 1
    t.run(is_factor(a, b) == True)

    a = 37
    b = 25
    t.run(is_factor(a, b) == False)

    a = 100
    b = 0
    t.run(is_factor(a, b) == False)

    a = 100
    b = 3
    t.run(is_factor(a, b) == False)

