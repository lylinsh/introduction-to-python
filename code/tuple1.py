#coding=utf-8


if __name__ == "__main__":
    tp1 = (1, 2, 3)
    tp2 = ()
    tp3 = tuple([4, 5, 6])
    print(tp1)
    print(tp3[0])
    try:
        tp1[1] = 0
    except TypeError:
        print("Tuple can not be modified!")
    tp4 = tp1 * 2
    print(tp4)
    tp5 = tp1 + tp3
    print(tp5)
    
    v1, v2, v3 = tp3 
    print(v1, v2, v3)

    
