N = int(input())

inp = 0
out = 0

for i in range(N):
    X = int(input())
    if 10 <= X <= 20:
        inp += 1
    else:
        out += 1

print('{} in\n{} out'.format(inp, out))
