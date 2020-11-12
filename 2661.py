from math import sqrt


def despojado(x):
    if x == 1:
        return False
    else:
        i = 2
        r = int(sqrt(x))

        primo, resultado = True, True

        while i <= r and resultado:
            if x % i**2 == 0:
                resultado = False
            elif x % i == 0:
                primo = False
            i += 1
        return (resultado and primo)


n = int(input())
resp = 0

for i in range(1, int(sqrt(n))):
    if n % i == 0:
        if despojado(i):
            resp += 1

        if i != n / i and despojado(n/i):
            resp += 1

print(int(2**resp-resp-1))

