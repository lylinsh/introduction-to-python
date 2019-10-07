#coding=utf-8

if __name__ == "__main__":
    print("Initial List:")
    l1 = [1, 2, 3]
    print(l1[1])
    l2 = l1 + [4, 5, 6]
    print(l2)
    l3 = l2 * 3
    print(l3)
    l3[1] = 7
    print(l3)

    print("\nSlice index:")
    l4 = l3[6:]
    l5 = l3[:2]
    l6 = l3[2:5]
    l7 = l3[3:-1]
    l8 = l3[::2]
    print(l4, l5, l6, l7, l8, sep='\n')

    print("\nThe warning of multiply!")
    l9 = [l2]
    print(id(l9))
    l9 = l9 * 3
    print(id(l9))
    print(l9)
    l9[0][2] = 7
    print(l9)
    print(id(l9[0]))
    print(id(l9[1]))
    print(id(l9[2]))
    print(l2)
    l9 = [l2[:], l2[:], l2[:]]
    l9[0][2] = 3
    print(l9)
    print(id(l9[0]))
    print(id(l9[1]))
    print(id(l9[2]))

    print("\nCommon mathods:")
    print("")
    print(7 in l3)
    print(9 in l3)
    print("len of ls and l9 are: "+
    "{}, {}".format(len(l3), len(l9)))
    print("min and max of l3 are:"+
    "{}, {}".format(min(l3), max(l3)))

