target = 600851475143
left = 0
right = target - 1


while left <= right:
    mid = (left + right) // 2
    if target % mid == 0:
        break
