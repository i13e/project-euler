class Solution:
    def nthPrime(self, n: int, count=2):
        for i in range(3, n**2, 2):
            k = 1
            while k**2 < i:
                k += 2
                if i % k == 0:
                    break
            else:
                count += 1
            if count == n:
                return i


print(Solution().nthPrime(10001))
