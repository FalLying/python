from fractions import Fraction

while True:
    try:

        num = int(input())

        casos = num*num
        qtCasos = 0
        l = int(num/2)

        for i in range(2, l):
            qtCasos += num % i

        rem = num % (l + 1)
        qtCasos += ((1+rem)*rem) if rem > 1 else rem

        r = Fraction(qtCasos, casos)
        print('0/1' if r == 0 else r)
    except EOFError:
        break
