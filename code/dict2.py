#coding=utf-8

if __name__=="__main__":
    d1 = dict(v1=1, v2="abc", v3=[1, 2, 3])
    d2 = {"a":1, "b":2, "c":3, "d":4, "e":5}
    d3 = d1.copy()
    print(d3) 
    d3.clear()
    print(d3)
    d4 = dict.fromkeys(["1", "b", "c"])
    print(d4)
    print(d2.get("a"))
    l1 = d2.items()
    print(l1)
    n1 = d2.pop("e")
    print(n1, d2)
    t1 = d2.popitem()
    print(t1, d2)
    d2.setdefault("v1", "a")
    d2.setdefault("a", (1, 2))
    print(d2)
    d2.update(d1)
    print(d2)
    print(d2.values())

