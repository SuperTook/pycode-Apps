def fzys(n):
    lis = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    index = 0
    numbers = 0

    while True:
        item = lis[index]
        if n % item == 0:
            print(item, end=' ')
            n /= item
            numbers += 1
        elif index < lis.__len__()-1:
            index += 1
        else:
            break

    if not numbers:  # if numbers == 0:
        print(n)
