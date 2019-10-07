#coding=utf-8
from time import sleep


def flattenYield(netsed):
    for sublist in netsed:
        for element in sublist:
            print("yield an anser")
            yield element


def flattenReturn(netsed):
    ans = []
    for sublist in netsed:
        for element in sublist:
            print("return an anser")
            ans.append(element)
    return ans
    

if __name__=="__main__":
    netsed = [[1, 2], [3, 4], [5]]
    for num in flattenYield(netsed):
        print("Result of yield: {}".format(num))
    for num in flattenReturn(netsed):
        print("Result of function: {}".format(num))
