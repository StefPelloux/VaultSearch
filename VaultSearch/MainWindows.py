# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1070, 660)
        MainWindow.setMinimumSize(QSize(1070, 660))
        MainWindow.setMaximumSize(QSize(3000, 2000))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(187, 193, 200, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush2 = QBrush(QColor(62, 62, 62, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Courier New")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamily(u"Courier New")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.label.setPalette(palette1)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineurl = QLineEdit(self.centralwidget)
        self.lineurl.setObjectName(u"lineurl")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineurl.sizePolicy().hasHeightForWidth())
        self.lineurl.setSizePolicy(sizePolicy)
        self.lineurl.setMinimumSize(QSize(500, 25))
        self.lineurl.setMaximumSize(QSize(600, 25))
        self.lineurl.setFont(font)

        self.gridLayout.addWidget(self.lineurl, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(100, 30))
        self.pushButton.setMaximumSize(QSize(100, 30))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        brush4 = QBrush(QColor(0, 0, 127, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.pushButton.setPalette(palette2)

        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 3, 1, 1)

        self.linepath = QLineEdit(self.centralwidget)
        self.linepath.setObjectName(u"linepath")
        sizePolicy.setHeightForWidth(self.linepath.sizePolicy().hasHeightForWidth())
        self.linepath.setSizePolicy(sizePolicy)
        self.linepath.setMinimumSize(QSize(500, 25))
        self.linepath.setMaximumSize(QSize(600, 25))
        self.linepath.setFont(font1)

        self.gridLayout.addWidget(self.linepath, 3, 0, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)

        self.linetoken = QLineEdit(self.centralwidget)
        self.linetoken.setObjectName(u"linetoken")
        sizePolicy.setHeightForWidth(self.linetoken.sizePolicy().hasHeightForWidth())
        self.linetoken.setSizePolicy(sizePolicy)
        self.linetoken.setMinimumSize(QSize(500, 25))
        self.linetoken.setMaximumSize(QSize(600, 25))
        self.linetoken.setFont(font1)

        self.gridLayout.addWidget(self.linetoken, 1, 1, 1, 2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.label_2.setPalette(palette3)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setMaximumSize(QSize(4000, 4000))
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textEdit.setAutoFormatting(QTextEdit.AutoNone)

        self.gridLayout.addWidget(self.textEdit, 4, 0, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.linepath.raise_()
        self.lineurl.raise_()
        self.pushButton.raise_()
        self.linetoken.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.textEdit.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1070, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VaultSearch", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Vault Path", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Vault URL", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Read", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Token", None))

    # retranslateUi



