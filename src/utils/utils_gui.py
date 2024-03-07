from PySide6.QtWidgets import QFileDialog, QLabel


#读取文件夹 并设置到label上
def read_and_set_file_path(app, messege: str, label: QLabel):
    path = QFileDialog.getExistingDirectory(app, messege)
    label.setText(path)
    return path

def read_and_set_file_path(app, messege: str, label: QLabel, dir: str = None):
    path = QFileDialog.getOpenFileName(app, messege, dir)[0]
    label.setText(path.split("/")[-1])
    return path