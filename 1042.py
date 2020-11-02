num = input().split()

r = [num[0], num[1], num[2]]
for x in range(0, 3):
    for y in range(x, 3):
        if int(r[x]) > int(r[y]):
            s = r[x]
            r[x] = r[y]
            r[y] = s

print('{}\n{}\n{}\n\n{}\n{}\n{}'.format(r[0], r[1], r[2], num[0], num[1], num[2]))
