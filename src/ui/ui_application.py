# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'application.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import ui.ui_resource

class Ui_application(object):
    def setupUi(self, application):
        if not application.objectName():
            application.setObjectName(u"application")
        application.resize(1536, 809)
        application.setStyleSheet(u"background-color: rgb(221, 221, 221);")
        application.setAnimated(True)
        self.main = QWidget(application)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font: 16pt \"\u5b8b\u4f53\";\n"
"color:  rgb(179, 179, 179)")
        self.gridLayout = QGridLayout(self.main)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.infomation = QFrame(self.main)
        self.infomation.setObjectName(u"infomation")
        self.infomation.setStyleSheet(u"")
        self.infomation.setFrameShape(QFrame.StyledPanel)
        self.infomation.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.infomation)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.info_version = QLabel(self.infomation)
        self.info_version.setObjectName(u"info_version")
        self.info_version.setStyleSheet(u"font: 12pt \"\u5b8b\u4f53\";")
        self.info_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.info_version, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.infomation, 2, 1, 1, 1)

        self.control_bar = QFrame(self.main)
        self.control_bar.setObjectName(u"control_bar")
        self.control_bar.setMinimumSize(QSize(150, 0))
        self.control_bar.setStyleSheet(u"QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.control_bar.setFrameShape(QFrame.StyledPanel)
        self.control_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.control_bar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.info = QLabel(self.control_bar)
        self.info.setObjectName(u"info")
        self.info.setMinimumSize(QSize(0, 50))
        palette = QPalette()
        brush = QBrush(QColor(179, 179, 179, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(40, 44, 52, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(179, 179, 179, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.info.setPalette(palette)
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.info.setFont(font)
        self.info.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.info.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.info)

        self.btn_page_all = QPushButton(self.control_bar)
        self.btn_page_all.setObjectName(u"btn_page_all")
        self.btn_page_all.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.btn_page_all)

        self.btn_task1 = QPushButton(self.control_bar)
        self.btn_task1.setObjectName(u"btn_task1")
        self.btn_task1.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.btn_task1)

        self.btn_task2 = QPushButton(self.control_bar)
        self.btn_task2.setObjectName(u"btn_task2")
        self.btn_task2.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.btn_task2)

        self.btn_task3 = QPushButton(self.control_bar)
        self.btn_task3.setObjectName(u"btn_task3")
        self.btn_task3.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.btn_task3)

        self.btn_setting = QPushButton(self.control_bar)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.btn_setting)

        self.verticalSpacer = QSpacerItem(20, 525, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.control_bar, 1, 0, 2, 1)

        self.title = QFrame(self.main)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"")
        self.title.setFrameShape(QFrame.StyledPanel)
        self.title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.app_logo = QFrame(self.title)
        self.app_logo.setObjectName(u"app_logo")
        self.app_logo.setMinimumSize(QSize(0, 58))
        self.app_logo.setStyleSheet(u"")
        self.app_logo.setFrameShape(QFrame.StyledPanel)
        self.app_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.app_logo)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.info_jmu_logo = QLabel(self.app_logo)
        self.info_jmu_logo.setObjectName(u"info_jmu_logo")
        self.info_jmu_logo.setMinimumSize(QSize(180, 30))
        self.info_jmu_logo.setStyleSheet(u"image: url(:/image/resource/image/logo_jmu.png);")

        self.horizontalLayout_3.addWidget(self.info_jmu_logo)

        self.line = QFrame(self.app_logo)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(69, 76, 90);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.label = QLabel(self.app_logo)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.label)

        self.label_5 = QLabel(self.app_logo)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(180, 30))
        self.label_5.setStyleSheet(u"image: url(:/image/resource/image/logo_huawei.png);")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(17, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.info_app_title = QLabel(self.app_logo)
        self.info_app_title.setObjectName(u"info_app_title")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush3 = QBrush(QColor(33, 37, 43, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.info_app_title.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"\u5b8b\u4f53"])
        font1.setPointSize(24)
        font1.setBold(False)
        font1.setItalic(False)
        self.info_app_title.setFont(font1)
        self.info_app_title.setStyleSheet(u"font: 24pt \"\u5b8b\u4f53\";")
        self.info_app_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.info_app_title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.horizontalLayout.addWidget(self.app_logo)

        self.window_control_bar = QFrame(self.title)
        self.window_control_bar.setObjectName(u"window_control_bar")
        self.window_control_bar.setStyleSheet(u"QPushButton {\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"	border: none;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(33, 37, 43);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.window_control_bar.setFrameShape(QFrame.StyledPanel)
        self.window_control_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.window_control_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_min = QPushButton(self.window_control_bar)
        self.btn_min.setObjectName(u"btn_min")
        self.btn_min.setMaximumSize(QSize(30, 30))
        self.btn_min.setStyleSheet(u"background-image: url(:/icon/resource/icon/icon_minimize.png);\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_min)

        self.btn_max = QPushButton(self.window_control_bar)
        self.btn_max.setObjectName(u"btn_max")
        self.btn_max.setMaximumSize(QSize(30, 30))
        self.btn_max.setStyleSheet(u"background-image: url(:/icon/resource/icon/icon_maximize.png);\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_max)

        self.btn_close = QPushButton(self.window_control_bar)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMaximumSize(QSize(30, 30))
        self.btn_close.setStyleSheet(u"background-image: url(:/icon/resource/icon/icon_close.png);")

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.window_control_bar)


        self.gridLayout.addWidget(self.title, 0, 0, 1, 2)

        self.display = QFrame(self.main)
        self.display.setObjectName(u"display")
        self.display.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.display.setFrameShape(QFrame.StyledPanel)
        self.display.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.display)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.display_stack_widget = QStackedWidget(self.display)
        self.display_stack_widget.setObjectName(u"display_stack_widget")
        self.display_stack_widget.setStyleSheet(u"")
        self.p1_all = QWidget()
        self.p1_all.setObjectName(u"p1_all")
        self.gridLayout_6 = QGridLayout(self.p1_all)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.f_all = QFrame(self.p1_all)
        self.f_all.setObjectName(u"f_all")
        self.f_all.setFrameShape(QFrame.StyledPanel)
        self.f_all.setFrameShadow(QFrame.Raised)
        self.f_all.setLineWidth(1)
        self.gridLayout_5 = QGridLayout(self.f_all)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lb_p1_img_2 = QLabel(self.f_all)
        self.lb_p1_img_2.setObjectName(u"lb_p1_img_2")
        self.lb_p1_img_2.setMinimumSize(QSize(563, 150))
        self.lb_p1_img_2.setMaximumSize(QSize(563, 150))
        self.lb_p1_img_2.setStyleSheet(u"")
        self.lb_p1_img_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_p1_img_2, 1, 3, 2, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 24, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 0, 2, 1, 1)

        self.lb_info_2 = QLabel(self.f_all)
        self.lb_info_2.setObjectName(u"lb_info_2")
        self.lb_info_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_info_2, 3, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(114, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 3, 4, 1, 1)

        self.lb_p1_img_1 = QLabel(self.f_all)
        self.lb_p1_img_1.setObjectName(u"lb_p1_img_1")
        self.lb_p1_img_1.setMinimumSize(QSize(563, 150))
        self.lb_p1_img_1.setMaximumSize(QSize(563, 150))
        self.lb_p1_img_1.setStyleSheet(u"")
        self.lb_p1_img_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_p1_img_1, 1, 1, 1, 1)

        self.lb_info_4 = QLabel(self.f_all)
        self.lb_info_4.setObjectName(u"lb_info_4")
        self.lb_info_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_info_4, 6, 3, 1, 1)

        self.lb_info = QLabel(self.f_all)
        self.lb_info.setObjectName(u"lb_info")
        self.lb_info.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_info, 2, 1, 2, 1)

        self.horizontalSpacer_3 = QSpacerItem(114, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 2, 0, 2, 1)

        self.lb_info_3 = QLabel(self.f_all)
        self.lb_info_3.setObjectName(u"lb_info_3")
        self.lb_info_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_info_3, 6, 1, 1, 1)

        self.lb_p1_img_3 = QLabel(self.f_all)
        self.lb_p1_img_3.setObjectName(u"lb_p1_img_3")
        self.lb_p1_img_3.setMinimumSize(QSize(563, 150))
        self.lb_p1_img_3.setMaximumSize(QSize(563, 150))
        self.lb_p1_img_3.setStyleSheet(u"")
        self.lb_p1_img_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_p1_img_3, 5, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 24, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 7, 2, 1, 1)

        self.lb_p1_img_4 = QLabel(self.f_all)
        self.lb_p1_img_4.setObjectName(u"lb_p1_img_4")
        self.lb_p1_img_4.setMinimumSize(QSize(563, 150))
        self.lb_p1_img_4.setMaximumSize(QSize(563, 150))
        self.lb_p1_img_4.setStyleSheet(u"")
        self.lb_p1_img_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_p1_img_4, 5, 3, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 4, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 3, 2, 1, 1)


        self.gridLayout_6.addWidget(self.f_all, 0, 0, 1, 1)

        self.display_stack_widget.addWidget(self.p1_all)
        self.p2_depth = QWidget()
        self.p2_depth.setObjectName(u"p2_depth")
        self.gridLayout_7 = QGridLayout(self.p2_depth)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.f_p2_depth = QFrame(self.p2_depth)
        self.f_p2_depth.setObjectName(u"f_p2_depth")
        self.f_p2_depth.setFrameShape(QFrame.StyledPanel)
        self.f_p2_depth.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.f_p2_depth)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 179, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(57, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.lb_p2_img = QLabel(self.f_p2_depth)
        self.lb_p2_img.setObjectName(u"lb_p2_img")
        self.lb_p2_img.setMinimumSize(QSize(1126, 300))
        self.lb_p2_img.setMaximumSize(QSize(1126, 300))
        self.lb_p2_img.setStyleSheet(u"")
        self.lb_p2_img.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.lb_p2_img, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(57, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.lb_info_5 = QLabel(self.f_p2_depth)
        self.lb_info_5.setObjectName(u"lb_info_5")
        self.lb_info_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.lb_info_5, 2, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 179, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_6, 3, 1, 1, 1)


        self.gridLayout_7.addWidget(self.f_p2_depth, 0, 0, 1, 1)

        self.display_stack_widget.addWidget(self.p2_depth)
        self.p3_road = QWidget()
        self.p3_road.setObjectName(u"p3_road")
        self.gridLayout_9 = QGridLayout(self.p3_road)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.f_p3_road = QFrame(self.p3_road)
        self.f_p3_road.setObjectName(u"f_p3_road")
        self.f_p3_road.setFrameShape(QFrame.StyledPanel)
        self.f_p3_road.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.f_p3_road)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_8 = QSpacerItem(20, 197, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_8, 0, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_9, 1, 0, 1, 1)

        self.lb_p3_img = QLabel(self.f_p3_road)
        self.lb_p3_img.setObjectName(u"lb_p3_img")
        self.lb_p3_img.setMinimumSize(QSize(1126, 300))
        self.lb_p3_img.setMaximumSize(QSize(1126, 300))
        self.lb_p3_img.setStyleSheet(u"")
        self.lb_p3_img.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lb_p3_img, 1, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_10, 1, 2, 1, 1)

        self.lb_info_6 = QLabel(self.f_p3_road)
        self.lb_info_6.setObjectName(u"lb_info_6")
        self.lb_info_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lb_info_6, 2, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 197, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_7, 3, 1, 1, 1)


        self.gridLayout_9.addWidget(self.f_p3_road, 0, 0, 1, 1)

        self.display_stack_widget.addWidget(self.p3_road)
        self.p4_seg = QWidget()
        self.p4_seg.setObjectName(u"p4_seg")
        self.gridLayout_11 = QGridLayout(self.p4_seg)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.p4_seg)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_10 = QSpacerItem(20, 197, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_10, 0, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)

        self.lb_p4_img = QLabel(self.frame)
        self.lb_p4_img.setObjectName(u"lb_p4_img")
        self.lb_p4_img.setMinimumSize(QSize(1126, 300))
        self.lb_p4_img.setMaximumSize(QSize(1126, 300))
        self.lb_p4_img.setStyleSheet(u"")
        self.lb_p4_img.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.lb_p4_img, 1, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_12, 1, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 197, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_9, 3, 1, 1, 1)

        self.lb_info_7 = QLabel(self.frame)
        self.lb_info_7.setObjectName(u"lb_info_7")
        self.lb_info_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.lb_info_7, 2, 1, 1, 1)


        self.gridLayout_11.addWidget(self.frame, 0, 0, 1, 1)

        self.display_stack_widget.addWidget(self.p4_seg)
        self.p5_setting = QWidget()
        self.p5_setting.setObjectName(u"p5_setting")
        self.gridLayout_4 = QGridLayout(self.p5_setting)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.f_set = QFrame(self.p5_setting)
        self.f_set.setObjectName(u"f_set")
        self.f_set.setStyleSheet(u"QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.f_set.setFrameShape(QFrame.StyledPanel)
        self.f_set.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.f_set)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.verticalSpacer_12 = QSpacerItem(497, 289, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_12, 4, 1, 1, 3)

        self.verticalSpacer_11 = QSpacerItem(20, 244, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_11, 0, 2, 1, 1)

        self.btn_p5_select_video = QPushButton(self.f_set)
        self.btn_p5_select_video.setObjectName(u"btn_p5_select_video")
        self.btn_p5_select_video.setMinimumSize(QSize(120, 50))
        self.btn_p5_select_video.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px groove gray;\n"
"border-style: outset;")

        self.gridLayout_13.addWidget(self.btn_p5_select_video, 1, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(370, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_13, 3, 4, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_13.addItem(self.verticalSpacer_13, 2, 1, 1, 3)

        self.lb_p5_video_path = QLabel(self.f_set)
        self.lb_p5_video_path.setObjectName(u"lb_p5_video_path")
        self.lb_p5_video_path.setMinimumSize(QSize(0, 50))
        self.lb_p5_video_path.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px groove gray;\n"
"border-style: outset;")
        self.lb_p5_video_path.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.lb_p5_video_path, 1, 2, 1, 2)

        self.btn_p5_start = QPushButton(self.f_set)
        self.btn_p5_start.setObjectName(u"btn_p5_start")
        self.btn_p5_start.setMinimumSize(QSize(500, 50))
        self.btn_p5_start.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px groove gray;\n"
"border-style: outset;")

        self.gridLayout_13.addWidget(self.btn_p5_start, 3, 1, 1, 3)

        self.horizontalSpacer_6 = QSpacerItem(370, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_6, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.f_set, 0, 0, 1, 1)

        self.display_stack_widget.addWidget(self.p5_setting)

        self.gridLayout_3.addWidget(self.display_stack_widget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.display, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 5)
        self.gridLayout.setColumnStretch(0, 2)
        application.setCentralWidget(self.main)

        self.retranslateUi(application)

        self.display_stack_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(application)
    # setupUi

    def retranslateUi(self, application):
        application.setWindowTitle(QCoreApplication.translate("application", u"MainWindow", None))
        self.info_version.setText(QCoreApplication.translate("application", u"v1.3.1", None))
        self.info.setText(QCoreApplication.translate("application", u"\u83dc\u5355", None))
        self.btn_page_all.setText(QCoreApplication.translate("application", u"\u603b\u89c8", None))
        self.btn_task1.setText(QCoreApplication.translate("application", u"\u6df1\u5ea6\u56fe\u9884\u6d4b", None))
        self.btn_task2.setText(QCoreApplication.translate("application", u"\u9053\u8def\u9884\u6d4b", None))
        self.btn_task3.setText(QCoreApplication.translate("application", u"\u573a\u666f\u8bed\u4e49\u9884\u6d4b", None))
        self.btn_setting.setText(QCoreApplication.translate("application", u"\u8bbe\u7f6e", None))
        self.info_jmu_logo.setText("")
        self.label.setText("")
        self.label_5.setText("")
        self.info_app_title.setText(QCoreApplication.translate("application", u"\u667a\u80fd\u8de8\u6a21\u6001\u8857\u666f\u53ef\u89c6\u5316\u7cfb\u7edf", None))
        self.btn_min.setText("")
        self.btn_max.setText("")
        self.btn_close.setText("")
        self.lb_p1_img_2.setText("")
        self.lb_info_2.setText(QCoreApplication.translate("application", u"\u9884\u6d4b\u6df1\u5ea6\u56fe", None))
        self.lb_p1_img_1.setText("")
        self.lb_info_4.setText(QCoreApplication.translate("application", u"\u9884\u6d4b\u8bed\u4e49\u4fe1\u606f", None))
        self.lb_info.setText(QCoreApplication.translate("application", u"\u539f\u59cbRGB", None))
        self.lb_info_3.setText(QCoreApplication.translate("application", u"\u9884\u6d4b\u9053\u8def\u4fe1\u606f", None))
        self.lb_p1_img_3.setText("")
        self.lb_p1_img_4.setText("")
        self.lb_p2_img.setText("")
        self.lb_info_5.setText(QCoreApplication.translate("application", u"\u6df1\u5ea6\u56fe\u9884\u6d4b", None))
        self.lb_p3_img.setText("")
        self.lb_info_6.setText(QCoreApplication.translate("application", u"\u9053\u8def\u9884\u6d4b", None))
        self.lb_p4_img.setText("")
        self.lb_info_7.setText(QCoreApplication.translate("application", u"\u573a\u666f\u8bed\u4e49\u9884\u6d4b", None))
        self.btn_p5_select_video.setText(QCoreApplication.translate("application", u"\u9009\u62e9\u89c6\u9891\u6e90", None))
        self.lb_p5_video_path.setText("")
        self.btn_p5_start.setText(QCoreApplication.translate("application", u"\u5f00\u59cb\u63a8\u7406", None))
    # retranslateUi

