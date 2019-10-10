import cv2 
import numpy as np 
from myos import * 


if __name__ == "__main__":
    img_dir = "./../data/img"
    paths = getPathAll(img_dir)
    # print(paths)
    for i, item in enumerate(paths):
        for j, img_pth in enumerate(item):
            # print(img_pth)
            img = cv2.imread(img_pth)
            if (np.array(img.shape) != np.array([256, 256, 3])).any():
                nh, nv, nd = np.array(img.shape) // np.array([256, 256, 3])
                img = np.split(img, nh, axis=0)[0]
                img = np.split(img, nv, axis=1)[0]
                print(img.shape)

            img = img[:256, :256, :]
            img = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0)
            img = cv2.copyMakeBorder(img, 2, 2, 2, 2, cv2.BORDER_CONSTANT, value=[255, 255, 255])
            if j == 0:
                img_set = img
                # print(img_set.shape)
            else:
                img_set = np.vstack((img_set, img))
                # img_set = np.concatenate((img_set, img), axis=0)
        if i == 0:
            img_all = img_set
        else:
            img_all = np.hstack((img_all, img_set))
            # img_all = np.concatenate((img_all, img_set), axis=1)
    cv2.imwrite("./../data/result.png", img_all)