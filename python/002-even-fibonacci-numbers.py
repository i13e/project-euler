def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def even(seq):
    for i in seq:
        if i % 2 == 0:
            yield i


def under(seq, limit):
    for i in seq:
        if i > limit:
            break
        yield i


print(sum(under(even(fib()), 4000000)))
