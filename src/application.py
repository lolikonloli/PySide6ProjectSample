# pyside6
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QThread, Signal, Qt, Slot
from PySide6.QtGui import QMovie
from PySide6.QtGui import QPixmap, QImage
from ui.ui_application import Ui_application
from ui.ui_resource import *

from utils.utils_mat import transform_mat_to_qpixel
import cv2
from utils.utils_gui import read_and_set_file_path


class Application(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_application()
        self.ui.setupUi(self)

        self.page_init()
        self.slot_init()

    def slot_init(self):
        self.ui.btn_p5_select_video.clicked.connect(self.select_video)
        self.ui.btn_p5_start.clicked.connect(self.video_play)

    @Slot(cv2.Mat)
    def set_task1_image(self, frame):
        self.ui.lb_p1_img_1.setPixmap(transform_mat_to_qpixel(frame, 563, 150))

    @Slot(cv2.Mat)
    def set_task2_image(self, frame):
        self.ui.lb_p1_img_2.setPixmap(transform_mat_to_qpixel(frame, 563, 150))
        self.ui.lb_p2_img.setPixmap(transform_mat_to_qpixel(frame, 1126, 300))

    @Slot(cv2.Mat)
    def set_task3_image(self, frame):
        self.ui.lb_p1_img_3.setPixmap(transform_mat_to_qpixel(frame, 563, 150))
        self.ui.lb_p3_img.setPixmap(transform_mat_to_qpixel(frame, 1126, 300))

    @Slot(cv2.Mat)
    def set_task4_image(self, frame):
        self.ui.lb_p1_img_4.setPixmap(transform_mat_to_qpixel(frame, 563, 150))
        self.ui.lb_p4_img.setPixmap(transform_mat_to_qpixel(frame, 1126, 300))

    def page_init(self):
        self.ui.btn_page_all.clicked.connect(lambda: self.ui.display_stack_widget.setCurrentIndex(0))
        self.ui.btn_task1.clicked.connect(lambda: self.ui.display_stack_widget.setCurrentIndex(1))
        self.ui.btn_task2.clicked.connect(lambda: self.ui.display_stack_widget.setCurrentIndex(2))
        self.ui.btn_task3.clicked.connect(lambda: self.ui.display_stack_widget.setCurrentIndex(3))
        self.ui.btn_setting.clicked.connect(lambda: self.ui.display_stack_widget.setCurrentIndex(4))

    @Slot()
    def select_video(self):
        if not hasattr(self, "task_1"):
            from task.task1.task import Task1
            from task.task2.task import Task2
            from task.task3.task import Task3
            from task.task4.task import Task4

            raw_video_path = read_and_set_file_path(self, "选择视频源", self.ui.lb_p5_video_path, "../")
            video_name = raw_video_path.split("/")[-1]
            self.video_name = video_name

            delay = 50
            self.task_1 = Task1(self, f"../demo/raw/{video_name}", delay)
            self.task_2 = Task2(self, f"./demo/depth/{video_name}", delay)
            self.task_3 = Task3(self, f"./demo/road/{video_name}", delay)
            self.task_4 = Task4(self, f"./demo/segmentation/{video_name}", delay)
        else:
            raw_video_path = read_and_set_file_path(self, "选择视频源", self.ui.lb_p5_video_path, "../")
            video_name = raw_video_path.split("/")[-1]
            self.video_name = video_name

    @Slot()
    def video_play(self):
        if not self.task_1.isRunning():
            self.task_1.start()
            self.task_2.start()
            self.task_3.start()
            self.task_4.start()
        else:
            self.task_1.new_video_path = f"../demo/raw/{self.video_name}"
            self.task_2.new_video_path = f"./demo/depth/{self.video_name}"
            self.task_3.new_video_path = f"./demo/road/{self.video_name}"
            self.task_4.new_video_path = f"./demo/segmentation/{self.video_name}"
