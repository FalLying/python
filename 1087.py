while(1):
    x1, y1, x2, y2 = list(map(int, input().split()))

    if [x1, x2, y1, y2].count(0) == 4:
        break

    if x1 == x2 and y1 == y2:
        print('0')
    elif x1 == x2 or y1 == y2 or abs(x2-x1) == abs(y2-y1):
        print('1')
    else:
        print('2')
