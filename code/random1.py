#coding=utf-8

import random 
from random import randint 
from random import shuffle
from random import gauss


def displayFloatList(list_in):
    for item in list_in:
        print("{:.2f}".format(item), end=" ")
    print()


if __name__ == "__main__":
    l1 = [random.random() for i in range(10)]
    l2 = [gauss(0, 1) for i in range(10)]
    l3 = [randint(0, 10) for i in range(10)]

    print("l1:")
    displayFloatList(l1)

    print("l2:")
    displayFloatList(l2)

    l3.sort()
    print("l3:")
    print("Before shuffle:", l3, sep="\n")
    shuffle(l3)
    print("After shuffle:", l3, sep="\n")
