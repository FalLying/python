from decimal import Decimal


def fib(x):
    o = 1.618034

    a = Decimal(o)**Decimal(x)
    b = Decimal(1)-Decimal(o)**Decimal(x)

    y = ((a-b)/Decimal(2.236067))
    return y


while True:
    try:
        n, m = map(int, input().split())
        if n <= 3:
            print(1)
        else:
            r = Decimal(fib(fib(n))) % Decimal(m)
            print('{:.0f}'.format(r))
    except EOFError:
        break
