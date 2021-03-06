def qzhsh(num):
    lis = []
    tmp = True

    for n in range(2, num+1):
        for x in range(1, n):
            if (n % x == 0) and (x != 1):
                tmp = False
                break
        if tmp:
            print(n)

    return ', '.join(lis)
