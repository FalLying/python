numberOfPhrases = int(input())

while numberOfPhrases > 0:
    words = input().split()
    words.sort(key=len, reverse=True)

    print(*words)

    numberOfPhrases -= 1
