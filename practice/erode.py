import cv2 as cv
import numpy as np


def pic_dir():
    return 'e:/image/erode/'


src = cv.imread(pic_dir() + 'he2.png')

# 形态学——腐蚀操作
kernel = np.ones((3, 3), np.uint8)
erosion = cv.erode(src, kernel, iterations=1)  # iterations=1 迭代腐蚀次数/ 值越大腐蚀的越多

res = np.hstack((src, erosion))
cv.imshow('pic', erosion)
cv.waitKey(0)
cv.destroyAllWindows()
