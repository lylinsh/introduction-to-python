#coding=utf-8

class Base(object):
    def __init__(self):
        super(Base, self).__init__()
        print("Base")
        self.n = 0
    
    def setN(self, n):
        self.n = 0
        print("class Base", self.n)

class A(Base):
    def __init__(self):
        super(A, self).__init__()
        self.n = 1
        print("class A") 
    
    def setN(self, n):
        super().setN(n)
        self.n = n
        print("class A", self.n)


class B(Base):
    def __init__(self):
        super(B, self).__init__()
        self.n = 2
        print("class B")
    
    def setN(self, n):
        super().setN(n)
        self.n = -n 
        print("class B", self.n)


class C(A, B):
    def __init__(self, n):
        self.n = 3
        super(C, self).__init__() 
        print(self.n)
        print("class C")
    
    def setN(self, n):
        super().setN(n)
        self.n = 2*n 
        print("Class C", self.n)
        print(self.n)
        A.setN(self, n)
        print(self.n)
        B.setN(self, n)
        print(self.n) 


class D(object):
    n0 = 1
    __n1 = 0
    def __init__(self, n):
        self.n2 = n

    def setN0(self, n):
        D.n0 = n
    
    def setN1(self, n):
        D.__n1 = n 
    
    def getN1(self):
        return D.__n1


if __name__ == "__main__":
    c1 = C(4)
    print(C.__mro__)
    c1.setN(5)

    d1 = D(2) 
    d2 = D(3)
    print("the n0 of class1 and class2 are: {}, {}".format(d1.n0, d2.n0))
    print("the n2 of class1 and class2 are: {}, {}".format(d1.n2, d2.n2))
    try:
        print(d1._n1)
    except:
        print("Can not get the private value directly!")
    d1.setN1(4)
    print(d1._D__n1)
    n3 = d2.getN1()
    print(n3)  

