#coding=utf-8

import math 


def func1(x):
    """return the result of log"""
    return math.log(x)


def func2(m, n=2):
    """return the result of log(m, n)"""
    return math.log(m, n)


if __name__ == "__main__":
    x = 8
    y = func1(x)
    print("the log of {:.2f} is: {:.2f}".format(x, y))
    print("the explaination of func1:", func1.__doc__)
    m, n = 8, 2
    y1 = func2(m)
    y2 = func2(m=m)
    y3 = func2(m=m, n=n)
    ans = {"n":n, "m":m, "y1":y1, "y2":y2, "y3":y3}
    print("the result of log{n}({m}) is: \
            {y1}, {y2}, {y3}".format(**ans))

