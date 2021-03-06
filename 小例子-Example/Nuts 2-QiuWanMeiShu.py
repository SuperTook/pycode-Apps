def qwms(num):
    def find_yin(x):
        for n in range(1, x+1):
            if (x % n == 0) and (n != x):
                yield n

    for i in range(5, num+1):
        if sum([j for j in find_yin(i)]) == i:
            print(i)
