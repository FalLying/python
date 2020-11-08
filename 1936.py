nums = int(input())

n = int(nums)
c = 0

fats = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

while n != 0:
    for i in range(1, 9):
        if fats[i] >= n or i > 8:
            break
    if fats[i] <= n:
        n -= fats[i]
    else:
        n -= fats[i-1]
    c += 1

print(int(c))
