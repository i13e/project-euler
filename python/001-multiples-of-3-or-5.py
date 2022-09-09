def multiples_of_3_or_5(limit):
    for num in range(1, limit):
        if not num % 3 or not num % 5:
            yield num


print(sum(multiples_of_3_or_5(1000)))
