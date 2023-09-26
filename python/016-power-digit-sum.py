def powerDigits(num, power):
    num **= power
    while num > 0:
        yield num % 10
        num //= 10


print(sum(powerDigits(2, 1000)))
