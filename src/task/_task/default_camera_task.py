from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QPixmap
import cv2

from application import Application
from utils.utils_mat import transform_mat_to_qpixel


class DefaultCameraTask(QThread):
    signal_change_pixmap = Signal(cv2.Mat)

    def __init__(self, app: Application, video: str = None, delay: int = 30, parent=None) -> None:
        super().__init__(parent)

        self.video_path = video
        self.new_video_path = None
        self.delay = delay

    def run(self):
        cap = cv2.VideoCapture(self.video_path)

        while True:
            if self.new_video_path is not None:
                self.video_path = self.new_video_path
                self.new_video_path = None
                cap.release()
                cap = cv2.VideoCapture(self.video_path)

            if cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    self.signal_change_pixmap.emit(frame)
                    QThread.msleep(self.delay)
