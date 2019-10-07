#coding=utf-8

import random 


if __name__=="__main__":
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]

    l1.append(l2)
    print(l1)
    
    l1 = [1, 2, 3]
    l1.extend(l2)
    print(l1)

    l3 = [random.randint(1, 20) for i in range(20)]
    print(l3)
    l3.sort() 
    print(l3)

    random.shuffle(l3)
    print(l3) 
    l3.sort(reverse=True)
    print(l3)

    random.shuffle(l3) 
    l4 = sorted(l3)
    print(l3)
    print(l4)

    l3.clear()
    print(l3)

    l3 = l4 
    print(id(l3))
    print(id(l4))
    l3[0] = -l3[0]
    print(l3, l4, sep='\n')

    l3 = l4.copy()
    print(id(l3))
    print(id(l4))

    l3[0] = -l3[0]
    print(l3, l4, sep='\n')

    print(l3.count(l3[1]))
    try:
        print(l3.index(10))
    except ValueError:
        print("can not find value")

    l3.insert(0, 21)
    print(l3) 

    n = l3.pop(0)
    print(n, l3) 

    l3.remove(l3[0]) 
    print(l3) 

    l3.reverse()
    print(l3)

    