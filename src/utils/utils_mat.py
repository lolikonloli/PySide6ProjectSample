import cv2


def transform_pixel(img: cv2.Mat, input_num: int, output_num: int):
    target = img.copy()
    target[target == input_num] = output_num
    return target


import cv2
from PySide6 import QtCore
from PySide6.QtGui import QImage, QPixmap


def transform_mat_to_qpixel(img: cv2.Mat, width: int = None, height: int = None):
    cv_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    qt_img = QImage(cv_img, cv_img.shape[1], cv_img.shape[0], cv_img.strides[0], QImage.Format_RGB888)
    if width:
        qt_pixel = QPixmap(qt_img).scaled(width, height)
    else:
        qt_pixel = QPixmap(qt_img)
    return qt_pixel
