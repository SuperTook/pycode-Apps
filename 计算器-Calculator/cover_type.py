def int_(*args):
    argl = list()
    for x in args:
        argl.append(int(x))
    return argl


def str_(*args):
    argl = list()
    for x in args:
        argl.append(str(x))
    return argl


def float_(*args):
    argl = list()
    for x in args:
        argl.append(float(x))
    return argl