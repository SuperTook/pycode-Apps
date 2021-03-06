def qqhs(n):
    t = 0
    """
    求亲和数（n=几以内）
    """

    def find_yin(x):
        for i in range(1, x + 1):
            if (x % i == 0) and (i != x):  # 若i能整除n,则n是i的因数
                yield i

    for num in range(1, n + 1):
        a = num
        a_sum = sum([nm for nm in find_yin(a)])
        b = a_sum
        b_sum = sum([nm for nm in find_yin(b)])
        if (b_sum == a) and (a != b):  # 无需判断 a_sum == b, 因为前面的赋值操作 b = a_sum
            print(a, end=' ')  # print(a, b) 会造成重复，b再往后会被遍历并输出
            t += 1
        if t == 2:  # 2个一换行
            print()
            t = 0
