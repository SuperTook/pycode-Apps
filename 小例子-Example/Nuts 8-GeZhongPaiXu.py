def sort1(lis):  # 冒泡
    lis_len = len(lis)
    for i in range(lis_len - 1):  # -1是为了防止<IndexError: index out of range>  # 需要遍历完整个序列
        for j in range(lis_len - 1 - i):  # -1同上，-i是因为最底下的都排过了
            if lis[j] > lis[j + 1]:  # 比较相邻的两个，若前面的>后面的，则换位
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
    return lis


def sort2(lis):  # 选择
    lis_len = len(lis)
    for i in range(lis_len):  # 需要遍历完整个序列
        min_idx = i  # 设：第一个为最小
        for j in range(i + 1, lis_len):
            if lis[j] < lis[min_idx]:  # 若<这个>小于第一个，改变索引
                min_idx = j
        lis[i], lis[min_idx] = lis[min_idx], lis[i]  # 换位
    return lis


def sort3(lis):  # 插入
    ln = len(lis)
    for i in range(1, ln):  # range(1, ln)的<1>是因为假定第一个是有序的
        j = i
        target = lis[i]  # 每次循环的一个待插入的数
        while j > 0 and target < lis[j - 1]:  # 比较、移动，给target腾位置
            lis[j] = lis[j - 1]
            j -= 1
        lis[j] = target
    return lis


def sort4(lis):  # 计数
    ret = []
    for num in range(min(lis), max(lis) + 1):
        x = 0
        for i in lis:
            if i == num:
                x += 1
        for i in range(x):
            ret.append(num)
    return ret


def sort5(lis):  # 自创（计数升级+列表推导=一行代码实现排序）
    # 语法糖形式：
    # ret = [k for j in [[i for i in lis if i == num] for num in range(min(lis), max(lis) + 1)] for k in j]
    #
    # 展开形式：
    ret = []
    for num in range(min(lis), max(lis) + 1):
        for i in lis:
            if i == num:
                ret.append(i)
    return ret


def sort6(lis):  # 快速
    if len(lis) >= 2:
        tmp_num = lis.pop(len(lis) // 2)  # 选取基准值，并从原始列表中移除基准值
        left = []   # 定义基准值左侧的列表
        right = []  # 定义基准值右侧的列表
        for num in lis:
            if num >= tmp_num:
                right.append(num)
            else:
                left.append(num)
        return sort6(left) + [tmp_num] + sort6(right)
    else:
        return lis
