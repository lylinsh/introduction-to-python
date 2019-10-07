#coding=utf-8

if __name__ == "__main__":
    set0 = set()
    set1 = {1, 2, 3, 4}
    set1.add(1)
    set1.add(5)
    print("set0: {}".format(set0))
    print("set1: {}".format(set1))

    set3 = {"a", "b", "c"}
    set2 = set1.copy()
    set2.remove(2)
    n1 = set2.pop()
    print("n1 and set2 are: {}, {}"
            .format(n1, set2))
    set4 = set.union(set2, set3)
    set0.update(set3)
    set3.clear()

    d1 = dict(s0=set0, s1=set1, s2=set2,
                 s3=set3, s4=set4)

    print("""set0: {s0}\nset1: {s1}
            \rset2: {s2}\nset3: {s3}
            \rset4: {s4}""".format(**d1))

    l1 = list(set4)
    print("set to list:", l1)
    s1 = str(set4)
    print("set to string:", s1)
    t1 = tuple(set4)
    print("set to tuple: ", t1)

