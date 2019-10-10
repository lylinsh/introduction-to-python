#coding=utf-8

import cv2
import os


def imgOperate(img_path):
    img = cv2.imread(img_path)
    cv2.namedWindow("image", 4)
    cv2.imshow("image", img)
    cv2.waitKey(0)


def videoOperate(video_pth, output_pth):
    videoCapture = cv2.VideoCapture(video_pth)
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    videoWriter = cv2.VideoWriter(
        output_pth, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
        fps, size)
    success, frame = videoCapture.read()
    i = 0
    while success and i < 200:
        i += 1
        print("\rSave {:3d} frame".format(i), end="")
        videoWriter.write(frame)
        cv2.waitKey(1)
        success, frame = videoCapture.read()
    videoCapture.release()


def cameraOperate(id_c):
    try:
        cameraCapture = cv2.VideoCapture(id_c)
        fps = 30
        size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        i = 0
        cv2.namedWindow("Camera", 0)
        success, frame = cameraCapture.read()
        while success and i < 100:
            i += 1
            print("\rSave {:3d} frame".format(i), end="")
            cv2.imshow("Camera", frame)
            cv2.waitKey(1)
            success, frame = cameraCapture.read()
        cameraCapture.release()
        cv2.destroyALLWindow()
    except:
        pass


if __name__=="__main__":
    video_in_pth = "./../data/video/00.mp4"
    video_out_pth = "./../data/video/00_copy.mp4"
    # imgOperate("./../data/00.jpg")
    # videoOperate(video_in_pth, video_out_pth)
    cameraOperate(0)