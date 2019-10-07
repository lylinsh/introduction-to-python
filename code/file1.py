#coding=utf-8

if __name__ == "__main__":
    n1 = 1
    str1 = "Hello World!"
    list1 = ["1", "2", "3", "4", "5"]
    dict1 = {"a":1, "b":2}
    tuple1 = (1, 2)
    set1 = {1, 2, 3}

    filename1 = "./../data/file.txt"
    filename2 = "./../data/filecopy.txt"

    f1 = open(filename1, "w") 
    f1.write(str(n1)+"\n")
    f1.close()

    f2 = open(filename1, "a")
    f2.write(str(list1)+"\n")
    f2.write(str(dict1)+"\n")
    f2.write(str(tuple1)+"\n")
    f2.write(str(set1)+"\n")
    f2.close()

    with open(filename1, "r") as f1, \
        open(filename2, "w") as f2:
        lines = f1.readlines()
        print("Data in file: ")
        for line in lines:
            print(line, end="")
        f2.writelines(lines)
    
    with open(filename2, "a") as f3:
        f3.writelines(list1)

    with open(filename2, "r") as f4:
        data = f4.read()
        print("\nAfter append data:\n" + data)
