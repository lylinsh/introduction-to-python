#coding=utf-8

import time


def loop():
    j = 0
    for i in range(10000000):
        j += 1
        if i % 1000000 == 0:
            time.sleep(0.1)


if __name__ == "__main__":
    t1 = time.time() 
    loop()
    t2 = time.time() 
    print("time cost measure by " + 
        "time.time() is: {}s".format(t2-t1))

    t3 = time.process_time()
    loop()
    t4 = time.process_time() 
    print("time cost measure by " + 
        "time.process_time() is: {}s".format(t4-t3)) 

    t5 = time.perf_counter()
    loop()
    t6 = time.perf_counter() 
    print("time cost measure by " + 
        "time.perf_counter() is: {}s".format(t6-t5)) 
