while True:
    qtAlunos = int(input())
    if qtAlunos == 0:
        break
    totalGasto = 0
    for i in range(qtAlunos):
        totalGasto += float(input())

    resultado = totalGasto / qtAlunos
    print('${:.2f}'.format(resultado))
