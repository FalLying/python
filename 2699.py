I = [str(i) for i in input().split()]

if I[0][0] == '?':
    I[0] = str(I[0]).replace('?', '1', 1)

S = int(I[0].replace('?', '0'))
N = int(I[1])
L = len(I[0])

if (N % 2 == 0) and (int(I[0][L-1]) % 2 != 0):
    S = '*'
else:
    while len(str(S)) == L:
        if S % N == 0:
            break
        else:
            S += 1
    else:
        S = '*'

print(S)
