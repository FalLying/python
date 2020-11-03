hr = [int(i) for i in input().split()]

diminuihora = 0
if hr[1] > hr[3]:
    r = (hr[3] - hr[1])
    if r < 0:
        r = 60 + r
        diminuihora = 1
elif hr[1] < hr[3]:
    r = hr[3] - hr[1]
else:
    r = 0

if hr[0] > hr[2]:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24-hr[0]+hr[2]-diminuihora, r))
elif hr[0] < hr[2]:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hr[2] - hr[0]-diminuihora, r))
else:
    if r == 0:
        print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
    else:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hr[0] - hr[2] - diminuihora, r))
        