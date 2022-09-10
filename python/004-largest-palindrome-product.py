def palindromeProduct(min, max):
    result = 0
    for x in range(max, min, -1):
        for y in range(max, min, -1):
            product = x * y
            if str(product) == str(product)[::-1] and product > result:
                result = product
                break
            elif result > product:
                break
    return result


print(palindromeProduct(100, 1000))
