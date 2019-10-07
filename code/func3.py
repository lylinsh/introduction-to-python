#coding=utf-8

def func1(l1):
    print(v1)
    l1[2] = 'a'
    print(id(l1))
    l1 = [1, 2, 3]
    print(id(l1))
    return "a", (1, 2)


def func2(v, l1):
    global v1
    v1 = 'b'


def func3(v1, l1):
    print(globals()["v1"])
    v1 = 'c'
    print(v1)


if __name__ == "__main__":
    l1 = [1, 2, 3, 4]
    v1 = "a"
    print(id(l1))
    v2, _ = func1(l1)
    print(v1, l1)
    print(id(l1))
    func2(v1, l1)
    func3(v1, l1)
    print(v1)
    