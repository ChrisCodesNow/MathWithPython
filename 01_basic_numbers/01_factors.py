'''
Date: Monday July 30, 2018
Update: Saturday May 18, 2019
'''

'''
Find all factors of the integer num
(int) -> (array int)
'''
def get_factors(num):
    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
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

    num = 25
    factors = sorted(get_factors(num))
    ans = sorted([1, 25, 5])
    t.run(factors == ans)

    num = 17
    factors = sorted(get_factors(num))
    ans = sorted([1, 17])
    t.run(factors == ans)

    num = 100
    factors = sorted(get_factors(num))
    ans = sorted([1, 100, 2, 50, 4, 25, 5, 20, 10])
    t.run(factors == ans)

