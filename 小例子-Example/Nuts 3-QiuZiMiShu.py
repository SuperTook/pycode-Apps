def qzms(number):
    def get_num(num):
        s = 1
        for _ in range(num-1):
            s *= 10
        return s

    for i in range(get_num(number), get_num(number + 1)):
        sums = sum([eval(f'{x}**{number}') for x in str(i)])
        if sums == i:
            print(i, end=' ')
