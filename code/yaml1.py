#coding=utf-8

import yaml 


if __name__ == "__main__":
    l1 = [0, (1, 2), 3, 4, {"a":1, "b":[1, 2], "c":"aaa"}, [6, 7]]
    d1 = {"a":1, "b":2, "c":3, "d":4, "e":5}
    s1 = r"Hello world!"   
    set1 = {1, 2, 3, 4, 5}
    t1 = (1, 2)
    with open("./../data/tmp.yaml", "w") as f:
        yaml.dump(l1, f)
        f.write("---\n")
        yaml.dump(d1, f)
        f.write("---\n")
        yaml.dump(s1, f)
        f.write("---\n")
        yaml.dump(set1, f)
        f.write("---\n")
        yaml.dump(t1, f)
    with open("./../data/tmp.yaml", "r") as f:
        r1 = yaml.full_load_all(f)
        for item in r1:
            print(item)
            