class Solution:
    def evenFib(self, target: int, a=0, b=1):
        while a <= target:
            a, b = b, a + b
            if a % 2 == 0:
                yield a


# Project Euler Problem 2: https://projecteuler.net/problem=2
target = int(input("Enter the target number: "))
# print(list(evenFib(target)))
print(sum(Solution().evenFib(target)))
