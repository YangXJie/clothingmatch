import cv2 as cv
import numpy as np


def pic_dir():
    return 'e:/image/'


src = cv.imread(pic_dir() + 'pic.jpg')

# 阈值
# ret, thresh = cv.threshold(src, 127, 255, cv.THRESH_BINARY)

'''
图像平滑
'''
# 均值滤波
blur = cv.blur(src, (3, 3))
# 方框滤波, 基本和均值滤波一样，可以选择归一化(normalize)，容易越界
box = cv.boxFilter(src, -1, (3, 3), normalize=True)
# 高斯滤波
aussian = cv.GaussianBlur(src, (5, 5), 1)
# 中值滤波
wedian = cv.medianBlur(src, 5)

res = np.hstack((src, blur, wedian))  # hstack:横着拼接    vstack:竖着拼接
print(type(res))
cv.imshow('pic', res)

cv.waitKey(0)  # 按任意键关闭窗口，cv2.waitKey(1000) 延时一秒关闭窗口
cv.destroyAllWindows()
