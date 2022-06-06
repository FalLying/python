while True:
    try:
        phrase = input()
        newPhrase = ''
        isFirst = True

        for letter in phrase:
            if (letter == ' '):
                newPhrase += ' '
            else:
                if (isFirst == True):
                    newPhrase += letter.upper()
                else:
                    newPhrase += letter.lower()
                isFirst = not isFirst
        print(newPhrase)
    except:
        break
