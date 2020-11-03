hr = [int(i) for i in input().split()]

if hr[0] > hr[1]:
    print('O JOGO DUROU {} HORA(S)'.format(24-hr[0]+hr[1]))
elif hr[0] < hr[1]:
    print('O JOGO DUROU {} HORA(S)'.format(hr[1] - hr[0]))
else:
    print('O JOGO DUROU 24 HORA(S)')
