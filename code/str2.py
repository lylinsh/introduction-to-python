#coding=utf-8

from random import randint


if __name__=="__main__":
    s1 = ("  Whether you're new to programming " +
            "or an experienced developer, it's " +
            "easy to learn and use Python.  ")
    print(s1.encode("ASCII"))
    # print(s1.encode("UTF-32"))
    l1 = s1.split("'") 
    s2 = s1.strip()
    print(l1)
    print(s2) 
    s3 = " ".join(l1).strip()
    print(s3)

    l2 = [randint(0, 5) for i in range(20)]
    s4 = str(l2) 
    if s4.find("2") != -1:
        print(s4.count("2"))
        s5 = s4.replace("2", "a")
        print(s5)
    
    s5 = s4.center(100, "*")
    print(s5)

    print(s2.upper())
    