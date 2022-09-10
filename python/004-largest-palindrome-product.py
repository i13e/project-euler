def palindromeProduct(min, max):
    res = 0
    for x in range(max, min, -1):
        for y in range(max, min, -1):
            prod = tmp = x * y
            # Numerical solution
            if tmp % 10 == 0:
                continue
            rev = 0
            while tmp > rev:
                rev = rev * 10 + tmp % 10
                tmp = tmp // 10
            if (tmp == rev or tmp == rev // 10) and prod > res:
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
