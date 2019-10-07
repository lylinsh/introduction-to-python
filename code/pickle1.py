#coding=utf-8

import pickle 
import yaml


def writeFile(filename, data):
    with open(filename, "ab") as f:
        pickle.dump(data, f)
    

def loadFile(filename):
    with open(filename, "rb") as f:
        rst = pickle.load(f) 
    return rst 


if __name__ == "__main__":
    test = [
        dict(name=r"./../data/num.pkl", value = 1), 
        dict(name=r"./../data/str.pkl", value="Hello world!"), 
        dict(name=r"./../data/list.pkl", value=[1, 2, 3, 4, 5, 6, 7]), 
        dict(name=r"./../data/dict.pkl", value={"a":1, "b":2, "c":3, "d":4}), 
        dict(name=r"./../data/set.pkl", value={1, 2, 3, 4, 5}), 
        dict(name=r"./../data/tuple.pkl", value=(1, 2))
    ]
    # for item in test:
        # print("the type and value of input data is: \n{}\n{}".format(
        #     type(item["value"]), item["value"]))
        # writeFile(item["name"], item["value"])
        # rst = loadFile(item["name"])
        # print("the type and value of data loaded is: \n{}\n{}".format(
        #     type(rst), rst))
        # print("\n")
    with open("./../data/tmp.pkl", "wb") as f:
        for item in test:
            print(item["value"])
            pickle.dump(item["value"], f)
    rst = []
    with open("./../data/tmp.pkl", "rb") as f:
        for i in range(len(test)):
            rst.append(pickle.load(f))
    print(rst)

        