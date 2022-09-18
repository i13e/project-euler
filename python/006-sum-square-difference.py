def arithmeticSeries(start, stop, step=1):
    terms = (stop - start) // step
    extrema = start + (stop - step)
    return terms * extrema // 2


def squareDifference(min: int, max: int):
    squared_sum = 0
    sum = arithmeticSeries(min, max + 1) ** 2
    for i in range(min, max + 1):
        squared_sum += i**2
    return sum - squared_sum


print(squareDifference(1, 100))
