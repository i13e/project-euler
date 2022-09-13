def multiplesOf(vars, limit: int):
    for num in range(1, limit):
        for multiple in vars:
            if num % multiple == 0:
                yield num
                break


print(sum(multiplesOf([3, 5], 1000)))
