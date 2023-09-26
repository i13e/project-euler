class Solution:
    def nthPrime(self, n: int, count=2):
        for i in range(3, n**2, 2):
            k = 1
            for k in range(3, int(i**0.5) + 1, 2):
                if i % k == 0:
                    break
            else:
                count += 1
            if count == n:
                return i


print(Solution().nthPrime(10001))
