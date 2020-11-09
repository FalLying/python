n = int(input())

for i in range(0, n):
    num = input()
    r = 0
    for _ in num:
        l = int(_)
        if l in (2, 3, 5):
            r += 5
        elif l == 1:
            r += 2
        elif l == 4:
            r += 4
        elif l in (6, 9, 0):
            r += 6
        elif l == 8:
            r += 7
        elif l == 7:
            r += 3
    print(r, 'leds')
