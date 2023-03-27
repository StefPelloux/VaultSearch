# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Search(object):
    def setupUi(self, Search):
        if not Search.objectName():
            Search.setObjectName(u"Search")
        Search.resize(302, 90)
        self.buttonBox = QDialogButtonBox(Search)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(210, 10, 81, 241))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.searchtext = QLineEdit(Search)
        self.searchtext.setObjectName(u"searchtext")
        self.searchtext.setGeometry(QRect(20, 30, 171, 31))

        self.retranslateUi(Search)
        self.buttonBox.accepted.connect(Search.accept)
        self.buttonBox.rejected.connect(Search.reject)

        QMetaObject.connectSlotsByName(Search)
    # setupUi

    def retranslateUi(self, Search):
        Search.setWindowTitle(QCoreApplication.translate("Search", u"Dialog", None))
    # retranslateUi





