# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vehicle-Detector.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1427, 696)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1149, 110, 211, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_folder = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_folder.setAutoFillBackground(False)
        self.pushButton_folder.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"C:\Users\AKSHAY\Desktop\Veichel Detection\Veichel Detection\icons\Folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_folder.setIcon(icon)
        self.pushButton_folder.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_folder.setFlat(True)
        self.pushButton_folder.setObjectName("pushButton_folder")
        self.horizontalLayout.addWidget(self.pushButton_folder)
        self.pushButton_Link = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Link.setMouseTracking(False)
        self.pushButton_Link.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(r"C:\Users\AKSHAY\Desktop\Veichel Detection\Veichel Detection\icons/icon_vid.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Link.setIcon(icon1)
        self.pushButton_Link.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_Link.setFlat(True)
        self.pushButton_Link.setObjectName("pushButton_Link")
        self.horizontalLayout.addWidget(self.pushButton_Link)
        self.pushButton_webcam = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_webcam.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(r"C:\Users\AKSHAY\Desktop\Veichel Detection\Veichel Detection\icons/icon_webcam.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_webcam.setIcon(icon2)
        self.pushButton_webcam.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_webcam.setFlat(True)
        self.pushButton_webcam.setObjectName("pushButton_webcam")
        self.horizontalLayout.addWidget(self.pushButton_webcam)
        self.label_Source = QtWidgets.QLabel(self.centralwidget)
        self.label_Source.setEnabled(True)
        self.label_Source.setGeometry(QtCore.QRect(1120, 180, 281, 21))
        self.label_Source.setObjectName("label_Source")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(1130, 460, 231, 121))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4_ScoreBoard = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4_ScoreBoard.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4_ScoreBoard.setObjectName("label_4_ScoreBoard")
        self.horizontalLayout_2.addWidget(self.label_4_ScoreBoard)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Total_lcdNumber_2 = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_2)
        self.Total_lcdNumber_2.setEnabled(True)
        self.Total_lcdNumber_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Total_lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Total_lcdNumber_2.setProperty("intValue", 6)
        self.Total_lcdNumber_2.setObjectName("Total_lcdNumber_2")
        self.verticalLayout.addWidget(self.Total_lcdNumber_2)
        self.safe_lcdNumber_4 = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_2)
        self.safe_lcdNumber_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.safe_lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.safe_lcdNumber_4.setProperty("intValue", 6)
        self.safe_lcdNumber_4.setObjectName("safe_lcdNumber_4")
        self.verticalLayout.addWidget(self.safe_lcdNumber_4)
        self.Low_lcdNumber_3 = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_2)
        self.Low_lcdNumber_3.setAutoFillBackground(False)
        self.Low_lcdNumber_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Low_lcdNumber_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Low_lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Low_lcdNumber_3.setProperty("intValue", 6)
        self.Low_lcdNumber_3.setObjectName("Low_lcdNumber_3")
        self.verticalLayout.addWidget(self.Low_lcdNumber_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.label_4_ScoreBoard_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_4_ScoreBoard_2.setGeometry(QtCore.QRect(1200, 600, 91, 31))
        self.label_4_ScoreBoard_2.setObjectName("label_4_ScoreBoard_2")
        self.label_3_MediaFrame = QtWidgets.QLabel(self.centralwidget)
        self.label_3_MediaFrame.setGeometry(QtCore.QRect(10, 20, 1101, 621))
        self.label_3_MediaFrame.setAutoFillBackground(True)
        self.label_3_MediaFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3_MediaFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3_MediaFrame.setText("")
        self.label_3_MediaFrame.setObjectName("label_3_MediaFrame")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1190, 360, 131, 31))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(1170, 260, 160, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_start = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_start.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(r"C:\Users\AKSHAY\Desktop\Veichel Detection\Veichel Detection\icons/play.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_start.setIcon(icon3)
        self.pushButton_start.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_start.setFlat(True)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_3.addWidget(self.pushButton_start)
        self.pushButton_stop = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_stop.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(r"C:\Users\AKSHAY\Desktop\Veichel Detection\Veichel Detection\icons/stopq.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_stop.setIcon(icon4)
        self.pushButton_stop.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_stop.setFlat(True)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout_3.addWidget(self.pushButton_stop)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1152, 50, 211, 20))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1427, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionVideo = QtWidgets.QAction(MainWindow)
        self.actionVideo.setObjectName("actionVideo")
        self.actionImage = QtWidgets.QAction(MainWindow)
        self.actionImage.setObjectName("actionImage")
        self.actionCam_Feed = QtWidgets.QAction(MainWindow)
        self.actionCam_Feed.setObjectName("actionCam_Feed")
        self.menuOpen.addAction(self.actionVideo)
        self.menuOpen.addAction(self.actionImage)
        self.menuOpen.addAction(self.actionCam_Feed)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Source.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Select the Source for Detection</span></p></body></html>"))
        self.label_4_ScoreBoard.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Total Vehicle </span><span style=\" font-size:10pt; color:#000000;\">--</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Safe  </span><span style=\" font-size:10pt; font-weight:600; color:#00aa00;\">--</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Risk  </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">--</span></p></body></html>"))
        self.label_4_ScoreBoard_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">MONITOR</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Control Panel</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Vehicle Detection</span></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionVideo.setText(_translate("MainWindow", "Video"))
        self.actionImage.setText(_translate("MainWindow", "Image"))
        self.actionCam_Feed.setText(_translate("MainWindow", "Cam Feed"))
