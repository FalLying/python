salario = float(input())

r = 0
g = 0
p = 0

if 0 <= salario <= 400:
    g = salario * .15
    p = 15
elif 400.01 <= salario <= 800:
    g = salario * .12
    p = 12
elif 800.01 <= salario <= 1200:
    g = salario * .10
    p = 10
elif 1200.01 <= salario <= 2000:
    g = salario * .07
    p = 7
else:
    g = salario * .04
    p = 4

r = salario + g

print(
    'Novo salario: {:.2f}\n'
    'Reajuste ganho: {:.2f}\n'
    'Em percentual: {} %'.format(r, g, p)
)
