#coding=utf-8

from functools import cmp_to_key


if __name__ == "__main__":
    l1 = [[1, 2, 1], [4, 2], [1, 4], [3, 3], [5, 5]]

    def compare(x, y):
        kx = x[1]/x[0]
        ky = y[1]/y[0]
        if kx < ky:
            return 1
        elif kx == ky and x[1] < y[1]:
            return 1
        else:
            return -1
    
    l2 = sorted(l1, key=lambda x:x[1]/x[0])
    print(l2)

    l1.sort(key=cmp_to_key(compare))
    print(l1)