n, m = list(map(int, input().split()))


def check(i, j):
    try:
        if i == 0:
            return False
        elif t[i-1][j-1] == 7 and t[i-1][j] == 7 and t[i-1][j+1] == 7\
                and t[i][j-1] == 7 and t[i][j+1]\
                and t[i+1][j-1] == 7 and t[i+1][j] == 7 and t[i+1][j+1] == 7:
            return True
    except:
        return False


t = []

for i in range(n):
    t.append(list(map(int, input().split())))

a, b, f = 0, 0, False

for i in range(n):
    for j in range(m):
        if t[i][j] == 42:
            if check(i, j):
                a, b = i, j
                f = True
                break
    if f:
        break
if f:
    a += 1
    b += 1

print(a, b)
