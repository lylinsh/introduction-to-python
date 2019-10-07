#coding=utf-8

import csv 


def writeList(filename, header, rows):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f) 
        writer.writerow(header)
        writer.writerows(rows) 


def writeDict(filename, header, rows):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, header) 
        writer.writeheader()
        writer.writerows(rows)

    
def reader(filename):
    rst = []
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for item in reader:
            rst.append(item)
    return rst 


if __name__ == "__main__":
    l1 = ["a", "b", "c", "d", "e"]
    l2 = [[1, 2, 3, 4, 5], 
            [2, 3, 4, 5, 6]]
    l3 = [{"a":1, "b":2, "c":3, "d":4, "e":5}, 
            {"a":2, "b":3, "c":4, "d":5, "e":6}]

    writeList("./../data/list.csv", l1, l2)
    writeDict("./../data/dict.csv", l1, l3)

    rst_list = reader("./../data/list.csv")
    rst_dict = reader("./../data/dict.csv")

    print("the data saved as list is:\n", rst_list)
    print("the data saved as dict id:\n", rst_dict)
