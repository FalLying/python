qt = 0
seq = 0

def sequence(num):
    r = '0'
    global seq
    global qt
    qt = 0
    for i in range(0, num+1):
        for j in range(i):
            r += str(' {}'.format(i))
            qt += 1
    seq += 1
    return r


while True:
    try:
        N = sequence(int(input()))

        print('Caso {}: {} numero{}\n{}\n'.format(seq,  qt+1, 's' if qt >= 1 else '', N))

    except EOFError:
        break
