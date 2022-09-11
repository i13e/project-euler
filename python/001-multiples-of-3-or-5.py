def multiplesOf(vars: list[int], limit: int) -> int:
    res = 0
    for num in range(1, limit):
        for multiple in vars:
            if num % multiple == 0:
                res += num
                break
    return res


print(multiplesOf([3, 5], 1000))
