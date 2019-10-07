#coding=utf-8

if __name__=="__main__":
    d1 = dict(v1=1, v2="abc", v3=[1, 2, 3])
    d2 = {"a":"1", "b":2, "c":3, "d":4, "e":5}
    d3 = dict([("v1", 1), ("v2", 2), ("v3", 3)])
    d4 = {}
    d4["a"] = 1
    d4["b"] = 2
    d4["c"] = 3
    print(d1, d2, d3, d4, sep="\n")
    print(len(d2))
    del d2["d"]
    print(len(d2))
    if "e" in d2:
        print("key was in d2!")
    else:
        print("Can not find key in d2")
    
    