while True:
    try:
        clones = int(input())
        clonado = 0
        while clones > 0:
            if clones % 2 == 0:
                clones /= 2
                clonado += 1
            else:
                break
        print(clonado)
    except EOFError:
        break
