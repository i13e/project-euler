def evenFib(limit):
    a, b = 1, 2
    while a <= limit:
        if a % 2 == 0:
            yield a
        a, b = b, a + b


print(sum(evenFib(4000000)))
