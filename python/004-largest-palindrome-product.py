class Solution:
    def palindromeProduct(self, min: int, max: int, res=0):
        for x in range(max, min, -1):
            for y in range(max, min, -1):
                # Numerical solution
                prod, rev = x * y, 0
                while prod > 0:
                    rev = rev * 10 + prod % 10
                    prod //= 10
                if x * y == rev and x * y > res:
                    res = x * y
                    break
                # String solution
                # if str(x * y) == str(x * y)[::-1] and x * y > res:
                #     res = prod
                #     break
                elif x * y < res:
                    break
        return res


print(Solution().palindromeProduct(1000, 10000))
