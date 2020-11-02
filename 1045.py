from math import pow

num = [float(i) for i in input().split()]
num.sort(reverse=True)

x = float(num[0])
y = float(num[1])
z = float(num[2])

if x >= y+z:
    print('NAO FORMA TRIANGULO')
else:
    if pow(x, 2) == pow(y, 2)+pow(z, 2):
        print('TRIANGULO RETANGULO')
    elif pow(x, 2) > pow(y, 2)+pow(z, 2):
        print('TRIANGULO OBTUSANGULO')
    elif pow(x, 2) < pow(y, 2)+pow(z, 2):
        print('TRIANGULO ACUTANGULO')
    if x == y == z:
        print('TRIANGULO EQUILATERO')
    elif not (x != y != z):
        print('TRIANGULO ISOSCELES')
