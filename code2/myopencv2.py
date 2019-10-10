import cv2 
import numpy as np 


def sobel(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_sobel = cv2.Sobel(img_gray, cv2.CV_16S, 1, 1, ksize=3)
    img_sobel = cv2.convertScaleAbs(img_sobel)
    return img_sobel


def canny(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_canny = cv2.Canny(img_gray, 200, 300)
    return img_canny
    # cv2.imshow("Canny", img_canny)


def laplace(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_laplace = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=3)
    img_laplace = cv2.convertScaleAbs(img_laplace)
    return img_laplace


def faceDect(img):
    face_cascade = cv2.CascadeClassifier("./../tools/haarcascades/haarcascade_frontalface_default.xml")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)
    return img


def myConv(img, kernel):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rst = cv2.filter2D(img_gray, -1, kernel)
    return rst


def medianBlur(img):
    return cv2.medianBlur(img, 3)


def gaussBlur(img, ksize, sigma):
    return cv2.GaussianBlur(img, ksize=ksize, sigmaX=sigma)


if __name__ == "__main__":
    img = cv2.imread("./../data/02.jpg")
    # img = cv2.resize(img, (512, 512))
    cv2.namedWindow("img", 0)
    # img_l = medianBlur(img)
    cv2.imshow("img", img)

    # kernel = np.array([[0.0947416, 0.118318, 0.0947416], 
    #                     [0.118318, 0.147761, 0.118318],
    #                     [0.0947416, 0.118318, 0.0947416]])
    # kernel = np.array([[0, -1, 0],
    #                     [-1, 4, -1], 
    #                     [0, -1, 0]])
    # img_my = myConv(img, kernel)
    # cv2.imshow("img_my", img_my)
    
    img = faceDect(img)
    cv2.imshow("img_detect", img)
    cv2.waitKey(0)

    