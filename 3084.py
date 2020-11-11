while True:
    try:
        h, m = input().split()
        h = int(h)
        m = int(m) * 10

        rh = int(h / 30)
        rm = int(m / 60)

        print('{:0>2}:{:0>2}'.format(rh, rm))
    except EOFError:
        break
