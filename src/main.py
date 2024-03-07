# ----------------------------------- 注释开始 ----------------------------------- #
# 图片大小 563*150
# ----------------------------------- 注释结束 ----------------------------------- #

from PySide6.QtWidgets import QApplication

# from qt_material import apply_stylesheet

from application import Application


if __name__ == "__main__":
    q_appication = QApplication()
    app = Application()
    app.show()
    q_appication.exec()
