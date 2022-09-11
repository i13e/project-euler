def palindromeProduct(min, max):
    res = 0
    for x in range(max, min, -1):
        for y in range(max, min, -1):
            prod = tmp = x * y
            # Numerical solution
            rev = 0
            while tmp > 0:
                rev = rev * 10 + tmp % 10
                tmp //= 10
            if (prod == rev or prod == rev // 10) and prod > res:
                res = prod
                break
            # String solution
            # if str(prod) == str(prod)[::-1] and prod > res:
            #     res = prod
            #     break
            elif prod < res:
                break
    return res


print(palindromeProduct(100, 1000))
