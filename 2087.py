import re

while True:
    num = int(input())
    if num == 0:
        break
    words = []
    for _ in range(num):
        words.append(input())
    words = sorted(words, key=len)
    r = False

    for i, j in enumerate(words):
        for l in range(0, num):
            if l == i or len(j) > len(words[l]):
                continue
            k = words[l]
            k = k[0:len(words[i])].strip()
            if re.search(words[i], k):
                r = True
                break
        if r:
            break
    if r:
        print('Conjunto Ruim')
    else:
        print('Conjunto Bom')
