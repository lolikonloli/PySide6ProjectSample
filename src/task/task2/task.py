from application import Application
from task._task.default_camera_task import DefaultCameraTask


class Task2(DefaultCameraTask):
    def __init__(self, app: Application, video: str = None, delay: int = 30, parent=None) -> None:
        super().__init__(app, video, delay, parent)
        self.signal_change_pixmap.connect(app.set_task2_image)
