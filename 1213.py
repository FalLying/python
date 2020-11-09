while True:
    try:
        n = int(input())
        t = 1
        c = 1
        while t % n != 0:
            t = (10 * t + 1) % n
            c += 1
        else:
            print(c)

    except EOFError:
        break
