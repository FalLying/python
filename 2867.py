from math import pow, log10, floor

cases = int(input())

for _ in range(0, cases):
    nums = [int(i) for i in input().split()]
    r = floor(log10(pow(nums[0], nums[1])))+1
    print('{:.0f}'.format(r))
