#coding=utf-8

import math 
import cmath


if __name__=="__main__":
    n0 = 1
    print(id(n0))
    del(n0)
    try:
        print(id(n0))
    except:
        print("name 'n0' is not defined") 

    n1, n2 = 2, 3.0
    print(type(n1))
    print(type(n2))
    print(type(int(n2)))
    print(type(float(n1)))
    print(complex(n1, n2))

    n3, n4 = 7, 9.0
    print(n3 // n1)
    print(n4 // n1)

    n5 = n1**n2
    print(n5)
    
    n5 += n1 
    print(n5) 

    print(math.ceil(math.pi))
    print(math.floor(math.pi))
    print(round(math.pi))

    try:
        print(math.sqrt(-1))
    except:
        print("Negative data!")
    
    print(cmath.sqrt(-1))



