num = 0
sum = 0

while num < 1000:
    if num % 3 == 0:
        sum += num
    elif num % 5 == 0:
        sum += num
    num += 1

print(sum)
