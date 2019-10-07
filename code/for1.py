#coding=utf-8

import math
from random import randint


if __name__ == "__main__":
    l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for item in l1:
        print("{:.2f}".format(math.sin(item)), end=" ")

    print("\n")
    print("The mutiple of 7 between 10 and 100 are:")
    for i in range(10, 100, 2):
        if math.gcd(i, 7) != 1:
            print(i, end=",")
    
    print("\n")
    l2 = [randint(10, 20) for i in range(10)]
    l3 = [randint(20, 30) for i in range(10)]
    print(l2, l3, sep="\n")

    l4 = [(a, b) for a in l2[:2] for b in l3[:3]]
    l5 = [a+b for a, b in zip(l2, l3) if a+b>40]
    print(l4, l5, sep="\n")

    ans = []
    for i in range(10, 20, 2):
        for j in range(10, 20, 2):
            if i+j > 25:
                continue 
            ans.append((i, j))
            if len(ans) == 6:
                break 
        if len(ans) == 6:
            break 
    print(i, j, ans, sep="\n")

    