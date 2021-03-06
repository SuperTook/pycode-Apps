def fbnqs(n):
    i = 0
    j = 1
    for _ in range(n):
        print(i, end=' ')
        i += j
        print(j, end=' ')
        j += i
