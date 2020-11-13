while True:
    try:
        num = input()
        r = ''
        e = False
        for _ in num:
            if _ in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                r += str(_)
            elif _ == 'o' or _ == 'O':
                r += str('0')
            elif _ == 'l':
                r += str('1')
            elif _ not in (' ', ','):
                e = True
        if e:
            r = 'error'
        else:
            if len(r) == 0:
                r = 'error'
            elif int(r) > 2147483647:
                r = 'error'
            else:
                r = int(r)
        print(r)
    except EOFError:
        break
