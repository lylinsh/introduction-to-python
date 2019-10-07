#coding=utf-8

import re 


if __name__ == "__main__":
    s1 = r"Hello, *world!*"
    pat1 = re.compile(r"\*([^\*]+)\*")
    s2 = re.sub(pat1, r'<em>\1</em>', s1)
    print(s2)

    pat2 = re.compile(r'[a-z\-\.]+@[a-z\-\.]+', re.IGNORECASE)
    addresses = set()
    with open("./../data/string.txt", "r") as f:
        string = f.read()
        address = pat2.findall(string)
        addresses = set(address)
        print(addresses)
        