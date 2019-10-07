#coding=utf-8

if __name__=="__main__":
    s1 = input("Please input a sentense:\n")
    print("the sentense input is: ", s1)
    words = s1.split() 
    l = len(words)
    for item in words:
        print(item)
    for item in words:
        print(item, end=" ")
    print("\n")
    print("Python", "is", "easy!", sep=",")

