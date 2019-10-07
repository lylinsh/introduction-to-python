#coding=utf-8

if __name__ == "__main__":
    s1 = 'hello "world"!'
    s2 = "Convert a list to string: "
    s3 = """this is a string 
            \rin mutiple lines"""
    s4 = "This is another string " + \
        "in mutiple lines!"

    print(s1, s2, s3, s4, sep="\n")

    s7 = "hello world\n"
    s8 = r"hello world\n"
    print(s7, s8, sep="\n")

    s4 = str([1, 2, 3])
    print(len(s4))

    s5 = s4[1:-1]
    print(s5)
    try:
        s5[0] = '4'
    except TypeError:
        print("Cannot modify a string"+
                " through slice!")
    
    s6 = s2 + s4 
    print(s6)
    print("1 in list: {}"
            .format("1" in s4))

    n1, n2, n3 = 1, 2, 3
    l1 = {"n1":2, "n2":3, "n3":8}
    print("{} + {} = {}"
            .format(n1, n2, n3))
    print("{n3} - {n2} = {n1}"
            .format(n1=1, n2=2, n3=3))
    print("log{n1}({n3}) = {n2}"
            .format(**l1))

