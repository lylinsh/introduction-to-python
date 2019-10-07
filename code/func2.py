#-*-coding:utf-8-*-

def func1(data_in, ksize, stride, padding, rate, bias, name=None):
    pass


def func2(data_in, ksize, *params, name=None):
    print(params)


def func3(data_in, ksize, **params):
    print(params)


if __name__=="__main__":
    data_in = [[None], [None]]
    ksize = [2, 3, 3, 32]
    stride = 1
    padding = "SAME"
    bias = None
    rate = 1
    name = None
    func1(data_in, ksize, stride, padding, rate, bias, name)
    func2(data_in, ksize, stride, padding, rate, bias, name)
    func3(data_in, ksize, stride=stride, padding=padding,
             rate=rate, bias=bias, name=name)
    d1 = dict(stride=stride, padding=padding,
             rate=rate, bias=bias, name=name)
    func3(data_in, ksize, **d1)

