def squareDifference(min, max):
    sum, squared_sum = 0, 0
    for i in range(min, max + 1):
        sum += i
        squared_sum += i**2
    return sum**2 - squared_sum


print(squareDifference(1, 100))
