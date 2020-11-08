pula = 0
while True:
    try:
        ano = int(input())
        b = ''
        bissexto = 0
        normal = 1

        if pula:
            print('')
        pula = 1

        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print('This is leap year.')
            bissexto = 1
            normal = 0
        if ano % 15 == 0:
            print('This is huluculu festival year.')
            normal = 0
        if ano % 55 == 0 and bissexto:
            print('This is bulukulu festival year.')
        if normal:
            print('This is an ordinary year.')

    except EOFError:
        break