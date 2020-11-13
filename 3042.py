while True:
    num = int(input())
    if num == 0:
        break
    pos = []
    for _ in range(num):
        pos.append([int(i) for i in input().split()])
    jogador = 1
    p = 1
    qt = 0
    for i in range(0, num):
        for x, j in enumerate(pos[i]):
            if pos[i][jogador] == 0:
                break
            elif j == 0:
                p = x
                break

        if p != jogador:
            if p > jogador:
                r = p - jogador
            else:
                r = jogador - p
            if r >= 2:
                qt += 2
            else:
                qt += 1
            jogador = p

    print(qt)
