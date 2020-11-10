while True:
    a, b = list(map(int, input().split()))

    if a <= 0 or b <= 0:
        break

    lista = []
    soma = 0
    if a > b:
        c = a
        a = b
        b = c
    for i in range(a, b+1):
        lista.append(i)
        soma += i
    lista.sort()

    print('{} Sum={}'.format(str(lista).strip('[]').replace(',', ''), soma))
