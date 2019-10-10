import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


if __name__=="__main__":
    t  = np.arange(-np.pi, np.pi, np.pi/100)
    x = np.cos(t)
    y = np.sin(t)
    fig = plt.figure()
    plt.title("circle")
    plt.xlabel("x=cos(t)")
    plt.ylabel("y=sin(t)")
    plt.plot(x, y, label="circle", color="r")
    plt.show()
    plt.savefig("./../data/circle.png")